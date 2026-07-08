#!/usr/bin/env python3
"""Read-only path diagnostics for spine chain + alignment unlock chain."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, timedelta

from futures_sim.ci import parse_date, sim_dates
from futures_sim.config import load_config
from futures_sim.spine import SpineCatalog
from futures_sim.state import WorldState

SPINE_CHAIN = ["sp_c1", "sp_c2", "sp_c5", "sp_c6", "sp_c7", "sp_c8", "sp_c9"]

ALIGNMENT_CHAIN = [
    "sp_c8",
    "sp_c9",
    "ev_c10_internal_concern",
    "ev_whistle_memo",
    "ev_whistle_dump",
    "ev_deploy_incident",
    "ev_concern_no_leak",
]


@dataclass
class SpineReport:
    milestone_id: str
    window_days: int
    eligible_days: int
    block_reason: str
    p_cumulative: float
    max_p_if_eligible: float


def _dates_in_window(start: date, end: date) -> list[date]:
    out: list[date] = []
    d = start
    while d <= end:
        out.append(d)
        d += timedelta(days=1)
    return out


def _max_p_if_eligible(p_cum: float, eligible_days: int) -> float:
    if eligible_days <= 0:
        return 0.0
    from futures_sim.events import cumulative_to_daily_hazard

    h = cumulative_to_daily_hazard(p_cum, eligible_days)
    survive = 1.0
    for _ in range(eligible_days):
        survive *= 1 - h
    return 1 - survive


def spine_report(spine: SpineCatalog, state: WorldState, mid: str) -> SpineReport:
    ms = spine.milestones[mid]
    start, end = spine._parsed[mid]
    dates = _dates_in_window(start, end)
    eligible = sum(1 for d in dates if spine.is_eligible(mid, state, d))
    p_cum = float(ms.get("schedule", {}).get("p_cumulative", 0))
    block = "ok" if eligible > 0 else "preconditions never met in window"
    pre = ms.get("preconditions", {})
    if pre.get("spine_fired"):
        missing = [s for s in pre["spine_fired"] if s not in state.fired_spine]
        if missing:
            block = f"needs spine_fired {missing}"
    return SpineReport(
        milestone_id=mid,
        window_days=len(dates),
        eligible_days=eligible,
        block_reason=block,
        p_cumulative=p_cum,
        max_p_if_eligible=_max_p_if_eligible(p_cum, eligible),
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--best-case", action="store_true", help="Assume all prior spine milestones fired")
    args = p.parse_args()

    config = load_config()
    spine = SpineCatalog(config["spine"])
    sim_start, _, _ = sim_dates(config["sim"]["start_date"], config["sim"]["end_date"])

    state = WorldState()
    state.set_var("ci_level", 0.5)
    if args.best_case:
        for mid in SPINE_CHAIN:
            spine.fire(mid, state)

    print("=" * 72)
    print("Spine chain (AI-2027 capability milestones)")
    print("=" * 72)
    for mid in SPINE_CHAIN:
        rep = spine_report(spine, state, mid)
        status = "OK" if rep.eligible_days > 0 else "BLOCKED"
        print(f"\n{mid} {status}")
        print(f"  window days          : {rep.window_days}")
        print(f"  eligible days        : {rep.eligible_days}")
        print(f"  p_cumulative         : {rep.p_cumulative}")
        print(f"  max P(fire) eligible : {rep.max_p_if_eligible:.1%}")
        if rep.eligible_days == 0:
            print(f"  >> {rep.block_reason}")

    print("\n" + "=" * 72)
    print("Alignment chain (spine → C10 plot → whistle variants)")
    print("=" * 72)
    from futures_sim.events import EventCatalog

    catalog = EventCatalog(config["events"], society_hazards=config.get("society_hazards"))
    for eid in ALIGNMENT_CHAIN[2:]:
        ev = catalog.events[eid]
        start, end = catalog._parsed[eid]
        dates = _dates_in_window(start, end)
        eligible = sum(1 for d in dates if catalog.is_eligible(eid, state, d))
        p_cum = float(ev.get("schedule", {}).get("p_cumulative", 0))
        print(f"\n{eid}: eligible {eligible}/{len(dates)} days, p_cum={p_cum}")


if __name__ == "__main__":
    main()
