"""CLI entrypoint."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import numpy as np
from tqdm import tqdm

from .config import load_config
from .engine import SimEngine, run_monte_carlo
from .terminals import classify_region


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Futures Monte Carlo simulator")
    parser.add_argument("-n", "--runs", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None, help="JSON summary path")
    args = parser.parse_args()

    config = load_config(args.config)

    if args.runs > 50:
        eng = SimEngine(config=config, rng=np.random.default_rng(args.seed))
        results = [eng.run_once() for _ in tqdm(range(args.runs), desc="sim runs")]
    else:
        results = run_monte_carlo(config, n_runs=args.runs, seed=args.seed)

    terminal_counts = Counter(r.terminal for r in results)
    region_counts: Counter[str] = Counter()
    for tid, c in terminal_counts.items():
        region = classify_region(tid, config["terminals"])
        region_counts[region] += c

    n = len(results)
    summary = {
        "runs": n,
        "seed": args.seed,
        "horizon_days": (None),  # filled below
        "by_terminal": {k: {"count": v, "p": v / n} for k, v in terminal_counts.most_common()},
        "by_region": {k: {"count": v, "p": v / n} for k, v in region_counts.most_common()},
        "median_fired_events": sorted(len(r.fired_events) for r in results)[n // 2],
        "median_fired_spine": sorted(len(r.fired_spine) for r in results)[n // 2],
        "median_terminal_day": sorted(r.terminal_day for r in results)[n // 2],
    }
    from .ci import sim_dates

    _, _, days = sim_dates(config["sim"]["start_date"], config["sim"]["end_date"])
    summary["horizon_days"] = days

    print(json.dumps(summary, indent=2))

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
