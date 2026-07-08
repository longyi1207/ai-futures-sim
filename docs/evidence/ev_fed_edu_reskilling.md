---
event_id: ev_fed_edu_reskilling
category: utopia
conf: medium
port_status: done
source_node: crosscut_x4
research_ref: docs/research/spine/crosscut_x4_education_evidence_rationale.md
p_cumulative: 0.22
---

# ev_fed_edu_reskilling — Federal AI reskilling package >$10B

## Observable

US federal AI-literacy/reskilling **enacted** appropriation **>$10B** (single bill or 3-yr cumulative supplemental) — step-change vs baseline WIOA Title I (~$3.9–5.7B/yr aggregate).

## Claim

**P ≈ 0.14–0.32** (YAML **0.22**) for EV-EDU-FED by 2030 — X4 central estimate. Distinct from CX-EDU-RESPONSE modal P=**0.60** (reskilling **fails** to absorb C4 shock).

## Why

- Time asymmetry: METR 50%-horizon doubles ~90 days; credentialed pathway = 6–24 mo + 12–24 mo bill lag
- So-so automation incentive — firms profit from junior cuts without retraining obligation (Block, Cloudflare)
- Federal fiscal headwind: MASA consolidation proposed (~29% cut vs FY25 WIOA); no >$10B step-change in pipeline
- S.3319 — $160M Ed + $90M DOL grants authorized (not $10B threshold)
- Workforce of Future Act authorizes ~$250M — studies + small grants, not billions
- TEGL 03-25 modal ceiling P=**0.75** — guidance without appropriation scale
- Node 1 modal: hearings + vetting, not federal spending revolution — P(narrow AI-workforce legislation $1–3B/yr) = **0.30**

## Evidence

- `docs/research/spine/crosscut_x4_education_evidence_rationale.md` §EV-EDU-FED — P=**0.22** (0.14–0.32)
- `docs/research/spine/crosscut_x4_education_evidence_rationale.md` §CX-EDU-RESPONSE — P=**0.60** failure modal
- `docs/research/spine/crosscut_x4_education_evidence_rationale.md` §P=0.55 — MASA block-grant cut proposal
- https://www.congress.gov/bill/119th-congress/senate-bill/3319/text — S.3319 scale
- `docs/research/spine/node1_evidence_rationale.md` §P=0.85 — labs reskilling PR modal, not federal $10B

## Analogue

Post-2008 stimulus job training — authorized billions but delivered incrementally; WIOA reauth fights typically flat-funded.

## Would update if

- Workforce bill marked up at ≥$3B/yr AI line → revise up to **≥0.35**
- CBO scores funded UBI with compute/SWF revenue and passes Senate → adjacent pathway opens
- Amazon/Google audited placement ≥2M with federal reporting mandate → conditional P **0.35** given EV-EDU-FED

## Conf

**medium** on direction (activity without absorption modal); **medium** on exact 0.22 band

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2027-06-01 → 2031-12-31 | Post-C4 shock response window |
| `p_cumulative` | **0.22** | **Aligned** with X4 EV-EDU-FED |
| `on_fire` | `employment_stress` −0.12; `human_autonomy_index` delta | Partial absorption if fires |
| `requires_unlock` | none | Correlates with C4 timing |

**Calibration:** Success branch conjunct ≤0.25 after correlation — EV-EDU-FED alone +4pp U4 per X4 parent.
