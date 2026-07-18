# Calibration

Scripts and targets for Model 2 spine + **emergent** outcome distribution.

## What we calibrate vs what we measure

| Calibrate (has targets) | Measure only (emergent) |
|-------------------------|-------------------------|
| Spine `P(by deadline)` | Outcome regions: doom / utopia / friction / severe |
| Spine conditionals `P(cN\|parent)` | Terminal mix, path buckets |
| Plot event marginals (`ev_no_pause_2028`, etc.) | `P(doom\|sp_c9)`, alignment chain rates |

**Important:** The headline partition **19% / 28% / 53%** in `notes/ai_futures_archive_2026-07/02_outcome_partition.md` came from a **pre–Model-2 algorithm** and is **not** a sim target. The joint Monte Carlo output (doom 6.2% ± 0.1%, utopia 20.8% ± 2.3%, friction 66.4% ± 2.5%, severe 6.7% ± 0.4% at n=400×3 seeds, current as of 2026-07-17 — see the dated entries below for the full recalibration history) is the more honest forecast object.

Do **not** tune terminals to reproduce 19/28/53.

## Spine / event targets

Defined in `scripts/calibration_lib.py` — AI-2027 deadlines, conditional spine, crux event marginals.

**C5 deadline:** `2029-03-31` (modal ~2029 Q1 per `03_ci_spine.md`).

## Commands

```bash
python scripts/calibration_check.py -n 2000 --seed 42 \
  --output outputs/runs/calibration_summary.json

python scripts/path_frequency.py -n 2000 --seed 42 \
  --output outputs/runs/path_frequency.json

python scripts/seed_sweep.py -n 1000 --seeds 42 123 456 \
  --output outputs/runs/seed_sweep.json
```

## Web explorer

```bash
cd web && python -m http.server 8787
# Load outputs/runs/calibration_summary.json
```

## Horizon assignment

Runs reaching 2050 without an absorbing terminal are classified via `horizon_default` cascade in `config/terminals.yaml`. `horizon_only` terminals (e.g. `friction_modal`) are not checked mid-sim.

## Terminal reachability (2026-07-16 investigation)

`horizon_default` is a **first-match-wins list** (`terminals.py::default_terminal_at_horizon`). Two independent failure modes were found and partially fixed:

**1. Ordering shadowing (fixed).** `friction_ghost_gdp_no_transfer`'s condition
(`ghost_gdp_index>=0.30, distribution_regime<0.30, inequality_index>=0.48`) is
satisfied by the large majority of horizon-assigned runs (ghost_gdp_index ratchets up
via `employment_coupling` once capability crosses 4.0; distribution_regime rarely
crosses 0.30 since only `ev_swf_enacted` moves it). Sitting first in the list, it was
silently pre-empting `friction_modal`, `friction_labor_backlash`,
`friction_surveillance`, and one `utopia_golden_age` variant — all of which had
individually satisfiable conditions but fired **0/400 times**. Fixed by reordering
the whole `horizon_default` list doom -> utopia -> friction, and *within* friction
from most-specific-condition to least (ghost_gdp_no_transfer now last, right before
the true `friction_unclassified` fallback).

**2. Structural unreachability (partially fixed).** `gdp_index` had no capability
coupling at all — see "GDP growth coupling" in `docs/CAPABILITY_DYNAMICS.md` — making
`utopia_golden_age`/`utopia_radical_abundance`'s gdp thresholds mathematically
unreachable regardless of ordering. Added `gdp_growth_coupling`.

**Before → after** (n=800, seed=42; cumulative effect of the ordering fix, the
real-data-grounded compounding gdp coupling, the `ev_state_revenue_measures` event,
and the `utopia_radical_abundance`/`severe_cyber_cascade` threshold recalibration —
see `docs/CAPABILITY_DYNAMICS.md` "GDP growth coupling" for why the first, additive
version of the gdp coupling was replaced same-day):

| Terminal | Before (no fixes) | After |
|---|---|---|
| `friction_ghost_gdp_no_transfer` | 69.8% (dominant) | 5.6% |
| `friction_modal` | 0% (shadowed) | 30.8% |
| `friction_managed_non_utopia` | 0% (unreachable — no intermediate event) | 10.5% |
| `friction_unclassified` (residual) | ~0% | 12.9% |
| `utopia_golden_age` | 0% (shadowed + gdp-unreachable) | 10.4% |
| `utopia_modest_welfare` | 7.0% | 6.4% |
| `severe_cyber_cascade` | 7.0%-ish pre-WIP, 0% after gdp fix broke it | 5.8% (fixed) |
| `utopia_radical_abundance` | 0% (mathematically impossible), then 12.6% (threshold too low) | 2.2% (rare tail, as intended) |
| region mix (doom/severe/friction/utopia) | 4.8/6.8/80.2/8.2 | 3.8/5.8/69.6/20.9 |

The two open questions from the previous pass are resolved:

- **`utopia_radical_abundance`** — raised the `gdp_index` gate from 1.85 to **2.5**,
  which also fixes a drift where `horizon_default`'s check (1.85) and the canonical
  `terminals.utopia_radical_abundance` definition (2.5) had silently diverged. n=800
  showed P(gdp_index≥2.5)=5.2% unconditionally; combined with the tech_level/autonomy/
  event requirements, the terminal now lands at 2.2% — a genuinely rare tail rather
  than a common outcome, without touching the (real-data-grounded) growth rate itself.
- **`severe_cyber_cascade`** — traced `gdp_index` on the actual day `ev_cyber_cascade`
  fires (post its own -0.25 delta) across 9 sample runs: min=1.01, p50=1.05, max=1.21.
  The old `[0.4, 0.85]` gate assumed gdp_index barely moves from 1.0 (true before the
  gdp coupling fix) and became unreachable once realistic compounding applies — by the
  time this event is eligible (2029-2035, gated on sp_c6), baseline+AI-accelerated
  growth has already pushed gdp_index past 1.0 net of the shock. New gate `[0.85, 1.30]`
  is anchored on that trace, not re-guessed, and the terminal fires at a sane 5.8%.

**Still unreached / rare** — reachable in principle, structurally rare or gated on a mechanism gap not addressed this pass:

- `friction_labor_backlash` — gated on `ev_reskilling_fails_absorb_c4` firing, which requires `ev_fed_edu_reskilling` NOT fired; but `ev_labor_ai_mobilization` (a precondition-adjacent event) *boosts* `ev_fed_edu_reskilling`'s hazard, so the two paths partly cancel each other out. Worth checking event correlation, not just terminal ordering.
- `friction_surveillance` — needs `human_autonomy_index` in [0.25, 0.58]; autonomy's empirical distribution rarely sits in that band (typically ~0.68-0.93 outside doom trajectories, <0.4 inside them) — the band falls in a gap between "normal friction" and "doom" trajectories under current dynamics.

### Fixed: `friction_managed_non_utopia` — added the missing event rather than inventing a number

`docs/research/utopia/node_u2_distribution_evidence_rationale.md` already had a sourced
probability estimate for an intermediate policy outcome with **no corresponding
event** — the actual fix for this terminal's reachability gap, not a new invented
number:

- **"P=0.38 — State-level AI-adjacent revenue measures (CA/NY/WA) by 2028"** — a
  state-level compute tax / data-center surcharge / equity-severance mandate "with
  teeth," distinct from (and more likely than) full federal SWF (`ev_swf_enacted`,
  P=0.10-0.12). Would plausibly raise `distribution_regime` by a *partial* amount
  (patchwork, not full settlement) — exactly the intermediate state
  `friction_managed_non_utopia` needs and currently has no path to. Also matches
  "P=0.45 — Second-wave policy window @C6-C7" (serious federal commission → bill,
  not enactment) as a second, later-window variant.

**Added 2026-07-16** as `ev_state_revenue_measures` (`docs/evidence/ev_state_revenue_measures.md`,
p_cumulative=0.38, distribution_regime +0.22, inequality_index -0.05 — sized to land
in `friction_managed_non_utopia`'s band alone, deliberately smaller than
`ev_swf_enacted`'s deltas since it's a partial/patchwork mechanism by design). The
"second-wave" variant (P=0.45, later C6-C7 window) was not modeled as a separate
event — folded into the rationale for the same event's window rather than adding a
second near-duplicate. `friction_managed_non_utopia`'s horizon_default rule was also
split into two OR'd variants (distribution-led vs reskilling-led) since requiring
both `distribution_regime` and `reskilling_absorption` in-band simultaneously — with
no event moving both — made the AND-form unreachable regardless of this fix.

## Capability-growth parameter sensitivity (identifiability check)

`capability.py::_growth_factor` composes **22 independent multiplicative scale/exponent
constants** from `config/capability_dynamics.yaml`, but the calibration targets in
`calibration_lib.py` are only **12 numbers** (7 `cap_by_deadline` marginals + 5
`SPINE_CONDITIONALS`). That is an under-identified system: many different parameter
settings can hit the same milestone-deadline targets while differing arbitrarily
elsewhere. Before trusting any single constant's exact value, it's worth knowing which
of the 22 the calibration targets actually respond to.

**Method** (`scripts/sensitivity_capability.py`): one-at-a-time ±25% perturbation from
the current YAML value, common random numbers (same seed, `probability_uncertainty`
forced off to isolate structural sensitivity from elicitation noise), n=60,
seed=42. `sensitivity_score` = sum of `|Δ|` across `sp_c5_by_deadline`,
`sp_c9_by_deadline`, `doom` region share, `utopia` region share, comparing the −25%
and +25% runs.

| Rank | Parameter | Score | Read |
|---|---|---|---|
| 1 | `multiplier_exponent` | **161.7%** | Exponent on the RSI multiplier (up to 55×) — by far the most load-bearing single number in the model. A ±25% swing alone moves `sp_c9_by_deadline` by 50pp. |
| 2 | `carrying_capacity` | **98.3%** | Logistic ceiling on `internal_capability`; directly gates how much of the spine is reachable at all. |
| 3 | `base_daily_growth` | **95.0%** | Linear growth-rate multiplier; moves `sp_c5_by_deadline` by 78pp. |
| 4 | `coordination_brake.scale` | 23.3% | |
| 5 | `governance_brake.governance_scale` | 21.7% | |
| 6 | `sovereignty_fragmentation.scale` | 20.0% | |
| 6 | `race_amplification.scale` | 20.0% | |
| 8 | `governance_brake.salience_scale` | 18.3% | |
| 8 | `trust_governance_brake.scale` | 18.3% | |
| 10 | `admin_ai_posture.growth_scale` | 13.3% | |
| 10 | `kinetic_escalation.growth_penalty` | 13.3% | |
| 10 | `secret_race_boost.scale` | 13.3% | |
| 13 | `bio_spillover.bio_to_cap_scale` | 8.3% | |
| 13 | `gdp_funding.scale` | 8.3% | |
| 15 | `input.frontier_capex_index.scale` | 1.7% | |
| 16–22 | `input.deployment_pressure/china_frontier_parity/us_china_race_index/compute_concentration/eu_regulatory_bind/open_weights_regime/frontier_lab_polarization.scale` | **0.0%** (all seven) | See below — structurally inert, not just "small effect." |

Full per-parameter lo/hi metrics: `outputs/runs/sensitivity_capability.json`.

**Takeaways:**

1. **Three numbers do almost all the work**: `multiplier_exponent`, `carrying_capacity`,
   `base_daily_growth` account for the overwhelming majority of the model's response to
   the calibration targets. These three should get the most scrutiny/evidence when
   revised — everything else is comparatively cheap to get wrong.
2. **The seven `input.*.scale` terms at exactly 0.0% aren't merely "low sensitivity" —
   they're structurally inert under the current dynamics.** `_input_factor()` computes
   `1 + scale * max(0, val/reference - 1)`: if the driving state variable
   (`deployment_pressure`, `china_frontier_parity`, `us_china_race_index`,
   `compute_concentration`, `eu_regulatory_bind`, `open_weights_regime`,
   `frontier_lab_polarization`) stays close to its `reference` value for most of a
   typical 2026–2050 trajectory, the excess term never activates regardless of `scale`.
   Two honest readings: (a) these variables are supposed to move further from baseline
   in scenarios this sweep's fixed seed/config didn't sample — worth re-running the
   sweep at a seed/config where e.g. `china_frontier_parity` swings further — or (b)
   these knobs are currently decorative and the model would behave identically with
   them deleted. Don't treat their YAML values as calibrated until one of these is
   resolved.
3. **This does not fix the identifiability problem** — it only tells you where the
   slack is. Reducing free parameters (e.g., folding the seven inert `input.*.scale`
   terms into a single generic "governance/geopolitics index" coupling, or dropping
   them) would make the remaining ~15 parameters easier to actually calibrate against
   12 targets.

Re-run: `python scripts/sensitivity_capability.py -n 200 --seed 42 --output outputs/runs/sensitivity_capability.json` (takes ~25-45 min pure Python at n=200; the script logs progress per parameter and writes partial results after each one, so it's safe to inspect mid-run or kill early).

## Fixed: 5 of 7 dead `input.*.scale` parameters (2026-07-17)

Takeaway 2 above left two honest readings open for why the seven `input.*.scale` terms
scored exactly 0.0%: (a) these variables just don't move far from `reference` in the
sampled trajectories, or (b) the knobs are currently decorative. Checked directly rather
than guessed: **(b), and worse than "decorative" — mathematically guaranteed to be zero
for the lifetime of any run, not merely unobserved.** None of the seven had an explicit
`reference` in `config/capability_dynamics.yaml`, so `_input_factor()` fell back to its
default of 1.0. Unlike `frontier_capex_index` (the one `input.*` term with an explicit
`reference: 1.0`, legitimately clamped up to 3.0 so it can exceed that reference), all
seven of the others are 0-1-bounded indices, and *every* `add_vars`/`set_vars` in
`config/events.yaml` that touches them carries `clamp: [0, 1]` — confirmed by grep, not
sampled. `max(0, val/1.0 - 1)` cannot be positive for a value that can never exceed 1.0.

**Fix** (`config/capability_dynamics.yaml`): gave each of the seven an explicit
`reference` equal to its own initial value from `config/variables.yaml` — already-elicited
numbers, not new judgment calls. Re-ran the sweep (`n=60`, seed 42):

| Parameter | Before | After | Why |
|---|---|---|---|
| `input.deployment_pressure.scale` | 0.0% | 20.0% | Fixed — can rise above its own initial value via race-related events |
| `input.china_frontier_parity.scale` | 0.0% | 18.3% | Fixed |
| `input.eu_regulatory_bind.scale` | 0.0% | 18.3% | Fixed |
| `input.compute_concentration.scale` | 0.0% | 13.3% | Fixed |
| `input.us_china_race_index.scale` | 0.0% | 13.3% | Fixed |
| `input.open_weights_regime.scale` | 0.0% | **0.0%** | Still dead — no event in `events.yaml` touches this variable at all; it never moves from its initial value regardless of `reference` |
| `input.frontier_lab_polarization.scale` | 0.0% | **0.0%** | Still dead — the only two events touching it (`ev_compute_triopoly_lock`, `ev_singleton_lab_dominance`) both `set_vars` it *below* its initial 0.55 (to 0.45, 0.15); it can only fall from reference, never exceed it, so the "excess above baseline" gate still can't fire |

Consequence, not incidental: giving five parameters real (net-positive) effect for the
first time pushed absolute capability timing further from the AI-2027-derived targets —
`sp_c5_by_deadline` moved from ~80-90% to ~90-95% against a 65% target, and **every**
milestone deadline check now fails (previously most, not all). The top-3 dominant
parameters' own scores dropped too (`multiplier_exponent` 161.7%→121.7%,
`carrying_capacity` 98.3%→71.7%, `base_daily_growth` 95.0%→70.0%) since variance in the
overall growth factor now has more places to go. This is not a sign the fix was wrong —
the seven parameters were genuinely dead code — but it does mean `base_daily_growth` and
the `calendar_rsi` anchors need a fresh calibration pass against an engine where these
five terms are live, not the one they were originally tuned against. That recalibration
is not done as part of this fix.

Full before/after data: `outputs/runs/sensitivity_capability.json` (post-fix),
`docs/CHANGELOG.md` 2026-07-17 entry.

## Fixed: the remaining 2 of 7 — `frontier_lab_polarization` and `open_weights_regime` (2026-07-17, cont.)

The two parameters left inert above needed genuinely different fixes, not more reference-value
tweaks — investigated with real evidence rather than guessed, per the owner's explicit
request to "spend time doing evidence research."

**`open_weights_regime`.** No event in `config/events.yaml` touched it at all. Checked
`ev_open_weights_equilibrium` and `ev_open_weights_tamper_response` (thematically the
right pair — one is literally titled "open-weights frontier equilibrium persists") and
found their `on_fire` blocks only moved `bio_risk_pressure` and `china_open_weight_strategy`
(a distinct variable, per `docs/VARIABLES.md`), never `open_weights_regime`. The tamper-response
event's own evidence doc (`docs/evidence/ev_open_weights_tamper_response.md`) already had a
row in its YAML-mapping table specifying `open_weights_regime: -0.3` — researched, documented,
and never actually implemented. Wired both events in: `ev_open_weights_equilibrium` +0.20
`[GUESS]` (mirrored from its own `china_open_weight_strategy` delta on the same event, no
existing number to reuse), `ev_open_weights_tamper_response` -0.3 (the pre-existing
documented-but-unimplemented figure).

**`frontier_lab_polarization`.** The only two events touching it (`ev_compute_triopoly_lock`,
`ev_singleton_lab_dominance`) both set it *below* its initial value (0.45, 0.15 vs. initial
0.55) — the growth function's "excess above reference" gate could structurally never fire in
either direction that mattered. Researched (not guessed) whether the relationship between lab-market
polarization and capability growth should be one-sided or two-sided: Aghion, Bloom, Blundell,
Griffith & Howitt (2005, *QJE* 120(2), "Competition and Innovation: An Inverted-U
Relationship") — neck-and-neck competitors innovate faster specifically to escape their
rivals ("escape-competition effect"), supporting the existing positive `scale` direction, not
a flip. Bueno de Mesquita, Dziuda & Polborn (2026, NBER w35276) — AI-specific and more direct:
more competing labs means each devotes a larger resource share to speed over safety; fewer,
more consolidated labs face less pressure to prioritize speed. Both support a genuinely
*two-sided* relationship (consolidation should dampen growth, not just fail to bonus it), not
merely a missing upside. Added a `symmetric: true` option to `_input_factor()`
(`capability.py`) — applied only to this one input, removing the `max(0, ...)` floor so
consolidation now measurably dampens growth. `scale` magnitude (0.08) left unchanged: the
citations support direction and functional form, not a specific number.

**Result** (`n=60` sweep, seed 42): `input.frontier_lab_polarization.scale` 0.0%→31.7%,
`input.open_weights_regime.scale` 0.0%→20.0%. All 22 parameters now show real sensitivity.

**Consequence:** as with the first round, giving these two real effect further sped up
capability growth, pushing spine timing off target again — see the recalibration entry below.

## Fixed: `frontier_capex_index` drift-clamp bug (2026-07-17, cont.)

An unexpected finding while re-running the sweep after the fix above: `input.frontier_capex_index.scale`
— the *one* `input.*` term that had never been inert (its driving variable is legitimately
clamped to `(0.5, 3.0)`, not `[0,1]`, so it can genuinely exceed its `reference: 1.0`) — dropped
to exactly 0.0%. Direct sampling (150 runs, `engine.run_once()` in isolation) found
`frontier_capex_index` frozen at *exactly* 1.000 in **100% of sampled runs**, despite
`gdp_index` ranging up to 2.0 in the same runs.

**Root cause:** `engine.py::_drift_variables()` applies a generic small daily drift to several
state variables, using `clamp=(0.0, 1.0)` by default for anything not explicitly excluded.
`tech_level` and `deployment_pressure` were already excluded from this loop because they have
their own dedicated, differently-clamped mechanisms elsewhere in `capability.py` —
`frontier_capex_index` has the exact same situation (the `gdp_capex_coupling` mechanism,
correctly clamped to `(0.5, 3.0)`) but was missing from the exclusion set. Every day, that
dedicated mechanism's small upward nudge toward `gdp_index` was immediately clamped back down
to exactly 1.0 by the generic drift function running afterward, canceling it out completely —
confirmed by isolating `_apply_macro_couplings()` alone (real movement, 1.0→1.032 over 1000
calls with a forced gap) versus the full engine loop (zero movement, ever).

**Fix:** added `frontier_capex_index` to `_drift_variables()`'s exclusion set, matching the
existing precedent for `tech_level`/`deployment_pressure`.

**Result:** post-fix sampling — 97% of 150 runs now show `frontier_capex_index` above 1.0
(median 1.26, max 1.71), versus 0% before. Sensitivity sweep confirms: 0.0%→25.0%.

This closes the identifiability investigation started earlier today: **zero of 22 capability-growth
parameters remain structurally inert**, down from seven when the sweep was first run.

## Spine recalibration (2026-07-17, two rounds, 8 probe iterations)

Each of the three fixes above gave previously-dead or previously-frozen parameters real,
net-growth-positive effect, and each one pushed the spine's absolute deadline timing further
from the AI-2027-derived targets — the growth rate tuned against an engine with those
parameters inert was no longer the right rate once they went live. Recalibrated
`base_daily_growth` and the late `calendar_rsi` anchors against `scripts/calibration_check.py`'s
7 absolute-deadline + 5 conditional-probability targets, using fast `n=200` probes and a final
`n=600` confirmation.

**Round 1** (after the 5-of-7 reference-value fix): `base_daily_growth` 0.00136→0.00110;
`calendar_rsi` late anchors 2028-10: 8.4→7.5, 2029-01: 11.0→10.5, 2030-06: 50.0→32.0. Landed at
5/7 absolute + 2/5 conditional passing (best of 5 probes).

**Round 2** (after the `frontier_lab_polarization`/`open_weights_regime`/`frontier_capex_index`
fixes, which sped growth up again): `base_daily_growth` 0.00110→0.00104; `calendar_rsi`
2030-06 anchor 32.0→26.0 (2028-10 and 2029-01 anchors unchanged from round 1). Landed at
**7/7 absolute passing at n=600** — the best calibration state this project has had — but only
**1/5 conditional** (`P(sp_c5|sp_c2)`) passing, down from round 1's 2/5.

**The absolute/conditional trade-off is real, not a search-quality problem.** Probing found
that pushing absolute deadlines onto target (via a uniform `base_daily_growth` reduction and/or
flattened late `calendar_rsi` anchors) systematically throttles runs that are *already ahead of
schedule*, because `calendar_rsi` anchors are indexed to calendar date, not to how far along a
given run's own trajectory already is — a fast-starting run gets slowed by the same time-indexed
anchor as a slow one, which is exactly what the conditional-probability targets penalize. Settled
on the round-2 config (maximizes absolute-deadline compliance, since that was the
originally-disclosed, headline-visible gap) rather than continuing to iterate; the conditional
shortfall is now the primary open calibration item (see `docs/TECHNICAL_REPORT.md` §9 for
possible structural fixes — a capability-progress-indexed rather than purely calendar-indexed
RSI curve is the most promising direction, not attempted here).

**Final headline** (n=400×3 seeds): doom 6.2% ± 0.1%, utopia 20.8% ± 2.3%, friction 66.4% ±
2.5%, severe 6.7% ± 0.4% — versus the pre-today baseline of 7.1% / 18.0% / 68.5% / 6.4%. All 44
tests pass throughout every step of this process.
