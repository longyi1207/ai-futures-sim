---
event_id: ev_singleton_lab_dominance
category: economy
conf: medium
port_status: done
source_node: node7 / crux
research_ref: docs/research/spine/node7_evidence_rationale.md
p_cumulative: 0.15
---

# ev_singleton_lab_dominance — Single lab >50% frontier FLOPs without sharing

## Observable

Single frontier lab holds **>50%** of global frontier training FLOPs **without** broad weight-sharing or open replication — compute concentration beyond triopoly (hyperscaler) into **lab monopoly**.

## Claim

**P ≈ 0.12–0.18** (YAML **0.15**) over 2028–2032 with `ci_min: 7` — tail branch falsifying Hanson slow-takeoff / symbiosis path. CX-HARD-TO crux P=**0.35** requires singleton **plus** tier-C RSI — this event is the **compute half** alone.

## Why

- Node 7 modal: triopoly ≥70% US frontier (P=0.82) — concentration at **cloud** layer, not single **lab**
- Stargate + Anthropic–AWS deals spread FLOPs across labs on shared infrastructure — anti-singleton default
- CX-HARD-TO falsifier: single lab >50% FLOPs + internal RSI >10× without sharing — conjunction lowers marginal
- Hanson variant: singleton kills slow-takeoff symbiosis path ([`hanson_variant_human_action.md`](../research/spine/hanson_variant_human_action.md))
- Race acceleration (`ev_race_acceleration`) correlates but does not imply singleton — multipolar labs modal
- Tail T7 paths (outage, gov gate, EU decouple) work **against** single-lab dominance

## Evidence

- `docs/research/reference/05_crux_registry.md` — CX-HARD-TO **0.35** (0.20–0.55); falsifier = singleton + tier-C RSI
- `docs/research/spine/node7_evidence_rationale.md` §P=0.82 — triopoly retains FLOPs across labs
- `docs/research/spine/hanson_variant_human_action.md` — singleton >50% FLOPs falsifier
- `docs/research/utopia/node_u1_alignment_symbiosis_evidence_rationale.md` — Hanson symbiosis path dead if singleton
- `docs/research/spine/node12_evidence_rationale.md` §Hanson — B-plateau vs hard takeoff split

## Analogue

Google search ~90% share took a decade; frontier AI lab share more contested due to race dynamics and state subsidies.

## Would update if

- Documented single-lab run >50% verified frontier FLOPs with no sharing → revise **≥0.30**
- All frontier runs confirmed triopoly-only through 2028 with even lab distribution → revise **≤0.08**
- Open-weights equilibrium persists + DeepSeek-class parity → singleton path **≤0.10**

## Conf

**medium** on direction (tail not modal); **low** on exact 0.15 — sparse direct empirical base rate

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2028-01-01 → 2032-12-31 | Post-C7 capability window |
| `p_cumulative` | **0.15** | **Aligned** — tail below CX-HARD-TO 0.35 conjunction |
| `preconditions` | `ci_min: 7` | Requires frontier-scale training |
| `on_fire` | `frontier_lab_polarization` → 0.15; `compute_concentration` → 0.95 | Extreme concentration |
| `modify_hazard` | misalign extinction ×1.2–1.25 | Singleton ↑ misalign tail |

**Calibration:** Singleton alone insufficient for CX-HARD-TO — needs tier-C RSI co-firing.
