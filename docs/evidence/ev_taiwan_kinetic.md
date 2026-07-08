---
event_id: ev_taiwan_kinetic
category: conflict
conf: low-medium
port_status: done
source_node: node9 / node3
research_ref: docs/research/spine/node9_evidence_rationale.md §15
p_cumulative: 0.06
---

# ev_taiwan_kinetic — Kinetic engagement Taiwan Strait

## Observable

**Kinetic** military engagement in Taiwan Strait (not cyber-only): exchange of fire, blockade enforcement with casualties, or invasion attempt — may be coupled to AI weight-theft/export-control crisis but **not required**.

## Claim

**P ≈ 0.04–0.08** (YAML **0.06**) unconditional kinetic in 2028–2035 window. Node 9 §15: P(Taiwan hot war **primarily via** AI crisis) **0.03**; unconditional slightly higher.

## Why

- Node 3 T1 kinetic: **0.02–0.04** — AI 2027 datacenter strike is scenario device
- Node 8: P(kinetic | cyber) **<0.03** — cyber on TSMC preferred to invasion (Huang 2025)
- Nuclear shadow + economic interdependence cap escalation
- Node 9: Taiwan fires → **+2–4pp** extinction (speed channel), not independent cause
- YAML unlock from `ev_laws_mass_deploy` is **narrative coupling** — Taiwan can fire without LAWS; correlation ρ modest

## Evidence

- `docs/research/spine/node9_evidence_rationale.md` §15 — P=**0.03** AI-triggered
- `docs/research/spine/node3_evidence_rationale.md` §11 — T1 kinetic 0.02–0.04
- `docs/research/spine/node8_evidence_rationale.md` — kinetic|cyber <0.03
- CFR cyber ops tracker — few kinetic cyber responses

## Analogue

2022 Pelosi visit — high tension, no war. 1996 Taiwan Strait Crisis — exercises, not invasion.

## Would update if

- Documented US strike on PRC datacenter after cyber → revise **≥0.12**
- PRC blockade with casualties → event fires regardless of AI coupling

## Conf

**low-medium** — fat tail, well-studied base rates

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.06** | Unconditional kinetic |
| `on_fire` | `kinetic_escalation` +; unlock `ev_wmd_escalation` path | |
| `preconditions` | narrative unlock from LAWS optional | Decouple in future if over-correlated |
