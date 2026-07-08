---
event_id: ev_tier3_release_attempt
category: bio
conf: medium-low
port_status: done
source_node: node2
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.08
---

# ev_tier3_release_attempt — Tier-3 release / lab escape / deliberate deploy attempt

## Observable

Documented attempt at **low-skill** Tier-3 path: deliberate release, lab escape with community transmission risk, or open-weight-facilitated deploy — attributed to AI-assisted design pipeline.

## Claim

**P ≈ 0.06–0.10** (YAML **0.08**) cumulative in 2029–2035 window, gated on `ev_tier3_path_open`. Node 2 TAIL-A (Tier 3 before screening): **0.20** of Tier-2 futures — **attempt** is lower than path-open because most attempts are intercepted.

## Why

- TAIL-A: low-skill viable before reg catches up — **0.20** branch mass, not majority
- GeneBreaker scaling + non-IGSC vendors + 50bp delay create window
- No public Tier-3 confirmed as of 2026 — extrapolation from skilled-actor path
- BMIA pass ×0.35 hazard modifier — screening shrinks attempt rate sharply
- Open weights equilibrium keeps FM gating off — chronic tail not modal

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` §TAIL-A P=**0.20**
- `docs/research/supplements/node2_cbrn_full.md` §TAIL-A
- https://arxiv.org/abs/2505.23839 (GeneBreaker)
- RAND RBA4087-1 — assistive now; autonomous design post-2027
- `docs/research/supplements/biosecurity_evo_dual_use.md` §4

## Analogue

Aum Shinrikyo sarin — low-tech terror with high intent; COVID lab-leak debate — attribution fights even when harm is real.

## Would update if

- Documented Tier-3 attack under full MODAL rules → TAIL-A underestimated, revise **≥0.15**
- BMIA + EU both enforced with IGSC upgrade → revise **≤0.04**

## Conf

**medium-low** — tail extrapolation; no confirmed Tier-3 event yet

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.08** | Attempt, not extinction — unlocks `ev_extinction_bio_release` |
| `requires_unlock` | `ev_tier3_path_open` | Path must be viable first |
| `modify_hazard` | BMIA pass ×0.35; open-weights tamper ×0.8 | Mitigation stack |
