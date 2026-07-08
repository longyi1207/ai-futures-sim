> **Ported from:** `notes/timeline_prediction/node11_evidence_rationale.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 11 — Corporate Governance & Safety Independence: Evidence Rationale

> **Parent:** [`node11_corporate_governance.md`](./node11_corporate_governance.md)  
> **Purpose:** Claim | Why | Evidence | Analogue | Would update if | Conf — for every Node 11 probability.

---

## 1. Node definition — governance structure is load-bearing for halt

**Claim:** Frontier lab **corporate governance** (board independence, PBC/LTBT teeth, safety reporting lines) is a **separate crux** from whistleblower *events* (Node 4): it sets P(halt | internal crisis) ≈ **0.12**, not ~0.40 naive prior.

**Why:** Node 4 models human *response* to leaks; Node 11 models **institutional default** leaks face. Board crisis 2023 + Leike 2024 + Sharma 2026 = **repeated** observation of **zero** training stop despite **internal** leverage.

**Evidence:**
- `node4_evidence_rationale.md` §29–31 — board crisis, Leike, Saunders
- `crosscut_secondary_cruxes.md` §2 — hollowing branch 0.65
- `<!-- private monorepo only -->` §2.3, §5 — crisis timeline

**Analogue:** 2008 financial crisis — board risk committees existed on paper; **no** trading halt when models broke.

**Would update if:** ≥2 labs halt >90d after **pure governance** crisis (no autonomous harm).

**Conf:** H

---

## 2. Branch M1 — modal hollowing P = 0.65

**Claim:** P(continued safety-team hollowing + narrative without veto, 2026–28) = **0.65**.

**Why:** Default track 2024–26: superalignment dissolved, safety absorbed into product divisions, conditional pause rhetoric without halt, Sharma **exit not organize**. Oct 2025 OpenAI recap and Apr 2026 LTBT majority are **paper upgrades** atop **practice flat**.

**Evidence:**
- `<!-- private monorepo only -->` §23 OpenAI — "actions contradicted stated commitments"
- `node4_evidence_rationale.md` §23 — P(public halt >30d) = 0.08 modal
- OpenAI post-board-crisis: training continued (`node4` §29)

**Analogue:** Pharma — pharmacovigilance teams exist; **blockbuster launch** pressure overrides rare drug withdrawals.

**Would update if:** Documented ≥2 labs restore **independent** safety org reporting to CEO-only with **deploy veto** used once.

**Conf:** M

---

## 3. Branch T1 — board crisis repeat without halt P = 0.25

**Claim:** P(acute OpenAI-2023-class governance fight **without** training stop by 2028) = **0.25**.

**Why:** Single strongest analogue: board **had** firing power, 5-day media storm, safety-aligned directors **lost** — training **never paused**. Base rate for **second** crisis at OpenAI or peer given capex/Stargate pressure: ~**1 in 4** over 2 yr window.

**Evidence:**
- `<!-- private monorepo only -->` §2.3 — Altman fired 2023-11-17, reinstated 2023-11-21, Toner out
- `node4_evidence_rationale.md` §29 — "insiders with leverage still lost"
- [NBC News — OpenAI restructuring Oct 2025](https://www.nbcnews.com/tech/tech-news/openai-restructuring-company-structure-chatgpt-invest-own-rcna240138) — commercial/IPO pressure **continues**

**Analogue:** WeWork 2019 — board challenge → CEO returns → governance **reverted**.

**Would update if:** OpenAI Foundation removes Altman **and** new CEO announces **30d training pause**.

**Conf:** M

---

## 4. Branch T2 — safety re-empowered P = 0.10

**Claim:** P(safety team **re-empowered** — hard RSP/FSF stop invoked + visible halt or deploy block by 2028) = **0.10**.

**Why:** Counter-tail reserved for **observed** invocation, not rhetoric. Anthropic RSP v3.0, OpenAI SSC, DeepMind FSF v3.1 create **mechanisms**; **zero** public invocations 2024–26. LTBT majority (Apr 2026) **theoretically** enables block — Sharma exit same quarter **undercuts** insider confidence.

**Evidence:**
- Anthropic RSP v3.0 (Feb 2026) — self-enforced, no external accountability (`research_ai_governance_landscape.md`)
- [Anthropic LTBT announcement](https://www.anthropic.com/news/the-long-term-benefit-trust)
- Node 4 §23 — P(RSP hard stop) = 0.12 modal, 0.25 tail-gov

**Analogue:** Nuclear SCRAM — designed to work; **rarely** tested in production crisis.

**Would update if:** Public RSP ASL-4+ trigger → documented **training slowdown** + Risk Report.

**Conf:** L–M

---

## 5. P(halt >30d | internal governance crisis) = 0.12

**Claim:** P(any frontier lab **public training halt >30 days** | internal governance crisis without autonomous harm) = **0.12** (range 0.08–0.18).

**Why:** Product of conditional chain in `node11_corporate_governance.md` — board favors safety ~15% × eval trigger ~35% × low race-pressure counterfactual ~20%. **Four** historical crises → **zero** halts.

**Evidence:**
- Node 4 §29–31 — board, Leike, Saunders
- `<!-- private monorepo only -->` §5.2 — Sharma 2026 no halt
- Crosscut §2 — derived P(halt|crisis) 0.10–0.15

**Analogue:** `node4` composite prior on lab halt | scandal.

**Would update if:** Leike-class resignation **immediately** followed by named run pause (never observed).

**Conf:** M

---

## 6. P(≥2 labs halt >30d | governance crisis) = 0.03

**Claim:** P(**multi-lab** coordinated halt >30d | governance crisis) = **0.03**.

**Why:** Node 4 §23 — P(≥2 labs halt) = 0.18 × 0.15 tail-gov ≈ 0.03 in whistleblower frame; governance-only crisis **weaker** trigger than C10 eval — **same order of magnitude**, not higher.

**Evidence:**
- `node4_evidence_rationale.md` §23, §308–309
- Anthropic RSI — multilateral verify **prerequisite** (`Anthropic_When_AI_Builds_Itself_2026.md` §1)
- Seoul 2024 Frontier Commitments — voluntary, no halt

**Analogue:** COVID vaccine pause (AZ thrombosis) — **single** product hold, not industry halt.

**Would update if:** Seoul-style summit produces **binding** synchronized halt clause with verification.

**Conf:** M

---

## 7. OpenAI board crisis 2023 — training continued (anchor)

**Claim:** OpenAI Nov 2023 crisis is the **strongest downward bound** on P(halt | scandal): board power + insider coalition → **commercial default**.

**Why:** Even **structural** governance failure (CEO fired) did not pause GPT-4-era training. Sets prior for all subsequent lab crises.

**Evidence:**
- `<!-- private monorepo only -->` §2.3–2.4 — "安全派输了董事会战争"
- `node4_evidence_rationale.md` §29
- `node1_evidence_rationale.md` — board crisis → commercial default

**Analogue:** Stronger than FLI 2023 (no insider leverage) for modal calibration.

**Would update if:** FOIA/SEC filing shows **undisclosed** training pause during Nov 17–21 window (no public evidence).

**Conf:** H

---

## 8. Leike / superalignment dissolution — zero operational leverage

**Claim:** Jan Leike May 2024 resignation + superalignment team dissolution moved **narrative** but **zero** operational leverage on OpenAI training.

**Why:** Viral tweet ("safety culture lost to shiny products"); 20% compute pledge **abandoned**; team absorbed. **Cheaper** costly signal than Saunders (no memo dump) — between E4 and E1 in Node 4 taxonomy.

**Evidence:**
- `<!-- private monorepo only -->` §3.2 — Leike 2024-05-17, superalignment dissolved
- `<!-- private monorepo only -->` §23 OpenAI — compute pledge denied
- Node 4 §31 — "Insider moral authority ≠ operational leverage"
- [TechCrunch — superalignment withered](https://techcrunch.com/2024/05/18/openai-created-a-team-to-control-superintelligent-ai-then-let-it-wither-source-says)

**Analogue:** Executive resigning on principle — stock price blip, **no** strategy change.

**Would update if:** OpenAI **reconstitutes** independent superalignment-class team with **published** compute budget.

**Conf:** H

---

## 9. Sharma exit 2026 — exit not organize; pipeline thins

**Claim:** Mrinank Sharma Feb 2026 exit (Sleeper Agents co-author → leave industry for poetry) **increases** P(thin whistleblower pipeline) and **decreases** P(costly internal leak).

**Why:** Breaks "migrate to Anthropic" pattern (Leike, Schulman). Signals **structural** despair vs company-specific. Safeguards Research lead vacancy **without** public succession narrative.

**Evidence:**
- `<!-- private monorepo only -->` §5.1–5.2 — Sharma 2026-02-09
- `../supplements/Mrinank_Sharma_学习路线.md` — Sleeper Agents, Constitutional Classifiers lineage
- Node 4 §24 — "Sharma 2026: exit not organize — defection from insider advocacy"
- Node 4 §10 — E4 ↑ as managed disclosure substitute

**Analogue:** Climate scientist leaving academia for farming — field loses advocate, not just employer loses employee.

**Would update if:** Sharma or peer publishes **documented** leak with policy effect (Kokotajlo-class).

**Conf:** M

---

## 10. Anthropic RSI essay — E4 managed disclosure; continue training

**Claim:** Anthropic Institute *When AI Builds Itself* (2026-06-04) is **primary E4 path**: internal RSI data + conditional *expect* pause — **same month** Trump EO + GAAIA **acceleration frame** wins.

**Why:** Wording `we expect that we would` not `commit`; verification mechanism **does not exist**; publication **preempts** whistleblower pressure while training implied continue. Node 4 P(E4)=0.37 anchor.

**Evidence:**
- `https://www.anthropic.com/institute/recursive-self-improvement` — §1 conditions, §5.2 tension (8× code velocity + expect pause)
- `<!-- private monorepo only -->` §5.1 — 2026-06-04 entry
- Node 4 §32 — "Labs preempt whistleblower with managed disclosure"

**Analogue:** Tobacco industry "we support regulation" while opposing binding rules.

**Would update if:** Anthropic **actually pauses** a named training run citing RSP + RSI essay triggers.

**Conf:** H

---

## 11. P(RSP hard stop invoked by 2028) = 0.12

**Claim:** P(Anthropic **publicly invokes** RSP ASL hard stop with documented safeguard escalation by 2028) = **0.12**.

**Why:** RSP v3.0 most detailed framework; v3.0 **honestly** splits commitments vs recommendations — **weakens** binding mass. Zero invocations 2024–26 despite Apollo scheming, Greenblatt misalignment reports. **12%** = tail-gov adjacent, not modal.

**Evidence:**
- `<!-- private monorepo only -->` §23 Anthropic RSP v3.0
- Node 4 §23 — P(RSP hard stop) = 0.12 modal
- [Anthropic RSP v3.0](https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0)

**Analogue:** Fed "break glass" emergency lending — exists, **rarely** used pre-crisis.

**Would update if:** Misalignment Risk Report triggers ASL-4+ and **public** deployment delay >30d.

**Conf:** M

---

## 12. OpenAI Oct 2025 restructuring — paper governance ↑

**Claim:** OpenAI Foundation + OpenAI Group PBC recap (Oct 28, 2025) **increases nominal** safety governance (SSC, mission-only fiduciary on safety) but **does not yet** lower P(no halt) — track record discount applies.

**Why:** Structure **after** superalignment gutting and **before** proof of SSC veto use. CA AG MOU conditions non-objection to recap. Kolter SSC chair **exclusive** Foundation board — **separation** on paper.

**Evidence:**
- [OpenAI — Our structure](https://openai.com/our-structure/) — Oct 28, 2025
- [CA AG MOU Oct 27, 2025](https://oag.ca.gov/system/files/attachments/press-docs/Final%20Executed%20MOU%20Between%20OpenAI%20and%20California%20AG%20re%20Notice%20of%20Conditions%20of%20Non-Objection%20%2810.27.2025%29%20%28Signed%20by%20OpenAI%29%20%28Signed%20by%20CA%20DOJ%29.pdf) — SSC halt authority, advance notice
- OpenAI PBC articles — safety decisions may ignore shareholder pecuniary interest ([DocumentCloud](https://s3.documentcloud.org/documents/26205026/openai-pbc-articles-of-incorporation.pdf))

**Analogue:** Post-2008 bank **living wills** — compliance document until tested.

**Would update if:** SSC **blocks** a named model release with public CA AG notice within 12 mo.

**Conf:** M

---

## 13. P(OpenAI SSC blocks frontier release by 2028) = 0.15

**Claim:** P(OpenAI Safety and Security Committee **blocks or delays** a frontier model release past internal schedule by 2028) = **0.15**.

**Why:** CA MOU grants SSC role over release when risk thresholds exceeded; **higher** than P(full training halt) because **deployment** veto is narrower than **compute stop**. Still **no** observed block 2025–26 post-recap.

**Evidence:**
- CA AG MOU § — SSC advance notice, material risk
- OpenAI structure page — SSC "continue its current role" over safety practices
- Node 11 lab tracker — OpenAI P(halt|crisis) = 0.08 vs P(SSC block) = 0.15

**Analogue:** FDA complete response letter — delays launch, not factory shutdown.

**Would update if:** GPT-5.x or successor launch **publicly delayed** citing SSC.

**Conf:** L–M

---

## 14. Anthropic LTBT board majority — Apr 2026

**Claim:** LTBT-appointed directors achieving **board majority** (Narasimhan, Apr 14, 2026) is **real governance power on paper** but **P(invoked to delay release)** ≈ **0.12** given Sharma exit + RSI continue-implied.

**Why:** Trust holds Class T shares; trustees **no equity** — mission alignment by design. Majority **first time** — but concurrent insider exodus and *expect* not *commit* pause rhetoric.

**Evidence:**
- [Anthropic LTBT](https://www.anthropic.com/news/the-long-term-benefit-trust)
- [Harvard CorpGov — LTBT analysis](https://corpgov.law.harvard.edu/2023/10/28/anthropic-long-term-benefit-trust/)
- AI Biz Insider Apr 2026 — Narasimhan appointment, LTBT majority
- Hinton Big Technology Podcast 2026-06 — "Anthropic 难扛资本市场" (`AI_safety_大事记`)

**Analogue:** Dual-class founder control — **potential** veto, **observed** product speed.

**Would update if:** LTBT board **publicly blocks** DoD contract or frontier deploy citing public benefit.

**Conf:** M

---

## 15. P(Anthropic conditional pause → actual multilab halt) = 0.08

**Claim:** P(Anthropic RSI-style conditional pause ** converts to** ≥2-lab verifiable halt by 2028) = **0.08**.

**Why:** Requires (a) verification infrastructure **built**, (b) other frontier labs **sync**, (c) Anthropic **acts** not **expects**. Node 3 P(verified training-limit treaty) ≈ 0.04–0.06 — **upper bound** on multilateral halt.

**Evidence:**
- `Anthropic_When_AI_Builds_Itself_2026.md` §1.1 — four conditions
- Node 9 — P(durable multilateral pause) < 0.05
- Node 4 §219 — "No revenue-peak voluntary halt precedent"

**Analogue:** Paris climate — conditional pledges without enforcement.

**Would update if:** Anthropic Institute publishes **working** verification protocol adopted by OpenAI + DeepMind.

**Conf:** M

---

## 16. P(whistleblower pipeline thins 2026–28) = 0.60

**Claim:** P(insider advocacy shifts from **organize/leak** to **exit/ silence** over 2026–28) = **0.60**.

**Why:** Sharma pattern + Kokotajlo costly signal **rare** + Right to Warn **transparency not pause** + NDA enforcement. E4 managed disclosure **substitutes** for leak.

**Evidence:**
- Node 4 §105 — "Safety employee pipeline structurally homeless post-Sharma"
- Node 4 §162 — insider exhaustion ↑
- `<!-- private monorepo only -->` §6.4 — exit派 vs 中悲观派 table

**Analogue:** Post-Snowden tech — fewer new whistleblowers, more **internal compliance theater**.

**Would update if:** ≥3 named frontier researchers **testify under oath** with document dumps in 12 mo.

**Conf:** M

---

## 17. P(safety org reports to product/revenue, ≥2 labs by 2028) = 0.45

**Claim:** P(at least **two** frontier labs have safety/research integrity org **formally reporting** to CPO, product, or revenue lead by 2028) = **0.45**.

**Why:** OpenAI post-superalignment absorption documented; Google Apr 2024 moved Responsible AI **into** DeepMind model-building (`Building for our AI future`). Industry trend = **proximity to models** framed as safety; **independence** ↓.

**Evidence:**
- `<!-- private monorepo only -->` §23 OpenAI — "absorbed into other divisions"
- [Google blog Apr 2024](https://blog.google/company-news/inside-google/company-announcements/building-ai-future-april-2024/) — Responsible AI → DeepMind
- Crosscut §2 would-update — "safety reorg reporting to product/revenue" ↑ hollowing

**Analogue:** Security embedded in DevOps (DevSecOps) — faster shipping, **weaker** veto.

**Would update if:** OpenAI or Anthropic **publicly restores** CEO-only reporting line for Alignment/Safeguards with board seat.

**Conf:** M

---

## 18. Google DeepMind — AI Safety org + FSF v3.1

**Claim:** DeepMind **framework sophistication ↑** (FSF v3.1 Apr 2026, AI Safety & Alignment org Feb 2024) but P(FSF triggers **deployment pause**) ≈ **0.10** — self-enforced, Alphabet product pressure.

**Why:** FSF adds TCLs, SL2+, misalignment domain merged with ML R&D; governance section describes escalation to "appropriate corporate governance bodies" — **no** public halt precedent. Gemini launch cadence **continues**.

**Evidence:**
- [TechCrunch Feb 2024 — AI Safety and Alignment org](https://techcrunch.com/2024/02/21/google-deepmind-forms-a-new-org-focused-on-ai-safety/)
- [DeepMind FSF v3.1 PDF Apr 2026](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf)
- `<!-- private monorepo only -->` §23 DeepMind — influence 5/10

**Analogue:** OpenAI Preparedness — sophisticated paper, **untested** brake.

**Would update if:** Gemini frontier launch **delayed** citing FSF CCL threshold.

**Conf:** M

---

## 19. Meta / xAI — weakest governance; race pressure ↑

**Claim:** P(Meta or xAI **voluntary halt** | internal crisis) < **0.03**; P(xAI **mission drift** under defense/commercial pressure by 2028) = **0.75**.

**Why:** Meta — open-weight philosophy, no RSP-class hard stop. xAI — Feb 2026 Pentagon classified Grok deal **"all lawful purposes"** vs Anthropic safeguards refusal narrative; no formal alignment framework.

**Evidence:**
- `<!-- private monorepo only -->` — xAI Pentagon Feb 2026
- `<!-- private monorepo only -->` §23 Meta — weakest formal framework 4/10
- Crosscut §2 — "xAI all lawful purposes Pentagon deal vs Anthropic safeguards"

**Analogue:** Open-source vs safety — **recall impossible** once weights out.

**Would update if:** xAI publishes RSP-equivalent with **external** audit.

**Conf:** M

---

## 20. P(E4 managed disclosure preempts halt pressure) = 0.40

**Claim:** P(when internal alignment concern rises, lab **publishes** managed longform (RSI essay class) **instead of** leak + **continues training**) = **0.40**.

**Why:** Anthropic Institute model — own narrative before whistleblower. Reduces costly leak incentive; **institutionalizes** transparency-without-brakes (Cluster D).

**Evidence:**
- Node 4 §32, P(E4)=0.37
- `Anthropic_When_AI_Builds_Itself_2026.md` §5.2 — company framing + conditional pause
- Node 4 §417 — "We take this seriously + continue"

**Analogue:** Corporate **pre-bunking** in crisis PR.

**Would update if:** Managed disclosure **immediately followed by** halt (never observed).

**Conf:** M

---

## 21. Revenue / capex peak prevents voluntary halt P = 0.70

**Claim:** P(frontier labs **do not** voluntarily halt during Stargate-class capex / revenue peak, conditional on governance crisis) = **0.70**.

**Why:** Node 1 labor/capex modal + Node 4 "no revenue-peak voluntary halt precedent." OpenAI/Microsoft/Google **$100B+** AI infra commitments 2025–26 — opportunity cost of halt **↑**.

**Evidence:**
- Node 4 §161 — "Revenue peak + capex cycle — no voluntary halt precedent"
- Node 1 — agent labor shock modal reinforces commercial default
- OpenAI recap Oct 2025 — investor returns + IPO path ([NBC](https://www.nbcnews.com/tech/tech-news/openai-restructuring-company-structure-chatgpt-invest-own-rcna240138))

**Analogue:** Oil majors during price spike — **delay** climate capex, not stop pumping.

**Would update if:** Major lab **publicly cuts** training budget >20% citing safety (not market).

**Conf:** M

---

## 22. PBC mission clause invoked to delay release P = 0.10

**Claim:** P(any frontier PBC **publicly cites** mission/benefit clause to **delay** a frontier release 2026–28) = **0.10**.

**Why:** Legal latitude exists (OpenAI PBC articles, Anthropic charter); **observed** invocations **zero**. Clauses function as **litigation shield** and **marketing**, not operational brake.

**Evidence:**
- OpenAI PBC incorporation — safety-only fiduciary language
- Anthropic PBC public benefit purpose (`research_ai_governance_landscape.md`)
- Crosscut §2 — "PBC erosion under revenue/capex pressure"

**Analogue:** B-Corp certification — **rarely** blocks profitable product.

**Would update if:** SEC or CA filing cites PBC duty as **reason** for delayed launch.

**Conf:** L–M

---

## 23. P(second OpenAI governance crisis by 2028) = 0.18

**Claim:** P(OpenAI experiences **second** C-suite/board governance crisis with global media coverage by 2028) = **0.18**.

**Why:** First crisis 2023; recap **concentrates** power in Foundation but **same** CEO; investor/IPO pressure + safety tensions **recur**. Not identical to P(halt) — crisis can fire **without** halt (T1 branch).

**Evidence:**
- 2023 crisis base rate — 1 event in ~4 yr company history at frontier scale
- Oct 2025 structure — Altman remains CEO on both boards
- `AI_safety_大事记` — "安全 vs 商业" recurring narrative

**Analogue:** Uber 2017 — repeated governance scandals, **no** business model halt.

**Would update if:** 24 mo **without** any OpenAI governance headline (downward).

**Conf:** L

---

## 24. Superalignment arc repeats at another lab P = 0.35

**Claim:** P(another frontier lab ** announces** dedicated superintelligence/safety team with compute pledge, then **dissolves or hollows** it within 24 mo, 2026–28) = **0.35**.

**Why:** DeepMind AI Safety & Alignment (2024) parallels superalignment **narrative**; industry pattern = announce → absorb. OpenAI **template** copied then abandoned.

**Evidence:**
- TechCrunch 2024 — DeepMind org "Similar in mission to Superalignment"
- OpenAI superalignment arc (`AI_safety_大事记` §3.2)
- `research_ai_governance_landscape.md` — pattern of contradiction

**Analogue:** Corporate **innovation lab** lifecycle — launch, hype, merge into core product.

**Would update if:** DeepMind **maintains** separate AGI safety team with **published** budget through 2028.

**Conf:** L–M

---

## 25. Node 11 → P(no effective pause) +3–5pp

**Claim:** Integrating Node 11 branch mix **raises** P(no federal/industry training pause through 2028) from **0.82–0.84** to **0.85–0.89** (+3–5pp).

**Why:** 65% modal hollowing + 25% crisis-without-halt **both** imply continue; only 10% re-empower tail reduces. Confirms Node 4 modal whistleblower branch **structurally underpinned**.

**Evidence:**
- `../supplements/pdoom_methodology.md` crux #5 — 0.82 (0.72–0.92)
- Node 9 net on P(no pause) +0.02–0.03 — Node 11 **stronger** channel (US labs)
- Crosscut §2 p(doom) — "+3–5pp vs −2–3pp" on extinction from hollowing vs re-empower

**Analogue:** Bayesian — same evidence, **explicit** institutional prior.

**Would update if:** Re-stitch with **invoked** RSP hard stop observed.

**Conf:** M

---

## 26. Node 11 → P(no shutdown at ASI) +3–5pp

**Claim:** Node 11 **raises** P(no effective shutdown when ASI threshold reached) from **~0.60** to **~0.63–0.65** (+3–5pp).

**Why:** Labs that **cannot halt at C7–C9** (governance evidence) unlikely to **execute shutdown at C10** without external coercion (DPA 0.03, EU deployment 0.14 — insufficient for training stop). Node 4 multiplier 3 chain.

**Evidence:**
- Node 4 §672 — RSP hard stops 0.12; if not credible, raises P(no shutdown)
- `../supplements/pdoom_methodology.md` — failure mode bang vs whimper; modal = oversight not halt
- Node 4 §585 — P(no effective shutdown at ASI) × 0.50–0.70 in extinction chain

**Analogue:** Fukushima — institutions **fail to SCRAM** when design assumes they will.

**Would update if:** Live-fire **shutdown drill** at ≥1 frontier lab with public report.

**Conf:** M

---

## 27. Cluster A correlation — hollowing ↔ race ↔ no pause

**Claim:** P(modal hollowing) correlates **↑** with P(no pause), P(race post-theft N3), P(GAAIA preemption N6) — joint tail **~3–5×** product of marginals, not independent.

**Why:** Same capital/capex/natsec coalition blocks halt. Node 11 makes **explicit** what correlation matrix listed for Cluster A.

**Evidence:**
- `correlation_matrix.md` Cluster A — acceleration block
- Crosscut §2 links table — N1, N3, N4, N6
- Node 3 — post-theft race correlates with hollowing

**Analogue:** Correlated defaults in CDOs — **joint** tail risk.

**Would update if:** EU-only brake **decouples** US lab pace from governance (Node 9 T1 tail).

**Conf:** M

---

## 28. p(doom) net — extinction bucket +1.5–3pp

**Claim:** Node 11 contributed **~+1pp** to Phase 2b re-stitch (18%→**19%**), primarily via misalignment tail branch (+0.5–1pp) and modal race speed (+0.5pp).

**Why:** Does **not** add independent bio risk. Misalignment branch weight 25% × higher P(no shutdown) × continued training → **compound** not additive — use mixture not product of 28 marginals.

**Evidence:**
- `../supplements/pdoom_methodology.md` — branch model 58% modal / 25% misalign / 17% bio
- Crosscut §2 — "+3–5pp on P #1 and P #6"
- Node 11 parent doc — p(doom) table

**Analogue:** Phase 4a stitch methodology — node-by-node delta.

**Would update if:** Full re-stitch with correlation_matrix Cluster A discount.

**Conf:** L — pending Phase 4b calibration

---

## Related files

- [`node11_corporate_governance.md`](./node11_corporate_governance.md)
- [`node4_evidence_rationale.md`](./node4_evidence_rationale.md)
- [`crosscut_secondary_cruxes.md`](./crosscut_secondary_cruxes.md) §2
- [`correlation_matrix.md`](./correlation_matrix.md)
- [`../my_pdoom.md`](../my_pdoom.md)

---

## Update log

| Date | Change |
|------|--------|
| 2026-07-04 | Initial — 28 evidenced P sections |
