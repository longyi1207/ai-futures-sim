---
event_id: ev_bio_tier2_live
category: bio
conf: medium
port_status: done
source_node: node2
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.75
---

# ev_bio_tier2_live — Tier-2 skilled-actor CBRN uplift live

## Observable

Skilled actors achieve **end-to-end assist** on synthesizable sequences (GeneBreaker-class, WMDP + synthesis pipeline) — Tier 2 **confirmed**, not Tier 3 (low-skill viable). Wet-lab skill + chokepoint evasion still required.

## Claim

**P ≈ 0.70–0.80** (YAML **0.75**) in modal window **2027-01 – 2028-12**, gated on Tier-1 (`ev_bio_tier1_live`).

Timing: Tier 1→2 crossing modal **Aug 2026 – Jun 2027** per node2 §P(timing); YAML window allows tracker lag + one frontier refresh cycle.

## Why

- GeneBreaker ~60% ASR on Evo2-40B; case studies show high DNA/protein similarity to pathogen targets
- Evo2/GeneBreaker scaling + frontier LLM refresh cycles compress Tier 1→2 interval
- RAND: AI remains **assistive** not autonomous designer through ~2027 — Tier 2 = skilled actor + FM/LLM stack
- **Not** low-skill viable — no documented Tier-3 attack as of 2026-07
- Unlocks bio scare, near-miss branches, and `ev_tier3_path_open` — load-bearing for bio extinction bucket
- `ci_min: 4` — C4–C5 capability gate in YAML

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` §P(timing) Tier 1→2; §P(status) Tier 2 emerging→partial
- `docs/research/supplements/node2_cbrn_full.md` — full CBRN tree, branch weights
- `docs/research/supplements/biosecurity_evo_dual_use.md` — Evo2 dual-use scaling
- [GeneBreaker — arxiv:2505.23839](https://arxiv.org/abs/2505.23839)
- [RAND RBA4087-1](https://www.rand.org/pubs/research_briefs/RBA4087-1.html)
- `docs/research/spine/node2_evidence_rationale.md` §MODAL branch 0.55 — Tier-2 futures baseline

## Analogue

Stuxnet-level skill floor — nation/sophisticated actor, not teenager. AlphaFold3 gating debate — ~18 mo delay without stopping misuse research.

## Would update if

- Documented Tier-3 attack → skip to tier 3 path; demote Tier-2 confirmation timing
- GeneBreaker ASR collapse + Arc mitigations → demote to Tier 1 through 2028, lower P to **≤0.55**
- BMIA + IGSC v4 function-based SOC before Tier-2 confirm → regulatory front-run (unlikely)

## Conf

**medium** — timing window judgment; capability direction clearer than calendar

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `requires_unlock` | true (tier1 chain) | Correct |
| `schedule.p_cumulative` | **0.75** | Within 0.70–0.80 — **aligned** |
| `preconditions.ci_min` | 4 | C4–C5 capability gate — consistent |
| `schedule.start` / `end` | 2027-01-01 → 2028-12-31 | Matches node2 timing section |
| `on_fire.set_vars.bio_capability_tier` | 2.0 | Tier 2 confirmed |
| `on_fire.unlock` | scare / near-miss / tier3 path | Bio chain — correct |

**Calibration:** Conditional on tier1; P(Tier 2 \| Tier 1) ≈ 0.75 over window, not P(Tier 2 unconditional).
