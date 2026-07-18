"""Monte Carlo simulation engine — one day per step."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

import numpy as np

from .capability import parse_calendar_rsi_anchors, step_capability
from .ci import sim_dates
from .correlations import CorrelationModel
from .events import EventCatalog
from .spine import SpineCatalog
from .state import WorldState
from .terminals import check_terminals, default_terminal_at_horizon


@dataclass
class RunResult:
    terminal: str
    terminal_day: int
    fired_events: list[str]
    fired_spine: list[str]
    spine_fire_days: dict[str, int]
    final_state: dict[str, Any]
    absorbed_at_horizon: bool = False
    trace: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class SimEngine:
    config: dict[str, Any]
    rng: np.random.Generator

    def __post_init__(self) -> None:
        self.catalog = EventCatalog(
            self.config["events"],
            society_hazards=self.config.get("society_hazards"),
        )
        self.spine = SpineCatalog(self.config["spine"])
        self.capability_dyn = self.config.get("capability_dynamics") or {}
        sim = self.config["sim"]
        self.start, self.end, self.n_days = sim_dates(sim["start_date"], sim["end_date"])
        self._rsi_anchors = parse_calendar_rsi_anchors(
            self.capability_dyn.get("calendar_rsi"),
            self.start,
        )
        self.max_fires_per_day = int(sim.get("max_fires_per_day", 2))
        self.max_spine_fires_per_day = int(sim.get("max_spine_fires_per_day", 2))
        self.trace = bool(sim.get("record_trace", False))
        correlations_doc = self.config.get("correlations")
        self.correlation_model = CorrelationModel.from_config(correlations_doc)
        self.use_correlations = bool(sim.get("use_correlations", True)) and self.correlation_model is not None
        self._dates = [self.start + timedelta(days=i) for i in range(self.n_days)]
        self._event_window_by_day: list[list[str]] = [
            [eid for eid in self.catalog.events if self.catalog.in_window(eid, d)] for d in self._dates
        ]
        self._spine_window_by_day: list[list[str]] = [
            [mid for mid in self.spine.milestones if self.spine.in_window(mid, d)] for d in self._dates
        ]

    def run_once(self) -> RunResult:
        state = WorldState()
        self._apply_initial(state)
        self._sample_probability_overrides(state)
        het = self.capability_dyn.get("run_heterogeneity") or {}
        if float(het.get("growth_scale_spread", 0)) > 0:
            spread = float(het["growth_scale_spread"])
            state.capability_growth_scale *= float(self.rng.uniform(1.0 - spread, 1.0 + spread))
        trace: list[dict[str, Any]] = []
        cluster_latents = (
            self.correlation_model.init_latents(self.rng)
            if self.use_correlations and self.correlation_model
            else None
        )

        for day, current in enumerate(self._dates):
            if cluster_latents is not None and self.correlation_model is not None:
                cluster_latents = self.correlation_model.step_latents(cluster_latents, self.rng)

            step_capability(state, self.rng, self.capability_dyn, day=day, rsi_anchors=self._rsi_anchors)
            ceiling = self.spine.effective_capability_ceiling(state)
            if state.internal_capability > ceiling:
                state.internal_capability = ceiling
            self._drift_variables(state)

            terminal = check_terminals(state, self.config["terminals"])
            if terminal:
                state.terminal = terminal
                state.terminal_day = day
                break

            spine_fired_today = self._fire_spine_thresholds(state, current, day)
            for mid in spine_fired_today:
                state.spine_fire_days[mid] = day
                terminal = check_terminals(state, self.config["terminals"])
                if terminal:
                    state.terminal = terminal
                    state.terminal_day = day
                    break

            if state.terminal:
                break

            fired_today = self._sample_events(state, current, day, cluster_latents)
            for eid in fired_today:
                self.catalog.fire(eid, state, rng=self.rng)
                terminal = check_terminals(state, self.config["terminals"])
                if terminal:
                    state.terminal = terminal
                    state.terminal_day = day
                    break

            if state.terminal:
                break

            if self.trace:
                trace.append(
                    {
                        "day": day,
                        "date": current.isoformat(),
                        "spine": spine_fired_today,
                        "events": fired_today,
                        **state.snapshot(),
                    }
                )

        absorbed_at_horizon = False
        if not state.terminal:
            state.terminal = default_terminal_at_horizon(state, self.config["terminals"])
            state.terminal_day = self.n_days - 1
            absorbed_at_horizon = True

        return RunResult(
            terminal=state.terminal,
            terminal_day=state.terminal_day or self.n_days - 1,
            fired_events=sorted(state.fired_events),
            fired_spine=sorted(state.fired_spine),
            spine_fire_days=dict(state.spine_fire_days),
            final_state=state.snapshot(),
            absorbed_at_horizon=absorbed_at_horizon,
            trace=trace,
        )

    def _apply_initial(self, state: WorldState) -> None:
        for name, spec in self.config["variables"].get("initial", {}).items():
            state.set_var(name, float(spec["value"]))

    def _sample_probability_overrides(self, state: WorldState) -> None:
        """Sample run-level uncertainty around elicited p_cumulative inputs."""
        cfg = self.config["sim"].get("probability_uncertainty") or {}
        if not bool(cfg.get("enabled", False)):
            return
        concentration = float(cfg.get("beta_concentration", 80.0))
        if concentration <= 0:
            return
        include = set(cfg.get("events") or [])
        for eid, ev in self.catalog.events.items():
            if include and eid not in include:
                continue
            sched = ev.get("schedule", {})
            if "p_cumulative" not in sched:
                continue
            p = float(sched.get("p_cumulative", 0.0))
            if p <= 0.0 or p >= 1.0:
                continue
            alpha = max(1e-6, p * concentration)
            beta = max(1e-6, (1.0 - p) * concentration)
            state.event_p_overrides[eid] = float(self.rng.beta(alpha, beta))

    def _drift_variables(self, state: WorldState) -> None:
        """Slow exogenous drift — capability dynamics handle RSI; this is residual."""
        drift = self.config["variables"].get("daily_drift", {})
        for name, delta in drift.items():
            # tech_level and deployment_pressure already have their own dedicated
            # mechanisms elsewhere (capability.py) and are excluded here for that
            # reason. frontier_capex_index has the same situation (gdp_capex_coupling
            # in capability.py, correctly clamped to (0.5, 3.0)) but was missing from
            # this list -- found 2026-07-17 via the sensitivity sweep: this loop's
            # default clamp=(0.0, 1.0) doesn't fit frontier_capex_index's real (0.5,
            # 3.0) range, so it silently clamped the variable back to exactly 1.0
            # every day, canceling out its dedicated mechanism entirely (confirmed
            # empirically: frontier_capex_index == 1.000 in 150/150 sampled runs
            # despite gdp_index reaching up to 2.0).
            if name in {"tech_level", "deployment_pressure", "frontier_capex_index"}:
                continue
            clamp = (0.0, 1.0) if name not in {"gdp_index", "ai_rd_multiplier"} else None
            state.apply_delta(name, float(delta), clamp=clamp)

    def _fire_spine_thresholds(self, state: WorldState, current: date, day: int) -> list[str]:
        """Register latent threshold crossings; fire when publicly legible (stochastic)."""
        pool = self._spine_window_by_day[day]
        self.spine.register_latent_crossings(state, current, pool)

        fired: list[str] = []
        pending = sorted(state.latent_spine, key=lambda mid: self.spine.threshold(mid))
        for mid in pending:
            if mid in state.fired_spine:
                state.latent_spine.discard(mid)
                continue
            if not self.spine.is_latent_ready(mid, state, current):
                continue
            if not self.spine.try_observe(mid, state, self.rng):
                continue
            fired.append(mid)
            self.spine.fire(mid, state)
            ceiling = self.spine.effective_capability_ceiling(state)
            if state.internal_capability > ceiling:
                state.internal_capability = ceiling
        return fired

    def _sample_events(
        self,
        state: WorldState,
        current: date,
        day: int,
        cluster_latents: dict[str, float] | None = None,
    ) -> list[str]:
        eligible = self.catalog.eligible_ids(state, current, self._event_window_by_day[day])
        if not eligible:
            return []

        correlation = self.correlation_model if self.use_correlations else None
        latents = cluster_latents if correlation else None

        hazards = [
            (
                eid,
                self.catalog.daily_hazard(
                    eid,
                    state,
                    current,
                    correlation=correlation,
                    cluster_latents=latents,
                ),
            )
            for eid in eligible
        ]
        hazards = [(e, h) for e, h in hazards if h > 0]
        hazards.sort(key=lambda x: x[1], reverse=True)
        hazards = hazards[: int(self.config["sim"].get("max_eligible_checks_per_day", 12))]

        fired: list[str] = []
        for eid, h in hazards:
            if len(fired) >= self.max_fires_per_day:
                break
            if self.rng.random() < h:
                fired.append(eid)
        return fired


def run_monte_carlo(config: dict[str, Any], n_runs: int, seed: int = 42) -> list[RunResult]:
    rng = np.random.default_rng(seed)
    engine = SimEngine(config=config, rng=rng)
    return [engine.run_once() for _ in range(n_runs)]
