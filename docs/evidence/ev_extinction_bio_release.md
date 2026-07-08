---
event_id: ev_extinction_bio_release
category: doom
conf: low
port_status: done
source_node: node2 / my_pdoom
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.15
---

# ev_extinction_bio_release — Catastrophic pandemic / bioweapon extinction event

## Observable

Human extinction or >90% population loss from AI-enabled biological release — pandemic with R₀ and CFR sufficient for civilization collapse, attributed to AI-assisted design/deployment chain.

## Claim

**P ≈ 0.10–0.20** (YAML **0.15**) cumulative **conditional on** `ev_tier3_release_attempt` unlock in 2029–2040 window. Unconditional bio extinction by 2050: **~1–3%** of total extinction mass under MODAL governance (Node 2); higher under TAIL-A/B/C.

## Why

- Node 2 §p(doom): P(extinction | MODAL) bio slice **~1–3%** of all extinction mass — most bio risk is **severe not extinct**
- TAIL-A (Tier 3 before screening): moderate–high **within bio bucket** — this event is the **extinction tail** of that bucket
- Adelstein: bio risks separate ~8–10% in some decompositions — MODAL discounts skilled-actor tail
- Release attempt (0.08) × conditional extinction given attempt — YAML 0.15 is the **hazard of terminal absorption**, not marginal world probability
- Screening + RAISE shrink tail; nuclear terrorism analogue — gated by access

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` §p(doom) conditional claims
- `docs/research/supplements/node2_cbrn_full.md` §p(doom) link, §TAIL-A/B/C
- `docs/research/supplements/pdoom_methodology.md` — Adelstein bio ~8–10% separate; branch mixture retired
- RAND RBA4087-1

## Analogue

1918 flu (severe, not extinct); engineered pandemic tail in Bostrom/Ord — low base rate, catastrophic conditional.

## Would update if

- Tier-3 under full MODAL rules → MODAL estimate failed, revise unconditional bio extinction up
- Successful BMIA + near-miss disclosure → revise conditional **≤0.08**

## Conf

**low** on point estimate — direction medium; quant highly uncertain

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.15** | **Conditional hazard** post-attempt, not marginal P(extinction) |
| `requires_unlock` | `ev_tier3_release_attempt` | Chain terminal |
| `on_fire` | `force_terminal: doom_extinction_bio` | Absorbing state |
| `preconditions` | tier3 attempt fired | |

**Calibration note:** Sim marginal P(bio extinction) should land **~1–5%** after full chain gating — if >>10%, lower `p_cumulative` or attempt rate.
