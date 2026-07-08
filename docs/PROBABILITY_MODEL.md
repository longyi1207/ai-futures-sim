# Probability model

## The #1 mistake to avoid

**`p_cumulative` is NOT `p_per_day`.**

In `events.yaml`:

```yaml
schedule:
  start: "2027-01-01"
  end: "2028-12-31"
  p_cumulative: 0.40
```

Means: **P(event fires at least once between 2027-01-01 and 2028-12-31) = 0.40**, conditional on staying eligible each day.

## Daily hazard conversion

For once-only events, the engine uses a **constant daily hazard** over remaining days in the window:

```
h = 1 − (1 − p_cumulative)^(1 / days_remaining)
```

Implemented in `cumulative_to_daily_hazard()` (`src/futures_sim/events.py`).

Each eligible day: `P(fire today) = h × hazard_multipliers[event]`.

After fire (once-only): event removed from eligible pool.

## Explicit daily hazard

For fine control, set:

```yaml
schedule:
  daily_hazard: 0.0003   # literal P(fire on an eligible day)
```

Use when cumulative window framing is wrong (e.g. recurring shocks).

## Calibrating from annual statements

If evidence says "~40% chance by end of 2028" → set `p_cumulative: 0.40` with matching window. **Do not** divide by 365.

If evidence says "~5% per year" for a repeatable process, decide:

- **Repeatable:** multiple fires allowed (`once: false`) + daily_hazard from yearly rate.
- **One-shot:** convert to window cumulative.

## Checking calibration

After `futures-sim -n 10000`:

```python
# Fraction of runs where event fired should ≈ p_cumulative (conditional on eligibility paths)
```

Large drift → wrong window, wrong precondition gates, or hazard multipliers dominating.

## Correlation

**Latent cluster shocks** (`config/correlations.yaml`, `src/futures_sim/correlations.py`) modulate daily hazards so events in the same research cluster co-move. See `docs/CORRELATIONS.md`.

Additional coupling still emerges from **shared variables and unlock chains** via `modify_hazard` and `add_vars`.

Toggle: `sim.yaml` → `use_correlations: true` (default).

## Uncertainty (planned)

Sample each `p_cumulative` from a Beta distribution per run (parameter ensemble). Report 5th–95th percentile on `P(doom)`.
