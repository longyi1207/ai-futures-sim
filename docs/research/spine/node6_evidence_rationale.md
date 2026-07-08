> **Ported from:** `notes/timeline_prediction/node6_evidence_rationale.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 6 — GAAIA / Preemption: Evidence Rationale

> **Parent:** [`node6_gaia_preemption.md`](./node6_gaia_preemption.md)

---

### P = 0.12 — GAAIA passes with 3-year state preemption intact

**Claim:** House/Senate passes GAAIA-class bill **including** 3-year preemption of state "model development" rules.

**Why:** Strongest federal safety **text** yet (Jun 2026 draft) but preemption fought same as Cruz moratorium — industry wants one federal rule; states resist. **12%** = tail not modal: Encode + unions + Newsom-style governors historically block pure preemption.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` — GAAIA Jun 4 2026; Cruz stripped 99–1 Jul 2025
- `node1_evidence_rationale.md` §T2 P=0.12 (same event)
- `<!-- private monorepo only -->` §3.4 GAAIA vs SB 53 table
- ~$8.5M Q1 2026 lobbying on preemption (playbook)

**Analogue:** ACA vs state health laws — partial preemption fights took years.

**Would update if:** Bipartisan markup keeps preemption + White House endorsement.

**Conf:** M

---

### P = 0.18 — GAAIA passes, preemption stripped

**Claim:** Federal audit/reporting law passes **without** gutting SB 53/RAISE dev obligations.

**Why:** Compromise path — Banks/Trahan safety text + Wiener/Encode strip preemption (mirrors SB 1047→SB 53 negotiation). More likely than full preemption win.

**Evidence:**
- SB 1047 veto → SB 53 signed (transparency survives, caps die)
- Anthropic endorsed SB 53, criticized heavy-handed caps
- `node4_evidence_rationale.md` GAAIA passes House 0.25 — subset is stripped-preemption pass

**Conf:** M

---

### P = 0.45 — Gridlock; states primary

**Claim:** No federal law by 2028; SB 53 + RAISE enforce as designed.

**Why:** Default US federal dysfunction on tech; Trump EO voluntary framework may satisfy industry **enough** to kill GAAIA urgency. States already moving (SB 53 law, RAISE effective 2027-01-01).

**Evidence:**
- FLI 2023 → zero federal law
- EO 14409 Jun 2026 as federal substitute
- `node2_evidence_rationale.md` RAISE P=0.70 prep

**Conf:** M

---

### P = 0.25 — GAAIA dies; EO-only federal framework

**Claim:** GAAIA fails; Trump-class voluntary review becomes **de facto** federal standard.

**Why:** Industry preference for voluntary + export controls over statutory audits. OpenAI alignment with lighter EO.

**Evidence:**
- Playbook §Trump EO 2026-06 — explicitly not mandatory licensing
- Same-month cluster: EO + GAAIA + Banks letter — EO may satisfy moderate Rs

**Conf:** M

---

### P = 0.55 — Unions + populist right block federal preemption (conditional on GAAIA floor)

**Claim:** If GAAIA reaches floor, **~55%** chance preemption stripped or bill dies (joint with Encode).

**Why:** Jul 2025 Cruz moratorium stripped **99–1** — left + right united against federal ban on **state** AI action. Preemption is different frame but overlapping coalition.

**Evidence:**
- `node1_evidence_rationale.md` anti-preemption 0.55
- Playbook §1.4 coalitions

**Conf:** M

---

### p(doom) — P(no effective pause) +1–3pp if O1

**Claim:** Federal preemption win **increases** P(coordination failure on pause) modestly.

**Why:** Removes state-level "laboratory" for harder rules; centralizes to DC where pause is dead. Does not directly cause extinction.

**Evidence:**
- Cross-node `correlation_matrix.md` — GAAIA ↔ P(no pause)

**Conf:** L–M

---

## Phase 2b — AI-lab-as-state / classified defense stack (crosscut §4)

> **Source:** [`crosscut_secondary_cruxes.md`](./crosscut_secondary_cruxes.md) §4 — ranked **#4** leverage on **19%** extinction (+2–4pp if natsec capture tail).  
> **Parent link:** Extends Node 6 GAAIA/preemption; ties to Node 4 §10 E4 (P=0.37), Trigger E2 classification fight.

### Claim — alignment migrates to classified/natsec channel

Frontier AI governance **migrates to classified/natsec channel**: Palantir/Anduril-style integration, Pentagon deals (xAI Feb 2026), CAISI/Banks visibility demands, NSA vs CAISI turf. **Alignment debates happen in secret** — increasing P(E4), decreasing public Trigger E, increasing **race + modal oversight without halt**.

**Node 6 framing:** GAAIA/EO modal path (§Gridlock 0.45, §EO-only 0.25) assumes **public** federal rulemaking. Classified stack crux says **parallel track** may absorb C10 eval fights — weakening public preemption fight while **hardening** E4 no-leak path.

---

### P(modal / tail) — dual track vs natsec capture vs transparency win

| Outcome | P | Notes | Node 6 / N4 mapping |
|---------|---|-------|---------------------|
| **Modal:** Dual track — public voluntary EO + **classified evals** | **0.60** | Jun 2026 stack (EO 14409, GAAIA, Banks, OpenAI blueprint) | Reinforces §Gridlock 0.45 + EO-only 0.25 **combined** public track |
| **Tail:** **Natsec capture** — alignment classified; public gets sanitized RSI essays only | **0.28** | E4 path amplified | ↑ Node 4 §10 P(E4) from 0.37 — **not independent**; conditional boost |
| **Tail:** **Transparency win** — CAISI public benchmarks + anti-NSA-solo (Banks framing) holds | **0.12** | Encode/state allies | ↓ E4; ↑ Trigger E1/E2 if public benchmarks leak concern |

**Conditional dynamics:**

```
P(public Trigger E | natsec capture tail) << P(public Trigger E | modal dual track)
P(E4 | natsec capture) ≈ 0.50–0.55  (vs baseline 0.37)
P(GAAIA with natsec exempt deployment category) ↑ if capture tail
```

---

### Evidence — xAI, Banks, OpenAI blueprint, AISI→CAISI

| Stream | Detail | p(doom) direction |
|--------|--------|-------------------|
| **xAI Pentagon Grok (Feb 2026)** | "All lawful purposes" — no Anthropic-style safeguards | ↑ race; ↓ public alignment leverage |
| **Banks letter (Jun 2026)** | RSI testing, **unpublished internal models** visibility, CAISI vs NSA | **Natsec hawk**, not pause — visibility not veto |
| **OpenAI blueprint (Jun 2026)** | CAISI mandatory eval, RSI indicators — **visibility not veto**; preemption negotiation | Supports §P=0.18 stripped GAAIA; **not** halt |
| **AISI → CAISI rebrand (Jun 2025)** | Shift from broad societal risk to innovation/natsec | Modal dual-track evidence |
| **Node 4 §10 E4** | Natsec classification **↑** criminal exposure for leakers; managed disclosure cheaper | P(E4)=**0.37** baseline — capture tail pushes higher |
| **Node 3** | Theft crisis → **more** classified evals, **same** P(halt) | Race cluster hot without brake |

**Sources:** `<!-- private monorepo only -->`; `research_RSI_june2026_glossary_and_responses.md`; `research_recursive_self_improvement_SOTA_2026.md` §4.

---

### E4 no-public-leak path — amplified under classified stack

**Mechanism:** When C10 evals move SCI/SAP-adjacent, **E4 becomes cheaper** than E1/E2:

| Factor | Effect on E4 | Evidence |
|--------|--------------|----------|
| Criminal exposure for leakers | ↑ E4 | CFAA/espionage risk on eval dump (Node 4 §8 E2) |
| Managed disclosure substitute | ↑ E4 | Anthropic RSI (2026-06) — corporate-framed warning **same month** as EO/GAAIA |
| Whistleblower pipeline thinning | ↑ E4 | Sharma "exit not organize" (2026) — Node 4 §10 |
| Banks visibility **without** public release | ↑ E4 | Regulators see evals; public sees sanitized summary |
| **No** training halt from classified review | Modal | Classified eval **≠** pause — parallel to Saunders → transparency not compute |

**Quantitative sketch:** Baseline P(E4)=0.37 (Node 4 §10). Under natsec capture tail (P=0.28 of this crux), conditional P(E4 | capture) ≈ **0.50–0.55** — public Trigger E mass shifts to E4.

**Policy consequence for Node 6:** GAAIA **public** audit text may pass (§P=0.18 stripped) while **C10 scheming evals** sit in classified annex — **modal oversight without halt** (Cluster A, `correlation_matrix.md`).

---

### Palantir / Anduril — classified stack and revolving door

**Institutional fusion (not necessarily ideological capture):**

| Entity | Role | Timeline relevance |
|--------|------|-------------------|
| **Palantir** | Data fusion, natsec analytics, classified contracts | Template for **lab-as-state** integration — eval visibility to IC without public leak |
| **Anduril** | Defense AI, autonomous systems, Lattice | **Defense-AI stack** vendor class — competes with frontier labs for **classified** deployment slots |
| **MTS pipeline** | Anduril → Anthropic Applied AI (reported) | Talent revolving door — **institutional fusion** |
| **Alex Bores** | ex-Palantir, RAISE (NY) | State-level vetting **bridge** — public track; different from classified eval |
| **Kevin Zhu / Doom Debates** | CS students avoid Palantir on liberal bias | **Polarized** talent/politics — AI safety coded TESCREAL-left → **right-flank** anti-pause alliance space |

**Natsec capture tail (P=0.28):** Alignment/scheming evals default **SCI/SAP-classified**; public gets RSI essays; **Palantir/Anduril-class** integrators run classified eval pipeline — **not** frontier lab safety team with public veto.

**Counter-tail transparency win (P=0.12):** Banks framing blocks NSA-only lane; CAISI publishes redacted scheming eval summaries — forces Node 4 Trigger E2 **despite** classification fight.

---

### Defense-AI stack — alignment debates in secret

**Claim:** Under natsec capture, **alignment debates happen in secret** — decreasing public Trigger E, increasing **race + modal oversight without halt**.

| Dimension | Public track | Classified / defense-AI track |
|-----------|--------------|-------------------------------|
| Scheming eval results | Sanitized blog (RSI essay class) | Full probes in SAP compartment |
| Halt decision | Conditional pause rhetoric (no verify) | **No** public halt; IC continuity mission |
| Whistleblower Trigger E | E1 memo, E2 dump | **Suppressed** — E4 modal |
| GAAIA / EO | Voluntary review, audit reporting | **Exempt** natsec deployment category (tail risk) |
| Race narrative | "Beat China" public | Classified eval **accelerates** mil deployment without public scare |

**Alignment in secret — p(doom):** Public **cannot** apply political pressure for halt what they cannot see; **↓** P(organized pause); **↑** P(no shutdown at ASI) load-bearing P #6. Whistleblower E2 (eval dump) **despite** classification would shift back to Node 4 tail — low P under capture.

**Interaction Node 2:** Natsec framing **helps** BMIA (physical layer) while **hurting** CBRN eval mandates — split governance (`crosscut_secondary_cruxes.md` §4 links table).

---

### p(doom) direction — natsec capture vs transparency win

| Path | Effect on 19% | Cluster |
|------|---------------|---------|
| **Natsec capture tail** (0.28) | **+2–4pp** | Cluster A — P(no pause), P(E4), P(race post-theft) ↑; public whistleblower ↓ |
| **Modal dual track** (0.60) | **+0–1pp** | Public EO + classified evals — already partially in Node 6 base rates |
| **Transparency win tail** (0.12) | **−1pp** | CAISI public benchmarks; anti-NSA-solo holds |

**Rough:** Natsec capture vs transparency win → **+2–4pp** vs **−1pp** on extinction (`crosscut_secondary_cruxes.md` §4).

**Node 6 O1 preemption interaction:** Capture tail **increases** industry preference for **single federal** classified framework (§P=0.12 full preemption **or** EO-only 0.25) — state vetting labs (SB 53) **bypassed** for natsec deployment category.

---

### Would update if — falsifiers and confirmers

| Observation | Direction |
|-------------|-----------|
| C10 evals **SCI/SAP-classified** by default | **Up (capture)** |
| GAAIA passes with **exempt** natsec deployment category | **Up (capture)** |
| Second frontier lab signs unrestricted classified contract (xAI-class) | **Up (capture)** |
| CAISI publishes **redacted** scheming eval summaries with statutory basis | **Down (transparency)** |
| Banks/OpenAI blueprint **blocks** NSA-only testing lane | **Down (transparency)** |
| Whistleblower E2 (eval dump) **despite** classification | **Down (capture)** → Node 4 tail |

---

### Links to existing nodes

| Node | Link |
|------|------|
| **N4 §10 E4** | P(E4)=0.37; classification ↑ leak cost |
| **N4 §8 E2** | Eval dump — classification fight |
| **N6** | GAAIA O1 preemption; CAISI codification; Trump EO modal |
| **N3** | Export controls + classified evals post-theft |
| **N2** | Natsec helps BMIA physical layer; hurts CBRN eval mandates |
| **`correlation_matrix.md`** | Cluster A acceleration / race |

---

**Phase 2b status (Node 6):** 8 sections appended 2026-07-04. Crosscut §4 — zero omissions.
