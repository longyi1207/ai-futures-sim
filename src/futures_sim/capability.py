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
        excess = val / ref - 1.0
        # Default is excess-only (bonus above reference, no penalty below) --
        # correct for most of these inputs, where we have no evidence a shortfall
        # below baseline should actively drag growth rather than just withhold a
        # bonus. `symmetric: true` opts a specific input out of that floor when
        # there's a direct evidentiary case for a two-sided effect (see
        # frontier_lab_polarization in capability_dynamics.yaml for the one
        # current instance and its citations).
        if not spec.get("symmetric", False):
            excess = max(0.0, excess)
        return 1.0 + scale * excess
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

    # Added 2026-07-16: kinetic_escalation previously had NO decay -- once any
    # kinetic event fired, tension stayed at its peak value for the rest of the
    # simulation (potentially 20+ years), permanently dragging capability growth
    # and (via gdp_growth_coupling) GDP growth. Real great-power tension cycles up
    # and down over years-to-decades (Cold War thaws/re-freezes are the standard
    # reference case), it doesn't monotonically ratchet. Exponential relaxation
    # toward a residual floor (0.08, matching the 2026 initial value -- tension
    # doesn't fully return to a pre-conflict baseline). [GUESS] on the decay rate
    # (0.0003/day => ~6yr half-life): no natural experiment exists for "AI-era
    # great-power tension half-life" specifically.
    decay = float(kin.get("daily_decay", 0.0))
    floor = float(kin.get("decay_floor", 0.08))
    if decay > 0 and k > floor:
        state.apply_delta("kinetic_escalation", -decay * (k - floor), clamp=(0.0, 1.0))


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
    delayed_day = max(0, day - int(round(state.rsi_calendar_delay_days)))
    cal_m = calendar_rsi_multiplier(delayed_day, anchors)
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
        # Stock-flow, not a one-way ratchet: displacement flows in continuously,
        # absorption/redistribution flows out continuously (scaled by the same
        # reskilling_absorption/distribution_regime variables the event graph
        # already moves), rather than only offsetting via one-off event deltas
        # (e.g. ev_fed_edu_reskilling's one-time -0.12). Before this, 84% of runs
        # (n=500) saturated employment_stress AND ghost_gdp_index at exactly 1.0
        # regardless of outcome -- the one-time nudges couldn't keep up with 15-20+
        # years of continuous inflow, so these variables carried almost no
        # discriminating information between "well-managed" and "unmanaged"
        # transitions.
        stress_in = float(emp.get("daily_stress", 0.00028))
        stress_absorb_scale = float(emp.get("daily_stress_absorption_scale", 0.0))
        state.apply_delta(
            "employment_stress",
            stress_in - stress_absorb_scale * state.reskilling_absorption,
            clamp=(0.0, 1.0),
        )

        ghost_in = float(emp.get("daily_ghost_gdp", 0.00018))
        ghost_absorb_scale = float(emp.get("daily_ghost_gdp_absorption_scale", 0.0))
        state.apply_delta(
            "ghost_gdp_index",
            ghost_in - ghost_absorb_scale * state.distribution_regime,
            clamp=(0.0, 1.0),
        )

        # inequality_index had the same bug as gdp_index originally did: no
        # continuous coupling at all, only a handful of discrete event deltas
        # (max observed ceiling ~0.62 across 800 runs) -- meaning it could never
        # reach genuinely high concentration levels regardless of outcome. This is
        # the same real-world mechanism as ghost_gdp_index (compute/capital rents
        # accruing to owners rather than being broadly shared -- research:
        # node_u2_distribution_evidence_rationale.md "P=0.73 -- top decile
        # captures >=60% of AI-attributed surplus", explicitly a *continuous*
        # concentration process, not a one-off event), so it gets the same
        # stock-flow treatment: concentration flows in with capability, offset by
        # active distribution policy.
        ineq_in = float(emp.get("daily_inequality_concentration", 0.0))
        ineq_absorb_scale = float(emp.get("daily_inequality_absorption_scale", 0.0))
        state.apply_delta(
            "inequality_index",
            ineq_in - ineq_absorb_scale * state.distribution_regime,
            clamp=(0.0, 1.0),
        )

    # human_autonomy_index had the same missing-mechanism bug as gdp_index/
    # inequality_index/employment_stress originally did: only discrete event
    # deltas, no continuous drift -- empirically never dropped below ~0.53 across
    # 800 runs. This silently made 3 of doom_whimper's 4 horizon_default paths
    # (needing autonomy <=0.32/0.40/0.48) structurally unreachable, collapsing
    # doom_whimper from ~15% (documented blog headline) to ~1.5-1.8% with no
    # terminal-reachability test catching it (autonomy staying high isn't
    # "impossible" the way gdp_index<1.45 was, just empirically never observed).
    # This is exactly the mechanism Christiano's "What Failure Looks Like" (cited
    # in the blog post as the friction/whimper reference case) describes: gradual
    # loss of human oversight as deployment outpaces trustworthy alignment, offset
    # by institutions actively maintaining control. Not gated behind a capability
    # threshold like the others -- scaled continuously by tech_level instead, so
    # it activates gracefully as deployment ramps up rather than switching on at a
    # fixed point.
    auto = dyn.get("autonomy_erosion") or {}
    erosion_scale = float(auto.get("daily_erosion_scale", 0.0))
    protection_scale = float(auto.get("daily_protection_scale", 0.0))
    erosion = erosion_scale * state.tech_level * state.deployment_pressure * (1.0 - state.alignment_trust)
    protection = protection_scale * state.tech_level * state.governance_capacity
    state.apply_delta("human_autonomy_index", protection - erosion, clamp=(0.0, 1.0))

    gdp = dyn.get("gdp_growth_coupling") or {}
    baseline_annual = float(gdp.get("baseline_annual_growth", 0.022))
    accel_scale = float(gdp.get("tech_level_accel_scale", 0.0))

    kinetic_drag_scale = float(gdp.get("kinetic_drag_scale", 0.0))
    gov_drag_scale = float(gdp.get("governance_collapse_drag_scale", 0.0))
    gov_drag_ref = float(gdp.get("governance_collapse_reference", 0.5))
    frag_drag_scale = float(gdp.get("fragmentation_drag_scale", 0.0))

    governance_deficit = max(0.0, gov_drag_ref - state.governance_capacity) / max(1e-6, gov_drag_ref)

    annual_rate = (
        baseline_annual
        + accel_scale * state.tech_level
        - kinetic_drag_scale * state.kinetic_escalation
        - gov_drag_scale * governance_deficit
        - frag_drag_scale * state.sovereignty_fragmentation
    )
    daily_rate = (1.0 + annual_rate) ** (1.0 / 365.0) - 1.0
    state.set_var("gdp_index", state.gdp_index * (1.0 + daily_rate), clamp=(0.15, 10.0))

    align = dyn.get("alignment_coupling") or {}
    if (
        state.deployment_pressure > float(align.get("deployment_threshold", 0.7))
        and state.alignment_trust < float(align.get("trust_ceiling", 0.35))
    ):
        state.apply_delta("deception_risk", float(align.get("daily_deception", 0.0002)), clamp=(0.0, 1.0))

    _apply_bio_spillover(state, state.internal_capability, dyn)

    state.ci_level = max(state.ci_level, min(10.0, state.internal_capability))
    return growth
