---
event_id: ev_federal_pause_succeeds
category: governance
conf: medium
port_status: done
source_node: node1 / crux / playbook
research_ref: docs/research/spine/node1_evidence_rationale.md
p_cumulative: 0.08
---

# ev_federal_pause_succeeds — Durable federal training pause enacted (>90 days)

## Observable

Binding federal statute or executive order caps frontier **training** FLOPs/compute for **≥90 days** at **≥2 major labs** — durable training pause, not voluntary rhetoric or export gating alone.

## Claim

**P ≈ 0.05–0.12** (YAML **0.08**) for durable federal training pause before 2030 — governance **right tail**. Mutex with `ev_no_pause_2028` (P≈0.88 no-pause through 2028); joint exhausts pause_outcome group.

## Why

- CX-NO-PAUSE **0.88** (0.83–0.93) — modal = no effective federal training pause through 2028
- Node 1 P(federal binding training FLOP cap | labor shock) **<0.05** — distinct from alignment scare
- Node 1 P(cross-ideological pause coalition tail) = **0.10** — requires C10 + live incident (Trigger E3)
- Node 4 P(halt | whistleblower modal) ≈ **0.08** — Saunders 2024: transparency, not pause
- Playbook §1.2: federal mandatory pause **dead**; culture-war coalition = vetting not halt
- Cruz moratorium stripped **99–1**; FLI pause letter (2023) **zero policy effect**
- Anthropic conditional pause = rhetoric requiring multilateral verification that **does not exist**

## Evidence

- `docs/research/reference/05_crux_registry.md` — CX-NO-PAUSE **0.88**; falsifier = ≥2 labs halt >90d post-leak
- `docs/research/spine/node1_evidence_rationale.md` §P=0.10 — cross-ideological pause coalition tail
- `docs/research/spine/node4_evidence_rationale.md` §12 — modal 0.58 given E: continue training
- `docs/research/supplements/ai_pause_advocacy_playbook.md` §1.2–1.5 — pause coalition weakness
- `docs/evidence/ev_no_pause_2028.md` — mutex partner; absence-of-event framing

## Analogue

Saunders testimony (2024): maximum salience → SB 53 transparency, **no pause**; OpenAI board crisis (2023) without training halt.

## Would update if

- ≥2 frontier labs **public halt >90 days** post-leak → CX-NO-PAUSE falsified; this event **↑**
- Post-whistleblower multilateral pause with verification teeth
- 2028 election → transparency scenario (X5-C) with binding audit statute including training gate

## Conf

**medium** on direction (tail not modal); **medium-high** on magnitude ≤0.12 — well-bounded by no-pause 0.88

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2027-06-01 → 2029-12-31 | Post-C4 / pre-2030 window |
| `p_cumulative` | **0.08** | **Aligned** — right tail complement to 0.88 no-pause |
| `mutex_group` | `pause_outcome` | vs `ev_no_pause_2028` |
| `on_fire` | `deployment_pressure` −0.25; locks race paths | Governance success branch |
| `modify_hazard` | misalign extinction ×0.4 | Pause ↓ misalign tail if fires |

**Calibration:** P(pause) + P(no-pause) need not sum to 1.0 globally — different windows; mutex applies within same sim path after gating.
