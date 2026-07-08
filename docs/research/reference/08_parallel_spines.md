> **Ported from:** `notes/ai_futures_archive_2026-07/08_parallel_spines.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Event domains beyond Ci (internal granularity map)

> **Parent:** [`README.md`](./README.md)  
> **Public framing (blog):** Don't call these "parallel spines." Say **one capability calendar (C0–C10) + other important events on the same calendar**, with lag rules (politics/labor ~+30%; embodied policy +12–24 mo).  
> **Internal IDs** (S_phys, S_geo, …) stay here for research indexing.

**Rule:** **Ci** = digital cognitive AI capability milestones only. Other topics (LAWS, physical AI, cyber, geo, society, dual-use) are **event domains** that attach to Ci gates — not a second timeline.

---

## Six spines (orthogonal axes)

| Spine | ID | What it tracks | Canonical research | Ci coupling |
|-------|-----|----------------|-------------------|-------------|
| **Digital cognitive AI** | **S_Ci** | METR horizon, agents, RSI, alignment evals | [`03_ci_spine.md`](./03_ci_spine.md) C0–C10 | — (anchor) |
| **Physical deployment** | **S_phys** | Embodied robots, factory KPIs, energy/GW, data wall | [`../spine/node_physical_ai_evidence_rationale.md`](../spine/../spine/node_physical_ai_evidence_rationale.md), [`crosscut_physical_economy_limits.md`](../spine/crosscut_physical_economy_limits.md) | Same Ci, **+12–24 mo** policy lag |
| **Geopolitics & actors** | **S_geo** | US–China, EU, India, Gulf, Global South, theft | **N3**, **N9**, C3 | Events can **pull Ci** (theft → race) |
| **Conflict & security** | **S_conflict** | Cyber CI, kinetic tail, LAWS, espionage | **N8**, N3 §14, X2-A battlefield | Cyber **pre-C6**; kinetic **orthogonal** |
| **Society & political economy** | **S_soc** | Jobs, Ghost GDP, UBI/SWF, paralysis, civil tail, education | **N1**, **U2**, **S2** crosscut, **c8** | C4 labor shock gates |
| **Adjacent science & dual-use** | **S_dual** | Bio, nuclear, quantum, SC, space, longevity clinic | **N2**, **U3**, **U4**, bio primer | Discovery loops **@C6–C7** |
| **Cosmology / Fermi / expansion** | **S_cosm** | Abiogenesis, grabby aliens, physical limits on AGI expansion, SETI | [`cosmic_life_ai_modeling_framework.md`](../cosmic_life_ai_modeling_framework.md), [`superintelligence_physical_limits.md`](../superintelligence_physical_limits.md) | Couples **post-AGI** branch to cosmic ensemble; not Ci-gated |

**Composition rule:**  
`Outcome ≈ f(S_Ci, S_phys, S_geo, S_conflict, S_soc, S_dual)` — **do not multiply** spines as independent. Extinction stitching: **mechanism union** in [`09_extinction_rebuild.md`](./09_extinction_rebuild.md) (not exclusive branch mixtures — retired 2026-07-07).

```text
                    S_Ci (capability)
                         │
     S_phys ─────────────┼──────────── S_dual (enablers)
     (embodied)          │              (bio/nuke/space)
                         │
     S_soc ──────────────┼──────────── S_geo (actors)
     (labor/UBI)         │              (China/EU/…)
                         │
                    S_conflict
                    (cyber/kinetic/LAWS)
                         │
                         ▼
              Events (04) → Cruxes (05) → Nodes (06)
```

---

## Your list → coverage matrix

Status: **✅ researched** · **◐ partial** (in cross-cut, not spine-indexed) · **○ gap** (needs new cross-cut or node)

| Topic | Spine | Status | Where | Implications if moves |
|-------|-------|--------|-------|------------------------|
| **Autonomous weapons (LAWS)** | S_conflict + S_phys | ✅ | **[`../spine/crosscut_x3_laws_evidence_rationale.md`](../spine/../spine/crosscut_x3_laws_evidence_rationale.md)**; X2-A §battlefield; EV-LAWS-MASS | ↑ race narrative; ↓ domestic robot moratorium (P≈0.70); kinetic escalation if attribution fails; **whimper** via permanent war economy |
| **Physical AI / embodied** | S_phys | ✅ | X2-A full node; N12 locus; N1 physical wave | Deskilling **2028–32**; RSI locus embodied → Hanson mix ↑, ext −2–3pp; U4 deployment crux |
| **Civil war (domestic)** | S_soc | ◐ | S2 crosscut P≈**0.03** by 2030 | **Low tail** — whimper/severe, not extinction modal; BMIA ×0.7 if paralysis confounded |
| **Cyberwar / CI** | S_conflict | ✅ | **N8** (~22 P sections); EV-CYBER-CASCADE | Severe **30%** bucket; P(kinetic\|cyber)<0.03; Ghost GDP / finance tail |
| **Other countries** | S_geo | ✅ | **N9** (EU, India, China, Japan, Korea, Gulf, Global South) | Brussels effect; open-weights diplomacy; **not** US pause |
| **International conversation** | S_geo | ✅ | N9 M1 modal forum talk P≈0.58 | Salience without teeth; competes with BMIA window |
| **Treaties (binding vs empty)** | S_geo | ✅ | N9 taxonomy; U6; EV-U6-TREATY | Empty-shell **dangerous** P≈0.10; verification tail → U3 |
| **Heated / kinetic war** | S_geo + S_conflict | ◐ | N3; N9 T4 Taiwan P≈**0.03**; N8 P(kinetic\|cyber)<0.03 | Export controls; theft; **race ↑**; compute disruption; usually **not** extinction path alone |
| **Job loss / labor shock** | S_soc | ✅ | **N1**, EV-C4-LABOR, c8 | Gates U2 distribution window; whimper 24%; culture-war coalition |
| **Economy / Ghost GDP** | S_soc | ✅ | c8, U2, `ai_meltdown_ghost_gdp_crisis.md` | **Modal friction 53%**; CX-GHOST-GDP Tier 1 |
| **UBI / SWF / compute dividend** | S_soc | ✅ | **[`../utopia/node_u2_distribution_evidence_rationale.md`](../spine/../utopia/node_u2_distribution_evidence_rationale.md)**; U2, EV-SWF; `UBI_post_work_meaning_AI.md` | Flourishing vs Speenhamland trap; CX-UBI-SPEENHAMLAND |
| **Social change / meaning** | S_soc | ✅ | **U7**, CX-MEANING | Caps U2 even if aligned |
| **Education** | S_soc | ✅ | **X4** [`../spine/crosscut_x4_education_evidence_rationale.md`](../spine/../spine/crosscut_x4_education_evidence_rationale.md) | Human capital / reskilling → U4 vs whimper; **policy response to N1** |
| **Political administration change** | S_soc | ✅ | **X5** [`../spine/crosscut_x5_admin_evidence_rationale.md`](../spine/../spine/crosscut_x5_admin_evidence_rationale.md); CX-ADMIN-FLIP; EV-ADMIN-28; extends S2 | BMIA/GAAIA timing; preemption fights; AISI funding |
| **Nuclear + AI** | S_dual + S_conflict | ✅ | **X6** §1; CX-NUKE-AI-COUP | Escalation ladder; whimper/severe; **not** misalign ext modal |
| **Quantum computing** | S_dual | ✅ | **X6** §2; CX-QC-RELEVANT; N8 PQC | Crypto migration friction; **not** 2030 ext crux |
| **Superconductivity / materials** | S_dual | ✅ | **X6** §3; U3/U4; EV-SC-DEMO | U1 energy tail `[SPEC]`; LK-99 closed |
| **Life science / longevity** | S_dual | ✅ | N2 bio; U3; **X6** §4; CX-LONGEVITY-CLINIC | Bio **extinction tail** vs U1 defer |
| **Space technology** | S_dual | ✅ | U4; **X6** §5; EV-SPACE-LIFT | U1 tail; deployment human-paced @C7 |

---

## Implications map (what each spine **enables**)

| Spine moves… | Enables (doom) | Enables (flourish) | Enables (friction) |
|--------------|----------------|--------------------|--------------------|
| **S_Ci** ↑ fast | Misalign/bio tails live | U2/U3 science loop | c8 acceleration default |
| **S_phys** ↑ before digital salience peaks | Whimper via deskilling | U4 manufacturing abundance | Blue-collar Ghost GDP |
| **S_geo** EU binds | Slight misalign ↓ | U3/U4 via deployment duties | Compliance cost, not halt |
| **S_geo** China open-weights + race | Bio tail ↑ (N5); theft | Global South access narrative | IP fragmentation |
| **S_conflict** cyber cascade | Severe 30%; finance | — | Modal N8 path |
| **S_conflict** LAWS scale | War x-risk tail; race ↑ | — | Permanent emergency state |
| **S_conflict** Taiwan hot (3%) | Compute choke; ext via war **low** alone | — | Supply shock |
| **S_soc** paralysis S2 | Bio BMIA delay | U5 blocked | States-primary patchwork |
| **S_soc** UBI/SWF | — | U3/U4 if not Speenhamland | Wage suppression risk |
| **S_soc** education reform | — | U4 reskilling path | So-so automation persists |
| **S_dual** longevity clinic solved | — | U1 unlocked | Inequality in lifespan |
| **S_dual** room-temp SC **[SPEC]** | — | U1 energy tail | Compute cost ↓ → race ↑ |
| **S_dual** quantum break **[SPEC]** | CI/crypto crisis | — | Transition chaos |

---

## Tier 2 / Tier 3 crux candidates (promotion queue)

Not headline yet — promote to Tier 1 when evidence supports **≥2–3pp** move or interview load-bearing.

| ID | Statement | P(holds) | Range | Spine | Research priority |
|----|-----------|----------|-------|-------|-------------------|
| **CX-LAWS-ESCALATE** | LAWS deployment expands without international restraint through 2028 | **0.72** | 0.62–0.82 | S_conflict | **HIGH** — new X3 cross-cut |
| **CX-KINETIC-TW** | Taiwan Strait kinetic conflict by 2030 | **0.03** | 0.01–0.06 | S_geo | N9 T4 — keep tail |
| **CX-CYBER-KINETIC** | Kinetic strike primarily triggered by AI cyber CI crisis | **<0.03** | — | S_conflict | N8 — keep tail |
| **CX-CIVIL-WAR** | US civil war-scale organized conflict by 2030 | **0.03** | 0.01–0.05 | S_soc | S2 — whimper only |
| **CX-PHYS-BEFORE-DIGITAL** | Physical labor salience peaks **after** digital (≥12 mo lag) | **0.65** | 0.55–0.75 | S_phys | X2-A — promote if deskilling accelerates |
| **CX-EMBODIED-RSI** | RSI first locus is embodied / factory not cloud | **0.12** | 0.08–0.18 | S_phys | N12 tail — opposite of CX-RSI-LOCUS |
| **CX-UBI-SPEENHAMLAND** | UBI enacted **without** hour reduction **lowers** real wages | **0.55** | 0.45–0.65 | S_soc | U2 + Polanyi — blocks naive U4 |
| **CX-EDU-RESPONSE** | Education/reskilling **fails** to absorb C4 labor shock by 2032 | **0.60** | 0.50–0.70 | S_soc | **HIGH** — new cross-cut |
| **CX-ADMIN-FLIP** | 2028 US administration **materially** shifts federal AI posture | **0.50** | 0.40–0.60 | S_soc | **MED** — election crux |
| **CX-CHINA-CDZ** | China CDZ-style mobilization matches US frontier pace | **0.45** | 0.35–0.55 | S_geo | C3 + N9 |
| **CX-EMPTY-TREATY** | Major signed AI treaty **without** verification enforcement | **0.10** | 0.06–0.15 | S_geo | N9 T2 — complacency |
| **CX-NUKE-AI-COUP** | AI materially lowers nuclear command/control misjudgment risk **before** raising it | **0.40** | 0.30–0.50 | S_dual | **MED** — new primer node |
| **CX-QC-RELEVANT** | Cryptographically relevant quantum computer before 2035 | **0.15** | 0.08–0.25 | S_dual | LOW for AI timeline |
| **CX-SC-BREAK** | Room-temp superconductor **deployed** at grid scale by 2035 | **0.08** | 0.03–0.15 | S_dual | **[SPEC]** — U1 enabler tail |
| **CX-SPACE-ISRU** | ISRU / heavy lift breaks space deployment crux upward | **0.12** | 0.06–0.20 | S_dual | U4 LIFT milestones |

Full registry: [`05_crux_registry.md`](./05_crux_registry.md) §Tier 3.

---

## Recommended new research (granularity expansion)

Priority order for **20% research** passes — each becomes cross-cut or node extension:

| Priority | Deliverable | Status |
|----------|-------------|--------|
| **1** | **X3 — LAWS** — [`../spine/crosscut_x3_laws_evidence_rationale.md`](../spine/../spine/crosscut_x3_laws_evidence_rationale.md) | ✅ |
| **2** | **X4 — Education** — [`../spine/crosscut_x4_education_evidence_rationale.md`](../spine/../spine/crosscut_x4_education_evidence_rationale.md) | ✅ |
| **3** | **X5 — Admin/elections** — [`../spine/crosscut_x5_admin_evidence_rationale.md`](../spine/../spine/crosscut_x5_admin_evidence_rationale.md) | ✅ |
| **4** | **X6 — Science enablers** — [`../spine/crosscut_x6_science_evidence_rationale.md`](../spine/../spine/crosscut_x6_science_evidence_rationale.md) | ✅ |
| **5** | **X7 — UBI/SWF variants** — [`../utopia/node_u2_distribution_evidence_rationale.md`](../spine/../utopia/node_u2_distribution_evidence_rationale.md) | ✅ |

**Do not** add parallel Ci calendars — date **events** on S_phys/S_geo with **Ci gates** + lag columns in [`04_events_registry.md`](./04_events_registry.md).

---

## New events (registered — observables in cross-cuts)

| ID | Definition | Spine | Ci gate |
|----|------------|-------|---------|
| **EV-LAWS-MASS** | ≥3 states deploy autonomous strike systems without new restraint treaty | S_conflict | none |
| **EV-EDU-FED** | Federal AI-literacy / reskilling package >$10B enacted | S_soc | C4+ |
| **EV-ADMIN-28** | US administration with **opposite** AI posture takes office Jan 2029 | S_soc | none |
| **EV-TAIWAN-KINETIC** | Kinetic engagement Taiwan Strait | S_geo | none |
| **EV-SC-DEMO** | Credible room-temp SC device replicated ×3 labs | S_dual | none |
| **EV-SPACE-LIFT** | Starship-class or equivalent >100t LEO at <$500/kg sustained | S_dual | C7+ |

---

## How this changes workflow

[`01_workflow.md`](./01_workflow.md) Step 1–2 unchanged for **headline**. For **granular forecasts**:

1. Pick **primary spine** for the question (e.g. "UBI" → S_soc, not S_Ci).
2. Find **Ci gate** (if any) + **lag** (S_phys +12–24 mo).
3. Map to **event** → **crux candidate** → existing **node** or **new cross-cut**.
4. State **implications** on three regions (table above) before assigning P.

**Interview:** Ci + 1 non-Ci spine crux (e.g. "My load-bearing assumptions are no-pause **and** gains concentrate, not AGI date alone").

---

## Update log

| Date | Change |
|------|--------|
| 2026-07-05 | X7 UBI/SWF variants cross-cut — CX-UBI-SPEENHAMLAND, six variants A–F, EV-SWF |
| 2026-07-05 | X7 UBI/SWF variants cross-cut — CX-UBI-SPEENHAMLAND, EV-SWF |
| 2026-07-05 | X4 education cross-cut researched — CX-EDU-RESPONSE, EV-EDU-FED |
| 2026-07-05 | X3–X6 deep research complete — cross-cut + evidence rationale files |
| 2026-07-05 | Initial parallel spines + user topic coverage matrix |
| 2026-07-05 | X3 LAWS cross-cut delivered — LAWS row ✅ |
