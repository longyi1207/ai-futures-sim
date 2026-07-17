"""Apply event effects: unlock, lock, hazard multipliers, variable deltas."""

from __future__ import annotations

from typing import Any

from .state import WorldState


def apply_effects(state: WorldState, effects: dict[str, Any] | None, event_id: str) -> None:
    if not effects:
        return

    for eid in effects.get("unlock", []):
        state.unlocked_events.add(eid)

    for eid in effects.get("lock", []):
        state.locked_events.add(eid)

    for eid, spec in (effects.get("modify_hazard") or {}).items():
        mult = float(spec.get("multiply", 1.0))
        state.hazard_multipliers[eid] = state.hazard_multipliers.get(eid, 1.0) * mult

    for name, spec in (effects.get("set_vars") or {}).items():
        clamp = tuple(spec["clamp"]) if "clamp" in spec else (0.0, 1.0) if _is_unit_var(name) else None
        state.set_var(name, float(spec["value"]), clamp=clamp)

    for name, spec in (effects.get("floor_vars") or {}).items():
        clamp = tuple(spec["clamp"]) if "clamp" in spec else (0.0, 1.0) if _is_unit_var(name) else None
        floor = float(spec["value"])
        state.set_var(name, max(state.get(name), floor), clamp=clamp)

    for name, spec in (effects.get("add_vars") or {}).items():
        clamp = tuple(spec["clamp"]) if "clamp" in spec else (0.0, 1.0) if _is_unit_var(name) else None
        state.apply_delta(name, float(spec["delta"]), clamp=clamp)

    for terminal in effects.get("force_terminal", []):
        if state.terminal is None:
            state.terminal = terminal

    ctrl = effects.get("capability_controls")
    if ctrl:
        if "growth_scale" in ctrl:
            state.capability_growth_scale *= float(ctrl["growth_scale"])
        if "growth_scale_set" in ctrl:
            state.capability_growth_scale = float(ctrl["growth_scale_set"])
        if "hard_ceiling" in ctrl:
            state.capability_hard_ceiling = min(
                state.capability_hard_ceiling,
                float(ctrl["hard_ceiling"]),
            )
        if "hard_ceiling_delta" in ctrl:
            state.capability_hard_ceiling = min(
                state.capability_hard_ceiling,
                state.internal_capability + float(ctrl["hard_ceiling_delta"]),
            )
        if "rsi_delay_days" in ctrl:
            state.rsi_calendar_delay_days += float(ctrl["rsi_delay_days"])
        if "capability_drop" in ctrl:
            # Absolute one-time reduction to internal_capability -- for physical
            # destruction of compute infrastructure (fabs, datacenters), not just a
            # growth slowdown. Growth-rate controls above (growth_scale,
            # hard_ceiling) can only cap *future* growth; nothing previously could
            # reduce capability already reached. Deliberately does NOT reduce
            # ci_level (the public observed-milestone tracker, a running max) --
            # already-trained models and know-how don't get un-invented just
            # because some fabs are destroyed; only the ability to keep advancing
            # is set back.
            state.internal_capability = max(0.0, state.internal_capability - float(ctrl["capability_drop"]))


def _is_unit_var(name: str) -> bool:
    return name not in {
        "gdp_index",
        "ai_rd_multiplier",
        "ci_level",
        "internal_capability",
        "bio_capability_tier",
        "bio_governance_tier",
        "frontier_capex_index",
        "admin_ai_posture",
    }
