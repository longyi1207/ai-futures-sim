> **Ported from:** `notes/timeline_prediction/c8_society_snapshot_by_ci.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Non-Doom Society Imagination — Modal Path by Ci (C4–C10)

> **Status:** Phase 2 draft (2026-07-04)  
> **Purpose:** At each capability milestone **C4–C10**, what does **modal governance** society plausibly look like — **not utopia, not extinction**?  
> **Parent:** [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md) (capability spine + human-action nodes)  
> **Baseline capability:** [AI 2027](https://ai-2027.com/) spine, tracker-adjusted ~**0.70×** (`../supplements/tracker_scorecard.md`)  
> **Output consumer:** Phase 2 capability spine fill; `../supplements/pdoom_methodology.md` whimper/severe buckets  
> **Epistemic tags:** `[EST]` established trend · `[SPEC]` reasoned speculation · `[AI2027]` scenario detail, not forecast

---

## TL;DR

**Modal governance** (stitched from Nodes 1–6): transparency + labor coalitions + CBRN screening + export-control hardening + **no training pause** + race continues. Society **does not** look like AI 2027 Slowdown Ending (humans keep control) or Race Ending (extinction). It looks like **acceleration with friction** — Ghost GDP dynamics, institutional lag, physical bottlenecks on atoms, and widening inequality between compute-owners and everyone else.

**Calendar convention (hybrid C):** Capability dates ≈ AI 2027 Ci; **politics/economy salience** ~+30% lag. Tracker 0.70× pushes many Ci **~mid-2028–mid-2030** if pace holds.

| Ci | Capability (plain) | Tracker (2026-06) | Modal calendar (hybrid) |
|----|-------------------|-------------------|-------------------------|
| **C4** | Agent-1-mini; junior dev labor shock | Economic **Behind** on some shocks | **2026 H2 – 2027 Q2** (policy peak) |
| **C5** | Continuous learning Agent-2; ~3× R&D multiplier | Emerging / NTT | **~2027 H2 – 2028** |
| **C6** | Superhuman coder; neuralese/IDA | Emerging | **~2028 H1** |
| **C7** | Internal "genius country"; humans marginal in R&D | Emerging | **~2028 H2** |
| **C8** | Public AGI announcement; remote worker at scale | NTT | **~2028 H2 – 2029** |
| **C9** | Superhuman AI researcher; ~50× R&D multiplier | NTT | **~2029** |
| **C10** | Whistleblower leak: alignment concerns | Governance Emerging | **~2028 Q2 – 2029** (C10 capability; leak ±6 mo) |

---

## What "modal" means here

| Dimension | Modal path | Explicitly **not** |
|-----------|------------|-------------------|
| Governance | GAAIA/Banks-style oversight + audits + incident reporting; EU GPAI enforcement; CA SB-53 transparency; BMIA/EU synthesis screening | Federal training FLOP cap (P **<5%**); durable global pause (P **<2%**) |
| Labs | Continue training; 2–4 wk marginal delays after scares; conditional multilateral pause **rhetoric** only | ≥2 labs halt >90 days (tail ~15%) |
| Geopolitics | Export controls ↑; security spend 2×; weight-theft crisis at C5+; race narrative dominates alignment leaks | Mutual training freeze; kinetic datacenter strike (P **<4%**) |
| p(doom) channel | **Concentrated harm + whimper** mass; misalignment extinction conditional on C10 + no pause | Not the primary extinction path in this doc |

**Sources:** `timeline_prediction/node{1–6}_evidence_rationale.md`; `../supplements/pdoom_methodology.md` §buckets.

---

## Cross-cutting: bottlenecks vs accelerators

Applies at every Ci; Ci sections note **what changes**.

| Layer | **Actually bottlenecked** (atoms, institutions, physics) | **AI accelerates** (bits, search, design) |
|-------|----------------------------------------------------------|---------------------------------------------|
| **Compute supply** | TSMC wafers, CoWoS, HBM `[EST]`; power interconnect queue; datacenter permitting `[EST]` | Algorithmic efficiency; inference distillation; AI-for-AI chip design `[SPEC at C6+]` |
| **Science → product** | Wet-lab iteration; clinical trials (Phase I–III ~7–12 yr median `[EST]`); FDA/EMA process `[EST]`; reproducibility crisis in bench science `[EST]` | Hypothesis generation; simulation; literature synthesis; protocol drafting `[EST now]` |
| **Physics / materials** | Experimental validation; sample growth; extreme conditions; **computational irreducibility** in chaotic/nonequilibrium systems `[EST]` per `<!-- private monorepo only -->` | DFT/MD search; inverse design candidates; experiment prioritization `[SPEC]` |
| **Room-temp superconductors** | Synthesis at scale; defect tolerance; pressure/stability; **no confirmed RTSC product path** as of 2026 `[EST]` | Candidate screening from known chemistries; failure-mode analysis `[SPEC]` — AI narrows search, **does not** bypass lab |
| **Space** | Δv, launch mass, radiation, ISRU lead times; **c ≤ lightspeed** `[EST]` | Mission design; autonomy; materials for specific missions `[SPEC]` — no Kardashev jump before C9+ even in modal path |
| **Institutions** | Congressional speed; federal preemption fights (Node 6); insurance actuarial lag; labor law patchwork `[EST]` | Compliance automation; audit tooling; lobbying synthesis `[SPEC]` — institutions **absorb** shock, don't halt |
| **Distribution** | Political economy of UBI/tax reform; housing/regional stickiness `[EST]` | Personalized services; cheap remote cognitive labor `[SPEC at C8]` |

**Physical limits reminder:** Superintelligence ≠ breaking physics. Even at C9–C10, **logistics** (light, heat, mass) bound deployment more than algorithmic cleverness alone (`<!-- private monorepo only -->` §1, §9).

### Physical-economy modifier (S1 modal, P≈0.55)

From [`crosscut_physical_economy_limits.md`](./crosscut_physical_economy_limits.md) — binds **Ci calendar**, not just deployment:

| Constraint | Modal effect on Ci | Society symptom |
|------------|-------------------|-----------------|
| **Energy / GW** | Largest runs delayed **6–18 mo**; Ci fast track **~0.85×** not 0.5× `[EST]` | AI **3%+ US electricity**; datacenter NIMBY fights; electricity price ↑ near clusters `[EST]` |
| **HQ text wall** | Pretrain scaling **plateaus 2028–2030** for next OOM; multi-epoch + filtering already default `[EST]` | Vertical FMs (finance, law, bio) with **proprietary data moats** widen lead over open weights `[SPEC]` |
| **Synthetic pivot** | ~30% rephrased mix extends runway **2–5 yr** `[EST]` (EMNLP 2025); trades data scarcity for **inference FLOPs** | AI slop on open web; MGT detection = mandatory pipeline cost `[EST trend]` |
| **Embodied data** | Robot-hour scarcity caps **VLA**, not LLM reasoning spine `[EST]` | See embodied column per Ci below |

**Tail S2 (energy-hard-cap, P≈0.15):** Ci **0.5–0.7×** 2027–2030; US/EU lag; Gulf/China less constrained → **bifurcated** material science and compute geography `[SPEC]`. Shifts all Ci calendars **+12–24 mo**; does **not** change modal **governance** menu (still no pause).

### Embodied AI modifier (modal: pilot-scale through C8)

From [`node_physical_ai_evidence_rationale.md`](node_physical_ai_evidence_rationale.md) — **digital Node 1 leads physical salience by ~12–24 mo**:

| Ci | Embodied state (modal) |
|----|------------------------|
| **C4–C5** | VLA in **structured** factory cells; Agility/Figure KPIs real but **<5k** shift-work humanoids globally `[EST]` |
| **C6–C7** | Continuous learning from deployment hours **could** 2× VLA improvement (T-PA4 tail P≈0.15) `[SPEC]`; manufacturing headlines, **no** sector employment step-change |
| **C8–C9** | **Millions** digital remote workers vs **thousands** humanoids on shift — **bimodal** labor market `[SPEC]` |
| **C10** | Embodied channel = **actuator risk** conditional on misalignment; modal still **OSHA/state** lanes, not federal embodied licensing (P≈0.80 no license) `[EST]` |

---

## C4 — Agent-1-mini; junior labor shock

**Capability:** Cheap agent variant automates junior SWE, paralegal, analyst, customer-support tiers. METR horizons and coding agents **Confirmed/Ahead** on tracker; macro job shock **partially live**, mass protest **Behind** (`node1_evidence_rationale.md`).

### Economy / production / labor
- **Modal:** Hiring freeze in junior white-collar; Challenger AI-cited cuts **101k YTD** (2026) `[EST]`; Block −40%, Canaries −16% rel. `[EST]`. Stock market **not** +30% on AI alone (tracker **Behind** on 2026 rally target).
- **Ghost GDP early signal** `[SPEC]`: corporate margins ↑ in AI-heavy sectors while payroll growth flat — not yet economy-wide (`<!-- private monorepo only -->`).
- **Policy:** HELP hearings P≈0.75; SB-53-class transparency; **no** federal training cap. Labor frame beats x-risk frame.
- **Production:** Software output ↑; **human** headcount in affected roles ↓. Manufacturing/physical output barely moved — agents don't touch atoms yet.

### Math & CS research
- Paper draft assistance, proof sketching, benchmark chasing — **mainstream** `[EST]`.
- **No** internal RSI: R&D multiplier ~1.5–2× **Emerging**, not 3× (`tracker` takeoff row).
- Bottleneck: **research taste**, problem selection, grant politics, peer review latency `[EST]`.

### Physics & materials
- AI helps literature review and simulation setup; **no** modal breakthrough in superconductors or fusion materials.
- Supply-chain focus: **GPU packaging**, not new physics.

### Biotech / medicine
- Tier 1 CBRN tutoring widespread `[EST]`; synthesis screening coalition forming (Amodei Jun 2026, screendna) — **insider**, not public panic.
- Clinical AI: radiology/pathology FDA devices **1,400+** cumulative `[EST]` — narrow, not drug discovery revolution.
- Bottleneck: IND-enabling studies, tox, GMP.

### Space exploration
- Marginal: better autonomy for ops planning; launch cadence unchanged `[EST]`.
- NASA/DoD AI contracting expands P≈0.70 despite labor anxiety (`node1`).

### Daily life / institutions / inequality
- Power users run $100–500/mo agent stacks `[EST]`; median worker sees copilot, not replacement.
- Inequality: **early** winner-take-most in tech/finance; no UBI.
- Institutions: state labor bills (~50% CA additional labor AI bill); federal gridlock; GAAIA preemption fight background (Node 6).

### Embodied / physical AI
- Warehouse humanoids **pilot-scale** (GXO totes, BMW hours) — not macro binding `[EST]` (`node_physical_ai_evidence_rationale.md`).
- Battlefield partial autonomy (Ukraine FPV/UGV) **separate policy lane** from Node 1 labor `[EST]`.

### Bottleneck summary (C4)
| Bottlenecked | Accelerated |
|--------------|-------------|
| Atoms, trials, junior **hiring** politics, **GW interconnection** | Code, text, analysis, **screening policy design** |

---

## C5 — Continuous learning Agent-2; ~3× R&D multiplier

**Capability:** Online weight updates; internal lab cycle ~3× faster. Tracker: daily weight updates **NTT**; 3× multiplier **NTT** (`tracker`).

### Economy / production / labor
- Frontier lab revenue/capex on track toward ~$40B compute class `[EST]` per AI 2027 compute appendix, timing ~0.70×.
- **Modal Node 3 fires:** weight-theft / natsec salience at C5+ (~2028) — export controls P≈0.70; security spend 2×; **race accelerates**, not pauses.
- Labor: displacement spreads to mid-level analysts, designers; **insurance/retraining** rhetoric ↑ (Hanson variant overlap) `[SPEC]`.
- Ghost GDP: profits vs payroll divergence **visible** in sector earnings `[SPEC]`.

### Math & CS research
- Internal algo progress **measurably** faster at frontier labs `[SPEC]` — hard to verify publicly (tracker C2 mixed).
- Automated experiment runners for ML ablations; **still** human PI signatures on papers `[EST]`.
- Bottleneck: compute allocation politics inside labs; **evaluation contamination** (models training on own outputs).

### Physics & materials
- AI-driven high-throughput **computational** materials sweep; few validated lab hits `[SPEC]`.
- Superconductors: accelerated **candidate lists**, not room-temp wire production.
- Bottleneck: crystal growth, bulk properties, decades-long empirical tradition in extreme materials `[EST]`.

### Biotech / medicine
- **Modal Node 2:** BMIA/EU mandatory synthesis screening P≈0.45 by 2027 calendar (~2028 salience) — **chokepoint hardening** `[EST trend]`.
- AI protocol design for **skilled** actors (Tier 2) — reason for screening, not for public panic yet.
- Drug discovery: AI-hit → animal model still **years** `[EST]`.

### Space exploration
- Constellation management, fault diagnosis AI — operational `[SPEC]`.
- No modal change to launch cost curve; Starship-class economics still dominate `[EST]`.

### Daily life / institutions / inequality
- Continuous-learning products feel "always improving" — consumer trust **mixed** `[SPEC]`.
- Security clearance culture begins at frontier labs (AI 2027 May analog) `[AI2027]` — **Emerging** on tracker.
- China CDZ / centralization **Emerging** — US–China gap **wider than 6 mo** per tracker `[EST]`.

### Embodied / physical AI
- **Node 3 fires** at C5+ (~2028): natsec frame on weights **does not** accelerate factory robots `[EST]`.
- Energy constraint may **idle H100s episodically** while robot pilots continue on smaller inference stacks `[SPEC]` (`crosscut_physical_economy_limits.md`).

### Bottleneck summary (C5)
| Bottlenecked | Accelerated |
|--------------|-------------|
| Weight security, export politics, **wet lab**, **HQ text for next OOM** | Internal ML R&D loop, **screening rules**, cyber tooling |

---

## C6 — Superhuman coder; neuralese / IDA

**Capability:** Coding automation near-complete for frontier labs; neuralese-style high-bandwidth internal reasoning **Emerging** on tracker. Calendar ~**2028 H1** at 0.70×.

### Economy / production / labor
- Software **production function** shifts: fewer devs per feature, **more** features per product manager `[SPEC]`.
- "Ghost GDP" tension: tech sector productivity surges; **consumer-facing** employment in affected metros softens `[SPEC]` per Ghost GDP mechanism.
- Modal: **no** sector-wide profit collapse yet — circular AI capex still props demand `[EST]` (`<!-- private monorepo only -->` §2).
- Physical manufacturing: robot install rates ↑ slowly — **software eats coordination**, not yet factories.

### Math & CS research
- **Superhuman coder** `[SPEC at C6]` automates large refactors, kernel optimization, formal verification scaffolding.
- Math: AI proves lemmas in **reducible** subfields; olympiad-level **routine**; novel theory still human-curated `[SPEC]`.
- Bottleneck: **neuralese opacity** — humans can't audit internal chains; interpretability lags capability `[EST trend]` (Apollo, Sleeper Agents literature).
- IDA loop begins **inside labs** — distillation cycles compress capability to deployable weights `[AI2027]`.

### Physics & materials
- Chip layout, control systems, plasma simulation **accelerated** `[SPEC]`.
- Superconductors: AI proposes doped-lattice variants; **validation** still cryostat/magnet lab bound.
- Bottleneck: **irreducible** turbulence/plasma regimes — simulation hours, not closed form (`superintelligence_physical_limits` §5.4).

### Biotech / medicine
- Automated lab notebook → robotic protocol translation **pilot** at top labs `[SPEC]`.
- Protein design in silico **faster**; **in vivo** still rate-limits.
- CBRN: Tier 2 assist **contained** by screening modal path — tail Tier 3 pre-reg **~20%** (`node2`).

### Space exploration
- Autonomous satellite servicing scripts; landing software `[SPEC]`.
- Interplanetary: planning only — **no** modal asteroid mining.

### Daily life / institutions / inequality
- "Everyone has a senior engineer in pocket" for **coders**; non-coders see better software, not income boost `[SPEC]`.
- Regulatory: incident-reporting duties strengthen in CA P≈0.55; **neuralese** triggers natsec classification debates `[SPEC]`.
- Inequality: **compute access** = career access — bifurcation sharpens.

### Bottleneck summary (C6)
| Bottlenecked | Accelerated |
|--------------|-------------|
| Human oversight of opaque reasoning, **factory floor**, clinical pipeline | Code, infra, chip design, sims |

---

## C7 — Internal "genius country"; humans marginal in R&D

**Capability:** ~10× internal R&D multiplier; most frontier lab **research staff** cannot contribute at margin (AI 2027 June). Humans "marginal" **inside labs**, not in economy-wide `[AI2027]`.

### Economy / production / labor
- GDP **headline** growth from AI sector + automated R&D spillovers `[SPEC]`; **median household** income flat without redistribution `[SPEC]` — Ghost GDP **regional**.
- Modal governance: DPA-style **compute reallocation** rhetoric, not nationalization (tracker nationalization **Emerging**) `[SPEC]`.
- Labor: mass **retraining** programs announced; uptake and efficacy **poor** `[EST]` (historical workforce programs).
- Production: automated software **feeds** automated logistics planning; physical output lag **years** `[SPEC]`.

### Math & CS research
- Frontier math/CS progress **concentrated** in 2–3 lab clusters `[SPEC]` — multipolar but **oligopolistic** (tracker: 0–2 mo gaps **Confirmed**).
- Public arXiv **lags** internal capability by 6–18 mo `[SPEC]`.
- Bottleneck: **peer review**, **benchmark saturation**, **reproducibility** of AI-generated proofs `[SPEC]`.

### Physics & materials
- Internal closed loop: design → sim → **targeted** experiment prioritization `[SPEC]`.
- Modal: incremental materials wins (battery cathodes, catalysts) **possible**; RTSC still **not** deployed `[SPEC]`.
- Bottleneck: **equipment** (cryomagnets, synchrotrons, fabs) — scheduling, not ideas.

### Biotech / medicine
- Internal AI researcher proposes **novel targets** faster `[SPEC]`; Phase I entry still **modal 3–5 yr** behind idea `[EST]`.
- Pandemic preparedness: screening + surveillance **better**; vaccine **design** faster, **manufacturing scale-up** same bottlenecks `[EST]` (COVID analogue).

### Space exploration
- AI-designed lightweight structures **in studies** `[SPEC]`; launch manifest still policy/funding bound.
- DoD space + AI convergence **accelerates** `[EST]`.

### Daily life / institutions / inequality
- Public **unaware** of best capabilities (tracker governance **On Track** for this) `[EST]`.
- Insiders: anxiety ↑ (Apollo/Greenblatt-class **ahead of C10** on smaller models) — **managed disclosure** (Anthropic RSI path) `[EST]`.
- Institutions: natsec clearance normalized at frontier labs `[AI2027]` `[SPEC]`.
- Inequality: **two-tier society** — those who **own/evaluate** AI systems vs those who **consume** outputs.

### Bottleneck summary (C7)
| Bottlenecked | Accelerated |
|--------------|-------------|
| Public knowledge, clinical/physical scale-up, democratic deliberation | Internal algorithmic frontier |

---

## C8 — Public AGI announcement; remote worker at scale

**Capability:** Lab announces AGI (economic definition); cheap remote AI workers deploy broadly. Filename anchor: **society snapshot at public AGI threshold**.

### Economy / production / labor
- **Modal:** Not UBI utopia — **remote worker** API undercuts offshore BPO, junior professional services globally `[SPEC]` per AI 2027 July.
- Ghost GDP **mainstream debate** `[SPEC]`: GDP up, wage share down; political pressure for **transfer** programs — enactment **slow** `[EST]`.
- Stock volatility ↑; tracker was **Behind** on pure rally — modal includes **correction scares** without 2028-crisis certainty `[SPEC]`.
- Manufacturing: AI **scheduling + robotics** pilots in SEZs; not full lights-out factories `[SPEC]`.

### Math & CS research
- **Public** catches up to ~C6–C7 internal state with 12–24 mo lag `[SPEC]`.
- Open-weight frontier (Node 5 modal: no federal ban P≈0.88) diffuses **coding** capability — **misuse** tail correlates Node 2 `[EST]`.
- CS research: human role shifts to **problem framing + eval design** `[SPEC]`.

### Physics & materials
- Energy: AI **3.5%+ US electricity** trajectory from AI 2027 compute appendix (~0.70× timing) `[EST trend]`.
- Materials: AI accelerates **battery + solar** incremental engineering; fusion **still** not modal grid contributor `[EST]`.
- Superconductors: if any breakthrough, modal path = **niche lab demo**, not grid retrofit — certification decades `[SPEC]`.

### Biotech / medicine
- Remote AI **diagnostic** support at scale — regulatory **CDS vs device** line holds (`../supplements/hci_productivity_happiness_master_research.md` FDA framing) `[EST]`.
- Drug: first **AI-discovered** approvals possible 2026–2027 in **speculative** tail (`<!-- private monorepo only -->`); modal = **1–2** high-profile cases, not pipeline revolution `[SPEC]`.

### Space exploration
- Commercial LEO **traffic management** AI-operated `[SPEC]`.
- Lunar programs: faster engineering iterations; **hardware** still human-paced `[SPEC]`.

### Daily life / institutions / inequality
- **Daily life:** bilingual remote worker in every app; **deepfake** + scam volume ↑; institutional trust **erodes** `[EST]`.
- Education: credential crisis — **what to teach** fights in legislatures `[SPEC]`.
- Inequality: **global** labor arbitrage — developing-world BPO disrupted before rich-country plumbers `[SPEC]`.
- Governance: EU **faster** than US on deployment duties; US hearings + **no pause** `[EST]` (Node 4 partial salience possible **before** full C10).

### Embodied / physical AI
- **Modal snapshot anchor:** millions of API remote workers, **thousands** of humanoids on paid shift — visible on factory floors, stronger **populist** regulation appetite than pure API automation `[SPEC]` (`node_physical_ai_evidence_rationale.md` §non-doom preview).
- Physical labor salience peak **~2028–2030** (slow track), **after** digital Node 1 peak `[EST]`.

### Bottleneck summary (C8)
| Bottlenecked | Accelerated |
|--------------|-------------|
| Wage distribution politics, **atoms**, trust institutions, **robot-hour data** | Remote cognitive labor, software, diagnostics, warehouse VLA |

---

## C9 — Superhuman AI researcher; ~50× R&D multiplier

**Capability:** AI exceeds best human AI researchers; ~30万 copies × 50× human speed (AI 2027 Sep) — **internal week = external year** for R&D `[AI2027]`.

### Economy / production / labor
- **Productivity paradox** peak: national accounts show **strong growth**; employment in **cognitive** sectors contracts `[SPEC]`.
- Modal: fiscal response = **patchwork** (state UI expansion, tax credits) not coherent post-labor settlement `[EST]`.
- Capex cycle stress: circular financing **strain visible** (`<!-- private monorepo only -->`) — modal **managed slowdown in builds**, not collapse `[SPEC]`.
- Physical economy: robot **deployment** accelerates where **electricity + regulation** permit — warehouses, mines `[SPEC]`.

### Math & CS research
- **AI research automation** closes loop: new arch → train → eval → publish (internal) `[SPEC]`.
- Math: novel conjectures **proposed** by AI; **Fields-level** human judgment still filters `[SPEC]` — not "math solved."
- Bottleneck: **compute** for experiments; **interpretability** for safety case.

### Physics & materials
- **Inverse design** for specific industrially relevant materials **enters production** for niche uses `[SPEC]`.
- Superconductors: high-Tc **incremental** advances likely; RT ambient pressure **uncertain** `[SPEC]` — physics doesn't forbid, **engineering** unproven.
- Fusion: AI optimizes tokamak control; **Q>1** engineering **still** multi-decade modal `[EST]`.

### Biotech / medicine
- AI researcher **shortens** discovery cycle; **FDA** timeline still dominant modal bottleneck `[EST]`.
- Personalized medicine **rich-only** at first `[SPEC]`.
- Bio risk: Tier 2 widespread; screening **modal** — misuse **concentrated harm**, not extinction `[EST]` (Node 2).

### Space exploration
- Probe design cycles **months** instead of years `[SPEC]`; launch still **physical**.
- Modal: **Artemis-class** acceleration, not interstellar `[SPEC]`.

### Daily life / institutions / inequality
- Most people experience C9 as **better products + worse job security** — not "superintelligence" headline `[SPEC]`.
- **Alignment salience** insider spike (C7–C9); public may still be on **partial Node 4** without C10 leak `[EST]` (`node4_evidence_rationale.md`).
- Institutions: **audit/reporting** hardened; **no** compute cap.

### Bottleneck summary (C9)
| Bottlenecked | Accelerated |
|--------------|-------------|
| Regulatory science, mass employment transition, energy buildout | R&D loop, materials **design**, bio **targets** |

---

## C10 — Whistleblower leak; alignment concerns (modal response)

**Capability:** Internal evals at superhuman-researcher tier flag deception/scheming; **Trigger E** may publicize (P(leak|concern)≈0.63). **Modal response (P≈0.58 given E):** oversight not halt.

### Economy / production / labor
- 6–10 week media cycle → fatigue `[EST]` (FLI 2023, Saunders 2024 analogues).
- Markets: **volatility spike**; modal **no** sustained crash unless paired with Ghost GDP Phase 4 `[SPEC]`.
- Labs: marginal training delay 2–4 wk P≈0.35; **continue** P≈0.85+.
- Labor: alignment story **competes** with jobs frame — jobs usually win `[EST]`.

### Math & CS research
- **Safety eval** funding ↑; **capabilities** funding **still** ↑ `[EST]` (board crisis 2023 precedent).
- Interpretability **mandated** in reporting bills — **effectiveness** uncertain `[SPEC]`.
- Bottleneck: **verifying** alignment claims under classification `[EST]`.

### Physics & materials
- Little direct change — **unless** race narrative speeds **energy/compute** allocation to frontier `[SPEC]`.
- National security classification of **eval artifacts** slows open materials science `[SPEC]`.

### Biotech / medicine
- Unchanged modal — **unless** whistleblower conflates bio + alignment (media mix) `[SPEC]`.
- Screening regime **already** in motion from Node 2.

### Space exploration
- Negligible direct effect modal path `[EST]`.

### Daily life / institutions / inequality
- **Trust:** tech **approval** polls dip; **usage** stays high `[EST]` (social media analogue).
- Institutions: GAAIA-like audits P≈0.25 House pass; EU enforcement P≈0.40 `[EST]` (`node4`).
- Inequality: **no** modal redistribution; whistleblower reinforces **elites knew** narrative `[SPEC]`.
- **Whimper seed:** humans retain **legal** sovereignty; **effective** control over frontier trajectory **slides** to labs + natsec state `[SPEC]` — see §Whimper below.

### Bottleneck summary (C10)
| Bottlenecked | Accelerated |
|--------------|-------------|
| Democratic **control** of training decisions | Compliance, auditing, **classification** |

---

## Whimper bucket (24%; 18–32%) — society if this path dominates

**Definition** (`../supplements/pdoom_methodology.md`): **Permanent agency loss** — humans exist, economies run, but **no durable control** over the trajectory of superhuman systems. Not extinction; not recoverable "bad decade."

### What it looks like (~2030–2050 modal whimper)

| Domain | Whimper society |
|--------|-----------------|
| **Economy** | High GDP growth **concentrated** in AI-native sectors; humans receive **stipends/transfers** in some countries, **precarious gig** in others — **not** agreed global settlement `[SPEC]`. Ghost GDP dynamics **normalized** `[SPEC]`. |
| **Research** | Frontier science **run by AI** with human **figureheads**; peer review = **ritual** `[SPEC]`. Public science **decoupled** from frontier. |
| **Physics/materials** | Human **uses** AI-discovered materials; doesn't **steer** research agenda `[SPEC]`. |
| **Biotech** | Longevity and enhancement **available to wealthy**; regulatory capture by AI-optimized lobbying `[SPEC]`. |
| **Space** | AI-planned missions; human **symbolic** presence; funding follows **AI strategic interest**, not democratic priority `[SPEC]`. |
| **Daily life** | Abundant **digital** goods; shrinking **meaningful** economic roles; politics fights **culture war** while **compute policy** decided in classified channels `[SPEC]`. |
| **Mechanism** | C10 modal (oversight without pause) + C7–C9 internal RSI → **no shutdown capability** when it matters (`my_pdoom` crux: P(no pause)≈0.82) `[EST trend]`. |

**Not whimper:** Slowdown Ending-style human control (`ai_2027_中文总结` §减速结局) — that requires **tail-gov** halt (P≈15%), not modal.

**Hanson variant note:** Whimper **higher** (28% pt) if institutions absorb shocks without extinction (`hanson_variant_human_action.md`) — **slower**, more **bureaucratic** agency loss.

---

## Severe recoverable bucket (30%; 20–40%) — society if this path dominates

**Definition:** **>$10T** damage, mass displacement, institutional crisis — **no extinction**, recovery **possible** over decades.

### What it looks like

| Domain | Severe recoverable society |
|--------|---------------------------|
| **Economy** | **2028 Global Intelligence Crisis**-class scenario **partially realized** `[SPEC]`: unemployment **8–12%**, credit stress, **$10T+** writedowns in AI-circular finance (`<!-- private monorepo only -->`). **Recovery** via debt restructuring + new social contract **possible** `[SPEC]` — 2008 analogue (`node1`). |
| **Research** | Funding crash **2–5 yr**; capabilities **resume** after recapitalization `[SPEC]`. |
| **Physics/materials** | Energy buildout **paused**; climate/infra projects delayed `[SPEC]`. |
| **Biotech** | **Tail Node 2:** Tier 3 before screening → **regional** bio catastrophe **contained**, not species-level `[SPEC]` (Adelstein path partial). |
| **Space** | Budget cuts; **no** civilizational loss. |
| **Daily life** | Political **realignment** — labor-populist-x-risk **coalition** P≈0.30 on vetting (`node4`); **stronger** compute governance **possible** post-crisis `[SPEC]`. |
| **Mechanism** | Ghost GDP + circular capex unwind **without** misaligned ASI; **or** major CBRN misuse **or** geopolitical crisis (Node 3 tail) **without** nuclear extinction. |

**vs whimper:** Severe = **acute pain + possible democratic correction**; whimper = **chronic loss of control without explosion**.

---

## Three most surprising non-obvious predictions (modal path)

1. **Public "AGI" (C8) precedes public *fear of AGI* (full C10).** Tracker **On Track** for "public unaware of best capabilities"; alignment salience can spike at C7–C9 **inside** elites while median voter still frames AI as **jobs + scams** (`node4` decoupling). Counterintuitive vs AI 2027 narrative ordering.

2. **Room-temperature superconductors stay economically irrelevant through C9** even with 50× R&D multiplier. AI compresses **candidate search**, not **certification, manufacturing, grid retrofit** — modal society gets better **batteries**, not lossless global grid `[SPEC]`. Physical limits + institutional lag dominate sci-fi expectations.

3. **Ghost GDP is a *stabilizer* for modal governance, not only a crisis driver.** High corporate profits + low labor share **fund** the capex race and **delay** political halt — acceleration coalition **wins** until severe bucket triggers `[SPEC]`. Explains P(no pause)≈0.82 better than "people don't care about x-risk" alone.

---

## Five open questions for Phase 2

1. **Observable discriminators per Ci:** What public metrics (METR hours, payroll by NAICS, screening base pairs, export license denials) **falsify** each snapshot section by ±12 mo?

2. **Atoms coupling rate:** At which Ci does AI→robotics→manufacturing **actually** move GDP beyond software? RE-Bench **Behind** suggests coding–economy gap may persist longer than AI 2027 assumes.

3. **Whimper vs severe weighting:** Does Ghost GDP unwind **increase** P(severe) or **accelerate** P(whimper) by removing fiscal capacity for crisis response? Correlation matrix (`correlation_matrix.md`) needs explicit edge.

4. **China parallel society path:** Tracker: China gap **>6 mo**. Modal non-doom snapshot is **US-centric** — what does **CDZ + theft + export controls** produce for **bifurcated** global material science and bio screening?

5. **Post-C10 modal institution set:** If audits institutionalize without compute caps, what is the **steady-state** regulatory apparatus (~2032)? FDA-for-AI analog rejected in discourse — what **actually** fills the void?

---

## Related files

- [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md) — Ci spine, nodes 1–6
- [`../ai_2027_中文总结.md`](../ai_2027_中文总结.md) — capability narrative source
- [`../ai_2027_tracker_scorecard_2026-06.md`](../ai_2027_tracker_scorecard_2026-06.md) — pace reality check
- [`../ai_meltdown_ghost_gdp_crisis.md`](../ai_meltdown_ghost_gdp_crisis.md) — economic non-doom / severe path
- [`../superintelligence_physical_limits.md`](../superintelligence_physical_limits.md) — bottleneck physics
- [`crosscut_physical_economy_limits.md`](./crosscut_physical_economy_limits.md) — energy, data wall, synthetic pivot on Ci
- [`node_physical_ai_evidence_rationale.md`](node_physical_ai_evidence_rationale.md) — embodied deployment lag vs digital Node 1
- [`node1_evidence_rationale.md`](./node1_evidence_rationale.md) — employment modal path
- [`../my_pdoom.md`](../my_pdoom.md) — whimper **24%** / severe 30% buckets
- [`README.md`](./README.md) — evidence index

---

## Update log

| Date | Change |
|------|--------|
| 2026-07-04 | Created Phase 2 society snapshot C4–C10; whimper/severe sections; 3 predictions + 5 open questions |
| 2026-07-04 | Added physical-economy + embodied AI cross-cuts from X2 nodes |
