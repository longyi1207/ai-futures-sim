"""Correlation latent shocks tests."""

import numpy as np

from futures_sim.config import load_config
from futures_sim.correlations import CorrelationModel
from futures_sim.engine import SimEngine


def test_correlation_model_loads():
    config = load_config()
    model = CorrelationModel.from_config(config["correlations"])
    assert model is not None
    assert "race" in model.clusters
    assert "ev_no_pause_2028" in model.event_to_clusters


def test_high_latent_increases_hazard():
    config = load_config()
    model = CorrelationModel.from_config(config["correlations"])
    assert model is not None

    base = 0.01
    low = model.adjust_hazard("ev_no_pause_2028", base, {"race": -2.0})
    high = model.adjust_hazard("ev_no_pause_2028", base, {"race": 2.0})
    assert high > base > low


def test_same_cluster_events_share_latent_boost():
    config = load_config()
    model = CorrelationModel.from_config(config["correlations"])
    assert model is not None

    latents = {"race": 1.5}
    base = 0.02
    h1 = model.adjust_hazard("ev_race_acceleration", base, latents)
    h2 = model.adjust_hazard("ev_weight_theft", base, latents)
    assert h1 > base and h2 > base
    assert abs(h1 - h2) < 1e-9  # same single-cluster sensitivity for both


def test_ar1_latents_persist():
    config = load_config()
    model = CorrelationModel.from_config(config["correlations"])
    assert model is not None

    rng = np.random.default_rng(0)
    z0 = model.init_latents(rng)
    z1 = model.step_latents(z0, rng)
    assert set(z0) == set(z1)
    # Not independent — correlated with previous
    assert not all(abs(z0[c] - z1[c]) > 1.0 for c in z0)


def test_engine_runs_with_correlations():
    config = load_config()
    config["sim"]["use_correlations"] = True
    rng = np.random.default_rng(1)
    engine = SimEngine(config=config, rng=rng)
    result = engine.run_once()
    assert result.terminal is not None
    assert isinstance(result.fired_spine, list)
