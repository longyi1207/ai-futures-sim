# Correlation model

## Problem

Independent daily hazards **overstate joint tails**. Research (`docs/research/spine/correlation_matrix.md`) documents clusters where P's move together — e.g. whistleblower + no halt + theft + preemption should be treated as **~3–5×** the product of marginal tail probs, not independent.

## Design: latent cluster shocks

Each run samples **per-cluster latent variables** `z_c ~ N(0,1)` that evolve daily via AR(1):

```
z_{t+1} = φ · z_t + √(1 − φ²) · ε,   φ = 0.98
```

For event `e` in cluster(s) `C(e)`:

```
h_adj(e) = h_base(e) · exp( Σ_{c ∈ C(e)} β_c · z_c )
```

- `h_base` — from `p_cumulative` conversion + `modify_hazard` multipliers (unchanged)
- `β_c` — `hazard_sensitivity` per cluster (0.15–0.22), from `config/correlations.yaml`
- `ρ` in YAML — documents target intra-cluster correlation from research (not used directly in AR(1); sensitivity tuned to match joint-tail guidance)

When `z_c` is high (+1.5σ…+2σ), all events in cluster `c` see elevated hazard **on the same day** → correlated fires.

## Clusters (config → research)

| Cluster | Research source | ρ | Example events |
|---------|-----------------|---|----------------|
| `race` | Cluster A — acceleration | 0.55 | `ev_no_pause_2028`, `ev_race_acceleration`, `ev_gaia_preemption` |
| `bio_governance` | Cluster B — bio mitigation | 0.50 | `ev_bmia_pass`, `ev_multilateral_screening_pilot` |
| `bio_tail` | Cluster C — bio tail | 0.52 | `ev_tier3_path_open`, `ev_bio_nearmiss_hidden` |
| `alignment_governance` | Cluster D — transparency glue | 0.45 | `ev_whistle_memo`, `ev_labor_hearings_peak` |
| `compute_chokepoint` | Cluster E — Node 7 chokepoint | 0.48 | `ev_compute_triopoly_lock`, `ev_singleton_lab_dominance` |
| `governance_hollowing` | Cluster F + H (N10–N11) | 0.50 | `ev_us_paralysis_s2`, `ev_corp_safety_hollowing` |
| `sovereignty` | Node 7 T7-C + Node 9 Gulf | 0.42 | `ev_india_sovereign_ai_stack`, `ev_gulf_compute_sovereignty` |

Events may appear in **multiple** clusters; sensitivities **sum in log space**.

## Config & toggles

- `config/correlations.yaml` — cluster membership, ρ, sensitivities
- `config/sim.yaml` — `use_correlations: true` (default on)
- Implementation: `src/futures_sim/correlations.py`, wired in `engine._sample_events()`

## What this does NOT do

- Does not replace scenario-branch weights in `my_pdoom.md` stitching
- Does not correlate events across mutex groups (mutex still hard-blocks)
- Does not sample `p_cumulative` uncertainty (planned in `PROBABILITY_MODEL.md`)

## References

- `docs/research/spine/correlation_matrix.md` — master table + Clusters A–H
- `docs/PROBABILITY_MODEL.md` — hazard conversion + correlation section
