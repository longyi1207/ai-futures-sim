---
event_id: ev_eu_gpai_binds
category: governance
conf: medium
port_status: done
source_node: node9 / node4
research_ref: docs/research/spine/node9_evidence_rationale.md
p_cumulative: 0.14
---

# ev_eu_gpai_binds — EU GPAI Act binds US frontier labs

## Observable

≥1 US frontier lab **materially constrained** by EU GPAI enforcement (fines, systemic-risk duties, market access) by 2028 — compliance filings, adversarial testing, incident reporting.

## Claim

**P ≈ 0.14** (range 0.10–0.20) — CX-EU-BINDS crux. GPAI obligations **in force** from Aug 2025; **binding** globally for EU market access; systemic-risk models (>10²⁵ FLOPs) face toughest duties.

## Why

Brussels effect real but **limited**: labs can segment EU deployment; open-weight exception narrowed for systemic-risk. Node 9: formal enforcement action P **0.40–0.55** by 2028, but **material US lab constraint** lower (**0.14**) — compliance cost not training halt.

## Evidence

- `docs/research/spine/node9_evidence_rationale.md` §9 — P=**0.14**
- `docs/research/reference/05_crux_registry.md` — CX-EU-BINDS **0.14** (0.10–0.20)
- [EC GPAI guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers)
- Node 4 tail-gov: EU licensing branch overlaps

## Analogue

GDPR — compliance overhead, not US industry shutdown.

## Would update if

- First **major fine** on US frontier lab before 2027 → revise **0.20–0.25**
- US federal law **explicitly** blocks EU extraterritorial GPAI → revise **≤0.08**

## Conf

**medium** — enforcement timeline uncertain

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.14** | **Aligned** with crux registry |
| `on_fire` | `international_coord` +0.12; `deployment_pressure` −0.05 | Brake not pause |

## RSI delay assumption `[GUESS]`

- `capability_controls.rsi_delay_days`: **45**

This magnitude is **not independently sourced** — no public data exists on how many days/weeks a governance or disclosure event of this type measurably slows frontier-lab internal R&D velocity (`ai_rd_multiplier` / calendar RSI). It is a relative-ordering judgment call: EU GPAI Code of Practice enforcement binding on frontier labs plausibly costs compliance/legal engineering time proportional to a multi-jurisdiction regulatory response — set comparable to a major internal safety incident (45d), well short of a binding US pause.

The **ordering** across the `rsi_delay_days` cluster (whistle_memo 21d < eu_gpai_binds/whistle_dump 45d < deploy_incident 60d < beneficial_ai_treaty 90d < prod_interp_halt 120d < federal_pause_succeeds 540d) tracks intervention severity/duration and is more defensible than any single absolute value.

**Would update if:** a real-world natural experiment (a lab's public before/after R&D-velocity data following a comparable disclosure, incident, or regulatory bind) becomes available; or if `docs/research/` gains a dedicated crux for RSI-delay magnitude, at which point this should move from `[GUESS]` to a cited estimate with a confidence band, matching the `p_cumulative` sourcing bar in CLAUDE.md.
