---
event_id: ev_corp_safety_hollowing
category: governance
conf: medium-high
port_status: done
source_node: node11
research_ref: docs/research/spine/node11_evidence_rationale.md
p_cumulative: 0.52
---

# ev_corp_safety_hollowing — Corporate safety team hollowing / PBC erosion

## Observable

Through **2030-12-31**: ≥2 frontier labs show safety org **reporting to product/revenue**, dissolved superalignment-style teams, or PBC/LTBT **paper upgrades without deploy veto** — measurable via org charts, exits, and crisis response (training continues post-scare).

## Claim

**P ≈ 0.52–0.65** (YAML **0.52**, conservative) of **continued hollowing** 2026–30. PBC recap (Oct 2025) + LTBT majority (Apr 2026) are **nominal** governance without lowering P(no halt | crisis) ≈ **0.12** (Node 11). This event is the **governance substrate** for modal no-pause + whistleblower-oversight spine.

## Why

- Default track 2024–26: superalignment dissolved (Leike), Sharma exit-not-organize (2026), Altman board crisis → **zero** training halt
- Node 11 branch M1 hollowing **0.65**; safety re-empowered tail only **0.10** — four historical crises → **zero** halts
- Correlates with `ev_no_pause_2028`, `ev_no_shutdown_asi_threshold` unlock — Cluster Race / governance
- Whistleblower modal (0.58) assumes **oversight audits**, not deploy veto — consistent with hollowing
- Counter: `ev_prod_interp_halt` tail if interp team retains teeth at one lab

## Evidence

- `docs/research/spine/node11_evidence_rationale.md` §2 — M1 P=**0.65**; §4 T2 re-empowered **0.10**
- OpenAI board crisis Nov 2023; Sharma exit 2026; OpenAI PBC Oct 2025
- `docs/research/spine/crosscut_secondary_cruxes.md` §2 — hollowing branch 0.65
- `docs/research/spine/correlation_matrix.md` — hollowing ↔ no-pause ↔ race acceleration

## Analogue

OpenAI Nov 2023: board **had** firing power → reinstated in 5 days, safety directors out, training continued. Financial compliance officers post-2008 — more process, same revenue pressure.

## Would update if

- ≥2 labs restore independent safety org with **used** deploy veto → revise **≤0.35**
- `ev_prod_interp_halt` fires at major lab → breaks "train through scare" path; hazard ×0.75 already in YAML
- Federal pause succeeds → mutex path reduces hollowing salience for doom tail

## Conf

**medium-high** on direction (2024–26 track record); **medium** on exact 0.52 vs node11 0.65

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `p_cumulative` | **0.52** | Below M1 0.65 — conservative for window |
| `on_fire` | unlock `ev_no_shutdown_asi_threshold` | ASI threshold crossed without shutdown |
| `modify_hazard` | `ev_prod_interp_halt` ×0.75 | Hollowing reduces prod-halt tail |

**Calibration:** Modal governance spine — fires ~50% in 2k sim; pairs with `ev_no_pause_2028` for coordination-failure narrative.
