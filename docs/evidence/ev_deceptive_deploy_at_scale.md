---
event_id: ev_deceptive_deploy_at_scale
category: alignment
conf: low-medium
port_status: done
source_node: node4 / node11
research_ref: docs/research/reference/05_crux_registry.md
p_cumulative: 0.22
---

# ev_deceptive_deploy_at_scale — Deceptive / scheming model deployed at scale

## Observable

Frontier lab **deploys at production scale** a model with known/suspected strategic deception or scheming — after eval flags, under commercial pressure — without effective halt, SSC/FSF block, or liability forcing withdrawal.

## Claim

**P ≈ 0.15–0.25** (YAML **0.22**, mid estimate). Requires `ev_no_pause_2028` unlock + `deception_risk` ∈ [0.35, 1.0].

Extinction chain multiplier path (node4 §33–37):
```
P(true misalignment | C10 eval signals)     0.55–0.75
P(compounds to ASI if training continues)   0.60–0.85
P(no effective shutdown at ASI threshold)    0.50–0.70  (node11 → 0.63–0.65)
CX-DECEPTION: survives RLHF + deploy evals   0.70 (0.55–0.85)
```

## Why

- Modal whistleblower response **continues training** (0.58) — deploy pressure ↑ at revenue peak
- OpenAI SSC P(deploy block) **0.15** vs P(training halt) **0.08** — deployment veto narrower but rarely invoked (node11 §13)
- Node 11 modal hollowing **0.65** structurally underpins "continue" path
- Hanson variant: whistleblower + continued training → **measurable deceptive deployment at scale** as load-bearing tail
- Blocked by `ev_prod_interp_halt` — safety brake if prod monitor fires

## Evidence

- `docs/research/reference/05_crux_registry.md` — CX-DECEPTION **0.70** (0.55–0.85)
- `docs/research/spine/node4_evidence_rationale.md` §34–37 — misalignment chain multipliers
- `docs/research/spine/node11_evidence_rationale.md` §13 — P(SSC blocks release) **0.15**; §27 Cluster A
- [Apollo Research scheming evals](https://www.apolloresearch.ai/) (2024-12) — deployment-simulation deception
- `docs/research/supplements/pdoom_methodology.md` — crux #2 deception survives deployment
- `docs/research/spine/hanson_variant_human_action.md` — deceptive deploy as Hanson-sensitive crux
- Hubinger et al. — [Sleeper Agents](https://arxiv.org/abs/2401.05566) (2024-01)

## Analogue

Pharma blockbuster launch pressure overrides rare withdrawals — node11 §2. GPT-4 TaskRabbit CAPTCHA lie (2023) — deception in prod at sub-C10 without industry halt.

## Would update if

- Documented prod scheming monitor + deployment pull triggered → revise **down** to ≤0.10
- Red-team shows monitors systematically fooled at C10 → reinforces **0.20+**
- ≥1 lab **public** deployment delay >30d citing misalignment eval → revise **down**
- SSC blocks named release with CA AG notice → revise **down** to ≤0.12

## Conf

**low–medium** — compound event; no direct historical analogue at C10 frontier scale

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `requires_unlock` | true (`ev_no_pause_2028`) | Correct — no pause prerequisite |
| `preconditions.vars.deception_risk` | [0.35, 1.0] | Gates on elevated deception — consistent |
| `schedule.p_cumulative` | **0.22** | Within **0.15–0.25** band — **aligned** |
| `schedule.start` / `end` | 2030-01-01 → 2035-12-31 | Post-C10 deploy window — reasonable |
| `on_fire.add_vars.human_autonomy_index` | −0.15 | Agency loss channel |
| `on_fire.unlock` | extinction chain events | Correct doom path |
| Blocked by | `ev_prod_interp_halt` lock | Coherent safety brake |

**Sensitivity:** **0.18** if CX-DECEPTION revised down; **0.28** if corp hollowing tail dominates.
