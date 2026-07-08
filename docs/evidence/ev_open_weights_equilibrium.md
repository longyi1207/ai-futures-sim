---
event_id: ev_open_weights_equilibrium
category: security
conf: medium
port_status: done
source_node: node5
research_ref: docs/research/spine/node5_evidence_rationale.md
p_cumulative: 0.45
---

# ev_open_weights_equilibrium — Open-weights frontier equilibrium persists

## Observable

No US **federal ban** on open frontier weights through 2029; Meta/LMSYS ecosystem continues releases; EU GPAI documentation duties bind but **weights release persists**; Fable-class export controls remain model-specific, not category ban.

## Claim

**P ≈ 0.40–0.50** (YAML **0.45**) that open-weights **equilibrium under pressure** persists through 2029 sim window — distinct from Node 5 P(no federal ban by 2028) = **0.88**. Equilibrium = ban absent **plus** continued release **plus** no post-incident licensing regime (T5-A P=0.12).

## Why

- Node 5 P=0.88 no federal ban by 2028 — DC "innovation + China competition" frame; Cruz 99–1 anti-state-ban precedent
- Trump EO 14409 pro-deployment; Fable targets **deemed export** to adversaries, not open release generally
- EU AI Act GPAI duties (P=0.55) = documentation, not weight confiscation
- Fable-class export on specific models (P=0.35) — precedent exists but narrow, not equilibrium-breaker
- DeepSeek/Meta open-weights PR maintains race equilibrium; tamper-response tail (`ev_open_weights_tamper_response` P=0.20) pressures but doesn't collapse
- Structural safety–capability coupling at frontier remains weak (P=0.15) — decoupled safety incentives persist

## Evidence

- `docs/research/spine/node5_evidence_rationale.md` §P=0.88 — no federal open-weight ban by 2028
- `docs/research/spine/node5_evidence_rationale.md` §P=0.55 — EU GPAI documentation duties
- `docs/research/spine/node5_evidence_rationale.md` §P=0.35 — Fable-class export control precedent
- `docs/research/spine/node5_evidence_rationale.md` §T5-A — post-incident licensing P=**0.12**
- `docs/research/supplements/ai_pause_advocacy_playbook.md` §1.2 — federal ban less likely than training cap

## Analogue

Encryption export controls (1990s) — narrowed over time, never banned open crypto research; Linux vs proprietary OS coexistence.

## Would update if

- Bipartisan bill banning >X param open release with industry split (not just Anthropic/Google)
- EU explicitly exempts open weights from **all** GPAI duties → equilibrium **↑**
- High-profile tampered-open-model bio attack → `ev_open_weights_tamper_response` fires, equilibrium breaks

## Conf

**medium** on direction (no ban modal); **medium-low** on 0.45 vs node5 0.88 [CALIBRATE] — sim encodes **equilibrium under pressure**, not pure ban absence

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2027-01-01 → 2029-12-31 | Extended vs 2028 ban-horizon |
| `p_cumulative` | **0.45** | **[CALIBRATE]** — composite of 0.88 ban-absence × release persistence × no licensing |
| `on_fire` | `bio_risk_pressure` +0.08; tamper hazard modifier | Open-weight misuse channel |
| `modify_hazard` | weight_theft ×1.15 | Diffusion enables theft tail |

**Calibration:** Joint with `ev_open_weights_tamper_response` (0.20) — not mutex; tamper is post-equilibrium-break path.
