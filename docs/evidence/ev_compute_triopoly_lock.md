---
event_id: ev_compute_triopoly_lock
category: economy
conf: medium-high
port_status: done
source_node: node7
research_ref: docs/research/spine/node7_evidence_rationale.md
p_cumulative: 0.82
---

# ev_compute_triopoly_lock — Frontier training locked to hyperscaler triopoly

## Observable

≥**70%** of US frontier **training FLOPs** run on AWS/Azure/GCP through 2028-12 — Anthropic–AWS 5GW Trainium (Mar 2026), OpenAI Stargate multi-cloud but triopoly-retained, neocloud overflow not majority.

## Claim

**P ≈ 0.75–0.88** (YAML **0.82**) that US frontier training remains triopoly-locked through 2028 — CX-COMPUTE-CHOKE crux. Sets `compute_concentration` → 0.85 in sim.

## Why

- Multi-year GW deals create **too-big-to-pause** coalition — hyperscaler capex $200B+ AWS, Stargate political asset
- Self-build partial (Abilene) not full migration by 2028 — OpenAI multi-cloud pattern (Azure primary + Oracle Stargate)
- Neocloud captures **overflow**, not majority of frontier training
- Synergy Q1 2026: triopoly **~63–68%** global IaaS — frontier **more** concentrated than average
- Fable Jun 2026 shows gov **can** cut API access but chose narrow export frame — infrastructure rules tighten, industry keeps training
- Modal branch (Node 7 P=0.58): triopoly + incremental KYC, **no** durable training stop

## Evidence

- `docs/research/spine/node7_evidence_rationale.md` §P=0.82 — US frontier ≥70% triopoly through 2028
- `docs/research/reference/05_crux_registry.md` — CX-COMPUTE-CHOKE **0.82** (0.75–0.88)
- `docs/research/spine/node7_evidence_rationale.md` §P=0.58 — modal triopoly + no halt
- CSA 2025 report — triopoly overwhelming majority of AI-grade enterprise compute
- Anthropic–AWS 5GW commitment Mar 2026 — multi-year binding

## Analogue

Mobile OS duopoly — alternatives exist but not for frontier scale; post-9/11 airline security — infrastructure rules tighten, industry keeps operating.

## Would update if

- Meta or xAI announces **>50%** training on **non-triopoly** owned DC with verified FLOPs
- ≥2 labs **public halt >90d** citing cloud/gov gate (not rhetoric)
- EU/India decouple >25% frontier spend off US hyperscalers (T7-C tail fires)

## Conf

**medium-high** — strong deal-flow evidence; exact 70% threshold uncertain ±5pp

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2026-01-01 → 2028-12-31 | Through 2028-12 per crux horizon |
| `p_cumulative` | **0.82** | **Aligned** with CX-COMPUTE-CHOKE |
| `on_fire` | `compute_concentration` → 0.85; `frontier_lab_polarization` delta | Concentration lock-in |
| `modify_hazard` | race_acceleration ×1.1 | Speed-without-pause channel |

**Calibration:** Run 10k sim — fraction fired should land **0.75–0.88** band.
