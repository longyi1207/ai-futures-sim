#!/usr/bin/env python3
"""P(region | event X) and lift vs baseline from joint MC runs."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from calibration_lib import run_calibration  # noqa: E402
from futures_sim.config import load_config  # noqa: E402
from futures_sim.terminals import classify_region  # noqa: E402

REGIONS = ("doom", "utopia", "friction", "severe")

# Load-bearing + high-salience events (subset of 57)
TRACKED_EVENTS = [
    "ev_no_pause_2028",
    "ev_federal_pause_succeeds",
    "ev_federal_pause_attempt_fails",
    "ev_us_paralysis_s2",
    "ev_bmia_pass",
    "ev_bmia_enforcement_weak",
    "ev_c10_internal_concern",
    "ev_whistle_memo",
    "ev_whistle_dump",
    "ev_prod_interp_halt",
    "ev_deceptive_deploy_at_scale",
    "ev_extinction_misalign_catastrophe",
    "ev_extinction_bio_release",
    "ev_bio_tier2_live",
    "ev_bio_nearmiss_hidden",
    "ev_tier3_path_open",
    "ev_weight_theft",
    "ev_race_acceleration",
    "ev_corp_safety_hollowing",
    "ev_beneficial_ai_treaty",
    "ev_meaning_pilot_success",
    "ev_c4_labor_shock",
    "ev_china_cdz_mobilization",
    "ev_cyber_cascade",
    "ev_gaia_preemption",
    "ev_eu_gpai_binds",
    "ev_no_shutdown_asi_threshold",
    "ev_rsi_cloud_dominant",
]


def region_dist(items, indices) -> dict[str, float]:
    if not indices:
        return {r: 0.0 for r in REGIONS}
    c: Counter[str] = Counter()
    for i in indices:
        c[items[i].region] += 1
    n = len(indices)
    return {r: c[r] / n for r in REGIONS}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=1200)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--min-n", type=int, default=25, help="min runs with event to report")
    p.add_argument("--output", type=Path, default=Path("web/data/event_impact.json"))
    args = p.parse_args()

    config = load_config()
    terminals_doc = config["terminals"]
    report, results = run_calibration(args.n, args.seed)

    wrapped = []
    for r in results:
        w = type("RunWrap", (), {})()
        w.raw = r
        w.region = classify_region(r.terminal, terminals_doc)
        wrapped.append(w)

    baseline = report.regions
    n = len(wrapped)

    rows = []
    all_fired = set()
    for r in wrapped:
        all_fired.update(r.raw.fired_events)

    events = sorted(set(TRACKED_EVENTS) | all_fired)

    for eid in events:
        with_idx = [i for i, r in enumerate(wrapped) if eid in r.raw.fired_events]
        without_idx = [i for i, r in enumerate(wrapped) if eid not in r.raw.fired_events]
        n_with = len(with_idx)
        n_without = len(without_idx)
        if n_with < args.min_n or n_without < args.min_n:
            continue

        p_event = n_with / n
        given = region_dist(wrapped, with_idx)
        not_given = region_dist(wrapped, without_idx)

        row = {
            "event": eid,
            "p_fire": round(p_event, 4),
            "n_with": n_with,
            "n_without": n_without,
            "p_region_given": {k: round(given[k], 4) for k in REGIONS},
            "p_region_not_given": {k: round(not_given[k], 4) for k in REGIONS},
            "lift": {
                k: round(given[k] - not_given[k], 4) for k in REGIONS
            },
            "lift_vs_baseline": {
                k: round(given[k] - baseline[k], 4) for k in REGIONS
            },
        }
        # impact score: max absolute lift on doom or utopia
        row["impact_score"] = round(
            max(abs(row["lift"]["doom"]), abs(row["lift"]["utopia"]), abs(row["lift"]["severe"])),
            4,
        )
        rows.append(row)

    rows.sort(key=lambda x: (-x["impact_score"], -x["p_fire"]))

    payload = {
        "meta": {
            "runs": n,
            "seed": args.seed,
            "baseline_regions": {k: round(baseline[k], 4) for k in REGIONS},
            "note": "lift = P(region|event) - P(region|not event); causal not guaranteed",
        },
        "top_doom_lift": sorted(rows, key=lambda x: -x["lift"]["doom"])[:10],
        "top_utopia_lift": sorted(rows, key=lambda x: -x["lift"]["utopia"])[:10],
        "events": rows,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {args.output} ({len(rows)} events with n>={args.min_n})")
    print("\nTop doom lift (P(doom|X) - P(doom|¬X)):")
    for row in payload["top_doom_lift"][:6]:
        d = row["lift"]["doom"]
        print(f"  {row['event']:40s} +{d:.1%}" if d >= 0 else f"  {row['event']:40s} {d:.1%}")
    print("\nTop utopia lift:")
    for row in payload["top_utopia_lift"][:6]:
        u = row["lift"]["utopia"]
        print(f"  {row['event']:40s} +{u:.1%}" if u >= 0 else f"  {row['event']:40s} {u:.1%}")


if __name__ == "__main__":
    main()
