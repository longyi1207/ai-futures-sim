---
event_id: ev_bio_tier1_live
category: bio
conf: medium-high
port_status: done
source_node: node2
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.90
---

# ev_bio_tier1_live — Tier-1 bio assist widespread

## Observable

Frontier LLMs provide **actionable post-jailbreak bio guidance** (WMDP-bio uplift, synthesis-relevant detail) at scale — Tier 1 **confirmed** not merely emerging. Skilled red-teams demonstrate uplift under jailbreak; not yet Tier-2 end-to-end skilled actor.

## Claim

**P ≈ 0.85–0.95** (YAML **0.90**) that Tier-1 is live by end-2027 window. High P because **already partially live** in 2026 — status claim more than future forecast.

Node 2 §P(status): Tier 1 **confirmed at frontier** — jailbroken models pass WMDP-bio subsets with synthesis-relevant detail.

## Why

- GeneBreaker ~60% ASR on Evo2-40B for pathogen-homologous outputs (2025)
- RAND RBA4087-1: **assistive** acceleration **now**; autonomous design ~post-2027
- Tier 1 = actionable post-jailbreak guidance; **not** Tier 2 (end-to-end skilled actor) or Tier 3 (low-skill)
- Sandbagging/eval-awareness caveat: public WMDP scores may be lower bounds (node2 §sandbagging)
- Unlocks `ev_bio_tier2_live` — chain start for bio extinction path

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` §P(status) Tier 1 confirmed
- [GeneBreaker — arxiv:2505.23839](https://arxiv.org/abs/2505.23839) — ~60% ASR on pathogen-homologous outputs
- [CAIS — AI biorisk work](https://www.safe.ai/work/ai-biorisk)
- [RAND RBA4087-1](https://www.rand.org/pubs/research_briefs/RBA4087-1.html) — assistive acceleration now
- `docs/research/supplements/biosecurity_evo_dual_use.md` — Evo2/GeneBreaker scaling context
- WMDP-bio benchmark — jailbreak uplift on frontier LLMs (2024–25 red-team literature)

## Analogue

Early cyber exploit kits — assist exists before automated weaponization. Script kiddies get tools before turnkey weapons.

## Would update if

- Third-party eval with realism controls shows **no** jailbreak uplift → demote to emerging, lower P to **≤0.60**
- Arc/Evo mitigations collapse GeneBreaker ASR → demote Tier 1 status through 2028
- Documented Tier-3 attack → skip chain to tier 3 path

## Conf

**medium-high** — public red-team evidence strong; sandbagging caveat lowers certainty on exact 0.90

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule.p_cumulative` | **0.90** | Within 0.85–0.95 band — **aligned** |
| `schedule.start` / `end` | 2026-01-01 → 2027-06-30 | Early window; near-live status — correct |
| `on_fire.set_vars.bio_capability_tier` | 1.0 | Tier 1 confirmed |
| `on_fire.unlock` | `[ev_bio_tier2_live]` | Chain start — correct |

**Note:** High P reflects **status confirmation** in sim window, not distant extrapolation.
