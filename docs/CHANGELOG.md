# Changelog

## 2026-07-08 — calibration philosophy

- **Outcome regions are emergent**, not tuned to legacy 19/28/53 partition (pre–Model-2 artifact)
- `calibration_check` / `seed_sweep` report doom/utopia/friction without pass/fail vs those numbers

## 2026-07-08 — v2.4 outcome + path calibration

- **`calibration_check.py`** — outcome regions vs partition targets, early/horizon absorb, path buckets, JSON export
- **`path_frequency.py`** — spine prefixes, event signatures, terminal×spine combos
- **`seed_sweep.py`** — multi-seed stability (42, 123, 456, …)
- **`horizon_default` cascade** — doom/utopia/friction assignment at 2050 (not 100% blind `friction_modal`)
- **C5 deadline** → `2029-03-31`; RSI `2028-10` knot; `sp_c7` threshold 7.15 + legibility ↓
- **`web/`** — static explorer (load JSON from `outputs/runs/`)
- **`docs/CALIBRATION.md`**

## 2026-07-08 — v2.3 Model 2 calibration + society + docs

- **Calibration pass** — `base_daily_growth` + `calendar_rsi` anchors retuned; chain ceiling slack +0.38; c1/c5 legibility hazards adjusted
- **`calibration_check.py`** — conditional P(c5\|c2)…P(c9\|c8), median fire dates, monotonicity flag
- **`ev_c10` consistency** — unlock moved from `sp_c8` → `sp_c9` (matches `preconditions.spine_fired: [sp_c9]`)
- **`capability_controls`** — `ev_prod_interp_halt` (growth×0.78), `ev_multilateral_screening_pilot` (growth×0.92)
- **Society hazards** — Tier 1+2 variable → event feedback (`society_hazard.yaml`)
- **Docs** — `ARCHITECTURE.md` Model 2 + legibility; `CAPABILITY_DYNAMICS.md` synced to yaml

## 2026-07-08 — v2.2 political coupling + legibility

- **Legibility** — latent spine crossing ≠ public fire; `observability.daily_hazard`
- **`capability_controls`** — federal pause, US paralysis S2
- **Early terminals** — `friction_pause_stall`, `friction_governance_paralysis`
- **Variance** — shock prob 0.018, `run_heterogeneity.growth_scale_spread: 0.10`

## 2026-07-08 — v2.1 spine calibration + evidence

- **Spine P/windows tuned** — wider overlapping windows; conditional targets 0.65–0.82
- **`calibration_check.py`** — by-deadline unconditional, conditional \| parent, event conditionals
- **`spine_fire_days`** tracked in engine for deadline calibration
- **Evidence:** `sp_c1`–`sp_c9` full files; `ev_c5/c6/c8` → superseded redirect stubs
- **`ev_c10` evidence** — `spine_fired: [sp_c9]`, unlock from `sp_c8`

## 2026-07-08 — v2.0 probabilistic spine

- **BREAKING:** `ci_schedule.yaml` deterministic calendar **removed** from engine
- **`config/spine.yaml`** — 7 stochastic AI-2027 capability milestones (`sp_c1`–`sp_c9`, skip C3/C4/C10 plot beats)
- **`spine.py`** — same hazard/eligibility model as events; fires before events each day
- **Merged into spine:** `ev_c5_agent2_internal`, `ev_c6_superhuman_coder`, `ev_c8_agi_public` (57 events remain)
- **Plot beats events-only:** C3=`ev_china_cdz`, C4=`ev_c4_labor_shock`, C10=`ev_c10_internal_concern`
- Events use `preconditions.spine_fired` instead of `ci_min`
- **Alignment chain fixed:** `sp_c8` unlocks C10 plot; `sp_c9` + extended windows
- `docs/SPINE.md`; `calibration_check.py` reports spine + event marginals
- Tests: `tests/test_spine.py`

## 2026-07-07 — v1.2 correlations + sovereignty events

- **Research link hygiene** — `--rewrite-research-links` rewrites internal `docs/research/` citations; `supplements/tracker_scorecard.md` stub; relative links within research tree
- **Latent cluster correlations** — `config/correlations.yaml`, `correlations.py`, `docs/CORRELATIONS.md`; 7 clusters (race, bio_governance, bio_tail, alignment_governance, compute_chokepoint, governance_hollowing, sovereignty)
- **Stochastic Ci** — `ci_schedule.yaml` `stochastic:` section; opt-in via `sim.yaml` `stochastic_ci: false` (default)
- **+2 events** — `ev_india_sovereign_ai_stack` (P=0.40), `ev_gulf_compute_sovereignty` (P=0.35); **60 events** total
- **`sovereignty_fragmentation`** state variable
- Tests: `tests/test_correlations.py`

## 2026-07-07 — v1.1 OSS-ready evidence + research

- **58 events** — ontology complete (mutex groups, terminals fixed)
- **58/58 evidence** files — Claim | Why | Evidence | YAML mapping
- **`docs/research/`** — ~38 ported spine/utopia/reference/supplements files; self-contained for OSS
- Link rewrite: evidence → `docs/research/`; Chinese/private refs → public URLs
- `docs/research/reference/` — Ci spine, crux registry, parallel spines (was confusing `archive/`)
- Removed `docs/ONTOLOGY_GAPS.md` (closure doc, stale)
- `docs/EVENTS_INDEX.md` updated to 58 events

**Not done (v1.1):** calibration pass; 10k sim validation.

## 2026-07-07 — v1.3 evidence depth + YAML calibration

- **Evidence depth** — India/Gulf sovereignty events expanded to full template; corp hollowing deepened; thin-file pass on whistleblower/C10 timing
- **YAML ↔ evidence sync** — `ev_bmia_pass` 0.45, `ev_race_acceleration` 0.22, `ev_cyber_cascade` 0.12, C10 + whistleblower windows from **2028-07-01** (tracker Q2–Q3)
- **`scripts/calibration_check.py`** — marginal fire rates vs targets
- Evidence frontmatter `p_cumulative` aligned with YAML for calibrated events
- **Engine fix** — `daily_hazard` now uses full-window constant hazard (was re-scaling `p_cumulative` against shrinking `remaining` days → marginals → 1)

## 2026-07-07 — v1.1 ontology scaffold

- +8 events, +6 variables, `ev_wmd_escalation` terminal fix
- All events → `research_ref: docs/evidence/<id>.md`

## 2026-07-07 — v0.1 scaffold

- Initial repo: 50 events, engine, daily timestep to 2050
