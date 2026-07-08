---
event_id: ev_bmia_pass
category: bio_policy
conf: medium-high
port_status: done
source_node: node2
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.45
---

# ev_bmia_pass — Federal BMIA-class mandatory nucleic-acid synthesis screening enacted

## Observable

US enacts **mandatory federal synthesis screening** (BMIA / S.3741-class): nucleic-acid order screening, recordkeeping, enforcement teeth at synthesis vendors — **not** training pause or compute cap. Presidential signature + implementing rule path initiated.

## Claim

**P ≈ 0.42–0.48** (by end-2028) that BMIA-class screening becomes law. YAML **0.45** aligns with node2 **0.45** for 119th Congress window.

Narrow bipartisan physical chokepoint — **not** training pause. Screening coalition broader than pause camp (playbook §1.5).

## Why

- Cotton–Klobuchar bipartisan bill (Jan 29 2026); industry endorsements (Twist, IDT, Ginkgo)
- Jun 2026 screendna letter aligns frontier labs + synthesis CEOs
- Trump admin prefers voluntary frameworks but supports screening per AI Action Plan
- **0.45** ≈ 50% chance in 119th Congress; **0.60** adds second session / EU pressure
- Still in Commerce committee as of Jul 2026 — no floor vote yet
- Under S2 paralysis: P ×**0.70** → ~0.32 (crosscut worked example)

## Evidence

- [S.3741 — 119th Congress](https://www.congress.gov/bill/119th-congress/senate-bill/3741)
- [Cotton–Klobuchar press release](https://www.cotton.senate.gov/news/press-releases/cotton-klobuchar-introduce-bill-to-establish-federal-biotech-security-framework)
- [screendna.org letter](https://screendna.org/) (Jun 4, 2026)
- [ARI — BMIA analysis](https://ari.us/cotton-klobuchar-intro-biosecurity-modernization-and-innovation-act-to-address-ai-era-biosecurity-risks/)
- `docs/research/spine/node2_evidence_rationale.md` — P(BMIA) **0.45** / **0.60**
- `docs/research/spine/crosscut_us_governance_capacity.md` — S2 ×0.70 modifier
- `docs/research/supplements/ai_pause_advocacy_playbook.md` §1.5 — screening > pause

## Analogue

IGSC voluntary → OSTP procurement mandate (2024) → BMIA as third ratchet. Post-2001 airport security — mandatory physical screening, not "stop flying."

## Would update if

- BMIA **signed** before Dec 2027 → set early-window P **≥0.70**; accelerate compliance timeline
- BMIA **dies in committee** without substitute by Dec 2027 → revise 2028-06 to **≤0.35**
- `ev_us_paralysis_s2` fires → apply ×0.70 modifier (crosscut)
- `ev_bio_public_scare` fires → hazard ×1.4 accelerates passage

## Conf

**medium-high** on direction (bipartisan + industry coalition real); **medium** on exact calendar P

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule.p_cumulative` | **0.45** | **Aligned** with node2 **0.45** |
| `schedule.start` / `end` | 2027-01-01 → 2028-12-31 | Spans evidence anchors — correct |
| `on_fire.set_vars.bio_governance_tier` | 2.5 | Screening enacted; CBRN evals may stay voluntary |
| `on_fire.modify_hazard.ev_tier3_path_open` | ×0.45 | Strong screening cuts Tier-3-before-screening tail |
| `on_fire.modify_hazard.ev_tier3_release_attempt` | ×0.35 | Coherent downstream mitigation |
| `on_fire.lock` | `[ev_bmia_enforcement_weak]` | Mutually exclusive weak-enforcement branch |

**p_cumulative adjustment:** Calibrated **0.45** (2026-07); under S2 paralysis effective P ~0.32 via hazard modifier.
