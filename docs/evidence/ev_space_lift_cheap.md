---
event_id: ev_space_lift_cheap
category: utopia
conf: low
port_status: done
source_node: crosscut_x6 / node_u4
research_ref: docs/research/spine/crosscut_x6_science_evidence_rationale.md §EV-SPACE-LIFT
p_cumulative: 0.08
---

# ev_space_lift_cheap — <$500/kg LEO sustained (>100t)

## Observable

≥4 qualifying **commercial** flights in one calendar quarter: **>100 t** payload to LEO at **<$500/kg** sustained pricing (public manifest or audited customer disclosure).

## Claim

**P ≈ 0.08** cumulative in sim window **2032–2040** (YAML). Research strict bar by 2030: **0.22** (X6 §EV-SPACE-LIFT). Sim uses **later window + ci_min 7** — reconciles lower `p_cumulative`.

## Why

- X6 EV-SPACE-LIFT: P=**0.22** before 2031 strict bar (≥4 qualifying flights/quarter)
- Starship V3 May 2026 — capacity target >100t; **pricing/cadence unproven**; refueling incomplete
- U4 Starship commercial payload P=**0.72** by 2027 — **loose** bar (hardware flies, economics not)
- Union EV-SC-DEMO + EV-SPACE-LIFT P≈**0.55** before 2032 — mostly partial commercial lift
- `[SPEC]` — economics lag hardware validation

## Evidence

- `docs/research/spine/crosscut_x6_science_evidence_rationale.md` §EV-SPACE-LIFT P=**0.22**
- SpaceX Starship flight records — https://www.spacex.com/vehicles/starship/
- X6 §P=0.55 union before 2032

## Analogue

Falcon 9 — years between first flight and <$1000/kg economics.

## Would update if

- ≥6 paid >100t flights at disclosed <$500/kg in 2028 → revise sim **p_cumulative ≥0.25**
- Starship commercial pause >24 mo → revise **≤0.03**

## Conf

**low** — hardware [EST]; price bar [SPEC]

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.08** | Late window vs research 0.22 @2030 — intentional |
| `ci_min` | 7 | Post-internal-genius-country |
| `schedule` | 2032–2040 | |

**Calibration note:** If aligning to X6 0.22, widen window to 2030 or raise `p_cumulative` to ~0.15–0.20.
