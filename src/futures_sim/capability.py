"""Continuous internal capability dynamics + calendar RSI (Model 2)."""

from __future__ import annotations

from datetime import date
from typing import Any

import numpy as np

from .ci import parse_date
from .state import WorldState


def parse_calendar_rsi_anchors(
    cal_doc: dict[str, Any] | None,
    sim_start: date,
) -> list[tuple[int, float]]:
    """Parse calendar RSI knot points to (day_offset, multiplier)."""
    if not cal_doc:
        return [(0, 1.15)]
    parsed: list[tuple[int, float]] = []
    for knot in cal_doc.get("anchors", []):
        d = parse_date(knot["date"])
        parsed.append(((d - sim_start).days, float(knot["multiplier"])))
    parsed.sort(key=lambda x: x[0])
    return parsed


def calendar_rsi_multiplier(day: int, anchors: list[tuple[int, float]]) -> float:
    """Piecewise-linear internal R&D multiplier vs sim day (AI 2027 plot curve)."""
    if not anchors:
        return 1.0
    if day <= anchors[0][0]:
        return anchors[0][1]
    for i in range(len(anchors) - 1):
        d0, m0 = anchors[i]
        d1, m1 = anchors[i + 1]
        if d0 <= day <= d1:
            if d1 <= d0:
                return m1
            t = (day - d0) / (d1 - d0)
            return m0 + t * (m1 - m0)
    return anchors[-1][1]


def _input_factor(state: WorldState, name: str, spec: dict[str, Any]) -> float:
    ref = float(spec.get("reference", 1.0))
    scale = float(spec.get("scale", 0.0))
    val = state.get(name)
    if ref > 0:
        return 1.0 + scale * max(0.0, val / ref - 1.0)
    return 1.0 + scale * val


def _apply_macro_couplings(state: WorldState, dyn: dict[str, Any]) -> None:
    gdp_capex = dyn.get("gdp_capex_coupling") or {}
    pull = float(gdp_capex.get("daily_pull", 0.0))
    if pull > 0:
        state.apply_delta(
            "frontier_capex_index",
            pull * (state.gdp_index - state.frontier_capex_index),
            clamp=(0.5, 3.0),
        )

    admin = dyn.get("admin_ai_posture") or {}
    admin_val = max(0.0, state.admin_ai_posture)
    capex_daily = float(admin.get("daily_capex", 0.0))
    if capex_daily > 0 and admin_val > 0:
        state.apply_delta("frontier_capex_index", capex_daily * admin_val, clamp=(0.5, 3.0))
    gov_daily = float(admin.get("daily_governance", 0.0))
    if gov_daily > 0 and admin_val > 0:
        state.apply_delta("governance_capacity", gov_daily * admin_val, clamp=(0.0, 1.0))

    kin = dyn.get("kinetic_escalation") or {}
    k = state.kinetic_escalation
    if k > 0:
        state.apply_delta(
            "international_coord",
            -float(kin.get("daily_coord_erosion", 0.0)) * k,
            clamp=(0.0, 1.0),
        )
        state.apply_delta(
            "frontier_capex_index",
            -float(kin.get("daily_capex_penalty", 0.0)) * k,
            clamp=(0.5, 3.0),
        )


def _growth_factor(state: WorldState, dyn: dict[str, Any]) -> float:
    factor = 1.0
    for name, spec in (dyn.get("inputs") or {}).items():
        factor *= _input_factor(state, name, spec)

    gdp = dyn.get("gdp_funding") or {}
    gdp_ref = float(gdp.get("reference", 1.0))
    factor *= 1.0 + float(gdp.get("scale", 0.0)) * max(0.0, state.gdp_index / gdp_ref - 1.0)

    race = dyn.get("race_amplification") or {}
    race_scale = float(race.get("scale", 0.0))
    race_term = race_scale * state.deployment_pressure * (1.0 - state.governance_capacity)
    factor *= 1.0 + max(0.0, race_term)

    gov_brake = dyn.get("governance_brake") or {}
    g_scale = float(gov_brake.get("governance_scale", 0.0))
    s_scale = float(gov_brake.get("salience_scale", 0.0))
    brake = 1.0 - g_scale * state.governance_capacity - s_scale * state.public_xrisk_salience
    factor *= max(0.55, brake)

    tg = dyn.get("trust_governance_brake") or {}
    factor *= max(0.72, 1.0 - float(tg.get("scale", 0.0)) * state.alignment_trust * state.governance_capacity)

    secret = dyn.get("secret_race_boost") or {}
    factor *= 1.0 + float(secret.get("scale", 0.0)) * (1.0 - state.alignment_trust) * state.deployment_pressure

    coord_brake = dyn.get("coordination_brake") or {}
    factor *= max(0.75, 1.0 - float(coord_brake.get("scale", 0.0)) * state.international_coord)

    frag = dyn.get("sovereignty_fragmentation") or {}
    dispersion = state.sovereignty_fragmentation * (1.0 - state.compute_concentration)
    factor *= max(0.78, 1.0 - float(frag.get("scale", 0.0)) * dispersion)

    admin = dyn.get("admin_ai_posture") or {}
    factor *= 1.0 + float(admin.get("growth_scale", 0.0)) * max(0.0, state.admin_ai_posture)

    kin = dyn.get("kinetic_escalation") or {}
    factor *= max(0.82, 1.0 - float(kin.get("growth_penalty", 0.0)) * state.kinetic_escalation)

    bio = dyn.get("bio_spillover") or {}
    factor *= 1.0 + float(bio.get("bio_to_cap_scale", 0.0)) * state.bio_capability_tier

    return factor


def _apply_bio_spillover(state: WorldState, cap: float, dyn: dict[str, Any]) -> None:
    bio = dyn.get("bio_spillover") or {}
    threshold = float(bio.get("cap_to_bio_threshold", 3.0))
    if cap < threshold:
        return
    daily = float(bio.get("cap_to_bio_daily", 0.0))
    if daily > 0:
        state.apply_delta("bio_capability_tier", daily * min(cap, 10.0), clamp=(0.0, 5.0))
    pressure = float(bio.get("cap_to_bio_risk_daily", 0.0))
    if pressure > 0:
        state.apply_delta(
            "bio_risk_pressure",
            pressure * min(cap, 10.0) * max(0.0, 1.0 - state.bio_governance_tier),
            clamp=(0.0, 1.0),
        )


def step_capability(
    state: WorldState,
    rng: np.random.Generator,
    dyn: dict[str, Any],
    *,
    day: int = 0,
    rsi_anchors: list[tuple[int, float]] | None = None,
) -> float:
    """Advance internal_capability one day; sync ai_rd_multiplier from calendar RSI."""
    _apply_macro_couplings(state, dyn)

    anchors = rsi_anchors or []
    cal_m = calendar_rsi_multiplier(day, anchors)
    state.ai_rd_multiplier = max(state.ai_rd_multiplier, cal_m)

    base = float(dyn.get("base_daily_growth", 0.002))
    alpha = float(dyn.get("multiplier_exponent", 1.0))
    k_carry = float(dyn.get("carrying_capacity", 11.0))
    m = min(max(1.0, state.ai_rd_multiplier), float(dyn.get("max_multiplier_in_growth", 55.0)))

    cap_before = state.internal_capability
    factor = _growth_factor(state, dyn)
    saturation = max(0.02, 1.0 - cap_before / k_carry)
    growth = base * (m**alpha) * factor * saturation * state.capability_growth_scale

    shock_cfg = dyn.get("shock") or {}
    if float(shock_cfg.get("prob", 0)) > 0 and rng.random() < float(shock_cfg["prob"]):
        growth *= float(np.exp(rng.normal(0.0, float(shock_cfg.get("log_std", 0.25)))))

    hard_cap = min(k_carry, state.capability_hard_ceiling)
    state.internal_capability = min(hard_cap, cap_before + growth)

    lag = float(dyn.get("tech_deploy_lag", 0.35))
    state.apply_delta("tech_level", lag * growth, clamp=(0.0, 1.0))

    emp = dyn.get("employment_coupling") or {}
    if state.internal_capability >= float(emp.get("capability_threshold", 4.0)):
        state.apply_delta("employment_stress", float(emp.get("daily_stress", 0.00025)), clamp=(0.0, 1.0))
        state.apply_delta("ghost_gdp_index", float(emp.get("daily_ghost_gdp", 0.00015)), clamp=(0.0, 1.0))

    align = dyn.get("alignment_coupling") or {}
    if (
        state.deployment_pressure > float(align.get("deployment_threshold", 0.7))
        and state.alignment_trust < float(align.get("trust_ceiling", 0.35))
    ):
        state.apply_delta("deception_risk", float(align.get("daily_deception", 0.0002)), clamp=(0.0, 1.0))

    _apply_bio_spillover(state, state.internal_capability, dyn)

    state.ci_level = max(state.ci_level, min(10.0, state.internal_capability))
    return growth
