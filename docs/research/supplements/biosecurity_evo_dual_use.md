> **Ported from:** `notes/research_ai_medicine_longevity/10_biosecurity_evo_dual_use.md` · snapshot from private monorepo · canonical edit in private monorepo until OSS lock

# Biosecurity × Evo: genomic foundation models as dual-use AI

> **Date:** 2026-05-30  
> **Audience:** AI safety researchers crossing into AI×bio  
> **Broader biorisk map (start here if new):** `https://www.rand.org/pubs/research_briefs/RBA4087-1.html`  
> **Related:** `<!-- private monorepo only -->`, `<!-- private monorepo only -->`, `code/safety_interventions/`

---

## Executive summary

**Evo/Evo2** (Arc Institute) are autoregressive DNA foundation models that both **predict** and **generate** functional genomic sequences at up to megabase context — with lab-validated outputs including CRISPR systems, anti-CRISPRs, and toxin:antitoxin pairs. The same stack that accelerates longevity and drug discovery (target finding, protein design, synthetic biology) lowers the skill floor for designing pathogenic or toxin-encoding DNA, especially when paired with cheap synthesis and automated wet labs. Governance today is **layered but porous**: IGSC/OSTP synthesis screening, NIH DURC/PEPP for funded wet-lab work, BSL containment — but Evo weights are **fully open**, screening is pattern-matching (evadable), and model-release norms (cf. AlphaFold3) remain unsettled for generative biology FMs.

---

## 1. What Evo / Evo2 is (technical)

**Evo** (Science, Nov 2024; 7B params, 131 kb context) and **Evo2** (Nature, Mar 2026; up to 40B params, 1 Mb context) are autoregressive genomic language models from Arc Institute (+ Stanford, UCSF, Berkeley, NVIDIA, Goodfire, UW). Architecture: **StripedHyena 2** (sub-quadratic long-context SSM hybrid), trained on **OpenGenome2** (~8.8–9 T nucleotides across prokaryotes, eukaryotes, phage, humans). Single-nucleotide resolution; zero-shot variant effect prediction (e.g. BRCA1, noncoding pathogenic SNPs) without task-specific fine-tuning. **Generative mode:** autoregressive completion / semantic design of DNA segments; experimentally validated designs include functional **CRISPR-Cas systems**, **mobile genetic elements** (Evo1), **anti-CRISPR proteins** and **toxin:antitoxin modules** (Evo 1.5). Weights, inference code, SAE interpretability tooling, and an **Evo Designer** web UI are public (GitHub, HuggingFace, NVIDIA BioNeMo NIM). This is not structure prediction (AlphaFold) — it is **sequence design in the generative regime**, closer to a biology Codex than a biology calculator.

---

## 2. Dual-use framing

| Beneficial path | Misuse path |
|-----------------|-------------|
| Longevity target discovery via variant effect + regulatory element modeling | Design/modify **virulence factors**, receptor-binding domains, immune-evasion motifs |
| CRISPR / gene-editing tool design for therapy | Design **toxin genes**, **select-agent-adjacent** modules, anti-defense systems |
| Synthetic biology for biomanufacturing, phage therapy | **Codon-optimized** sequences that evade naive screening while retaining function |
| Accelerating drug discovery pipelines (with AlphaFold, automated labs) | Iterative **in silico → synthesize → test** loops for pathogen optimization |

The dual-use is **structural**, not incidental: generative capability + biological grounding is exactly what makes the model useful for medicine. Unlike LLM text harm (policy refusal, jailbreaks), the hazard is **physical instantiation** — a designed sequence that becomes DNA in a tube.

**Beneficial uses** sit in the same repo thread as your longevity research (`03_real_science.md`, Insilico, Isomorphic/AlphaFold3). **Misuse paths** do not require AGI — a motivated actor with biology grad-student literacy + GPU + synthesis budget may suffice, with the FM acting as search/optimization oracle.

---

## 3. Concrete risk mechanisms (not vague)

Three multiplicative factors — any one alone is manageable; together they compress timelines:

### 3.1 Genomic FM as search engine

- **Generative completion:** propose novel ORFs, regulatory cassettes, or viral segments conditioned on context.
- **In silico optimization:** mutate sequences for stability, expression, binding — BIORISKEVAL framework tests this on Evo2-7B along GEN / MUT / virulence-prediction axes (OpenReview 2025).
- **Jailbreaking:** **GeneBreaker** (2025) uses LLM-agent prompt design + beam search steered by pathogenicity LM to elicit pathogen-homologous outputs from Evo series; reports up to **~60% attack success rate** on Evo2-40B across viral categories, with SARS-CoV-2 spike and HIV-1 envelope case studies. Scaling model size **increases** dual-use capability (authors' finding) — opposite of the safety scaling hope in some LLM work.

### 3.2 Cheaper, faster DNA synthesis

- Oligo and gene synthesis costs have fallen ~**million-fold** since 2000; turnaround days not weeks.
- **Screening chokepoint:** IGSC members screen orders ≥200 bp against Regulated Pathogen Database (RPD) + GenBank; six-frame translation catches some codon optimization. **Gaps:** non-IGSC vendors, international leakage, oligo pools, benchtop synthesizers, sequences **below length threshold**, **novel** sequences with no DB hit, **fragment ordering** across vendors.
- OSTP Framework (2024): mandatory for **federally funded** procurement; 200 bp window now, **50 bp by Oct 2026**. Still voluntary for much private/non-US traffic.

### 3.3 Automated / cloud labs (DBTL closure)

**Design–Build–Test–Learn** loops: AI proposes → robotic synthesis → automated assay → feedback. IAB (Intelligent Automated Biology) tier framework (2025): Level 5 = closed-loop with minimal human oversight — already demonstrated (PLMeAE, iBioFAB). Effect: reduces **iterations**, **expertise**, and **visibility** of suspicious work. RAND expert elicitation (2025): through ~2027 AI remains **assistive**, not autonomous pathogen designer — but it **accelerates** human-driven design and lowers the bar for sophisticated misuse.

**Composite scenario:** actor uses Evo2 to generate candidate sequences → splits orders across vendors / uses sub-200 bp fragments → assembles in BSL-2 garage lab or cloud lab with weak KYC → tests in automated assay without publishing. Screening catches **known** bad sequences; FM helps find **unknown** bad sequences.

---

## 4. Existing policy and governance

| Layer | What it covers | Limits for Evo-class tools |
|-------|----------------|----------------------------|
| **IGSC Harmonized Screening Protocol v3.0** (2024) | Sequence + customer screening for commercial synthesis | Pattern-matching; evasion via optimization, fragmentation, non-member vendors |
| **OSTP Nucleic Acid Synthesis Screening Framework** (Apr 2024; [PDF](https://aspr.hhs.gov/S3/Documents/OSTP-Nucleic-Acid-Synthesis-Screening-Framework-Sep2024.pdf)) | Unified US process; federal funding tied to compliant providers (effective ~Apr 2025) | Does not regulate **model weights** or **in silico** design |
| **NIH DURC / PEPP Policy** (May 2024 policy, effective May 2025) | Federally funded wet-lab work on select agents, RG3/4, gain-of-function categories; institutional review entities | **In silico** FM use generally **outside scope** unless tied to funded experiments on listed agents |
| **BSL-3/4 + Select Agent regulations** | Physical containment, registration for work with listed pathogens | Irrelevant until material exists; doesn't stop sequence design or overseas work |
| **Export controls (Australia Group)** | Sequences that "endow or enhance" pathogenicity | Slow, jurisdiction-specific |
| **Model release decisions** | No binding US rule for biology FM weights | See below |

### AlphaFold3 as parallel (model release, not generation)

DeepMind released AlphaFold3 (May 2024) as **server-only** with pseudocode — no weights. Open letter (>650 signatories) argued this violated reproducibility norms and limited verification ([Science](https://www.science.org/content/article/limits-access-deepmind-s-new-protein-program-trigger-backlash), [Nature editorial](https://www.nature.com/articles/d41586-024-01463-0)). DeepMind later open-sourced **inference code** (Nov 2024) but **weights remain gated** (academic application). Tension: **commercial** drug discovery (Isomorphic Labs) vs **open science** vs **dual-use** (structure of toxins, virulence factors). Evo took the **opposite default**: full open weights from day one — faster science, harder retraction.

### What's missing

- No standard **pre-release red-team** for biology FMs (cf. NIST AI 800-1 for cyber/bio dual-use LLMs — guidance, not law).
- No **output screening** requirement at inference (unlike synthesis screening at build).
- **Function-based** screening (IBBIS Common Mechanism direction) not yet deployed at scale — needed because AI generates **novel** sequences.
- EO 14110 (2023) biosecurity provisions partially **revoked** under Trump admin (Jan 2025); OSTP synthesis framework survived as procurement rule but broader AI-bio EO momentum stalled.

---

## 5. Connection to AI safety work in this repo

Parallel structure to `<!-- private monorepo only -->`:

| LLM safety (your stack) | Biology FM (Evo) |
|-------------------------|------------------|
| Refusal direction ablation → HarmBench ASR ↑ (`code/safety_interventions/`, Qwen7B spec) | GeneBreaker jailbreak → pathogen-homologous DNA ↑ |
| Open weights → attack requires GPU, not API gate | Open weights → same; Evo2-7B runs on single high-end GPU |
| Shallow safety switch vs distributed safety | Screening as **perimeter defense** vs **alignment** of generative prior |
| HarmBench standardized behaviors + classifier | JailbreakDNABench / BIORISKEVAL — **immature but emerging** |
| Persona vectors / evil directions (steerable misalignment) | Semantic design prompts steering toward toxin/virulence regions |
| Mech interp (SAE on Evo layer 26, Goodfire) | **Dual-use interp:** features that light up on virulence motifs are also handles for steering |

**Actionable cross-pollination for your research program:**

1. **Eval methodology:** HarmBench's behavior × attack × classifier pattern maps directly to biology red-teaming (GeneBreaker as "attack suite"). Your factorial intervention grid is the template for testing **inference-time biology safety layers** (output filters, unlearning, steering away from pathogenicity features).
2. **Open-weight policy:** Your Qwen7B work assumes local weight access — same political surface as Evo (see `all_in_ep275` note on open-weight ban rhetoric). Biology FMs make the stakes physical.
3. **Interp as offense and defense:** Evo ships SAE visualizer; Arc/Goodfire treat interpretability as product. Same Arditi-style worry: if virulence is a low-dimensional feature, ablation/steering works both ways.
4. **Not your current codebase, but adjacent experiment:** fine-tune or steer Evo2 away from RPD-homologous outputs; measure ASR on JailbreakDNABench — direct analog of ReFAT/DeepRefusal for DNA.

---

## 6. Open questions and what responsible researchers do

### Open questions

1. **Capability threshold:** At what model scale / training data does generative pathogen design cross from "assistive grad student" to "meaningfully novel threat"? GeneBreaker suggests scale hurts; RAND says autonomous design not before ~2027+ — reconcile.
2. **Screening arms race:** Can function-based screening (AlphaFold fold + binding assay prediction, toxicity predictors) close the gap before FMs outpace it?
3. **Release policy equilibrium:** Is Evo-style full open, AF3-style gated weights, or API-only optimal for social welfare? Who decides?
4. **Lab automation governance:** Should cloud labs require experiment-level prescreening (not just sequence screening)?
5. **International coordination:** IGSC is industry-led, US-centric; synthesis arbitrage to jurisdictions without screening.
6. **Eval standards:** What is the HarmBench equivalent for DNA FMs? BIORISKEVAL and GeneBreaker are starts, not consensus.

### Responsible researcher checklist

- **Before running generative experiments:** check if outputs touch DURC/PEPP categories; institutional biosafety review even for *in silico* work if downstream synthesis is plausible.
- **Before publishing sequences:** run IGSC Common Mechanism or BLAST against RPD; document screening in supplementary materials.
- **Before releasing models:** red-team with pathogen-homology benchmarks; document training exclusions (Evo2 reportedly excluded eukaryotic viral genomes — test whether that holds under fine-tune).
- **Before collaborating with synthesis vendors:** use IGSC-compliant providers only; never split orders to evade screening.
- **Advocacy:** support 50 bp screening adoption, function-based SOC databases, cloud-lab KYC — not "stop all biology AI."

---

## 7. Sources

### Evo / Evo2 primary

- Arc Institute Evo hub: https://arcinstitute.org/tools/evo  
- Evo2 Nature (2026): https://www.nature.com/articles/s41586-026-10176-5  
- Evo1 Science (2024): https://www.science.org/doi/10.1126/science.ado9336  
- GitHub: https://github.com/ArcInstitute/evo2  
- Evo2 one-year update (validated designs): https://arcinstitute.org/news/evo-2-one-year-later  
- NVIDIA technical blog: https://developer.nvidia.com/blog/understanding-the-language-of-lifes-biomolecules-across-evolution-at-a-new-scale-with-evo-2/

### Dual-use / red-teaming

- GeneBreaker (jailbreak Evo): https://arxiv.org/abs/2505.23839 — code https://github.com/zaixizhang/GeneBreaker  
- BIORISKEVAL (Evo2-7B risk eval): https://openreview.net/forum?id=N5DhtpYJ21  
- RAND expert elicitation — AI pathogen design timeline: https://www.rand.org/pubs/research_briefs/RBA4087-1.html  
- IAB / DBTL risk framework: https://pmc.ncbi.nlm.nih.gov/articles/PMC12872745/

### Synthesis screening / biosecurity policy

- IGSC Harmonized Screening Protocol v3.0 (2024): https://genesynthesisconsortium.org/wp-content/uploads/IGSC-Harmonized-Screening-Protocol-v3.0-1.pdf  
- OSTP Framework for Nucleic Acid Synthesis Screening (2024): https://aspr.hhs.gov/S3/Documents/OSTP-Nucleic-Acid-Synthesis-Screening-Framework-Sep2024.pdf  
- Gene synthesis screening hub: https://genesynthesisscreening.centerforhealthsecurity.org/key-policies  
- IBBIS Common Mechanism baseline: https://ibbis.bio/wp-content/uploads/2024/02/Developing-a-Common-Global-Baseline-for-Nucleic-Acid-Synthesis-Screening-IBBIS-Archival.pdf  
- USG DURC/PEPP Policy (2024): https://aspr.hhs.gov/S3/Documents/USG-Policy-for-Oversight-of-DURC-and-PEPP-May2024-508.pdf  
- NIH DURC overview: https://aspr.hhs.gov/S3/Pages/Dual-Use-Research-of-Concern-Oversight-Policy-Framework.aspx

### Model release parallel

- AlphaFold3 access backlash: https://www.science.org/content/article/limits-access-deepmind-s-new-protein-program-trigger-backlash  
- Nature editorial on AF3 code availability: https://www.nature.com/articles/d41586-024-01463-0  
- AF3 code release (Nov 2024): https://www.science.org/content/article/google-deepmind-releases-code-behind-its-most-advanced-protein-prediction-program  
- Open letter (Zenodo): https://zenodo.org/records/11186537

### Internal repo

<!-- private monorepo only: - `[private note]` -->
<!-- private monorepo only: - `[private note]` -->
<!-- private monorepo only: - `[private note]` -->
- `code/safety_interventions/`
