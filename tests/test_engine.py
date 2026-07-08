"""Basic engine and hazard tests."""

from futures_sim.config import load_config
from futures_sim.engine import run_monte_carlo
from futures_sim.events import cumulative_to_daily_hazard


def test_hazard_conversion_bounds():
    h = cumulative_to_daily_hazard(0.4, 365)
    assert 0 < h < 1
    # Over 365 days at least one success should approximate 0.4
    survive = 1.0
    for _ in range(365):
        survive *= 1 - h
    assert abs(1 - survive - 0.4) < 0.05


def test_sim_runs_complete():
    config = load_config()
    results = run_monte_carlo(config, n_runs=50, seed=0)
    assert len(results) == 50
    for r in results:
        assert r.terminal is not None
        assert 0 <= r.terminal_day < 9000
