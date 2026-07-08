"""Terminal horizon_only flag."""

from futures_sim.config import load_config
from futures_sim.state import WorldState
from futures_sim.terminals import check_terminals


def test_friction_modal_not_absorbed_mid_sim():
    config = load_config()
    state = WorldState()
    state.employment_stress = 0.55
    state.inequality_index = 0.6
    state.human_autonomy_index = 0.5
    assert check_terminals(state, config["terminals"]) is None
