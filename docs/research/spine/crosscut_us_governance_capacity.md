> **Ported from:** `notes/timeline_prediction/crosscut_us_governance_capacity.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Cross-Cut — US Domestic Instability & Governance Capacity

> **Parent:** [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md)  
> **Correlates:** [`correlation_matrix.md`](./correlation_matrix.md) · Node 1 T2 · Node 2 BMIA · Node 6 GAAIA  
> **Purpose:** Modifier layer on node P's — **not** a separate timeline node. Main crux = **governance paralysis blocking federal AI law**; civil war-scale = **low tail**.  
> **Date:** 2026-07-04

---

## Executive summary

US AI timeline risk is dominated by **institutional throughput**, not kinetic domestic conflict. Through Jul 2026: record **43-day** FY2026 shutdown (Sep–Nov 2025), brief Jan 2026 lapse, **76-day DHS** partial shutdown (Feb–Apr 2026); Commerce/Science appropriations passed but **AI omnibus legislation stalls** on preemption fights; **CA/NY frontier bloc converges** (SB 53 + RAISE) while **TX/FL** stay disclosure/deepfake-focused; Trump EO 14365 (Dec 2025) + National Policy Framework (Mar 2026) push **federal preemption** without passing statute.

**Modal path (~55%):** friction + gridlock → **states primary**, narrow bio bills **eventually** pass, GAAIA/BMIA **delayed not dead**.  
**Elevated paralysis (~28%):** repeated CRs, committee starvation, AISI/NIST underfunding → apply **×0.6–0.7** to federal enactment P's.  
**Constitutional-crisis tail (~10% by 2030):** contested legitimacy, enforcement vs blue states, court injunction wars — **ambiguous** for misalign (↓ coordination, ↑ race speed).  
**Civil war-scale (~3% by 2030):** organized interstate armed conflict — **exclude from modal planning**; include only in p(doom) **societal whimper** channel.

---

## Core probabilities (this cross-cut)

| Event | P(by horizon) | Role | Conf |
|-------|---------------|------|------|
| **P(governance paralysis materially delays/blocks federal AI law)** | **0.55** by 2028 | **Main crux** — default modifier path | M |
| **P(elevated paralysis: ≥2 multi-week shutdowns + no major AI statute)** | **0.28** by 2028 | Apply full modifier table | M |
| **P(constitutional crisis affecting AI federalism)** | **0.10** by 2030 | Tail — courts/EO vs states | L–M |
| **P(civil war-scale domestic conflict)** | **0.03** by 2030 | **Low tail** — not main path | L |

**Definition — governance paralysis (operational):** Any 12-month window where (a) ≥1 shutdown or CR **>90 days** covering Commerce, Judiciary, or HHS; **and** (b) no GAAIA-class or BMIA-class bill reaches **presidential signature** despite committee referral; **and** (c) median federal AI rulemaking comment-to-final **>18 mo** (vs playbook 12–18 mo invariant).

**Definition — constitutional crisis (AI-relevant):** Contested federal legitimacy **plus** active federal litigation/task force (EO 14365-class) seeking to **enjoin or preempt** blue-state frontier laws **before** Congress settles preemption text — i.e. governance by injunction, not statute.

---

## Scenario tree (2025–2030)

```
                    US governance capacity
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
    MODAL (55%)         PARALYSIS (28%)      CRISIS TAIL (10%)
    friction+gridlock   shutdown+CR loop     legitimacy+injunction
         │                    │                    │
    N6 O3 default       BMIA×0.7, GAAIA×0.6   race↑, law ambiguous
    states primary      AISI $ delayed         misalign ±
         │                    │                    │
         └────────────────────┴────────────────────┘
                              │
                    CIVIL WAR-SCALE (3%) — parallel low tail
```

---

## Mechanism channels

### 1. Shutdown / appropriations paralysis

**Claim:** Shutdowns **do not stop** frontier labs; they **do** starve NIST/CAISI, Commerce committee bandwidth, and grant-driven safety research.

**Why:** BMIA (S.3741) sits in **Commerce** — same subcommittee stack as CJS appropriations fights. Credence Wire (Jun 2026): **$12B AI research package** split DOD vs NSF/NIST; Freedom Caucus riders blocked House markup — AI $ bundled, not standalone.

**Evidence:**
- Brookings — 43-day FY2026 shutdown (longest to date), Jan 2026 brief lapse, **76-day DHS** shutdown ended Apr 30 2026
- FAS Gil on the Hill Feb 2026 — partial shutdown **ongoing** on DHS/ICE line
- `../supplements/ai_pause_advocacy_playbook.md` §1.2 — federal dysfunction default; Cruz stripped 99–1 shows **anti-preemption** coalition survives even in crisis Congress
- `node6_evidence_rationale.md` — O3 gridlock **0.45** already modal

**Modifier:** P(BMIA signed by 2027-12) **×0.70** under elevated paralysis; P(GAAIA any pass) **×0.60**.

**Conf:** M

---

### 2. Federal–state split & red–blue legislative divergence

**Claim:** **Bifurcated federalism** — CA/NY/IL **frontier transparency bloc** vs TX/FL **gov-use + deepfake** lanes — increases **compliance surface** but **not** uniform pause capacity.

**Why:** RAISE amended Mar 2026 to track SB 53 (Carnegie, Lexology); TX TRAIGA effective Jan 2026 focuses gov procurement; **50+ states** on deepfakes/elections (Regulations.ai summary). Divergence **helps** bio screening (narrow physical chokepoint bills cross ideology) but **hurts** unified frontier licensing.

**Evidence:**
- `<!-- private monorepo only -->` §3.4 — GAAIA vs SB 53 preemption table
- KPMG 2026 reg alert — CA/NY "unified benchmark"; deferral if **federal** reporting ≥ state
- Law.com Jan 2026 — EO 14365 challenges Jan 1 effective dates; **courts unsettled**
- `node2_evidence_rationale.md` — RAISE/SB53 P **0.70** by 2027-12

**Modifier:** Under modal friction, P(RAISE/SB53 enforced) **×1.05** (states fill vacuum). Under **successful GAAIA preemption (O1)**, **×0.55** on state dev-stage duties — see Node 6.

**Conf:** M–H on divergence; L–M on court outcomes

---

### 3. Courts & constitutional crisis tail

**Claim:** **Judicial federalism fights** are more likely than civil war; they **delay** and **polarize** AI rulemaking without stopping capability.

**Why:** EO 14365 (Dec 2025) + AI Litigation Task Force + Mar 2026 Framework call for **preemption**; GUARDRAILS Act (House Ds) seeks EO repeal — symmetric escalation. Gibson Dunn Mar 2026: comprehensive federal AI faces **narrow window, bipartisan anti-preemption, House–Senate split**.

**Evidence:**
- Gibson Dunn — National Policy Framework Mar 20 2026; headwinds enumerated
- `<!-- private monorepo only -->` §3.4 — Encode/Wiener preemption fight
- Nextgov Feb 2026 — Obernolte: moratorium was **not** long-term; preemption must ride **same bill** as federal standard

**Tail behavior:**
- **↑** P(EO-only federal framework) Node 6 **O4** (+5pp conditional on crisis)
- **↓** P(BMIA) if Commerce frozen; **↑** if framed as **natsec** narrow bill (Cotton–Klobuchar lane)
- Misalign: **ambiguous** — less epistemic coordination, more race (see p(doom) below)

**Conf:** L–M

---

### 4. Epistemic & democratic response capacity

**Claim:** Paralysis ** degrades** government's ability to **interpret** frontier risk — not public belief in risk.

**Why:** AISI/CAISI codification in GAAIA depends on **statute + appropriations**; shutdown RIF threats (Vought Sep 2025 memo, Brookings) even if partially reversed, drain institutional memory. Modal Node 4 path already assumes **oversight without halt** — paralysis **reinforces** that modal.

**Evidence:**
- `crosscut_physical_economy_limits.md` — slow track +30% politics vs capability
- `node4_evidence_rationale.md` — whistleblower modal, media fatigue
- Carnegie Feb 2026 — states lack capacity to **analyze** incident reports under SB 53/RAISE

**Modifier:** P(mandatory CBRN eval federal) **×0.75**; P(whistleblower → binding halt) **×0.85**; P(hearings within 90d of shock) **×0.90** (still high — Congress **talks** under paralysis).

**Conf:** M

---

## Modifier framework — how to scale node P's

**Usage:** Multiply **baseline node P** (from node rationale files) by factor below when cross-cut scenario is **active**. Do **not** double-apply Node 6 O3 gridlock (0.45) **and** full paralysis stack — use **Scenario column**.

| Scenario | Trigger (simplified) | Duration |
|----------|----------------------|----------|
| **S0 — Baseline** | Repo defaults (Jul 2026) | — |
| **S1 — Modal friction** | P=0.55; partial shutdown history but BMIA/GAAIA **possible** | 2026–2028 |
| **S2 — Elevated paralysis** | P=0.28; ≥2 CR/shutdown cycles + zero major AI signature | 2026–2029 |
| **S3 — Constitutional tail** | P=0.10; EO litigation + contested enforcement | 2027–2030 |
| **S4 — Civil war-scale** | P=0.03; organized interstate conflict | tail only |

### Master modifier table

| Node / P | Baseline (S0) | S1 Modal × | S2 Paralysis × | S3 Crisis × | Notes |
|----------|---------------|------------|----------------|-------------|-------|
| **N2 P(BMIA by 2027-12)** | 0.45 | 1.00 | **0.70** → 0.32 | 0.55 | Narrow bipartisan; survives paralysis **better** than GAAIA |
| **N2 P(BMIA by 2028-06)** | 0.60 | 1.00 | **0.75** → 0.45 | 0.65 | Second session recovery |
| **N2 P(EU screening)** | 0.35 / 0.55 | 1.00 | 1.00 | 1.00 | **Decoupled** from US shutdown |
| **N2 P(Tier 3 before screening \| T2)** | tail | 1.00 | **1.15–1.25** | **1.10–1.20** | Bio tail **↑** if US delay |
| **N2 P(OSTP 50bp)** | 0.30 | 0.95 | **0.60** | 0.50 | Already limbo; paralysis kills |
| **N6 P(any GAAIA-like federal)** | 0.30 | 1.00 | **0.60** → 0.18 | 0.40 | Omnibus needs functioning Congress |
| **N6 P(O1 preemption wins)** | 0.12 | 1.00 | 0.75 | **1.20** → 0.14 | Crisis **may** push uniformity — low absolute |
| **N6 P(O3 gridlock, states primary)** | 0.45 | **1.10** → 0.50 | **1.25** → 0.56 | 0.90 | Paralysis **is** gridlock |
| **N6 P(O4 EO-only framework)** | 0.25 | 1.05 | 1.15 | **1.25** | Substitute when statute fails |
| **N1 P(GAAIA enacted w/ preemption)** | 0.20 / T2 0.12 | 1.00 | 0.65 | 0.80 | Overlaps N6 |
| **N1 P(SB53 compliance)** | 0.85 | 1.02 | 1.05 | 0.88 | Unless injunction |
| **N1 P(federal training cap)** | <0.05 | 0.90 | **0.50** | 0.40 | Already near floor |
| **N1 P(hearings 90d post-shock)** | 0.75 | 0.95 | 0.90 | 0.85 | Congress still performs |
| **N3 P(race accelerates post-theft)** | modal ↑ | 1.03 | **1.08** | **1.10** | Weak federal response |
| **N4 P(whistleblower modal oversight)** | ~0.58 | 1.05 | 1.08 | 1.05 | Transparency without brakes |
| **N4 P(tail-gov halt)** | tail | 0.95 | **0.85** | 0.80 | Paralysis cuts **positive** tail too |
| **N5 P(US open-weight ban)** | ~0.12 | 0.95 | 0.90 | 0.85 | No bandwidth for ban politics |
| **P(no effective pause through 2028)** | ~0.85 | 1.02 | **1.05–1.08** | 1.03 | +3–8pp **relative** not additive |

**Stitching rule:** When assigning branch weights in `my_pdoom.md`, if S2 active, shift **~5–8pp** from modal governance branch toward **bio-tail** branch (screening delay), not misalign-extinction branch.

---

## Modal vs tail (this cross-cut)

| Path | P | AI policy signature | p(doom) channel |
|------|---|---------------------|-----------------|
| **Modal — friction federalism** | **55%** | SB53/RAISE live; BMIA **late 2027–28**; GAAIA dies or strips preemption; EO audits | Bio tail trimmed **if** BMIA passes; misalign **unchanged** |
| **Elevated paralysis** | **28%** | States only + IGSC; BMIA **2028+**; AISI underfunded | **Bio tail ↑** (+3–6pp extinction conditional on T2) |
| **Constitutional tail** | **10%** | Injunction wars; possible EO "win" on preemption | Misalign **ambiguous**; societal whimper ↑ |
| **Civil war-scale** | **3%** | Governance collapse; labs **de facto** autonomous | Whimper >> extinction; not AI-specific |

---

## p(doom) channels

| Channel | Direction under S1/S2 | Mechanism |
|---------|----------------------|-----------|
| **Bio tail (Tier 3 before screening)** | **↑** under S2 | BMIA ×0.7; IGSC voluntary lag; EU partial decouple |
| **Misalignment extinction** | **Ambiguous** | ↓ coordinated eval capacity; ↑ race speed (N3, N4 modal); net **±0–2pp** on **19%** pt est |
| **No pause / race** | **↑** | Paralysis correlates with Cluster A in `correlation_matrix.md` |
| **Societal whimper** | **↑** | Node 1 labor shock + weak federal transition law; **not** extinction |
| **Civil war-scale** | **↑ whimper, ≈0 direct extinction** | Treat as **domestic catastrophe** modifier on Node 1 concentrated harm, not misalign |

**Load-bearing interaction:** S2 **does not** justify raising extinction above **~22%** without independent misalign evidence — bio tail is the primary moved margin.

---

## Evidenced probability sections

### P = 0.55 — Governance paralysis blocks timely federal AI law (main crux)

**Claim:** **~55%** that US federal AI **omnibus** (GAAIA-class) fails or slips past 2028 **and** BMIA-style enactment is delayed **≥12 mo** vs base case, due to shutdown/CR/appropriations dysfunction — **without** civil war.

**Why:** Node 6 O3 already **0.45** gridlock; add shutdown-era Commerce bandwidth loss + midterm narrowing (Gibson Dunn). Not mutually exclusive with ** eventual** BMIA — paralysis **delays**, doesn't always **kill**.

**Evidence:**
- Brookings shutdown tracker 2025–2026
- Node 6 O3 **0.45**; BMIA committee referral Jan 29 2026, no floor vote Jul 2026
- Playbook §313 — "Will federal preemption pass?" = open; default **no** on timeline

**Analogue:** Post-Sandy Hook — salience + gridlock; state action (CT) while federal stalls.

**Would update if:** GAAIA or BMIA **signed** before Dec 2026 → revise down to **≤0.35**.

**Conf:** M

---

### P = 0.28 — Elevated paralysis (full modifier stack)

**Claim:** **~28%** conditional world: ≥2 multi-week shutdown/CR cycles in 2026–28 **and** zero presidential signature on GAAIA/BMIA by end 2028.

**Why:** DHS 76-day shutdown demonstrates **single-issue veto** capacity; AI rides omnibus (Credence Wire); Freedom Caucus + CBC blocking pattern repeatable.

**Evidence:**
- FAS Feb 2026 — DHS funding unsettled after other agencies funded
- Credence Wire Jun 2026 — House AI $ markup stalled

**Would update if:** Bipartisan Commerce markup on BMIA **and** CJS full-year pass without CR → revise to **≤0.15**.

**Conf:** M

---

### P = 0.10 — Constitutional crisis affecting AI federalism (by 2030)

**Claim:** **~10%** that contested federal legitimacy + active preemptive litigation **materially** disrupts SB 53/RAISE enforcement for **≥6 mo** in 2027–30 window.

**Why:** EO 14365 task force + GUARDRAILS backlash + Obernolte preemption-in-same-bill strategy → **court-first** federalism. Still **not** civil war — injunction/removal chain.

**Evidence:**
- Law.com Jan 2026; Gibson Dunn Mar 2026 Framework
<!-- private monorepo only: - `[private note]` §3.4 -->

**Would update if:** Supreme Court **upholds** state frontier laws against EO preemption with narrow ruling → crisis path weakens to **≤0.05**.

**Conf:** L–M

---

### P = 0.03 — Civil war-scale domestic conflict (by 2030)

**Claim:** **~3%** organized **interstate** armed conflict with federal command breakdown — **low tail** for timeline planning.

**Why:** Polarization ↑ (shutdown weaponization, ICE politicization) but **no** institutional secession cascade analogous to 1860; military chain intact in modal forecasts. Include for **tail completeness** only.

**Evidence:**
- Brookings — shutdown economic damage; no interstate war gaming in mainstream policy shops
- Node 1 rationale — political instability → **whimper**, not extinction modal

**Would update if:** Sustained **multi-state** National Guard vs federal deployment cycle **>90 days** with congressional impasse → revise to **0.08–0.12**.

**Conf:** L

---

### P = 0.45 base × 0.70 — BMIA under elevated paralysis (worked example)

**Claim:** Under S2, P(BMIA by 2027-12) drops from **0.45 → ~0.32**.

**Why:** Commerce committee calendar + rulemaking staff; bipartisan **narrow** bill still **more resilient** than GAAIA (0.30 × 0.60 → 0.18). screendna coalition (Jun 2026) provides **floor**.

**Evidence:**
- Node 2 BMIA § P=0.45
- ARI / Cotton–Klobuchar endorsements Jan 2026
- Playbook — physical chokepoint bills **win** vs pause letters

**Conf:** M

---

## Integration with existing nodes

| Existing artifact | Relationship |
|-------------------|----------------|
| Node 6 O3 **0.45** | S1 modal friction **overlaps** — do not add linearly |
| Node 2 BMIA **0.45** | Apply S2 ×0.70 when elevated paralysis scenario selected |
| `crosscut_physical_economy_limits.md` slow track +30% | **Same mechanism** — this doc **names** US governance as driver |
| `correlation_matrix.md` Cluster A | Paralysis **↑** P(no pause) — add explicit row |
| `my_pdoom.md` modal 58% | S2 shifts **~5–8pp** to bio-tail branch |

---

## Suggested updates to `correlation_matrix.md`

Add rows:

| P / event | Correlates ↑ with | Correlates ↓ with | Cluster |
|-----------|-------------------|-------------------|---------|
| **P(governance paralysis S2)** | P(N6 O3 gridlock); P(N2 TAIL-B delay); P(no pause); P(EO-only O4) | P(BMIA on time); P(GAAIA pass); P(mandatory federal CBRN eval) | **Governance capacity** |
| **P(constitutional crisis S3)** | P(N6 O1 preemption attempt); P(litigation vs SB53); P(race post-theft) | P(state compliance clarity); P(multi-lab halt) | **Federalism crisis** |
| **P(civil war-scale S4)** | Node 1 concentrated harm; political whimper | P(coordinated pause); BMIA passage | **Societal tail** |

Add **Cluster E — Governance capacity**:

```
P(paralysis S2)  ↔  P(N6 O3)  ↔  P(N2 bio delay tail)  ↔  P(no pause)
P(paralysis S2)  ↓  P(BMIA on schedule)   [partial ↓ only — EU/IGSC offset]
P(crisis S3)     ↔  P(EO preemption)       [ambiguous ↔ misalign]
```

Add stitching note:

> When S2 weight **>25%** in scenario mix, **do not multiply** P(BMIA) × P(GAAIA) × P(no pause) as independent — see [`crosscut_us_governance_capacity.md`](./crosscut_us_governance_capacity.md) modifier table.

---

## Open questions

1. Does **DHS-only** shutdown pattern repeat FY2027 without touching Commerce — reducing S2 severity?
2. Will BMIA **detach** to standalone floor vote (natsec framing) under paralysis?
3. Court timeline for EO 14365 vs SB 53 — injunction before or after 2028 election?
4. Does state **enforcement capacity** (Carnegie critique) matter for p(doom) or only federal?

---

## Sources

<!-- private monorepo only: - `[private note]` §3.4–3.5 -->
- `../supplements/ai_pause_advocacy_playbook.md` §1.2, §313  
- `node1_evidence_rationale.md` — T2, SB53, anti-preemption  
- `node2_evidence_rationale.md` — BMIA, RAISE, TAIL-B  
- `node6_evidence_rationale.md` — O1–O4  
- https://www.brookings.edu/articles/what-is-a-government-shutdown-and-why-are-we-likely-to-have-another-one/  
- https://fas.org/publication/gil-on-the-hill-february-2026/  
- https://www.gibsondunn.com/toward-a-national-ai-policy-the-trump-administration-releases-proposed-framework-for-federal-legislation/  
- https://www.nextgov.com/artificial-intelligence/2026/02/ai-moratorium-was-never-long-term-solution-lawmaker-says/411223/  
- https://rollcall.com/2026/06/04/bipartisan-ai-draft-proposes-three-year-preemption-of-state-laws/  
- https://carnegieendowment.org/emissary/2026/02/ai-state-law-new-york-raise-act-california-sb53  
- https://www.congress.gov/bill/119th-congress/senate-bill/3741  

---

## Update log

| Date | Change |
|------|--------|
| 2026-07-04 | Initial cross-cut: modifier framework, core P's, correlation_matrix suggestions |
