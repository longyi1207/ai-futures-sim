# CLAUDE.md — Agent instructions for AI Futures Sim

> **Audience:** Cursor, Claude, Codex, or any agent working in this repository.  
> **Owner priority:** intellectual honesty, epistemic diligence, reproducibility. This project will be **open-sourced**.

---

## What this project is

**AI Futures Sim** is a Monte Carlo simulator of AI-related civilizational outcomes (~2026–2050).

- **Not** a narrative fanfic generator.
- **Not** a branch-mixture model (retired approach — see `docs/research/reference/03_ci_spine.md` for Ci definitions).
- **Is** a falsifiable event graph: discrete events with observables, conditional probabilities, effects on state variables, and absorbing terminals (doom / utopia / friction).

Each run produces one **complete joint timeline** — bio, misalignment, and governance dynamics **co-occur**, as in the real world.

---

## Behavioral expectations (non-negotiable)

### 1. Epistemic integrity

- **Never** invent probabilities without labeling them `[GUESS]`, `[PLACEHOLDER]`, or `[CALIBRATE]`.
- **Never** present scaffold numbers as calibrated forecasts in user-facing copy.
- Every material `p_cumulative` or `daily_hazard` must trace to:
  - a `research_ref` in `config/events.yaml`, or
  - a new `docs/evidence/<event_id>.md` with **Claim | Why | Evidence | Would update if | Conf**.
- Distinguish clearly: **established fact** · **recent finding** · **author judgment** · **speculation**.
- If evidence is weak, **widen ranges** and document sensitivity — do not fake precision.

### 2. Diligence before edits

Before changing any event probability or effect:

1. Read `docs/PROBABILITY_MODEL.md` — understand daily hazard conversion.
2. Read the linked evidence file (`docs/evidence/`) and deep rationale (`docs/research/`).
3. Check downstream effects (unlock/lock chains) for unintended consequences.
4. Run `pytest` and a small sim (`futures-sim -n 200`) and note if headline regions moved >3pp.
5. Log the change in `docs/CHANGELOG.md` (create entry if missing).

### 3. Do not break reproducibility

- Config is canonical — logic reads YAML, not hardcoded story beats.
- Keep `seed` support; document default seed in README.
- Do not commit `.venv/`, credentials, or machine-specific paths.

### 4. Clean code (open-source bar)

- Match existing style: type hints, small modules, no over-abstraction.
- Tests for hazard math and engine invariants.
- User-facing docs updated when schema changes.
- Prefer explicit YAML over magic constants in Python.

### 5. Budget & external resources

**Project budget: $200 USD total** (owner-approved, 2026-07-07). Applies to `ai_futures_sim` and direct supporting work (LLM API, cloud compute, paid data).

**You may use LLM APIs and cloud when justified** — e.g. batch-calibrating 50 events from evidence files, parallel sensitivity runs, embedding news for observable matching. **Do not use** paid resources for work a local agent loop can do cheaply (YAML edits, pytest, single-machine 10k sims).

**Before any single spend > $20:** note the estimate in `docs/BUDGET.md` and proceed only if the task clearly needs it (owner has pre-approved the $200 cap for the project; still avoid surprise large charges).

**Always:**
- Log every incurred cost in [`docs/BUDGET.md`](docs/BUDGET.md) — date, vendor, purpose, amount, running total.
- Prefer **local sim** (M4, `.venv`) over cloud for Monte Carlo unless runs need >100k or GPU.
- Use **LLM Vault** for API keys (`vault get KEY_NAME` inline); never commit secrets.
- After paid LLM batches, record **model, approximate tokens, $ estimate** in the budget log.
- If cumulative spend exceeds **$150**, flag the owner in your response before more paid work.

**Good uses of budget:** evidence synthesis per event (`docs/evidence/`), automated calibration checks, web viz hosting, large parameter ensembles on cloud.

**Poor uses:** replacing careful human judgment on cruxes; generating probabilities without `research_ref`; cloud for 10k-run sims that finish in 30 min locally.

### 6. What not to do

- Do not reintroduce **mutually exclusive branch weights** (modal/bio/misalign %).
- Do not multiply independent node marginals without correlation structure.
- Do not add events without `id`, `schedule`, `on_fire`, and observables description.
- Do not sync headline P's to the public blog until owner explicitly requests calibration lock.

---

## Repository layout

```
ai_futures_sim/
  CLAUDE.md          ← you are here
  README.md          ← human onboarding
  config/            ← CANONICAL scenario definition
  src/futures_sim/   ← engine (read-only unless fixing bugs)
  docs/
    evidence/        ← per-event summaries (58)
    research/        ← ported deep rationale (spine, utopia, reference, supplements)
  tests/
  scripts/run_sim.py
  web/               ← future interactive viz (planned)
  outputs/runs/      ← gitignored sim outputs

Private monorepo (`ai_notes/`) may still hold canonical edits until OSS lock; re-run `scripts/port_research_refs.py --copy` before release.
```

---

## Core concepts

### Time

- **1 step = 1 calendar day** (`config/sim.yaml`).
- Horizon: `2026-01-01` → `2050-01-01` (8,766 days).
- Runs end early on **absorbing terminal**; otherwise **horizon default** at 2050.

### Ci spine (probabilistic)

- **`config/spine.yaml`** — AI-2027 capability milestones `sp_c1`…`sp_c9` (plot beats C3/C4/C10 are events only).
- Same hazard model as events; fires **before** events each day.
- `on_fire` sets `ci_level` and may `unlock` plot events (e.g. `sp_c8` → `ev_c10_internal_concern`).
- Events gate on `preconditions.spine_fired`, not deterministic calendar.
- See `docs/SPINE.md` and `docs/research/reference/03_ci_spine.md` for cross-validation.

### Events (58)

Schema in `config/events.yaml`:

| Field | Meaning |
|-------|---------|
| `schedule.p_cumulative` | P(at least one fire in window) — **not** per-day P |
| `schedule.daily_hazard` | Optional explicit daily h |
| `preconditions` | ci_min, vars ranges, events_fired / events_not_fired |
| `requires_unlock` | Event starts blocked until `unlock:` from another event |
| `mutex_group` | At most one variant fires (e.g. whistleblower paths) |
| `on_fire` | unlock, lock, modify_hazard, set_vars, add_vars, force_terminal |

### State variables

See `docs/VARIABLES.md`. Events move **variables**; terminals check **variables + events**.

### Terminals

See `config/terminals.yaml`. Regions: `doom`, `severe`, `utopia`, `friction`.

Example doom chain (bio): low governance → tier-2 live → tier-3 path → release attempt → `doom_extinction_bio`.

---

## Probability workflow

1. Researcher sets **target cumulative P** for a window (from evidence).
2. Engine computes daily hazard (see `cumulative_to_daily_hazard` in `events.py`).
3. Monte Carlo aggregates `P(terminal)` over N runs.
4. **Calibration:** marginal checks — e.g. `P(ev_no_pause_2028 fires)` ≈ 0.88 across runs.

When owner says "X% per year", convert to cumulative window P before editing YAML:

```
p_cumulative_window = 1 - (1 - p_annual)^years_in_window  # approx if interpreting as annual at-least-once
```

Document conversion in commit message.

---

## Pruning (complexity control)

Configured in `sim.yaml`:

- `max_fires_per_day: 2` — prevents unrealistic event stacks
- `max_eligible_checks_per_day: 12` — only highest-hazard eligible events sampled

Do not remove pruning without discussing combinatorial explosion with owner.

---

## Testing checklist

```bash
cd ai_futures_sim
source .venv/bin/activate
pytest -q
futures-sim -n 500 --seed 1
```

Expected: all tests pass; JSON summary with `by_region` and `median_fired_events` ~12–35.

---

## UI / viz roadmap

Open-source UX goals:

- Event DAG diagram (Mermaid or D3) generated from `events.yaml`
- Interactive Sankey: terminal ← event paths
- Sliders for sensitivity on top 5 load-bearing P's
- Export: `outputs/runs/<timestamp>/summary.json` + `paths.parquet`

Place web app under `web/`; keep config in repo root `config/`.

---

## Relationship to owner's notes repo

This folder lives inside `ai_notes` but is designed to be **detachable** for open source.

- Evidence + research are **in-repo** for OSS (`docs/evidence/`, `docs/research/`).
- Owner headline P(doom) comes **from** sim calibration (`docs/research/supplements/pdoom_methodology.md`), not the reverse.

---

## Meta pitfalls (remind the owner)

1. **Daily P confusion** — cumulative vs daily hazard (see PROBABILITY_MODEL.md).
2. **False precision** — 58 events × subjective P's can look scientific while being garbage.
3. **Terminal overlap** — whimper vs friction vs severe need clear precedence rules.
4. **Ci determinism** — capability may deserve stochastic Ci shocks later.
5. **10k runs variance** — report confidence intervals, not point estimates only.

---

## Update log

| Date | Note |
|------|------|
| 2026-07-07 | Initial CLAUDE.md; v0.1 scaffold with 50 events |
| 2026-07-07 | Budget policy: $200 cap; `docs/BUDGET.md` cost ledger |
