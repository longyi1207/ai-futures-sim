---
event_id: ev_no_pause_2028
category: governance
conf: high
port_status: done
source_node: crosscut_x5 / node1 / node4 / playbook
research_ref: docs/research/spine/crosscut_x5_admin_evidence_rationale.md
p_cumulative: 0.88
---

# ev_no_pause_2028 — No federal training pause through 2028

## Observable

Through 2028-12-31: **no** binding federal statute or executive order capping frontier **training** FLOPs/compute for ≥90 days at ≥2 major labs; training runs continue after Trigger E-class scares.

## Claim

**P ≈ 0.88** (range 0.83–0.93) that there is **no effective federal training pause** through 2028 — CX-NO-PAUSE crux. This is **absence-of-event**: high P means pause **fails** to materialize.

## Why

- Culture-war vetting modal (Node 1): economic + natsec coalitions beat pause camp
- Cruz stripped moratorium **99–1** (Jul 2025); FLI pause letter (2023) **zero policy effect**
- Whistleblower modal (Node 4 P=0.58): oversight + audits, **not** halt — Saunders 2024 precedent
- Anthropic "conditional pause" = rhetoric, not binding commitment
- All four X5 admin scenarios preserve ~88% no-pause (`crosscut_x5` §P=0.88)
- Federal bio-motivated pause alone only **0.05–0.08** (Node 2) — even narrower than general pause

## Evidence

- `docs/research/spine/crosscut_x5_admin_evidence_rationale.md` §P=0.88 — CX-NO-PAUSE X5-stable
- `docs/research/reference/05_crux_registry.md` — CX-NO-PAUSE **0.88** (0.83–0.93)
- `docs/research/supplements/ai_pause_advocacy_playbook.md` §1.5 — screening coalition > pause; conditional pause mainstream
- `docs/research/spine/node1_evidence_rationale.md` — P(federal training cap) <0.05
- `docs/research/spine/node4_evidence_rationale.md` §12 — modal 0.58 given E: continue training
- `docs/research/spine/correlation_matrix.md` — Cluster Race: no-pause ↔ race acceleration

## Analogue

Saunders testimony (2024): maximum salience → SB 53 transparency, **no pause**. Y2K remediation — industry continues under oversight narrative.

## Would update if

- ≥2 frontier labs **public halt >90 days** post-leak (Node 4 falsifier)
- Binding federal training FLOP cap **signed** with enforcement teeth
- `ev_federal_pause_succeeds` fires → mutex excludes this event

## Conf

**high** on direction; **medium** on exact 0.88 vs 0.83–0.93 band

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `schedule` | 2028-01-01 → 2028-12-31 | Tests **by end-2028** — aligns with crux horizon |
| `p_cumulative` | **0.88** | **Aligned** with CX-NO-PAUSE |
| `mutex_group` | `pause_outcome` | vs `ev_federal_pause_succeeds` (P≈0.08 right tail) |
| `on_fire` | unlock race/misalign paths | Modal coordination-failure spine |

**Calibration:** Run 10k sim — fraction with `ev_no_pause_2028` fired should land **0.83–0.93** after gating.
