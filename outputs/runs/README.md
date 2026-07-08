# Run outputs

Generated JSON is gitignored except this README. Reproduce baseline:

```bash
python scripts/calibration_check.py -n 600 --seed 42 \
  --output outputs/runs/calibration_summary.json
python scripts/path_frequency.py -n 600 --seed 42 \
  --output outputs/runs/path_frequency.json
python scripts/seed_sweep.py -n 400 --seeds 42 123 456 \
  --output outputs/runs/seed_sweep.json
```

Load these in `web/` for the static explorer.
