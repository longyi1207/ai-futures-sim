#!/usr/bin/env python3
"""Monte Carlo path frequency report — top signatures and branch rates."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from calibration_lib import PATH_BUCKETS, run_calibration  # noqa: E402

KEY_EVENTS = [
    "ev_no_pause_2028",
    "ev_federal_pause_succeeds",
    "ev_us_paralysis_s2",
    "ev_c4_labor_shock",
    "ev_c10_internal_concern",
    "ev_whistle_memo",
    "ev_prod_interp_halt",
    "ev_deceptive_deploy_at_scale",
    "ev_extinction_misalign_catastrophe",
    "ev_beneficial_ai_treaty",
    "ev_meaning_pilot_success",
]

SPINE_PREFIX = ["sp_c1", "sp_c2", "sp_c5", "sp_c6", "sp_c7", "sp_c8", "sp_c9"]


def spine_prefix(fired_spine: list[str]) -> str:
    parts = []
    for mid in SPINE_PREFIX:
        if mid in fired_spine:
            parts.append(mid.replace("sp_", ""))
        else:
            break
    return "→".join(parts) if parts else "none"


def event_signature(fired_events: list[str]) -> str:
    return "+".join(e for e in KEY_EVENTS if e in fired_events) or "(no key events)"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=2000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    report, results = run_calibration(args.n, args.seed)

    spine_paths: Counter[str] = Counter()
    event_paths: Counter[str] = Counter()
    terminal_by_spine: Counter[tuple[str, str]] = Counter()

    for r in results:
        sp = spine_prefix(r.fired_spine)
        spine_paths[sp] += 1
        event_paths[event_signature(r.fired_events)] += 1
        terminal_by_spine[(sp, r.terminal)] += 1

    print(f"Path frequency report  n={args.n}  seed={args.seed}\n")

    print("Spine prefix reached:")
    for path, c in spine_paths.most_common(12):
        print(f"  {path:40s} {c/args.n:6.1%}")

    print("\nPath buckets (from calibration_lib):")
    for name, prob in sorted(report.path_buckets.items(), key=lambda x: -x[1]):
        print(f"  {name:30s} {prob:6.1%}")

    print("\nTop event signatures (key events only):")
    for sig, c in event_paths.most_common(15):
        print(f"  {sig[:70]:70s} {c/args.n:6.1%}")

    print("\nTerminal given spine prefix (top combos):")
    for (sp, term), c in terminal_by_spine.most_common(15):
        print(f"  {sp:25s} → {term:35s} {c/args.n:6.1%}")

    if args.output:
        payload = {
            "runs": args.n,
            "seed": args.seed,
            "spine_paths": {k: v / args.n for k, v in spine_paths.items()},
            "event_paths": {k: v / args.n for k, v in event_paths.most_common(30)},
            "path_buckets": report.path_buckets,
            "terminal_by_spine": {f"{a}|{b}": c / args.n for (a, b), c in terminal_by_spine.most_common(40)},
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"\nWrote {args.output}")


if __name__ == "__main__":
    main()
