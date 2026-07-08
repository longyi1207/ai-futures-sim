"""Spine capability ceiling tests."""

import pytest
from futures_sim.config import load_config
from futures_sim.spine import SpineCatalog
from futures_sim.state import WorldState


def test_capability_ceiling_at_next_milestone():
    spine = SpineCatalog(load_config()["spine"])
    state = WorldState()
    state.fired_spine.add("sp_c1")
    assert spine.capability_ceiling(state) == pytest.approx(2.53)
