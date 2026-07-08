> **Ported from:** `notes/timeline_prediction/node8_evidence_rationale.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 8 — Cyberwar / Critical Infrastructure: Evidence Rationale

> **Parent:** [`node8_cyber_infra.md`](./node8_cyber_infra.md)  
> **Date:** 2026-07-04  
> **Format:** Claim | Why | Evidence | Analogue | Would update if | Conf

Each section documents one probability or timing claim from Node 8. Probabilities are **subjective elicitation** unless noted as derived.

---

## Hybrid timing

### P(timing) — Capability: AI-for-cyber operational, modal window 2025 H2 – 2027

**Claim:** Frontier AI materially uplifts offensive cyber (vuln discovery, exploit chaining, OT mapping, agentic fraud) in the modal window **H2 2025 – 2027**, **before** C6 calendar anchor.

**Why:** Multiple **confirmed** 2026 incidents — Monterrey SCADA autonomous OT pivot (Jan 2026, Dragos); Mythos zero-day disclosure (Apr 2026); GTIG/CSA nation-state operationalization reports (May 2026). Capability layer runs **fast** like Node 5 open weights, not C5+ theft timing.

**Evidence:**
- https://lyrie.ai/research/research/2026-05-07-claude-agua-monterrey-ot-scada — first documented LLM end-to-end OT campaign
- https://www.anthropic.com/glasswing — Mythos Preview offensive cyber threshold
- https://safeguard.sh/resources/blog/gtig-ai-threat-tracker-nation-state-may-2026 — PRC/DPRK/RU/IR operational AI integration
- `<!-- private monorepo only -->` §3 (AI-for-cyber timeline)
- `<!-- private monorepo only -->` — gov response **same quarter** as capability jump

**Analogue:** GPT-4 jailbreak ecosystem matured ~6–12 mo post-release; cyber-agent uplift **faster** because state actors + criminals already had tooling pipelines.

**Would update if:** Through Dec 2027, no third-party replication of AI-assisted OT pivot **and** METR cyber autonomy evals flat → demote to 2028+.

**Conf:** M–H

---

### P(timing) — Policy salience: CI crisis calendar 2027 – 2029

**Claim:** **DC/mainstream** policy crisis (hearings, mandatory-testing debate, sector CIP overhaul) clusters **2027–2029**, not 2026 — unless Trigger E cascade fires early.

**Why:** Fable/Mythos (Jun 2026) created **elite** salience without mass outage. Hybrid rule from parent timeline: human-response calendar lags capability ~30%. Colonial Pipeline 2021 → statutory action **12+ mo**. Insider/regulator attention can lead public by 6–12 mo (Node 2 pattern).

**Evidence:**
- `../reference/03_ci_spine.md` — hybrid time rule
- `node2_evidence_rationale.md` — 12–18 mo regulatory lag
- `<!-- private monorepo only -->` — export recall **without** grid outage
- Colonial Pipeline 2021 → TSA Security Directive timeline

**Analogue:** SolarWinds Dec 2020 → sustained congressional cycle 2021–22.

**Would update if:** T8-A cascade before Q4 2026 → salience window **too slow**.

**Conf:** M

---

## Modal path

### P = 0.82 — State cyber remains espionage-dominant through 2028

**Claim:** ≥82% that **modal** state-linked cyber activity stays **espionage / fraud / ransomware**-weighted, not sustained kinetic-adjacent sabotage campaigns.

**Why:** CFR Cyber Operations Tracker (2005–2022): state ops overwhelmingly exfil, DDoS, disinformation — **Stuxnet-class OT sabotage rare**. AI lowers **cost** of sabotage but **escalation ladder** still disfavors repeated physical-effect ops by great powers. Forescout: OT-specific malware **still rare** vs IT.

**Evidence:**
- https://www.cfr.org/cyber-operations/ — reference class; 77% suspected ops from CN/RU/IR/KP
- `node3_evidence_rationale.md` §14 — CFR espionage dominance; Stuxnet rarity
- Monterrey attack = **attempted** OT access, not confirmed physical damage

**Analogue:** Decades of PRC IP theft on semiconductors without fab bombing.

**Would update if:** ≥2 confirmed state-linked OT **physical-effect** events (grid trip, water contamination) in 2026–27 → revise to ≤0.65.

**Conf:** M–H

---

### P = 0.97 — No kinetic war triggered by AI cyber crisis (P(kinetic) < 0.03)

**Claim:** P(US or ally **executes kinetic strike** primarily triggered by AI-assisted cyber CI crisis \| through 2028) **< 0.03**.

**Why:** Same escalation logic as Node 3 §14. TSMC mutual destruction; cyber retaliation **preferred**. AI 2027 discusses kinetic options; **scenario** not base rate. Huang Yen-nan (Dec 2025): cyber on TSMC **substitute** for military strike, not prelude.

**Evidence:**
- `node3_evidence_rationale.md` §14, §17 T1
- https://www.taiwannews.com.tw/news/6262405 — ex-digital minister: hacking TSMC **more practical** than force
- CFR Cyber Tracker — few kinetic follow-ons from cyber

**Analogue:** North Korea Sony 2014 — sanctions + cyber, not invasion.

**Would update if:** Documented US strike on PRC datacenter **after** CI cyber event → revise **≥0.10**.

**Conf:** M

---

### P = 0.70 — Export / access gating on cyber-capable frontier models expands by 2028

**Claim:** US expands **deemed-export / whitelist** gating on cyber-tier frontier APIs (Fable/Mythos class) to additional models or sectors by end-2028.

**Why:** **Precedent live** Jun 2026 — EAR on foreign-national API access; Mythos Annex A CI whitelist. Bipartisan natsec hawk baseline. Banks letter (Jun 2026) frames 防窃取 + misuse. Not 0.90+ because Mythos **partially lifted** Jul 2026; industry pushback (freefable.org).

**Evidence:**
<!-- private monorepo only: - `[private note]` — full timeline -->
- `node3_evidence_rationale.md` §10 — export ctrl P≈0.70
- https://www.anthropic.com/news/fable-mythos-access

**Analogue:** ITAR expansion after satellite tech leaks — sector-specific, not industry halt.

**Would update if:** Jul 2026 restrictions become **permanent global ban** on all cyber models with **no** whitelist path → revise **0.85+**.

**Would update if:** All Fable/Mythos controls lifted with **no** replacement framework by 2027 → revise **≤0.45**.

**Conf:** M–H

---

### P = 0.65 — CI defensive AI partnerships (Glasswing-class) scale by 2028

**Claim:** ≥1 major frontier lab runs **structured** CI vulnerability-hunting program with **≥50** critical-infrastructure partners by 2028.

**Why:** Glasswing announced Apr 2026 with explicit CI scope; Mythos as tool; gov co-funding narrative. Post-Mythos, **defensive** story is politically easier than offensive release. CISA Dec 2025 OT+AI joint guidance creates bureaucratic hook.

**Evidence:**
- https://www.anthropic.com/glasswing
- CSA research note May 2026 — CISA/NSA/NIST Cyber AI Profile draft
- `<!-- private monorepo only -->` §3 — defense vendors (Gray Swan, Asymmetric)

**Analogue:** MS-ISAC expansion after sector breaches — voluntary → quasi-standard.

**Would update if:** Glasswing **canceled** or **<10** partners through 2027 → revise **≤0.35**.

**Conf:** M

---

### P = 0.60 — EO 14409 voluntary CI / frontier cyber review uptake through 2027

**Claim:** ~60% of covered frontier developers **participate** in EO 14409 voluntary pre-release / CI security engagement through 2027.

**Why:** Same mechanism as Node 2 actor row (P≈0.70) — slightly lower here because cyber-specific track newer and Meta/open-weight shops may opt out. EO explicitly names critical infrastructure cybersecurity.

**Evidence:**
- https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- https://www.cooley.com/news/insight/2026/2026-06-08-ai-executive-order-creates-voluntary-framework-for-frontier-models-advances-critical-infrastructure-cybersecurity
- `node2_evidence_rationale.md` §EO 14409

**Analogue:** Voluntary SOC 2 — commercial pressure not mandate.

**Would update if:** ≥2 frontier labs publicly refuse EO engagement with no contract penalty → **≤0.45**.

**Conf:** M

---

### P = 0.55 — US offensive cyber surge post salient CI crisis (modal)

**Claim:** P(US IC/CyberCom **significantly expands** offensive cyber operations against adversary CI/AI infra within 12 mo of salient Trigger E) ≈ **0.55**.

**Why:** Node 3 IC actor row P(offensive cyber)=**0.55** — same institutional reflex. Theft crisis and CI crisis **both** increase hunt-forward tempo without kinetic default. Stuxnet proved willingness for **sabotage** in cyber domain; AI 2027 Security Forecast: sabotage ramps 2027.

**Evidence:**
- `node3_evidence_rationale.md` §16 — US IC actor table
- CFR — Stuxnet as rare offensive template
- `<!-- private monorepo only -->` — security appendix sabotage ramp

**Analogue:** SolarWinds → offensive counter-intel + public attribution pressure, not invasion.

**Would update if:** Documented **stand-down** of offensive cyber after major CI event → **≤0.25**.

**Conf:** M

---

### P = 0.35 — Federal OT segmentation / CIP upgrade mandate by 2028

**Claim:** ~35% chance of **binding** federal requirement for IT/OT segmentation, MFA on OT management interfaces, or NERC CIP equivalent upgrade **passed/enforced** by 2028.

**Why:** CISA/FBI AA26-097a (Apr 2026) Iranian OT targeting — advisory not mandate. Sector resistance + legacy PLC constraints. **Higher** than training-cap P because **bipartisan CI** support; **lower** than export gating because OT retrofit **expensive**.

**Evidence:**
- Lyrie/Dragos Monterrey report — weak OT auth, IT-OT bridge
- https://postquantum.com/cyber-kinetic-security/ai-offensive-capabilities-critical-infrastructure-ot/ — segmentation recommendations
- Colonial Pipeline → TSA SD-02D precedent (sector-specific mandate)

**Analogue:** Post-9/11 aviation security — slow mandatory retrofit.

**Would update if:** T8-A cascade → mandate P **≥0.60** within 18 mo.

**Conf:** L–M

---

### P < 0.08 — Training pause or cyber-driven frontier slowdown

**Claim:** P(frontier labs **halt >30d** or US **caps training** primarily due to CI cyber crisis) **< 0.08**.

**Why:** Node 3 + Node 2 establish pause coalition weakness. Fable response = **gating deployment**, not stopping training. Natsec hawks frame cyber lead as **race imperative** (Glasswing: "maintain decisive lead").

**Evidence:**
- `../supplements/ai_pause_advocacy_playbook.md` §1.2
- `node3_evidence_rationale.md` §15
- Anthropic Glasswing — offensive **and** defensive; no pause rhetoric

**Analogue:** Post-Colonial Pipeline — no oil-industry compute cap.

**Would update if:** ≥2 labs public halt after CI cascade → **≥0.20**.

**Conf:** M–H

---

## OT / energy / water

### P = 0.40 — AI-assisted OT attack **attempt** per year (US critical sector, 2027)

**Claim:** ~40% annual probability of **credible** AI-assisted attempt against US OT-connected CI (energy, water, transport) in 2027.

**Why:** Monterrey demonstrated playbook exportability. Iran Nimbus Manticore post–Feb 2026 kinetic ops **↑** CI tempo (CSA note). Base rate of OT attempts rising; AI fraction still **minority** of total — hence 0.40 not 0.80.

**Evidence:**
- https://lyrie.ai/research/research/2026-05-07-claude-agua-monterrey-ot-scada
- CSA Nimbus Manticore note — Iran aviation/defense + CI retaliation frame
- FBI/CISA joint advisories 2026 on OT targeting

**Analogue:** Ransomware OT attempts ~2019–21 base rate before AI — AI **multiplies** attempts, not replaces all.

**Would update if:** Zero AI-attributed OT attempts 2026–27 in US → **≤0.20**.

**Conf:** L–M

---

### P = 0.12 — Confirmed OT **physical effect** from AI-assisted attack (US, by 2028)

**Claim:** ~12% cumulative through 2028 for AI-assisted attack causing **measurable** physical effect (outage, unsafe process state, ≥1hr service disruption) on US CI.

**Why:** Most OT campaigns **fail** at IT-OT boundary; safety systems, manual overrides. Monterrey **attempted** password spray on SCADA — outcome limited. Higher than pre-AI decade because barrier **lowered**; still **<<** attempt rate.

**Evidence:**
- Monterrey case — mapping + exploit gen; physical effect unclear/limited
- Forescout OT malware rarity (cited in Node 3)
- Postquantum OT analysis — PLCs lack endpoint agents; exploitation ≠ sustained control

**Analogue:** Triton/Trisis 2017 — rare success; years between major OT physical events.

**Would update if:** 2027 US grid event **confirmed** AI-assisted → **≥0.25** for 2028 tail.

**Conf:** L

---

## Financial / agentic fraud

### P = 0.92 — Agentic / AI-enhanced fraud remains **industrialized** (modal, 2025–28)

**Claim:** ≥92% that AI-enhanced fraud stays **high-volume modal harm** — not a tail — through 2028.

**Why:** **Already observed** at scale: Interpol $442B global fraud 2025; FBI IC3 $893M **reported** AI-enabled US fraud 2025 (true toll higher). Agentic pipelines documented (Arkose Gen 3 agents; ScamAgents academic work). 4.5× profitability vs traditional (Interpol).

**Evidence:**
- https://thenextweb.com/news/global-scam-economy-442-billion-ai-fraud-yahoo-boys
- https://www.arkoselabs.com/blog/agentic-ai-fraud
- https://www.secureworld.io/industry-news/ai-enabled-fraud-topped-893m-fbi
- Kroll 2025 — deepfake BEC, synthetic KYC

**Analogue:** Email phishing 2000s — became background condition, not policy crisis per incident.

**Would update if:** Global AI-fraud losses **fall** YoY 2026–27 with effective sector-wide defense → revise modal harm trajectory.

**Conf:** H

---

### P = 0.35 — Single-institution **>$1B** loss from AI-agent fraud episode (by 2028)

**Claim:** ~35% cumulative probability of one financial institution or corporate treasury losing **>$1B** in a single AI-agent fraud campaign by 2028.

**Why:** Arup $25.6M (2024) and Singapore $499K (2025) prove executive deepfake path; agentic **scale** + persistence raises tail. $1B requires systemic treasury or market-manipulation tail — **not** median but **plausible** before 2028.

**Evidence:**
- TechTimes / Kroll — Arup deepfake video conference
- Interpol — agentic end-to-end campaigns
- WEF Global Cybersecurity Outlook 2026 — 73% CEOs affected by cyber-enabled fraud

**Analogue:** Nick Leeson / Société Générale — single-actor large loss; AI **lowers skill floor**.

**Would update if:** Confirmed $1B+ case in 2026 → revise 2028 tail **≥0.55**.

**Conf:** L–M

---

### P = 0.30 — Salient cyber Trigger E is **financial** not OT (conditional on any E)

**Claim:** Given a Node 8 Trigger E fires, ~30% it is **primarily financial** (>$10B aggregate or systemic payment stress) vs OT/grid.

**Why:** Fraud base rate **>>** OT physical success. OT events **rarer** but **more** DC salient — so financial E must be **large** to compete. 30% reflects **size** threshold for financial E vs **lower** threshold for OT E.

**Evidence:**
- Interpol industrialization frame
- Node 8 main doc — Trigger E definition
- Colonial vs fraud — fraud rarely triggers same emergency powers

**Analogue:** 2008 financial crisis vs regional blackout — different political triggers.

**Would update if:** OT cascade occurs → financial-primary E **overestimated**.

**Conf:** L

---

## Supply chain: TSMC / ASML / HBM

### P = 0.88 — Semiconductor supply-chain cyber espionage continues (modal)

**Claim:** ≥88% that state-linked espionage against TSMC ecosystem, ASML IP, and HBM suppliers **continues** through 2028 without sustained fab sabotage.

**Why:** Proofpoint Jul 2025 — three PRC groups targeting Taiwan semi **Mar–Jun 2025**; "persistent threat... constant interest." Tata Electronics breach 2026 exposed TSMC/Apple specs — **supplier tier** weakest link. Aligns with CFR espionage modal.

**Evidence:**
- https://www.reuters.com/technology/cybersecurity/china-linked-hackers-target-taiwan-chip-industry-with-increasing-attacks-researchers-say-2025-07-16/
- Reuters Tata Electronics / World Leaks 2026 — 630GB supplier docs
- `<!-- private monorepo only -->` — TSMC/CoWoS/HBM bottlenecks (motivation to steal, not destroy)

**Analogue:** ASML IP theft attempts decade-long; no EUV kinetic strikes.

**Would update if:** Fab **production halt** from cyber **attributed** to state actor → espionage-only modal wrong.

**Conf:** M–H

---

### P = 0.15 — Cyber sabotage on HBM/CoWoS **bottleneck** supplier causes ≥2-week global AI compute delay

**Claim:** ~15% cumulative (2026–28) for cyber sabotage on HBM packaging or CoWoS-adjacent supplier causing **≥2 week** frontier GPU shipment delay.

**Why:** Bottlenecks concentrated (SK Hynix HBM, TSMC CoWoS). Supplier OT bridges exist (Tata-style). **Lower** than espionage P because destruction **harms all** including attacker supply chain; **higher** than kinetic TSMC P because **remote** feasible.

**Evidence:**
- `<!-- private monorepo only -->` — post-2027 wafer/packaging constraints
- Tata breach — supplier tier compromise
- Huang Yen-nan — ransomware on supply chain **profitable**

**Analogue:** 2017 NotPetya shipping/logistics spillover — unintended cascade.

**Would update if:** Confirmed HBM line halt from cyber → **≥0.30**.

**Conf:** L

---

### P < 0.04 — Kinetic strike on TSMC/fab **triggered by** cyber campaign

**Claim:** P(kinetic attack on Taiwan fabs **as direct response** to AI/cyber semi campaign) **< 0.04**.

**Why:** Decoupled to Node 3 / Taiwan geopolitics. Cyber on TSMC is **alternative** to invasion (Huang 2025), not automatic escalation to missiles.

**Evidence:**
- https://www.taiwannews.com.tw/news/6262405
- Node 3 §14 kinetic P<0.02 for datacenter strike — fab strike similarly constrained

**Conf:** L–M

---

## Tail branches

### P = 0.10 — T8-A: "AI cyber 9/11" multi-sector cascade (central)

**Claim:** ~10% cumulative (through 2028) for coordinated or tightly-spaced incidents causing **≥2** of {regional grid outage ≥24h, water/treatment unsafe state, financial payment rail disruption ≥48h, transport hub shutdown} with **AI assistance** attributed.

**Why:** Barrier to each individual event **moderate**; **joint** tail lower. Mythos collapses disclose-to-exploit window (Bridewell). Iran CI retaliation tempo post-2026. **Not** 0.01 — AI agent velocity breaks human SOC timescales.

**Evidence:**
- Bridewell Mythos analysis — CTEM urgency; ML detection required
- CSA Iran notes — CI retaliation **assessed likely**
- Colonial Pipeline — single-sector precedent; cascade requires coordination or shared vuln

**Analogue:** 2003 Northeast blackout (cascade) — rare; AI **raises** conditional P.

**Would update if:** 2026–27 multi-sector event occurs → **≥0.20** for remaining window.

**Conf:** L

---

### P = 0.18 — T8-B: Emergency FAA-style mandatory cyber testing law (by 2028)

**Claim:** ~18% that US passes or **seriously enacts** (not just proposes) mandatory third-party frontier **cyber** capability testing after incident or Fable-class sequel.

**Why:** Amodei Jun 2026 FAA analogy **before** law. Bipartisan CI appetite **higher** than training-cap appetite. **Below** 0.30 because EO 14409 explicitly **blocks** mandatory licensing interpretation; Cruz coalition; industry lobbying.

**Evidence:**
- `readings/Dario_Amodei_Policy_on_the_AI_Exponential_2026.md` / Anthropic policy essay
- `<!-- private monorepo only -->` — Dario FAA frame → ban 48h later
- `../supplements/ai_pause_advocacy_playbook.md` — mandatory licensing blocked in EO

**Analogue:** Post-9/11 TSA — emergency security agency; **partial** avionics testing parallel.

**Would update if:** T8-A fires → P **≥0.40** within 12 mo.

**Conf:** L–M

---

### P = 0.12 — T8-C: Surveillance / preemptive access tail (without sunset)

**Claim:** ~12% that emergency response includes **durable** expansion of transaction AI monitoring, biometric API gating, or bulk comms surveillance **without** 5-year sunset — civil-liberty tail.

**Why:** Fable foreign-national ban = **precedent** for identity gating. Fraud industrialization creates **broad coalition** for surveillance. **Below** 0.20 because US libertarian + industry friction; EU **different** path (GDPR friction).

**Evidence:**
- `<!-- private monorepo only -->` — deemed export scope
- Interpol — cross-border fraud requires intel sharing
- Node 6 — preemption fights show **limits** on federal overreach

**Analogue:** PATRIOT Act provisions — some sunset, some persist.

**Would update if:** T8-B passes **with** explicit surveillance annex and no sunset → **≥0.25**.

**Conf:** L

---

### P = 0.03 — T8-D: Kinetic escalation from cyber crisis

**Claim:** P(kinetic great-power escalation **primarily caused** by AI CI cyber crisis) ≈ **0.03** — aligns with Node 3 T1.

**Why:** Same evidence stack as Node 3 §14. T8-A **raises discussion** not execution.

**Evidence:**
- `node3_evidence_rationale.md` §14, §17

**Conf:** L–M

---

## Cross-node correlations

### P = 0.55 — Offensive cyber surge **given** Node 3 modal (ρ ≈ 0.45)

**Claim:** Conditional P(T8-E offensive surge | Node 3 modal) ≈ **0.55**; marginal correlation **ρ ≈ 0.45** with N3 export-ctrl expansion.

**Why:** Shared actor (US IC); theft crisis and CI crisis **reinforce** offensive cyber **without** pause. Export gating on models **correlates** with cyber retaliation — not independent.

**Evidence:**
- `node3_evidence_rationale.md` §16, §23
- `correlation_matrix.md` — Cluster A race/acceleration

**Would update if:** Post-theft **only** defensive response observed → ρ **≤0.20**.

**Conf:** M

---

### P = 0.70 — Cyber uplift at scale **given** Node 5 open-weight modal (ρ ≈ 0.55)

**Claim:** Conditional P(major cyber incident involves tampered/open weights | N5 modal) ≈ **0.70** for **criminal** tier; **0.25–0.35** for **salient** Trigger E attribution to open weights.

**Why:** Node 5 defines tamper at scale. Qwen/Llama cyber fine-tunes **already** circulate. Attribution harder → **political** salience may focus on **closed** cyber tiers (Mythos) anyway.

**Evidence:**
- `node5_evidence_rationale.md`
- GTIG UNC5673 — LLM abuse infrastructure at scale
- `code/typebits/` — refusal ablation on open models

**Would update if:** Salient E traced **only** to closed API with no open-weight component → lower open-weight **political** linkage.

**Conf:** M

---

### P = 0.30 — Open-weight attribution **given** salient cyber Trigger E

**Claim:** If Node 8 Trigger E fires, P(media/gov **primary blame** on open-weight tamper) ≈ **0.30**.

**Why:** Mythos/Fable frame = **closed** cyber tier danger. Meta open strategy provides **counter-narrative**. Higher for **fraud** E than **OT** E.

**Evidence:**
- Fable narrative — closed frontier cyber
- Node 5 T5-A — licensing tail needs attribution event
- `node5_evidence_rationale.md`

**Conf:** L–M

---

## Nation-state operationalization

### P = 0.85 — Major APT integrates AI into **routine** ops by 2027

**Claim:** ≥85% that ≥3 of {PRC, RU, IR, KP} state-linked ecosystems use commercial LLMs for **malware dev, vuln research, or op support** routinely (not experimental) by end-2027.

**Why:** GTIG May 2026 documents operational integration. CSA notes May 2026 — KONNI, MuddyWater, APT28 LAMEHUG runtime LLM query. GREYVIBE full-lifecycle AI (May 2026). **Already true** at confidence threshold — 0.85 not 0.99 due to attribution uncertainty.

**Evidence:**
- https://safeguard.sh/resources/blog/gtig-ai-threat-tracker-nation-state-may-2026
- CSA AI-assisted backdoor note May 2026
- CSA GREYVIBE note May 2026

**Analogue:** Excel macros in 2000s malware — became standard kit.

**Would update if:** GTIG retracts operationalization claims → **≤0.50**.

**Conf:** M–H

---

### P = 0.45 — PRC uses AI for **automated** LLM account farming at scale (2026–27)

**Claim:** ~45% annual probability of documented PRC-nexus **industrial-scale** evasion of LLM provider ToS (relay services, premium account cycling) to fuel cyber ops.

**Why:** GTIG: UNC6201 automated premium account registration; UNC5673 Claude-Relay-Service infrastructure. **Specific** to PRC pipeline; probability on **detection** not activity.

**Evidence:**
- GTIG May 2026 report — UNC6201, UNC5673

**Analogue:** VPN/proxy farms for cybercrime — cat-and-mouse.

**Conf:** M

---

## p(doom) conditional lifts

### Δ = +0.5–1.5pp — Node 8 modal on P(extinction by 2050)

**Claim:** Node 8 modal branch adds **+0.5–1.5pp** to extinction via **war bucket** and **coordination failure** (no pause), not direct misalignment.

**Why:** Offensive cyber ↑ cold-war miscalculation risk **slightly**; concentrated fraud does **not** add extinction. Aligns with Node 3 modal lift magnitude.

**Evidence:**
- `../supplements/pdoom_methodology.md` — Hanson disjunction P(AI war)
- `node3_evidence_rationale.md` §23

**Conf:** L

---

### Δ = +1–3pp — T8-A cascade on P(severe catastrophe)

**Claim:** T8-A adds **+1–3pp** to **severe but recoverable** bucket; **+0.5–1.5pp** incremental extinction if escalation misread.

**Why:** Regional grid + finance disruption = **>$10T** class harm plausible without extinction.

**Evidence:**
- `../supplements/pdoom_methodology.md` — severe bucket 30%
- Colonial + NotPetya economic damage estimates

**Conf:** L

---

## Confidence summary

| Claim | Conf |
|-------|------|
| Capability live 2025–27 | **M–H** |
| Policy salience 2027–29 | **M** |
| Espionage modal | **M–H** |
| Kinetic **<0.03** | **M** |
| Export gating **0.70** | **M–H** |
| T8-A cascade **~0.10** | **L** |
| Fraud industrialized | **H** |
| Cross-node ρ estimates | **L** |

---

## External sources (full list)

- [CFR Cyber Operations Tracker](https://www.cfr.org/cyber-operations/)
- [Anthropic — Glasswing](https://www.anthropic.com/glasswing)
- [Anthropic — Fable/Mythos access](https://www.anthropic.com/news/fable-mythos-access)
- [Lyrie — Monterrey SCADA](https://lyrie.ai/research/research/2026-05-07-claude-agua-monterrey-ot-scada)
- [GTIG AI Threat Tracker May 2026](https://safeguard.sh/resources/blog/gtig-ai-threat-tracker-nation-state-may-2026)
- [CSA — AI-assisted nation-state backdoors (PDF)](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_research_note_ai_assisted_malware_nation_state_20260527-csa-styled.pdf)
- [CSA — Nimbus Manticore (PDF)](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_research_note_nimbus-manticore-ai-assisted-malware-irgc-nation-state_20260526-csa-styled.pdf)
- [Interpol 2026 Global Financial Fraud Threat Assessment](https://www.interpol.int/)
- [Arkose — Agentic AI fraud](https://www.arkoselabs.com/blog/agentic-ai-fraud)
- [Reuters — Taiwan chip cyber espionage Jul 2025](https://www.reuters.com/technology/cybersecurity/china-linked-hackers-target-taiwan-chip-industry-with-increasing-attacks-researchers-say-2025-07-16/)
- [White House EO 14409](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)

## Repo sources

<!-- private monorepo only: - `[private note]` -->
<!-- private monorepo only: - `[private note]` -->
<!-- private monorepo only: - `[private note]` -->
- `node3_evidence_rationale.md`
- `node5_evidence_rationale.md`
- `node2_evidence_rationale.md`
- `correlation_matrix.md`
- `../supplements/pdoom_methodology.md`
