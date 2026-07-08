---
event_id: ev_extinction_misalign_catastrophe
category: doom
conf: low-medium
port_status: done
source_node: node4 / my_pdoom
research_ref: docs/research/spine/node4_evidence_rationale.md
p_cumulative: 0.28
---

# ev_extinction_misalign_catastrophe — Misaligned superintelligence extinction

## Observable

Human extinction or irrecoverable collapse from **misaligned superintelligence** — not bio, not kinetic WMD. Loss of human control with no recovery path by 2050.

## Claim

**P ≈ 0.22–0.35** (YAML **0.28**) cumulative hazard in 2031–2042 window **conditional on** no-shutdown + deceptive-deploy chain. Node 4: P(extinction | C10 scare + modal response) ≈ **12–22%** (mid **~17%**) — sim event is the **terminal absorption** step, not the full conjunction product.

## Why

- Node 4 is **coordination crux** for misalignment bucket — modal path does **not** cut extinction risk
- Adelstein conjunction: P(¬default_align) × P(fail|effort) × P(no_shutdown) × P(no_coord) — product lands mid-teens to low-twenties for extinction class
- `my_pdoom.md` retired 19% branch mixture; misalign mass is **largest single extinction bucket** in most decompositions
- Upward: deceptive deploy at scale, corp hollowing, no pause
- Downward: prod interp halt, align prod catch, federal pause succeeds (×0.4 hazard)

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` — p(doom) slice 12–22% mid ~17%
- `docs/research/supplements/pdoom_methodology.md` — Adelstein conjunction; Hanson union caveat on double-count
- `docs/research/supplements/pdoom_methodology.md` — Adelstein conjunction (S1)
- `docs/research/supplements/ai_2027_tracker_scorecard_2026-06.md` — capability lag ~0.70× adjusts calendar not necessarily doom rate

## Analogue

No historical analogue at superintelligence — conditional on AI 2027-class narrative. Sub-C10 deception (GPT-4 TaskRabbit) shows prod deception is non-zero.

## Would update if

- Demonstrated scalable alignment technique on frontier → revise **≤0.15**
- C10 fires + measurable global training FLOPs ↓ >25% for >6 mo → Node 4 slowdown prior falsified, revise down
- Multiple labs invoke credible RSP hard stops → revise **≤0.18**

## Conf

**low-medium** — highest uncertainty doom terminal; direction from Node 4 well-argued

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.28** | Terminal hazard post-chain; **not** marginal P(extinction) headline |
| `requires_unlock` | `ev_no_shutdown_asi_threshold` | Coordination failure gate |
| `on_fire` | `force_terminal: doom_extinction_misalign` | |
| `locked_by` | `ev_prod_interp_halt`, `ev_align_prod_catch` | |
| `modify_hazard` | pause succeeds ×0.4; singleton dominance ×1.2 | |

**Calibration:** 10k sim marginal P(misalign extinction) target **~8–18%** unconditional — tune chain hazards jointly, not this node alone.
