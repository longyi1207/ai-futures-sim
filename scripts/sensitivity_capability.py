#!/usr/bin/env python3
"""One-at-a-time sensitivity sweep over capability_dynamics.yaml growth parameters.

Motivation: `capability.py::_growth_factor` composes ~22 independent multiplicative
scale/exponent constants, but `calibration_lib.py` only exposes ~12 calibration
targets (7 cap_by_deadline marginals + 5 spine conditionals). That is an
under-identified system — many different parameter settings can hit the same
milestone-deadline targets while differing arbitrarily elsewhere. This script
does not fix that (it would require re-deriving the model with fewer degrees of
freedom, a design decision for the owner), but it tells you which of the 22
knobs the *current* calibration targets are actually sensitive to, so you know
which numbers are load-bearing and which are decorative.

Method: for each parameter, perturb ±25% from its config/capability_dynamics.yaml
value, holding everything else (including the RNG seed) fixed — common random
numbers — and re-run calibration at moderate n. probability_uncertainty is forced
off so parameter sensitivity isn't confounded with elicitation noise. Reports the
resulting shift in sp_c5/sp_c9 by-deadline and doom/utopia region share.
"""

from __future__ import annotations

import argparse
import copy
import json
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from calibration_lib import run_calibration  # noqa: E402
from futures_sim.config import load_config  # noqa: E402

# (label, path-in-capability_dynamics-dict) — path is a tuple of keys to walk/set
PARAMS: list[tuple[str, tuple[str, ...]]] = [
    ("base_daily_growth", ("base_daily_growth",)),
    ("multiplier_exponent", ("multiplier_exponent",)),
    ("carrying_capacity", ("carrying_capacity",)),
    ("input.frontier_capex_index.scale", ("inputs", "frontier_capex_index", "scale")),
    ("input.deployment_pressure.scale", ("inputs", "deployment_pressure", "scale")),
    ("input.china_frontier_parity.scale", ("inputs", "china_frontier_parity", "scale")),
    ("input.us_china_race_index.scale", ("inputs", "us_china_race_index", "scale")),
    ("input.compute_concentration.scale", ("inputs", "compute_concentration", "scale")),
    ("input.eu_regulatory_bind.scale", ("inputs", "eu_regulatory_bind", "scale")),
    ("input.open_weights_regime.scale", ("inputs", "open_weights_regime", "scale")),
    ("input.frontier_lab_polarization.scale", ("inputs", "frontier_lab_polarization", "scale")),
    ("gdp_funding.scale", ("gdp_funding", "scale")),
    ("race_amplification.scale", ("race_amplification", "scale")),
    ("governance_brake.governance_scale", ("governance_brake", "governance_scale")),
    ("governance_brake.salience_scale", ("governance_brake", "salience_scale")),
    ("trust_governance_brake.scale", ("trust_governance_brake", "scale")),
    ("secret_race_boost.scale", ("secret_race_boost", "scale")),
    ("coordination_brake.scale", ("coordination_brake", "scale")),
    ("sovereignty_fragmentation.scale", ("sovereignty_fragmentation", "scale")),
    ("admin_ai_posture.growth_scale", ("admin_ai_posture", "growth_scale")),
    ("kinetic_escalation.growth_penalty", ("kinetic_escalation", "growth_penalty")),
    ("bio_spillover.bio_to_cap_scale", ("bio_spillover", "bio_to_cap_scale")),
]


def _get(d: dict, path: tuple[str, ...]) -> float:
    cur = d
    for k in path[:-1]:
        cur = cur[k]
    return float(cur[path[-1]])


def _set(d: dict, path: tuple[str, ...], value: float) -> None:
    cur = d
    for k in path[:-1]:
        cur = cur[k]
    cur[path[-1]] = value


def summary_metrics(config: dict, n: int, seed: int) -> dict[str, float]:
    report, _ = run_calibration(n, seed, config=config)
    return {
        "sp_c5_by_deadline": report.spine_by_deadline.get("sp_c5", 0.0),
        "sp_c9_by_deadline": report.spine_by_deadline.get("sp_c9", 0.0),
        "doom": report.regions.get("doom", 0.0),
        "utopia": report.regions.get("utopia", 0.0),
        "friction": report.regions.get("friction", 0.0),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=150)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--pct", type=float, default=0.25, help="fractional perturbation, e.g. 0.25 = ±25%%")
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    base_config = load_config()
    base_config["sim"] = copy.deepcopy(base_config["sim"])
    base_config["sim"].setdefault("probability_uncertainty", {})["enabled"] = False

    t0 = time.monotonic()

    def log(msg: str) -> None:
        print(f"[{time.monotonic() - t0:6.1f}s] {msg}", flush=True)

    def write_partial(baseline: dict, rows: list[dict]) -> None:
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(
                json.dumps({"baseline": baseline, "params": rows, "complete": len(rows) == len(PARAMS)}, indent=2),
                encoding="utf-8",
            )

    log(f"Baseline (n={args.n}, seed={args.seed}, probability_uncertainty off)")
    baseline = summary_metrics(copy.deepcopy(base_config), args.n, args.seed)
    for k, v in baseline.items():
        log(f"  baseline {k}: {v:.1%}")
    write_partial(baseline, [])

    rows = []
    log(f"Sweeping {len(PARAMS)} parameters x2 directions ({2 * len(PARAMS) + 1} total sim batches of n={args.n})")
    print(f"\n{'parameter':38s} {'base_val':>10s} {'lo_val':>10s} {'hi_val':>10s}  "
          f"{'Δsp_c5':>8s} {'Δsp_c9':>8s} {'Δdoom':>8s} {'Δutopia':>8s}  |elasticity|", flush=True)
    for i, (label, path) in enumerate(PARAMS):
        log(f"[{i + 1}/{len(PARAMS)}] {label} — running lo/hi pair...")
        cfg_dyn = base_config["capability_dynamics"]
        base_val = _get(cfg_dyn, path)
        lo_val = base_val * (1 - args.pct)
        hi_val = base_val * (1 + args.pct)

        cfg_lo = copy.deepcopy(base_config)
        _set(cfg_lo["capability_dynamics"], path, lo_val)
        m_lo = summary_metrics(cfg_lo, args.n, args.seed)

        cfg_hi = copy.deepcopy(base_config)
        _set(cfg_hi["capability_dynamics"], path, hi_val)
        m_hi = summary_metrics(cfg_hi, args.n, args.seed)

        d_c5 = m_hi["sp_c5_by_deadline"] - m_lo["sp_c5_by_deadline"]
        d_c9 = m_hi["sp_c9_by_deadline"] - m_lo["sp_c9_by_deadline"]
        d_doom = m_hi["doom"] - m_lo["doom"]
        d_utopia = m_hi["utopia"] - m_lo["utopia"]
        score = abs(d_c5) + abs(d_c9) + abs(d_doom) + abs(d_utopia)

        rows.append(
            {
                "parameter": label,
                "base_val": base_val,
                "lo_val": lo_val,
                "hi_val": hi_val,
                "lo": m_lo,
                "hi": m_hi,
                "delta_sp_c5": d_c5,
                "delta_sp_c9": d_c9,
                "delta_doom": d_doom,
                "delta_utopia": d_utopia,
                "sensitivity_score": score,
            }
        )
        print(
            f"{label:38s} {base_val:10.4f} {lo_val:10.4f} {hi_val:10.4f}  "
            f"{d_c5:+7.1%} {d_c9:+7.1%} {d_doom:+7.1%} {d_utopia:+7.1%}  {score:6.1%}",
            flush=True,
        )
        write_partial(baseline, rows)
        log(f"[{i + 1}/{len(PARAMS)}] done, score={score:.1%} — partial results written")

    rows.sort(key=lambda r: -r["sensitivity_score"])
    print("\nRanked by sensitivity_score (sum of |Δ| across sp_c5/sp_c9/doom/utopia):")
    for r in rows:
        print(f"  {r['parameter']:38s} {r['sensitivity_score']:6.1%}")

    write_partial(baseline, rows)
    log(f"Wrote final results to {args.output}")


if __name__ == "__main__":
    main()
