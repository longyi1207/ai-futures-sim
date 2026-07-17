"""World state: continuous variables + discrete flags."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorldState:
    """All numeric state variables. Most are normalized [0, 1] or indexed to 2026 baseline."""

    # --- Capability & economy ---
    internal_capability: float = 0.5  # continuous latent Ci; spine = threshold observables
    ci_level: float = 0.0
    gdp_index: float = 1.0
    employment_stress: float = 0.0
    ai_rd_multiplier: float = 1.0
    tech_level: float = 0.0

    # --- Bio ---
    bio_capability_tier: float = 0.0
    bio_governance_tier: float = 0.0
    bio_risk_pressure: float = 0.0

    # --- Alignment & deployment ---
    alignment_trust: float = 0.55
    deception_risk: float = 0.15
    deployment_pressure: float = 0.35
    human_autonomy_index: float = 0.85

    # --- Governance & geopolitics ---
    governance_capacity: float = 0.50
    international_coord: float = 0.25
    compute_concentration: float = 0.70
    public_xrisk_salience: float = 0.20
    frontier_lab_polarization: float = 0.55
    frontier_capex_index: float = 1.0
    admin_ai_posture: float = 0.0
    china_frontier_parity: float = 0.25
    us_china_race_index: float = 0.30
    eu_regulatory_bind: float = 0.10
    china_open_weight_strategy: float = 0.20
    open_weights_regime: float = 0.45
    sovereignty_fragmentation: float = 0.15

    # --- Society ---
    inequality_index: float = 0.55
    meaning_institution_health: float = 0.50
    kinetic_escalation: float = 0.0
    ghost_gdp_index: float = 0.15
    labor_mobilization: float = 0.10
    reskilling_absorption: float = 0.20
    distribution_regime: float = 0.10

    # Capability dynamics controls (pause, governance friction)
    capability_growth_scale: float = 1.0
    capability_hard_ceiling: float = 11.0
    rsi_calendar_delay_days: float = 0.0
    latent_spine: set[str] = field(default_factory=set)

    fired_events: set[str] = field(default_factory=set)
    fired_spine: set[str] = field(default_factory=set)
    spine_fire_days: dict[str, int] = field(default_factory=dict)
    locked_events: set[str] = field(default_factory=set)
    unlocked_events: set[str] = field(default_factory=set)
    hazard_multipliers: dict[str, float] = field(default_factory=dict)
    event_p_overrides: dict[str, float] = field(default_factory=dict)

    terminal: str | None = None
    terminal_day: int | None = None

    def get(self, name: str) -> float:
        if not hasattr(self, name):
            raise KeyError(f"Unknown state variable: {name}")
        return float(getattr(self, name))

    def set_var(self, name: str, value: float, clamp: tuple[float, float] | None = None) -> None:
        if not hasattr(self, name):
            raise KeyError(f"Unknown state variable: {name}")
        v = float(value)
        if clamp:
            v = max(clamp[0], min(clamp[1], v))
        setattr(self, name, v)

    def apply_delta(self, name: str, delta: float, clamp: tuple[float, float] | None = None) -> None:
        self.set_var(name, self.get(name) + delta, clamp=clamp)

    def ci_int(self) -> int:
        return int(min(10, max(0, round(self.ci_level))))

    def snapshot(self) -> dict[str, Any]:
        skip = {
            "fired_events",
            "fired_spine",
            "latent_spine",
            "locked_events",
            "unlocked_events",
            "hazard_multipliers",
            "event_p_overrides",
        }
        d = {k: v for k, v in self.__dict__.items() if k not in skip}
        d["fired_events"] = sorted(self.fired_events)
        d["fired_spine"] = sorted(self.fired_spine)
        d["latent_spine"] = sorted(self.latent_spine)
        d["spine_fire_days"] = dict(sorted(self.spine_fire_days.items()))
        return d
