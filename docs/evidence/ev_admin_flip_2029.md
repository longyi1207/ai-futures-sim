---
event_id: ev_admin_flip_2029
category: governance
conf: medium
port_status: done
source_node: crosscut_x5
research_ref: docs/research/spine/crosscut_x5_admin_evidence_rationale.md
p_cumulative: 0.5
---

# ev_admin_flip_2029 — 2029 US administration flips AI posture

## Observable

Jan 2029 administration implements **≥2 of 4** posture reversals: rescind 14365/14409 EO stack, restore AISI safety mandate, sign stronger audit statute, halt DOJ state-law challenges — material shift from Trump-class acceleration default.

## Claim

**P ≈ 0.45–0.55** (YAML **0.50**) for CX-ADMIN-FLIP — 2028-cycle admin materially shifts federal AI posture. Symmetric flip risk = **policy vector** uncertainty, not raw party odds.

## Why

- Trump continuity modal P=**0.38** through 2029 (Scenario A) — not certain; Dem coalition includes Encode/labor/natsec split
- EO 14110 revoked 15 mo after signing — executive AI policy **fragile** across administrations
- Even R successor may shift (Hawley vetting vs Cruz preemption) — Blackburn carve-out path
- All four X5 scenarios preserve ~**88%** P(no pause) — flip moves **vetting/screening**, not training moratorium
- P(BMIA delayed ≥24 mo | admin flip) = **0.55** — transition cost regardless of flip direction
- State frontier laws effective Jan 2027 with ≥85% enforcement continuity — federal flip **does not** repeal SB 53

## Evidence

- `docs/research/spine/crosscut_x5_admin_evidence_rationale.md` §CX-ADMIN-FLIP — P=**0.50**
- `docs/research/spine/crosscut_x5_admin_evidence_rationale.md` §Scenario A — continuity P=**0.38**
- `docs/research/spine/crosscut_x5_admin_evidence_rationale.md` §P=0.88 — no-pause stable across scenarios
- `docs/research/reference/05_crux_registry.md` — CX-ADMIN-FLIP Tier 3 queue
- `docs/research/supplements/ai_pause_advocacy_playbook.md` — executive fragility; EO reversals precedent

## Analogue

Obama EO 13636 (cyber) → Trump revocation pattern; Biden 14110 → Trump 14365/14409 stack — 15-month half-life on AI EOs.

## Would update if

- 2028 R nominee commits to 14365/14409 continuity → revise **≤0.35**
- Dem 2029 Day 1 AISI re-rebrand → BMIA delay probability **≤0.40**
- Supreme Court blocks SB 53 dev duties → state enforcement continuity **≤0.50**

## Conf

**medium** on direction (flip plausible); **medium-low** on exact 0.50 vs Scenario A 0.38 continuity weight

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2029-01-01 → 2029-06-30 | 6-mo inauguration window |
| `p_cumulative` | **0.50** | **Aligned** with CX-ADMIN-FLIP |
| `on_fire` | `governance_capacity` +0.12; hazard modifiers | Posture-dependent paths |
| `modify_hazard` | gaia_preemption, bmia timing | Flip delays BMIA P=0.55 |

**Calibration:** Flip direction unspecified in YAML — event fires on **material change**, not pro-safety only.
