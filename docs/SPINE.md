# Spine — probabilistic AI-2027 capability milestones

**Canonical config:** [`config/spine.yaml`](../config/spine.yaml)  
**Research reference:** [`docs/research/reference/03_ci_spine.md`](../research/reference/03_ci_spine.md)  
**Evidence:** [`docs/evidence/sp_c*.md`](evidence/)

## What spine is

## Model 2 (continuous threshold)

Spine milestones fire when `internal_capability` crosses `threshold` **and** pass a daily **legibility** draw (`observability.daily_hazard`). Latent capability can run ahead of public milestones. **`schedule.start`** = earliest plausible public confirmation; **`schedule.end`** = sim horizon.

Events can apply `capability_controls` (federal pause → growth↓, hard ceiling) and early `friction_*` terminals when governance stalls the ladder.

| | Spine (`sp_c*`) | Events (`ev_*`) |
|---|-----------------|-----------------|
| Source | AI 2027 **capability** ladder | World **plot** beats |
| Sets `ci_level` | Yes (`on_fire.set_vars`) | Rarely |
| Cross-validate | By-deadline + conditional \| parent | Crux / node marginals |

**Plot beats (events only):** C3 → `ev_china_cdz_mobilization`, C4 → `ev_c4_labor_shock`, C10 → `ev_c10_internal_concern` + whistle chain.

**Capability (spine only):** C1, C2, C5, C6, C7, C8, C9 — formerly duplicate events `ev_c5/c6/c8` removed.

## Chain

```
sp_c1 → sp_c2 → sp_c5 → sp_c6 → sp_c7 → sp_c8 → sp_c9
                                              ↓ unlock (sp_c9)
                                    ev_c10_internal_concern (requires sp_c9)
sp_c8 unlocks ev_meaning_pilot_success
```

## Calibration targets (AI-2027 modal deadlines)

| Milestone | Deadline | Unconditional target | Conditional \| parent |
|-----------|----------|----------------------|------------------------|
| sp_c1 | 2027-06-30 | 0.78 | — |
| sp_c2 | 2027-12-31 | 0.62 | 0.80 \| sp_c1 |
| sp_c5 | 2029-03-31 | 0.65 | 0.78 \| sp_c2 |
| sp_c6 | 2029-06-30 | 0.45 | 0.75 \| sp_c5 |
| sp_c7 | 2029-12-31 | 0.38 | 0.72 \| sp_c6 |
| sp_c8 | 2030-06-30 | 0.35 | 0.85 \| sp_c7 |
| sp_c9 | 2030-12-31 | 0.30 | 0.82 \| sp_c8 |

## Calibration status (v2.3)

Tune `base_daily_growth` + `calendar_rsi` anchors in `capability_dynamics.yaml` — spine has no `p_cumulative`.

**Known tension:** early milestones (c1/c2) vs mid-chain (c5/c6) — faster mid RSI lifts c5 but can overshoot c2; legibility hazards on c1/c2 help.

Run:

```bash
python scripts/calibration_check.py -n 2000 --seed 42
```

Reports: unconditional by-deadline, **P(child|parent)**, median fire dates, monotonicity, event marginals.

## Deprecated

`config/ci_schedule.yaml` — deterministic calendar removed in v2.0.
