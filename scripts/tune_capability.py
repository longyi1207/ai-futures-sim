#!/usr/bin/env python3
"""Score spine deadline calibration error (lower is better)."""

from __future__ import annotations

import argparse

import numpy as np

from futures_sim.ci import parse_date, sim_dates
from futures_sim.config import load_config
from futures_sim.engine import SimEngine

TARGETS: dict[str, tuple[str, float, float]] = {
    "sp_c1": ("2027-06-30", 0.78, 0.10),
    "sp_c2": ("2027-12-31", 0.62, 0.12),
    "sp_c5": ("2029-03-31", 0.65, 0.12),
    "sp_c6": ("2029-06-30", 0.45, 0.12),
    "sp_c7": ("2029-12-31", 0.38, 0.12),
    "sp_c8": ("2030-06-30", 0.35, 0.12),
    "sp_c9": ("2030-12-31", 0.30, 0.10),
}


def score_runs(n: int, seed: int) -> tuple[float, dict[str, float]]:
    config = load_config()
    sim_start, _, _ = sim_dates(config["sim"]["start_date"], config["sim"]["end_date"])
    eng = SimEngine(config=config, rng=np.random.default_rng(seed))
    hits: dict[str, int] = {mid: 0 for mid in TARGETS}

    for _ in range(n):
        r = eng.run_once()
        for mid, (deadline, _, _) in TARGETS.items():
            dday = (parse_date(deadline) - sim_start).days
            fd = r.spine_fire_days.get(mid)
            if fd is not None and fd <= dday:
                hits[mid] += 1

    sim_p = {mid: hits[mid] / n for mid in TARGETS}
    err = 0.0
    for mid, (_, target, tol) in TARGETS.items():
        diff = abs(sim_p[mid] - target)
        err += (diff / tol) ** 2
    return err, sim_p


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=400)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()
    err, sim_p = score_runs(args.n, args.seed)
    print(f"score={err:.3f}  runs={args.n}  seed={args.seed}")
    for mid, (_, target, tol) in TARGETS.items():
        ok = "✓" if abs(sim_p[mid] - target) <= tol else "✗"
        print(f"  {mid}: {sim_p[mid]:6.1%}  target {target:5.0%}  {ok}")


if __name__ == "__main__":
    main()
