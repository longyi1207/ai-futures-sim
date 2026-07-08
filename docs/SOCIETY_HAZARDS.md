# Society → event hazard feedback

**Config:** [`config/society_hazard.yaml`](../config/society_hazard.yaml)  
**Code:** `src/futures_sim/society_hazards.py`

Downstream state feeds back into **event hazards** via `EventCatalog.daily_hazard()`.

## Modes

| Mode | Formula term | Use when |
|------|----------------|----------|
| `excess` | `1 + scale × max(0, val − ref)` | High var → more event pressure |
| `deficit` | `1 + scale × max(0, ref − val)` | Low var → more event pressure |
| negative `scale` on `excess` | High var → *less* hazard | e.g. high trust → less deceptive deploy |

A variable may use **multiple spec blocks** (list) for different modes (e.g. `governance_capacity`).

## Variables wired (Tier 1 + 2)

| Variable | Events affected (summary) |
|----------|---------------------------|
| `employment_stress`, `ghost_gdp_index` | Labor / Ghost GDP chain |
| `public_xrisk_salience` | BMIA, pause, whistle, bio scare |
| `deployment_pressure` | Race, theft, deceptive deploy |
| `deception_risk` | C10, whistle, deploy incident |
| `bio_risk_pressure` | Tier-3 bio tail |
| `open_weights_regime` | Open-weights security equilibrium |
| `governance_capacity` | BMIA / treaty ↑; paralysis ↑ when low |
| `inequality_index`, `human_autonomy_index` | Distribution / doom chain |
| `meaning_institution_health` | Utopia / meaning pilots |
| `china_frontier_parity`, `compute_concentration` | Geopolitics / chokepoint |
| `alignment_trust` | Prod interp ↑; deceptive deploy ↓ |

## Preconditions (Tier 2)

`ev_c4_labor_shock` requires `employment_stress ≥ 0.25` (in addition to `sp_c2`).

Events still **modify** vars on fire; this closes the feedback loop.
