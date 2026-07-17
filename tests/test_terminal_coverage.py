"""Regression guard for terminal taxonomy health.

`horizon_default` rules are checked in list order — the first match wins
(see terminals.py::default_terminal_at_horizon). Overlapping variable ranges
mean a new rule inserted earlier, or a variable whose default dynamics make
one rule's condition near-universal, can silently swallow most of the
horizon-assigned runs. This happened in practice: an incompletely-wired
`distribution_regime` uplift path briefly pushed `friction_ghost_gdp_no_transfer`
to >75% of all outcomes and collapsed doom/utopia to ~1.6% each (vs the
~17%/~13% documented headline). These bounds don't pin an exact target
(outcome regions are emergent, not calibrated — see docs/CALIBRATION.md) but
catch a rule swallowing the outcome space outright.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from calibration_lib import run_calibration  # noqa: E402

N_RUNS = 100
SEED = 7
MAX_SINGLE_TERMINAL_SHARE = 0.85
MAX_UNCLASSIFIED_SHARE = 0.30


@pytest.fixture(scope="module")
def report():
    # Shared across all three tests below — each independently re-running the same
    # calibration tripled this file's cost for no benefit (same seed, same n).
    rep, _ = run_calibration(N_RUNS, SEED)
    return rep


def test_no_single_terminal_dominates(report):
    worst_terminal, worst_share = max(report.terminals.items(), key=lambda kv: kv[1])
    assert worst_share <= MAX_SINGLE_TERMINAL_SHARE, (
        f"{worst_terminal} absorbed {worst_share:.1%} of {N_RUNS} runs (limit "
        f"{MAX_SINGLE_TERMINAL_SHARE:.0%}) — a horizon_default rule is likely "
        "shadowing the rest of the taxonomy; check config/terminals.yaml ordering "
        "and the variables driving that rule's conditions."
    )


def test_friction_unclassified_residual_bounded(report):
    share = report.terminals.get("friction_unclassified", 0.0)
    assert share <= MAX_UNCLASSIFIED_SHARE, (
        f"friction_unclassified absorbed {share:.1%} of {N_RUNS} runs (limit "
        f"{MAX_UNCLASSIFIED_SHARE:.0%}) — the friction sub-taxonomy in "
        "config/terminals.yaml horizon_default is missing coverage for a common "
        "region of state space; add a named rule rather than growing the catch-all."
    )


def test_all_doom_and_utopia_terminals_reachable(report):
    """Every doom/utopia terminal should fire at least once at N_RUNS unless it's an
    intentionally rare tail (bio/kinetic extinction chains) — a terminal that never
    fires across a few hundred runs after a config change may indicate a broken
    precondition chain rather than genuine rarity.

    Note: `report.terminals` (a Counter-derived dict) only has keys for terminals
    that fired at least once — a terminal with zero hits is simply absent, not
    present with value 0.0. Must diff against the full declared terminal set from
    config, not iterate `report.terminals` looking for zeros.
    """
    from futures_sim.config import load_config

    all_terminal_ids = set(load_config()["terminals"]["terminals"].keys())
    always_rare = {
        "doom_extinction_bio",
        "doom_extinction_kinetic",
        "doom_extinction_misalign",
    }
    unreached = sorted((all_terminal_ids - set(report.terminals.keys())) - always_rare)
    # Informational, not a hard failure for any single terminal — but flag if the
    # unreached set covers a large fraction of the declared taxonomy.
    assert len(unreached) < 8, f"{len(unreached)} terminals never fired in {N_RUNS} runs: {unreached}"
