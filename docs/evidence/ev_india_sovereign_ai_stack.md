---
event_id: ev_india_sovereign_ai_stack
category: geopolitics
conf: medium
port_status: done
source_node: node7
research_ref: docs/research/spine/node7_evidence_rationale.md §P=0.40
p_cumulative: 0.40
window: 2026-06-01 → 2029-12-31
---

# ev_india_sovereign_ai_stack — India national AI off US hyperscaler for sovereign projects

## Observable

By **2029-12-31**: Indian **government / national-security / CDAC-class** frontier AI projects train or host inference primarily on **non-US sovereign** compute (G42 UAE link, Core42, domestic DC, IndiaAI Mission clusters) — **not** exclusively on AWS/Azure Mumbai for those workloads. Commercial hyperscaler spend continues in parallel (UPI analogue: domestic rail + foreign cards coexist).

## Claim

**P ≈ 0.35–0.45** (YAML **0.40**) that India operates a **material sovereign AI stack** for national frontier projects by end-2029. This is **partial decoupling**, not autarky — ~40% of national-security-linked compute off US triopoly.

## Why

- G42–Cerebras sovereign deal (May 2026); India–UAE AI corridor at India AI Summit framing
- DPDP Act 2023 + draft rules push **data residency** for government datasets
- Node 7: P(India national AI off US hyperscaler) **0.40** — commercial cloud stays modal for startups
- Paris 2025 signatory (#26 India): multilateral **sovereign AI** narrative without US pause dependency
- US export-control friction on H100-class → incentive for Gulf / domestic routing for **classified-adjacent** workloads
- Counterweight: cost + talent on AWS/GCP still wins for most private sector — caps unconditional decouple

## Evidence

- `docs/research/spine/node7_evidence_rationale.md` — P=**0.40** India national AI off US hyperscaler
- `docs/research/spine/node9_evidence_rationale.md` — Global South access + sovereign framing
- [Rest of World — India G42 corridor](https://restofworld.org/2026/india-uae-g42-cerebras-ai-sovereignty/)
- `docs/research/spine/correlation_matrix.md` — Cluster **sovereignty**: India ↔ Gulf ↔ EU GPAI

## Analogue

UPI (domestic payments rail) + Visa/Mastercard coexistence — government mandates local stack; commerce stays hybrid. EU Gaia-X / sovereign cloud bids 2020–2024 — partial, not full exit from US hyperscalers.

## Would update if

- National frontier project **exclusively** on AWS Mumbai with no sovereign duplicate → revise **≤0.20**
- CDAC + IndiaAI Mission **>50%** of gov AI spend on domestic/Gulf stack by 2028 → revise **≥0.55**
- `ev_gulf_compute_sovereignty` fires → hazard ×1.15 (correlated sovereignty cluster)

## Conf

**medium** — direction clear (residency + Gulf link); **medium-low** on exact 0.40 vs 0.35–0.45 band

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2026-06-01 → 2029-12-31 | Long window — sovereign projects slow to stand up |
| `p_cumulative` | **0.40** | **Aligned** with node7 |
| `on_fire.sovereignty_fragmentation` | +0.18 | Government-linked decouple, not full bloc split |
| `correlations` | `sovereignty` cluster | Co-moves with Gulf hub, EU GPAI |

**Calibration:** 2k sim — marginal fire rate **0.32–0.48** acceptable given wide window.
