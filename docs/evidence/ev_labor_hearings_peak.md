---
event_id: ev_labor_hearings_peak
category: policy
conf: medium
port_status: done
source_node: node1
research_ref: docs/research/spine/node1_evidence_rationale.md
p_cumulative: 0.75
---

# ev_labor_hearings_peak — Peak DC labor / AI hearings

## Observable

Senate HELP or relevant committees hold **sustained AI + workforce oversight hearings** during Node 1 salience peak (~2027 Q2); AFL-CIO Workers First agenda visible in DC — not single one-off briefing.

## Claim

**P ≈ 0.70–0.80** (YAML **0.75**) for peak DC labor/AI hearings during 2027 — conditional on `ev_c4_labor_shock` unlock. Node 1 P(HELP hearings by peak) = **0.75**.

## Why

- Sanders chairs HELP; AFL-CIO Apr 2026 meeting with Sanders — Workers First agenda sustained (P=0.75)
- 2023–25 established AI hearing pattern; Saunders 2024 arc (transparency not pause) same reference class
- Policy salience peaks ~2027 Q2 (+30% lag vs capability) — hybrid time rule (C)
- Modal outcome = hearings + state bills, **not** federal training cap (P<0.05)
- 79% voters want worker-protection plan (Sanders op-ed, Blue Rose poll cited) — demand side live
- CA Newsom EO N-6-26 (May 2026) study/recommendations on AI workforce — executive branch parallel track

## Evidence

- `docs/research/spine/node1_evidence_rationale.md` §P=0.75 — US Congress AI & jobs hearings by Node 1 peak
- `docs/research/spine/node1_evidence_rationale.md` §P=0.75 — AFL-CIO Workers First sustains agenda
- `docs/research/utopia/node_u2_distribution_evidence_rationale.md` §C4 window — peak political salience ~2027 Q2
- `docs/research/spine/node4_evidence_rationale.md` — P(hearings within 90d | whistleblower) = 0.75 same class
- AFL-CIO Workers First Oct 2025 launch; Sanders Apr 2026 meeting

## Analogue

Saunders 2024 testimony arc — maximum insider salience → hearings + transparency bills, no training halt.

## Would update if

- Zero HELP/jurisdiction AI-labor hearings through 2027-12 after Block-scale events → salience model wrong; revise **≤0.40**
- Hawley/Encode co-sponsor joint workforce + vetting bill with committee hearing → revise **≥0.85**

## Conf

**medium** on direction (hearings modal given shock); **medium** on exact 0.75 vs timing ±1 quarter

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2027-01-01 → 2027-12-31 | Narrow peak window |
| `p_cumulative` | **0.75** | **Aligned** with Node 1 hearing P |
| `requires_unlock` | `ev_c4_labor_shock` | Shock → salience chain |
| `on_fire` | `governance_capacity` +0.05 | Oversight attention, not halt |

**Calibration:** Hearings fire ≠ federal labor law — Node 1 P(binding federal standards) only **0.12**.
