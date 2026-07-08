"""Continuous capability dynamics tests."""

import numpy as np

from futures_sim.capability import calendar_rsi_multiplier, parse_calendar_rsi_anchors, step_capability
from futures_sim.ci import parse_date
from futures_sim.config import load_config
from futures_sim.state import WorldState


def test_capability_grows_with_multiplier():
    dyn = load_config()["capability_dynamics"]
    rng = np.random.default_rng(0)
    low = WorldState()
    low.internal_capability = 2.0
    low.ai_rd_multiplier = 1.5
    high = WorldState()
    high.internal_capability = 2.0
    high.ai_rd_multiplier = 5.0

    g_low = step_capability(low, rng, dyn, day=400)
    g_high = step_capability(high, rng, dyn, day=400)
    assert g_high > g_low


def test_calendar_rsi_linear_between_anchors():
    anchors = [
        (0, 1.15),
        (365, 1.5),
        (730, 3.0),
    ]
    assert calendar_rsi_multiplier(0, anchors) == 1.15
    mid = calendar_rsi_multiplier(182, anchors)
    assert 1.15 < mid < 1.5
    assert calendar_rsi_multiplier(365, anchors) == 1.5


def test_calendar_rsi_parsed_from_config():
    dyn = load_config()["capability_dynamics"]
    anchors = parse_calendar_rsi_anchors(dyn["calendar_rsi"], parse_date("2026-01-01"))
    assert anchors[0] == (0, 1.13)
    assert calendar_rsi_multiplier(0, anchors) == 1.13


def test_capability_step_uses_calendar_rsi():
    dyn = load_config()["capability_dynamics"]
    start = parse_date("2026-01-01")
    anchors = parse_calendar_rsi_anchors(dyn["calendar_rsi"], start)
    state = WorldState()
    state.internal_capability = 0.5
    rng = np.random.default_rng(1)
    for day in range(2000):
        step_capability(state, rng, dyn, day=day, rsi_anchors=anchors)
    assert state.ai_rd_multiplier >= 1.5
    assert state.internal_capability > 1.0
