#!/usr/bin/env python3
"""Calibration for Model 2: spine, events, outcomes, paths."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

# Allow `python scripts/calibration_check.py` without install
sys.path.insert(0, str(Path(__file__).resolve().parent))

from calibration_lib import (  # noqa: E402
    CAP_BY_DEADLINE,
    EVENT_TARGETS,
    OUTCOME_REGIONS,
    SPINE_CONDITIONALS,
    SPINE_DEADLINE,
    CalibrationReport,
    ok,
    run_calibration,
)


def print_report(report: CalibrationReport) -> None:
    n = report.runs
    print(f"Runs: {n}  seed={report.seed}  model=continuous_threshold_v1\n")

    print("CAPABILITY P(cap>=N by deadline):")
    prev_p = 1.0
    for level, (deadline, target, tol) in CAP_BY_DEADLINE.items():
        sim_p = report.cap_by_deadline[level]
        print(f"  >={level} by {deadline}: {sim_p:6.1%}  target {target:5.0%}  {ok(sim_p, target, tol)}")
    print(f"  monotonic spine: {'✓' if report.monotonic_spine else '✗'}")

    print("\nSPINE observables by deadline:")
    prev_p = 1.0
    for mid, level in SPINE_DEADLINE.items():
        deadline, target, tol = CAP_BY_DEADLINE[level]
        sim_p = report.spine_by_deadline[mid]
        mono_flag = "" if sim_p <= prev_p + 0.02 else " !mono"
        prev_p = sim_p
        print(
            f"  {mid} by {deadline}: {sim_p:6.1%}  target {target:5.0%}  {ok(sim_p, target, tol)}"
            f"  median {report.spine_median_day[mid] or '—'}  never {report.spine_never[mid]:5.1%}{mono_flag}"
        )

    print("\nSPINE conditional P(child | parent by child deadline):")
    for child, parent, level, target in SPINE_CONDITIONALS:
        deadline, _, tol = CAP_BY_DEADLINE[level]
        key = f"{child}|{parent}"
        den = report.spine_conditional_n.get(key, 0)
        if den == 0:
            print(f"  P({child}|{parent}) by {deadline}: n/a")
            continue
        sim_p = report.spine_conditional[key]
        print(f"  P({child}|{parent}) by {deadline}: {sim_p:6.1%}  (n={den})  target {target:5.0%}  {ok(sim_p, target, tol)}")

    print("\nEVENTS:")
    for eid, (target, tol, note) in EVENT_TARGETS.items():
        sim_p = report.events.get(eid, 0.0)
        print(f"  {eid}: {sim_p:6.1%}  target {target:5.0%}  {ok(sim_p, target, tol)}  {note}")

    print(f"\nOUTCOME REGIONS (emergent — not legacy 19/28/53 targets):")
    print(f"  early absorb: {report.early_absorb_rate:6.1%}  horizon assign: {report.horizon_absorb_rate:6.1%}")
    for reg in OUTCOME_REGIONS:
        sim_p = report.regions.get(reg, 0.0)
        print(f"  {reg}: {sim_p:6.1%}")

    print("\nOUTCOME conditionals:")
    for label, sim_p in sorted(report.outcome_conditional.items()):
        n_cond = report.outcome_conditional_n[label]
        print(f"  P({label}): {sim_p:6.1%}  (n={n_cond})")

    print("\nPATH buckets:")
    for name, p in sorted(report.path_buckets.items(), key=lambda x: -x[1]):
        print(f"  {name}: {p:6.1%}")

    print("\nTerminals (top):")
    for tid, p in sorted(report.terminals.items(), key=lambda x: -x[1])[:12]:
        print(f"  {tid}: {p:6.1%}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=2000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", type=Path, default=None, help="Write JSON summary for web explorer")
    args = p.parse_args()

    report, _ = run_calibration(args.n, args.seed)
    print_report(report)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        payload = asdict(report)
        args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"\nWrote {args.output}")


if __name__ == "__main__":
    main()
