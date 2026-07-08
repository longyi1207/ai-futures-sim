# Web explorer — simulation outcomes & paths

Interactive view of **Monte Carlo results**: emergent outcome regions, capability spine course, path buckets, terminal×spine flows, and sample world timelines.

No build step — static HTML + bundled demo JSON.

**Live:** https://longyi1207.github.io/ai-futures-sim/web/

## Quick start

```bash
# Generate fresh data (or use committed web/data/ demo)
python scripts/calibration_check.py -n 600 --seed 42 \
  --output web/data/calibration_summary.json
python scripts/path_frequency.py -n 600 --seed 42 \
  --output web/data/path_frequency.json
python scripts/export_sample_runs.py -n 800 --seed 42 \
  --output web/data/sample_runs.json
python scripts/export_dag.py   # → web/data/event_graph.json

cd web && python -m http.server 8787
# http://localhost:8787 — or use live Pages URL above
```

## What you see

| Panel | Source | Meaning |
|-------|--------|---------|
| **Outcome regions** | `calibration_summary.json` | Emergent doom/utopia/friction/severe — not hand-tuned |
| **Spine course** | median fire dates | How capability milestones land on the calendar |
| **Path buckets** | calibration | Named story paths (alignment chain, paralysis, …) |
| **Outcome × spine** | `path_frequency.json` | Which terminals follow which ladder depth |
| **Sample runs** | `sample_runs.json` | Concrete timelines: spine + key events → terminal |

## Event graph (DAG)

```bash
python scripts/export_dag.py
```

Produces `web/data/event_graph.json` and `docs/EVENT_GRAPH.mmd`. See [`docs/TRY_IT.md`](../docs/TRY_IT.md) for how to edit YAML and re-run.

## Planned

- Interactive DAG viewer (D3) from `event_graph.json`
- Sensitivity sliders → API re-run
