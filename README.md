# ai-futures-sim

Joint **Monte Carlo simulator** for AI-related futures (2026–2050): capability spine, plot events, society feedback → emergent outcome regions (doom / utopia / friction / severe).

Companion to the public forecast on [longyi.blog](https://longyi.blog/writing/my-ai-futures-forecast) and the on-site [evidence index](https://longyi.blog/writing/futures-evidence-index). Every event `p_cumulative` in `config/events.yaml` traces to a Claim / Why / Evidence page.

**Blog headline (emergent, not hand-tuned):** ~17% doom · ~13% utopia · ~65% friction · ~5% severe (3 seeds × 400 runs).

---

## Quick start

```bash
git clone https://github.com/longyi1207/ai-futures-sim.git
cd ai-futures-sim
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Smoke test (~15s)
pytest -q

# Calibration summary (~2 min at n=600)
python scripts/calibration_check.py -n 600 --seed 42 \
  --output outputs/runs/calibration_summary.json

python scripts/path_frequency.py -n 600 --seed 42 \
  --output outputs/runs/path_frequency.json

python scripts/seed_sweep.py -n 400 --seeds 42 123 456 \
  --output outputs/runs/seed_sweep.json
```

CLI entry point: `futures-sim -n 1000 --seed 42 --output outputs/runs/summary.json`

Requires **Python ≥ 3.11**.

---

## How one run works

```
capability_dynamics.yaml   latent internal_capability + RSI anchors
        ↓
spine.yaml                 threshold crossings sp_c1…sp_c9 (+ legibility)
        ↓
events.yaml                57 stochastic plot events (p_cumulative from evidence)
        ↓
society_hazard.yaml        employment_stress, governance, salience → hazard mods
        ↓
terminals.yaml             absorbing states + 2050 horizon cascade
        ↓
regions                    doom | utopia | friction | severe
```

Read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) first. Probability semantics: [`docs/PROBABILITY_MODEL.md`](docs/PROBABILITY_MODEL.md).

---

## Repo map

| Path | Purpose |
|------|---------|
| `config/` | All tunable YAML — spine, events, terminals, society hazards |
| `src/futures_sim/` | Engine, events, spine, terminals |
| `scripts/calibration_check.py` | Spine targets + emergent regions + JSON export |
| `scripts/path_frequency.py` | Spine prefixes, event signatures, terminal×spine |
| `scripts/seed_sweep.py` | Multi-seed stability |
| `docs/CALIBRATION.md` | What we calibrate vs what emerges |
| `docs/evidence/` | Per-event rationale (mirrors blog evidence) |
| `docs/research/` | Deep spine / node research (ported from private notes) |
| `web/` | Static JSON explorer (`python -m http.server` in `web/`) |
| `tests/` | pytest suite |

---

## Calibrating vs forecasting

| **Calibrate** (has targets) | **Emergent** (measure only) |
|-----------------------------|-----------------------------|
| Spine P(by deadline), P(cN\|parent) | Outcome regions |
| Plot event marginals (`ev_no_pause_2028`, …) | Terminal mix, path buckets |

Do **not** tune terminals to hit a pre-baked headline partition. See [`docs/CALIBRATION.md`](docs/CALIBRATION.md).

---

## `p_cumulative` semantics

In `events.yaml`, `schedule.p_cumulative` = P(event fires **at least once** in `[start, end]` while eligible). The engine converts to a constant daily hazard for remaining days in the window. Do not paste annual P directly as daily P.

---

## Performance (M-series Mac, Python 3.12)

| Runs | ~Time |
|------|-------|
| 100 | 15–20 s |
| 600 | ~3 min |
| 2,000 | ~10 min |
| 10,000 | ~60–85 min |

---

## Web explorer (outcomes & paths)

**Live:** https://longyi1207.github.io/ai-futures-sim/web/

Outcome donut, spine course timeline, path buckets, terminal×spine flows, and sample run timelines. Bundled demo data in `web/data/`.

```bash
# Local
cd web && python -m http.server 8787
```

Regenerate after config edits — see [`docs/TRY_IT.md`](docs/TRY_IT.md).

## Modify the model yourself

**Start here:** [`docs/TRY_IT.md`](docs/TRY_IT.md) — edit one `p_cumulative`, re-run calibration, read emergent regions.

| Doc | Contents |
|-----|----------|
| [`docs/VARIABLES.md`](docs/VARIABLES.md) | State variables glossary |
| [`docs/PROBABILITY_MODEL.md`](docs/PROBABILITY_MODEL.md) | `p_cumulative` semantics |
| [`docs/SPINE.md`](docs/SPINE.md) | Capability milestones |
| [`docs/EVENTS_INDEX.md`](docs/EVENTS_INDEX.md) | All 57 plot events |
| `python scripts/export_dag.py` | Event graph JSON + Mermaid |

---

## License

MIT — see [`LICENSE`](LICENSE).

## For contributors / agents

Read [`CLAUDE.md`](CLAUDE.md) before editing probabilities. Epistemic rule: every `p_cumulative` change needs Claim | Why | Would update if in `docs/evidence/`.
