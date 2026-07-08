---
event_id: ev_bio_public_scare
category: bio
conf: medium
port_status: done
source_node: node2
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.30
---

# ev_bio_public_scare — Public bio scare (Trigger E mainstream)

## Observable

FBI/CDC-style investigation, NYT/Science front-page, or congressional hearing on **AI-assisted synthesis** — mainstream Trigger E converting Tier-2 capability into public CBRN salience. Sustained media >2 mo in ~25% of Trigger E worlds (node2 actor table).

## Claim

**P ≈ 0.25–0.35** (YAML **0.30**) **conditional on Tier-2 live** (`ev_bio_tier2_live`). Node2 Trigger E variant bands:

| Variant | P (by ~2027) |
|---------|--------------|
| FBI/CDC synthesis order linked to AI design | 0.15–0.25 |
| NYT/Science after leaked red-team report | 0.20–0.30 |
| Documented near-miss (screening catches AI sequence) | 0.25–0.35 |
| **No Trigger E (modal)** | 0.40–0.50 |

YAML 0.30 = midpoint of public-scare composite, not unconditional calendar draw.

## Why

- Public linkage **rarer** than incident — needs investigation disclosure, whistleblower, or leak
- Screening + recordkeeping (IGSC, proposed BMIA) ↑ traceability of synthesis orders
- Capability alone insufficient for mass public salience — hybrid rule requires Trigger E (node2 §P(timing) public salience)
- Trigger E → P(mandatory screening) **0.75+**; P(mandatory CBRN eval) **0.50+** (conditional effect)
- Salience spike accelerates BMIA hazard ×1.4 in YAML — screening coalition broader than pause camp

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` §Trigger E table — P=0.15–0.35 by variant
- `docs/research/supplements/node2_cbrn_full.md` §Trigger E, §Hybrid rule
- [CAIS — AI biorisk work](https://www.safe.ai/work/ai-biorisk) §4 — red-team landscape
- `docs/research/spine/node2_evidence_rationale.md` §P(effect) — Trigger E → screening P>0.75
- 2001 anthrax letters — single incident → massive salience precedent
- `docs/research/supplements/ai_pause_advocacy_playbook.md` §1.5 — screening > pause coalition

## Analogue

2001 anthrax letters — massive salience from single incident. FLI 2023 — attention without binding policy; bio Trigger E more **concrete** than x-risk letter.

## Would update if

- BMIA mandates near-miss reporting → upper range **0.35**
- Zero public Tier-2 disclosures through 2027 → revise **≤0.20**
- Sustained >2 mo media on leaked red-team **without** synthesis incident → public salience decouples from Trigger E

## Conf

**medium** — variant bands well-documented; exact composite midpoint judgment

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `requires_unlock` | true (`ev_bio_tier2_live`) | Correct capability gate |
| `schedule.p_cumulative` | **0.30** | Mid of node2 Trigger E band — **aligned** |
| `schedule.start` / `end` | 2027-06-01 → 2029-12-31 | Post-Tier-2 window — reasonable |
| `on_fire.add_vars.public_xrisk_salience` | +0.15 | Bio CBRN salience channel |
| `on_fire.modify_hazard.ev_bmia_pass` | ×1.4 | Salience → screening pressure — consistent |

**Calibration:** Conditional on Tier-2; unconditional P much lower if tier2 chain fails.
