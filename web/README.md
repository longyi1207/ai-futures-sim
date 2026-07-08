# Web / interactive viz

Static explorer for calibration JSON — no build step.

## Quick start

```bash
# Generate data
python scripts/calibration_check.py -n 2000 --seed 42 \
  --output outputs/runs/calibration_summary.json
python scripts/path_frequency.py -n 2000 --seed 42 \
  --output outputs/runs/path_frequency.json

# Serve
cd web && python -m http.server 8787
```

Open http://localhost:8787 and load `outputs/runs/calibration_summary.json`.

## Planned (later)

1. Event graph from `config/events.yaml`
2. Sensitivity sliders → re-run via API
3. Sankey export

CLI batch runs:

```bash
futures-sim -n 10000 --output outputs/runs/summary.json
```
