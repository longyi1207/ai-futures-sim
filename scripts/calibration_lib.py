"""Shared calibration targets and run aggregation."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import timedelta
from typing import Any

import numpy as np

from futures_sim.ci import parse_date, sim_dates
from futures_sim.config import load_config
from futures_sim.engine import RunResult, SimEngine
from futures_sim.terminals import classify_region


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion — robust at small n / extreme p.

    Used instead of the point estimate alone: with n≈500-2000 MC runs, a region at
    ~2% has a relative CI width of ±1-2pp that a bare percentage hides (see CLAUDE.md
    meta-pitfall #5 — "report confidence intervals, not point estimates only").
    """
    if n <= 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (max(0.0, center - half), min(1.0, center + half))

# AI-2027 spine deadlines (c5 aligned to modal ~2029 Q1 per 03_ci_spine.md)
CAP_BY_DEADLINE: dict[int, tuple[str, float, float]] = {
    1: ("2027-06-30", 0.78, 0.10),
    2: ("2027-12-31", 0.62, 0.12),
    5: ("2029-03-31", 0.65, 0.12),
    6: ("2029-06-30", 0.45, 0.12),
    7: ("2029-12-31", 0.38, 0.12),
    8: ("2030-06-30", 0.35, 0.12),
    9: ("2030-12-31", 0.30, 0.10),
}

SPINE_DEADLINE = {f"sp_c{k}": k for k in CAP_BY_DEADLINE}

SPINE_CONDITIONALS: list[tuple[str, str, int, float]] = [
    ("sp_c5", "sp_c2", 5, 0.78),
    ("sp_c6", "sp_c5", 6, 0.75),
    ("sp_c7", "sp_c6", 7, 0.72),
    ("sp_c8", "sp_c7", 8, 0.85),
    ("sp_c9", "sp_c8", 9, 0.82),
]

EVENT_TARGETS: dict[str, tuple[float, float, str]] = {
    "ev_no_pause_2028": (0.88, 0.06, "CX-NO-PAUSE"),
    "ev_bmia_pass": (0.45, 0.10, "node2 BMIA"),
    "ev_us_paralysis_s2": (0.55, 0.12, "S2 modal"),
    "ev_china_cdz_mobilization": (0.65, 0.12, "C3 plot"),
}

# Outcome regions are EMERGENT from the joint sim — not calibrated to legacy headline
# partition (19/28/53 from pre-Model-2 wrong algorithm). See docs/CALIBRATION.md.

OUTCOME_REGIONS = ("doom", "severe", "friction", "utopia")

PATH_SIGNATURES: list[tuple[str, callable]] = []  # filled below


def _has_spine(r: RunResult, mid: str) -> bool:
    return mid in r.fired_spine


def _has_event(r: RunResult, eid: str) -> bool:
    return eid in r.fired_events


PATH_BUCKETS: list[tuple[str, Any]] = [
    ("c9_no_whistle", lambda r: _has_spine(r, "sp_c9") and "ev_c10_internal_concern" not in r.fired_events),
    ("paralysis_mid_ladder", lambda r: "ev_us_paralysis_s2" in r.fired_events and _has_spine(r, "sp_c5") and not _has_spine(r, "sp_c8")),
    ("pause_stall", lambda r: "ev_federal_pause_succeeds" in r.fired_events and not _has_spine(r, "sp_c9")),
    ("full_alignment_chain", lambda r: "ev_c10_internal_concern" in r.fired_events and any(e in r.fired_events for e in ("ev_whistle_memo", "ev_whistle_dump", "ev_deploy_incident"))),
    ("stops_before_c5", lambda r: _has_spine(r, "sp_c2") and not _has_spine(r, "sp_c5")),
    ("full_spine", lambda r: _has_spine(r, "sp_c9")),
]


@dataclass
class CalibrationReport:
    runs: int
    seed: int
    horizon_days: int
    cap_by_deadline: dict[int, float] = field(default_factory=dict)
    spine_by_deadline: dict[str, float] = field(default_factory=dict)
    spine_median_day: dict[str, str | None] = field(default_factory=dict)
    spine_never: dict[str, float] = field(default_factory=dict)
    spine_conditional: dict[str, float] = field(default_factory=dict)
    spine_conditional_n: dict[str, int] = field(default_factory=dict)
    events: dict[str, float] = field(default_factory=dict)
    events_ci: dict[str, tuple[float, float]] = field(default_factory=dict)
    regions: dict[str, float] = field(default_factory=dict)
    regions_ci: dict[str, tuple[float, float]] = field(default_factory=dict)
    terminals: dict[str, float] = field(default_factory=dict)
    early_absorb_rate: float = 0.0
    horizon_absorb_rate: float = 0.0
    outcome_conditional: dict[str, float] = field(default_factory=dict)
    outcome_conditional_n: dict[str, int] = field(default_factory=dict)
    path_buckets: dict[str, float] = field(default_factory=dict)
    monotonic_spine: bool = True


def deadline_day(sim_start, level: int) -> int:
    deadline, _, _ = CAP_BY_DEADLINE[level]
    return (parse_date(deadline) - sim_start).days


def run_calibration(
    n: int,
    seed: int,
    config: dict[str, Any] | None = None,
) -> tuple[CalibrationReport, list[RunResult]]:
    config = config or load_config()
    sim_start, _, horizon_days = sim_dates(config["sim"]["start_date"], config["sim"]["end_date"])
    eng = SimEngine(config=config, rng=np.random.default_rng(seed))
    results: list[RunResult] = [eng.run_once() for _ in range(n)]

    fired_events: Counter[str] = Counter()
    spine_by_deadline: Counter[str] = Counter()
    cap_by_deadline: dict[int, int] = {k: 0 for k in CAP_BY_DEADLINE}
    terminals: Counter[str] = Counter()
    regions: Counter[str] = Counter()
    spine_fire_days_all: list[dict[str, int]] = []
    median_days: dict[str, list[int]] = {mid: [] for mid in SPINE_DEADLINE}
    cond_num: Counter[str] = Counter()
    cond_den: Counter[str] = Counter()
    outcome_num: Counter[str] = Counter()
    outcome_den: Counter[str] = Counter()
    path_counts: Counter[str] = Counter()
    early = 0

    for r in results:
        spine_fire_days_all.append(dict(r.spine_fire_days))
        for eid in r.fired_events:
            fired_events[eid] += 1
        terminals[r.terminal] += 1
        regions[classify_region(r.terminal, config["terminals"])] += 1
        if r.absorbed_at_horizon:
            pass
        else:
            early += 1

        for level in CAP_BY_DEADLINE:
            dday = deadline_day(sim_start, level)
            mid = f"sp_c{level}"
            fd = r.spine_fire_days.get(mid)
            if fd is not None and fd <= dday:
                cap_by_deadline[level] += 1

        for mid, level in SPINE_DEADLINE.items():
            dday = deadline_day(sim_start, level)
            fd = r.spine_fire_days.get(mid)
            if fd is not None:
                median_days[mid].append(fd)
            if fd is not None and fd <= dday:
                spine_by_deadline[mid] += 1

        for child, parent, level, target in SPINE_CONDITIONALS:
            dday = deadline_day(sim_start, level)
            key = f"{child}|{parent}"
            if r.spine_fire_days.get(parent) is not None and r.spine_fire_days[parent] <= dday:
                cond_den[key] += 1
                if r.spine_fire_days.get(child) is not None and r.spine_fire_days[child] <= dday:
                    cond_num[key] += 1

        # outcome conditionals
        if _has_spine(r, "sp_c9"):
            outcome_den["doom|sp_c9"] += 1
            if classify_region(r.terminal, config["terminals"]) == "doom":
                outcome_num["doom|sp_c9"] += 1
        if _has_spine(r, "sp_c8"):
            outcome_den["utopia|sp_c8"] += 1
            if classify_region(r.terminal, config["terminals"]) == "utopia":
                outcome_num["utopia|sp_c8"] += 1
        if _has_event(r, "ev_c10_internal_concern"):
            outcome_den["doom|ev_c10"] += 1
            if classify_region(r.terminal, config["terminals"]) == "doom":
                outcome_num["doom|ev_c10"] += 1
            outcome_den["ev_whistle_memo|ev_c10"] += 1
            if _has_event(r, "ev_whistle_memo"):
                outcome_num["ev_whistle_memo|ev_c10"] += 1
        if _has_event(r, "ev_federal_pause_succeeds"):
            outcome_den["friction_pause_stall|pause"] += 1
            if r.terminal == "friction_pause_stall":
                outcome_num["friction_pause_stall|pause"] += 1
        if _has_event(r, "ev_us_paralysis_s2"):
            outcome_den["friction_governance_paralysis|paralysis"] += 1
            if r.terminal == "friction_governance_paralysis":
                outcome_num["friction_governance_paralysis|paralysis"] += 1

        for name, pred in PATH_BUCKETS:
            if pred(r):
                path_counts[name] += 1

    mono = True
    prev = 1.0
    for level in sorted(CAP_BY_DEADLINE):
        p = spine_by_deadline[f"sp_c{level}"] / n
        if p > prev + 0.02:
            mono = False
        prev = p

    report = CalibrationReport(
        runs=n,
        seed=seed,
        horizon_days=horizon_days,
        cap_by_deadline={k: cap_by_deadline[k] / n for k in CAP_BY_DEADLINE},
        spine_by_deadline={mid: spine_by_deadline[mid] / n for mid in SPINE_DEADLINE},
        spine_never={
            mid: 1.0 - sum(1 for sfd in spine_fire_days_all if mid in sfd) / n for mid in SPINE_DEADLINE
        },
        spine_median_day={
            mid: (
                (sim_start + timedelta(days=sorted(median_days[mid])[len(median_days[mid]) // 2])).isoformat()
                if median_days[mid]
                else None
            )
            for mid in SPINE_DEADLINE
        },
        spine_conditional={k: cond_num[k] / cond_den[k] for k in cond_den},
        spine_conditional_n=dict(cond_den),
        events={eid: fired_events[eid] / n for eid in EVENT_TARGETS},
        events_ci={eid: wilson_ci(fired_events[eid], n) for eid in EVENT_TARGETS},
        regions={k: regions[k] / n for k in OUTCOME_REGIONS},
        regions_ci={k: wilson_ci(regions[k], n) for k in OUTCOME_REGIONS},
        terminals={k: terminals[k] / n for k in terminals},
        early_absorb_rate=early / n,
        horizon_absorb_rate=(n - early) / n,
        outcome_conditional={k: outcome_num[k] / outcome_den[k] for k in outcome_den},
        outcome_conditional_n=dict(outcome_den),
        path_buckets={k: path_counts[k] / n for k, _ in PATH_BUCKETS},
        monotonic_spine=mono,
    )
    return report, results


def ok(sim: float, target: float, tol: float) -> str:
    return "✓" if abs(sim - target) <= tol else "✗"
