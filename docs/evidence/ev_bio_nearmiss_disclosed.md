---
event_id: ev_bio_nearmiss_disclosed
category: bio
conf: medium
port_status: done
source_node: node2 / node10
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.12
---

# ev_bio_nearmiss_disclosed — Tier-2 near-miss disclosed publicly

## Observable

Documented Tier-2 near-miss becomes **public**: CDC/FBI investigation, IGSC catch disclosed, leaked red-team report, or congressional hearing on AI-assisted synthesis **near-miss** (not full release).

## Claim

**P ≈ 0.10–0.15** (YAML **0.12**) of **public disclosure** of Tier-2 near-miss in window, given Tier-2 live. Node 10: P(public Trigger E | Tier 2) ≈ **0.30** union; near-miss disclosure is **subset** — lower than full Trigger E union.

## Why

- Node 2 Trigger E near-miss branch: **0.25–0.35** for documented near-miss **as Trigger E type** — but public **linkage** rarer than incident
- Node 10 §7: public Trigger E **0.30** upper bound — near-miss disclosure is one branch, not additive
- YAML **0.12** = conservative point on disclosed-near-miss specifically (vs hidden 0.28)
- BMIA/RAISE reporting norms would push **up**; GAAIA preemption pushes **down**

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` §Trigger E — near-miss 0.25–0.35; FBI/CDC 0.15–0.25
- `docs/research/spine/node10_evidence_rationale.md` §7 — P(public Trigger E | Tier 2) **0.30**
- https://www.safe.ai/work/ai-biorisk §4

## Analogue

2001 anthrax — single incident → massive salience. Whistleblower vs internal audit — minority of findings become policy punctuations.

## Would update if

- BMIA signed with mandatory near-miss reporting → revise **0.18–0.25**
- Zero IGSC catches reported through 2027 despite Tier-2 live → revise **≤0.08**

## Conf

**medium**

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.12** | Subset of node10 public Trigger E mass |
| `preconditions` | `ev_bio_tier2_live` | Capability gate |
| `on_fire` | `ev_bmia_pass` ×1.5; locks `ev_bio_nearmiss_hidden` | Public punctuation opens policy window |
| `modify_hazard` | vs hidden path | Disclosure → BMIA salience ↑ |
