# State variables

All variables live on `WorldState` (`src/futures_sim/state.py`). Initial values in `config/variables.yaml`.

## Capability & economy

| Variable | Scale | Meaning |
|----------|-------|---------|
| `ci_level` | 0–10 | Capability index; advanced by spine milestones (`sp_c*`), not calendar |
| `gdp_index` | ≥0, baseline 1.0 | Real GDP vs 2026 |
| `employment_stress` | 0–1 | Junior white-collar displacement / labor shock |
| `ai_rd_multiplier` | ≥1 | Frontier internal R&D speed vs 2026 |
| `tech_level` | 0–1 | Deployed aggregate capability |

## Bio

| Variable | Scale | Meaning |
|----------|-------|---------|
| `bio_capability_tier` | 0–3 | 0 none → 3 catastrophic design path |
| `bio_governance_tier` | 0–3 | Screening / BMIA enforcement strength |
| `bio_risk_pressure` | 0–1 | Latent misuse accessibility |

## Alignment & deployment

| Variable | Scale | Meaning |
|----------|-------|---------|
| `alignment_trust` | 0–1 | Institutional confidence in frontier safety |
| `deception_risk` | 0–1 | Scheming / eval-gaming pressure |
| `deployment_pressure` | 0–1 | Race-to-deploy vs caution |
| `human_autonomy_index` | 0–1 | Human control retained (whimper axis) |

## Governance & geopolitics

| Variable | Scale | Meaning |
|----------|-------|---------|
| `governance_capacity` | 0–1 | US federal effectiveness (↓ = paralysis) |
| `international_coord` | 0–1 | Multilateral AI governance |
| `compute_concentration` | 0–1 | Hyperscaler triopoly chokehold |
| `public_xrisk_salience` | 0–1 | Media / DC extinction attention |
| `frontier_lab_polarization` | 0–1 | 0≈singleton, 1≈multipolar labs |
| `frontier_capex_index` | ≥1 | Frontier AI CapEx vs 2026 |
| `admin_ai_posture` | −1…+1 | Admin acceleration vs regulation |
| `china_frontier_parity` | 0–1 | China frontier vs US |
| `us_china_race_index` | 0–1 | US-China competitive race intensity (race dynamics, separate from raw parity) |
| `eu_regulatory_bind` | 0–1 | EU GPAI/AI Act enforcement bite on frontier labs |
| `china_open_weight_strategy` | 0–1 | China's strategic push on open-weights release |
| `open_weights_regime` | 0–1 | Open-weights norm strength |
| `sovereignty_fragmentation` | 0–1 | EU/India/Gulf sovereign compute decouple from US hyperscalers |
| `kinetic_escalation` | 0–1 | Great-power kinetic risk |

## Society

| Variable | Scale | Meaning |
|----------|-------|---------|
| `inequality_index` | 0–1 | AI gains concentration (↑ worse for utopia) |
| `meaning_institution_health` | 0–1 | Wellbeing / civic pilots |
| `ghost_gdp_index` | 0–1 | GDP↑ without broad wage/employment participation |
| `labor_mobilization` | 0–1 | Organized labor/political response to visible AI-driven displacement |
| `reskilling_absorption` | 0–1 | How much displaced labor is actually re-employed via reskilling (vs. guidance-only programs) |
| `distribution_regime` | 0–1 | Strength of active gains-distribution policy (SWF, reskilling, wellbeing pilots) — low + high `ghost_gdp_index` ⇒ `friction_ghost_gdp_no_transfer` |

## Capability dynamics controls

| Variable | Scale | Meaning |
|----------|-------|---------|
| `rsi_calendar_delay_days` | ≥0, days | Cumulative delay applied to the calendar-RSI lookup (`capability.py::step_capability`) from governance/disclosure events' `capability_controls.rsi_delay_days`. Each contributing event's magnitude is `[GUESS]`-labeled — see the "RSI delay assumption" section in that event's `docs/evidence/<id>.md`. |

## Why not raw "job loss %" only?

`employment_stress` is normalized — easier to couple across regions. Prefer **multiple coupled indices** over one GDP number: Ghost GDP can rise while `gdp_index` rises (productivity vs wages decoupling).

## Terminal checks use variables + events

Example utopia (`utopia_golden_age`):

- `gdp_index` ≥ 1.6
- `governance_capacity` ≥ 0.65
- `inequality_index` ≤ 0.42
- plus optional positive events

Example doom bio: forced by `ev_extinction_bio_release` or terminal conditions on tier + release chain.
