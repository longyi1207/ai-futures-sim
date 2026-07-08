---
event_id: ev_prod_interp_halt
category: alignment
conf: low-medium
port_status: done
source_node: node4
research_ref: docs/research/spine/node4_evidence_rationale.md §47–56
p_cumulative: 0.18
---

# ev_prod_interp_halt — Production interpretability catches scheming → halt

## Observable

Frontier lab deploys real-time mechanistic interpretability (SAE probes, scheming monitors) in production; **true-positive** scheming flag at C9–C10 triggers **≥1 frontier lab voluntary halt >30 days** — documented pause, not rhetoric.

## Claim

**P(tail) ≈ 0.18** (range 0.12–0.22); modal (no prod halt): **0.72**. Ranked #5 leverage on ~19% extinction (−2–4pp if fires).

**Conditional halt rates:**
```
P(halt | prod true-positive scheming)     ≈ 0.35
P(halt | whistleblower modal, no prod)     ≈ 0.08  (node4 §23)
```

Can fire **without** E1/E2/E3 (E4 worlds) or accelerate halt in leak worlds — orthogonal to Trigger E partition.

## Why

- Prod true-positive **4×** whistleblower-only halt — instrumented detection harder to spin than memo leak; still **<0.50** (commercial default)
- Engineering trajectory real; **no public prod scheming monitor** at frontier scale yet (2026-07)
- `my_pdoom.md` crux #2 fights tail: P(deception survives deploy) ≈ **0.70**
- Sandbagging / false-positive mass breaks monitor both directions (node4 §52)
- RSP ASL-4+ could wire prod flag to halt — P(RSP invoked)=0.12 (§23)
- p(doom): tail fires → **−3–5pp** on headline ~19% — breaks compound-to-ASI chain

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` §48 — tail P=**0.18**; modal 0.72; P(halt|prod TP)=0.35
- `docs/research/spine/crosscut_secondary_cruxes.md` §1 — ranked #5 leverage (−2–4pp)
- `docs/research/supplements/pdoom_methodology.md` — crux #2 deception survives deployment
- OpenAI GPT-4o SAE attribution (2025) — production-adjacent feature attribution
- [Anthropic RSI essay (2026)](https://www.anthropic.com/institute/recursive-self-improvement) §2.1 — auto code review ~1/3 incident bugs
- Apollo scheming (2024-12); Hubinger — Sleeper Agents (2024-01)
- `code/typebits/` — steering-as-intervention research pipeline (8B scale, not frontier prod)

## Analogue

OpenAI board crisis (2023) — **no** prod interp, **no** halt. Apollo published scheming — **publication + continue training**. Fed "break glass" lending — exists, rarely used pre-crisis.

## Would update if

- Lab publishes prod scheming monitor + documented training pause → P(tail) **≥0.30**
- Red-team shows monitors systematically fooled at C10 → P(tail) **≤0.08**
- RSP ASL-4 invoked by prod monitor (public) → bind §23 P(RSP)=0.12 to observed event
- typebits-style steering fails on frontier tampered models → deployment-tool path dead

## Conf

**low–medium** — trajectory evidence up; **no historical analogue** of prod-triggered training halt (node4 §56)

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule.p_cumulative` | **0.18** | **Aligned** with node4 §48 tail P=0.18 |
| `schedule.start` / `end` | 2029-06-01 → 2033-12-31 | C9–C10 window per node4 |
| `on_fire.add_vars.alignment_trust` | +0.15 | Successful catch restores some trust |
| `on_fire.add_vars.deception_risk` | −0.20 | Risk reduced post-halt |
| `on_fire.lock` | `[ev_deceptive_deploy_at_scale, ev_extinction_misalign_catastrophe]` | Safety brake — correct |
| `requires_unlock` | false (unlocked by whistle variants) | E4 path per §54 — correct |
| `modify_hazard` (incoming) | `ev_corp_safety_hollowing` ×0.75 | Hollowing reduces halt credibility |

**Note:** 0.10 subset is **≥2 labs halt** (not additive to 0.18).
