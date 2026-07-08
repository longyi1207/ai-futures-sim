> **Ported from:** `notes/timeline_prediction/correlation_matrix.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Correlation Matrix — Timeline Probabilities

> **Parent:** [`../reference/03_ci_spine.md`](../reference/03_ci_spine.md)  
> **Purpose:** Which P's move together; **do not multiply as independent** when stitching p(doom).  
> **Date:** 2026-07-03

---

## How to use

When updating one probability, check **linked rows**. Joint tails are **smaller** than product of marginals only if correlation is positive on **bad** outcomes — we list direction.

**Notation:** ↑ = positive correlation (one up → other up); ↓ = negative; ≈ = weak.

---

## Master correlation table

| P / event | Correlates ↑ with | Correlates ↓ with | Cluster |
|-----------|-------------------|-------------------|---------|
| **P(no federal pause through 2028)** | Race acceleration (N3 T3); GAAIA preemption wins (N6 O1); Open-weight status quo (N5) | Multi-lab halt (N4 tail-gov); EU licensing (N4 tail) | **Race** |
| **P(BMIA / screening by 2027-12)** | Insider bio salience; Amodei/screendna coalition; EU Biotech Act | OSTP-only gridlock; GAAIA preemption **if** it kills state reporting | **Bio governance** |
| **P(Tier 3 before screening \| Tier 2)** | Open-weight tamper (N5 T5-B); regulatory delay tail (N2 TAIL-B); eval sandbagging | BMIA pass; IGSC v4; function-based SOC | **Bio tail** |
| **P(whistleblower modal \| E)** | Short media cycle; GAAIA audits no pause; labs continue training | Tail-gov halt; EU fast enforcement | **Alignment governance** |
| **P(race accelerates post-theft \| N3)** | P(no pause); P(export ctrl expansion); natsec framing | US–China treaty (N3 T2); verification R&D spend | **Geopolitics** |
| **P(GAAIA preemption wins)** | Industry lobbying; federal weak standard; P(no pause) +1–3pp | SB 53 enforcement; state transparency; Encode wins | **Federalism** |
| **P(open-weight ban)** | EU-only licensing (N5 T5-A); **not** US federal ban | Meta strategy; China open-weights PR | **Open weights** |
| **P(extinction \| misalign tail)** | Hard takeoff; deceptive alignment at C10; P(no shutdown) | Hanson slow takeoff; multipolar balance | **Misalignment** |
| **P(concentrated harm ↑)** | Node 1 labor modal; open weights; deskilling | — | **Societal** |
| **P(US frontier on triopoly \| N7)** | Stargate/GW deals; P(no pause); P(race post-theft N3) | Self-build >50% FLOPs; EU full decouple | **Compute chokepoint** |
| **P(cloud KYC / registration by 2028)** | BIS IaaS enforcement (N7); export ctrl (N3); CN block | Federal gridlock; industry lawsuit block | **Compute chokepoint** |
| **P(Fable-class API recall repeat)** | Natsec framing; P(no pause); deemed-export expansion | Commerce "no more recalls" policy | **Kill switch** |
| **P(EU/India sovereign decouple \| N7 T7-C)** | Node 3 T4 allied fracture; P(fragmentation) | EU–US joint cloud audit; CADA softened | **Sovereignty** |
| **P(outage >30d frontier delay \| N7 T7-A)** | Grid/cooling tails; US-EAST-1 concentration | Multi-region failover proven; zero >7d outages 2yr | **Infra tail** |
| **P(HEM pilot \| N7 T7-D)** | Export-controlled DC; Node 3 T2 treaty prep | HEM mandate on Stargate; FlexHEG product slip | **Verification** |
| **P(DPA DC seizure \| N7)** | Node 3 DPA; Node 4 executive tail; concentration | Actual seizure attempt; legal block | **Gov chokepoint** |
| **P(US governance paralysis S2)** | N6 O3 gridlock; N2 TAIL-B delay; P(no pause); EO-only framework | BMIA on time; GAAIA pass; fed CBRN eval | **Governance capacity** |
| **P(constitutional crisis S3)** | O1 preemption attempt; litigation vs SB53; race post-theft | State compliance clarity; multi-lab halt | **Federalism crisis** |
| **P(civil war-scale S4)** | N1 concentrated harm | Coordinated pause; BMIA | **Societal tail** |
| **P(CI export gating expands \| N8)** | N3 export ctrl; Fable recall (N7); P(no pause) | Training halt; cyber arms treaty | **Cyber / CI** |
| **P(offensive cyber surge \| salient E)** | N3 modal post-theft; natsec framing | Multi-lab halt; guardrails treaty | **Cyber / CI** |
| **P(T8-A AI cyber cascade)** | T8-D kinetic discussion; N3 T1 kinetic tail | Resilient OT segmentation; no compound E | **Cyber tail** |
| **P(agentic fraud industrialized)** | N1 labor modal; deskilling; N5 open-weight misuse | — | **Societal** |
| **P(open-weight blamed \| cyber E)** | N5 modal; N5 T5-B | Closed-model Mythos tier dominates narrative | **Open weights** |
| **P(hidden near-miss stays hidden \| N10)** | Tier 3 before screening; S2 paralysis; anthropic shadow | Mandatory disclosure law; SB53 incident duty enforced | **Disclosure** |
| **P(corp safety hollowing \| N11)** | P(no pause); P(no shutdown); E4 path | Board crisis → halt; PBC enforcement | **Governance hollowing** |
| **P(RSI locus cloud \| N12)** | Misalign tail; N7 race speed | Energy cap; Hanson variant | **Takeoff geometry** |

---

## Clusters (move as blocks)

### Cluster A — **Acceleration / race** (tight ↑)

```
P(no pause)  ↔  P(labs continue after whistleblower)  ↔  P(race post-theft)  ↔  P(GAAIA preemption)
```

**Joint tail example:** Whistleblower + no halt + theft + preemption ≈ **not** P₁×P₂×P₃ — treat as **~3–5×** the product of **marginal** tail probs (correlated).

### Cluster B — **Physical-layer bio mitigation** (tight ↑)

```
P(BMIA)  ↔  P(EU screening)  ↔  P(RAISE/SB53 compliance)  ↔  P(IGSC upgrade)
```

**Partial ↓ with Cluster A:** Screening can pass **while** race continues — **not** mutually exclusive (modal storyline).

### Cluster C — **Bio tail risk** (tight ↑)

```
P(Tier 3 before screening)  ↔  P(N2 TAIL-B delay)  ↔  P(N5 open-weight CBRN cascade)  ↔  P(hidden near-miss)
```

### Cluster D — **Transparency without brakes** (modal glue)

```
P(hearings N1)  ↔  P(whistleblower oversight N4 modal)  ↔  P(voluntary EO review)
```

**↓ with:** P(training halt), P(mandatory licensing)

### Cluster E — **Compute chokepoint** (Node 7; tight ↑ with Cluster A)

```
P(triopoly concentration N7)  ↔  P(cloud KYC N7)  ↔  P(export ctrl N3)  ↔  P(no pause)  ↔  P(Stargate/GW build)
```

**↓ with:** P(EU sovereign decouple T7-C), P(self-build >50% FLOPs), P(HEM pilot T7-D)

**Kill switch sub-cluster:** P(Fable recall) ↔ P(deemed export on models) ↔ P(CN cloud block) — **not** ↔ P(training halt) (modal decoupling)

### Cluster F — **Governance capacity** (crosscut US paralysis)

```
P(paralysis S2) ↔ P(N6 O3) ↔ P(N2 bio delay tail) ↔ P(no pause)
P(paralysis S2) ↓ P(BMIA on schedule)   [partial — EU/IGSC can offset]
P(crisis S3) ↔ P(EO preemption)         [ambiguous ↔ misalign speed]
```

**Stitching:** When S2 elevated (>25% scenario mix), apply modifier table in `crosscut_us_governance_capacity.md` — **don't** multiply P(BMIA) × P(GAAIA) × P(no pause) as independent; overlap with N6 O3 is **not additive**.

### Cluster G — **Cyber / CI** (Node 8)

```
P(CI export gating N8) ↔ P(export ctrl N3) ↔ P(Fable recall N7)
P(offensive cyber surge) ↔ P(N3 modal post-theft)
P(open-weight cyber uplift) ↔ P(N5 modal)
P(T8-A cascade) ↔ P(T8-D kinetic discussion)   [not execution]
P(T8-B vetting) ↔ P(T8-C surveillance)         [emergency bundle]
P(semi espionage) ↔ P(N3 theft attempt)
```

**Joint tail:** Don't multiply N8 T8-A × N3 T1 kinetic as independent — joint escalation tail ≈ **3–5×** product of marginals when both fire.

### Cluster H — **Disclosure / governance hollowing** (N10–N11)

```
P(hidden near-miss N10) ↔ P(Tier 3 before screening N2) ↔ P(BMIA delay S2)
P(corp hollowing N11) ↔ P(no pause) ↔ P(no shutdown) ↔ P(E4 no public leak N4)
P(interp prod halt N4) ↓ P(misalign conditional)     [partial — tail only]
P(epistemic collapse N2 ext) ↔ P(BMIA delay) ↔ P(S2 paralysis)
P(RSI locus cloud N12) ↔ P(misalign tail weight) ↔ P(N7 race speed)
P(RSI locus bio N12) ↔ P(bio tail weight) ↔ P(N10)
```

**Stitching:** N10 + S2 jointly move bio branch weight — use `my_pdoom.md` Phase 2b mixture, not P(N10)×P(S2) independent.

---

## Stitching rule for `my_pdoom.md`

**Don't:** `P(modal) × P(BMIA) × P(no pause)` as independent.

**Do:** Assign **scenario branch weights** (modal / bio-tail / misalignment-tail) that **already encode** correlation, then conditional P(extinction | branch).

---

## Update log

| Date | Change |
|------|--------|
| 2026-07-03 | Initial matrix from Phase 4c critique |
| 2026-07-04 | Node 7 rows + Cluster E (compute chokepoint) |
| 2026-07-04 | Cluster F + governance paralysis rows (`crosscut_us_governance_capacity.md`) |
| 2026-07-04 | Node 8 rows + Cluster G (cyber/CI) |
| 2026-07-04 | Cluster H + N10–N12 rows (Phase 2b zero omissions) |
