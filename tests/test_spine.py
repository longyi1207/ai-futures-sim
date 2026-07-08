"""Spine threshold crossing tests."""

import numpy as np

from futures_sim.ci import parse_date
from futures_sim.config import load_config
from futures_sim.engine import SimEngine
from futures_sim.spine import SpineCatalog
from futures_sim.state import WorldState


def test_spine_threshold_eligibility():
    config = load_config()
    spine = SpineCatalog(config["spine"])
    state = WorldState()
    state.internal_capability = 5.5
    state.fired_spine.update({"sp_c1", "sp_c2"})

    d = parse_date("2028-01-01")
    assert spine.is_eligible("sp_c5", state, d)
    assert not spine.is_eligible("sp_c6", state, d)


def test_spine_fire_sets_ci_and_unlock():
    config = load_config()
    spine = SpineCatalog(config["spine"])
    state = WorldState()
    state.internal_capability = 5.5
    state.fired_spine.update({"sp_c1", "sp_c2"})
    spine.fire("sp_c5", state)
    assert state.ci_level >= 5.0
    assert "ev_rsi_cloud_dominant" in state.unlocked_events


def test_alignment_chain_possible():
    config = load_config()
    eng = SimEngine(config=config, rng=np.random.default_rng(99))
    state = WorldState()
    eng._apply_initial(state)
    state.internal_capability = 9.5
    for mid in ("sp_c1", "sp_c2", "sp_c5", "sp_c6", "sp_c7", "sp_c8"):
        eng.spine.fire(mid, state)
    assert "ev_c10_internal_concern" not in state.unlocked_events
    eng.spine.fire("sp_c9", state)
    assert "ev_c10_internal_concern" in state.unlocked_events
    assert eng.catalog.is_eligible("ev_c10_internal_concern", state, parse_date("2029-06-01"))
