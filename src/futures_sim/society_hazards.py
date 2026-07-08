"""Society state variables → event hazard multipliers."""

from __future__ import annotations

from typing import Any

import numpy as np

from .state import WorldState


def _apply_spec(mult: float, event_id: str, state: WorldState, spec: dict[str, Any]) -> float:
    events = spec.get("events") or {}
    if event_id not in events:
        return mult
    scale = float(events[event_id].get("scale", 0.0))
    if scale == 0.0:
        return mult

    val = state.get(spec["_var_name"])
    ref = float(spec.get("reference", 0.5))
    mode = spec.get("mode", "excess")

    if mode == "deficit":
        excess = max(0.0, ref - val)
    else:
        excess = max(0.0, val - ref)

    return mult * (1.0 + scale * excess)


def society_hazard_multiplier(
    event_id: str,
    state: WorldState,
    society_doc: dict[str, Any] | None,
) -> float:
    """Scale daily hazard from society / governance / deployment state."""
    if not society_doc:
        return 1.0

    mult = 1.0
    for var_name, raw_spec in society_doc.items():
        specs = raw_spec if isinstance(raw_spec, list) else [raw_spec]
        for spec in specs:
            spec = dict(spec)
            spec["_var_name"] = var_name
            mult = _apply_spec(mult, event_id, state, spec)

    return float(np.clip(mult, 0.35, 3.0))
