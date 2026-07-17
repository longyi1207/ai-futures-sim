---
title: "A Joint Monte Carlo Model of AI-Driven Civilizational Outcomes, 2026–2050"
author: "Longyi"
date: "July 2026"
---

## Abstract

We present `ai-futures-sim`, an open-source joint Monte Carlo simulator that forecasts the distribution of civilizational outcomes attributable to advanced AI development between 2026 and 2050. Unlike scenario-writing approaches that produce a small number of hand-authored narrative branches, or elicitation surveys that report a single scalar probability of catastrophe ("p(doom)"), this model draws thousands of complete, internally consistent world-timelines from a single probabilistic event graph and reports the *emergent* distribution over four outcome regions — doom, utopia, friction, and severe-but-recoverable — as a simulation output rather than a hand-tuned input. The model combines a continuous latent-capability process (an extension of the AI-2027 capability spine) with a 61-node stochastic event graph, 33 continuous state variables, 9 latent correlation clusters, and 17 absorbing terminal states. Probabilities are elicited through structured expert judgment, individually sourced and disclosed, rather than fit to a target distribution. We report calibration results against published capability-timeline forecasts, a parameter-identifiability analysis showing that three of twenty-two capability-growth parameters account for nearly all of the model's calibration-relevant behavior, and the current headline distribution (doom 7.1% ± 1.0%, utopia 18.0% ± 0.8%, friction 68.5% ± 0.8%, severe 6.4% ± 0.6%; three seeds × 400 runs). We discuss the model's limitations candidly, including two classes of engine bugs discovered and fixed during development, sample-size constraints on rare terminal states, and the model's fundamental status as structured judgment rather than a validated predictive instrument.

---

## 1. Introduction

Public discourse on AI existential risk is dominated by two incompatible formats. The first is the scalar "p(doom)" — a single probability, frequently asserted without a visible model, that compresses years of disagreement about definitions, time horizons, and causal chains into one number that cannot be interrogated. The second is scenario narrative — exemplified by *AI 2027* [Kokotajlo et al., 2025] — which is far more legible about its assumptions but typically presents a small, fixed number of mutually exclusive branches (e.g., "slowdown" vs. "race"), which understates the true joint uncertainty: bio-risk, misalignment, and governance failure are not mutually exclusive story arcs that a civilization picks one of, but co-occurring processes whose interaction is itself part of what determines the outcome.

`ai-futures-sim` is an attempt to combine the transparency of scenario modeling with the statistical honesty of Monte Carlo simulation. Every run draws **one coherent joint timeline** — capability growth, governance response, labor-market disruption, bio-risk, and geopolitical shocks all evolve together, coupled through shared state variables and latent correlation structure, exactly as they would in a single real future. Aggregating thousands of such runs yields an *emergent* distribution over outcome regions, rather than a distribution the modeler chose in advance and then justified.

This report documents the model's architecture, elicitation methodology, calibration procedure, and — at comparable length — its limitations. The companion artifact is a narrative blog post at [longyi.blog/writing/my-ai-futures-forecast](https://longyi.blog/writing/my-ai-futures-forecast), which presents the same model through worked story-path examples and is the better entry point for a reader who wants intuition before formalism. This report is written for a reader who wants the formalism first: the state space, the hazard model, the validation procedure, and an honest accounting of where the model's evidentiary support is strong and where it is thin.

**Source and reproducibility.** The full engine, configuration, per-event evidence pages, and this report's source are at [github.com/longyi1207/ai-futures-sim](https://github.com/longyi1207/ai-futures-sim) (MIT license). Every reported number in this document is reproducible from the commands in Appendix C.

---

## 2. Related Work

**Scenario forecasting.** *AI 2027* [Kokotajlo, Alexander, Larsen, Lifland & Song, 2025] is the direct structural ancestor of this model's capability spine (§3.2) and roughly half of its event graph — this project extends its plot skeleton with a joint (rather than branch-mixture) execution model and adds society-level feedback (labor, distribution, autonomy) that AI 2027's narrative treatment does not formalize into state variables.

**Structured expert elicitation.** The probability-elicitation methodology (§4) follows the general pattern of IPCC-style expert elicitation and Delphi-method structured judgment: no claim to statistical estimation from data where no dataset exists, but a discipline of making the *claim*, *evidence*, and *falsification condition* explicit and public for every probability, so that disagreement can be localized to a specific, arguable number rather than an unstated intuition.

**Forecasting platforms and aggregation.** Metaculus and comparable prediction-aggregation platforms produce well-calibrated forecasts for questions with enough independent forecasters and enough resolved history to compute a Brier score. This model has neither — it is a single analyst's structured judgment, not a calibrated forecasting-tournament output, and we flag this distinction explicitly rather than borrow forecasting-platform credibility by association (§8).

**Published p(doom) elicitations.** Public estimates from researchers and lab leadership range from <0.1% to >95% [Yudkowsky, Hanson, Hinton, Bengio, Amodei, et al. — full list and citations in the companion blog post's "What others say" table]. The spread is overwhelmingly attributable to differing definitions and time horizons rather than a single latent disagreement, which is itself part of the motivation for this model's explicit four-region taxonomy (§3.5) in place of a single scalar.

---

## 3. Model Architecture

### 3.1 State Space

The world state is a vector of **33 continuous variables** (`config/variables.yaml`) spanning five domains: capability (`internal_capability`, `ci_level`, `tech_level`, `ai_rd_multiplier`), economy (`gdp_index`, `employment_stress`, `ghost_gdp_index`, `inequality_index`, `distribution_regime`, `reskilling_absorption`), governance and trust (`governance_capacity`, `alignment_trust`, `deception_risk`, `human_autonomy_index`, `international_coord`), bio-risk (`bio_capability_tier`, `bio_governance_tier`, `bio_risk_pressure`), and geopolitics (`china_frontier_parity`, `us_china_race_index`, `sovereignty_fragmentation`, `kinetic_escalation`, `compute_concentration`, and seven more). Full glossary: `docs/VARIABLES.md`.

Variables are updated through two mechanisms that the model treats as structurally distinct:

- **Discrete deltas**, applied when a scheduled event fires (`on_fire.add_vars` / `set_vars` in `config/events.yaml`) — the natural representation for one-off political or technical events (a bill passing, a treaty signing).
- **Continuous daily coupling**, applied every simulated day as a function of other state variables (§3.2) — the natural representation for slow structural processes (capital concentrating, trust eroding, GDP compounding) that no single discrete event fully captures.

A methodologically important finding from this project's development (§6.2, §8) is that variables driven *only* by discrete deltas are prone to a specific failure mode: if no event's delta is individually large enough, or frequent enough, to move the variable into a terminal-defining threshold band over a 24-year horizon, the corresponding terminal state becomes empirically — sometimes mathematically — unreachable, regardless of how "correct" each individual event probability is. Five variables (`gdp_index`, `employment_stress`, `ghost_gdp_index`, `inequality_index`, `human_autonomy_index`) were found to have exactly this defect during development and were given continuous coupling mechanisms; §6.2 documents the diagnostic process and §8 discusses what auditing was and was not done to rule out further instances.

### 3.2 Capability Dynamics

Latent capability `internal_capability` follows a bounded logistic-growth process:

```
ΔC(t) = base_growth · multiplier(t)^exponent · f(state(t)) · (1 − C(t)/K) · growth_scale
```

where `base_growth` is a base daily growth rate, `multiplier(t)` is an R&D-acceleration multiplier (capped at 55×, driven by a piecewise-linear "calendar RSI" curve anchored to AI-2027's plot timeline plus a capability-triggered internal recursive-self-improvement term), `exponent` is the power on that multiplier, `K = 11.0` is a logistic carrying capacity, `growth_scale` is a global capability-growth scale, and `f(state(t))` is a composite multiplicative factor built from 15 further terms — race dynamics (deployment pressure vs. governance capacity), a governance/salience brake, a trust–governance interaction, a "secret race" boost under low trust, an international-coordination brake, sovereignty-fragmentation drag, administration posture, kinetic-escalation drag, and bio-capability spillover. In total, **22 independent scale/exponent constants** parameterize `f` and the outer growth equation; §6.3 reports a sensitivity analysis of this parameter set.

Seven capability milestones (`sp_c1`…`sp_c9`, skipping c3/c4/c10, which are plot events rather than capability tiers) are threshold crossings on this scale: `C1 = 1.14` (≈10²⁸ FLOP-class training), `C2 = 2.15` (Agent-1), `C5 = 5.0` (Agent-2), `C6 = 5.92` (superhuman coder), `C7 = 7.15` (internal "genius country"), `C8 = 8.0` (public AGI-class), `C9 = 9.0` (superhuman AI researcher). Milestone crossings unlock downstream plot events and set `ci_level`, the discrete capability tier used in event preconditions.

Two macro-couplings run off the same state each day: a GDP-growth process (baseline historical growth rate, accelerated by `tech_level`, dragged by kinetic escalation, governance-capacity deficit, and sovereignty fragmentation — parameters and citations in `docs/CAPABILITY_DYNAMICS.md`), and a human-autonomy erosion/protection process (erosion scaled by `tech_level × deployment_pressure × (1 − alignment_trust)`, offset by protection scaled by `tech_level × governance_capacity` — the model's operationalization of Christiano's "What Failure Looks Like" [2018] gradual-loss-of-control mechanism).

### 3.3 Event Graph and Hazard Model

**61 stochastic plot events** (`config/events.yaml`) extend the AI-2027 plot skeleton across governance, labor, bio-risk, alignment, and geopolitics. Each event has a scheduling window `[start, end]`, a set of preconditions (minimum capability tier, variable-range gates, prerequisite events fired/not-fired, `requires_unlock` gating from other events), and `on_fire` effects (variable deltas, event unlocks/locks, hazard modifiers on other events, or `force_terminal`).

Event probabilities are specified as **window cumulative probability** `p_cumulative` — "P(this event fires at least once during its eligible window)" — not a daily rate. The engine converts this to a constant daily hazard for the event's remaining eligible days:

```
daily_hazard = 1 − (1 − p_cumulative)^(1 / days_remaining)
```

Each simulated day, up to `max_eligible_checks_per_day = 12` eligible events are sampled against their current daily hazard, and up to `max_fires_per_day = 2` are allowed to actually fire (a combinatorial-explosion control, documented in `docs/PROBABILITY_MODEL.md`). The capability spine has its own independent daily draw, capped at one spine milestone per day.

**Elicitation uncertainty propagation.** Rather than treating each event's `p_cumulative` as a fixed point estimate, each run independently samples every event's cumulative probability from `Beta(p · κ, (1 − p) · κ)` with concentration `κ = 80` (≈5.5 percentage points of standard deviation at `p = 0.5`, calibrated to a "medium confidence" elicitation rating) before converting to a daily hazard. This means the reported outcome distribution already incorporates first-order uncertainty in the probability *elicitations themselves*, not only the stochastic realization of a fixed-probability process.

### 3.4 Correlation Structure

Sixty-one nominally independent event hazards would understate real joint-tail risk: in the real world, an acceleration shock, a governance failure, and a bio-risk near-miss are not independent draws — they share upstream drivers (a weak administration, a compute breakthrough, a geopolitical crisis). The model captures this through **9 latent AR(1) cluster processes** (`config/correlations.yaml`, informally labeled A–H in the underlying research notes, with one merged cluster) — race/acceleration, bio-governance, bio-tail, alignment-governance transparency, an internal-alignment-signal cluster, compute-chokepoint, US governance-capacity/corporate-hollowing, sovereignty, and actor-geopolitics. Each cluster is a latent Gaussian process with daily persistence `φ = 0.98`; an event's daily hazard is multiplied by `exp(Σ hazard_sensitivity_c · z_c)` summed over every cluster the event belongs to, where `z_c` is the cluster's current latent value and `hazard_sensitivity_c` its coupling strength (0.15–0.22 across clusters). This is a **calibration-free correlation structure** in the specific sense that its cluster memberships and correlation/sensitivity values are elicited, not fit to any joint-occurrence dataset — no such dataset exists for civilizational-scale AI scenarios. We treat this as an honest approximation of directional co-movement rather than a quantitatively validated covariance structure (§8).

### 3.5 Terminal Classification

**17 absorbing terminal states**, grouped into four regions (doom, utopia, friction, severe), are checked in two ways: `event_forced` terminals fire immediately when a specific extinction-class event occurs (e.g., `ev_extinction_bio_release → doom_extinction_bio`); all other terminals are `horizon_only`, meaning they are evaluated once, at the 2050 horizon, against the world state accumulated over the full run.

Horizon evaluation uses a **first-match-wins ordered rule list** (`terminals.yaml::horizon_default`), checked doom → utopia → friction, and — critically — from most-specific to least-specific *within* each region, so that a broad, easily-satisfied rule cannot silently pre-empt a narrower, more narratively distinct one before it is ever checked. §6.2 documents a case where this ordering property was violated and one terminal shadowed three others for an unknown period of development.

---

## 4. Probability Elicitation Methodology

No historical dataset exists for "federal AI training pause," "AGI-class public deployment," or "Tier-2 biological near-miss disclosure rate." Every probability in the model is therefore **structured expert judgment**, not statistical estimation, and not a black-box model output. Each of the ~313 individual probability judgments in the crux registry, and each of the 61 event `p_cumulative` values, is documented against a fixed six-field template:

| Field | Content |
|---|---|
| Claim | The exact, falsifiable question the probability answers |
| Why | The reasoning that produced this magnitude |
| Evidence | Public sources — bills, papers, lab statements, historical base rates |
| Analogue | A historical reference class, where the AI-specific case has no data of its own |
| Would update if | An observable condition that would change the estimate, stated in advance |
| Confidence | High / Medium / Low |

Every constant in the continuous-mechanism layer (§3.2's growth couplings, the autonomy-erosion and GDP-growth parameters) is labeled inline in `config/capability_dynamics.yaml` as either sourced from a specific citation or explicitly `[GUESS]` — a deliberate convention to prevent a cited-but-arbitrarily-scaled constant from reading as more evidentially grounded than it is.

A worked example, chosen because it is the single highest-leverage judgment in the model (a ±25% perturbation to this crux moves more downstream mass than any other single probability): **P(no binding federal training pause through 2028) = 0.88** (range 0.83–0.93). This rests on four independent lines of evidence — a 99–1 Senate vote against a training-pause amendment (2025), the empirical base rate that the 2023 OpenAI board crisis did not stop training at a frontier lab under acute internal pressure, a conditional chain (P(whistleblower response is oversight, not halt) ≈ 0.58, further conditioned on P(halt | sustained corporate crisis > 30 days) ≈ 0.12), and an explicit coalition-strength argument (the economic and national-security coalition favoring continued training is broader and better organized than the pause coalition across all four modeled administration-posture scenarios). Full sourcing: `docs/evidence/ev_no_pause_2028.md`.

A researcher who disagrees with a headline region percentage is directed not to argue with the percentage, but to identify one load-bearing probability judgment, apply the same four-step challenge (definition correctness → evidentiary support for the magnitude → analogue fairness → observable falsifiability), edit the corresponding YAML value, and re-run the simulation.

---

## 5. Simulation Procedure

Each run advances the world state one calendar day at a time from 2026-01-01 to 2050-01-01 (8,766 steps). Per day: (1) the capability-spine hazard is drawn (at most one milestone fires); (2) up to 12 eligible events are checked against their correlation-adjusted daily hazard, at most 2 of which are allowed to fire; (3) continuous couplings (§3.2) are applied unconditionally; (4) `event_forced` terminals are checked. A run terminates early on a forced terminal, or otherwise is evaluated once against the horizon-terminal rule list at day 8,766.

Aggregating `N` runs (typically 400–2,000 per seed; 10,000 for high-precision headline estimates) over the resulting terminal labels produces the emergent region distribution. All reported multi-seed statistics in this document use 3 independent seeds (42, 123, 456) at 400 runs each, with the spread across seeds reported as an empirical range rather than a parametric confidence interval.

Runtime on a single Apple-silicon core: ~15–20s at `N=100`, ~3min at `N=600`, ~60–85min at `N=10,000` (pure Python, no compiled extensions).

---

## 6. Calibration and Validation

We distinguish two categories of quantity throughout this section, following the discipline documented in `docs/CALIBRATION.md`: **calibration targets** — quantities with an independent external target the model is checked against (spine milestone-by-deadline probabilities, core plot-event marginals) — and **emergent measurements** — quantities the model produces with no target to tune toward (the four headline region percentages, terminal composition, event-impact lift). Tuning a horizon-terminal rule, a variable threshold, or a mechanism's functional form to move an emergent measurement toward a desired value is treated as a methodological violation in this project (see §8's discussion of one instance where this discipline was nearly, then explicitly not, broken).

### 6.1 Cross-Check Against AI 2027

| Check | Target | Status |
|---|---|---|
| P(`ev_no_pause_2028`) | ~88% | ✓ on target |
| P(`ev_bmia_pass`) | ~45% | ✓ on target |
| P(`ev_us_paralysis_s2`) | ~55% | ✓ on target |
| Spine C-tier deadlines | AI-2027-derived calendar | ✗ off in 2 of 3 seed checks |
| Emergent doom region | — (no target; measured) | 7.1% |

The plot-event marginals — the quantities that carry the model's actual crux content — are on target. The capability-timing calendar (how quickly the spine crosses its milestones relative to the AI-2027-derived target dates) is not: C1- and C6-adjacent milestones fire somewhat faster than the target calendar in the majority of seed checks. We publish with this miss disclosed rather than delaying release for an open-ended internal-consistency pass; §6.3 shows the same underlying parameter set is under-identified in a way that plausibly explains this drift, and identifies which parameters would need to move to close it.

### 6.2 Terminal Reachability Testing

During development, direct sampling of run-level variable trajectories (rather than trusting that "each terminal's individual condition is independently satisfiable" implies "each terminal is jointly reachable") surfaced two structurally distinct classes of defect, both now fixed and covered by regression tests (`tests/test_terminal_coverage.py`, `tests/test_config_integrity.py`):

1. **Rule-ordering shadowing.** `friction_ghost_gdp_no_transfer`'s condition, though narrower in principle, matched 70–90% of all horizon-assigned runs in practice because it was checked before three narrower, more narratively distinct rules (`friction_modal`, `friction_labor_backlash`, `friction_surveillance`) and one `utopia_golden_age` variant — all of which fired 0/400 times despite being individually satisfiable. Fixed by imposing the most-specific-first ordering documented in §3.5.
2. **Missing continuous mechanism.** As described in §3.1, five state variables that only received discrete event deltas could not accumulate enough movement over a 24-year horizon to cross the variable-range thresholds that several terminals gate on. The most consequential instance: `human_autonomy_index` empirically never fell below ≈0.53 across 800 sampled runs, silently making three of `doom_whimper`'s four horizon-default paths (which require autonomy ≤0.32/0.40/0.48) structurally unreachable and collapsing the model's dominant doom pathway from ~15% of all runs to ~1.5–1.8% with no test catching it — "never observed below 0.53" does not fail a hard-impossibility check the way a literal mathematical bound does. This was caught specifically because a pre-publication sanity check compared a new headline run against a previously published figure and found a 10× discrepancy; it is not clear an equivalent check would have been run absent that specific publication deadline (§8).

A separate, related audit — performed for this report rather than during original development — checked whether any *other* discrete-only variable shared this defect. Five candidates gating terminal conditions (`reskilling_absorption`, `labor_mobilization`, `alignment_trust`, `distribution_regime`, `deception_risk`) were checked against their event deltas; in each case the largest single available delta (0.15–0.45 in magnitude) is large enough to cross the relevant threshold band in one or two event firings, unlike the five variables above, which either had zero non-event mechanism or deltas too small to accumulate meaningfully. No further instance of the defect was found. We report this as a negative result: an explicit search that did not find what it was looking for, not an absence of search.

### 6.3 Sensitivity Analysis and Parameter Identifiability

The capability-growth function (§3.2) has **22 independent scale/exponent constants**; the calibration targets it is checked against (§6.1) number **12** (7 milestone-deadline marginals + 5 spine conditional probabilities). This is an under-identified system: many distinct parameter settings can satisfy the same 12 targets while differing arbitrarily elsewhere, so satisfying calibration does not by itself establish that any individual constant's value is correct, only that the target-relevant *combination* is in a plausible range.

A one-at-a-time sensitivity sweep (±25% perturbation per parameter from its current value, common random numbers across the low/high runs to isolate structural sensitivity from Monte Carlo noise, `n=60`, seed 42) quantifies this:

| Rank | Parameter | Sensitivity score | Interpretation |
|---|---|---|---|
| 1 | `multiplier_exponent` | 161.7% | RSI-multiplier exponent (multiplier capped at 55×) — the single most load-bearing constant in the model; a ±25% swing alone moves `sp_c9_by_deadline` by 50 percentage points |
| 2 | `carrying_capacity` | 98.3% | Logistic ceiling on `internal_capability`; directly gates how much of the spine is reachable at all |
| 3 | `base_daily_growth` | 95.0% | Linear growth-rate multiplier; moves `sp_c5_by_deadline` by 78 percentage points |
| 4–14 | (11 further parameters) | 8.3%–23.3% | Governance/coordination/fragmentation brakes, kinetic and bio-spillover terms |
| 15 | `input.frontier_capex_index.scale` | 1.7% | |
| 16–22 | Seven `input.*.scale` terms | **0.0% (all seven)** | Structurally inert under the trajectories this model samples — see below |

Three parameters — `multiplier_exponent`, `carrying_capacity`, `base_daily_growth` — account for the overwhelming majority of the model's response to every calibration target measured. Everything else is comparatively cheap to get wrong. More pointedly: seven of the twenty-two parameters (the `input.*.scale` terms gating on `deployment_pressure`, `china_frontier_parity`, `us_china_race_index`, `compute_concentration`, `eu_regulatory_bind`, `open_weights_regime`, and `frontier_lab_polarization`) score **exactly 0.0% sensitivity** — not merely small, but structurally inert, because `_input_factor()` computes `1 + scale · max(0, v/reference − 1)`, and the driving variables stay close enough to their reference values across the trajectories this configuration actually samples that the excess term never activates. Each of these seven carries an inline evidentiary citation in `config/capability_dynamics.yaml`; the sensitivity result shows that citation is not currently doing the epistemic work a citation is supposed to do, since the parameter it justifies has zero measured effect on any model output. This does not resolve the identifiability problem — it only localizes where the slack is — but it does mean that any claim of the form "this specific constant is well-supported because it cites paper X" should be read alongside this table before being trusted. Full per-parameter results: `outputs/runs/sensitivity_capability.json`; methodology and reproduction command: `docs/CALIBRATION.md`.

### 6.4 Regression Testing

The engine carries 44 automated tests (`pytest`) covering hazard-conversion math, terminal-reachability regressions for the two defect classes in §6.2, config cross-reference integrity (every event ID referenced in a precondition, unlock, or terminal rule must exist), and society-hazard coupling invariants. All 44 pass as of this report.

---

## 7. Results

### 7.1 Headline Region Estimates

| Region | Seed 42 | Seed 123 | Seed 456 | Mean ± range |
|---|---|---|---|---|
| Doom | 6.2% | 6.8% | 8.2% | **7.1% ± 1.0%** |
| Utopia | 18.8% | 18.0% | 17.2% | **18.0% ± 0.8%** |
| Friction | 69.2% | 68.5% | 67.8% | **68.5% ± 0.8%** |
| Severe | 5.8% | 6.8% | 6.8% | **6.4% ± 0.6%** |

These four numbers sum to 100% by construction (every run resolves to exactly one region) and are **measured**, not tuned — no threshold or rule in `terminals.yaml` was adjusted to move this distribution toward a pre-specified target (§6, §8).

### 7.2 Terminal Decomposition

At `n=600` (seed 42), the 17 terminal states decompose as: `friction_managed_non_utopia` 21%, `friction_ghost_gdp_no_transfer` 20%, `utopia_modest_welfare` 12%, `friction_governance_paralysis` 11%, `friction_labor_backlash` 9%, `utopia_golden_age` 6%, `severe_cyber_cascade` 6%, `doom_whimper` 5%, with the remaining ~10% distributed across `utopia_symbiosis`, `doom_extinction_misalign`, `friction_surveillance`, `friction_pause_stall`, `doom_extinction_bio`, and `utopia_radical_abundance` — several of the latter resting on fewer than 15 occurrences at this sample size (§8).

### 7.3 Event Impact Analysis

Defining lift as `Δ_region = P(region | event fired) − P(region | event not fired)` over 1,200 runs (seed 42; baseline 6.8% doom, 18.8% utopia, 68.8% friction, 5.6% severe):

| Event | P(fire) | Δ doom | Δ utopia | Δ friction |
|---|---|---|---|---|
| `ev_fed_edu_reskilling` | 15% | −1.9% | **+43.3%** | −43.6% |
| `ev_deploy_incident` | 2% | **+37.2%** | −18.8% | −12.8% |
| `ev_deceptive_deploy_at_scale` | 7% | **+30.7%** | −11.2% | −18.8% |
| `ev_prod_interp_halt` | 11% | −5.3% | **+24.6%** | −20.0% |
| `ev_swf_enacted` | 5% | +1.6% | **+23.6%** | −29.8% |
| `ev_whistle_dump` | 6% | **+14.3%** | −3.3% | −9.7% |
| `ev_no_shutdown_asi_threshold` | 30% | **+9.9%** | −3.4% | −4.3% |
| `ev_c10_internal_concern` | 32% | **+7.1%** | −4.8% | −2.3% |

`ev_fed_edu_reskilling` (a successful *federal*, not state-level, reskilling program) is the single largest utopia lever in the graph. **This table reports association, not a causal effect estimate.** Because events share latent correlation-cluster membership (§3.4), a large lift is consistent with either "this event causes the shift" or "this event is disproportionately likely to co-occur with other events already driving the trajectory toward that region" — the joint simulator's correlation structure means these are not separable from the lift statistic alone.

### 7.4 Illustrative Trajectory

A single sampled run (seed 42, run #17, terminal `friction_labor_backlash`) illustrates a distributional, not control-loss, pathway to friction: the C4 labor shock fires 2028-03-10, organized labor mobilization follows 2030-05-07, and federal reskilling formally fails to absorb the shock 2031-06-20 — while `human_autonomy_index` remains high (0.98) throughout, distinguishing this run's mechanism from the autonomy-erosion pathway that dominates `doom_whimper`. Three further worked trajectories, covering managed-distribution friction, alignment-scare-plus-war doom, and an institutional-plus-interpretability utopia path, are presented at day-level resolution in the companion blog post's "Four story paths" section, which this report does not duplicate.

---

## 8. Limitations

We list these in roughly descending order of how much they should discount confidence in the headline numbers.

**This is structured judgment, not a validated predictive model.** There is no track record of resolved predictions behind these percentages, no Brier score, and no forecasting-tournament calibration. The four headline percentages should be read as a defensible, falsifiable starting point for argument about specific cruxes — not as a number carrying a statistical confidence interval in the sense a calibrated forecaster's track record would earn.

**The capability engine is under-identified (§6.3).** Twenty-two free parameters against twelve calibration targets means most individual constants are not independently pinned down by the calibration procedure, and seven currently have zero measured effect on any tracked output despite carrying evidentiary citations.

**The correlation structure (§3.4) is elicited, not fit.** Cluster memberships and hazard-sensitivity coefficients are structured judgment about which events *should* co-move and by roughly how much; no joint-occurrence dataset exists to fit or validate this structure against, because the events in question (civilizational-scale AI outcomes) have not occurred.

**Rare terminal states are sample-size-limited.** Terminals below ~1% prevalence (`doom_extinction_bio`, `utopia_radical_abundance`) rest on single-digit occurrence counts at `n=600`; these should be read as order-of-magnitude estimates, not two-significant-figure percentages, and would benefit from dedicated high-`n` runs before being cited individually.

**Event-impact lift (§7.3) understates its own causal ambiguity.** The correlation structure that makes the joint simulation more realistic also means the standard "association is not causation" caveat applies more strongly than usual: shared latent drivers across correlated events mean a large lift plausibly reflects selection into already-doom-leaning or already-utopia-leaning trajectories rather than a marginal causal contribution from the event itself.

**Two classes of engine defect were found and fixed during development, not before initial construction (§6.2).** The most consequential — a missing continuous mechanism on `human_autonomy_index` — silently suppressed the model's dominant doom pathway by roughly 10× for an unknown period, and was caught by a pre-publication sanity check against a previously published number rather than by the test suite. We disclose this rather than treat the corrected numbers as though no such history existed, because a reader evaluating this model's trustworthiness should know that internal consistency checks alone did not catch this class of error and a routine test suite pass is not sufficient evidence that no further instance exists (§6.2's negative-result audit addresses one specific hypothesis, not an exhaustive one).

**The spine-timing miss (§6.1) is open.** Capability milestones cross somewhat faster than the AI-2027-derived target calendar in most seed checks; §6.3 identifies the three parameters most likely responsible but does not resolve which of them should move, by how much, or on what evidentiary basis.

**Author expertise is uneven across domains.** Bio/CBRN-related probability judgments in particular were constructed from public-source synthesis (IGSC, WMDP, ScreenDNA, congressional testimony) rather than domain expertise, and are explicitly flagged as the weakest-sourced category in the underlying evidence pages.

---

## 9. Discussion and Future Work

The most direct way to strengthen this work's evidentiary standing would be **external elicitation**: replacing or supplementing single-analyst structured judgment with a small panel of domain-diverse forecasters using the same claim/evidence/falsifier template, which would convert several currently unaddressable disagreements (is 0.88 the right number, or should it be 0.75?) into a measurable inter-rater spread.

A second direction is **reducing the identifiable/inert parameter gap** found in §6.3 — either by folding the seven currently-inert `input.*.scale` terms into fewer, better-constrained couplings, or by adding calibration targets (e.g., published capability-growth-rate estimates with their own uncertainty bands) that would give those seven parameters something to respond to.

A third is **empirical grounding for the correlation structure** (§3.4, §8) — even an approximate joint-occurrence dataset from adjacent domains (technology-adoption shock co-occurrence, historical governance-crisis clustering) would let cluster correlation and hazard-sensitivity values move from elicited judgment toward something checkable.

Finally, this model would benefit from a **standing prediction log**: converting the "would update if" falsifiers already attached to every major crux (§4) into dated, timestamped predictions that can later be scored, which is the only way this kind of work eventually earns the calibration credibility that a Metaculus-style track record confers and that §8 explicitly notes this model currently lacks.

---

## 10. Conclusion

`ai-futures-sim` demonstrates that a joint (rather than branch-mixture) Monte Carlo architecture can produce a four-region outcome distribution as an emergent measurement rather than a hand-tuned input, while keeping every constituent probability individually sourced, disclosed, and falsifiable. The model's current headline distribution — doom 7.1%, utopia 18.0%, friction 68.5%, severe 6.4% — should be read in the context of this report's §8 in full: as one analyst's structured, falsifiable, and partially self-audited judgment about a domain with no historical dataset to check it against, built on an engine whose capability-growth core is demonstrably under-identified and whose correlation structure is elicited rather than empirically fit. We consider the value of this project to lie less in the specific percentages and more in making the assumptions that produce them individually inspectable, individually arguable, and individually falsifiable — and in disclosing, rather than quietly correcting, the engine defects found along the way.

---

## References

Kokotajlo, D., Alexander, S., Larsen, T., Lifland, E., & Song, R. (2025). *AI 2027*. [ai-2027.com](https://ai-2027.com/)

Christiano, P. (2018). *What Failure Looks Like*. [ai-alignment.com](https://ai-alignment.com/what-failure-looks-like-b6e7d8096fc8)

Acemoglu, D., & Johnson, S. (2023). *Power and Progress: Our Thousand-Year Struggle Over Technology and Prosperity*. PublicAffairs.

Aghion, P., Jones, B. F., & Jones, C. I. (2017). *Artificial Intelligence and Economic Growth*. NBER Working Paper 23928.

Davidson, T. (2021). *Could Advanced AI Drive Explosive Economic Growth?* Open Philanthropy.

Erdil, E., & Besiroglu, T. (2023). *Explosive Growth from AI Automation: A Review of the Arguments*. Epoch AI. arXiv:2309.11690.

Jorgenson, D. W., Ho, M. S., & Stiroh, K. J. Growth-accounting literature on the 1995–2004 US productivity surge.

IMF (2023). *Geoeconomic Fragmentation and the Future of Multilateralism*. Staff Discussion Note SDN/2023/001.

Bloomberg Economics (2024, updated 2026). *The $10 Trillion Fight: Modeling a US-China War Over Taiwan*.

Miller, C. (2022). *Chip War: The Fight for the World's Most Critical Technology*. Scribner.

Kaufmann, D., & Kraay, A. World Bank Worldwide Governance Indicators.

Full citation list with per-claim linkage: companion blog post, Appendix E, and `docs/evidence/*.md` throughout this repository.

---

## Appendix A — State Variable Glossary (Selected)

| Variable | Domain | Update mechanism |
|---|---|---|
| `internal_capability` | Capability | Continuous (§3.2 growth equation) |
| `gdp_index` | Economy | Continuous (compounding growth coupling) |
| `employment_stress` | Economy | Continuous (stock-flow, capability-gated) |
| `human_autonomy_index` | Governance/trust | Continuous (erosion/protection coupling) |
| `distribution_regime` | Economy | Discrete (event deltas only) |
| `reskilling_absorption` | Economy | Discrete (event deltas only) |
| `governance_capacity` | Governance/trust | Continuous (partial — admin-posture coupling) |
| `alignment_trust` | Governance/trust | Discrete (event deltas only) |
| `deception_risk` | Governance/trust | Mixed (conditional continuous drift + discrete) |
| `kinetic_escalation` | Geopolitics | Continuous (exponential decay to floor) |

Full glossary of all 33 variables: `docs/VARIABLES.md`.

## Appendix B — Terminal Taxonomy

| Region | Terminal | Mechanism |
|---|---|---|
| Doom | `doom_extinction_bio` | Bio-release event forced |
| Doom | `doom_extinction_misalign` | Deceptive deployment + no shutdown, forced |
| Doom | `doom_extinction_kinetic` | Taiwan kinetic + WMD escalation, forced |
| Doom | `doom_whimper` | Horizon: autonomy collapse without a single extinction trigger |
| Utopia | `utopia_radical_abundance` | Horizon: sustained real growth + longevity/space breakthrough |
| Utopia | `utopia_symbiosis` | Horizon: high alignment trust + high autonomy + production-scale interpretability catch |
| Utopia | `utopia_golden_age` | Horizon: institutional strength + a legible technical/policy win |
| Utopia | `utopia_modest_welfare` | Horizon: distribution/reskilling policy lands at a "good enough" level |
| Friction | `friction_managed_non_utopia` | Horizon: real but partial distribution policy |
| Friction | `friction_ghost_gdp_no_transfer` | Horizon: GDP growth without transfer |
| Friction | `friction_governance_paralysis` | Federal gridlock mid-capability-ladder |
| Friction | `friction_labor_backlash` | Organized labor response, reskilling formally failed |
| Friction | `friction_modal` | Horizon: acceleration + inequality, no distribution policy |
| Friction | `friction_surveillance` | Horizon: concentrated power + weak governance + reduced autonomy |
| Friction | `friction_pause_stall` | Federal pause enacted, capability plateaus |
| Friction | `friction_unclassified` | Residual catch-all (§6.2 — should be near-zero after the ordering fix) |
| Severe | `severe_cyber_cascade` | Recoverable systemic shock, forced |

Full conditions for each terminal: `config/terminals.yaml`.

## Appendix C — Reproducibility

```bash
git clone https://github.com/longyi1207/ai-futures-sim.git
cd ai-futures-sim
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

pytest -q                                              # 44 tests, ~2 min

python scripts/calibration_check.py -n 600 --seed 42 \
  --output outputs/runs/calibration_summary.json       # §6.1, §7.1

python scripts/seed_sweep.py -n 400 --seeds 42 123 456 \
  --output outputs/runs/seed_sweep.json                # §7.1 three-seed table

python scripts/event_impact.py -n 1200 --seed 42 \
  --output web/data/event_impact.json                  # §7.3

python scripts/sensitivity_capability.py -n 200 --seed 42 \
  --output outputs/runs/sensitivity_capability.json     # §6.3, ~25-45 min
```

Default seed: 42. Requires Python ≥ 3.11. Full environment and CLI reference: `README.md`, `docs/TRY_IT.md`.
