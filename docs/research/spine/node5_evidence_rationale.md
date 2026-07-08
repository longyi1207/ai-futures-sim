> **Ported from:** `notes/timeline_prediction/node5_evidence_rationale.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 5 — Open Weights + Tamper: Evidence Rationale

> **Parent:** [`node5_evidence_rationale.md`](node5_evidence_rationale.md)

---

### P = 0.88 — No federal open-weight ban by 2028

**Claim:** US will not criminalize or ban open release of frontier-scale weights by 2028.

**Why:** Meta/LMSYS ecosystem, DC "innovation + China competition" frame, Trump EO 14409 pro-deployment; Fable ban targets **deemed export** to adversaries, not open release generally. Cruz coalition killed **state** regulation ban 99–1 — federal ban on open weights even less likely than training cap.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §1.2–1.3
- `<!-- private monorepo only -->` — export control ≠ open-weight prohibition
- Meta Llama 4 open release strategy (2025–26 industry pattern)
- `node3_evidence_rationale.md` — China open-weights PR (DeepSeek)

**Analogue:** Encryption export controls (1990s) — narrowed, never banned open crypto research.

**Would update if:** Bipartisan bill introduced banning >X param open release with industry split (not just Anthropic/Google).

**Conf:** H

---

### P = 0.55 — Voluntary / regulatory model documentation (EU AI Act GPAI)

**Claim:** Major open models face **documentation + some eval duties** under EU AI Act / codes of practice by 2028.

**Why:** EU AI Act applies to GPAI providers including open; Code of Practice 2025–26; not the same as banning weights.

**Evidence:**
- `node4_evidence_rationale.md` EU enforcement rows
- EU AI Act GPAI obligations (2024–25 framework)

**Would update if:** EU explicitly exempts open weights from all GPAI duties.

**Conf:** M

---

### P = 0.35 — Fable-class export control on specific open models

**Claim:** US uses EAR/deemed-export to restrict **access** to specific frontier models (not ban training open).

**Why:** **Already happened** Jun 2026 Fable/Mythos — precedent for BIS acting on model access. P<0.5 because narrow, model-specific, not category ban.

**Evidence:**
<!-- private monorepo only: - `[private note]` -->
- `node3_evidence_rationale.md` Trigger E2

**Conf:** M–H (precedent exists)

---

### P = 0.15 — Structural safety–capability coupling at frontier

**Claim:** ≥1 major lab ships frontier model where removing safety directions **measurably** hurts MMLU/agent benchmarks, at scale.

**Why:** Your Qwen HarmBench work shows **one Pareto point** (Type-B LoRA) — not yet frontier-wide. Incentives weak: open-weight race rewards decoupled safety. CAIS RepE line is research not product default.

**Evidence:**
- `academia_application/cais_meeting_july2026/05_ai_safety_views.md` — Type-B LoRA
- `code/typebits/` — steering separable from capability on open models
- Arditi et al., "Refusal in Language Models Is Mediated by a Single Direction"

**Would update if:** You or CAIS publish coupling at 70B+ with replication by second lab.

**Conf:** L–M

---

### P = 0.05 — Mandatory tamper-resistant training standard (federal)

**Claim:** Binding US rule that frontier training must pass tamper-resistance eval.

**Why:** No legislative coalition; harder than CBRN screening; Meta opposes. Lower than pause P(<0.05).

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` — pause dead
- Node 1 federal cap <0.05

**Conf:** H (for "very unlikely")

---

### P = 0.18 — T5-B: Open-weight accelerates CBRN/bio tail

**Claim:** Conditional on open-weight modal, **~18%** of bio-extinction tail mass routes through tampered open models (jailbreak + local fine-tune).

**Why:** WMDP unlearning bypass easier on weights you own; correlates Node 2 TAIL-C (arbitrage). Not independent.

**Evidence:**
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.1 jailbreak
- `node2_evidence_rationale.md` TAIL-C
- CUT/WMDP unlearning literature

**Would update if:** Closed API-only models show **higher** misuse rate than open tampered models in incident data.

**Conf:** L–M

---

### P = 0.12 — T5-A: Post-incident weight licensing

**Claim:** **~12%** chance high-profile attack → EU/US **licensing** regime for releases above threshold.

**Why:** Smaller than bio screening coalition; tech industry split (Meta vs Anthropic). EU more likely than US.

**Evidence:**
- SB 1047 veto — hard caps fail
- EU Biotech Act screening path more politically viable than AI weight ban
- `node1_evidence_rationale.md` T3 vetting law 0.08 — similar magnitude

**Conf:** L–M
