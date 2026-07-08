---
event_id: ev_tier3_path_open
category: bio
conf: low-medium
port_status: done
source_node: node2 / node10
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.22
---

# ev_tier3_path_open — Tier-3 design path viable before screening effective

## Observable

**Tier-3** (low-skill viable pathogen design + synthesis evasion) becomes plausible **before** mandatory screening deployed at scale — given Tier-2 live. Not confirmed attack; **path open** = capability + governance gap, not release event.

## Claim

**P ≈ 0.22** (range 0.14–0.30) — CX-TIER3-BEFORE-SCREEN crux. **Conditional on Tier-2 live.**

```
Node 2 TAIL-A branch weight          ~0.20
Node 10 (hidden near-miss modal)     0.22–0.28 under suppression
Crux threshold: P(T3 before screen | T2) > ~0.15 → bio bucket dominates Adelstein split
```

## Why

- Evo2/GeneBreaker scaling; DBTL automation lowers skill floor toward Tier-3
- Non-IGSC vendors; OSTP 50bp delay (EO 14292 limbo) — screening lag structural
- **Not confirmed** as of 2026-07 — skilled-actor Tier-2 live, Tier-3 is **extrapolation**
- BMIA pass cuts hazard ×0.45; S2 paralysis ×1.15–1.25 on Tier-3-before-screening
- Hidden near-miss ratio 3:1–8:1 (node10 M10) → BMIA coalition slow → gap widens
- Unlocks `ev_tier3_release_attempt` — bio extinction chain gate

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` — TAIL-A **0.20**; crux >0.15 threshold
- `docs/research/spine/node10_disclosure_gap.md` — P(T3 before screen | T2) **0.22** (0.15/0.28)
- `docs/research/reference/05_crux_registry.md` — CX-TIER3-BEFORE-SCREEN **0.22** (0.14–0.30)
- [GeneBreaker — arxiv:2505.23839](https://arxiv.org/abs/2505.23839)
- [RAND RBA4087-1](https://www.rand.org/pubs/research_briefs/RBA4087-1.html)
- `docs/research/supplements/biosecurity_evo_dual_use.md` §3.3
- `docs/research/supplements/node2_cbrn_full.md` §TAIL-A

## Analogue

Aum Shinrikyo — small group, high skill; Tier-3 tail asks if skill floor drops further. AlphaFold3 gating — ~18 mo delay without stopping misuse research.

## Would update if

- Documented Tier-3 low-skill attack → reweight TAIL-A up, lower MODAL branch
- BMIA signed + IGSC v4 function-based SOC → revise to **≤0.12**
- FBI/CDC confirms AI-assisted synthesis from non-expert → Tier-3 **confirmed**, not just path open
- `ev_bmia_pass` fires → apply ×0.45 modifier in sim

## Conf

**low** on exact P (extrapolation from Tier-2); **medium-high** on direction (screening lag structural)

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `requires_unlock` | true (`ev_bio_tier2_live`, near-miss branches) | Correct capability gate |
| `preconditions.vars.bio_capability_tier` | [2.0, 3.0] | Tier-2 prerequisite — aligned |
| `schedule.p_cumulative` | **0.22** | **Aligned** with CX-TIER3-BEFORE-SCREEN and node10 |
| `schedule.start` / `end` | 2028-01-01 → 2032-12-31 | TAIL-A window post-Tier-2 — correct |
| `on_fire.set_vars.bio_capability_tier` | 3.0 | Path open = Tier-3 capability |
| `modify_hazard` (incoming) | `ev_bmia_pass` ×0.45; `ev_us_paralysis_s2` ×1.35 | Consistent with crosscut + node2 |

**Calibration:** Under S2-heavy mix, local hazard may feel **0.25–0.28** — partially captured via paralysis multiplier.
