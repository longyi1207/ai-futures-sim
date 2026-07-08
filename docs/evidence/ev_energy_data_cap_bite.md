---
event_id: ev_energy_data_cap_bite
category: economy
conf: medium
port_status: done
source_node: crosscut_physical_economy
research_ref: docs/research/spine/crosscut_physical_economy_limits.md
p_cumulative: 0.30
---

# ev_energy_data_cap_bite — Energy / data sovereignty caps bite on scaling

## Observable

Material binding constraint measurably slows frontier training: **(a)** grid/interconnection delay **>3 mo** or **>15%** cost increase; **(b)** high-quality text/data wall forces synthetic pivot with documented quality regression; **(c)** data-sovereignty rules block cross-border training data — any one sufficient.

## Claim

**P ≈ 0.28–0.35** (YAML **0.30**) that ≥1 cap **bites** 2028–2032. S2 energy-hard-cap tail **0.15**; data-wall modal absorbed but sovereignty adds margin; composite **~0.30**.

## Why

- `crosscut_physical_economy_limits` S2: energy-hard-cap **0.15** — Ci **0.5–0.7×** 2027–2030 if binding
- S1 modal **0.55** — DC load 42→95 GW trajectory; NIMBY pipeline shrink
- Epoch data limits — compute-optimal run up to ~5×10²⁸ FLOP **limited by data not compute**
- Synthetic pivot trades data scarcity for **power** scarcity — net Ci effect ambiguous
- IEA: datacenter demand 485→950 TWh 2025–2030

## Evidence

- `docs/research/spine/crosscut_physical_economy_limits.md` — S1/S2 branches; data wall §
- https://epoch.ai/publications/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data
- IEA Energy and AI executive summary (2025–26)
- `docs/research/spine/c8_society_snapshot_by_ci.md` — physical-economy modifier S1 P≈0.55

## Analogue

1970s oil shocks — physical input caps software narrative, not algorithmic ceiling.

## Would update if

- US DC load <45 GW 2028 with >30% cancellations → energy cap **≤0.15**
- Major lab trains 10²⁸+ on synthetic-only with no regression → data wall falsified for frontier

## Conf

**medium** — energy trend strong; data wall timing disputed

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.30** | Composite energy OR data OR sovereignty |
| `on_fire` | `frontier_capex_index` −0.15; `tech_level` growth slowed | Ci 0.75–0.85× fast track |
