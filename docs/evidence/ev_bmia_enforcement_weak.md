---
event_id: ev_bmia_enforcement_weak
category: bio_policy
conf: medium
port_status: done
source_node: node2
research_ref: docs/research/spine/node2_evidence_rationale.md
p_cumulative: 0.25
---

# ev_bmia_enforcement_weak — Weak bio enforcement without full BMIA

## Observable

**Full BMIA does not pass** (`ev_bmia_pass` locked), but bio governance stays **weak**: voluntary frameworks only, gutted substitute bill, phased enforcement delayed >18 mo, or state patchwork without federal teeth.

## Claim

**P ≈ 0.20–0.30** (YAML **0.25**) that the US ends 2029 without **effective** federal mandatory screening — either BMIA fails entirely or passes in name only. **Mutex with `ev_bmia_pass`** via `events_not_fired` precondition.

## Why

- Node 2: BMIA P(pass) **0.45** (2027-12) / **0.60** (2028-06) — complement ≈ **0.40–0.55** no full pass
- EU competitiveness framing waters down Ch. VIII; phased enforcement typical even when adopted
- GAAIA preemption tail **0.25–0.35** weakens RAISE/SB 53 enforcement
- TAIL-B regulatory delay **0.15** after near-miss — overlaps weak enforcement path
- Node 10: hidden near-miss → BMIA delay **0.55** on high-suppression path
- YAML **0.25** = point estimate below raw complement — allows some state-level enforcement (RAISE/SB 53) without counting as "weak"

## Evidence

- `docs/research/spine/node2_evidence_rationale.md` §P=0.45 BMIA; §TAIL-B 0.15; §GAAIA preemption
- `docs/research/spine/node10_evidence_rationale.md` §8 — BMIA delay 0.55 | T10-A
- `docs/research/spine/crosscut_us_governance_capacity.md` — S2 paralysis ×0.70 on BMIA

## Analogue

Post-2001 aviation security — years between incident and mandatory screening ratchet. EU GDPR phased enforcement.

## Would update if

- BMIA **signed with teeth** before Dec 2027 → event locked; `ev_bmia_pass` fires instead
- IGSC voluntary → federal mandate without BMIA → still weak path, revise tier to 1.5 not 1.0

## Conf

**medium**

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.25** | Weak-default path; complement to BMIA pass ~0.45 |
| `preconditions` | `ev_bmia_pass` **not** fired | Mutex with full pass |
| `on_fire` | `bio_governance_tier` → 1.0; `ev_tier3_path_open` ×1.2 | Weak gate → tail risk ↑ |
| `locked_by` | `ev_bmia_pass` on_fire | Full pass locks this event |
