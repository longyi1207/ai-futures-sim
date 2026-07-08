> **Ported from:** `notes/research_ai_pause_advocacy_playbook.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Frontier AI Pause / Stop — Policy & Personal Advocacy Playbook

**Created:** 2026-06-01  
**Purpose:** Consolidated reference from research conversation — how to stop frontier AI (policy levers), what individuals and civil society can do, what to follow, and realistic expectations.  
**Related repo notes:** [`research_us_ai_policy_primer_zh.md`](./research_us_ai_policy_primer_zh.md) (**术语与制度入门，中国留学生向**), [`research_international_ai_governance_platforms.md`](./research_international_ai_governance_platforms.md), [`research_us_china_ai_dialogues.md`](./research_us_china_ai_dialogues.md), [`research_why_ai_warnings_dismissed.md`](./research_why_ai_warnings_dismissed.md), [`ai_governance_political_strategy.md`](./ai_governance_political_strategy.md) (**政治学/历史学战略框架**), [`ACX_LessWrong_EA_rationalist_community_map.md`](./ACX_LessWrong_EA_rationalist_community_map.md), [`Anthropic_When_AI_Builds_Itself_2026.md`](./Anthropic_When_AI_Builds_Itself_2026.md)  
**Local readings:** [`readings/ai_policy/`](../readings/ai_policy/README.md)

---

## Executive summary

- **Full stop of frontier AI research** is technically designable (compute chokepoints + law + verification + US–China coordination) but **not politically viable in 2026**. Global governance is moving toward **acceleration + soft safety**, not pause (Paris 2025, US AI Action Plan, sovereign AI / Global South access).
- **Most realistic near-term wins:** state-level transparency → training licensing → compute caps; **blocking federal preemption** of state AI laws (largest active negative lever, ~$8.5M lobbying Q1 2026).
- **Grassroots impact** comes from **specific bills, elections, and institutions** — not more open letters (FLI March 2023 pause letter: 1,000+ signers, **zero policy effect**).
- **Individual leverage:** sustained advocacy (Encode-style), whistleblower/transparency infrastructure, bridging short-term harm ↔ long-term safety coalitions, and **research → legible policy briefs** (not LW discourse).

---

## Part 1 — How governments and frontier labs could stop (policy mechanics)

### 1.1 Clarify the target

| Goal | Controllability | Main levers |
|------|-----------------|-------------|
| **Stop frontier training** (>~10²⁵ FLOP class) | Highest | Chip export, cloud licensing, training permits |
| **Stop frontier deployment** | Medium | Pre-release review, API licensing, product liability |
| **Stop all AI research** | Near-zero | Academic freedom, open weights, algorithmic progress decoupled from compute |

Pause movements realistically target **training chokepoints**, not shutting down all ML.

### 1.2 Government levers

#### A. Compute governance (the only lever with a physical boundary)

**Compute Pause Button** framework (Ramiah et al., arxiv 2506.20530): requires **three legs** — technical, traceability, regulatory. Remove one and the system collapses.

| Leg | Examples |
|-----|----------|
| **Technical** | Tamper-proof FLOP caps, model locking, offline licensing, fixed-set cluster configs |
| **Traceability** | Chip registries, supply-chain monitoring, KYC for large training, digital compute receipts |
| **Regulatory** | Export controls, production caps, licensing above FLOP thresholds |

**Hardware verification taxonomy** (arxiv 2604.04712): treaty-grade verification needs on-chip FLOP metering (M5), proof-of-training (V2), hardware-embedded licensing (E6) — **least mature** mechanisms are those most needed for multilateral treaties.

**US export controls today:** aimed at **containing China**, not global pause. Unilateral pause without China → strategic suicide narrative.

#### B. Domestic legislation (US, 2025–2026 snapshot)

| Development | Outcome |
|-------------|---------|
| **SB 1047 (CA, 2024)** | Vetoed by Newsom; showed path + industry opposition (a16z, Meta, etc.) |
| **SB 53 (CA, 2025+)** | Transparency / safety reporting — **Encode-backed, Anthropic endorsed** |
| **Cruz BBB “AI moratorium” (2025)** | Would have **banned state AI regulation for 10 years** — **stripped 99–1** (July 2025) |
| **Federal direction (Trump 2025–26)** | Rescinded Biden EO 14110; push **preemption** + deregulation; OpenAI “reverse federalism” (win friendly state laws in CA/NY/IL) |
| **Trump EO frontier review (2026-06-02)** | Voluntary 30-day prerelease review for “covered frontier models” (criteria TBD in 60 days); explicitly **not** mandatory licensing |
| **GAAIA discussion draft (2026-06-04)** | Obernolte-Trahan bipartisan House bill: frontier audits + incident reporting + **3-yr state development preemption**; strongest federal safety text yet, preemption fight repeats Cruz dynamic |
| **Banks letter (2026-06-04, Bloomberg 6/5)** | RSI/自动化 AI R&D 须纳入自愿测试；要 CAISI 实质参与（反 NSA 独断）；未发布内部模型 visibility；防中国窃取 + 国安事件报告 — 见 `readings/ai_policy/bloomberg_2026-06-05_banks_ai_oversight.pdf` |

**Harder versions:** criminalize unlicensed frontier training; DPA; treat frontier training as WMD-precursor / public nuisance (Yudkowsky 2026 *Only Law Can Prevent Extinction* — state force, not voluntary commitments).

#### C. Government as buyer

- Cut DoD/IC/DOE contracts to frontier labs  
- Federal procurement ban on models above thresholds  
- **Limits revenue, does not stop** VC + commercial + foreign state buyers

#### D. International treaty (necessary for real full stop)

Minimum architecture:

1. Training FLOP ceiling (frozen or conditional)  
2. Independent verification body (IAEA-like for compute)  
3. Sanctions for violations  
4. **US and China both sign**

**Reality (2026-06-01):** US–China had **one** formal AI government dialogue (Geneva 2024-05-14); no joint statement; 2026 Beijing agreed to **restart** dialogue on **guardrails**, not pause. Global South (India AI Impact 2026) prioritizes **access**, not freeze.

### 1.3 Forcing frontier labs to stop

**Voluntary commitments** (Frontier commitments, Seoul 2024) — **no teeth**.

**Anthropic conditional pause (2026-06-04):** In [*When AI Builds Itself*](https://www.anthropic.com/institute/recursive-self-improvement), Clark + Favaro (Anthropic Institute) say that *if* credible verification systems existed so frontier labs could confirm others had stopped/slowed and no one could defect in secret, Anthropic *expects it would* slow or temporarily pause when other at-or-near-frontier developers did likewise. **Not a binding pledge** — `we expect that we would`, not `we commit to`. Unilateral pause explicitly dismissed as swapping the front-runner. Full parse: [`Anthropic_When_AI_Builds_Itself_2026.md`](./Anthropic_When_AI_Builds_Itself_2026.md). **Glossary + stakeholder responses:** [`research_RSI_june2026_glossary_and_responses.md`](./research_RSI_june2026_glossary_and_responses.md).

| Mechanism | Effect | Leakage |
|-----------|--------|---------|
| Training license + criminal penalties | High for compliant actors | Underground clusters, friendly jurisdictions |
| Cloud provider refusal | High | Sovereign clouds, self-built datacenters |
| Weight seizure / release ban | Medium | Leaked weights, distillation |
| Antitrust breakup | Reduces capacity | Does not directly stop research |
| Key-personnel / export controls on talent | Low–medium | Global talent market |

**Indirect pressure (more politically feasible):** product liability; SEC risk disclosure; whistleblower protection; insurance requiring independent safety audits.

**Internal “strike” / costly signals:** FLI pause letter failed because signatures were **costless**. Effective version needs whistleblowing (AIWI), engineer refusal, institutional boycott — not yet organized at scale.

### 1.4 Political coalitions (who wins / blocks)

| Force | Motivation | vs full stop |
|-------|------------|--------------|
| x-risk / pause camp | Existential risk | Support — politically weak alone |
| AI ethics / labor | Jobs, bias, power | Partial support (UK Seismic: **40% want development stopped**) |
| Populist right (Bannon/Hawley) | Elite experiment, jobs | **Vetting**, not necessarily full pause |
| Big Tech / a16z | Growth | **Anti-pause**, pro preemption |
| Natsec hawks | Beat China | **Strong anti-pause** |
| Global South | Digital sovereignty | **Anti-pause** (want compute access) |

**Winnable coalition (US):** x-risk + labor + populist right + some Democrats → **state-level** training cap / pre-deployment vetting — not overnight moratorium.

**Bridging short-term harm ↔ long-term safety** (Stix & Maas 2023 risk matrix) = most tractable political problem; industry defeats split coalitions (SB 1047 lesson).

### 1.5 Why full stop is harder than conditional pause

1. Algorithmic progress decouples from training FLOPs (test-time compute, distillation)  
2. Open weights — stopping labs ≠ stopping global fine-tuning  
3. Geopolitical race — unilateral pause loses to China narrative  
4. Economic framing — frontier AI = national power + productivity  
5. **Verification window closing** — hardware metering immature; delay makes treaties harder  

**Policy mainstream:** conditional pause at capability thresholds (hard RSP), not permanent full stop.

### 1.6 Staged action path (if pushing toward stop)

**Short (1–2 yr, US)**  
1. CA/NY **training compute cap** bills (narrower than SB 1047)  
2. Join populist-right **vetting** bills; tighten toward ban over time  
3. Federal executive order: **cloud training registration**

**Medium (3–5 yr)**  
4. AISI network: voluntary eval → **release licensing**  
5. R&D: on-chip FLOP metering, proof-of-training  
6. Track II: shift US–China dialogue from guardrails toward **mutual training freeze** (no current sign)

**Long (full stop prerequisites)**  
7. Multilateral compute treaty + verification agency  
8. Hardware-embedded licensing / kill switches  
9. Global advanced-chip **production cap** (TSMC/ASML/US/China/Korea)

Without 7–9, unilateral stop = **unilateral handicap**.

---

## Part 2 — What individuals can do

### 2.1 Realistic expectations

- **Bottleneck is not “more warnings.”** Overton window is already wide (Pew, Seismic, CAIS). Bottleneck = **specific, defensible, implementable policy** + engineering evidence.  
- **Open letters:** awareness only; FLI 2023 pause letter → no law.  
- **Highest negative risk right now:** **federal preemption** of state AI laws — if passed, SB-53-style wins wiped out.

### 2.2 Information diet (what to follow)

**Tier 1 — Legislation (check weekly)**

| Source | Watch for |
|--------|-----------|
| [CA LegInfo](https://leginfo.legislature.ca.gov/) | SB 53, any compute cap / training licensing |
| [The AI Lobby](https://www.theailobby.com/money) | Lobbying spend; preemption bills |
| IAPP / Brookings trackers | Federal EO, AISI, preemption |
| Hawley **GUARD Act**, Blackburn **RESPONSIBLE Act** | Bipartisan vetting / child-safety angles |

**Signal:** bill passes committee, senator flips, preemption in/out of reconciliation — **not** “another AGI warning op-ed.”

**Tier 2 — International (monthly)**

| Source | Watch for |
|--------|-----------|
| Repo: `research_international_ai_governance_platforms.md` | Summit series, UN Global Dialogue (Geneva 2026-07) |
| [CFR AI governance](https://www.cfr.org/articles/the-world-is-trying-to-govern-ai-the-un-wants-in) | Multilateral vs sovereign AI |
| [IDAIS](https://idais.ai/) | Scientist consensus statements |
| BIS / Reuters | Export controls — competition vs global training cap |

**Tier 3 — Industry (monthly)**

- Anthropic **RSP** updates (threshold templates for future law)  
- Frontier lab capex / Stargate / cloud deals (political opposition $)  
- [METR](https://www.metr.org/), UK/US AISI eval reports (capability pace)

**Tier 4 — Public opinion (quarterly)**

- [Pew AI 2025](https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/)  
- [Seismic UK 2025](https://report2025.seismic.org/media/documents/On_the_Razors_Edge_Seismic_Report_2025.pdf) — **40% want development stopped**  
- [Stanford AI Index — Public Opinion](https://hai.stanford.edu/ai-index/2025-ai-index-report/public-opinion)

**Low ROI for policy:** daily LW/Twitter x-risk drama; TESCREAL framing wars (see `research_why_ai_warnings_dismissed.md` Appendix B).

### 2.3 Personal actions by effort tier

#### Tier 0 — ~15 min/week

1. **Encode AI action alerts** — [encodeai.org](https://encodeai.org/)  
2. **Structured letters to legislators** — support specific bill sections; oppose preemption (not vague “stop AI”)  
3. **One issue, consistently** — e.g. “oppose federal preemption + support state training transparency/licensing”

#### Tier 1 — few hours/month

4. Local AI safety / EA / Encode meetups → **mobilizable voter bloc**  
5. **Framing translation** — x-risk → labor / national security / child safety language (avoid “existential risk” in hostile audiences; use “loss of control,” “catastrophic risk,” “severe harm”)  
6. **Public comments** on NIST/FTC/state AG rulemakings — technical comments from CS backgrounds get read

#### Tier 2 — sustained

7. Volunteer: **Encode**, **FLI**, **ControlAI** — policy research, briefs, phone banks  
8. **Whistleblower / transparency:** [AIWI](https://aiwi.org/), Right to Warn — Kokotajlo case showed movement  
9. **Research → 2-page policy brief** for legislators (legible evidence > philosophy)  
10. Expert witness pipeline — contact Encode / bill sponsors for technical testimony

#### Tier 3 — career-level

11. Fellowships: GovAI, AISI, CSET, Apollo  
12. Bridge FAccT/AI Now ↔ x-risk/METR coalitions  
13. Compute governance R&D (verification hardware) — stop is ultimately hardware + treaty problem

### 2.4 Framing cheat sheet (policy audiences)

From `research_why_ai_warnings_dismissed.md` Appendix B:

| Triggers dismissal (TESCREAL-coded) | Safer framings |
|-----------------------------------|----------------|
| “Existential risk,” Bayesian credences, AGI doom | “Catastrophic risk,” “severe harm,” “national security,” “loss of control” |
| Yudkowsky as messenger | Hinton, Bengio, Russell, Encode (youth/student advocates) |
| LW-only vocabulary | Populist right: jobs, unelected elites, vetting before release |

**Messengers hard to dismiss:** Hinton (Nobel), Bengio (LawZero), Encode/Revanur — not CAIS-only insiders.

### 2.5 Marginal hour ranking (if goal = move toward stop)

1. **Block federal preemption** — defensive; lose this and states are gutted  
2. **Research → policy brief** — not LW post  
3. **Join sustained advocacy org** — not one-time petition  
4. **Local network** (3 people phone-banking > 300 Twitter followers)  
5. **Public letters / petitions** — last

**Minimal viable civic engagement:** Encode alerts + monthly legislator contact + anti-preemption calls.

---

## Part 3 — What civil society can do

### 3.1 Proven partial wins

| Model | Example | Why it worked |
|-------|---------|---------------|
| Youth/student advocacy | **Encode AI** — SB 53, NY RAISE Act | Media frame; no corporate $ |
| Whistleblowing | Kokotajlo → **Right to Warn** (2024) | Costly signal; congressional attention |
| Populist coalition | Bannon/Hawley — killed Cruz moratorium 99–1; **GUARD Act** | Non-LW vocabulary; shared enemy (Big Tech) |
| Scientist letters | CAIS 2023, IDAIS | Overton window; **not direct legislation** |
| State legislation | SB 1047 → SB 53 lineage | States = realistic US battlefield |

### 3.2 Not yet effective at scale

| Model | Blocker |
|-------|---------|
| Engineer strike | NDAs, compensation, no union structure; need AIWI-style protection |
| Consumer boycott | Low elasticity (ChatGPT, Copilot embedded) |
| Shareholder activism | OpenAI private; Big Tech shareholders want ROI |
| International grassroots | Global South wants access, not pause |
| Direct action / violence | Polarizes; Yudkowsky 2026 argues for **lawful state force**, not street action |

### 3.3 Realistic collective strategy (2026)

```
Short-term harms (labor, copyright, deepfakes)
        ↓ ally with
Long-term safety (catastrophic / loss of control)
        ↓ push
State bills: transparency → licensing → compute cap
        ↓ defend against
Federal preemption (active threat)
        ↓ long run
International compute treaty (grassroots can only pressure governments)
```

**Weird but workable US coalition:** Encode + parts of AI Now + safety orgs + populist right (GUARD Act, anti-preemption) — **not** purity on ideology.

---

## Part 4 — Organizations & links

| Organization | Focus | How to participate |
|--------------|-------|-------------------|
| [Encode AI](https://encodeai.org/) | US state legislation | Volunteer, alerts, campus chapters |
| [FLI](https://futureoflife.org/) | Pause, international | Petitions, events |
| [ControlAI](https://controlai.com/) | UK/EU policy | UK campaigning |
| [AI Now Institute](https://ainowinstitute.org/) | Labor, power, near-term harm | Research, events |
| [AIWI](https://aiwi.org/) | Whistleblower protection | Support, awareness |
| [CIP](https://www.cip.org/) | Deliberative democracy / Global Dialogues | Public input programs |
| [PauseAI](https://pauseai.info/) | Global grassroots pause | Local chapters |
| Humans First (populist right) | Pre-deployment vetting | Policy overlap on vetting; different ideology |

**Encode note:** Founded by Saheel Revanur (~age 15); funds from FLI/SFF; **no corporate/foreign/AI-exec money**; Politico “Greta Thunberg of AI”; SB 53, NY RAISE Act, nuclear-launch AI law.

---

## Part 5 — Key policy timeline (US, condensed)

| Date | Event |
|------|-------|
| 2023-03-22 | FLI “Pause Giant AI Experiments” letter (1,000+ signers) |
| 2023-11 | Bletchley summit — frontier catastrophic risk frame |
| 2024 | SB 1047 passes CA legislature → **Newsom veto** |
| 2024-05-14 | US–China AI dialogue Geneva (only formal session to date) |
| 2024-06 | Right to Warn open letter (current/former lab employees) |
| 2025-02 | Paris AI Action Summit — investment focus; US/UK did not sign ministerial declaration |
| 2025-05–07 | Cruz federal **anti-regulation moratorium** in BBB → **stripped 99–1** |
| 2025+ | SB 53 (transparency); Anthropic endorsement |
| 2026 | ~$8.5M Q1 lobbying on **preemption**; GUARD Act in Senate Judiciary |
| 2026-05 | US–China agree to **restart** AI dialogue (guardrails, not pause) |

---

## Part 6 — Open questions (for future updates)

1. Will federal **preemption** pass in this Congress?  
2. Will Bannon/Hawley coalition merge with Encode/Wiener safety coalition or stay parallel?  
3. Does US–China dialogue ever move from guardrails to **mutual training limits**?  
4. When does on-chip FLOP metering mature enough for treaty verification?  
5. Next CA/NY bill: transparency only, or explicit **compute cap**?

**Update cadence suggestion:** refresh §1.2, §1.4, §2.2, §5 quarterly or after major bill votes.

---

## Sources

### Repo (internal)

<!-- private monorepo only: - `[private note]` -->
- `us_china_ai_dialogues.md`  
- `research_why_ai_warnings_dismissed.md` (§4.5–4.7, §9, Appendix B)  
- `ACX_LessWrong_EA_rationalist_community_map.md`  
<!-- private monorepo only: - `[private note]` -->
- `<!-- private monorepo only -->` (Encode, FLI, AISI, etc.)

### External

- Ramiah et al., [Toward a Global Regime for Compute Governance: Building the Pause Button](https://arxiv.org/html/2506.20530)  
- [Hardware verification mechanisms taxonomy](https://arxiv.org/pdf/2604.04712)  
- [CFR: The world is trying to govern AI](https://www.cfr.org/articles/the-world-is-trying-to-govern-ai-the-un-wants-in)  
- [Seismic UK 2025 — On the Razor's Edge](https://report2025.seismic.org/media/documents/On_the_Razors_Edge_Seismic_Report_2025.pdf)  
- [Pew: US public and AI experts](https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/)  
- [The AI Lobby](https://www.theailobby.com/money)  
- Stix & Maas (2023), [short vs long-term AI risks](https://link.springer.com/article/10.1007/s43681-023-00336-y)  
- [CAIS Statement on AI Risk](https://safe.ai/work/statement-on-ai-risk) (May 2023)  
- [IDAIS](https://idais.ai/)  
- Yudkowsky (2026), *Only Law Can Prevent Extinction* — [LessWrong](https://www.lesswrong.com/)  
- Newsom SB 1047 veto: [message PDF](https://www.dwt.com/-/media/files/2024/10/sb1047vetomessage.pdf)  
- Anthropic SB 53 endorsement: [anthropic.com/news](https://www.anthropic.com/news/anthropic-is-endorsing-sb-53)
