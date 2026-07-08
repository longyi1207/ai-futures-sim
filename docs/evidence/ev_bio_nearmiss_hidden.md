---
event_id: ev_bio_nearmiss_hidden
category: bio
conf: medium
port_status: done
source_node: node10
research_ref: docs/research/spine/node10_evidence_rationale.md
p_cumulative: 0.28
---

# ev_bio_nearmiss_hidden — Tier-2 near-miss stays hidden

## Observable

≥1 Tier-2-class incident (IGSC screening catch, agent-finance error, alignment-eval near-catastrophe, synthesis near-miss) occurs **without** public Trigger E disclosure through the event window — internal containment only.

## Claim

**P ≈ 0.25–0.35** (YAML **0.28**) that a **hidden** near-miss path dominates when Tier-2 is live — hidden:public ratio **>3:1** (Node 10 load-bearing P **0.55**). This event fires the **suppression** branch, not occurrence alone.

## Why

- True near-miss rate **exceeds** public Trigger E by modal **3:1–8:1** (Node 10 §1)
- Branch M10 suppression **0.55**; T10-A high suppression (>10:1) **0.30**
- Public Trigger E | Tier 2 only **0.25–0.35** — if incidents occur, most stay internal
- Natsec capture + market stability + "controlled science" framing (Apollo, Sleeper Agents) suppress headlines
- P(≥1 hidden Tier-2 near-miss | Tier 2 live, 2027) ≈ **0.75** — this event is the **policy-relevant** slice where hidden mass **delays** BMIA salience

## Evidence

- `docs/research/spine/node10_evidence_rationale.md` §2–5 — M10 0.55; hidden:public >3:1 P=**0.55**
- `docs/research/spine/node2_evidence_rationale.md` §Trigger E — public near-miss 0.25–0.35; P(no E) modal 0.40–0.50
- `docs/research/spine/correlation_matrix.md` — Cluster C: hidden near-miss ↔ Tier 3 before screening
- Aviation ASRS analogue — industry knew true rate >> headlines for decades

## Analogue

SolarWinds / Y2K insider response — severity known internally before public punctuation.

## Would update if

- BMIA mandates near-miss reporting **with penalties** + ≥2 public near-misses show no suppression gap → revise **≤0.15**
- FOIA/SB 53 discovery of undisclosed IGSC intercept predating public Trigger E by >12 mo → confirms T10-A, revise **≥0.35**

## Conf

**medium** on direction (suppression default); **medium-low** on exact 0.28 vs node10 0.55 (sim event is narrower — one hidden punctuation path)

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.28** | Conservative vs node10 0.55 — not every hidden near-miss fires this unlock |
| `requires_unlock` | tier2 chain | Gated on `ev_bio_tier2_live` |
| `on_fire` | `ev_bmia_pass` hazard ×0.85; unlock `ev_tier3_path_open` | Hidden → policy delay (Node 10 §8 BMIA delay 0.55 on T10-A) |

**Calibration:** Joint with `ev_bio_nearmiss_disclosed` (0.12) — not mutex; both can reflect different incidents or sequencing.
