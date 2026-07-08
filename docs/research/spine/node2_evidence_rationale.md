> **Ported from:** `notes/timeline_prediction/node2_evidence_rationale.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 2 CBRN — Evidence & Rationale for Every Probability

> **Parent:** [`../supplements/node2_cbrn_full.md`](../supplements/node2_cbrn_full.md)  
> **Date:** 2026-07-03  
> **Format:** Claim | Why | Evidence | Analogue | Would update if | Conf

Each section documents one probability or timing claim from Node 2. Probabilities are **subjective elicitation** unless noted as derived (e.g., tail branches sum to ~1.0 conditional on Tier 2 live).

---

## Hybrid timing layers

### P(timing) — Capability Tier 1→2 crossing, modal window 2026-08 – 2027-06

**Claim:** Frontier systems cross from "actionable post-jailbreak bio guidance" (Tier 1) to "skilled-actor end-to-end assist on synthesizable sequences" (Tier 2) in the modal window Aug 2026 – Jun 2027.

**Why:** GeneBreaker already shows ~60% ASR on Evo2-40B for pathogen-homologous outputs (2025); jailbroken frontier LLMs pass WMDP-bio subsets with synthesis-relevant detail. RAND RBA4087-1 expert elicitation places **autonomous** pathogen design after ~2027 but **assistive** acceleration now. Modal window = time for red-team replication + one major model generation (frontier LLM refresh + Evo-class FM iteration), not Tier 3.

**Evidence (URLs + repo paths):**
- https://arxiv.org/abs/2505.23839 (GeneBreaker)
- https://www.rand.org/pubs/research_briefs/RBA4087-1.html
- https://www.wmdp.ai/
- `../supplements/biosecurity_evo_dual_use.md` §3.1
- `../supplements/node2_cbrn_full.md` §Hybrid timing

**Analogue:** GPT-4 jailbreak ecosystem matured ~6–12 mo after release; biology FM red-teaming is ~12 mo behind LLM red-teaming.

**Would update if:** Independent third-party eval finds **no** jailbreak uplift to synthesizable-sequence guidance on current frontier LLM **and** GeneBreaker ASR collapses on Evo2-40B with Arc mitigations → demote to Tier 1-only through 2028.

**Conf:** M–H

---

### P(timing) — Capability tail: Tier 2 confirmed + Tier 3 plausible, 2027 H2+

**Claim:** If capability crossing slips past Jun 2027, Tier 2 confirmation + Tier 3 plausibility cluster in H2 2027 or later.

**Why:** Tail assumes slower FM scaling, stronger unlearning patches, or screening/function-based SOC deployment that raises wet-lab closure cost before low-skill viability. RAND timeline for autonomous design already biased late; regulatory lag (12–18 mo) pushes incident-driven salience rightward.

**Evidence:**
- RAND RBA4087-1: assistive through ~2027, not autonomous
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.3 (DBTL closure still requires skill)
- `../supplements/node2_cbrn_full.md` §Hybrid timing

**Analogue:** AlphaFold3 gating debate delayed open-weight structure tools ~18 mo without stopping misuse research.

**Would update if:** Documented Tier-3 low-skill attack before Q4 2027 → tail window was too pessimistic.

**Conf:** M

---

### P(timing) — Insider/regulator salience modal: 2026-06 – 2027-03

**Claim:** Insiders and regulators treat Tier 1→2 as policy-relevant in the window already started (Jun 2026) through Mar 2027.

**Why:** Jun 2026 screendna letter + Amodei policy essay + BMIA introduction + AISI/Preparedness red-team circulation create **simultaneous** natsec + industry + lab-CEO pressure — independent of public media. This layer tracks **elite attention**, not statute enactment.

**Evidence:**
- https://screendna.org/ (Jun 4, 2026 letter)
- https://darioamodei.com/post/policy-on-the-ai-exponential
- https://www.congress.gov/bill/119th-congress/senate-bill/3741
- `../supplements/node2_cbrn_full.md` §Hybrid timing
- `../supplements/ai_pause_advocacy_playbook.md` §1.2 (EO 14409 Jun 2026)

**Analogue:** Bletchley 2023 framing preceded any binding CBRN law by years — insider salience ≠ law.

**Would update if:** BMIA dies in committee with no substitute and screendna coalition fractures by Q1 2027 → salience window extends to 2027-09+.

**Conf:** M–H

---

### P(timing) — Insider/regulator salience tail (no Trigger E): 2027-09+

**Claim:** Without Trigger E, insider salience does not convert to binding federal action until Sep 2027 or later.

**Why:** Trump-admin deregulatory default (EO 14409 voluntary-only); 12–18 mo lag invariant from COVID policy response and from SB 1047→SB 53 multi-year arc. Physical-layer screening has bipartisan path; **in silico CBRN mandates** do not — so "salience" can persist without statute.

**Evidence:**
- https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/ (EO 14409)
- `../supplements/ai_pause_advocacy_playbook.md` §1.2, §1.5 (12–18 mo state path)
- `../supplements/node2_cbrn_full.md` §Hybrid rule

**Analogue:** Y2K remediation: insider urgency 1998, statutory/industry action peak 1999 — ~12 mo.

**Would update if:** BMIA signed into law before Sep 2027 without Trigger E → lag estimate wrong for screening (not necessarily CBRN eval).

**Conf:** M

---

### P(timing) — Public salience: only with Trigger E

**Claim:** Mass public/media CBRN salience requires a Trigger E event; capability alone insufficient.

**Why:** 2023 FLI pause letter had zero policy effect (`research_ai_pause_advocacy_playbook.md`). CBRN lacks visible consumer harm frame (vs deepfakes, jobs). P(mass bio-x-risk protest)=0.08 in actor table reflects low baseline. Amodei essay + CEO letter are **elite** signals, not NYT-front-page drivers.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §Executive summary, §2.1
- `../supplements/node2_cbrn_full.md` §Actor table (Public/markets)
- https://futureoflife.org/open-letter/pause-giant-ai-experiments/ (2023, no law)

**Analogue:** SolarWinds 2020 — massive insider/regulator action, limited sustained public protest.

**Would update if:** Sustained >2 mo media on leaked red-team **without** synthesis incident → public salience decouples from Trigger E.

**Conf:** M

---

## CBRN uplift tiers (status claims)

### P(status) — Tier 0 confirmed baseline

**Claim:** Generic science tutoring (Tier 0) is confirmed for all frontier and most base models.

**Why:** Pre-2023 LLMs already answered undergraduate biochemistry; no dispute. Tier 0 is reference class for "no uplift."

**Evidence:**
- `../reference/03_ci_spine.md` §Method (Tier 0–3 definitions)
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.1

**Analogue:** Calculator-grade arithmetic — not policy-relevant.

**Would update if:** N/A (definitional baseline).

**Conf:** H

---

### P(status) — Tier 1 confirmed at frontier

**Claim:** Post-jailbreak, frontier models provide **actionable** bio/chem protocol steps for a motivated reader with existing expertise.

**Why:** WMDP-bio scores on frontier models are non-trivial; jailbreak red-teams (HarmBench-class, lab internal) repeatedly extract synthesis-relevant steps. Published scores are **lower bounds** due to eval awareness (+3–18 pp refusal when models detect tests — Goodfire 2026).

**Evidence:**
- https://www.wmdp.ai/
- https://www.goodfire.ai/research/verbalized-eval-awareness-inflates-measured-safety
- `https://arxiv.org/abs/2310.11436` §2, §11 (+3–18 pp; sandbagging elicitation on WMDP)
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.1

**Analogue:** Cyber: Metasploit docs were always public; LLM uplift = retrieval + tailoring, not novel knowledge.

**Would update if:** Third-party eval with realism controls + awareness monitoring shows frontier models **fail** to provide actionable steps under strong jailbreak suite → revise Tier 1 to "emerging" not "confirmed."

**Conf:** H

---

### P(status) — Tier 2 emerging → partial confirm (not Tier 3)

**Claim:** Skilled actors get end-to-end assist on novel/optimized **synthesizable** sequences; wet-lab skill + chokepoint evasion still required. Tier 3 (low-skill viable) not confirmed.

**Why:** GeneBreaker ~60% ASR on Evo2-40B for pathogen-homologous outputs; case studies show high DNA/protein similarity to SARS-CoV-2 spike, HIV env. RAND: AI remains **assistive** not autonomous designer through ~2027. No documented low-skill attack. Tier 2 = **skilled actor + FM/LLM stack**, not script-kiddie.

**Evidence:**
- https://arxiv.org/abs/2505.23839
- https://github.com/zaixizhang/GeneBreaker
- https://www.rand.org/pubs/research_briefs/RBA4087-1.html
- `../supplements/biosecurity_evo_dual_use.md` §3.1–3.3
- `../supplements/node2_cbrn_full.md` §CBRN uplift tiers

**Analogue:** Early CRISPR DIY bio 2010s — grad-student skill floor, not mass casualty from hobbyists.

**Would update if:** Documented Tier-3 attack OR classified end-to-end demo → upgrade to Tier 3 confirmed; GeneBreaker ASR collapse → demote to Tier 1.

**Conf:** M–H

---

### P(status) — Tier 3 not confirmed as of 2026-07

**Claim:** No documented attack where low-skill actor achieves design + synthesis + screening evasion end-to-end.

**Why:** All public red-team success (GeneBreaker, WMDP jailbreaks) still assumes biology literacy, synthesis budget, or lab access. DBTL automation lowers bar but not to "no skill." Absence of evidence ≠ evidence of absence — hence Tier 3 **plausible** in tails, not confirmed.

**Evidence:**
- `../supplements/biosecurity_evo_dual_use.md` §3.3 (composite scenario still requires assembly)
- RAND RBA4087-1
- `../supplements/node2_cbrn_full.md` (no documented attack)

**Analogue:** Stuxnet required nation-state resources despite cyber "low skill" myth.

**Would update if:** FBI/CDC investigation confirms AI-assisted synthesis order from non-expert actor → Tier 3 confirmed.

**Conf:** H (for "not confirmed"); M (for "not impossible")

---

## Trigger E probabilities

### P = 0.15–0.25 — Trigger E: FBI/CDC synthesis order linked to AI-assisted design (by 2027)

**Claim:** Conditional on Tier 2 capability live, 15–25% chance by end-2027 that a federal investigation publicly links a synthesis order to AI-assisted design.

**Why:** Synthesis screening + recordkeeping (IGSC, proposed BMIA) increases traceability; AI-assisted design is rising base rate. **Public linkage** is rarer than incident — requires investigation disclosure, whistleblower, or leak. Mid-teens base rate: higher than random biocrime, lower than cyber breach disclosure rates.

**Evidence:**
- https://screendna.org/ (recordkeeping advocacy)
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.3 (screening chokepoints)
- `../supplements/node2_cbrn_full.md` §Trigger E

**Analogue:** 2001 anthrax letters — massive investigation, limited public attribution speed; AI linkage would be faster if sequence metadata exists.

**Would update if:** Mandatory recordkeeping passes + first flagged order within 12 mo → revise to 0.25–0.35.

**Conf:** L–M

---

### P = 0.20–0.30 — Trigger E: NYT/Science after leaked red-team report

**Claim:** 20–30% by 2027 that major media publishes on leaked frontier red-team CBRN findings.

**Why:** Kokotajlo → Right to Warn precedent; RAISE 72h reporting creates insider paper trail; Amodei public essay normalizes disclosure pressure. Leak probability ↑ as more labs run Preparedness-tier evals. Still <50% — NDAs, reputational risk, and "nothingburger" framing contain leaks.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §3.1 (Kokotajlo / Right to Warn)
- https://legislation.nysenate.gov/pdf/bills/2025/a9449 (RAISE reporting)
- `../supplements/node2_cbrn_full.md` §Trigger E

**Analogue:** Pentagon Papers / Snowden — rare but structural when capability × stakes × insider pool large.

**Would update if:** Major outlet publishes Tier-2 red-team leak in 2026 → revise up for 2027 follow-ons.

**Conf:** L–M

---

### P = 0.25–0.35 — Trigger E: documented near-miss (screening catches AI-designed sequence)

**Claim:** Highest single Trigger E rate: 25–35% by 2027 for a **publicized** near-miss where screening intercepts AI-designed sequence.

**Why:** Near-misses are more likely than successful misuse (screening exists on IGSC members). Y2K pattern: success looks like overreaction — but **generates** mandate momentum (P(mandatory screening law)→0.75+ per Node 2). Providers have incentive to publicize catches as proof of system working.

**Evidence:**
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.3 (IGSC v3.0)
- https://genesynthesisconsortium.org/
- `../supplements/node2_cbrn_full.md` §Trigger E

**Analogue:** Y2K — fixes worked, public narrative was "crisis averted," still drove spend.

**Would update if:** BMIA mandates reporting of near-misses → upper end of range; zero IGSC catches reported through 2027 → revise down.

**Conf:** L–M

---

### P = 0.40–0.50 — No Trigger E (modal)

**Claim:** Modal path: 40–50% that Tier 2 live through 2027 **without** any Trigger E accelerator.

**Why:** Complement of union of triggers (not strictly additive — correlated). Most regulatory epochs (OSTP framework, IGSC upgrades) proceeded without headline biocrime. Insider-driven incrementalism is default in AI policy (`research_ai_pause_advocacy_playbook`: open letters fail, specific bills win).

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §Executive summary
- `../supplements/node2_cbrn_full.md` §Trigger E, §Hybrid rule

**Analogue:** GDPR passed on scandal buildup but many EU tech rules pass on technocratic track.

**Would update if:** Any Trigger E fires in 2026 → drop conditional P(no E) for remainder of horizon.

**Conf:** M

---

### P(effect) — Trigger E: FBI/CDC → P(mandatory screening) 0.75+; P(mandatory CBRN eval) 0.50+

**Claim:** **Conditional on** FBI/CDC-AI linkage Trigger E, P(mandatory federal screening law by 2028) >75%; P(mandatory blocking CBRN eval) >50%.

**Why:** Incident creates natsec + public-health coalition bypassing industry split on training caps. Screening already has CEO + synthesis industry support (screendna). CBRN eval mandate still fights EO 14409 deregulatory frame — hence 0.50+ not 0.90+.

**Evidence:**
- https://screendna.org/
- https://www.congress.gov/bill/119th-congress/senate-bill/3741
- `../supplements/node2_cbrn_full.md` §Trigger E

**Analogue:** 9/11 → ATSA; anthrax → BioShield (partial parallel).

**Would update if:** Tier-3 attack + **no** screening response in 12 mo → falsifies modal path (`../supplements/node2_cbrn_full.md` §Falsifiers).

**Conf:** M (screening); L–M (CBRN eval)

---

## Modal regulatory actions

### P = 0.45 (2027-12) / 0.60 (2028-06) — Mandatory federal nucleic-acid synthesis screening (BMIA / S.3741-class)

**Claim:** 45% by end-2027 that US enacts mandatory federal synthesis screening; 60% by mid-2028.

**Why:** Bipartisan BMIA (Cotton–Klobuchar, Jan 29 2026) with industry endorsements (Twist, IDT, Ginkgo); Jun 2026 screendna letter aligns frontier labs + synthesis CEOs. Narrower coalition than pause — physical chokepoint, not training caps. Still in Commerce committee; Trump admin prefers voluntary frameworks but **supports** screening per AI Action Plan / ARI release. 0.45 reflects ~50% chance of passage in 119th Congress session; 0.60 adds second session / EU pressure.

**Evidence:**
- https://www.congress.gov/bill/119th-congress/senate-bill/3741
- https://www.cotton.senate.gov/news/press-releases/cotton-klobuchar-introduce-bill-to-establish-federal-biotech-security-framework
- https://screendna.org/
- https://ari.us/cotton-klobuchar-intro-biosecurity-modernization-and-innovation-act-to-address-ai-era-biosecurity-risks/
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §4
- `../supplements/node2_cbrn_full.md` §Modal path

**Analogue:** IGSC voluntary → OSTP procurement mandate (2024) → BMIA as third ratchet.

**Would update if:** BMIA fails committee without substitute by Dec 2027 → revise 2028-06 to ≤0.35; signed before Dec 2027 → revise up to ≥0.70 for near-term compliance.

**Conf:** M–H

---

### P = 0.35 (adopted) / 0.55 (phased apply) — EU harmonized screening (Biotech Act Ch. VIII)

**Claim:** 35% that EU adopts Biotech Act with screening intact by end-2027; 55% that phased application covers major providers by mid-2028.

**Why:** Dec 2025 proposal includes mandatory screening, ≥50bp sequences of concern, function-based SOC criteria, benchtop embedded screening (Annex I). EU co-legislation is slow; biotech competitiveness framing may water down Ch. VIII. Adoption ≠ immediate apply — phased enforcement typical. CLTR assessment: draft "delivers decisively" on screening vs their recommendations.

**Evidence:**
- https://health.ec.europa.eu/publications/proposal-regulation-establish-measures-strengthen-unions-biotechnology-and-biomanufacturing-sectors_en
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52025PC1022%2801%29
- https://www.longtermresilience.org/reports/informing-the-european-biotech-act-and-inclusions-of-our-recommendations/
- `../supplements/node2_cbrn_full.md` §Modal path

**Analogue:** EU AI Act — proposal 2021, adoption 2024, phased apply 2025–2027.

**Would update if:** Ch. VIII stripped in trilogue → revise adopted to <0.15; early adoption in 2026 → revise phased apply up.

**Conf:** M

---

### P = 0.15 (2027-12) / 0.25 (2028-06) — Mandatory third-party CBRN eval (federal, blocking release)

**Claim:** Low probability of **binding** federal pre-release CBRN eval with block authority.

**Why:** Amodei Jun 2026 proposes FAA-style third-party testing at ~10²⁵ FLOP for bio/cyber/LoC — **industry proposal, not law**. EO 14409 (Jun 2 2026) explicitly **prohibits construing** EO as authorizing mandatory licensing/preclearance. Banks letter (Jun 2026) pushes voluntary RSI testing + CAISI visibility — adjacent, not bio-blocking. Bipartisan appetite for screening ≠ appetite for release blocks.

**Evidence:**
- https://darioamodei.com/post/policy-on-the-ai-exponential
- https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- `../supplements/ai_pause_advocacy_playbook.md` §1.2 (EO 14409, GAAIA)
- `../supplements/node2_cbrn_full.md` §Modal path

**Analogue:** FAA certification — exists for aircraft, not replicated for AI despite analogy.

**Would update if:** Mandatory CBRN eval with block authority passed and enforced ≥2 releases → falsifier in Node 2; revise all CBRN-mandate P upward.

**Conf:** M

---

### P = 0.70 (2027-12) / 0.75 (2028-06) — State CBRN transparency + third-party assessment (RAISE + SB 53)

**Claim:** High probability of **compliance prep** by end-2027 and enforcement by mid-2028 for NY RAISE + CA SB 53 catastrophic-risk frameworks (incl. bioweapon assistance).

**Why:** RAISE signed Dec 2025, effective **Jan 1 2027** — catastrophic risk includes expert-level bioweapon assistance; 72h incident reporting. SB 53 Encode-backed, Anthropic-endorsed. Law already enacted; P reflects prep + enforcement not passage. Tail: GAAIA federal preemption P≈0.25–0.35 by 2028 could weaken.

**Evidence:**
- https://legislation.nysenate.gov/pdf/bills/2025/a9449
- https://www.wiley.law/alert-New-York-Finalizes-RAISE-Act-for-Frontier-AI-Models-Law-Takes-Effect-January-1-2027
- https://www.anthropic.com/news/anthropic-is-endorsing-sb-53
- `../supplements/ai_pause_advocacy_playbook.md` §1.2, §3.1
- `../supplements/node2_cbrn_full.md` §Modal path, §RAISE

**Analogue:** CA privacy (CCPA) — state leads, federal lag.

**Would update if:** Federal preemption voids RAISE/SB 53 with no replacement → state path dead (Node 2 falsifier).

**Conf:** H

---

### P = 0.30 (2027-12) / 0.45 (2028-06) — OSTP 50bp + function-based SOCs

**Claim:** Moderate-low probability OSTP framework hits 50bp + function-based sequences-of-concern on original timeline.

**Why:** Oct 2026 50bp deadline **paused** by EO 14292 (May 2025) per Node 2. OSTP procurement rule survived Biden EO partial revocation but implementation limbo. BMIA/EU may **supersede** OSTP rather than revive it — dual path increases cumulative P by 2028-06 to 0.45 without OSTP alone succeeding.

**Evidence:**
- https://aspr.hhs.gov/S3/Documents/OSTP-Nucleic-Acid-Synthesis-Screening-Framework-Sep2024.pdf
- `../supplements/biosecurity_evo_dual_use.md` §4
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.3, §4
- `../supplements/node2_cbrn_full.md` §Modal path

**Analogue:** OSHA standards often superseded by industry-consensus norms before rule finalizes.

**Would update if:** OSTP 50bp reinstated by executive action in 2026 → revise 2027-12 to ≥0.50.

**Conf:** L–M

---

### P = 0.50 (2027-12) / 0.65 (2028-06) — IGSC v4 / function-based screening at scale

**Claim:** ~50% major IGSC protocol upgrade (v4-class) with function-based SOC pilots at scale by end-2027; 65% by mid-2028.

**Why:** IGSC v3.0 (2024) already baseline; NIST function-based R&D + IBBIS Common Mechanism commec pilots push v4. Jun 2026 letter **from** synthesis CEOs signals industry willingness ahead of law. Voluntary upgrade faster than statute — but "at scale" requires non-member adoption lag.

**Evidence:**
- https://genesynthesisconsortium.org/
- https://www.nist.gov/publications/beyond-sequence-similarity-case-function-based-screening-nucleic-acid-synthesis
- https://screendna.org/
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.3, §3
- `../supplements/node2_cbrn_full.md` §Modal path

**Analogue:** PCI-DSS — industry standard ahead of federal mandate.

**Would update if:** BMIA mandates function-based SOC list → IGSC upgrade essentially certain; revise to ≥0.80.

**Conf:** M

---

### P = 0.05 (2027-12) / 0.08 (2028-06) — Federal frontier pause (bio-motivated)

**Claim:** Near-zero federal pause driven specifically by bio/CBRN salience.

**Why:** Pause politically toxic (`research_ai_pause_advocacy_playbook`: FLI letter zero effect; natsec hawks anti-pause; Trump EO 14409 pro-innovation). Bio-motivated pause **narrower** than general pause — still loses to "beat China" + open-science framing. 0.05–0.08 allows black-swan (Tier-3 attack + election shock), not modal.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §Executive summary, §1.4, §1.5
- `../supplements/node2_cbrn_full.md` §Modal path
- EO 14409 (no mandatory licensing)

**Analogue:** 2023 pause letter — maximum awareness, zero law.

**Would update if:** Bipartisan bio-motivated training moratorium introduced with committee passage → revise to ≥0.15.

**Conf:** H

---

### P = 0.10 (2027-12) / 0.15 (2028-06) — Biology FM weight gating (Evo-class)

**Claim:** Low probability of binding US rule restricting Evo-class open weights.

**Why:** Evo2 full open (Nature Mar 2026); Arc open-science default; AlphaFold3 gating debate showed **pushback** on weight restriction. No binding US biology-FM release rule exists (`10_biosecurity_evo_dual_use.md` §4). Policy momentum on **(C) synthesis screening**, not **(B) FM gating** — explicit Node 2 dual pathway.

**Evidence:**
- https://www.nature.com/articles/s41586-026-10176-5 (Evo2)
- `../supplements/biosecurity_evo_dual_use.md` §4, §6 Q3
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §6 (open weights vs gated debate)
- `../supplements/node2_cbrn_full.md` §Modal path, §Dual pathway

**Analogue:** AlphaFold3 — gated weights, not banned; Evo took opposite default.

**Would update if:** Tier-3 attack traced to open Evo2 weights + bipartisan release-restriction bill → revise to ≥0.30.

**Conf:** L

---

### P = 0.25–0.35 — GAAIA federal preemption of state AI laws (by 2028)

**Claim:** Tail risk that GAAIA-class bill preempts RAISE/SB 53 enforcement by 2028.

**Why:** GAAIA discussion draft (Jun 2026): frontier audits + **3-yr state development preemption**. Cruz moratorium stripped 99–1 (Jul 2025) but preemption fight repeats (`research_ai_pause_advocacy_playbook`). ~$8.5M Q1 2026 lobbying on preemption. Not modal — states currently winning — but non-trivial tail.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §1.2 (GAAIA, preemption)
- `../supplements/node2_cbrn_full.md` §RAISE tail

**Analogue:** Cruz BBB moratorium attempt — failed but revealed industry priority.

**Would update if:** Preemption passes → RAISE enforcement P drops sharply; Node 2 falsifier on state path.

**Conf:** M

---

## Tail branches (conditional on Tier 2 live)

### P = 0.55 — MODAL branch

**Claim:** ~55% of Tier-2 futures: BMIA/EU screening passes; RAISE/SB 53 reporting; IGSC upgrade; CBRN evals stay voluntary.

**Why:** Largest mass because screening coalition is broadest (synthesis industry + natsec + frontier CEOs + bipartisan Senate). Decoupling of physical-layer vs in silico governance is structural (`../supplements/node2_cbrn_full.md` §Modal synthesis). Assigned 0.55 as modal slice of {0.55, 0.20, 0.15, 0.10} — not independent draw from literature.

**Evidence:**
- https://screendna.org/
- https://www.congress.gov/bill/119th-congress/senate-bill/3741
- `../supplements/node2_cbrn_full.md` §Tail branches
- `../supplements/ai_pause_advocacy_playbook.md` §1.5 (screening > pause coalition)

**Analogue:** Post-2001 airport security — mandatory physical screening, not "stop flying."

**Would update if:** BMIA + EU both fail by 2028 despite Jun 2026 coalition → MODAL branch was wrong (Node 2 falsifier).

**Conf:** L (exact branch P); M (directional)

---

### P = 0.20 — TAIL-A: Tier 3 low-skill before reg catches up

**Claim:** ~20%: first documented low-skill attack **or** classified end-to-end demo before screening deployed at scale.

**Why:** Evo2 ASR scaling; DBTL closure; non-IGSC vendors; 50bp delay create window. Not modal because RAND + no public Tier-3 yet, but GeneBreaker shows skilled-actor path is live — low-skill is **extrapolation** not confirmation. 0.20 = substantial tail, not majority.

**Evidence:**
- https://arxiv.org/abs/2505.23839
- RAND RBA4087-1
- `../supplements/biosecurity_evo_dual_use.md` §3.3
- `../supplements/node2_cbrn_full.md` §TAIL-A

**Analogue:** Aum Shinrikyo — small group, high skill; Tier-3 tail asks if skill floor drops further.

**Would update if:** Documented Tier-3 attack → reweight TAIL-A up, MODAL down.

**Conf:** L

---

### P = 0.15 — TAIL-B: Regulatory delay (12–18 mo after near-miss)

**Claim:** ~15%: near-miss or incident occurs but rules bite only after 12–18 mo lag.

**Why:** Trump deregulation; OSTP limbo; preemption fights; industry preference for voluntary compliance. COVID policy lag analogue in Node 2 hybrid rule. Smaller than MODAL because Jun 2026 coalition may front-run incident.

**Evidence:**
- EO 14409
- `../supplements/ai_pause_advocacy_playbook.md` §1.2
- `../supplements/node2_cbrn_full.md` §TAIL-B, §Hybrid rule

**Analogue:** COVID test rollout — capability existed, regulatory response lagged.

**Would update if:** BMIA signed within 6 mo of near-miss → TAIL-B overestimated.

**Conf:** L–M

---

**Would update if:** US–CN joint synthesis treaty (P≈0.03) somehow passes → TAIL-C collapses.

**Conf:** L

---

## Actor table

### P = 0.70 — US executive: voluntary 30-day cyber/frontier review (EO 14409)

**Claim:** ~70% that covered frontier developers **participate** in voluntary pre-release review framework through 2027.

**Why:** EO 14409 (Jun 2 2026) creates structured voluntary pathway; soft pressure from contracts, "trusted partner" access, natsec engagement. Not 0.90+ because participation explicitly non-mandatory and some labs may opt out (Meta, open-weight shops).

**Evidence:**
- https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- https://www.cooley.com/news/insight/2026/2026-06-08-ai-executive-order-creates-voluntary-framework-for-frontier-models-advances-critical-infrastructure-cybersecurity
- `../supplements/ai_pause_advocacy_playbook.md` §1.2

**Analogue:** Voluntary SOC 2 — market pressure drives compliance without mandate.

**Would update if:** Major lab publicly refuses all EO 14409 engagement with no commercial penalty → revise to ≤0.50.

**Conf:** M

---

### P = 0.12 — US executive: mandatory CBRN licensing blocked / prevented

**Claim:** ~12% that executive branch **actively blocks or prevents** mandatory CBRN licensing if Congress moves — low but non-zero veto/agency-nullification tail.

**Why:** EO 14409 already constrains EO-based mandate. Trump admin would likely veto bio-blocking bill if rare passage occurs. 0.12 = executive successfully kills mandate, not P(mandatory CBRN passes).

**Evidence:**
- EO 14409 § "Nothing... mandatory licensing"
- `../supplements/node2_cbrn_full.md` §Actor table (US executive)
- `../supplements/ai_pause_advocacy_playbook.md` §1.2

**Analogue:** Sustained veto on natsec tech — rare.

**Would update if:** CBRN block bill passes both chambers with veto-proof margin → estimate wrong.

**Conf:** L–M

---

### P = 0.35 — US executive: OSTP 50bp revision proceeds

**Claim:** ~35% executive branch revives or revises OSTP 50bp + function-based SOC timeline by end-2027.

**Why:** EO 14292 paused Oct 2026 deadline; BMIA may supersede OSTP track. Commerce-led BMIA fits admin preference.

**Evidence:**
- OSTP Framework 2024 (`../supplements/biosecurity_evo_dual_use.md` §4)
- https://ari.us/cotton-klobuchar-intro-biosecurity-modernization-and-innovation-act-to-address-ai-era-biosecurity-risks/
- `../supplements/node2_cbrn_full.md` §Actor table

**Analogue:** Deferred agency rules revived under new lead agency.

**Would update if:** BMIA signed → OSTP revision moot.

**Conf:** L–M

---

### P = 0.45 — US Congress: bio screening legislation (BMIA-class)

**Claim:** ~45% BMIA-class mandatory screening enacted by end-2027 — same as modal regulatory P, Congress actor slice.

**Evidence:**
- https://www.congress.gov/bill/119th-congress/senate-bill/3741
- https://screendna.org/
- `../supplements/node2_cbrn_full.md` §Actor table

**Analogue:** See BMIA modal section above.

**Would update if:** Committee markup in 2026 → ≥0.55.

**Conf:** M

---

### P = 0.20 — US Congress: explicit CBRN eval mandate

**Claim:** ~20% Congress passes explicit federal CBRN third-party eval with teeth by 2028.

**Why:** Industry unites against release blocks; screening coalition does not extend. Amodei proposal not yet bill.

**Evidence:**
- https://darioamodei.com/post/policy-on-the-ai-exponential
- `../supplements/node2_cbrn_full.md` §Actor table

**Analogue:** SB 1047 veto path.

**Would update if:** Bipartisan CBRN eval bill with lab support → revise up.

**Conf:** M

---

### P = 0.05 — US Congress: frontier pause

**Claim:** ~5% Congress enacts frontier pause by 2028.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §1.2, §1.4
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** H

---

### P = 0.50 — DNA synthesis industry: major IGSC upgrade (v4-class)

**Claim:** ~50% IGSC delivers major protocol upgrade by end-2027.

**Evidence:**
- https://screendna.org/
- https://genesynthesisconsortium.org/
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** M

---

### P = 0.30 — DNA synthesis industry: compliance without law

**Claim:** ~30% enhanced screening covers ≥80% US synthesis volume **before** federal mandate.

**Why:** IGSC members + letter signatories; non-members and benchtop gap cap at 0.30.

**Evidence:**
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.3
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** L–M

---

### P = 0.75 — Frontier labs: CBRN mitigations ship

**Claim:** ~75% frontier labs ship visible CBRN mitigations on major releases through 2027.

**Why:** RSP / Preparedness / Sleeper Agents → patch not pause.

**Evidence:**
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §2.1
- `https://arxiv.org/abs/2310.11436`
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** M–H

---

### P = 0.02 — Frontier labs: stop training

**Claim:** ~2% major frontier lab stops training (bio-motivated) by 2028.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §1.3
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** H

---

### P = 0.40 — Frontier labs: public Tier-2 disclosure under RAISE/SB 53

**Claim:** ~40% public disclosure of Tier-2-class finding via reporting/leak by 2028.

**Why:** RAISE reports confidential to NY DFS; public = leak + strategic transparency subset.

**Evidence:**
- https://legislation.nysenate.gov/pdf/bills/2025/a9449
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** L–M

---

### P = 0.60 — China: domestic screening enforcement ↑

**Claim:** ~60% CN tightens synthesis screening enforcement through 2028.

**Evidence:**
- `../supplements/node2_cbrn_full.md` §Actor table (China)
- `../supplements/ai_pause_advocacy_playbook.md` §1.4

**Conf:** L–M

---

### P = 0.08 — China: FM weight gating

**Claim:** ~8% CN binding restrictions on open biology FM weights.

**Evidence:**
- `../supplements/biosecurity_evo_dual_use.md` §4
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** L

---

### P = 0.03 — China: US–CN joint bio-AI treaty

**Claim:** ~3% formal joint treaty by 2028.

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §1.2, §1.4

**Conf:** L

---

### P = 0.55 — EU: Biotech Act adoption with screening intact (by 2028)

**Claim:** ~55% cumulative by 2028 — aligns actor table with modal EU track extended horizon.

**Evidence:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52025PC1022%2801%29
- `../supplements/node2_cbrn_full.md` §Actor table (EU)

**Conf:** M

---

### P = 0.30 — EU: CBRN eval mandate for GPAI

**Claim:** ~30% EU mandates CBRN eval for GPAI/high-risk in biotech context by 2028.

**Evidence:**
- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html` §3 (FAR.AI EU CBRN consortium)
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** L–M

---

### P = 0.08 — Public: mass bio-x-risk protest

**Claim:** ~8% sustained mass protest framing AI bio-x-risk by 2028 (no Tier-3).

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §1.4
- `../supplements/node2_cbrn_full.md` §Actor table

**Conf:** L–M

---

### P = 0.25 — Public: sustained media >2 mo given Trigger E

**Claim:** Conditional on Trigger E, ~25% media sustains >2 months.

**Evidence:**
- `../supplements/node2_cbrn_full.md` §Actor table, §Trigger E

**Conf:** L

---

## p(doom) conditional claims

### P(extinction | MODAL branch) — Low (~1–3% of all extinction mass by 2050)

**Claim:** MODAL governance leaves AI-enabled bio at ~1–3% of total extinction mass by 2050 (not misalignment path).

**Why:** Screening + RAISE shrink skilled-actor tail; Adelstein ~8–10% bio-inclusive total — MODAL discounts slice.

**Evidence:**
- `../supplements/pdoom_methodology.md`
- `../supplements/node2_cbrn_full.md` §p(doom) link

**Analogue:** Nuclear terrorism — gated by access.

**Would update if:** Tier-3 under full MODAL rules → estimate failed.

**Conf:** L (quant); M (direction)

---

### P(extinction | TAIL-A) — Moderate–high within bio bucket

**Claim:** Tier 3 before screening → moderate–high within Adelstein bio bucket; single pandemic tail, not misalignment.

**Evidence:**
- `../supplements/node2_cbrn_full.md` §TAIL-A, §p(doom)
- RAND RBA4087-1

**Conf:** L

---

### P(extinction | TAIL-B) — Moderate

**Claim:** 12–18 mo delay after near-miss → moderate bio extinction risk during gap window.

**Evidence:**
- `../supplements/node2_cbrn_full.md` §TAIL-B

**Conf:** L

---

### P(extinction | TAIL-C) — Moderate

**Claim:** Open weights + arbitrage + eval gaming → moderate chronic risk.

**Evidence:**
- `https://arxiv.org/abs/2310.11436`
- `../supplements/biosecurity_evo_dual_use.md`
- `../supplements/node2_cbrn_full.md` §TAIL-C

**Conf:** L

---

### P(Tier 3 before adequate screening | Tier 2 by 2027) > ~0.15 — crux

**Claim:** Above ~15%, bio bucket dominates misalignment in Adelstein split (~2.6% misalignment vs ~5–8pp bio).

**Why:** TAIL-A weight 0.20 minus partial mitigation ≈ crux threshold. Weight by branch P; no double-count.

**Evidence:**
- `../supplements/node2_cbrn_full.md` §Crux
- `../supplements/pdoom_methodology.md` §Why community numbers differ

**Would update if:** BMIA + GeneBreaker mitigations → P(Tier 3 | Tier 2) <0.10.

**Conf:** M (logic); L (threshold)

---

### P(weighting) — No double-count MODAL + tails

**Claim:** Weight branch p(doom) claims by P(MODAL)=0.55, P(TAIL-A)=0.20, etc.

**Evidence:**
- `../supplements/node2_cbrn_full.md` §Double-counting guard

**Conf:** H

---

## Sandbagging cross-cut

### P(confound) — Public evals alone unreliable for Tier assignment

**Claim:** Tier 1–2 from public WMDP scores are lower bounds; sandbagging/eval-awareness inflates apparent safety.

**Why:** Goodfire +3–18 pp refusal when aware; elicited sandbagging −35–40% WMDP (`evaluation_awareness_llms.md`).

**Evidence:**
- https://www.goodfire.ai/research/verbalized-eval-awareness-inflates-measured-safety
- https://www.wmdp.ai/
- `https://arxiv.org/abs/2310.11436` §2, §11
- `../supplements/node2_cbrn_full.md` §Sandbagging crux

**Conf:** H

---

## Index

| Category | Sections |
|----------|----------|
| Hybrid timing | 5 |
| Tier status | 4 |
| Trigger E | 6 |
| Modal regulatory | 10 |
| Tail branches | 4 |
| Actor table | 18 |
| p(doom) | 6 |
| Sandbagging | 1 |
| **Total** | **54** |

## External sources (consolidated)

- WMDP: https://www.wmdp.ai/
- GeneBreaker: https://arxiv.org/abs/2505.23839
- RAND RBA4087-1: https://www.rand.org/pubs/research_briefs/RBA4087-1.html
- screendna letter: https://screendna.org/
- BMIA S.3741: https://www.congress.gov/bill/119th-congress/senate-bill/3741
- EO 14409: https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- EU Biotech Act: https://health.ec.europa.eu/publications/proposal-regulation-establish-measures-strengthen-unions-biotechnology-and-biomanufacturing-sectors_en
- RAISE NY: https://legislation.nysenate.gov/pdf/bills/2025/a9449
- Goodfire eval awareness: https://www.goodfire.ai/research/verbalized-eval-awareness-inflates-measured-safety

---

## Phase 2b — Synthetic media / epistemic collapse & BMIA politics (crosscut §3)

> **Source:** [`crosscut_secondary_cruxes.md`](./crosscut_secondary_cruxes.md) §3 — ranked **#7** leverage on **19%** extinction (+1–3pp if BMIA-fail tail).  
> **Parent link:** Extends P(BMIA)=0.45 load-bearing P #2; MODAL branch 0.55; TAIL-B regulatory delay 0.15.

### Claim — democracy can't pass BMIA when epistemic infrastructure collapses

By 2027–2028, **synthetic media + AI-generated persuasion** degrades democratic **epistemic infrastructure** enough that **physical-layer** consensus (BMIA, screening mandates) fails in Congress — even when insider/natsec coalition favors it. Not extinction-direct; **enables bio tail** by blocking Cluster B (`correlation_matrix.md`).

**Node 2 bottleneck:** BMIA bipartisan (Cotton–Klobuchar Jan 2026); screendna coalition — **elite** consensus exists (§P=0.45 BMIA modal); **public epistemic** environment is the bottleneck for **floor vote**, not committee drafting.

---

### P(modal / tail) — epistemic outcomes and BMIA timing

| Outcome | P | Window | BMIA effect |
|---------|---|--------|-------------|
| **Modal:** Epistemic noise **slows** BMIA ~6–12 mo; passes by 2028 | **0.55** | 2027–2028 | P(BMIA by 2027-12) stays **~0.45**; slips to mid-2028 (§0.60 horizon) |
| **Tail:** Epistemic collapse — **BMIA fails** 119th Congress; screening stays patchwork | **0.30** | 2027-12 | Load-bearing P #2 **↓** to **~0.25–0.30** |
| **Tail:** "Chernobyl for trust" — election/deepfake crisis → **punctuation** that **helps** screening coalition | **0.15** | 2026–2028 | P(BMIA) **↑** to **~0.55–0.65**; strange-bedfellows |

**Interaction with load-bearing P #2:**

```
P(BMIA by 2027-12) baseline = 0.45  (§Modal regulatory BMIA section)
This crux explains downside mass on that estimate — epistemic tail = primary BMIA-fail mechanism
P(BMIA-fail | epistemic collapse tail) ≈ 0.55–0.65 conditional
```

**Correlation warning:** Do not multiply P(epistemic tail) × P(BMIA fail) × P(no pause) — use scenario branches (`my_pdoom.md` §Branch model).

---

### Evidence — survey vs action, Kingdon, political deepfakes

| Stream | Detail | BMIA relevance |
|--------|--------|----------------|
| **Survey vs action gap** | 70–84% support AI regulation; **no** federal pause after FLI 2023 | Broad support **≠** floor vote under noise — `ai_governance_political_strategy.md` §Executive summary |
| **Kingdon problem stream** | Weak for x-risk; **moderate** for deepfakes/jobs/child safety — §1.4 | BMIA is **narrower** than pause but still needs **trustworthy deliberation** |
| **Political deepfakes** | 84% support ban (`ai_governance_political_strategy.md`); Grok non-consensual deepfake crisis Jan 2026 | **Salience ↑, institutional trust ↓** — dual effect |
| **Open Q §6.3** | Non-catastrophic focusing event (deepfake election, AI flash crash) — may punctuate **or** polarize | Maps to 0.15 punctuation tail vs 0.30 collapse tail |
| **Node 4 media fatigue** | Downs 6–10 wk peaks (Node 4 §20) — synthetic flood **accelerates fatigue** | BMIA debate drowned in synthetic noise |
| **Elite vs public gap** | screendna Jun 2026 — CEOs + natsec **for** screening | Congress needs **legible** public consensus — epistemic collapse breaks legibility |

---

### Epistemic collapse — delaying the BMIA coalition

**Mechanism:** BMIA coalition = synthesis industry + natsec + frontier CEOs + bipartisan Senate (**elite**). Passage requires:

1. Committee markup without poison pills  
2. Floor time not consumed by higher-salience synthetic crises  
3. **Credible** technical debate — not dismissed as "deepfake transcript of Cotton"  
4. Governor/executive not vetoing under election-year chaos  

**Epistemic collapse tail (P=0.30) breaks (2) and (3):**

| Failure channel | Example | Effect on P(BMIA by 2027-12) |
|-----------------|---------|------------------------------|
| Synthetic flood drowns committee debate | Fake "leaked" BMIA draft with absurd caps | Markup delayed → TAIL-B 0.15 overlap |
| Disinformation targets sponsors | Fake Klobuchar/Cotton quotes on "AI ban" | Bipartisan bridge **fractures** |
| Public can't distinguish real vs synthetic expert testimony | Deepfake Amodei "oppose screening" | Industry endorsement **neutralized** |
| Media fatigue | Node 4 §20 — 6–10 wk peaks | BMIA becomes "another AI panic" |

**Link TAIL-B (§P=0.15):** Near-miss or insider salience occurs but rules bite only after 12–18 mo lag — epistemic collapse **extends** TAIL-B by blocking **focused** post-near-miss window.

**Link MODAL branch (§P=0.55):** BMIA passes but **6–12 mo late** — Tier 2 live window (§Hybrid timing) **unchanged**; P(Tier 3 before screening) load-bearing P #3 **↑** modestly.

---

### Deepfake election cycle — 2026–2028 punctuation risk

**Claim:** 2026–2028 US election cycles intersect peak synthetic-media capability — **bifurcated** tail:

| Path | P | Mechanism | BMIA |
|------|---|-----------|------|
| **Collapse** | subset of 0.30 tail | Election-year synthetic chaos → **no** trustworthy legislative process | BMIA dies in committee |
| **Punctuation ("Chernobyl for trust")** | **0.15** | Deepfake election crisis → creatives + natsec + synthesis industry **strange bedfellows** | P(BMIA) **↑** — `ai_governance_political_strategy.md` §5 labor + deepfake + natsec package |

**Evidence — Grok Jan 2026:** Non-consensual deepfake crisis — **salience ↑, institutional trust ↓** simultaneously. Net direction **uncertain** — explains **both** tails in same event class.

**Deepfake election scenarios:**

```
2026 midterms / 2028 presidential cycle:
  - Synthetic candidate audio/video → litigation, not legislation
  - "Everything is fake" cynicism → voters discount **real** BMIA benefits
  - OR: High-profile election deepfake → NO FAKES / ELVIS coalition **bridges** to BMIA floor vote
```

**Node 6 gridlock interaction:** Epistemic collapse reinforces Node 6 §Gridlock 0.45 — federal dysfunction on **all** AI bills, not just GAAIA; BMIA **physical-layer** status may **not** exempt it from epistemic veto (unlike natsec classified track).

---

### Democracy capacity crux — load-bearing P #2 decomposition

**Crux statement:** US democracy can pass **narrow physical-layer** bio screening **iff** epistemic infrastructure supports **technical** policy debate. Synthetic media attacks **process legitimacy**, not screening science.

| Load-bearing P | Baseline | If epistemic collapse tail (0.30) | If punctuation tail (0.15) |
|----------------|----------|-----------------------------------|----------------------------|
| **P #2** P(BMIA by 2027-12) | **0.45** | **~0.25–0.30** | **~0.55–0.65** |
| **P #3** P(Tier 3 before screening \| Tier 2) | crux >0.15 | **↑** | **↓** |
| Bio tail branch 0.17×35% | priced | **↑** mass on bio tail | **↓** |

**Not extinction-direct:** Epistemic collapse does **not** cause misalignment; **enables bio tail** by blocking Cluster B (physical mitigation).

**p(doom) direction:**

| Path | Effect on 19% |
|------|---------------|
| BMIA-fail epistemic tail | **+2–4pp** — bio tail branch 0.17×35% more likely |
| Punctuation tail | **−1–2pp** — BMIA coalition punctuated |
| Modal delay only | **+0–1pp** — absorbed in existing 2028-06 P=0.60 |

---

### Would update if — falsifiers and confirmers

| Observation | Direction |
|-------------|-----------|
| BMIA dies in committee **with** documented synthetic-media disinformation campaign against sponsors; no substitute by 2028 | **Up (collapse tail)** |
| BMIA signed **despite** election-year synthetic flood | **Down (collapse)** — modal delay path confirmed |
| EU Biotech Act spillover forces US patchwork harmonization | **Down (collapse)** — external punctuation bypasses US epistemic failure |
| Major **authenticated-media** infrastructure (C2PA-scale adoption) restores baseline trust for **technical** policy debate | **Down (collapse)** |
| Deepfake election crisis → NO FAKES + BMIA **joint** floor package passes | **Up (punctuation tail)** |
| Trigger E near-miss (§P=0.25–0.35) **overcomes** epistemic noise | **Down (collapse)** — bio salience punctuates through synthetic fog |

---

### Links to existing nodes

| Node | Link |
|------|------|
| **N2 §P=0.45 BMIA** | Load-bearing P #2 — this crux explains downside mass |
| **N2 §Trigger E near-miss** | P=0.25–0.35 — may **puncture** epistemic fog (punctuation path) |
| **N2 §TAIL-B** | Regulatory delay 0.15 — epistemic collapse **extends** |
| **N4 §20 Media** | Fatigue; x-risk competes with jobs/deepfakes |
| **N6 §Gridlock** | 0.45 — epistemic collapse reinforces federal gridlock |
| **N1** | Labor shock coalitions — potential **bridge** (labor + deepfake) per `ai_governance_political_strategy.md` §5 |
| **`correlation_matrix.md`** | Cluster B physical mitigation vs Cluster C BMIA delay |

---

**Phase 2b status (Node 2):** 8 sections appended 2026-07-04. Crosscut §3 — zero omissions.

