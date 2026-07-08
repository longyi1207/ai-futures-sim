---
event_id: ev_us_paralysis_s2
category: governance
conf: medium
port_status: done
source_node: crosscut_us_governance_capacity
research_ref: docs/research/spine/crosscut_us_governance_capacity.md
p_cumulative: 0.55
---

# ev_us_paralysis_s2 — US federal governance paralysis (S2 elevated)

## Observable

Through 2028-12-31: ≥2 multi-week shutdown/CR cycles covering Commerce/Judiciary/HHS **and** zero GAAIA/BMIA-class presidential signature — **without** civil-war-scale kinetic conflict. NIST/CAISI underfunded; federal AI rulemaking median >18 mo.

## Claim

Two related probabilities from crosscut — **do not conflate:**

```
P(governance paralysis delays/blocks federal AI law)  ≈ 0.55  (main crux, S1 modal friction)
P(elevated S2: ≥2 shutdowns + no major AI statute)    ≈ 0.28  (full modifier stack)
```

YAML `p_cumulative: 0.55` encodes the **broader** governance-paralysis crux, not the narrower elevated-S2-only definition (0.28).

## Why

- Institutional throughput, not kinetic conflict, dominates US AI law risk
- Through Jul 2026: 43-day FY2026 shutdown, 76-day DHS shutdown, AI omnibus stalls on preemption fights
- BMIA sits in **Commerce** — same stack as CJS appropriations
- Node 6 O3 gridlock **0.45** — S1 modal friction **overlaps** S2; do not double-apply linearly
- S2 modifiers: BMIA ×**0.70** → ~0.32; GAAIA ×**0.60**; Tier 3 before screening ×**1.15–1.25**
- Shifts **~5–8pp** from modal governance toward bio-tail branch (`my_pdoom.md` stitching rule)

## Evidence

- `docs/research/spine/crosscut_us_governance_capacity.md` — P(paralysis) **0.55**; P(elevated S2) **0.28**; modifier table
- [Brookings — government shutdown explainer](https://www.brookings.edu/articles/what-is-a-government-shutdown-and-why-are-we-likely-to-have-another-one/)
- [FAS — Gil on the Hill Feb 2026](https://fas.org/publication/gil-on-the-hill-february-2026/)
- `docs/research/spine/node6_evidence_rationale.md` — O3 gridlock **0.45**
- `docs/research/supplements/ai_pause_advocacy_playbook.md` §1.2 — federal dysfunction default
- `docs/research/spine/correlation_matrix.md` — Cluster F: paralysis ↔ no pause ↔ bio delay tail

## Analogue

Post-Sandy Hook — salience + gridlock; state action while federal stalls. COVID policy lag — insider urgency precedes statutory action by 12–18 mo.

## Would update if

- GAAIA or BMIA **signed** before Dec 2026 → revise paralysis P down to **≤0.35**
- Bipartisan Commerce markup on BMIA **and** full-year CJS pass without CR → elevated S2 **≤0.15**
- Sustained multi-state National Guard vs federal deployment **>90 days** → civil-war tail (separate, P≈0.03)

## Conf

**medium** — shutdown history well-documented; exact P split between S1 modal friction vs S2 elevated is judgment

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule.start` / `end` | 2026-01-01 → 2028-12-31 | Matches crosscut 2026–2028 horizon |
| `schedule.p_cumulative` | **0.55** | **Aligned** with main crux P=0.55 (not 0.28 elevated-only) |
| `on_fire.add_vars.governance_capacity` | −0.20 | Material throughput loss — consistent |
| `on_fire.modify_hazard.ev_bmia_pass` | ×0.65 | Crosscut S2: BMIA ×0.70 — YAML **0.65** close |
| `on_fire.modify_hazard.ev_tier3_path_open` | ×1.35 | Crosscut ×1.15–1.25 — YAML at upper end; **[CALIBRATE]** may be aggressive |

**p_cumulative adjustment:** If sim should encode **elevated S2 only** (0.28), consider lowering to **0.28–0.35** or splitting S1/S2 events — current YAML conflates modal friction label with 0.55 crux.
