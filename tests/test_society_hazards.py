"""Society variable → event hazard coupling tests."""

from datetime import date

from futures_sim.config import load_config
from futures_sim.events import EventCatalog
from futures_sim.society_hazards import society_hazard_multiplier
from futures_sim.state import WorldState


def test_inequality_boosts_labor_shock_hazard():
    doc = load_config()["society_hazards"]
    low = WorldState()
    low.inequality_index = 0.54
    high = WorldState()
    high.inequality_index = 0.75
    assert society_hazard_multiplier("ev_c4_labor_shock", high, doc) > society_hazard_multiplier(
        "ev_c4_labor_shock", low, doc
    )


def test_low_autonomy_boosts_doom_chain():
    doc = load_config()["society_hazards"]
    healthy = WorldState()
    healthy.human_autonomy_index = 0.88
    weak = WorldState()
    weak.human_autonomy_index = 0.45
    assert society_hazard_multiplier("ev_deceptive_deploy_at_scale", weak, doc) > society_hazard_multiplier(
        "ev_deceptive_deploy_at_scale", healthy, doc
    )


def test_catalog_applies_society_multiplier():
    config = load_config()
    catalog = EventCatalog(config["events"], society_hazards=config["society_hazards"])
    low = WorldState()
    low.inequality_index = 0.54
    high = WorldState()
    high.inequality_index = 0.80
    d = date(2027, 6, 1)
    assert catalog.daily_hazard("ev_c4_labor_shock", high, d) > catalog.daily_hazard(
        "ev_c4_labor_shock", low, d
    )


def test_high_trust_reduces_deceptive_deploy_hazard():
    doc = load_config()["society_hazards"]
    low_trust = WorldState()
    low_trust.alignment_trust = 0.55
    high_trust = WorldState()
    high_trust.alignment_trust = 0.82
    assert society_hazard_multiplier("ev_deceptive_deploy_at_scale", high_trust, doc) < (
        society_hazard_multiplier("ev_deceptive_deploy_at_scale", low_trust, doc)
    )


def test_low_governance_boosts_paralysis_hazard():
    doc = load_config()["society_hazards"]
    strong = WorldState()
    strong.governance_capacity = 0.65
    weak = WorldState()
    weak.governance_capacity = 0.30
    assert society_hazard_multiplier("ev_us_paralysis_s2", weak, doc) > society_hazard_multiplier(
        "ev_us_paralysis_s2", strong, doc
    )


def test_c4_requires_employment_stress():
    config = load_config()
    catalog = EventCatalog(config["events"], society_hazards=config.get("society_hazards"))
    state = WorldState()
    state.fired_spine.add("sp_c2")
    state.employment_stress = 0.10
    assert not catalog.is_eligible("ev_c4_labor_shock", state, date(2027, 6, 1))
    state.employment_stress = 0.30
    assert catalog.is_eligible("ev_c4_labor_shock", state, date(2027, 6, 1))
