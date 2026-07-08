---
event_id: ev_concern_no_leak
category: alignment
conf: medium
port_status: done
source_node: node4
research_ref: docs/research/spine/node4_evidence_rationale.md §10
p_cumulative: 0.37
---

# ev_concern_no_leak — Internal concern without public whistleblower cycle

## Observable

C10 internal eval concern stays classified or corporate-managed; public sees RSI-style safety blog, voluntary framework update, or "we caught it in eval" narrative — **no** NYT memo cycle, eval dump, or attributed prod harm.

## Claim

**P(E4 | C10 internal concern) = 0.37** (range 0.32–0.42) — **modal single variant** at C10 decision point (highest mass in E1–E4 partition). Same mass as scenario row "No Trigger E" (node4 §16).

**Conditioning (critical):**
```
P(E4 | C10 concern)           = 0.37
P(E1 ∨ E2 ∨ E3 | C10)         = 0.63  (public leak)
E1 + E2 + E3 + E4             = 1.00
P(E4 | C10) unconditional   ≈ P(C10 concern) × 0.37 ≈ 0.16–0.22
P(meaningful slowdown | E4)   ≈ 0.08–0.12  vs 0.12–0.18 whistleblower worlds
```

E4 worlds **skip** §12–15 whistleblower response table — policy track follows capability-driven governance without scandal acceleration.

## Why

- Anthropic RSI (2026-06) preempted whistleblower narrative — corporate-framed warning + conditional pause same month as EO/GAAIA
- Natsec prefers classified channel (Banks letter Jun 2026): eval visibility, anti-NSA-solo, incident reporting
- Lab incentive at revenue peak: managed disclosure **cheaper** than post-leak scramble; Trump EO voluntary review gives official cover
- Insider exhaustion: Sharma "exit not organize" (2026) — leak pipeline may **thin**
- Historical: most OpenAI 2023–2024 concerns did **not** produce eval dumps; Leike tweet yes, full memo no
- GAAIA-like still advances via **capability** not scandal — lower DC urgency

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` §10 — P(E4)=**0.37**; §16 No Trigger E branch
- [Anthropic — When AI builds itself (2026)](https://www.anthropic.com/institute/recursive-self-improvement) — managed salience template (§32)
- `docs/research/spine/node4_evidence_rationale.md` §32 — RSI essay primary evidence for E4
- `docs/research/spine/correlation_matrix.md` — P(corp hollowing) ↔ P(E4 no public leak)
- `docs/research/spine/node11_evidence_rationale.md` §27 — hollowing thins whistleblower pipeline
- `docs/research/spine/node4_evidence_rationale.md` §54 — prod halt can fire **without** public Trigger E

## Analogue

Anthropic RSI (2026-06) — public safety essay + conditional pause rhetoric, **no** NYT memo cycle. Most 2023–2024 OpenAI internal concerns — Leike tweet yes, full memo no.

## Would update if

- Mandatory C10 incident reporting with teeth (SB 53 + federal) → E4 **↓**, E1 **↑**
- Second Kokotajlo-scale leak at C10 → E4 mass shifts to E1/E2
- Prod scheming halt **without** public Trigger E → E4 can still produce halt — decouples paths
- Managed disclosure fails (second leak within 6 mo) → E4 **≤0.25**

## Conf

**medium** — Anthropic RSI is live template; C10 timing uncertain (node4 §10 confidence M)

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `mutex_group` | `whistleblower_variant` | E4 competes with E1–E3 — **aligned** |
| `schedule.p_cumulative` | **0.37** | **Aligned** with P(E4\|C10) |
| `on_fire.modify_hazard.ev_no_pause_2028` | ×1.2 | No scandal brake → race continues — coherent |
| No `add_vars` salience spike | — | Correct — **lower** public salience than leak paths |
| `requires_unlock` | true (via C10 concern) | Correct gating |

**Calibration:** Conditional **0.37** correct. Unconditional **~0.16–0.22**. E4 worlds can reach `ev_prod_interp_halt` without public cycle.
