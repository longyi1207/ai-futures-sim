#!/usr/bin/env python3
"""Export day-resolved story paths for archetypal runs (seed 42)."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import timedelta
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from futures_sim.config import load_config  # noqa: E402
from futures_sim.engine import SimEngine  # noqa: E402
from futures_sim.terminals import classify_region  # noqa: E402

KEY_VARS = [
    "governance_capacity",
    "deployment_pressure",
    "deception_risk",
    "bio_governance_tier",
    "bio_risk_pressure",
    "alignment_trust",
    "employment_stress",
    "human_autonomy_index",
    "distribution_regime",
    "inequality_index",
    "internal_capability",
    "ci_level",
    "gdp_index",
]

NOTABLE_MISSES = [
    "ev_c4_labor_shock",
    "ev_federal_pause_succeeds",
    "ev_bmia_pass",
    "ev_c10_internal_concern",
    "ev_whistle_memo",
    "ev_prod_interp_halt",
    "ev_us_paralysis_s2",
    "ev_deceptive_deploy_at_scale",
    "ev_state_revenue_measures",
    "ev_swf_enacted",
    "ev_reskilling_fails_absorb_c4",
    "ev_labor_ai_mobilization",
]


def compress_timeline(trace: list[dict], terminal_day: int, sample_every: int) -> list[dict]:
    rows: list[dict] = []
    for step in trace:
        day = step["day"]
        fires = (step.get("spine") or []) + (step.get("events") or [])
        if fires or day % sample_every == 0 or day == terminal_day:
            rows.append(
                {
                    "date": step["date"],
                    "day": day,
                    "spine": step.get("spine") or [],
                    "events": step.get("events") or [],
                    "vars": {k: round(float(step.get(k, 0)), 3) for k in KEY_VARS},
                }
            )
    return rows


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--through-run", type=int, default=30, help="replay runs 0..N")
    p.add_argument("--runs", type=int, nargs="+", default=[1, 10, 24])
    p.add_argument("--sample-every", type=int, default=90, help="days between var snapshots")
    p.add_argument("--output", type=Path, default=Path("web/data/story_paths_detail.json"))
    args = p.parse_args()

    config = load_config()
    config["sim"]["record_trace"] = True
    rng = np.random.default_rng(args.seed)
    engine = SimEngine(config, rng)
    targets = set(args.runs)

    out: dict[str, dict] = {}
    for i in range(args.through_run + 1):
        r = engine.run_once()
        if i not in targets:
            continue
        timeline = compress_timeline(r.trace or [], r.terminal_day, args.sample_every)
        fire_only = [t for t in timeline if t["spine"] or t["events"]]
        out[str(i)] = {
            "run_id": i,
            "seed": args.seed,
            "region": classify_region(r.terminal, config["terminals"]),
            "terminal": r.terminal,
            "terminal_day": r.terminal_day,
            "terminal_date": (engine.start + timedelta(days=r.terminal_day)).isoformat(),
            "fired_events": sorted(r.fired_events),
            "not_fired_notable": [e for e in NOTABLE_MISSES if e not in r.fired_events],
            "fired_spine": r.fired_spine,
            "spine_fire_days": r.spine_fire_days,
            "final_state": {
                k: round(float(v), 3)
                for k, v in r.final_state.items()
                if k in KEY_VARS or k in ("ai_rd_multiplier",)
            },
            "timeline": timeline,
            "fire_timeline": fire_only,
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {args.output} runs {sorted(out.keys())}")


if __name__ == "__main__":
    main()
