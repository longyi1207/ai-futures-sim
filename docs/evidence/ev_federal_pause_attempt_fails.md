---
event_id: ev_federal_pause_attempt_fails
category: governance
conf: medium
port_status: done
source_node: node1 / node4 / playbook
research_ref: docs/research/spine/node1_evidence_rationale.md
p_cumulative: 0.35
---

# ev_federal_pause_attempt_fails — Pause bill advances but fails / watered down

## Observable

Congressional pause or training-cap bill **reaches committee/floor** but fails vote, is stripped, or passes without binding training limits before 2028.

## Claim

**P ≈ 0.30–0.40** (YAML **0.35**) that a **serious pause attempt** occurs and **fails** — distinct from no-attempt (embedded in 0.88 no-pause) and from pause **succeeds** (0.08 tail).

## Why

Post-Trigger E, pause **rhetoric** spikes (Node 4: scandal → failed pause attempt is modal-adjacent). Historical: moratorium amendments proposed and stripped (Cruz 99–1). Whistleblower path increases **attempt** hazard without success. Culture-war vetting (0.62) absorbs energy into transparency bills.

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` — GAAIA passes House P=0.25; pause tail separate
- `docs/research/supplements/ai_pause_advocacy_playbook.md` — FLI letter failed; moratorium stripped
- `docs/research/spine/node1_evidence_rationale.md` — anti-regulation tail +2–3pp no-pause
- Node 4 §12: modal response after E — oversight not halt

## Analogue

2023 FLI pause letter — high attention, zero law. Obamacare repeal votes — serious attempt, fail.

## Would update if

- Binding pause **passes** → `ev_federal_pause_succeeds` instead
- No pause bill introduced through 2028 → lower attempt P, still consistent with 0.88 no-pause

## Conf

**medium** — attempt rate less documented than no-pause crux

## YAML mapping

| Field | Value | Notes |
|-------|-------|-------|
| `p_cumulative` | **0.35** | Mid of 0.30–0.40 attempt band |
| `modify_hazard` | `ev_no_pause_2028` ×1.15 | Failed attempt reinforces no-pause |
| `on_fire` | `public_xrisk_salience` +0.10 | Media cycle without policy win |
