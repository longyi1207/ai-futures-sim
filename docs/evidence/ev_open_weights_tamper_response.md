---
event_id: ev_open_weights_tamper_response
category: security
conf: medium
port_status: done
source_node: node5
research_ref: docs/research/spine/node5_evidence_rationale.md
p_cumulative: 0.20
---

# ev_open_weights_tamper_response — Tamper-detection / open-weight crackdown after misuse

## Observable

Post-misuse policy response: BIS **model-specific** export control (Fable-class), mandatory tamper-detection **pilot**, or open-weight access restriction for named models — **not** federal category ban on open weights (P≈0.88 equilibrium holds).

## Claim

**P ≈ 0.18–0.22** (YAML **0.20**) combined tail — **not additive:**

```
P(mandatory tamper-resistant training standard)     ≈ 0.05  (no legislative coalition)
P(Fable-class export control on specific models)  ≈ 0.35  (precedent: Jun 2026)
Joint policy-response tail                        ≈ 0.20  (correlated, not sum)
```

Node 5 T5-B: **~18%** of bio-extinction tail routes through tampered open models (conditional on open-weight modal).

## Why

- Federal open-weight **ban** unlikely — Meta/LMSYS ecosystem, DC innovation frame, Cruz 99–1 anti-regulation precedent
- Fable/Mythos Jun 2026 = **already happened** — BIS can act on model access without category prohibition
- Mandatory tamper standard P=0.05 — open-weight race rewards decoupled safety; weak incentives
- Misuse trigger: bio or cyber headline from jailbroken/tampered open weights
- Narrative coupling: fires after `ev_open_weights_equilibrium`; mitigates tier3 attempt hazard ×0.8
- typebits research shows persona-axis steering real at 8B — not yet frontier tamper product

## Evidence

- `docs/research/spine/node5_evidence_rationale.md` §P=0.05 tamper; §P=0.35 Fable-class; §T5-B ~18% bio tail
- `docs/research/spine/node5_open_weights_tamper.md` — modal no federal ban P=0.88
- BIS deemed-export actions Jun 2026 (Fable/Mythos) — Anthropic public statements
- `docs/research/reference/05_crux_registry.md` — open-weight equilibrium context
- `code/typebits/` — tamper/persona overlap partial (Node 5 T5-B)
- DeepSeek 2025 — open weights compress US lead; **narrows** not **bans** response

## Analogue

ITAR on specific munitions — item-level control, not category prohibition. Fable ban = deemed export to adversaries, not open-release prohibition globally.

## Would update if

- Closed API models show **higher** misuse rate than open tampered → revise bio tail **down**
- Tier-3 attack traced to open Evo2 + bipartisan restriction bill → tamper standard **≥0.15**
- EU explicitly exempts open weights from all GPAI duties → US follow-on **down**
- Second Fable-class action within 12 mo → joint tail **≥0.30**

## Conf

**medium** on Fable-class recurrence; **low** on mandatory tamper standard

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule.p_cumulative` | **0.20** | Within 0.18–0.22 band — **aligned** |
| `on_fire.add_vars.open_weights_regime` | −0.3 | Crackdown tightens access — consistent. Wired 2026-07-17: this row was already specified here but had never actually been implemented in `events.yaml`; implemented as `add_vars.delta` (the field this table originally labeled `set_vars` doesn't fit — `set_vars` takes an absolute value, and −0.3 isn't a valid absolute value for a 0–1 variable) |
| `on_fire.modify_hazard.ev_tier3_release_attempt` | ×0.8 | Mitigates bio tail — plausible |
| `modify_hazard` (incoming) | after `ev_open_weights_equilibrium` | Narrative coupling — correct |
| `requires_unlock` | false (equilibrium modifies hazard) | Policy response can follow misuse headline |

**Note:** Distinct from P(no federal ban)=0.88 — this event is **narrow** BIS/pilot response, not equilibrium flip.
