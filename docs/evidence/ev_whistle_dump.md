---
event_id: ev_whistle_dump
category: alignment
conf: low-medium
port_status: done
source_node: node4
research_ref: docs/research/spine/node4_evidence_rationale.md §8
p_cumulative: 0.20
---

# ev_whistle_dump — Eval dump showing scheming

## Observable

Partial eval logs, red-team video, or interpretability probe output leaked to press or public — higher visceral impact than prose memo. May trigger FBI/natsec response if C10 evals are SCI/SAP-adjacent.

## Claim

**P(E2 | C10 internal concern) = 0.20** (range 0.15–0.25) — second leak variant; lower than E1 due to access/legal bottlenecks, higher tail overlap with E3 when dump shows **imminent** harm.

**Conditioning (critical):**
```
P(E2 | C10 concern)           = 0.20
P(E2 | C10) unconditional   ≈ P(C10 concern) × 0.20 ≈ 0.08–0.12  (if parent P≈0.50)
E1 + E2 + E3 + E4             = 1.00
P(E2 | public leak)           = 0.20 / 0.63 ≈ 0.32  (renormalized among leak paths)
```

## Why

- Impact if leaked ↑: video/logs harder to dismiss than memo; shifts tail-incident branch (node4 §14, P≈0.10)
- Difficulty ↓: smaller access circle; C10 evals likely **SCI/SAP-adjacent** — CFAA/espionage risk
- No full eval dump at frontier yet — Apollo paper is **published**, not leaked
- Whistleblower may prefer **narrative control** (E1) over raw dump that triggers discussion shutdown
- Radicalized insider tail: post-Balaji narrative raises E2 toward **0.30** in tail scenarios
- E2 dump showing imminent harm contributes ~half of tail-incident branch mass (node4 §14)

## Evidence

- `docs/research/spine/node4_evidence_rationale.md` §8 — P(E2)=**0.20**; §11 partition 0.63 public leak
- `docs/research/spine/node4_evidence_rationale.md` §14 — tail-incident 0.10; E2/E3 overlap
- [Apollo Research — Frontier Models are Capable of In-context Scheming](https://www.apolloresearch.ai/) (2024-12)
- Hubinger et al. — Sleeper Agents (2024-01) — backdoors survive training; eval artifacts sensitive
- `docs/research/spine/node4_evidence_rationale.md` §13 — tail-gov 0.15 concentrated in E2/E3

## Analogue

No direct frontier analogue — Snowden/Pentagon Papers class rare. Apollo publication = **voluntary** disclosure template, not leak. WikiLeaks collateral: raw dump can **backfire** on whistleblower narrative control.

## Would update if

- First full eval dump at frontier with documented policy effect → dominant calibration event; revise E2 up
- C10 evals uniformly classified with criminal prosecution → E2 **≤0.10**
- Radicalized insider post-public scare → E2 tail rises toward 0.30
- E2 dump + prod scheming confirm → joint P(halt) highest (node4 §991)

## Conf

**low–medium** — few direct analogues (node4 §8 confidence L–M)

## YAML mapping

| Field | Value | Evidence vs YAML |
|-------|-------|------------------|
| `mutex_group` | `whistleblower_variant` | Correct — competes with E1/E3/E4 |
| `schedule.p_cumulative` | **0.20** | Matches **conditional** P(E2\|C10) |
| `on_fire.add_vars.deception_risk` | +0.15 | Visceral evidence raises perceived deception |
| `on_fire.unlock` | `[ev_prod_interp_halt]` | Dump may force prod monitoring escalation — plausible |
| `schedule.start` / `end` | 2029-01-01 → 2031-12-31 | Same calendar lag note as E1 — **[CALIBRATE]** |

**Calibration:** Unconditional suggest **~0.08–0.12** unless `ev_c10_internal_concern` gates hazard.
