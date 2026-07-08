> **Ported from:** `notes/timeline_prediction/node7_evidence_rationale.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 7 — Compute / Cloud Concentration: Evidence Rationale

> **Parent timeline:** [`node7_compute_cloud.md`](./node7_compute_cloud.md)  
> **Master:** [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md)  
> **Date:** 2026-07-04  
> **Settings:** Hybrid time (C); modal + tail branches

---

## 1. Where this fits in the repo

| File | What's there |
|------|----------------|
| **This file** | Claim \| Why \| Evidence for every major Node 7 probability (~22 sections) |
| [`node7_compute_cloud.md`](./node7_compute_cloud.md) | Full node — definition, timing, modal/tail, actors, p(doom), falsifiers |
| [`node3_evidence_rationale.md`](./node3_evidence_rationale.md) | Cloud KYC P≈0.55; DPA seizure; EU sovereign AI — **overlapping levers** |
| [`research_ai_pause_advocacy_playbook.md`](../research_ai_pause_advocacy_playbook.md) | Cloud registration near-term win; HEM 3–5 yr; DPA hard version |
| [`HEM_hardware_enabled_mechanisms.md`](../HEM_hardware_enabled_mechanisms.md) | Verified compute attestation; VEU datacenter mandate |
| [`Anthropic_Fable_Mythos_export_ban_2026_深度解读.md`](../Anthropic_Fable_Mythos_export_ban_2026_深度解读.md) | Live **kill switch** on frontier API |
| [`RAND_2024_Securing_AI_Model_Weights_导读.md`](../RAND_2024_Securing_AI_Model_Weights_导读.md) | SL1 = cloud default; concentration = attack surface |
| [`correlation_matrix.md`](./correlation_matrix.md) | Cluster A race — do not double-count with N3/N4/N6 |

---

### P = 0.58 — Modal branch (triopoly + incremental rules, no halt)

**Claim:** Conditional on C2–C5 window, **~58%** of worlds follow modal: AWS/Azure/GCP retain ≥70% US frontier FLOPs; cloud KYC/export rules tighten; **no** durable training stop.

**Why:** Same playbook pattern as Nodes 2–4 — **physical/export layer** moves, **compute cap** dead. Hyperscaler capex ($200B+ AWS, Stargate) creates **too-big-to-pause** coalition. Fable shows gov **can** cut access but **chose** narrow export frame, lifted partially in 2 weeks.

**Evidence:**
- Synergy Q1 2026: triopoly **~63–68%** global IaaS — frontier **more** concentrated than average
- `research_ai_pause_advocacy_playbook.md` §1.2 — compute export **viable**; training cap **not**
- Fable Jun 2026 partial restore — **not** sustained global ban
- Node 4 modal 0.58 — **same** human-response reference class

**Analogue:** Post-9/11 airline security — **infrastructure rules** tighten; industry **keeps flying**.

**Would update if:** ≥2 labs **public halt >90d** citing cloud/gov gate (not just rhetoric).

**Conf:** M

---

### P = 0.82 — US frontier ≥70% on AWS/Azure/GCP through 2028

**Claim:** At least **70%** of US frontier **training FLOPs** run on the triopoly through 2028-12.

**Why:** Labs signed **multi-year GW** deals (Anthropic–AWS 5GW Mar 2026); OpenAI Stargate still **uses** hyperscaler + Oracle; self-build **partial** (Abilene) not full migration by 2028. Neocloud captures **overflow**, not majority.

**Evidence:**
- SQ Magazine / AWS stats Mar 2026 — Anthropic 5GW Trainium commitment
- CSA 2025 report — triopoly **overwhelming majority** of AI-grade enterprise compute
- `<!-- private monorepo only -->` — Stargate 2 buildings op / 8 building
- OpenAI multi-cloud pattern (Azure primary + Oracle Stargate)

**Analogue:** Mobile OS duopoly — alternatives exist but **not** for frontier scale.

**Would update if:** Meta or xAI announces **>50%** training on **non-triopoly** owned DC with verified FLOPs.

**Conf:** M–H

---

### P = 0.55 — Federal cloud training registration / KYC by 2028

**Claim:** US requires **registration or KYC** for large cloud training runs (BIS threshold or ~10²⁵ FLOP class) by 2028-12.

**Why:** Playbook lists as **near-term win #3**; BIS May 2025 explicitly flags IaaS training for D:5 parties; Jan 2026 chip rule requires **KYC procedures** from exporters; House Remote Access Security Act (Jan 2026) expands cloud under EAR. Trump EO 2026 **acceleration** frame still **natsec-hawk** on CN access.

**Evidence:**
- [BIS AI training policy statement](https://www.bis.gov/media/documents/ai-policy-statement-training-ai-models-may-13-2025) — IaaS + knowledge standard
- [Mayer Brown Jan 2026](https://www.mayerbrown.com/en/insights/publications/2026/01/administration-policies-on-advanced-ai-chips-codified) — remote end-user disclosure
- `node3_evidence_rationale.md` §10 — cloud KYC P≈0.55 (same lever)
- `research_ai_pause_advocacy_playbook.md` §1.3 items 3, 126

**Analogue:** Bank Secrecy Act for large wire transfers — **reporting**, not prohibition.

**Would update if:** Explicit Trump admin **repeal** of IaaS guidance + no replacement by 2028.

**Conf:** M

---

### P = 0.60 — BIS enforces IaaS / training catch-all (knowledge-based)

**Claim:** **≥1** major enforcement action or licensing denial for cloud-facilitated AI training to D:5 entities by 2028.

**Why:** May 2026 guidance **re-confirms** Nov 2023 D:5 HQ rule; DOJ/BIS **diversion** push on chips signals **will** to enforce. Gap: **proof of knowledge** hard — expect **case-by-case**, not blanket ban.

**Evidence:**
- [BIS May 31, 2026 guidance PDF](https://media.bis.gov/media/documents/bis-guidance-may-31-2026.pdf)
- MoFo Feb 2026 — compliance expectations **↑** across AI chip ecosystem
- Node 3 export ctrl P≈0.70 — **same** policy cluster

**Analogue:** Huawei Entity List enforcement — **selective**, high-impact.

**Would update if:** Zero enforcement actions despite public evidence of CN training on US cloud through 2028.

**Conf:** M

---

### P = 0.75 — China blocked from US cloud frontier training (effective)

**Claim:** **Effective** block on PRC-headquartered entities using US hyperscaler for **frontier-scale** training by 2028.

**Why:** Already **legal** requirement; hyperscalers **implement** D:5 screening; smuggling **tail** not modal. Jan 2026 certifications require **no prohibited remote access**.

**Evidence:**
- BIS 2025–26 policy stack (above)
- `node3_evidence_rationale.md` — chip-hawk bipartisan baseline
- AI 2027 CDZ — CN **domestic** training assumption

**Analogue:** Semiconductor equipment embargo — **leakage** exists but **not** at frontier scale modal path.

**Would update if:** Documented DeepSeek-scale run on **US cloud** with no enforcement response.

**Conf:** H

---

### P = 0.35 — Repeatable gov API / deployment recall (Fable-class)

**Claim:** US executive uses EAR / EO to **recall or gate** a frontier **deployed** model (API) **≥1 more time** by 2028, beyond Fable/Mythos.

**Why:** Precedent **live**; industry **pushback** strong (freefable.org, partial lift); **selective** not systematic. 35% = **more than once-off**, less than default.

**Evidence:**
- `Anthropic_Fable_Mythos_export_ban_2026_深度解读.md` — full timeline
- Nate Soares / Yudkowsky — gov **can** act "out of nowhere"
- Lawfare / Dean Ball — industry calls controls "cartoonish"

**Analogue:** FDA drug withdrawal — **rare**, high-profile, **not** industry shutdown.

**Would update if:** Second recall within 2026; or explicit **no-more-recalls** Commerce policy.

**Conf:** M

---

### P = 0.45 — DPA for grid / transformers (not datacenter seizure)

**Claim:** DPA **Section 303** or successor used to **prioritize domestic grid equipment** for AI power stack by 2028.

**Why:** Apr 20, 2026 Presidential Determination **already** identifies transformers, substations, etc. as defense-critical; binding constraint for GW DCs is **power**, not GPUs. **Distinct** from seizing OpenAI DC.

**Evidence:**
- [Atlas Peak Research — Apr 2026 DPA determination](https://www.atlaspeakresearch.com/report/56c3d4)
- CSA report — grid + cooling as systemic risk
- Azure May 2026 outage — **cooling/power** not cyber

**Analogue:** COVID DPA for PPE — **supply chain**, not seizing factories.

**Would update if:** DPA determination **rescinded** or grid crisis resolves without further action.

**Conf:** M

---

### P = 0.06 — DPA frontier datacenter seizure / mandatory training pause

**Claim:** US government **seizes or halts** a frontier AI datacenter under DPA or emergency authority for **>30 days** by 2028.

**Why:** Node 3/4 tables: P(DPA seizure)=**0.03–0.08**; Yudkowsky *Only Law* path **not** mainstream DC. Stargate = **political asset**; seizure triggers **market + ally** crisis. Slightly **higher** than Node 4 alone because **concentration** makes target **legible**.

**Evidence:**
- `research_ai_pause_advocacy_playbook.md` §1.2D — DPA as hard pause lever
- `node4_evidence_rationale.md` — P(DPA seizure)=0.03 modal
- Fable — gov chose **export recall**, not DC seizure

**Analogue:** Truman steel seizure 1952 — **struck down**; high bar.

**Would update if:** Pentagon **public** contingency plan for DC seizure; or actual seizure attempt.

**Conf:** L–M

---

### P = 0.10 — Tail T7-A: Outage delays frontier training >30 days

**Claim:** **≥1** hyperscaler regional incident causes **≥1** US frontier lab to delay a major training run **>30 days** (2026–2028).

**Why:** Oct 2025 + May 2026 AWS, May 2026 Azure show **multi-day** regional failures; SageMaker/GPU pools affected. **30d** requires **bad luck** (wrong region + no failover + grid compound). CSA: **90%** enterprises lose **>$300k/hr** downtime — labs **multi-region** mitigate.

**Evidence:**
- [Network World — AWS May 2026 thermal event](https://www.networkworld.com/article/4168878/aws-hit-by-us-east-1-outage-after-data-center-thermal-event.html)
- [Azure West US 2 May 2026](https://azure.status.microsoft/status/history/?trackingId=GHRP-84G)
- [CSA AI Compute Concentration report](https://labs.cloudsecurityalliance.org/research/ai-compute-concentration-systemic-risk-v1-csa-styled/)

**Analogue:** TSMC earthquake delay — **weeks**, not years; rare.

**Would update if:** 2026–2027 **second** >14d outage in same region with documented frontier delay.

**Conf:** L–M

---

### P = 0.12 — Tail T7-B: Gov gate on frontier training runs (beyond export)

**Claim:** US requires **prior approval** for frontier training runs above FLOP threshold on **US soil** (not just foreign-national access) by 2028.

**Why:** **Higher** than DPA seizure (0.06) because **registration** is softer — EO 2026-06 **30-day pre-brief** is **proto-gate**. Full gate needs statute or EO expansion; industry fights. 12% = **tail**, not modal.

**Evidence:**
- Fable trigger: Fable released **7 days** after policy, not 30 — **gap** invites gate
- `Anthropic_Fable_Mythos_export_ban_2026_深度解读.md` §3 — 8/1 covered-model framework deadline
- Playbook — training licensing **medium horizon**, not dead

**Analogue:** FDA IND for clinical trials — **gate** without banning research field.

**Would update if:** 8/1 2026 framework mandates **pre-approval** for training; or GAAIA adds cloud training license.

**Conf:** L

---

### P = 0.15 — Tail T7-C: EU/India materially decouple >25% frontier spend off US hyperscalers

**Claim:** By 2029, **>25%** of EU + India **government-linked** frontier AI compute spend runs on **non-US-hyperscaler** sovereign stacks.

**Why:** CADA **mandates** sovereignty assessment; €180M tender Apr 2026; India G42 deal May 2026. **Commercial** labs may stay on AWS; threshold is **government-linked** + **material** (25%, not 100%).

**Evidence:**
- [EU CADA COM(2026) 503](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52026PC0502)
- [EU press IP/26/833 — sovereign tender](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_26_833/IP_26_833_EN.pdf)
- [Rest of World — India G42](https://restofworld.org/2026/india-uae-g42-cerebras-ai-sovereignty/)
- Euronews Mar 2026 EURO-3C

**Analogue:** GDPR → local cloud — **partial** decouple, not autarky.

**Would update if:** CADA **withdrawn**; or EU **explicitly** allows US hyperscaler for all GPAI training.

**Conf:** M

---

### P = 0.50 — EU sovereign cloud >30% public-sector AI compute by 2028

**Claim:** EU institutions + member states procure **>30%** of public-sector AI compute from **SEAL-certified** EU sovereign providers by 2028.

**Why:** Commission **already** awarded €180M / 6yr tender; **mandate** for institutions; member state adoption **slower**. 50% = **institutional** more than **commercial**.

**Evidence:**
- IP/26/833 — four providers, diversification explicit
- Proximus–S3NS (Google JV) — **sovereign wrapper** on US tech
- `node3_evidence_rationale.md` — EU sovereign AI spend P≈0.60 (broader)

**Analogue:** EU Galileo vs GPS — **parallel**, not replacement.

**Would update if:** Tender **cancelled** or undersubscribed.

**Conf:** M

---

### P = 0.40 — India national AI off US hyperscaler for sovereign projects

**Claim:** Indian **government/national** frontier projects (CDAC-class) run primarily on **non-US** sovereign DC (G42, domestic) by 2028.

**Why:** G42–Cerebras May 2026; **parallel** to commercial AWS/Azure ($17B+ MS, AWS investments). DPDP **data residency** pressure.

**Evidence:**
- Rest of World May 2026 — CDAC + Core42, data under Indian rules
- Paris 2025 / India AI Summit — **sovereign AI** frame
- `research_ai_pause_advocacy_playbook.md` — Global South **anti-pause**, pro **access**

**Analogue:** India UPI — **domestic rail**, foreign cards still exist.

**Would update if:** National project **hosted on AWS Mumbai** exclusively with no sovereign duplicate.

**Conf:** M

---

### P = 0.08 — Tail T7-D: HEM / verified compute pilot deployed

**Claim:** **≥1** US export-controlled or VEU datacenter runs **FlexHEG-class** attestation on **frontier training** workload by 2028.

**Why:** HEM **R&D** not product (`HEM_hardware_enabled_mechanisms.md`); playbook puts **hardware licensing 3–5 yr**. 8% = **pilot**, not mandate. FlexHEG + gov **interest** on export scenarios.

**Evidence:**
- `HEM_hardware_enabled_mechanisms.md` — VEU datacenter mandate scenario
- `research_ai_pause_advocacy_playbook.md` §1.3 item 8 — HEM kill switches
- AI 2027 Appendix S — compute pause immature 2026

**Analogue:** Smart meter pilots — **years** before national roll-out.

**Would update if:** Commerce **mandates** HEM for licensed chip exports to allies.

**Conf:** L

---

### P = 0.12 — Tail T7-E: Cloud controls loosen for allies / accelerate build

**Claim:** Post-2027 policy **explicitly** **eases** cloud/chip access for **allied** sovereign AI **while** tightening CN — **net acceleration** of Western frontier capacity.

**Why:** Jan 2026 case-by-case China chip review = **dual track**; Stargate + DPA grid = **build more**; Trump AI Action Plan **acceleration** frame. **12%** as **distinct tail** from modal (modal already includes mild acceleration).

**Evidence:**
- Mayer Brown Jan 2026 — case-by-case H200 to China **under certs**
- `<!-- private monorepo only -->` — competition frame won
- Node 3 T3 race accelerates P≈0.15–0.25 — **subset** is cloud-specific

**Analogue:** Marshall Plan + COCOM — **allies in**, adversaries out.

**Would update if:** Unified **global** cloud training freeze proposed seriously in DC.

**Conf:** M

---

### P = 0.85 — Frontier labs maintain multi-cloud portfolio

**Claim:** **All** major US frontier labs use **≥2** of {AWS, Azure, GCP, CoreWeave, Oracle} for training or inference by 2028.

**Why:** Capacity crunch; Fable **single-provider** risk; Anthropic **AWS + Google**; OpenAI **Azure + Oracle + CoreWeave**. **Risk management**, not antitrust.

**Evidence:**
- CSA — concentration **risk** cited by CISOs; labs **respond** with multi-cloud
- Tech Insider 2026 — 89% enterprise multi-cloud

**Analogue:** Airlines multi-hub — still **oligopoly** suppliers.

**Would update if:** Lab **exclusive** single-cloud contract leaked with no fallback.

**Conf:** M–H

---

### P = 0.55 — Partial self-build (Stargate / lab-owned DC) for ≥1 major lab

**Claim:** OpenAI, Anthropic, Meta, or xAI operates **owned or dedicated** GW-scale DC capturing **>15%** of that lab's training FLOPs by 2028.

**Why:** Stargate Abilene; Meta $125–145B/yr DC capex; **partial** not **majority** by 2028. **55%** = **any** major lab **meaningful** self-build.

**Evidence:**
- `<!-- private monorepo only -->` — Stargate structure
- AWS stats — Anthropic still **5GW on Trainium** (self-build **complements**)

**Analogue:** Apple private CDN — **partial** bypass of carrier oligopoly.

**Would update if:** Stargate **cancelled**; or lab **100%** cloud by 2028.

**Conf:** M

---

### P = 0.70 — Neocloud (CoreWeave / Oracle) wins ≥1 frontier training contract

**Claim:** By 2028, **≥1** of {OpenAI, Anthropic, Google DeepMind, Meta AI} has **public** frontier training on CoreWeave or Oracle **Stargate-adjacent** cluster.

**Why:** OpenAI–CoreWeave **public**; capacity **bottleneck** on hyperscaler GPU; Oracle Stargate **explicit** for OpenAI.

**Evidence:**
<!-- private monorepo only: - `[private note]` §CoreWeave -->
- CSA — neoclouds "inch higher" in share

**Analogue:** TSMC vs in-house fab — **overflow** foundry.

**Would update if:** All frontier runs **confirmed** triopoly-only through 2028.

**Conf:** M

---

### P = 0.18 — Mandatory hyperscaler resilience / stress-test standard

**Claim:** US **binding** rule requiring frontier customers' cloud providers to meet **AI-specific** outage resilience standard by 2028.

**Why:** Outages **repeated** but **no** FAA-for-cloud yet; industry prefers **voluntary**; **18%** needs **Tail T7-A** fire + DC hearing.

**Evidence:**
- AWS Oct 2025 — **70+** services; **no** regulation
- Node 1 P(hearings)=0.75 — **could** extend to cloud

**Analogue:** NERC CIP for grid — **after** big blackout.

**Would update if:** GAAIA or EO adds **cloud BC** title.

**Conf:** L

---

### P = 0.35 — Congress passes cloud training reporting law

**Claim:** Statute requires **reporting** large cloud training runs to Commerce/DoC (not necessarily cap) by 2028.

**Why:** **Lower** than executive KYC (0.55) because **Congress slow**; Remote Access Security Act **passed House** Jan 2026 — **possible**. Reporting **≠** cap — Cruz coalition might accept.

**Evidence:**
- Mayer Brown — House Remote Access Security Act
- GAAIA draft — audit/reporting theme
- Node 4 P(GAAIA-like passes House)=0.25

**Analogue:** SAR bank reporting — transparency without ban.

**Would update if:** GAAIA **dies** with no cloud title substitute.

**Conf:** M

---

### P = 0.25 — EU bans US hyperscaler for **sensitive** GPAI training

**Claim:** EU member state or EU-wide rule **prohibits** GPAI **frontier training** on non-SEAL-3+ cloud for **defined sensitive** use cases by 2028.

**Why:** CADA enables **risk assessment → mandate**; **not yet** full ban; **25%** = **sectoral** (defense, gov), not Llama fine-tunes.

**Evidence:**
- CADA COM(2026) 503 — member states **must** assess sovereignty risk
- EU AI Act + GPAI — **enforcement** 2025–26

**Analogue:** EU Schrems II — **sectoral** data localization.

**Would update if:** CADA **softens** to voluntary labels only.

**Conf:** M

---

### P = 0.65 — Hyperscalers offer EU "sovereign SKU" (S3NS-class)

**Claim:** **≥2** of {AWS, Azure, GCP} market **EU sovereignty-compliant** AI cloud offering with **EU data boundary** by 2028.

**Why:** Proximus–S3NS already in tender; **commercial** response to CADA; **keeps** US hyperscaler **in** EU market.

**Evidence:**
- EU IP/26/833 — S3NS (Thales–Google) awarded
- Microsoft EU cloud sovereignty initiatives (2024–25 pattern)

**Analogue:** AWS GovCloud — **segmented** product.

**Would update if:** EU **rejects** US-JV sovereign wrappers as non-compliant.

**Conf:** M

---

### P = 0.08–0.12 / yr — Regional hyperscaler outage >7 days (any cause)

**Claim:** **Annual** probability of **≥1** AWS/Azure/GCP region **>7 days** impaired for GPU/training services.

**Why:** 2025–26 had **multiple** multi-hour to multi-day events; **7d** ** rare** (May 2026 AWS still recovering EC2 **days**). **0.08–0.12/yr** = **~20–30%** over 3yr window for **any** region.

**Evidence:**
- AWS US-EAST-1 history — Oct 2025 15h; May 2026 multi-day
- Azure May 2026 ~22h with **2 AZ**

**Analogue:** Major airline ground stop — **1–2×/decade** national visibility.

**Would update if:** Zero regional outages **>48h** through 2027.

**Conf:** L–M

---

### p(doom) — Modal +0.5–1.5pp (concentration → speed, not pause)

**Claim:** Node 7 **modal** branch adds **+0.5–1.5pp** to P(extinction by ~2050) vs distributed-compute counterfactual.

**Why:** Concentration **increases** frontier duty-cycle efficiency (Stargate, GW deals) → **faster** C9–C10; gov chokepoint used for **CN containment**, not alignment pause. **Partial offset:** kill switch **could** slow if used — **2026 track record** says **won't**.

**Evidence:**
- Node 3 modal +0.5–1.5pp — **export without pause**
- Node 4 — transparency not kill switch
- Fable — **2 week** partial restore

**Analogue:** Financial centralization → faster crises **and** faster growth.

**Would update if:** Gov **sustained** training halt **>90d** via cloud lever.

**Conf:** L–M

---

### p(doom) — T7-A outage −0.5–2pp (temporary)

**Claim:** Major outage tail **reduces** extinction risk **temporarily** by slowing training **weeks–months**.

**Why:** **Not** structural — labs **resume**; **no** treaty. **−0.5–2pp** = **speed** channel only, **low confidence**.

**Evidence:**
- AWS outages — **no** policy pause
- Node 4 — incidents rarely durable

**Would update if:** Outage triggers **binding** federal training moratorium.

**Conf:** L

---

### p(doom) — T7-C fragmentation +0.5–1.5pp

**Claim:** Sovereign cloud fragmentation **increases** coordination failure and multipolar race contribution to extinction.

**Why:** **Weakens** US-led HEM/verification (`node3_evidence_rationale.md` T4 allied fracture); CN + EU + India **parallel** stacks → **harder** mutual pause.

**Evidence:**
- Paris 2025 US unsigned; India sovereign frame
- `correlation_matrix.md` — race cluster

**Would update if:** EU–US **joint** cloud verification treaty.

**Conf:** L–M

---

### p(doom) — T7-D HEM pilot −0.5–2pp if scales

**Claim:** Verified compute pilot **reduces** extinction if it becomes **template** for caps — **conditional** on scale beyond pilot.

**Why:** **Only** path where concentration **helps** pause — **metered** FLOPs. Pilot alone **minimal**; **−0.5–2pp** if **adopted** by 2030.

**Evidence:**
- `HEM_hardware_enabled_mechanisms.md` — workload verification
- Playbook item 8 — 3–5 yr horizon

**Would update if:** HEM **mandated** on Stargate clusters.

**Conf:** L

---

## Confidence summary

| Claim | Conf |
|-------|------|
| Triopoly ≥70% US frontier through 2028 | **M–H** |
| Modal = KYC/export not halt | **M–H** |
| Cloud registration ~0.55 | **M** |
| DPA DC seizure ~0.06 | **L–M** |
| Outage >30d delay ~0.10 | **L–M** |
| EU/India fragmentation material | **M** |
| HEM pilot ~0.08 | **L** |
| p(doom) lifts | **L** |

---

## External sources

- [Synergy / CRN Q1 2026 cloud share](https://www.crn.com/news/cloud/2026/cloud-market-share-q1-2026-aws-microsoft-google-battling-in-ai-era)
- [CSA — AI Compute Concentration](https://labs.cloudsecurityalliance.org/research/ai-compute-concentration-systemic-risk-v1-csa-styled/)
- [BIS AI training policy May 2025](https://www.bis.gov/media/documents/ai-policy-statement-training-ai-models-may-13-2025)
- [BIS D:5 HQ May 2026](https://media.bis.gov/media/documents/bis-guidance-may-31-2026.pdf)
- [Mayer Brown Jan 2026 chips](https://www.mayerbrown.com/en/insights/publications/2026/01/administration-policies-on-advanced-ai-chips-codified)
- [EU CADA](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52026PC0502)
- [India–G42 Rest of World](https://restofworld.org/2026/india-uae-g42-cerebras-ai-sovereignty/)
- [AWS outage May 2026](https://www.networkworld.com/article/4168878/aws-hit-by-us-east-1-outage-after-data-center-thermal-event.html)

## Repo sources

- `node7_compute_cloud.md`
- `node3_evidence_rationale.md`
- `../supplements/ai_pause_advocacy_playbook.md`
- `../supplements/HEM_hardware_enabled_mechanisms.md`
<!-- private monorepo only: - `[private note]` -->
<!-- private monorepo only: - `[private note]` -->
- `correlation_matrix.md`
- `../supplements/pdoom_methodology.md`
