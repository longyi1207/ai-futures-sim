---
event_id: ev_wmd_escalation
category: conflict
conf: low
port_status: done
source_node: node9 / node3
research_ref: docs/research/spine/node9_evidence_rationale.md
p_cumulative: 0.04
---

# ev_wmd_escalation — WMD / strategic escalation crosses extinction threshold

## Observable

Conditional on major kinetic crisis (`ev_taiwan_kinetic`, `kinetic_escalation` ≥ 0.5): strategic nuclear or WMD exchange sufficient for **human extinction** — not conventional war severe bucket.

## Claim

**P ≈ 0.03–0.06** (YAML **0.04**) cumulative **conditional on** kinetic crisis unlock. Unconditional extinction from this path: **<<1%** — Taiwan AI-triggered kinetic P ≈ **0.03** (Node 9 §15); WMD extinction is **subset** of that tail.

## Why

- Node 9 §15: P(Taiwan hot war via AI weight/export crisis) **0.03** — upper-mid Node 3 T1 range
- Node 9 p(doom) coupling: Taiwan fires → **+2–4pp** extinction (speed/coordination, not independent cause)
- Nuclear shadow + economic interdependence cap escalation — Stuxnet-class rarity
- AI 2027 kinetic strike on PRC datacenters is **scenario device**, not base rate
- Requires `kinetic_escalation` ≥ 0.5 — filters to already-escalated worlds
- YAML **0.04** = P(extinction-class WMD | kinetic crisis), not P(kinetic)

## Evidence

- `docs/research/spine/node9_evidence_rationale.md` §15 — Taiwan **0.03**; §p(doom) coupling +2–4pp
- `docs/research/spine/node3_evidence_rationale.md` §11 — T1 kinetic **0.02–0.04**
- CFR cyber ops tracker — few kinetic cyber responses
- `docs/research/spine/crosscut_x6_science_evidence_rationale.md` — human-in-loop **0.88** through 2030

## Analogue

Cuban Missile Crisis — escalation contained; 1914 chain — rare full great-power WMD exchange.

## Would update if

- Explicit US–China nuclear doctrine shift toward launch-on-warning automation → revise up
- CCW/LAWS treaty with teeth + hotline upgrades post-crisis → revise **≤0.02**
- Taiwan kinetic fires without WMD → validates low conditional rate

## Conf

**low** — tail only; quant highly uncertain

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.04** | Conditional on kinetic crisis |
| `preconditions` | `ev_taiwan_kinetic`; `kinetic_escalation` ∈ [0.5, 1.0] | |
| `on_fire` | `force_terminal: doom_extinction_kinetic` | |
| Unconditional target | **<1%** marginal extinction from kinetic bucket | Joint tune with `ev_taiwan_kinetic` |
