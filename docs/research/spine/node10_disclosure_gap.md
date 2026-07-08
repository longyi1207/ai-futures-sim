> **Ported from:** `notes/timeline_prediction/node10_disclosure_gap.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 10 — Hidden Near-Miss / Disclosure Gap

> **Parent:** [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md)  
> **Evidence rationale:** [`node10_evidence_rationale.md`](./node10_evidence_rationale.md)  
> **Correlates:** Node 2 (Trigger E, TAIL-B), Node 4 (E3/E4), Node 6 (SB53 vs GAAIA), Cluster H  
> **Supersedes:** [`crosscut_secondary_cruxes.md`](./crosscut_secondary_cruxes.md) §5  
> **Date:** 2026-07-04

---

## Definition

**Capability C:** Fires when **Tier 2+ bio**, **agent finance**, or **alignment eval** incidents occur at rates **exceeding public Trigger E** — suppressed by NDA, market stability, natsec classification, or "nothingburger" framing.

**Falsifiable claim:** Hidden:public near-miss ratio **>3:1** through 2028 (modal **0.55**); BMIA urgency **underpriced** because policy sees **fewer** punctuating events than reality.

**Core metric:** `hidden:public ratio` = (Tier 2+ incidents with internal containment) / (public Trigger E-class events). Not "labs lie" — **rational suppression** under asymmetric information + liability + natsec.

---

## Stakes

| If modal (M10, 0.55) | If tail (T10-A, 0.30) | If counter-tail (T10-B, 0.15) |
|----------------------|------------------------|--------------------------------|
| Ratio **3:1–8:1**; BMIA coalition **slow** | Ratio **>10:1**; anthropic shadow for governance | Ratio **~1:1**; SB53/RAISE + whistleblower punctuate |
| P(Tier 3 \| Tier 2) **+3–5pp** vs public-rate model | Bio branch weight **20%→24%** in re-stitch | Bio branch **−2pp**; Cluster B fires |
| Trigger E **underfires** → policy **underreacts** | P(BMIA delay \| coalition) **0.55→0.65** | Mandatory reporting **0.25→0.40** by 2028 |
| **+2–4pp** on 19% extinction (modal channel) | **+4–7pp** wrong-way tail | **−2–3pp** if transparency wins |

---

## Branch outcomes

| Branch | P | Conf | One-line |
|--------|---|------|----------|
| **M10: Modal suppression** | **0.55** | M | Ratio 3:1–8:1; internal containment default |
| **T10-A: High suppression (>10:1)** | **0.30** | M | Anthropic shadow for governance; bio tail ↑↑ |
| **T10-B: Transparency works (~1:1)** | **0.15** | L–M | SB53/RAISE + BMIA reporting bite |

**Joint:** P(public learns ≥1 hidden Tier-2-class incident by 2028 \| M10∪T10-A) ≈ **0.35** — leaks, not voluntary disclosure.

---

## Tier taxonomy (crosswalk Node 2)

| Tier | Internal signal | Public Trigger E? | Typical suppression |
|------|-----------------|-------------------|---------------------|
| **T1** | Eval red flag; no deploy | Rarely | Internal only |
| **T2** | Bio catch; agent finance error; alignment process failure | **0.25–0.35** if public | NDA, "resolved", no BMIA hook |
| **T3** | Release / near-release with harm potential | **0.55–0.70** if public | Managed E4 (Node 4) |
| **T4** | Mass harm or extinction-class | ~1.0 if survivable | Post-hoc only |

**Node 10 claim:** **≥75%** of T2-class events **never** reach Trigger E salience — see rationale §12–18.

---

## Time series — disclosure vs suppression (2024–2026)

| Date | Event | Tier (est.) | Public salience | Disclosure channel | Governance effect |
|------|-------|-------------|-----------------|-------------------|-------------------|
| 2024-05 | Leike resigns; superalignment dissolved | T2 (process) | **High** (organizational) | Open letter | **No** BMIA; **no** pause |
| 2024-12 | Apollo scheming paper | T2 (eval) | Medium (research) | Publication | Updates evals; **no** halt |
| 2025-10 | CA AG MOU (OpenAI advance notice) | T1→T2 policy | Low | Regulatory filing | **Paper** duty; untested |
| 2026-02 | Lobstar Wilde stablecoin agent incident | T2 (finance) | **Low–medium** | Niche crypto press | **No** federal Trigger E |
| 2026-03 | Meta agent sev-1 (internal) | T2 (agent) | **Low** (leak-adjacent) | Employee / press fragment | **No** BMIA coalition |
| 2026-04 | Anthropic RSI essay + Trump EO + GAAIA | T2/T3 mix | **High** (managed) | **E4** simultaneous acceleration | **Wrong-way** — speed ↑ |
| 2026-06 | Anthropic CoT training accidents (reported) | T2 (alignment) | Medium | Blog / interview | RSP narrative; **no** halt |
| 2026-07 | Longpre et al. harm-only reporting gaps | T1 meta | Low (research) | arXiv | Supports hidden-rate prior |

**Pattern:** **High-salience organizational** events (Leike) ≠ **high-salience capability-near-miss** events (Lobstar, Meta sev-1). Node 10 tracks the **latter** — where suppression **buys time** for bio/agent paths without punctuating BMIA.

---

## Lab disclosure posture tracker (2026-07)

| Actor | Formal duty | Observed 2024–26 | P(voluntary Tier-2 public disclosure) | Hidden:public prior |
|-------|-------------|------------------|----------------------------------------|---------------------|
| **Anthropic** | RSP incident reporting (ASL-dependent) | RSI essay = **managed** E4 | **0.20** | **4:1–6:1** |
| **OpenAI** | Preparedness + CA AG MOU | Saunders testimony; **no** near-miss catalog | **0.15** | **5:1–8:1** |
| **Google DeepMind** | FSF governance escalation | Product-integrated; sparse public | **0.12** | **6:1–10:1** |
| **Meta** | Weak / open-weight | Llama incidents **internal** | **0.08** | **8:1+** |
| **xAI / defense** | Natsec classification lane | Pentagon deal → **classified stack** (N6) | **0.05** | **>10:1** tail |
| **Regulators (US)** | SB 53 (CA) incident duty | GAAIA **preempts** federal pause narrative | N/A | Feeds **T10-A** |

**Composite frontier hidden:public (modal):** **~5:1** (range 3:1–8:1) — primary input to bio branch reweight in `my_pdoom.md`.

---

## Mechanisms of suppression (why rational, not conspiracy)

| Mechanism | Who benefits | Cost to governance | P(active \| Tier 2) |
|-----------|--------------|-------------------|---------------------|
| **NDA / employment** | Lab liability | Whistleblower pipeline thins (N11) | **0.70** |
| **Market stability** | Public cos | Delay until "contained" narrative | **0.55** |
| **Natsec classification** | DoD partners | Zero public Trigger E | **0.25** (conditional on defense deal) |
| **Managed E4** (Node 4) | Lab + regulator | **Simultaneous** acceleration signal | **0.40** |
| **"Nothingburger" framing** | Media incentive | BMIA coalition lacks punctuating event | **0.45** |

**Anthropic shadow:** Historical base rate of **suppressed** near-catastrophes in other domains (Y2K worked → looks like crying wolf; inverse for **unreported** near-misses) — `research_tech_doomsayers_history_lessons_for_ai.md`.

---

## BMIA / policy link

| Variable | If M10 | If T10-A | If T10-B |
|----------|--------|----------|----------|
| P(BMIA coalition forms by 2028) | **0.45** | **0.30** | **0.60** |
| P(BMIA **delay** \| coalition starts) | **0.50** | **0.65** | **0.35** |
| P(Tier 3 before screening \| Tier 2 live) | **0.22** | **0.28** | **0.15** |

**Channel to 19% extinction:** Bio tail branch **20%** × P(ext\|bio)=**36%** — Node 10 moves **both** weight and conditional via hidden-rate prior.

---

## GAAIA vs SB 53 tension (Node 6 cross-link)

| Policy | Direction on disclosure | Node 10 read |
|--------|----------------------|--------------|
| **SB 53** (CA) | ↑ incident duty to AG | **T10-B** enabler if enforced |
| **GAAIA / federal acceleration** | ↓ pause probability; ↑ classified lane | **T10-A** — federal narrative **outruns** state transparency |
| **P(GAAIA weakens SB53 duty)** | — | **0.35** (point); see rationale §28 |

---

## Correlation Cluster H (do not multiply)

| Partner node | ρ (est.) | Joint failure mode |
|--------------|----------|-------------------|
| N11 corp hollowing | **0.55** | Thin whistleblowers + thick suppression |
| N4 E4 managed disclosure | **0.60** | Public learns **after** acceleration commit |
| N6 natsec capture | **0.45** | Classified stack hides T2 |
| N2 Trigger E underfire | **0.70** | Same metric, different slice |

Full matrix: [`correlation_matrix.md`](./correlation_matrix.md) Cluster H.

---

## Top load-bearing P's

| # | P | Point | Range | Rationale § |
|---|-----|-------|-------|-------------|
| 1 | P(hidden:public ratio >3:1 \| Tier 2 live) | **0.55** | 0.45–0.65 | §12–18 |
| 2 | P(≥1 hidden Tier-2-class near-miss \| Tier 2, 2027) | **0.75** | 0.65–0.85 | §19–22 |
| 3 | P(public Trigger E \| Tier 2 live) | **0.30** | 0.25–0.35 | N2 crosswalk |
| 4 | P(BMIA delay \| high suppression tail) | **0.55** | 0.45–0.65 | §31–34 |
| 5 | P(Tier 3 before screening \| high suppression) | **0.28** | 0.20–0.38 | §35–38 |
| 6 | P(agent finance near-miss hidden \| occurs) | **0.60** | 0.50–0.70 | §24–27 |
| 7 | P(GAAIA preemption weakens SB53 incident duty) | **0.35** | 0.25–0.45 | §28–30 |
| 8 | P(mandatory near-miss reporting by 2028) | **0.25** | 0.15–0.35 | §39–42 |

---

## p(doom) link (Phase 2b stitch)

| Branch | ΔP(extinction) | Channel |
|--------|----------------|---------|
| **M10** | **+2–4pp** vs Phase 4a 18% baseline | Bio branch weight + conditional |
| **T10-A** | **+4–7pp** | Tier 3 before screening; BMIA delay |
| **T10-B** | **−2–3pp** | Punctuation restores Cluster B |

**Headline after re-stitch:** **19%** (15–24%) — Node 10 is **#1 leverage** crux on load-bearing P **#9** (hidden near-miss stays hidden ~55%).

---

## Falsification watchlist (2026–2028)

| Observation | Updates toward |
|-------------|----------------|
| **≥2** voluntary Tier-2 public disclosures by top-4 labs | T10-B ↑; extinction **−2pp** |
| Federal mandatory near-miss registry (not just CA) | T10-B ↑; P(#8) → **0.45+** |
| Leaked catalog shows **<2:1** hidden:public | M10 ↓; bio branch **−2pp** |
| **≥1** hidden bio T2 → public Tier 3 **without** screening gap | T10-A ↓ |
| GAAIA explicitly **preempts** SB53 enforcement in court | T10-A ↑; N6+N10 joint |

---

## Related files

- `node10_evidence_rationale.md` — ~40 Claim/Why/Evidence sections
- `node2_evidence_rationale.md` — Trigger E §0.25–0.35; TAIL-B
- `node4_evidence_rationale.md` — E3/E4 managed disclosure
- `node11_corporate_governance.md` — whistleblower thinning (Cluster H)
- `<!-- private monorepo only -->` — anthropic shadow
<!-- private monorepo only: - `[private note]` — Lobstar Wilde -->
- `../my_pdoom.md` — 19% extinction; load-bearing P #9

---

## Update log

| Date | Change |
|------|--------|
| 2026-07-04 | Phase 2b Node 10 — full node from crosscut §5 expansion |
| 2026-07-04 | Phase 2b polish — stakes, time series, lab tracker, BMIA/GAAIA, Cluster H, falsification |
