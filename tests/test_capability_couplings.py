"""Coupling tests for capability dynamics."""

import numpy as np

from futures_sim.capability import step_capability
from futures_sim.config import load_config
from futures_sim.state import WorldState


def _growth_with(state: WorldState, rng: np.random.Generator, dyn: dict, day: int = 600) -> float:
    before = state.internal_capability
    step_capability(state, rng, dyn, day=day)
    return state.internal_capability - before


def test_gdp_funding_increases_growth():
    dyn = load_config()["capability_dynamics"]
    rng = np.random.default_rng(0)
    low = WorldState()
    low.internal_capability = 2.0
    low.gdp_index = 1.0
    high = WorldState()
    high.internal_capability = 2.0
    high.gdp_index = 1.25
    assert _growth_with(high, rng, dyn) > _growth_with(low, rng, dyn)


def test_trust_governance_brake_slows_growth():
    dyn = load_config()["capability_dynamics"]
    rng = np.random.default_rng(1)
    cautious = WorldState()
    cautious.internal_capability = 3.0
    cautious.alignment_trust = 0.85
    cautious.governance_capacity = 0.80
    reckless = WorldState()
    reckless.internal_capability = 3.0
    reckless.alignment_trust = 0.35
    reckless.governance_capacity = 0.25
    assert _growth_with(reckless, rng, dyn) > _growth_with(cautious, rng, dyn)


def test_sovereignty_fragmentation_penalty():
    dyn = load_config()["capability_dynamics"]
    rng = np.random.default_rng(2)
    concentrated = WorldState()
    concentrated.internal_capability = 3.0
    concentrated.sovereignty_fragmentation = 0.10
    concentrated.compute_concentration = 0.85
    fragmented = WorldState()
    fragmented.internal_capability = 3.0
    fragmented.sovereignty_fragmentation = 0.55
    fragmented.compute_concentration = 0.35
    assert _growth_with(concentrated, rng, dyn) > _growth_with(fragmented, rng, dyn)


def test_bio_spillover_raises_bio_tier():
    dyn = load_config()["capability_dynamics"]
    state = WorldState()
    state.internal_capability = 4.0
    state.bio_capability_tier = 0.1
    rng = np.random.default_rng(3)
    for day in range(500):
        step_capability(state, rng, dyn, day=day)
    assert state.bio_capability_tier > 0.15
