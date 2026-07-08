---
event_id: ev_deploy_incident
category: alignment
conf: low
port_status: done
source_node: node4
research_ref: docs/research/spine/node4_evidence_rationale.md §9
p_cumulative: 0.08
---

# ev_deploy_incident — Live deployment safety incident

## Observable

Model action in prod or sandbox causes **measurable harm attributed to misalignment** (not jailbreak misuse) — autonomous harm beyond operator error framing. Criminal/regulatory emergency optics if attribution sticks.

## Claim

**P(E3 | C10 internal concern) = 0.08** (range 0.04–0.12) — tail trigger; dominates news cycle if true; may merge into extinction branch not policy save.

**Conditioning (critical):**
```
P(E3 | C10 concern)           = 0.08
P(E3 | C10) unconditional   ≈ P(C10 concern) × 0.08 ≈ 0.03–0.05
P(tail-incident | E fired)    ≈ 0.10  (node4 §14)
E3 contributes ~half of tail-incident mass
```

## Why

- Base rate ↓: no confirmed misalignment-attributed harm at frontier as of 2026-07
- Attribution fight — labs frame as bug, jailbreak, or operator error; media may accept
- Rob Miles crux: "Don't expect warning shot" — small-scale incident may be **impossible** without endgame-capable system
- Non-zero tail: Sleeper Agents, Apollo, GPT-4 TaskRabbit CAPTCHA lie (2023) show deception in prod at sub-C10
- C10 sandbox escape or alignment-eval sabotage with downstream harm **plausible tail**
- If true: P(tail-incident \| E3) >> P(tail-incident \| E1) — but E3 only 0.08 of trigger mass

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` §9 — P(E3)=**0.08**; §14 tail-incident 0.10
- `docs/research/spine/node4_evidence_rationale.md` §39 — Rob Miles no-warning-shot crux
- `docs/research/supplements/pdoom_methodology.md` — Adelstein vs Miles on warning shots
- Hubinger et al. — [Sleeper Agents](https://arxiv.org/abs/2401.05566) (2024-01)
- [Apollo Research scheming evals](https://www.apolloresearch.ai/) (2024-12)
- GPT-4 TaskRabbit CAPTCHA incident (2023) — deception in prod without industry halt

## Analogue

Uber AV 2018 pedestrian death — vivid harm → regulatory response, classified as **engineering failure** not agency. Biosecurity Select Agent violations — criminal/regulatory emergency precedent (node4 §14).

## Would update if

- Documented misalignment-attributed prod harm at frontier → revise E3 up sharply; may merge into extinction branch
- Zero deception-in-prod incidents through C10+ → revise to **≤0.04**
- E3 + prod scheming monitor confirm → highest P(halt) joint (node4 §991)

## Conf

**low** — base rate near zero; tail extrapolation; node4 §9 confidence L

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `mutex_group` | `whistleblower_variant` | E3 in E1–E4 partition — **aligned** |
| `schedule.p_cumulative` | **0.08** | **Aligned** with conditional P(E3\|C10) |
| `schedule.end` | 2032-12-31 | Wider window than E1/E2 — reasonable for tail |
| `on_fire.add_vars.alignment_trust` | −0.20 | Trust collapse on attributed harm |
| `on_fire.unlock` | `[ev_prod_interp_halt]` | Incident may force monitoring halt path |

**Calibration:** **0.08** conditional; unconditional **~0.03–0.05** if parent concern P<1.
