# Changelog

## 2026-07-17 (cont. 5) — spine recalibration round 2 (final); identifiability investigation closed

Following the `frontier_capex_index` fix below, which sped growth up again, re-ran the same
iterative recalibration process (3 more `n=200` probes on top of round 1's 5).

- **Final config:** `base_daily_growth` 0.00110→**0.00104**; `calendar_rsi` 2030-06-01 anchor
  32.0→**26.0** (2028-10 and 2029-01 anchors unchanged from round 1).
- **Result** (n=600 confirmation): **7/7 absolute spine-deadline targets pass** — the best
  calibration state this project has had. Only 1/5 conditional targets pass (`P(sp_c5|sp_c2)`),
  down from round 1's 2/5. This is a disclosed trade-off, not an oversight: probing found the
  absolute/conditional tension is structural given the current 2-knob parameterization, not
  something a better probe would resolve — see `docs/CALIBRATION.md`.
- **Final headline** (n=400×3 seeds): doom **6.2% ± 0.1%**, utopia **20.8% ± 2.3%**, friction
  **66.4% ± 2.5%**, severe **6.7% ± 0.4%** — vs. this morning's pre-fix baseline of
  7.1%/18.0%/68.5%/6.4%.
- **Identifiability investigation closed:** started today with 7 of 22 capability-growth
  parameters completely inert; ends with **zero** inert, all 22 showing measurable sensitivity.
  Full test suite (44 tests) green throughout every step.

## 2026-07-17 (cont. 4) — `frontier_capex_index` drift-clamp bug found and fixed

Unexpected finding while re-running the sensitivity sweep after the previous fix:
`input.frontier_capex_index.scale` — the one `input.*` term that had never been inert — dropped
to exactly 0.0%. Direct sampling (150 isolated runs) found `frontier_capex_index` frozen at
*exactly* 1.000 in 100% of runs, despite `gdp_index` ranging up to 2.0 in the same sample.

- **Root cause:** `engine.py::_drift_variables()` applies a generic daily drift to several
  variables with a default `clamp=(0.0, 1.0)` for anything not explicitly excluded.
  `tech_level`/`deployment_pressure` were already excluded because they have dedicated,
  differently-clamped mechanisms elsewhere — `frontier_capex_index` has the identical
  situation (`gdp_capex_coupling`, correctly clamped to `(0.5, 3.0)`) but was missing from the
  exclusion list, so its own mechanism's small upward nudge was clamped back to exactly 1.0
  every single day.
- **Fix:** added `frontier_capex_index` to the exclusion set (`engine.py`).
- **Result:** post-fix, 97% of 150 sampled runs show values above 1.0 (median 1.26, max 1.71).
  Sensitivity: 0.0%→25.0%.
- Full test suite green. This is the fourth engine-defect class found this session, and the
  second found purely because fixing a previous bug made an unrelated parameter's absence of
  effect newly conspicuous.

## 2026-07-17 (cont. 3) — spine recalibration round 1

The reference-value fix (below) and the `frontier_lab_polarization`/`open_weights_regime` fix
(below) both gave previously-dead parameters real growth-accelerating effect, pushing spine
timing further from the AI-2027 targets each time. Iteratively recalibrated
`base_daily_growth` and the late `calendar_rsi` anchors against `scripts/calibration_check.py`
(5 `n=200` probes, `n=600` confirmation).

- **Config:** `base_daily_growth` 0.00136→0.00110; `calendar_rsi` late anchors
  2028-10: 8.4→7.5, 2029-01: 11.0→10.5, 2030-06: 50.0→32.0.
- **Result:** 5/7 absolute deadline targets pass (sp_c8/sp_c9 ~10-12pp over); 2/5 conditional
  targets pass (`P(sp_c5|sp_c2)`, `P(sp_c7|sp_c6)`). Best balance found across 5 probes between
  absolute-deadline compliance and conditional-progression compliance, which trade off against
  each other given the available parameterization — see `docs/CALIBRATION.md`.
- Superseded by round 2 (above) after the `frontier_capex_index` fix required further
  recalibration.

## 2026-07-17 (cont. 2) — `frontier_lab_polarization` and `open_weights_regime` fixed (evidence-grounded, not guessed)

The 2 of 7 dead `input.*.scale` parameters the previous fix couldn't reach needed different,
research-backed fixes rather than another reference-value tweak.

- **`open_weights_regime`:** no event touched it at all. Found that
  `ev_open_weights_equilibrium`/`ev_open_weights_tamper_response` were the thematically-correct
  pair but only moved `bio_risk_pressure`/`china_open_weight_strategy` (a distinct variable).
  The tamper-response event's own evidence doc already specified an `open_weights_regime: -0.3`
  delta in its YAML-mapping table — researched but never implemented. Wired both events in:
  `ev_open_weights_equilibrium` +0.20 `[GUESS]`, `ev_open_weights_tamper_response` -0.3
  (pre-existing documented figure).
- **`frontier_lab_polarization`:** the only two events touching it both lowered it below
  reference, so the excess-only gate could never fire. Researched the market-structure/
  innovation-speed relationship rather than guessing a fix: Aghion, Bloom, Blundell, Griffith &
  Howitt (2005, *QJE*) on neck-and-neck competitive innovation, and Bueno de Mesquita, Dziuda &
  Polborn (2026, NBER w35276) on AI-lab-specific competition/safety-speed trade-offs — both
  support a genuinely two-sided relationship. Added `symmetric: true` to `_input_factor()`
  (`capability.py`), applied only to this one input, removing the `max(0, ...)` floor so
  consolidation can now dampen growth. `scale` magnitude (0.08) left unchanged — citations
  support direction and functional form, not a number.
- **Result** (n=60 sweep): `frontier_lab_polarization` 0.0%→31.7%, `open_weights_regime`
  0.0%→18.3%–20.0% (varies slightly by run). All tests pass.
- Consequence: sped growth up again, requiring the recalibration in "cont. 3" above.

## 2026-07-17 — dead `input.*.scale` parameters fixed; headline moved, spine-timing miss sharpened

Found while writing up the technical report's parameter-identifiability section: seven
of `_growth_factor()`'s 22 capability-growth parameters (the `input.*.scale` terms
gating on `deployment_pressure`, `china_frontier_parity`, `us_china_race_index`,
`compute_concentration`, `eu_regulatory_bind`, `open_weights_regime`,
`frontier_lab_polarization`) scored exactly 0.0% sensitivity in the OAT sweep. Traced
the cause: none had an explicit `reference` in `capability_dynamics.yaml`, so
`_input_factor()` fell back to its default of 1.0 -- but all seven are 0-1-bounded
indices, and every event delta touching them (`config/events.yaml`) carries
`clamp: [0, 1]`. `max(0, val/1.0 - 1)` was not "empirically near zero" but
mathematically guaranteed to be exactly zero for the lifetime of any run.

- **Fix** (`config/capability_dynamics.yaml`): gave each of the seven an explicit
  `reference` equal to its own initial value from `config/variables.yaml`
  (already-elicited numbers, not new judgment calls) instead of an unreachable
  constant.
- **Result** (`n=60` OAT sweep, seed 42): 5 of 7 now show real sensitivity
  (`deployment_pressure` 20.0%, `china_frontier_parity`/`eu_regulatory_bind` 18.3%,
  `compute_concentration`/`us_china_race_index` 13.3%). The remaining 2 are inert for
  distinct, now-diagnosed reasons: `open_weights_regime` is never touched by any event
  (frozen at its initial value regardless of `reference`); `frontier_lab_polarization`
  is only ever `set_vars` *below* its initial value by the two events that touch it, so
  it can fall from reference but never exceed it -- the "excess above baseline" gate
  can't fire either direction that matters. Top-3 dominant-parameter scores dropped
  (`multiplier_exponent` 161.7%->121.7%, `carrying_capacity` 98.3%->71.7%,
  `base_daily_growth` 95.0%->70.0%) since variance now has more places to go.
- **Headline moved**: 3-seed re-run (n=400 each) gives doom 8.1% (+1.0pp), utopia 16.2%
  (-1.8pp), friction 68.6% (+0.1pp), severe 7.1% (+0.7pp) vs. the previous
  7.1/18.0/68.5/6.4.
- **Side effect, not incidental**: giving 5 net-growth-positive terms real effect for
  the first time pushed absolute capability timing further from the AI-2027-derived
  calendar -- `sp_c5_by_deadline` moved from ~80-90% to ~90-95% against a 65% target,
  and every milestone deadline check now fails (previously most, not all). Read as
  evidence that `base_daily_growth`/`calendar_rsi` need a fresh calibration pass against
  an engine where these terms are live, not the one they were tuned against -- that
  recalibration is **not** done as part of this fix, and is now the more pressing open
  item (`docs/CALIBRATION.md`, `docs/TECHNICAL_REPORT.md` §9).
- Full test suite (44 tests) green throughout. `scripts/generate_report_figures.py`
  updated to color sensitivity-chart bars by measured score rather than a hardcoded
  parameter-name list, so this class of staleness can't recur silently.

## 2026-07-16 (cont. 7) — human_autonomy_index coupling; doom_whimper recovered

Found while preparing a 3-seed headline re-run for blog publication: the new
headline (doom ~3.3%, down from the published ~17%) looked suspicious on its own,
so before publishing it the terminal composition was checked against the old post's
own numbers. The published blog states `doom_whimper` was ~15% of all runs (the
dominant doom pathway); the new run showed 1.5-1.8% — a 10x collapse.

Root cause: same missing-continuous-mechanism bug as gdp_index/inequality_index/
employment_stress, this time on `human_autonomy_index`. It only ever moved via
discrete event deltas and empirically never dropped below ~0.53 across 800 runs.
3 of `doom_whimper`'s 4 horizon_default paths require autonomy <=0.32/0.40/0.48 --
structurally unreachable the same way `friction_surveillance`'s autonomy band was
before today's other fixes (see "cont. 5"), just not caught yet because "never
observed below 0.53" doesn't fail a mathematical-impossibility check the way
gdp_index<1.45 did.

- Added `autonomy_erosion` to `capability_dynamics.yaml`/`capability.py` --
  continuous erosion scaled by `tech_level * deployment_pressure * (1 -
  alignment_trust)`, offset by continuous protection scaled by `tech_level *
  governance_capacity`. Mechanism grounded in Christiano's "What Failure Looks
  Like" (2018) -- gradual loss of human oversight as deployment outpaces
  trustworthy alignment, which the blog post already cites as its reference case
  for the friction/whimper modal path but which the model couldn't actually
  produce a mechanism for. `[GUESS]` on magnitude.
- **Result** (n=800, seed=42): `doom_whimper` 1.5-1.8% -> **4.9%**;
  `friction_surveillance` 0.1% -> **1.2%** (same autonomy-band fix helps both).
  `human_autonomy_index` can now reach 0.000 in the worst scenarios (previously
  floor ~0.53). Region mix: doom 7.1%, severe 5.9%, friction 67.8%, utopia 19.2%.
- Full test suite (44 tests) green. This was caught specifically *because* the
  headline number was being prepared for public publication and got a sanity
  check against the previously-published figures before going out -- the kind of
  check that doesn't happen for routine internal dev runs.

## 2026-07-16 (cont. 6) — verified economics citations via web search

All citations added in this session's capability_dynamics.yaml comments were
written from training-data memory, not verified live — owner asked for them to be
checked before this work gets published. Searched each; most held up, two needed
correction:

- **Confirmed accurate as stated**: Aghion/Jones/Jones NBER w23928 (2017); IMF SDN
  "Geoeconomic Fragmentation" (2023, 7% GDP-loss upper bound); Bloomberg Economics
  Taiwan conflict cost (~$10T/~10% global GDP — found an updated Feb 2026 Bloomberg
  figure too, $10.6T/~9.6%, plus regional breakdown showing South Korea/Japan/Taiwan
  hit far harder than the global average); Chris Miller *Chip War* (TSMC ~90% of
  most-advanced chips); IMF WEO April 2022 Russia-Ukraine spillover (-0.8pp global
  growth, matches the "-0.5 to -1pp" range cited); US/global real GDP baseline
  (~2.1-2.8%/yr recent BEA data, matches the 2.2% used).
- **Corrected — understated**: Jorgenson/Stiroh's actual finding is that IT
  accounted for ~47-60% of US productivity growth 1995-2003, not a standalone
  "+0.5-1.0pp" as the original comment said — translated against that era's ~2.5-3%
  productivity growth, the real implied figure is ~+1.2-1.8pp. `tech_level_accel_scale`
  (1.2pp) wasn't changed — it now sits at the low end of the corrected range instead
  of above the original (wrong) range.
- **Corrected — overstated confidence**: Davidson (2021) was cited as a
  "central-to-high" explosive-growth estimate; Davidson's own paper assigns only
  ~10% probability to explosive growth (>30%/yr) occurring *by 2100* — an explicit
  tail scenario in the source's own framing, not a central case.
- **Corrected — number wasn't actually sourced from the cited papers**:
  `governance_collapse_drag_scale` (-2pp at governance_capacity=0) was written as if
  read off Kaufmann-Kraay-Mastruzzi / Acemoglu-Robinson — both are real, well-
  established frameworks (confirmed the causal channel from governance quality to
  economic outcomes is real), but neither has a clean quotable growth-rate
  coefficient at this scale. Re-labeled as `[GUESS]` on magnitude, citations kept
  only for the qualitative channel they establish.
- `config/capability_dynamics.yaml` comments updated in place with corrected
  language and verification notes. No parameter *values* changed — this pass was
  about citation accuracy, not re-tuning. Full test suite (44 tests) green.

## 2026-07-16 (cont. 5) — real missing mechanisms: circular precondition bug, inequality coupling, kinetic decay

Follow-up to owner asking for a content audit ("what does the model actually still
lack") rather than a process critique — three items investigated and fixed, not
reverse-engineered from a target:

- **Fixed a genuine logic bug, not a calibration issue**: `ev_c4_labor_shock`'s
  precondition required `employment_stress` already in `[0.25, 1.0]` — but the
  event's own `on_fire` effect is what's supposed to *cause* employment_stress
  (+0.22), and nothing else could raise it that high before this event fires
  (the continuous coupling only activates at capability>=4.0, reached ~2029, after
  this event's own 2026-2028 window closes; its two downstream events both
  `requires_unlock` from it). This was a **logical impossibility**: 0/800 fires
  before the fix. Removed the circular precondition, kept `spine_fired: [sp_c2]`.
  Result: `ev_c4_labor_shock` now fires 474/800 (59%); the entire downstream
  labor-mobilization/reskilling-failure chain is unblocked;
  `friction_labor_backlash` went from structurally-0 to **61/800 (7.6%)**.
  Updated `tests/test_society_hazards.py::test_c4_requires_employment_stress`,
  which had encoded the buggy behavior as the expected/correct behavior.
- **`inequality_index` had the same missing-coupling bug `gdp_index` originally
  had**: only discrete event deltas, empirical ceiling ~0.62 across 800 runs —
  could never represent genuinely high concentration. Added the same stock-flow
  treatment as `employment_stress`/`ghost_gdp_index` (continuous concentration
  inflow, offset by `distribution_regime`) — grounded in the same research finding
  already cited for `ghost_gdp_index` (`node_u2_distribution_evidence_rationale.md`,
  "P=0.73 — top decile captures ≥60% of AI-attributed surplus", explicitly a
  continuous process). Correlation with `distribution_regime` now -0.480 (mechanism
  responds correctly to policy); saturates in 75.5% of runs (no policy response is
  common, mirroring employment_stress) — not further tuned down.
  `friction_surveillance` moved from structurally-impossible (inequality could
  never reach its 0.60 gate) to 1/800 — now genuinely rare rather than impossible;
  the remaining binding constraint is `human_autonomy_index`'s narrow [0.25,0.58]
  band (only ~2.9% of runs land there), which reads as legitimate rarity, not a bug.
- **`kinetic_escalation` had no decay** — once any kinetic event fired, tension
  stayed at peak for the rest of the run (up to 20+ years), permanently dragging
  capability and GDP growth. Added exponential relaxation toward a 0.08 residual
  floor (~6yr half-life, `[GUESS]` on rate — no real precedent for "AI-era
  great-power tension half-life" specifically), grounded in the standard reference
  case that great-power tension historically cycles rather than ratchets
  (Cold War thaw/re-freeze pattern).
- Full test suite (44 tests) green throughout.

## 2026-07-16 (cont. 4) — closed the friction_unclassified gap (13.6%→~0%)

Follow-up to inspecting real `friction_unclassified` sample runs (owner asked to
"take a deeper look" at what they actually contained). Traced to
`friction_managed_non_utopia`'s `human_autonomy_index` upper bound: `human_autonomy_index`
turns out to be driven entirely by discrete event deltas (no continuous drift), so
it clusters at ~15 distinct sums (0.53 to 1.00) rather than varying smoothly.

- Widened the bound 0.85→0.92 first (caught 109/800→16/800), then a second batch
  clustered at exactly 0.96 revealed the same bug recurring one cluster up — a
  finite ceiling just relocates *which* cluster falls through next, it doesn't fix
  the underlying issue.
- **Removed the upper bound entirely** rather than keep chasing clusters:
  `friction_managed_non_utopia` doesn't need `human_autonomy_index` to do any
  discriminating work — utopia rules are checked earlier in `horizon_default` and
  already claim genuinely-flourishing runs via their own (stricter)
  `distribution_regime`/`reskilling_absorption` thresholds.
- **Result** (n=800, seed=42): `friction_unclassified` dropped out of the top-12
  terminals entirely (was 13.6%); `friction_managed_non_utopia` absorbed nearly all
  of it, rising from 7.6%→21.1%. Region-level mix unchanged (both terminals are
  `friction` region) — this was a narrative-taxonomy fix, not an outcome-distribution
  fix.
- Full test suite (44 tests) green.

## 2026-07-16 (cont. 3) — employment_stress / ghost_gdp_index stock-flow fix

Follow-up to a self-audit (owner asked "what other gdp-style mistakes are there") that
found `employment_stress` and `ghost_gdp_index` saturated at exactly 1.0 in 84% of runs
(n=500) regardless of outcome — a one-way ratchet (continuous inflow via
`employment_coupling`, only one-off event deltas as counterweight) with no evidence/
citation grounding for the rates, same unexamined-parameter pattern as the original
gdp_index bug, just not caught by a terminal-reachability test since nothing was
mathematically *impossible* here — the variables just carried no discriminating
information.

- **`capability.py`**: both variables now net continuous inflow against continuous
  *outflow* scaled by the policy variables the event graph already moves
  (`reskilling_absorption` for `employment_stress`, `distribution_regime` for
  `ghost_gdp_index`) — a stock-flow model instead of a ratchet. `[GUESS]` on
  magnitude (`daily_stress_absorption_scale`, `daily_ghost_gdp_absorption_scale` in
  `capability_dynamics.yaml`): sized so "policy succeeded" levels (~0.55-0.58)
  roughly cancel inflow, baseline (~0.20, no policy) still saturates over the
  remaining simulation.
- **Result** (n=500, seed=42): `employment_stress` saturation 84%→67%,
  correlation with `reskilling_absorption` now **-0.731**; `ghost_gdp_index`
  saturation 83%→48%, correlation with `distribution_regime` now **-0.579**. Both
  variables now genuinely respond to whether labor/distribution policy succeeded,
  which is the structural fix — the remaining ~67% employment_stress saturation was
  *not* further tuned down: only ~22% of runs get any reskilling policy response at
  all (`ev_fed_edu_reskilling`'s p_cumulative), so a majority still hitting high
  stress over 20+ years of unaddressed displacement reads as a plausible outcome
  of that fact, not an artifact to chase toward a nicer-looking number.
- Full test suite (44 tests) green.

## 2026-07-16 (cont. 2) — regression mechanisms: capability_drop, sustained GDP drag

Follow-up to the previous entry's "not fixed this pass" flag on realism gaps: neither
`internal_capability` nor `gdp_index` could organically decline, and kinetic
escalation / governance collapse / sovereignty fragmentation never touched GDP
growth at all.

- **`effects.py`**: new `capability_controls.capability_drop` — absolute one-time
  reduction to `internal_capability` (physical infrastructure destruction, not just
  a growth slowdown). Deliberately does not touch `ci_level` (public
  observed-milestone tracker) — already-achieved milestones don't un-happen.
- **`ev_taiwan_kinetic`**: added `capability_drop: 0.5`, grounded in Taiwan/TSMC's
  real dominance of leading-edge chip fabrication (Chris Miller, *Chip War*, 2022).
- **`gdp_growth_coupling`**: added three *sustained* drag terms (subtracted from the
  annual rate for as long as the state stays bad, not a one-time hit) —
  `kinetic_drag_scale` (0.10, i.e. -10pp/yr at kinetic_escalation=1.0; IMF WEO
  Russia-Ukraine spillover + Bloomberg Economics 2024 Taiwan-conflict-cost
  estimates), `governance_collapse_drag_scale` (0.02; Kaufmann-Kraay-Mastruzzi /
  Acemoglu-Robinson institutional-quality-growth literature),
  `fragmentation_drag_scale` (0.012; IMF SDN "Geoeconomic Fragmentation", 2023).
- **Empirical check** (n=800, seed=42): the 6 runs where `ev_taiwan_kinetic` fired
  now show gdp_index p50=0.465 vs 1.349 for the other 794 — a real, lasting scar
  instead of a one-day dip. `internal_capability`, however, fully regrows to the
  11.0 ceiling in all 6 — read as a coherent emergent story (war devastates the
  civilian economy but doesn't stop the capability race, echoing wartime R&D
  acceleration analogues) rather than a bug, and left as-is pending owner input.
- Full test suite (44 tests) green. Full rationale in `docs/CAPABILITY_DYNAMICS.md`
  "Sustained drag" and "Capability regression" sections.

## 2026-07-16 (cont.) — real-data gdp growth, missing-mechanism event, threshold recalibration

Follow-up to the same-day terminal-reachability fix below, after the owner asked
where the gdp growth rate actually came from (correctly — it was reverse-engineered
to hit a target) and asked for the model to be checked against real-world realism.

- **`gdp_growth_coupling` rebuilt as compounding, not additive.** `gdp_index` is a
  level index and should compound like real GDP. New rate =
  `baseline_annual_growth` (2.2%/yr — BEA/World Bank long-run real GDP growth) +
  `tech_level_accel_scale` (1.2pp/yr at full deployment — anchored on IT-diffusion
  TFP-contribution estimates, Jorgenson/Stiroh-style, deliberately far below the
  "AI explosive growth" literature's 20-30%+/yr central estimates since `tech_level`
  saturates and never decays, so even a modest rate compounds over 15-20+ years).
  Full citations in `docs/CAPABILITY_DYNAMICS.md`.
- **Answered "is gdp/capability growth realistic enough" directly**: no — neither
  `internal_capability` nor (even after this fix) `gdp_index` can organically
  *decline*, only slow down or take a one-off event ding that immediately starts
  recovering the next day. No mechanism represents infrastructure destruction,
  verified capability rollback, or a sustained multi-year recession/depression
  regime; `kinetic_escalation`/governance collapse/`sovereignty_fragmentation`
  affect AI capability growth but not `gdp_index` growth at all. Not fixed this
  pass — flagged as a real, identifiable gap for a future session.
- **Added `ev_state_revenue_measures`** (`docs/evidence/ev_state_revenue_measures.md`) —
  fills the `friction_managed_non_utopia` reachability gap using a probability
  *already sourced* in `node_u2_distribution_evidence_rationale.md`
  ("P=0.38 — state-level AI-adjacent revenue measures by 2028") that had never been
  ported into `events.yaml`, rather than inventing a new number. Also split
  `friction_managed_non_utopia`'s horizon_default rule into two OR'd variants
  (distribution-led / reskilling-led) since no single event moves both axes at once.
- **Recalibrated two terminal thresholds using traced/sampled data, not re-guessing:**
  `utopia_radical_abundance`'s `gdp_index` gate raised 1.85→2.5 (also fixes a drift
  from the canonical `terminals.` definition, which was already 2.5) — was 12.6% of
  runs (too common for an "everything went right" tier) under the corrected growth
  model, now 2.2%. `severe_cyber_cascade`'s gate moved `[0.4,0.85]`→`[0.85,1.30]`,
  anchored on tracing actual `gdp_index` on the day `ev_cyber_cascade` fires
  (min=1.01, p50=1.05, max=1.21 across 9 sampled runs) — the old window assumed
  gdp_index barely moves from 1.0 and had become unreachable (0%) once realistic
  compounding applied.
- **Combined result** (n=800, seed=42): region mix 3.8(doom)/5.8(severe)/
  69.6(friction)/20.9(utopia) — `severe` recovered from 0% to 5.8%,
  `friction_managed_non_utopia` from 0% to 10.5%, `utopia_radical_abundance` settled
  at a plausible 2.2% instead of either impossible or too-common. Full before/after
  table in `docs/CALIBRATION.md` "Terminal reachability."
- Full test suite (44 tests) green throughout.

## 2026-07-16 — terminal reachability + gdp_index/capability coupling

Follow-up to a self-review of the 2026-07-15 fix, prompted by re-reading
`docs/research/utopia/node_u2_distribution_evidence_rationale.md` (which the
2026-07-15 fix should have consulted first but didn't).

- **Reverted** the `distribution_regime` deltas added to `ev_fed_edu_reskilling` and
  `ev_meaning_pilot_success` on 2026-07-15. The research explicitly separates
  "labor rules" (retraining, modal, P≈0.68) from "distribution settlement" (SWF,
  rare, P≈0.10-0.22) as sequential, distinct buckets — `terminals.yaml` already had a
  clean `reskilling_absorption`-keyed utopia path for `ev_fed_edu_reskilling`
  specifically to preserve this distinction; adding `distribution_regime` to it
  re-conflated the two. `ev_meaning_pilot_success`'s delta had no support in the
  research file at all. Kept only `ev_swf_enacted`'s delta (well-sourced). Region
  mix barely moved (4.8/8.2/80.2/6.8 → still ~doom/utopia/friction/severe in the same
  range) — the two reverted paths were redundant, not load-bearing.
- **Root cause #2 found**: `friction_ghost_gdp_no_transfer`'s condition is satisfied
  by ~70-90% of horizon-assigned runs and sat *first* in the `horizon_default` list,
  silently shadowing `friction_modal`, `friction_labor_backlash`,
  `friction_surveillance`, and one `utopia_golden_age` variant (all 0/400 despite
  individually-satisfiable conditions). Fixed by reordering the whole list
  doom → utopia → friction-specific-to-general, with the broad ghost_gdp rule moved
  last among friction rules.
- **Root cause #3 found**: `gdp_index` had zero coupling to capability growth (only 6
  discrete event deltas, max +0.40 combined) — `utopia_golden_age`
  (gdp_index≥1.45) and `utopia_radical_abundance` (≥1.85) were mathematically
  unreachable regardless of ordering.
- **First fix attempt (superseded same day)**: added a flat additive daily delta to
  `gdp_index`, magnitude picked empirically to make the terminal thresholds land in a
  plausible-looking distribution. Called out (correctly, by the owner) as
  reverse-engineering a parameter to hit a target rather than modeling the real
  mechanism — `gdp_index` is a level index that should compound like actual GDP.
- **Corrected fix**: `gdp_growth_coupling` (`config/capability_dynamics.yaml`) now
  compounds `gdp_index` daily at `baseline_annual_growth` (2.2%/yr — real long-run
  US/global average, BEA/World Bank) `+ tech_level_accel_scale` (1.2pp/yr at full
  deployment, anchored on IT-diffusion TFP-contribution estimates, deliberately far
  below the "AI explosive growth" literature's 20-30%+/yr scenarios — full citations
  and reasoning in `docs/CAPABILITY_DYNAMICS.md` "GDP growth coupling"). Applied from
  day 1 (not gated on a capability threshold) since ordinary economies grow too.
- **Combined effect of all three root-cause fixes** (n=500, seed=42): region mix
  moved from 4.8(doom)/6.8(severe)/80.2(friction)/8.2(utopia) (no fixes) to
  5.4/0.0/67.0/27.6 (all fixes). Terminal diversity: `friction_modal` reclaimed its
  intended ~48% share (was 0%, shadowed); `friction_ghost_gdp_no_transfer` dropped
  from ~70% to ~8%; `utopia_golden_age` 0%→7.4%; `utopia_radical_abundance`
  0%(impossible)→12.6%. Two items flagged as open questions rather than re-tuned:
  `utopia_radical_abundance` at 12.6% seems too common for an "everything went
  right" tier (likely means the **threshold**, not the growth rate, needs revisiting
  — 1.85x GDP by 2050 isn't extreme once compounding is realistic); `severe_cyber_cascade`
  dropped to 0% since its gdp-contraction gate now fights against upward-drifting
  gdp_index. Full before/after table, remaining rare terminals, and a concrete
  research-backed candidate event for `friction_managed_non_utopia` (state-level
  distribution measures, P≈0.38 per `node_u2_distribution_evidence_rationale.md`,
  not yet ported into `events.yaml`) in `docs/CALIBRATION.md` "Terminal reachability".
- Full test suite (44 tests) still green after all of the above.

## 2026-07-15 — outcome-region regression fix + calibration rigor pass

Follow-up to a review that found the labor/distribution WIP branch (US-China race,
EU regulatory bind, labor mobilization/reskilling/distribution-regime variables and
events) had silently collapsed the emergent outcome distribution from the ~17%
doom/~13% utopia/~65% friction/~5% severe headline to ~1.6%/~1.6%/~91%/~6% — a 74pp
region-mix shift with no CHANGELOG entry, caught by re-running calibration on the
uncommitted working tree.

- **Root cause + fix** — `distribution_regime` (new var, starts at 0.10, threshold
  0.30 in `friction_ghost_gdp_no_transfer`) could only be raised by `ev_swf_enacted`
  (p=0.12) even though `config/society_hazard.yaml` already implied
  `ev_meaning_pilot_success` and `ev_fed_edu_reskilling` should count too — an
  incompletely-wired uplift path. Added `distribution_regime` deltas to both events'
  `on_fire.add_vars` (+0.12, +0.22). Regions moved from 1.6/1.6/90.8/6.0 to
  5.0/7.4/82.6/6.0 (doom/utopia/friction/severe, n=500 seed=42) — close to the
  documented headline again. Residual `friction_ghost_gdp_no_transfer` concentration
  (~61%) reads as a legitimate emergent property of "no active distribution policy ⇒
  no transfer," not tuned further absent new evidence.
- **`probability_uncertainty`** (`config/sim.yaml`) — whitelist expanded from 8 to all
  60 `p_cumulative` events (`events: []` now means "all"); **enabled by default**.
  Addresses CLAUDE.md meta-pitfall #5 ("report confidence intervals, not point
  estimates only").
- **95% Wilson CI** added to `calibration_check.py` region/event output
  (`scripts/calibration_lib.py::wilson_ci`); `seed_sweep.py` now prints a cross-seed
  mean ± std aggregate instead of only per-seed rows.
- **`tests/test_config_integrity.py`** (new) — static cross-reference checks: every
  `unlock`/`lock`/`modify_hazard`/precondition event id, every spine precondition id,
  every terminal-condition event id, every `vars`/`on_fire` state-variable name, and
  every `research_ref` path resolves. Previously unenforced — a typo would silently
  no-op instead of erroring.
- **`tests/test_terminal_coverage.py`** (new) — regression guard for the exact failure
  mode above: no single `horizon_default` terminal may absorb >85% of runs,
  `friction_unclassified` residual capped at 30%, and doom/utopia terminals must be
  reachable within n=100 (excluding known-rare extinction chains). Uses a
  module-scoped fixture so the three tests share one `run_calibration` call instead
  of tripling the cost; the reachability test's original implementation also had a
  logic bug (`report.terminals` — a Counter-derived dict — only has keys for
  terminals that fired at least once, so scanning it for zero-count entries can never
  find any; fixed to diff against the full declared terminal id set from config).
- **Performance note** — `pytest -q` full suite is currently ~2m15s, not the
  README's documented "~15s smoke test." Isolated timing (`probability_uncertainty`
  on vs off, n=100, same seed) showed the uncertainty sampling adds ~0 overhead
  (1.01x) — the real cause is this WIP branch's baseline per-run cost already at
  ~630ms/run vs the ~150-200ms/run the README's performance table assumes (more
  events: 60 vs 57; more correlation clusters: 9 vs 7; extra per-day state). Not
  fixed here — out of scope for a review/calibration pass — but the README
  performance table and "~15s" smoke-test claim should be re-measured and updated
  once this branch lands.
- **`scripts/sensitivity_capability.py`** (new) — one-at-a-time ±25% sensitivity sweep
  over the 22 multiplicative constants in `capability_dynamics.yaml`'s growth model
  against the 12 calibration targets (identifiability check — 22 free params vs 12
  targets is under-determined). Finding: `multiplier_exponent` (161.7%),
  `carrying_capacity` (98.3%), `base_daily_growth` (95.0%) account for nearly all
  sensitivity; the seven `input.*.scale` geopolitics/openness terms are structurally
  inert (exactly 0.0%) because their driving state variables stay near `reference`
  through most trajectories. Full results + rationale in `docs/CALIBRATION.md`.
- **7× `rsi_delay_days`** (`ev_whistle_memo` 21d, `ev_eu_gpai_binds`/`ev_whistle_dump`
  45d, `ev_deploy_incident` 60d, `ev_beneficial_ai_treaty` 90d, `ev_prod_interp_halt`
  120d, `ev_federal_pause_succeeds` 540d) — were unsourced magic numbers violating
  CLAUDE.md's evidence-tracing rule. Added `[GUESS]`-labeled rationale sections to
  each event's `docs/evidence/<id>.md` explaining the relative-ordering logic and
  falsification conditions; flagged for upgrade to a cited estimate if a real natural
  experiment analogue is found.
- **`docs/VARIABLES.md`** — documented the 7 state variables this WIP round added
  (`us_china_race_index`, `eu_regulatory_bind`, `china_open_weight_strategy`,
  `labor_mobilization`, `reskilling_absorption`, `distribution_regime`,
  `rsi_calendar_delay_days`) that had shipped without doc updates.

## 2026-07-08 — web explorer v2 + contributor docs

- **`web/`** — outcome donut, spine course timeline, path buckets, terminal×spine flow, sample run courses
- **`scripts/export_sample_runs.py`** — representative timelines per outcome region
- **`scripts/export_dag.py`** — `web/data/event_graph.json` + `docs/EVENT_GRAPH.mmd`
- **`docs/TRY_IT.md`** — fork → edit YAML → re-run walkthrough

## 2026-07-08 — calibration philosophy

- **Outcome regions are emergent**, not tuned to legacy 19/28/53 partition (pre–Model-2 artifact)
- `calibration_check` / `seed_sweep` report doom/utopia/friction without pass/fail vs those numbers

## 2026-07-08 — v2.4 outcome + path calibration

- **`calibration_check.py`** — outcome regions vs partition targets, early/horizon absorb, path buckets, JSON export
- **`path_frequency.py`** — spine prefixes, event signatures, terminal×spine combos
- **`seed_sweep.py`** — multi-seed stability (42, 123, 456, …)
- **`horizon_default` cascade** — doom/utopia/friction assignment at 2050 (not 100% blind `friction_modal`)
- **C5 deadline** → `2029-03-31`; RSI `2028-10` knot; `sp_c7` threshold 7.15 + legibility ↓
- **`web/`** — static explorer (load JSON from `outputs/runs/`)
- **`docs/CALIBRATION.md`**

## 2026-07-08 — v2.3 Model 2 calibration + society + docs

- **Calibration pass** — `base_daily_growth` + `calendar_rsi` anchors retuned; chain ceiling slack +0.38; c1/c5 legibility hazards adjusted
- **`calibration_check.py`** — conditional P(c5\|c2)…P(c9\|c8), median fire dates, monotonicity flag
- **`ev_c10` consistency** — unlock moved from `sp_c8` → `sp_c9` (matches `preconditions.spine_fired: [sp_c9]`)
- **`capability_controls`** — `ev_prod_interp_halt` (growth×0.78), `ev_multilateral_screening_pilot` (growth×0.92)
- **Society hazards** — Tier 1+2 variable → event feedback (`society_hazard.yaml`)
- **Docs** — `ARCHITECTURE.md` Model 2 + legibility; `CAPABILITY_DYNAMICS.md` synced to yaml

## 2026-07-08 — v2.2 political coupling + legibility

- **Legibility** — latent spine crossing ≠ public fire; `observability.daily_hazard`
- **`capability_controls`** — federal pause, US paralysis S2
- **Early terminals** — `friction_pause_stall`, `friction_governance_paralysis`
- **Variance** — shock prob 0.018, `run_heterogeneity.growth_scale_spread: 0.10`

## 2026-07-08 — v2.1 spine calibration + evidence

- **Spine P/windows tuned** — wider overlapping windows; conditional targets 0.65–0.82
- **`calibration_check.py`** — by-deadline unconditional, conditional \| parent, event conditionals
- **`spine_fire_days`** tracked in engine for deadline calibration
- **Evidence:** `sp_c1`–`sp_c9` full files; `ev_c5/c6/c8` → superseded redirect stubs
- **`ev_c10` evidence** — `spine_fired: [sp_c9]`, unlock from `sp_c8`

## 2026-07-08 — v2.0 probabilistic spine

- **BREAKING:** `ci_schedule.yaml` deterministic calendar **removed** from engine
- **`config/spine.yaml`** — 7 stochastic AI-2027 capability milestones (`sp_c1`–`sp_c9`, skip C3/C4/C10 plot beats)
- **`spine.py`** — same hazard/eligibility model as events; fires before events each day
- **Merged into spine:** `ev_c5_agent2_internal`, `ev_c6_superhuman_coder`, `ev_c8_agi_public` (57 events remain)
- **Plot beats events-only:** C3=`ev_china_cdz`, C4=`ev_c4_labor_shock`, C10=`ev_c10_internal_concern`
- Events use `preconditions.spine_fired` instead of `ci_min`
- **Alignment chain fixed:** `sp_c8` unlocks C10 plot; `sp_c9` + extended windows
- `docs/SPINE.md`; `calibration_check.py` reports spine + event marginals
- Tests: `tests/test_spine.py`

## 2026-07-07 — v1.2 correlations + sovereignty events

- **Research link hygiene** — `--rewrite-research-links` rewrites internal `docs/research/` citations; `supplements/tracker_scorecard.md` stub; relative links within research tree
- **Latent cluster correlations** — `config/correlations.yaml`, `correlations.py`, `docs/CORRELATIONS.md`; 7 clusters (race, bio_governance, bio_tail, alignment_governance, compute_chokepoint, governance_hollowing, sovereignty)
- **Stochastic Ci** — `ci_schedule.yaml` `stochastic:` section; opt-in via `sim.yaml` `stochastic_ci: false` (default)
- **+2 events** — `ev_india_sovereign_ai_stack` (P=0.40), `ev_gulf_compute_sovereignty` (P=0.35); **60 events** total
- **`sovereignty_fragmentation`** state variable
- Tests: `tests/test_correlations.py`

## 2026-07-07 — v1.1 OSS-ready evidence + research

- **58 events** — ontology complete (mutex groups, terminals fixed)
- **58/58 evidence** files — Claim | Why | Evidence | YAML mapping
- **`docs/research/`** — ~38 ported spine/utopia/reference/supplements files; self-contained for OSS
- Link rewrite: evidence → `docs/research/`; Chinese/private refs → public URLs
- `docs/research/reference/` — Ci spine, crux registry, parallel spines (was confusing `archive/`)
- Removed `docs/ONTOLOGY_GAPS.md` (closure doc, stale)
- `docs/EVENTS_INDEX.md` updated to 58 events

**Not done (v1.1):** calibration pass; 10k sim validation.

## 2026-07-07 — v1.3 evidence depth + YAML calibration

- **Evidence depth** — India/Gulf sovereignty events expanded to full template; corp hollowing deepened; thin-file pass on whistleblower/C10 timing
- **YAML ↔ evidence sync** — `ev_bmia_pass` 0.45, `ev_race_acceleration` 0.22, `ev_cyber_cascade` 0.12, C10 + whistleblower windows from **2028-07-01** (tracker Q2–Q3)
- **`scripts/calibration_check.py`** — marginal fire rates vs targets
- Evidence frontmatter `p_cumulative` aligned with YAML for calibrated events
- **Engine fix** — `daily_hazard` now uses full-window constant hazard (was re-scaling `p_cumulative` against shrinking `remaining` days → marginals → 1)

## 2026-07-07 — v1.1 ontology scaffold

- +8 events, +6 variables, `ev_wmd_escalation` terminal fix
- All events → `research_ref: docs/evidence/<id>.md`

## 2026-07-07 — v0.1 scaffold

- Initial repo: 50 events, engine, daily timestep to 2050
