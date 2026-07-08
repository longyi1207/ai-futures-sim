#!/usr/bin/env python3
"""Export representative sample runs for the web explorer (spine course + outcomes)."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from futures_sim.config import load_config  # noqa: E402
from futures_sim.engine import SimEngine  # noqa: E402
from futures_sim.terminals import classify_region  # noqa: E402
import numpy as np  # noqa: E402

KEY_EVENTS = [
    "ev_no_pause_2028",
    "ev_c4_labor_shock",
    "ev_china_cdz_mobilization",
    "ev_c10_internal_concern",
    "ev_whistle_memo",
    "ev_bmia_pass",
    "ev_us_paralysis_s2",
    "ev_beneficial_ai_treaty",
]


def day_to_date(start, day: int) -> str:
    return (start + timedelta(days=day)).isoformat()


def summarize_run(engine: SimEngine, result, run_id: int, terminals_doc: dict) -> dict:
    event_days: dict[str, int] = {}
    if result.trace:
        for step in result.trace:
            for eid in step.get("events") or []:
                if eid not in event_days:
                    event_days[eid] = step["day"]

    timeline: list[dict] = []
    for mid, day in sorted(result.spine_fire_days.items(), key=lambda x: x[1]):
        timeline.append({"day": day, "date": day_to_date(engine.start, day), "id": mid, "kind": "spine"})
    for eid in KEY_EVENTS:
        if eid in result.fired_events:
            day = event_days.get(eid)
            entry = {"id": eid, "kind": "event"}
            if day is not None:
                entry["day"] = day
                entry["date"] = day_to_date(engine.start, day)
            timeline.append(entry)
    timeline.sort(key=lambda x: x.get("day", 99999))

    return {
        "run_id": run_id,
        "terminal": result.terminal,
        "region": classify_region(result.terminal, terminals_doc),
        "terminal_day": result.terminal_day,
        "terminal_date": day_to_date(engine.start, result.terminal_day),
        "fired_spine": result.fired_spine,
        "key_events": [e for e in KEY_EVENTS if e in result.fired_events],
        "timeline": timeline,
        "final_state": {k: round(v, 3) if isinstance(v, float) else v for k, v in list(result.final_state.items())[:12]},
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=800, help="runs to sample from")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--per-region", type=int, default=2)
    p.add_argument("--output", type=Path, default=Path("web/data/sample_runs.json"))
    args = p.parse_args()

    config = load_config(Path(__file__).resolve().parents[1] / "config")
    config["sim"]["record_trace"] = True
    rng = np.random.default_rng(args.seed)
    engine = SimEngine(config, rng)

    by_region: dict[str, list] = defaultdict(list)
    for i in range(args.n):
        r = engine.run_once()
        region = classify_region(r.terminal, config["terminals"])
        if len(by_region[region]) < args.per_region:
            by_region[region].append(summarize_run(engine, r, i, config["terminals"]))

    payload = {
        "seed": args.seed,
        "sampled_from": args.n,
        "runs": [run for runs in by_region.values() for run in runs],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {args.output} ({len(payload['runs'])} sample runs)")


if __name__ == "__main__":
    main()
