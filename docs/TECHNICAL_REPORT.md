---
title: "A Joint Monte Carlo Model of AI-Driven Civilizational Outcomes, 2026–2050"
author: "Long Yi — Independent Researcher — yilongjack2001@gmail.com"
date: "July 2026"
---

## Abstract

We present `ai-futures-sim`, an open-source joint Monte Carlo simulator that forecasts the distribution of civilizational outcomes attributable to advanced AI development between 2026 and 2050. Unlike scenario-writing approaches that produce a small number of hand-authored narrative branches, or elicitation surveys that report a single scalar probability of catastrophe ("p(doom)"), this model draws thousands of complete, internally consistent world-timelines from a single probabilistic event graph and reports the *emergent* distribution over four outcome regions — doom, utopia, friction, and severe-but-recoverable — as a simulation output rather than a hand-tuned input. The model combines a continuous latent-capability process (an extension of the AI-2027 capability spine) with a 61-node stochastic event graph, 33 continuous state variables, 9 latent correlation clusters, and 17 absorbing terminal states. Probabilities are elicited through structured expert judgment, individually sourced and disclosed, rather than fit to a target distribution. We report calibration results against published capability-timeline forecasts — after two rounds of recalibration, all 7 absolute spine-deadline targets are now met, though a residual conditional-probability gap remains open — a parameter-identifiability analysis showing that three of twenty-two capability-growth parameters still dominate the model's calibration-relevant behavior but that, after two engine-bug fixes uncovered by the analysis itself, zero of the 22 remain structurally inert (down from seven), and the current headline distribution (doom 6.2% ± 0.1%, utopia 20.8% ± 2.3%, friction 66.4% ± 2.5%, severe 6.7% ± 0.4%; three seeds × 400 runs). We discuss the model's limitations candidly, including four classes of engine bugs discovered and fixed during development — two found via the identifiability analysis itself, both dead-code conditions that left growth-relevant parameters silently inert — and the recalibration work each one triggered, sample-size constraints on rare terminal states, and the model's fundamental status as structured judgment rather than a validated predictive instrument.

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

Following AI-2027's plot-beat numbering, milestones are labeled C1–C10, but not all ten are capability thresholds. Seven — internally `sp_c1`…`sp_c9` in `config/spine.yaml` (naming skips to `sp_c9` because C3/C4/C10 are reserved for the non-threshold beats below) — are threshold crossings on the growth curve above: `C1 = 1.14` (≈10²⁸ FLOP-class training), `C2 = 2.15` (Agent-1), `C5 = 5.0` (Agent-2), `C6 = 5.92` (superhuman coder), `C7 = 7.15` (internal "genius country"), `C8 = 8.0` (public AGI-class), `C9 = 9.0` (superhuman AI researcher). The remaining three — C3, C4, C10 — are stochastic **plot events** in the event graph (§3.3) rather than capability-scale thresholds: C3 is a China compute-mobilization event (`ev_china_cdz_mobilization`), C4 is the labor-market shock (`ev_c4_labor_shock`), and C10 is the internal alignment-concern event (`ev_c10_internal_concern`) — each gated on capability tier and other preconditions rather than on `internal_capability` crossing a fixed value. Milestone crossings unlock downstream plot events and set `ci_level`, the discrete capability tier used in event preconditions.

Two macro-couplings run off the same state each day: a GDP-growth process (baseline historical growth rate, accelerated by `tech_level`, dragged by kinetic escalation, governance-capacity deficit, and sovereignty fragmentation — parameters and citations in `docs/CAPABILITY_DYNAMICS.md`), and a human-autonomy erosion/protection process (erosion scaled by `tech_level × deployment_pressure × (1 − alignment_trust)`, offset by protection scaled by `tech_level × governance_capacity` — the model's operationalization of Christiano's "What Failure Looks Like" [2018] gradual-loss-of-control mechanism).

### 3.3 Event Graph and Hazard Model

**61 stochastic plot events** (`config/events.yaml`) extend the AI-2027 plot skeleton across governance, labor, bio-risk, alignment, and geopolitics. Each event has a scheduling window `[start, end]`, a set of preconditions (minimum capability tier, variable-range gates, prerequisite events fired/not-fired, `requires_unlock` gating from other events), and `on_fire` effects (variable deltas, event unlocks/locks, hazard modifiers on other events, or `force_terminal`).

Event probabilities are specified as **window cumulative probability** `p_cumulative` — "P(this event fires at least once during its eligible window)" — not a daily rate. The engine converts this to a constant daily hazard:

```
daily_hazard = 1 − (1 − p_cumulative)^(1 / days_remaining)
```

`days_remaining` here is the event's **total window length**, fixed once from `[start, end]` and reused unchanged on every day the event is checked — not a shrinking countdown recomputed as the deadline approaches. This is a deliberate choice, not an oversight: re-deriving `days_remaining` from the days actually left as the window elapses would push the daily hazard upward each day the event hasn't yet fired, inflating the realized cumulative probability above the elicited `p_cumulative` (`events.py` carries an explicit comment warning against this). The result is a constant-hazard (geometric) process for the life of the window, identical in structure to solving "what per-roll probability makes at least one 6 in N dice rolls hit X%."

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

Each run advances the world state one calendar day at a time from 2026-01-01 to 2050-01-01 (8,766 steps). The per-day update is a five-step sequence with `check_terminals()` interleaved after every state-changing step rather than invoked once at the end (Figure 4): (1) each correlation cluster's latent AR(1) process is stepped forward one day (§3.4); (2) capability growth (§3.2) and continuous couplings are applied; (3) the capability spine is checked, firing at most one milestone, with a terminal check after any milestone fire; (4) up to `max_eligible_checks_per_day = 12` eligible events are ranked by their cluster-adjusted daily hazard and Bernoulli-sampled, capped at `max_fires_per_day = 2` fires — using the same cluster latents stepped in (1), so an event's daily fire probability, and even its eligibility to be sampled at all (the rank-and-truncate cutoff in step 4 is itself cluster-dependent), can shift substantially between the day the latent moves and the day the event is actually rolled (Figure 5); (5) each fired event's effects are applied, with a terminal check after each. A run terminates the instant any terminal check hits; otherwise it is evaluated once more against the horizon-terminal rule list at day 8,766.

![**Figure 4.** The real per-day control-flow order (`engine.py:79-121`), reconstructed from source rather than summarized from memory — an earlier draft of this figure mis-ordered steps 2 and 3 and collapsed the three separate `check_terminals()` call sites into one. Three "Check terminals" diamonds are shown because the function is called from three distinct call sites (after continuous updates, after each spine fire, after each event fire), not because it is a distinct pipeline stage; all three represent the same function and are drawn separately only for legibility. Reproduce: `scripts/generate_mermaid_figures.sh`.](figures/fig4_daily_loop.png)

![**Figure 5.** Expansion of Step 4 (event sampling). The rank-and-truncate step is the mechanism by which cluster correlation (§3.4) affects outcomes beyond simply reweighting a fixed candidate pool: an event boosted by a "hot" cluster can enter the top-12 eligibility cutoff on a day it otherwise would not have, and a suppressed event can drop out of it entirely — a gating effect on top of the probability adjustment itself.](figures/fig5_step4_detail.png)

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
| P(`ev_china_cdz_mobilization`) | ~65% | ✓ on target |
| Spine C-tier deadlines | AI-2027-derived calendar | ✓ on target, all 7 milestones (n=600) |
| Spine conditional P(child\|parent) | AI-2027-derived | ✗ 1 of 5 checks pass |
| Emergent doom region | — (no target; measured) | 6.2% |

This table went through two full recalibration cycles during this report's preparation (§6.3, §9): fixing dead capability-growth parameters repeatedly gave the engine more real growth-pressure than the existing `base_daily_growth`/`calendar_rsi` values were tuned for, pushing absolute spine timing off target each time, which then had to be re-tuned against. The plot-event marginals are on target and were never touched. The *absolute* capability-timing calendar — after landing `base_daily_growth` at `0.00104` (from an original `0.00136`) and re-shaping the late `calendar_rsi` anchors down (2028-10: 8.4→7.5; 2029-01: 11.0→10.5; 2030-06: 50.0→26.0) across two rounds and eight total probe iterations — now **meets all 7 absolute deadline targets at n=600**, a state this project did not have at any earlier point.

The *conditional* progression (given you've reached milestone N, how likely is N+1 by its deadline) tells a different story: only `P(sp_c5|sp_c2)` is on target; the other four are 12–31pp short. This is a real, disclosed trade-off, not an oversight — extensive probing (§9) found that the specific two-knob parameterization available (`base_daily_growth`, a handful of `calendar_rsi` anchor points) cannot simultaneously satisfy both objective sets. Pushing absolute timing onto target tends to slow "already-ahead" runs enough that they can no longer also clear the *next* milestone's deadline on schedule, since `calendar_rsi` is indexed to calendar date, not to how far along a given run's own trajectory already is — a fast-starting run gets throttled by the same calendar-time anchor as a slow one. We settled on the config that maximizes absolute-deadline compliance (7/7) since that was the originally-disclosed, headline-visible gap; the conditional-probability shortfall is the new, now-primary open item (§9).

### 6.2 Terminal Reachability Testing

During development, direct sampling of run-level variable trajectories (rather than trusting that "each terminal's individual condition is independently satisfiable" implies "each terminal is jointly reachable") surfaced two structurally distinct classes of defect, both now fixed and covered by regression tests (`tests/test_terminal_coverage.py`, `tests/test_config_integrity.py`):

1. **Rule-ordering shadowing.** `friction_ghost_gdp_no_transfer`'s condition, though narrower in principle, matched 70–90% of all horizon-assigned runs in practice because it was checked before three narrower, more narratively distinct rules (`friction_modal`, `friction_labor_backlash`, `friction_surveillance`) and one `utopia_golden_age` variant — all of which fired 0/400 times despite being individually satisfiable. Fixed by imposing the most-specific-first ordering documented in §3.5.
2. **Missing continuous mechanism.** As described in §3.1, five state variables that only received discrete event deltas could not accumulate enough movement over a 24-year horizon to cross the variable-range thresholds that several terminals gate on. The most consequential instance: `human_autonomy_index` empirically never fell below ≈0.53 across 800 sampled runs, silently making three of `doom_whimper`'s four horizon-default paths (which require autonomy ≤0.32/0.40/0.48) structurally unreachable and collapsing the model's dominant doom pathway from ~15% of all runs to ~1.5–1.8% with no test catching it — "never observed below 0.53" does not fail a hard-impossibility check the way a literal mathematical bound does. This was caught specifically because a pre-publication sanity check compared a new headline run against a previously published figure and found a 10× discrepancy; it is not clear an equivalent check would have been run absent that specific publication deadline (§8).

A separate, related audit — performed for this report rather than during original development — checked whether any *other* discrete-only variable shared this defect. Five candidates gating terminal conditions (`reskilling_absorption`, `labor_mobilization`, `alignment_trust`, `distribution_regime`, `deception_risk`) were checked against their event deltas; in each case the largest single available delta (0.15–0.45 in magnitude) is large enough to cross the relevant threshold band in one or two event firings, unlike the five variables above, which either had zero non-event mechanism or deltas too small to accumulate meaningfully. No further instance of the defect was found. We report this as a negative result: an explicit search that did not find what it was looking for, not an absence of search.

### 6.3 Sensitivity Analysis and Parameter Identifiability

The capability-growth function (§3.2) has **22 independent scale/exponent constants**; the calibration targets it is checked against (§6.1) number **12** (7 milestone-deadline marginals + 5 spine conditional probabilities). This is an under-identified system: many distinct parameter settings can satisfy the same 12 targets while differing arbitrarily elsewhere, so satisfying calibration does not by itself establish that any individual constant's value is correct, only that the target-relevant *combination* is in a plausible range.

A one-at-a-time sensitivity sweep (±25% perturbation per parameter from its current value, common random numbers across the low/high runs to isolate structural sensitivity from Monte Carlo noise, `n=60`, seed 42) quantifies this. This table is the result of **three successive fixes**, each surfaced by the sweep itself rather than assumed:

1. **Seven `input.*.scale` parameters** originally scored exactly 0.0% because they had no explicit `reference` in `config/capability_dynamics.yaml` and silently inherited a default of 1.0 — but they are all 0–1-bounded indices, clamped to `[0,1]` by every event that touches them, so the growth function's "excess above reference" condition (`max(0, v/reference − 1)`) was not merely small but mathematically guaranteed to be zero for the lifetime of any run. **Fixed 5 of 7** by referencing each variable against its own initial value from `config/variables.yaml`.
2. Of the two still at 0.0% after that: `frontier_lab_polarization` could only ever be *lowered* below its reference by the two events that touch it, so the excess-only gate could never fire. **Fixed** by adding a `symmetric: true` option to `_input_factor()` (only applied to this one input) so consolidation can now dampen growth, not just fail to bonus it — grounded in Aghion, Bloom, Blundell, Griffith & Howitt (2005, *QJE*) on neck-and-neck competitive innovation and Bueno de Mesquita, Dziuda & Polborn (2026, NBER w35276) on AI-lab-specific competition/safety-speed trade-offs. `open_weights_regime` was never touched by any event at all; **fixed** by wiring it into `ev_open_weights_equilibrium`/`ev_open_weights_tamper_response`, using a −0.3 delta that its own evidence doc had already specified but that had never actually been implemented in `events.yaml`.
3. A third, unrelated and unexpected finding: `input.frontier_capex_index.scale` — the *only* `input.*` term that had never been inert, since its driving variable is legitimately clamped to (0.5, 3.0) rather than [0,1] — dropped to exactly 0.0% after the fixes above. Direct sampling (150 runs) found `frontier_capex_index` frozen at *exactly* 1.000 in every single run despite `gdp_index` ranging up to 2.0. Root cause: `engine.py::_drift_variables()` applies a generic exogenous drift to several variables, defaulting to a `[0.0, 1.0]` clamp for anything not explicitly excluded — but `frontier_capex_index` has its own dedicated, correctly-clamped `(0.5, 3.0)` coupling elsewhere (§3.2's GDP-pull mechanism) and was missing from this function's exclusion list (which already excluded `tech_level` and `deployment_pressure` for the identical reason). Every day, the dedicated mechanism's small upward nudge was immediately clamped back down to exactly 1.0 by the generic drift function. **Fixed** by adding `frontier_capex_index` to the exclusion list — confirmed empirically post-fix: 97% of sampled runs now show values above 1.0 (median 1.26).

| Rank | Parameter | Sensitivity score | Interpretation |
|---|---|---|---|
| 1 | `multiplier_exponent` | 138.3% | RSI-multiplier exponent — still the single most load-bearing constant in the model |
| 2 | `carrying_capacity` | 113.3% | Logistic ceiling on `internal_capability`; directly gates how much of the spine is reachable at all |
| 3 | `base_daily_growth` | 101.7% | Linear growth-rate multiplier |
| 4 | `input.deployment_pressure.scale` | 61.7% | Largest of the originally-dead seven, now the fourth-ranked parameter overall |
| 5–20 | 16 further parameters, spanning every remaining `input.*` term | 8.3%–43.3% | Includes `input.frontier_capex_index.scale` (25.0%, recovered from the drift-clamp fix), `input.frontier_lab_polarization.scale` (25.0%, recovered from the symmetric-coupling fix), and `input.open_weights_regime.scale` (18.3%, recovered from the event-wiring fix) — the three most recently-fixed parameters land in the middle of the pack, not at the extremes |

**Zero of the 22 parameters remain structurally inert.** Three still dominate — `multiplier_exponent`, `carrying_capacity`, `base_daily_growth` — but each fix along the way narrowed their relative share of total variance as more of the model's other 19 parameters became live contributors rather than dead weight. This table does not by itself resolve the underlying identifiability problem (22 free parameters against 12 calibration targets is still under-identified, §9), but it does mean every constant in `capability_dynamics.yaml` now has a measurable, non-zero claim to mattering — a citation next to a parameter is no longer potentially attached to code that cannot execute. Full per-parameter results: `outputs/runs/sensitivity_capability.json`; methodology and reproduction command: `docs/CALIBRATION.md`.

![**Figure 1.** Ranked sensitivity of all 22 capability-growth parameters, fully resolved. Three parameters (red) still dominate; every other parameter (blue) now shows real, measurable sensitivity — none remain structurally inert. Reproduce: `python scripts/generate_report_figures.py`.](figures/fig2_sensitivity.png)

### 6.4 Regression Testing

The engine carries 44 automated tests (`pytest`) covering hazard-conversion math, terminal-reachability regressions for the two defect classes in §6.2, config cross-reference integrity (every event ID referenced in a precondition, unlock, or terminal rule must exist), and society-hazard coupling invariants. All 44 pass as of this report.

---

## 7. Results

### 7.1 Headline Region Estimates

| Region | Seed 42 | Seed 123 | Seed 456 | Mean ± range |
|---|---|---|---|---|
| Doom | 6.0% | 6.2% | 6.2% | **6.2% ± 0.1%** |
| Utopia | 22.8% | 18.2% | 21.2% | **20.8% ± 2.3%** |
| Friction | 64.5% | 69.2% | 65.5% | **66.4% ± 2.5%** |
| Severe | 6.8% | 6.2% | 7.0% | **6.7% ± 0.4%** |

These four numbers sum to 100% by construction (every run resolves to exactly one region) and are **measured**, not tuned — no threshold or rule in `terminals.yaml` was adjusted to move this distribution toward a pre-specified target (§6, §8). This is the headline after all four engine-bug fixes (§6.3, §8) and the full spine recalibration (§9): relative to the pre-fix baseline (doom 7.1%, utopia 18.0%, friction 68.5%, severe 6.4%), doom fell 0.9pp and utopia rose 2.8pp, consistent with a slower, better-governed capability trajectory giving institutions more time to catch up. Note the doom estimate's cross-seed spread is now unusually tight (±0.1pp, down from ±1.0–1.1pp at earlier checkpoints today) — a plausible sign of increased model stability once every mechanism was live, though with only 3 seeds this should not be over-read as a precise claim about the true variance.

![**Figure 2.** Emergent outcome-region distribution as a two-level sunburst. Inner ring: the four regions, averaged over 3 seeds × 400 runs (headline figures, matching the table above). Outer ring: the per-terminal breakdown within each region, from the seed-42, n=600 run cited in the "top terminals" text — rescaled onto each region's headline share so both rings sum consistently. Tail terminals below ~2% (e.g. `doom_extinction_bio`, `friction_surveillance`, `friction_pause_stall`, `utopia_symbiosis`) remain visible as unlabeled slivers rather than cluttering the chart with unreadable text. Error bars omitted from the figure; see the table above for the per-seed range.](figures/fig1_regions.png)

### 7.2 Terminal Decomposition

At `n=600` (seed 42, final config), the 17 terminal states decompose as: `friction_managed_non_utopia` 22%, `friction_ghost_gdp_no_transfer` 19%, `utopia_modest_welfare` 14%, `friction_governance_paralysis` 10%, `severe_cyber_cascade` 8%, `utopia_golden_age` 7%, `friction_modal` 6%, `friction_labor_backlash` 6%, `doom_whimper` 4%, with the remaining ~4% distributed across `doom_extinction_misalign`, `friction_pause_stall`, `friction_surveillance`, `utopia_symbiosis`, and `doom_extinction_bio` — several of the latter resting on fewer than 10 occurrences at this sample size (§8). `utopia_radical_abundance`, `doom_extinction_kinetic`, and `friction_unclassified` did not occur in this run.

![**Figure 3.** Branching structure of the joint Monte Carlo from capability gates (2026–28) through governance forks (2028–29) and the alignment-scare branch (2029–31) to the four emergent regions at the 2050 horizon. Ribbon width is share of simulated runs, not an independent scenario weight. Static export of the [interactive web explorer](https://longyi1207.github.io/ai-futures-sim/web/), regenerated after all four engine-bug fixes and the spine recalibration in §6.3/§9; colors follow the region legend embedded in the figure.](figures/fig3_branching.png)

### 7.3 Event Impact Analysis

Defining lift as `Δ_region = P(region | event fired) − P(region | event not fired)` over 1,200 runs (seed 42, final config; baseline 6.1% doom, 20.3% utopia, 67.5% friction, 6.2% severe):

| Event | P(fire) | Δ doom | Δ utopia | Δ friction |
|---|---|---|---|---|
| `ev_fed_edu_reskilling` | 17% | −5.0% | **+50.9%** | −52.8% |
| `ev_deceptive_deploy_at_scale` | 5% | **+45.3%** | −10.6% | −33.6% |
| `ev_swf_enacted` | 5% | −1.1% | **+47.1%** | −44.7% |
| `ev_prod_interp_halt` | 12% | −6.1% | **+28.7%** | −25.8% |
| `ev_deploy_incident` | 2% | **+18.5%** | −10.2% | −12.6% |
| `ev_no_shutdown_asi_threshold` | 28% | **+11.7%** | −6.0% | −4.5% |
| `ev_c10_internal_concern` | 31% | **+11.3%** | −6.8% | −5.8% |
| `ev_whistle_dump` | 6% | **+7.8%** | −5.6% | −1.9% |

`ev_align_prod_catch` (production-scale alignment interpretability catch, not shown above — a narrower-firing event) is the single largest utopia lever by lift magnitude (+65.1pp), with `ev_fed_edu_reskilling` (a successful *federal*, not state-level, reskilling program) close behind and firing far more often (17% vs. a few percent). **This table reports association, not a causal effect estimate.** Because events share latent correlation-cluster membership (§3.4), a large lift is consistent with either "this event causes the shift" or "this event is disproportionately likely to co-occur with other events already driving the trajectory toward that region" — the joint simulator's correlation structure means these are not separable from the lift statistic alone.

### 7.4 Illustrative Trajectory

A single sampled run (seed 42, run #17, terminal `friction_labor_backlash`) illustrates a distributional, not control-loss, pathway to friction: the C4 labor shock fires 2028-03-10, organized labor mobilization follows 2030-05-07, and federal reskilling formally fails to absorb the shock 2031-06-20 — while `human_autonomy_index` remains high (0.98) throughout, distinguishing this run's mechanism from the autonomy-erosion pathway that dominates `doom_whimper`. Three further worked trajectories, covering managed-distribution friction, alignment-scare-plus-war doom, and an institutional-plus-interpretability utopia path, are presented at day-level resolution in the companion blog post's "Four story paths" section, which this report does not duplicate.

---

## 8. Limitations

We list these in roughly descending order of how much they should discount confidence in the headline numbers.

**This is structured judgment, not a validated predictive model.** There is no track record of resolved predictions behind these percentages, no Brier score, and no forecasting-tournament calibration. The four headline percentages should be read as a defensible, falsifiable starting point for argument about specific cruxes — not as a number carrying a statistical confidence interval in the sense a calibrated forecaster's track record would earn.

**The capability engine is under-identified (§6.3).** Twenty-two free parameters against twelve calibration targets means most individual constants are not independently pinned down by the calibration procedure. The first run of the identifiability analysis found seven of the 22 completely inert (zero measured effect regardless of value); three successive bug fixes during this report's preparation brought that to zero, and each fix triggered a further round of capability-timing recalibration (§6.1, §9). All 22 now show measurable, non-zero sensitivity, but the underlying identifiability gap — many different parameter combinations can satisfy the same 12 calibration targets — is not resolved by this work, only better characterized.

**The correlation structure (§3.4) is elicited, not fit.** Cluster memberships and hazard-sensitivity coefficients are structured judgment about which events *should* co-move and by roughly how much; no joint-occurrence dataset exists to fit or validate this structure against, because the events in question (civilizational-scale AI outcomes) have not occurred.

**Rare terminal states are sample-size-limited.** Terminals below ~1% prevalence (`doom_extinction_bio`, `utopia_radical_abundance`) rest on single-digit occurrence counts at `n=600`; these should be read as order-of-magnitude estimates, not two-significant-figure percentages, and would benefit from dedicated high-`n` runs before being cited individually.

**Event-impact lift (§7.3) understates its own causal ambiguity.** The correlation structure that makes the joint simulation more realistic also means the standard "association is not causation" caveat applies more strongly than usual: shared latent drivers across correlated events mean a large lift plausibly reflects selection into already-doom-leaning or already-utopia-leaning trajectories rather than a marginal causal contribution from the event itself.

**Four classes of engine defect were found and fixed during development, not before initial construction.** Two are terminal-reachability defects (§6.2): the most consequential — a missing continuous mechanism on `human_autonomy_index` — silently suppressed the model's dominant doom pathway by roughly 10× for an unknown period, and was caught by a pre-publication sanity check against a previously published number rather than by the test suite. The other two (§6.3) were both found via this report's own identifiability analysis: a dead-code `reference` default that made seven capability-growth parameters structurally inert regardless of their `scale` value, and — discovered only after fixing that one, when a previously-healthy parameter unexpectedly went inert — a wrong-clamp bug in a generic exogenous-drift function that had silently frozen `frontier_capex_index` at exactly 1.000 in every sampled run for an unknown period, canceling its own dedicated growth mechanism entirely. We disclose all four rather than treat the corrected numbers as though no such history existed, because a reader evaluating this model's trustworthiness should know that internal consistency checks alone did not catch any of them, and a routine test suite pass is not sufficient evidence that no further instance exists (§6.2's negative-result audit addresses specific hypotheses, not an exhaustive search) — the fourth defect specifically was only found because fixing the third one changed the sensitivity ranking enough to make its absence conspicuous, which is itself a reason to expect more low-visibility instances could still exist.

**The spine-timing/conditional-probability trade-off (§6.1) is the current open item, not fully resolved.** After two full recalibration cycles, all 7 absolute spine-deadline targets are met at n=600 — a genuine improvement from every earlier checkpoint in this model's history — but only 1 of 5 conditional-progression targets (P(next milestone | reached previous one) by its own deadline) is met. Extensive probing (§9) suggests this is a real structural tension given the current two-knob parameterization (`base_daily_growth`, `calendar_rsi` anchors), not something a slightly different combination would resolve — bringing conditional probabilities into line would likely require either more anchor points, a capability-progress-indexed rather than purely calendar-indexed RSI curve, or accepting a different absolute-vs-conditional trade-off point than the one currently chosen.

**Author expertise is uneven across domains.** Bio/CBRN-related probability judgments in particular were constructed from public-source synthesis (IGSC, WMDP, ScreenDNA, congressional testimony) rather than domain expertise, and are explicitly flagged as the weakest-sourced category in the underlying evidence pages.

---

## 9. Discussion and Future Work

The most direct way to strengthen this work's evidentiary standing would be **external elicitation**: replacing or supplementing single-analyst structured judgment with a small panel of domain-diverse forecasters using the same claim/evidence/falsifier template, which would convert several currently unaddressable disagreements (is 0.88 the right number, or should it be 0.75?) into a measurable inter-rater spread.

A second direction, largely completed during this report's preparation but with one open piece remaining, was **recalibrating `base_daily_growth` and the calendar-RSI anchors** against the AI-2027 target dates. Each of the three bug fixes in §6.3 gave previously-dead or previously-frozen parameters real (net-growth-positive) effect, which pushed absolute capability timing further from target each time — the growth rate that was tuned against an engine with those parameters inert was no longer the right growth rate once they went live. Two full recalibration rounds (eight probe iterations total, `base_daily_growth` moved from `0.00136` to `0.00104`, the late `calendar_rsi` anchors reshaped downward) brought all 7 absolute spine-deadline targets back on target at n=600 — the best calibration state this project has had. What remains: only 1 of 5 conditional-progression targets is met (§6.1, §8), and the probing done so far suggests this is a genuine structural limit of the current two-knob parameterization rather than a slightly-better combination waiting to be found. Closing that gap properly likely needs either a richer `calendar_rsi` curve (more anchor points, allowing independent control of absolute pace vs. cascade speed) or a fundamentally different mechanism — e.g. indexing part of the RSI multiplier to a run's own capability progress rather than purely to calendar date, so a fast-starting run isn't throttled by the same time-indexed anchor as a slow one.

A third is **empirical grounding for the correlation structure** (§3.4, §8) — even an approximate joint-occurrence dataset from adjacent domains (technology-adoption shock co-occurrence, historical governance-crisis clustering) would let cluster correlation and hazard-sensitivity values move from elicited judgment toward something checkable.

Finally, this model would benefit from a **standing prediction log**: converting the "would update if" falsifiers already attached to every major crux (§4) into dated, timestamped predictions that can later be scored, which is the only way this kind of work eventually earns the calibration credibility that a Metaculus-style track record confers and that §8 explicitly notes this model currently lacks.

---

## 10. Conclusion

`ai-futures-sim` demonstrates that a joint (rather than branch-mixture) Monte Carlo architecture can produce a four-region outcome distribution as an emergent measurement rather than a hand-tuned input, while keeping every constituent probability individually sourced, disclosed, and falsifiable. The model's current headline distribution — doom 6.2%, utopia 20.8%, friction 66.4%, severe 6.7% — should be read in the context of this report's §8 in full: as one analyst's structured, falsifiable, and repeatedly self-audited judgment about a domain with no historical dataset to check it against, built on an engine whose capability-growth core is demonstrably under-identified and whose correlation structure is elicited rather than empirically fit. The identifiability work documented in §6.3 is itself an illustration of the point: closing one honest gap repeatedly surfaced the next one — a dead parameter revealed a second dead parameter, fixing that revealed a third parameter's clamp bug, and each fix required its own recalibration pass — which is the expected shape of this kind of work, not a failure of it. The model now has zero structurally inert growth parameters and meets all 7 absolute spine-deadline targets, a materially stronger state than when this identifiability investigation began; a real conditional-probability gap remains open and is reported as such, not smoothed over. We consider the value of this project to lie less in the specific percentages and more in making the assumptions that produce them individually inspectable, individually arguable, and individually falsifiable — and in disclosing, rather than quietly correcting, the engine defects found along the way.

---

## References

Kokotajlo, D., Alexander, S., Larsen, T., Lifland, E., & Song, R. (2025). *AI 2027*. [ai-2027.com](https://ai-2027.com/)

Christiano, P. (2018). *What Failure Looks Like*. [ai-alignment.com](https://ai-alignment.com/what-failure-looks-like-b6e7d8096fc8)

Acemoglu, D., & Johnson, S. (2023). *Power and Progress: Our Thousand-Year Struggle Over Technology and Prosperity*. PublicAffairs.

Aghion, P., Jones, B. F., & Jones, C. I. (2017). *Artificial Intelligence and Economic Growth*. NBER Working Paper 23928.

Aghion, P., Bloom, N., Blundell, R., Griffith, R., & Howitt, P. (2005). *Competition and Innovation: An Inverted-U Relationship*. Quarterly Journal of Economics, 120(2), 701–728.

Bueno de Mesquita, E., Dziuda, W., & Polborn, M. (2026). *[Working paper on AI competition, speed, and safety investment]*. NBER Working Paper 35276.

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
