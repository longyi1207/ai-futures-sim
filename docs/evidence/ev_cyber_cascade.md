---
event_id: ev_cyber_cascade
category: security
conf: medium
port_status: done
source_node: node8
research_ref: docs/research/spine/node8_evidence_rationale.md
p_cumulative: 0.12
---

# ev_cyber_cascade — AI-enabled cyber/finance cascade (non-extinction)

## Observable

Multi-sector critical-infrastructure cascade ("AI cyber 9/11"): coordinated or tightly-spaced incidents causing **≥2** of {regional grid outage ≥24h, water/treatment unsafe state, financial payment rail disruption ≥48h, transport hub shutdown} with **AI assistance** attributed — severe GDP/governance hit, **non-extinction** (P(kinetic) < 0.03 per Node 8).

## Claim

**P ≈ 0.10–0.15** (YAML **0.12**) for T8-A multi-sector cascade over sim window 2029–2035 with `ci_min: 6`. Node 8 central **0.10** through 2028; extended window + ci gate → **0.12** not 0.18.

## Why

- Node 8 T8-A: joint tail lower than individual sectors — barrier moderate per sector, coordination harder
- Mythos Preview (Apr 2026) + Dragos Monterrey SCADA campaign (Jan 2026) show AI-for-cyber **operational** before C6 anchor
- AI agent velocity breaks human SOC timescales — Bridewell CTEM analysis on disclose-to-exploit collapse
- Colonial Pipeline analogue — single-sector precedent; cascade requires shared vuln or coordination
- Modal state cyber remains espionage-dominant (P=0.82) — T8-A is **tail**, not base rate
- Non-extinction explicit: Node 8 P(kinetic | cyber crisis) **< 0.03**; cyber retaliation preferred over strike

## Evidence

- `docs/research/spine/node8_evidence_rationale.md` §T8-A — P=**0.10** central (through 2028)
- `docs/research/spine/node8_evidence_rationale.md` §P=0.97 — no kinetic war from AI cyber crisis
- `docs/research/spine/node8_evidence_rationale.md` §P=0.30 — salient Trigger E may be **financial** not OT
- https://www.anthropic.com/glasswing — Mythos Preview offensive cyber threshold
- Dragos Monterrey SCADA campaign Jan 2026 — OT targeting live

## Analogue

2003 Northeast blackout cascade — rare multi-sector failure; AI **raises** conditional P on shared-vuln scenarios.

## Would update if

- T8-A before Q4 2026 → salience window model too slow; revise timing down
- 2026–27 multi-sector event occurs → remaining-window P **≥0.20**
- Through Dec 2027, no third-party replication of AI-assisted OT pivot → demote to 2028+

## Conf

**medium** on direction (capability live, cascade tail); **low** on exact 0.18 vs node8 0.10 central [CALIBRATE]

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2029-01-01 → 2035-12-31 | Longer than node8 2028 anchor |
| `p_cumulative` | **0.12** | **Aligned** with T8-A 0.10 + modest window uplift (2026-07 cal) |
| `preconditions` | `ci_min: 6` | Cyber-agent capability gate |
| `on_fire` | `gdp_index` −0.25; `governance_capacity` −0.1 | Severe but recoverable |

**Calibration:** Non-extinction constraint explicit — does not route to extinction terminals directly.
