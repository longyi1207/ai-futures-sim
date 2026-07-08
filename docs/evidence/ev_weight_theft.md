---
event_id: ev_weight_theft
category: geopolitics
conf: medium
port_status: done
source_node: node3
research_ref: docs/research/spine/node3_evidence_rationale.md §6–8
p_cumulative: 0.25
---

# ev_weight_theft — Frontier weight theft / export-control crisis

## Observable

Salient, DC-visible state-linked weight theft or natsec export-control crisis at **C5+** — public leak, partial exfil discovery, or BIS emergency action. Triggers hardening + guardrails talks, **not** durable training-limit treaty.

## Claim

**P(salient public crisis by ~2030 window) ≈ 0.25–0.35** (YAML **0.25**, conservative end). Distinct from P(attempt):

```
P(attempt | C5+ through 2030)     ≈ 0.55–0.75  (central ~0.65)
P(discovered | successful theft)  ≈ 0.45–0.60
P(salient DC crisis)              ≈ attempt × discovery × salience at C5+
```

AI 2027 Feb heist is **scenario color**, not base forecast — 2-hour full exfil P **~0.05–0.12**.

## Why

- Capability anchor C5+ (~2028 H1 at 0.70× tracker) when gap-closure threatens natsec narrative
- Partial/secrets theft more likely than canonical 2 TB full exfil plot
- Fable/Mythos (Jun 2026) **front-runs** part of theft response via deployment export controls
- Trigger E salience by 2028: E1 public leak **0.15–0.25**; E2 classified selective leak **0.20–0.30**
- Modal response (58%): export ctrl + security spend ↑; tail T3 race acceleration **0.15–0.25**
- Downstream: more classified evals → whistleblower surface (node4 §41)

## Evidence

- `docs/research/spine/node3_evidence_rationale.md` §6–8 — P(attempt), P(discovered), Trigger E table
- [RAND RRA4087-1](https://www.rand.org/pubs/research_reports/RRA4087-1.html) — OC/SL framework; state-actor theft expert prior
- BIS Fable/Mythos deemed-export actions Jun 2026 — export-control precedent
- `docs/research/supplements/us_china_ai_dialogues.md` — Geneva 2024; 2026 guardrails restart
- `docs/research/reference/05_crux_registry.md` — CX-RACE-POST-THEFT conditional on theft
- https://ai-2027.com/ — Security appendix (scenario device, not base rate)

## Analogue

SolarWinds (2020) — espionage → hardening, not industry halt. Manhattan espionage — insider + state actor beats lab opsec. Chip export controls (2022–26) — race frame dominates.

## Would update if

- **Public confirm** of full-weight exfil before 2028 → revise up; compress window start
- C5+ slips past 2029 → delay window; lower near-term `p_cumulative`
- Commerce "no more recalls" policy after Fable → lower salience of **repeat** crisis

## Conf

**medium** on attempt base rate; **low–medium** on exact salient-crisis calendar (hidden espionage)

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule.start` / `end` | 2028-01-01 → 2030-12-31 | Aligns with C5+ ~2028 H1 calendar |
| `preconditions.ci_min` | 5 | Matches node3 C5+ anchor |
| `schedule.p_cumulative` | **0.25** | Within node3 E1 public leak **0.15–0.25 by 2028** — **aligned** |
| `on_fire.add_vars.deployment_pressure` | +0.18 | Modal response continues race |
| `on_fire.add_vars.kinetic_escalation` | +0.10 | T1 kinetic tail P<0.02 executed |
| `on_fire.unlock` | `[ev_race_acceleration, ev_whistle_memo]` | Theft → classified evals → whistleblower surface |

**p_cumulative adjustment:** **0.25** correct for **salient** crisis only. If encoding P(attempt), would need **~0.55–0.65** — current event definition is correct.
