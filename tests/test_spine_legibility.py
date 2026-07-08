"""Spine legibility and capability control tests."""

import numpy as np

from futures_sim.ci import parse_date
from futures_sim.config import load_config
from futures_sim.effects import apply_effects
from futures_sim.engine import SimEngine
from futures_sim.spine import SpineCatalog
from futures_sim.state import WorldState


def test_latent_crossing_not_immediate_fire():
    config = load_config()
    eng = SimEngine(config=config, rng=np.random.default_rng(0))
    state = WorldState()
    eng._apply_initial(state)
    state.internal_capability = 1.20
    current = parse_date("2026-06-01")
    eng.spine.register_latent_crossings(state, current, ["sp_c1"])
    assert "sp_c1" in state.latent_spine
    assert "sp_c1" not in state.fired_spine


def test_legibility_hazard_reduced_under_pause():
    config = load_config()
    spine = SpineCatalog(config["spine"])
    state = WorldState()
    state.fired_events.add("ev_federal_pause_succeeds")
    h = spine.legibility_daily_hazard("sp_c5", state)
    base = spine.legibility_daily_hazard("sp_c5", WorldState())
    assert h < base


def test_capability_controls_pause():
    state = WorldState()
    state.internal_capability = 6.0
    state.capability_hard_ceiling = 11.0
    apply_effects(
        state,
        {"capability_controls": {"growth_scale": 0.2, "hard_ceiling": 7.2}},
        "test",
    )
    assert state.capability_growth_scale == 0.2
    assert state.capability_hard_ceiling == 7.2


def test_prod_interp_halt_slows_growth():
    state = WorldState()
    state.capability_growth_scale = 1.0
    apply_effects(
        state,
        {"capability_controls": {"growth_scale": 0.78}},
        "ev_prod_interp_halt",
    )
    assert state.capability_growth_scale == 0.78


def test_spine_not_always_full_chain():
    config = load_config()
    eng = SimEngine(config=config, rng=np.random.default_rng(7))
    results = [eng.run_once() for _ in range(80)]
    full = sum(1 for r in results if "sp_c9" in r.fired_spine)
    assert full < 80
