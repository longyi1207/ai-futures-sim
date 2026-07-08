"""Probabilistic AI-2027 capability spine milestones."""

from __future__ import annotations

from datetime import date
from typing import Any

import numpy as np

from .ci import parse_date
from .effects import apply_effects
from .state import WorldState


class SpineCatalog:
    def __init__(self, spine_doc: dict[str, Any]):
        self.milestones: dict[str, dict] = {m["id"]: m for m in spine_doc["milestones"]}
        self.obs_defaults: dict[str, Any] = spine_doc.get("observability_defaults", {})
        self._parsed: dict[str, tuple[date, date]] = {}
        for mid, ms in self.milestones.items():
            sched = ms.get("schedule", {})
            start = parse_date(sched.get("start", "2026-01-01"))
            end = parse_date(sched.get("end", "2050-01-01"))
            self._parsed[mid] = (start, end)

    def in_window(self, milestone_id: str, current: date) -> bool:
        start, end = self._parsed[milestone_id]
        return start <= current <= end

    def threshold(self, milestone_id: str) -> float:
        return float(self.milestones[milestone_id]["threshold"])

    def is_latent_ready(self, milestone_id: str, state: WorldState, current: date) -> bool:
        """Latent capability reached threshold; public observation may still be pending."""
        if not self.in_window(milestone_id, current):
            return False
        ms = self.milestones[milestone_id]
        if state.terminal:
            return False
        if milestone_id in state.fired_spine and ms.get("once", True):
            return False
        if state.internal_capability < self.threshold(milestone_id):
            return False

        pre = ms.get("preconditions", {})
        for var, bounds in (pre.get("vars") or {}).items():
            lo, hi = bounds
            v = state.get(var)
            if v < lo or v > hi:
                return False
        for req in pre.get("spine_fired", []):
            if req not in state.fired_spine:
                return False
        for forbidden in pre.get("spine_not_fired", []):
            if forbidden in state.fired_spine:
                return False
        for req in pre.get("events_fired", []):
            if req not in state.fired_events:
                return False
        for forbidden in pre.get("events_not_fired", []):
            if forbidden in state.fired_events:
                return False
        return True

    def is_eligible(self, milestone_id: str, state: WorldState, current: date) -> bool:
        return self.is_latent_ready(milestone_id, state, current)

    def register_latent_crossings(
        self,
        state: WorldState,
        current: date,
        window_pool: list[str] | None = None,
    ) -> None:
        pool = window_pool if window_pool is not None else self.milestones
        for mid in pool:
            if mid in state.fired_spine:
                continue
            if self.is_latent_ready(mid, state, current):
                state.latent_spine.add(mid)

    def legibility_daily_hazard(self, milestone_id: str, state: WorldState) -> float:
        """P(publicly recording this milestone today | latent threshold already met)."""
        ms = self.milestones[milestone_id]
        obs = ms.get("observability") or {}
        base = float(obs.get("daily_hazard", self.obs_defaults.get("daily_hazard", 0.015)))

        gov_boost = float(self.obs_defaults.get("governance_boost", 0.22))
        factor = 1.0 + gov_boost * state.governance_capacity

        deception_penalty = float(self.obs_defaults.get("deception_penalty", 0.35))
        factor *= max(0.35, 1.0 - deception_penalty * state.deception_risk)

        salience_boost = float(self.obs_defaults.get("salience_boost", 0.18))
        factor *= 1.0 + salience_boost * state.public_xrisk_salience

        if "ev_federal_pause_succeeds" in state.fired_events:
            factor *= float(self.obs_defaults.get("pause_legibility_scale", 0.42))
        if "ev_us_paralysis_s2" in state.fired_events:
            factor *= float(self.obs_defaults.get("paralysis_legibility_scale", 0.75))

        for eid in obs.get("requires_events", []):
            if eid not in state.fired_events:
                return 0.0
        for eid in obs.get("blocks_if_fired", []):
            if eid in state.fired_events:
                return 0.0

        return float(np.clip(base * factor, 0.0, 0.35))

    def try_observe(self, milestone_id: str, state: WorldState, rng: np.random.Generator) -> bool:
        h = self.legibility_daily_hazard(milestone_id, state)
        return h > 0 and rng.random() < h

    def fire(self, milestone_id: str, state: WorldState) -> None:
        ms = self.milestones[milestone_id]
        state.fired_spine.add(milestone_id)
        state.latent_spine.discard(milestone_id)
        ci = float(ms.get("ci_level", state.internal_capability))
        state.ci_level = max(state.ci_level, ci)
        apply_effects(state, ms.get("on_fire"), milestone_id)

    def threshold_crossed_ids(
        self,
        state: WorldState,
        current: date,
        window_pool: list[str] | None = None,
    ) -> list[str]:
        pool = window_pool if window_pool is not None else self.milestones
        eligible = [mid for mid in pool if self.is_latent_ready(mid, state, current)]
        eligible.sort(key=lambda mid: self.threshold(mid))
        return eligible

    def capability_ceiling(self, state: WorldState) -> float:
        order = sorted(self.milestones.keys(), key=lambda mid: self.threshold(mid))
        chain_ceiling = 11.0
        for mid in order:
            if mid in state.fired_spine:
                continue
            ms = self.milestones[mid]
            pre = ms.get("preconditions", {})
            for req in pre.get("spine_fired", []):
                if req not in state.fired_spine:
                    return max(0.5, self.threshold(mid) - 0.12)
            return min(chain_ceiling, self.threshold(mid) + 0.38)
        return chain_ceiling

    def effective_capability_ceiling(self, state: WorldState) -> float:
        return min(self.capability_ceiling(state), state.capability_hard_ceiling)

    def eligible_ids(self, state: WorldState, current: date, window_pool: list[str] | None = None) -> list[str]:
        return self.threshold_crossed_ids(state, current, window_pool)
