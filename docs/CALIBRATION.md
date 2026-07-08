# Calibration

Scripts and targets for Model 2 spine + **emergent** outcome distribution.

## What we calibrate vs what we measure

| Calibrate (has targets) | Measure only (emergent) |
|-------------------------|-------------------------|
| Spine `P(by deadline)` | Outcome regions: doom / utopia / friction / severe |
| Spine conditionals `P(cN\|parent)` | Terminal mix, path buckets |
| Plot event marginals (`ev_no_pause_2028`, etc.) | `P(doom\|sp_c9)`, alignment chain rates |

**Important:** The headline partition **19% / 28% / 53%** in `notes/ai_futures_archive_2026-07/02_outcome_partition.md` came from a **pre–Model-2 algorithm** and is **not** a sim target. The joint Monte Carlo output (currently ~15–18% doom, ~12–15% utopia, ~64% friction at n=400×3 seeds) is the more honest forecast object.

Do **not** tune terminals to reproduce 19/28/53.

## Spine / event targets

Defined in `scripts/calibration_lib.py` — AI-2027 deadlines, conditional spine, crux event marginals.

**C5 deadline:** `2029-03-31` (modal ~2029 Q1 per `03_ci_spine.md`).

## Commands

```bash
python scripts/calibration_check.py -n 2000 --seed 42 \
  --output outputs/runs/calibration_summary.json

python scripts/path_frequency.py -n 2000 --seed 42 \
  --output outputs/runs/path_frequency.json

python scripts/seed_sweep.py -n 1000 --seeds 42 123 456 \
  --output outputs/runs/seed_sweep.json
```

## Web explorer

```bash
cd web && python -m http.server 8787
# Load outputs/runs/calibration_summary.json
```

## Horizon assignment

Runs reaching 2050 without an absorbing terminal are classified via `horizon_default` cascade in `config/terminals.yaml`. `horizon_only` terminals (e.g. `friction_modal`) are not checked mid-sim.
