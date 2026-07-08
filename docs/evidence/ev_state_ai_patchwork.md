---
event_id: ev_state_ai_patchwork
category: governance
conf: medium
port_status: done
source_node: node1 / node6
research_ref: docs/research/spine/node1_evidence_rationale.md
p_cumulative: 0.55
---

# ev_state_ai_patchwork — State-level AI patchwork (SB53-class) binds before federal framework

## Observable

State-level AI laws (CA SB 53, RAISE Act NY, CO AI Act) **materially bind** frontier labs before weak or absent federal preemption — transparency/catastrophic-risk reporting enforced, GAAIA preemption tail fails.

## Claim

**P ≈ 0.50–0.60** (YAML **0.55**) that SB 53-class state patchwork binds through 2028 — composite of P(SB 53 stands) **0.85**, P(unions + populist right block preemption) **0.55**, P(gridlock states primary) **0.45**.

## Why

- Node 1 P(SB 53 compliance path proceeds) = **0.85** — law signed 2025-09-29, effective 2026
- Node 1 P(unions + populist right block federal preemption) = **0.55** — Cruz 99–1 precedent against state-ban moratorium
- Node 6 P(gridlock; states primary) = **0.45** — default US federal dysfunction on tech
- Node 6 P(GAAIA full preemption) = **0.12** tail — Encode + Newsom-style governors resist
- Trump EO 2026 voluntary framework may satisfy industry enough to kill GAAIA urgency (P=0.25)
- Federal flip 2029 does **not** repeal state law — X5 P(state enforcement continuity) **≥0.85**
- `modify_hazard` gaia_preemption ×0.85 — patchwork moderates federal preemption tail

## Evidence

- `docs/research/spine/node1_evidence_rationale.md` §P=0.85 — SB 53 compliance path
- `docs/research/spine/node1_evidence_rationale.md` §P=0.55 — block federal preemption coalition
- `docs/research/spine/node6_evidence_rationale.md` §P=0.45 — gridlock, states primary
- `docs/research/spine/node6_evidence_rationale.md` §P=0.12 — GAAIA full preemption tail
- https://www.brookings.edu/articles/what-is-californias-ai-safety-law/ — SB 53 structure

## Analogue

ACA vs state health laws — partial preemption fights took years; environmental patchwork (CA emissions) binding before federal uniformity.

## Would update if

- GAAIA passes with 3-year preemption intact → revise **≤0.25**
- GAAIA preemption passes **and** SB 53 enforcement continues unscathed → legal model wrong
- Major lab publicly refuses SB 53 compliance without penalty → enforcement model fails

## Conf

**medium** on direction (state-first modal); **medium** on exact 0.55 composite vs component Ps

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2026-06-01 → 2028-12-31 | SB 53 effective + GAAIA fight window |
| `p_cumulative` | **0.55** | **Aligned** — between 0.45 gridlock and 0.85 SB 53 stand |
| `on_fire` | `governance_capacity` +0.05; `admin_ai_posture` +0.08 | State-led governance capacity |
| `modify_hazard` | gaia_preemption ×0.85 | Patchwork blocks clean federal preemption |

**Calibration:** Patchwork = **vetting/transparency**, not training pause — consistent with Node 1 modal 62%.
