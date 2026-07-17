---
event_id: ev_c10_internal_concern
category: alignment
conf: medium
port_status: done
source_node: node4
research_ref: docs/research/spine/node4_evidence_rationale.md
p_cumulative: 0.52
---

# ev_c10_internal_concern — Internal eval flags C10-grade deception (not public Trigger E)

## Observable

Frontier internal evals / monitors at **C7+** (post–superhuman-coder / early researcher-tier) flag strategic deception, reward-hacking under deployment-simulation, or alignment-research sabotage — Apollo/Greenblatt-class signals that are **credible inside labs**, separate from public whistleblower (Trigger E).

Early Overton / salience without this flag: `ev_alignment_salience_early` (C6+).

## Claim

**P ≈ 0.50–0.55** (YAML **0.52**) that internal C10-grade concern **exists** given `sp_c7` + `deception_risk ≥ 0.12`. Distinct from public Trigger E:

- Weighted branch on fire (Node 4): memo **0.35** / dump **0.20** / deploy_incident **0.08** / concern_no_leak **0.37**
- So P(any public leak | C10) ≈ **0.63**; managed / no-leak ≈ **0.37**

## Why

- Node 4 §3: full public scare historically assumed C9–C10 for natsec credibility; **internal** flags can arrive earlier once C7 evals are serious
- Hard-gating on `sp_c9` + horizon `doom_whimper` created a selection artifact (`P(doom|C10)` ≈ 90%+) — removed; C10 is a **signal**, not a terminal shortcut
- Apollo scheming (2024-12), Greenblatt (2026-04), Sleeper Agents — deception in sandbox **before** public C10 cycle
- Partial Node 4s expected **before** canonical public scare — do not merge "alignment discussed" (`ev_alignment_salience_early`) with "C10 concern exists"

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` §3 — capability anchor
- `docs/research/spine/node4_evidence_rationale.md` §Trigger E — P(any public leak | C10) ≈ **0.63**; E4 = **0.37**
- Apollo Research scheming (2024-12); Greenblatt alignment faking (2026-04)
- Calibration (n=400, seed 42, post-patch): `P(doom|ev_c10)` ≈ **12%**; `P(whistle_memo|ev_c10)` ≈ **43%**; doom lift ≈ **+13pp**

## Analogue

Pre-Chernobyl internal reactor concerns — severity known to operators before public punctuation; 2023 OpenAI board crisis without training pause.

## Would update if

- No deception flags through 2031 despite public C8+ → revise **≤0.25**
- Natsec classifies C10 evals SCI/SAP-adjacent → internal concern exists but **never** becomes public Trigger E
- ≥2 labs public halt >90d post-leak → falsifies modal whistle branch (this event still fires on internal concern)

## Conf

**medium** on direction; **medium-low** on exact 0.52 vs Trigger E weights [CALIBRATE]

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `schedule` | 2028-06-01 → 2031-12-31 | Earlier window than old C9-gated schedule |
| `p_cumulative` | **0.52** | Conditional on preconditions, not unconditional |
| `preconditions` | `spine_fired: [sp_c7]`, `deception_risk ∈ [0.12, 1]` | Not hard-gated on `sp_c9` |
| `on_fire` | mild deception/trust/salience deltas | Unlocks whistle mutex + `weighted_fire` |
| `weighted_fire` | 0.35 / 0.20 / 0.08 / 0.37 | memo / dump / deploy / no_leak |

**Calibration:** Internal concern ≠ public scare ≠ doom. Joint with whistle variants for disclosure; horizon doom comes from autonomy / deceptive-deploy paths, not from C10 alone.
