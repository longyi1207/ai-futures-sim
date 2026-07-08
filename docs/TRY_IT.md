# Try it yourself — modify the sim in 10 minutes

This guide walks through **one change** to `config/events.yaml`, re-running calibration, and reading emergent outcome regions. No branch-mixture math — the engine draws **joint worlds**.

## Prerequisites

```bash
git clone https://github.com/longyi1207/ai-futures-sim.git
cd ai-futures-sim
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q   # sanity check
```

## What you're editing

| File | What it defines |
|------|-----------------|
| [`config/spine.yaml`](config/spine.yaml) | Capability milestones `sp_c1`…`sp_c9` (threshold + legibility) |
| [`config/events.yaml`](config/events.yaml) | **57 plot events** — windows, `p_cumulative`, preconditions, effects |
| [`config/variables.yaml`](config/variables.yaml) | Initial state variable values |
| [`config/terminals.yaml`](config/terminals.yaml) | Absorbing outcomes (doom / utopia / friction / severe) |
| [`config/society_hazard.yaml`](config/society_hazard.yaml) | Society vars → hazard multipliers |
| [`docs/VARIABLES.md`](docs/VARIABLES.md) | Human-readable variable glossary |
| [`docs/PROBABILITY_MODEL.md`](docs/PROBABILITY_MODEL.md) | `p_cumulative` ≠ daily P |

Every event should have a matching rationale in [`docs/evidence/<id>.md`](docs/evidence/).

## The event graph (DAG)

Nodes = spine milestones + plot events. Edges = `preconditions`, `requires_unlock`, `on_fire.unlock`, `modify_hazard`.

```bash
python scripts/export_dag.py
# → web/data/event_graph.json  (for viz)
# → docs/EVENT_GRAPH.mmd       (Mermaid preview)
```

Open `docs/EVENT_GRAPH.mmd` in any Mermaid viewer, or load the JSON in the [web explorer](web/).

## Example: "What if no-pause is less likely?"

`ev_no_pause_2028` is a load-bearing crux (federal pause attempt fails / never happens).

1. Read evidence: [`docs/evidence/ev_no_pause_2028.md`](docs/evidence/ev_no_pause_2028.md)
2. Edit YAML — e.g. lower `p_cumulative` from `0.88` to `0.75`:

```yaml
# config/events.yaml (excerpt)
- id: ev_no_pause_2028
  schedule:
    start: '2027-06-01'
    end: '2028-12-31'
    p_cumulative: 0.75   # was 0.88 — your judgment
```

3. Re-run calibration:

```bash
python scripts/calibration_check.py -n 600 --seed 42 \
  --output outputs/runs/calibration_summary.json
```

4. Read **emergent** `regions` in the JSON (doom / utopia / friction / severe). Compare to baseline. Do **not** tune terminals to hit a headline — only calibrate spine marginals and event P's you have evidence for.

5. Log the change in [`docs/CHANGELOG.md`](docs/CHANGELOG.md) with Claim | Why | Would update if.

## CLI quick run

```bash
futures-sim -n 200 --seed 1 --output outputs/runs/summary.json
```

## Web explorer (outcomes + paths)

```bash
python scripts/calibration_check.py -n 600 --seed 42 --output outputs/runs/calibration_summary.json
python scripts/path_frequency.py -n 600 --seed 42 --output outputs/runs/path_frequency.json
python scripts/export_sample_runs.py -n 800 --seed 42 --output web/data/sample_runs.json
python scripts/export_dag.py

cd web && python -m http.server 8787
# http://localhost:8787 — or https://longyi1207.github.io/ai-futures-sim/web/
```

The explorer shows:

- **Outcome regions** — emergent doom/utopia/friction/severe distribution
- **Spine course** — median milestone dates along the capability ladder
- **Path buckets** — how often alignment / paralysis / full-spine paths occur
- **Sample runs** — concrete timelines (spine + key events → terminal)

## Adding a new event

1. Add `docs/evidence/ev_my_event.md` (Claim | Why | Evidence | Would update if | Conf)
2. Add entry to `config/events.yaml` with `id`, `schedule`, `preconditions`, `on_fire`
3. `pytest -q` and `calibration_check.py`
4. Update [`docs/EVENTS_INDEX.md`](docs/EVENTS_INDEX.md)

## What *not* to do

- Don't paste annual P as `p_cumulative` without conversion ([`PROBABILITY_MODEL.md`](docs/PROBABILITY_MODEL.md))
- Don't multiply node marginals across the graph
- Don't tune `terminals.yaml` to force ~17% doom — regions should **emerge**

See [`docs/CALIBRATION.md`](docs/CALIBRATION.md) for spine targets vs emergent outcomes.
