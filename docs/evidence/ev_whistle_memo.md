---
event_id: ev_whistle_memo
category: alignment
conf: medium
port_status: done
source_node: node4
research_ref: docs/research/spine/node4_evidence_rationale.md §7
p_cumulative: 0.35
---

# ev_whistle_memo — NYT/WSJ memo leak → hearings

## Observable

Named former safety employee + internal alignment memo reaches NYT/WSJ/TIME-class outlet; 6–10 week mainstream media cycle; congressional hearings within ~90 days. **Not** raw eval dump (E2) or attributed prod harm (E3).

## Claim

**P(E1 | C10 internal concern) = 0.35** (range 0.30–0.40) — highest single leak variant in Trigger E partition.

**Conditioning (critical):**
```
P(E1 | C10 concern)           = 0.35
P(E1 | C10) unconditional   ≈ P(C10 concern) × 0.35 ≈ 0.15–0.22  (if parent P≈0.50)
E1 + E2 + E3 + E4             = 1.00  (mutex_group: whistleblower_variant)
P(E1 ∨ E2 ∨ E3 | C10)         = 0.63  (public leak mass)
```

YAML `p_cumulative: 0.35` is **conditional** on `ev_c10_internal_concern` — not a calendar unconditional draw.

## Why

- Precedent density ↑: Kokotajlo (2024-04), Saunders (2024-06), Leike (2024-05), Right to Warn (2024-06) — memo/testimony-shaped leaks **normalized**
- Costly signal infrastructure: AIWI, Right to Warn, SEC NDA scrutiny post-Kokotajlo ($2M sacrifice)
- Without C10: 2024 arc had **zero** training pause despite TIME cover — scales to GAAIA/hearings at C10, still **modal** not tail-gov (0.58)
- Caps below 0.50: labs preempt with managed disclosure (E4); Anthropic RSI (2026-06) template
- Safety pipeline "structurally homeless" post-Sharma (2026) → exit-or-leak more common than stay-and-fix

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` §7 — P(E1)=**0.35**; §6 conditioning; §12 modal 0.58
- `docs/research/reference/05_crux_registry.md` — EV-E1–E3 cluster; CX-NO-PAUSE 0.88
- `docs/research/supplements/ai_pause_advocacy_playbook.md` §3.1 — Kokotajlo / Right to Warn; §1.2 pause dead federally
- Saunders Senate testimony Jun 2024 — ~2 mo internal decision → Congress (public record)
- [Apollo Research — Frontier Models are Capable of In-context Scheming](https://www.apolloresearch.ai/) (2024-12)
- `docs/research/spine/node4_evidence_rationale.md` §30 — Saunders analogue: transparency, not pause

## Analogue

Saunders 2024 — TIME + congressional testimony → SB-53 **transparency**, not pause. Pentagon Papers — rare but structural when capability × stakes × insider pool large.

## Would update if

- C10 slips past 2030 → shift window right; keep conditional 0.35
- Controlled disclosure at C10 preempts leak → E1 mass shifts to E4 (0.37)
- ≥2 frontier labs **public halt >90 days** post-memo → falsifies node4 modal (0.58)
- Federal binding training FLOP cap signed → falsifies CX-NO-PAUSE

## Conf

**medium** on conditional 0.35; **low** on unconditional calendar mapping if C10 parent not modeled separately

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `mutex_group` | `whistleblower_variant` | E1∨E2∨E3∨E4 partition — **aligned** |
| `requires_unlock` | true (via `ev_c10_internal_concern`) | Correct gating chain |
| `schedule.start` / `end` | 2029-01-01 → 2031-12-31 | **Later** than node4 tracker 2028 Q2–Q3 — **[CALIBRATE]** consider 2028-07-01 |
| `schedule.p_cumulative` | **0.35** | **Conditional** P(E1\|C10) — aligned if parent gates; overstates if unconditional |
| `on_fire.add_vars.public_xrisk_salience` | +0.20 | 6–10 week media cycle (node4 §20) |
| `on_fire.modify_hazard` | `ev_federal_pause_attempt_fails` ×1.3; `ev_no_pause_2028` ×1.1 | Modal: scandal → failed pause, not halt |

**Calibration:** With `ev_c10_internal_concern` P≈0.50, sim fraction firing E1 ≈ **0.15–0.18** unconditional, not 0.35.
