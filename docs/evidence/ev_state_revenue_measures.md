---
event_id: ev_state_revenue_measures
category: utopia
conf: medium
port_status: done
source_node: node_u2
research_ref: docs/research/utopia/node_u2_distribution_evidence_rationale.md
p_cumulative: 0.38
---

# ev_state_revenue_measures — State-level AI revenue measures with teeth (CA/NY/WA)

## Observable

≥1 large US state enacts a compute tax, data-center surcharge, or equity-severance mandate **with enforcement teeth** — not a study, EO, or notice-only bill (contrast CA EO N-6-26, which is study-only). Distinct from and does **not** require federal SWF (`ev_swf_enacted`).

## Claim

**P ≈ 0.38** that ≥1 large state (CA/NY/WA) enacts such a measure by 2028. This is the **intermediate** distribution outcome between "nothing" and full federal SWF: patchwork, partial, state-scoped — not the modest_welfare/golden_age-grade settlement `ev_swf_enacted` represents.

## Why

This event was identified as a **gap**, not invented fresh: `node_u2_distribution_evidence_rationale.md` already carries a sourced P for this outcome, but no corresponding event existed in `events.yaml` — meaning `distribution_regime` could previously only ever be "low" (0.10, no measures) or "high" (0.55, full SWF via `ev_swf_enacted`, p=0.12), with no path to an intermediate, partial-success state. That gap made `friction_managed_non_utopia` (needs `distribution_regime` in [0.30, 0.65] alongside other conditions) structurally unreachable — not because the scenario is rare, but because no event could produce it. This event fills that gap directly from existing research rather than backing into a new number to make a terminal reachable.

- States as policy labs when federal is gridlocked (Node 6 federal paralysis baseline)
- CA SB 951 (AI displacement notice, 60-day) already pending as of research date
- Newsom EO N-6-26 (May 2026) is study-only — this event requires going **past** that, to enactment with teeth
- Federal CX-NO-PAUSE-style gridlock (P≈0.88 no federal training pause) pushes distribution fights to the state level by the same logic

## Evidence

- `docs/research/utopia/node_u2_distribution_evidence_rationale.md` — "P = 0.38 — State-level AI-adjacent revenue measures (CA/NY/WA) by 2028"
- `docs/research/utopia/node_u2_distribution_evidence_rationale.md` — "P = 0.45 — Second-wave policy window @C6-C7" (later variant of the same mechanism, not separately modeled here)
- SB 951 (CA): AI displacement notice 60-day — pending
- Node 1 P(CA labor AI bill) 0.50 — adjacent precedent for state-level AI legislative activity

## Would update if

- GAAIA federal preemption passes **without** carve-outs for state AI labor/revenue bills (Node 1 P≈0.12) → this path narrows or closes
- ≥2 states enact measures before 2028 → shift window/probability up
- Federal SWF (`ev_swf_enacted`) enacted first and pre-empts state-level appetite for separate measures (not modeled as a direct interaction — no mutex currently)

## Conf

**medium** on direction and window; the research file itself notes this class of measure is easier to pass than federal equity/wealth-tax measures (administrability, no interstate-commerce fight at CA/NY/WA scale) but has not been enacted anywhere yet as of the research date, so magnitude carries the same uncertainty as other unenacted-tail estimates in this file.

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2027-01-01 → 2028-12-31 | Matches research's "by 2028" window |
| `p_cumulative` | **0.38** | Directly sourced, not backed into |
| `on_fire.add_vars.distribution_regime` | +0.22 | Sized to land in `friction_managed_non_utopia`'s [0.30, 0.65] band alone (0.10 baseline + 0.22 = 0.32) — deliberately smaller than `ev_swf_enacted`'s +0.45, since this is a partial/patchwork mechanism by design, not a settlement |
| `on_fire.add_vars.inequality_index` | -0.05 | Small relative to SWF's -0.15 — state-scoped, not national-scale redistribution |
| Not added to any `utopia_*` `events_any` list | — | Deliberate: research frames this as *insufficient alone* for true utopia/settlement, only for the intermediate "managed but not flourishing" terminal |

**Calibration:** fraction of runs where `ev_state_revenue_measures` fires should land ≈0.38 after gating; distinct from and not mutex with `ev_swf_enacted`.
