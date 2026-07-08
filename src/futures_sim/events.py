"""Event eligibility and daily hazard sampling."""

from __future__ import annotations

from datetime import date
from typing import Any

import numpy as np

from .ci import parse_date
from .correlations import CorrelationModel
from .effects import apply_effects
from .society_hazards import society_hazard_multiplier


def cumulative_to_daily_hazard(p_cumulative: float, days_remaining: int) -> float:
    """Convert once-per-window cumulative P to constant daily hazard for remaining days."""
    if days_remaining <= 0:
        return 0.0
    p = float(np.clip(p_cumulative, 0.0, 1.0))
    if p <= 0.0:
        return 0.0
    if p >= 1.0:
        return 1.0
    return 1.0 - (1.0 - p) ** (1.0 / days_remaining)


class EventCatalog:
    def __init__(self, events_doc: dict[str, Any], society_hazards: dict[str, Any] | None = None):
        self.events: dict[str, dict] = {e["id"]: e for e in events_doc["events"]}
        self.mutex_groups: dict[str, list[str]] = events_doc.get("mutex_groups", {})
        self.society_hazards = society_hazards
        self._parsed: dict[str, tuple[date, date]] = {}
        for eid, ev in self.events.items():
            sched = ev.get("schedule", {})
            start = parse_date(sched.get("start", "2026-01-01"))
            end = parse_date(sched.get("end", "2050-01-01"))
            self._parsed[eid] = (start, end)

    def in_window(self, event_id: str, current: date) -> bool:
        start, end = self._parsed[event_id]
        return start <= current <= end

    def is_eligible(self, event_id: str, state: WorldState, current: date) -> bool:
        if not self.in_window(event_id, current):
            return False
        ev = self.events[event_id]
        if state.terminal:
            return False
        if event_id in state.fired_events and ev.get("once", True):
            return False
        if event_id in state.locked_events:
            return False
        if ev.get("requires_unlock") and event_id not in state.unlocked_events:
            return False

        pre = ev.get("preconditions", {})
        if state.ci_int() < int(pre.get("ci_min", 0)):
            return False
        for var, bounds in (pre.get("vars") or {}).items():
            lo, hi = bounds
            v = state.get(var)
            if v < lo or v > hi:
                return False
        for req in pre.get("events_fired", []):
            if req not in state.fired_events:
                return False
        for forbidden in pre.get("events_not_fired", []):
            if forbidden in state.fired_events:
                return False
        for req in pre.get("spine_fired", []):
            if req not in state.fired_spine:
                return False
        for forbidden in pre.get("spine_not_fired", []):
            if forbidden in state.fired_spine:
                return False
        return True

    def daily_hazard(
        self,
        event_id: str,
        state: WorldState,
        current: date,
        *,
        correlation: CorrelationModel | None = None,
        cluster_latents: dict[str, float] | None = None,
    ) -> float:
        ev = self.events[event_id]
        sched = ev.get("schedule", {})
        start, end = self._parsed[event_id]
        if "daily_hazard" in sched:
            base = float(sched["daily_hazard"])
        else:
            p_cum = float(sched.get("p_cumulative", 0.0))
            total_days = max(1, (end - start).days + 1)
            # Constant daily hazard over the full window — do NOT re-scale p_cumulative
            # against shrinking remaining days (that inflates marginal P toward 1).
            base = cumulative_to_daily_hazard(p_cum, total_days)

        mult = state.hazard_multipliers.get(event_id, 1.0)
        mult *= society_hazard_multiplier(event_id, state, self.society_hazards)
        base = float(np.clip(base * mult, 0.0, 1.0))
        if correlation and cluster_latents is not None:
            base = correlation.adjust_hazard(event_id, base, cluster_latents)
        return base

    def fire(self, event_id: str, state: WorldState) -> None:
        ev = self.events[event_id]
        state.fired_events.add(event_id)
        group = ev.get("mutex_group")
        if group and group in self.mutex_groups:
            for other in self.mutex_groups[group]:
                if other != event_id:
                    state.locked_events.add(other)
        apply_effects(state, ev.get("on_fire"), event_id)

    def eligible_ids(self, state: WorldState, current: date, window_pool: list[str] | None = None) -> list[str]:
        pool = window_pool if window_pool is not None else self.events
        return [eid for eid in pool if self.is_eligible(eid, state, current)]
