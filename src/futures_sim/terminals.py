"""Terminal outcome checks (doom, utopia, friction)."""

from __future__ import annotations

from typing import Any

from .state import WorldState


def check_terminals(state: WorldState, terminals_doc: dict[str, Any]) -> str | None:
    if state.terminal:
        return state.terminal

    # Forced extinction paths from catastrophic events
    for rule in terminals_doc.get("event_forced", []):
        if rule["event"] in state.fired_events:
            return rule["terminal"]

    for tid, spec in terminals_doc.get("terminals", {}).items():
        if spec.get("horizon_only"):
            continue
        if _conditions_met(state, spec.get("conditions", {})):
            return tid

    return None


def classify_region(terminal_id: str, terminals_doc: dict[str, Any]) -> str:
    t = terminals_doc["terminals"][terminal_id]
    return t["region"]  # doom | utopia | friction | severe


def _conditions_met(state: WorldState, cond: dict) -> bool:
    vars_req = cond.get("vars", {})
    for name, bounds in vars_req.items():
        lo, hi = bounds
        v = state.get(name)
        if v < lo or v > hi:
            return False

    for eid in cond.get("events_all", []):
        if eid not in state.fired_events:
            return False
    if "events_any" in cond:
        if not any(e in state.fired_events for e in cond["events_any"]):
            return False

    for mid in cond.get("spine_not_fired", []):
        if mid in state.fired_spine:
            return False
    if "spine_any_fired" in cond:
        if not any(m in state.fired_spine for m in cond["spine_any_fired"]):
            return False

    return True


def default_terminal_at_horizon(state: WorldState, terminals_doc: dict[str, Any]) -> str:
    """If sim reaches end date without absorbing, assign friction subtype."""
    rules = terminals_doc.get("horizon_default", [])
    for rule in rules:
        if _conditions_met(state, rule.get("conditions", {})):
            return rule["terminal"]
    return terminals_doc.get("default_horizon_terminal", "friction_modal")
