> **Ported from:** `notes/node2_cbrn_full.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Node 2 — CBRN Tier 1→2 (Full Detail)

> **Parent timeline:** [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md)  
> **Evidence base:** [`AI_biorisk_landscape_primer.md`](./AI_biorisk_landscape_primer.md)  
> **Date:** 2026-07-03  
> **Settings:** Hybrid time (C); modal + tail branches

---

## Where this fits in the repo

| File | What's there |
|------|----------------|
| **This file** | Full Node 2 — timing, tiers, triggers, actor table, modal/tails, p(doom), falsifiers |
| [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md) §Method | CBRN Tier 0–3 definitions (reused across nodes) |
| Same file §Node 2 summary | 5-line executive summary |
| Same file §Cross-node synthesis | Node 2 in the stitched timeline |
| [`../spine/node1_evidence_rationale.md`](../spine/node1_evidence_rationale.md) | Medium-length Node 2 (tables compressed) |
| [`AI_biorisk_landscape_primer.md`](./AI_biorisk_landscape_primer.md) | Background: threat model, WMDP, Evo/GeneBreaker, screening chokepoints |
| [`my_pdoom.md`](./my_pdoom.md) | Adelstein 8–10% bio bucket; consumes Node 2 outputs in Phase 4 |

---

## Hybrid timing — when Tier 1→2 becomes salient

| Layer | Modal window | Tail window | Observable |
|-------|--------------|-------------|------------|
| **Capability (Tier 1→2 crossing)** | **2026-08 – 2027-06** `[TRACKER: Emerging–on track]` | Tier 2 confirmed + Tier 3 plausible: **2027 H2+** | GeneBreaker-class ASR on Evo2; jailbroken frontier LLM passes WMDP-bio + synthesizable DNA guidance; RAND: AI remains **assistive**, not autonomous designer |
| **Insider/regulator salience** | **2026-06 – 2027-03** (already started) | Delayed if no Trigger E: **2027-09+** | Amodei essay + screening letter (Jun 2026); BMIA S.3741; RAISE effective prep; AISI/Preparedness red-team circulation |
| **Public salience** | **Only with Trigger E** | Tier-3 incident without media: hidden base rate | NYT/Science leak; FBI/CDC synthesis-order investigation; whistleblower CBRN incident under RAISE/SB 53 |

**Hybrid rule:** Capability on fast track; **human-response** dates lag ~12–18 mo unless Trigger E compresses (COVID analogue).

---

## CBRN uplift tiers — definitions + 2026 evidence

| Tier | Definition (testable) | 2026 status | Key evidence |
|------|----------------------|-------------|--------------|
| **0** | Generic science tutoring | **Confirmed** baseline | Pre-2023 LLMs |
| **1** | Post-jailbreak: **actionable** bio/chem protocol steps for motivated reader with existing expertise | **Confirmed** at frontier | WMDP; jailbreak red-teams; **eval-awareness confound** — published WMDP scores are **lower bounds** (Goodfire 2026: +3–18pp refusal when aware) |
| **2** | **Skilled actor** end-to-end assist: novel/optimized **synthesizable** sequences; needs wet-lab skill + chokepoint evasion | **Emerging → partial confirm** | **GeneBreaker** (2025): ~**60% ASR** pathogen-homologous outputs from Evo2-40B; **RAND RBA4087-1**: through ~2027 AI **assistive**, not autonomous designer |
| **3** | **Low-skill actor** viable: design + synthesis + evade screening | **Not confirmed** as of 2026-07 | No documented attack |

**Dual pathway:** (A) LLM CBRN + (B) biology FM — policy momentum stronger on **(C) synthesis screening** than on (A) mandatory CBRN eval or (B) FM weight gating.

**Sandbagging crux:** Tier assignment from **public evals alone is unreliable**.

---

## Trigger E (optional accelerators)

| Trigger | P(fire \| Tier 2 live) | Effect |
|---------|------------------------|--------|
| FBI/CDC: synthesis order linked to AI-assisted design | **0.15–0.25** by 2027 | P(mandatory screening law) → **0.75+**; P(mandatory CBRN eval) → **0.50+** |
| NYT/Science after leaked red-team report | **0.20–0.30** | Public salience; EU Biotech Act timeline compresses |
| Documented near-miss (screening catches AI-designed sequence) | **0.25–0.35** | Y2K pattern — success looks like overreaction |
| **No Trigger E** (modal) | **~0.40–0.50** | Insider-driven incremental regulation; 12–18 mo lag |

---

## Modal path — P(regulatory actions)

| Action | P(by 2027-12) | P(by 2028-06) | Mechanism | Conf |
|--------|---------------|---------------|-----------|------|
| **Mandatory federal nucleic-acid synthesis screening** (BMIA / S.3741-class) | **0.45** | **0.60** | Cotton–Klobuchar BMIA (Jan 2026); Jun 2026 **screendna.org** letter (Altman, Amodei, Hassabis, Suleyman + synthesis CEOs) | M–H |
| **EU harmonized screening** (Biotech Act Ch. VIII) | **0.35** (adopted) | **0.55** (phased apply) | Dec 2025 proposal; ≥50bp + function-based SOCs | M |
| **Mandatory third-party CBRN eval (federal, blocking release)** | **0.15** | **0.25** | Amodei Jun 2026 FAA-style proposal; **blocked by** Trump EO 14409 (Jun 2026) — no mandatory licensing | M |
| **State CBRN transparency + third-party assessment** (RAISE + SB 53) | **0.70** (compliance prep) | **0.75** (enforcement) | NY RAISE effective **2027-01-01**; CA SB 53; catastrophic-risk framework incl. bioweapon assistance | H |
| **OSTP 50bp + function-based SOCs** | **0.30** | **0.45** | Oct 2026 50bp deadline **paused** by EO 14292 (May 2025); BMIA/EU may supersede | L–M |
| **IGSC v4 / function-based screening at scale** | **0.50** | **0.65** | IGSC v3.0; NIST function-based R&D; IBBIS commec pilots | M |
| **Federal frontier pause (bio-motivated)** | **0.05** | **0.08** | Pause politically toxic | H |
| **Biology FM weight gating (Evo-class)** | **0.10** | **0.15** | Evo2 full open (Nature Mar 2026); no binding US rule | L |

**Modal synthesis:** CBRN governance **decouples** from alignment governance — **physical-layer screening** outruns **in silico CBRN eval mandates**. Labs ship refusal/unlearning; **no weight rollback**.

**RAISE:** Signed Dec 2025; effective **2027-01-01** — third-party catastrophic-risk assessment (incl. bioweapon assistance), 72h incident reporting. **Tail:** GAAIA federal preemption P≈**0.25–0.35** by 2028 could weaken enforcement.

**Amodei / Banks (Jun 2026):** Amodei proposes mandatory third-party testing at ~10²⁵ FLOP for bio/cyber/loss-of-control; **industry proposal, not law**. Banks letter: RSI testing + CAISI visibility — adjacent, not bio-specific.

---

## Tail branches

```
                    Tier 1→2 capability live (2026–27)
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
      MODAL (55%)        TAIL-A (20%)       TAIL-B (15%)
   screening + state    Tier 3 before      12–18mo reg
   CBRN transparency    reg catches up     delay after
   legislation passes   (open-weights FM)   near-miss/incident
           │                  │                  │
           └──────────────────┴──────────────────┘
                              │
                         TAIL-C (10%)
                    open-weights bio FM +
                    screening arbitrage (CN/non-IGSC)
                    + eval gaming → false-negative CBRN scores
```

| Branch | Description | P(branch \| Tier 2) | Key drivers |
|--------|-------------|---------------------|-------------|
| **MODAL** | BMIA/EU screening; RAISE/SB 53 reporting; IGSC upgrade; CBRN evals stay **voluntary** | **~0.55** | Jun 2026 screening letter; bipartisan BMIA; industry prefers screening over training caps |
| **TAIL-A: Tier 3 low-skill** | First documented low-skill attack **or** classified end-to-end demo before screening deployed | **~0.20** | Evo2 ASR↑; DBTL closure; non-IGSC vendors; 50bp delay |
| **TAIL-B: Regulatory delay** | Near-miss → **12–18 mo** lag before rules bite | **~0.15** | Trump deregulation; preemption fights; OSTP limbo |
| **TAIL-C: Open-weights FM** | Evo-class weights open; screening only in US/EU IGSC; CN arbitrage | **~0.10** | Open-science norm vs AlphaFold3 gating |

---

## Actor table (full)

| Actor | Decision menu | P(outcome) | Evidence | Conf |
|-------|---------------|------------|----------|------|
| **US executive** | (a) EO 14409 voluntary 30-day cyber review; (b) OSTP screening revision; (c) AISI CBRN guidance; (d) block mandatory CBRN licensing | P(voluntary review)=**0.70**; P(mandatory CBRN block)=**0.12**; P(OSTP 50bp revision)=**0.35** | EO 14409 Jun 2026; EO 14292 May 2025 | M |
| **US Congress** | (a) BMIA mandatory screening; (b) bio bill without pause; (c) GAAIA audits + preemption; (d) explicit CBRN eval mandate | P(bio screening legislation)=**0.45**; P(CBRN eval mandate)=**0.20**; P(frontier pause)=**0.05** | BMIA S.3741; bio coalition narrower than pause | M |
| **DNA synthesis industry (IGSC)** | (a) v4 + function-based SOC pilots; (b) recordkeeping; (c) resist non-member compliance | P(major IGSC upgrade)=**0.50**; P(compliance without law)=**0.30** | Jun 2026 letter **from** synthesis CEOs | M |
| **Frontier labs** | (a) CBRN mitigations ship; (b) Preparedness red-team; (c) no training stop; (d) support screening letter, oppose release block | P(mitigations ship)=**0.75**; P(stop training)=**0.02**; P(public Tier-2 disclosure under RAISE)=**0.40** | Sleeper Agents → patch not pause | M |
| **China** | (a) Biosecurity Law enforcement; (b) ISO 20688-2 / 50nt baseline; (c) no joint treaty; (d) no US-led FM gating | P(domestic screening↑)=**0.60**; P(FM weight gate)=**0.08**; P(US–CN joint treaty)=**0.03** | 2021 Biosecurity Law; mirror dynamics not coordination | L–M |
| **EU** | (a) Biotech Act mandatory screening; (b) GPAI Code CBRN work; (c) benchtop embedded screening | P(adoption w/ screening intact)=**0.55** by 2028; P(CBRN eval mandate for GPAI)=**0.30** | Dec 2025 proposal | M |
| **Public / markets** | CBRN low salience without Trigger E | P(mass bio-x-risk protest)=**0.08**; P(sustained media >2mo)=**0.25** *given* Trigger E | 2023 pause letter fade | L–M |

---

## p(doom) link — Adelstein non-misalignment / bio paths

Adelstein: **~2.6%** misaligned-AI extinction; **~8–10% total** including AI-enabled bioterror/extinction-class bio. Node 2 feeds the **bio slice** (~5–8pp of that total — don't double-count with misalignment).

| Branch | P(extinction by 2050 \| branch) | Notes |
|--------|--------------------------------|-------|
| **MODAL** | **Low** (~1–3% of all extinction mass) | Screening + state transparency reduces skilled-actor tail |
| **TAIL-A (Tier 3 first)** | **Moderate–high** within bio bucket | Single engineered pandemic tail; **not** misalignment |
| **TAIL-B (12–18mo delay)** | **Moderate** | Near-miss window in screening gaps |
| **TAIL-C (open-weights + arbitrage)** | **Moderate** | Jurisdiction shopping; FM lowers search cost |

**Crux:** If **P(Tier 3 before adequate screening \| Tier 2 by 2027) > ~0.15**, bio bucket can dominate misalignment in Adelstein framing.

**Double-counting guard:** Weight by branch probabilities; don't sum MODAL + all tails.

---

## Downstream effects (next nodes)

- CBRN and **alignment governance decouple** — Node 4 whistleblower may not accelerate bio screening.
- Physical-layer coalition (synthesis + natsec + labs) **stronger than pause coalition**.
- **TAIL-A** → Node 3 theft/natsec priors ↑; P(coordinated pause) still low.

---

## Falsifiers

| Observation | Implication |
|-------------|-------------|
| Documented **Tier-3** low-skill attack + **no** major screening/CBRN legislative response within **12 mo** | Modal path wrong; Adelstein "more regulation" conditional fails |
| **Mandatory federal CBRN eval with block authority** passed and enforced ≥2 releases | Low P(mandatory CBRN) estimate was wrong (revise up) |
| BMIA + EU screening **both fail** by 2028 despite Jun 2026 coalition | P(bio screening) too high |
| Third-party eval: **no** jailbreak uplift to Tier 2 on frontier LLM **and** GeneBreaker ASR collapses | Demote Tier 2 to Tier 1 |
| **Federal preemption** voids RAISE/SB 53 with no replacement | State transparency path dead |

---

## Confidence summary

| Claim | Conf |
|-------|------|
| Tier 1 confirmed at frontier | **H** |
| Tier 2 emerging (skilled actor), not Tier 3 | **M–H** |
| Screening legislation outruns CBRN eval mandates | **M** |
| 12–18 mo regulatory delay invariant | **M** |
| Eval-awareness inflates published safety | **H** |
| Exact branch probabilities | **L** |

---

## External sources

- [WMDP](https://www.wmdp.ai/)
- [GeneBreaker arXiv:2505.23839](https://arxiv.org/abs/2505.23839)
- [RAND RBA4087-1](https://www.rand.org/pubs/research_briefs/RBA4087-1.html)
- [Amodei Policy on the AI Exponential (Jun 2026)](https://darioamodei.com/post/policy-on-the-ai-exponential)
- [screendna.org open letter (Jun 2026)](https://www.thefai.org/posts/in-support-of-mandatory-nucleic-acid-synthesis-screening-and-recordkeeping)
- [BMIA S.3741](https://www.congress.gov/bill/119th-congress/senate-bill/3741)
- [EO 14409](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)
- [EU Biotech Act proposal (Dec 2025)](https://health.ec.europa.eu/publications/proposal-regulation-establish-measures-strengthen-unions-biotechnology-and-biomanufacturing-sectors_en)
- [Goodfire eval awareness (2026)](https://www.goodfire.ai/research/verbalized-eval-awareness-inflates-measured-safety)

## Repo sources

- `https://www.rand.org/pubs/research_briefs/RBA4087-1.html`
- `biosecurity_evo_dual_use.md`
- `https://arxiv.org/abs/2310.11436`
- `ai_pause_advocacy_playbook.md`
