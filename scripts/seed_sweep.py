#!/usr/bin/env python3
"""Multi-seed stability check for spine + outcome marginals."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from calibration_lib import CAP_BY_DEADLINE, OUTCOME_REGIONS, SPINE_DEADLINE, ok, run_calibration  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=1000, help="Runs per seed")
    p.add_argument("--seeds", type=int, nargs="+", default=[42, 123, 456, 789, 2026])
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    rows: list[dict] = []
    print(f"Seed sweep: {len(args.seeds)} seeds × {args.n} runs\n")

    for seed in args.seeds:
        report, _ = run_calibration(args.n, seed)
        row = {
            "seed": seed,
            "regions": report.regions,
            "sp_c5": report.spine_by_deadline.get("sp_c5", 0),
            "sp_c9": report.spine_by_deadline.get("sp_c9", 0),
            "monotonic": report.monotonic_spine,
            "early_absorb": report.early_absorb_rate,
        }
        rows.append(row)
        print(f"seed={seed}")
        for reg in OUTCOME_REGIONS:
            print(f"  {reg}: {report.regions.get(reg, 0):6.1%}")
        c5_deadline, c5_target, c5_tol = CAP_BY_DEADLINE[5]
        print(
            f"  sp_c5 by {c5_deadline}: {report.spine_by_deadline['sp_c5']:6.1%}  "
            f"target {c5_target:5.0%}  {ok(report.spine_by_deadline['sp_c5'], c5_target, c5_tol)}"
        )
        print(f"  monotonic: {'✓' if report.monotonic_spine else '✗'}  early_absorb: {report.early_absorb_rate:.1%}\n")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps({"seeds": rows}, indent=2), encoding="utf-8")
        print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
