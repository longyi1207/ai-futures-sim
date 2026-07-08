"""Deterministic capability calendar (Ci spine) + optional stochastic pace."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any

import numpy as np


def parse_date(s: str) -> date:
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)


def day_index(start: date, current: date) -> int:
    return (current - start).days


@dataclass
class RunCiConfig:
    schedule: list[dict[str, Any]]
    pace_factor: float = 1.0
    shock_prob: float = 0.0
    shock_magnitude: float = 0.5


def build_run_ci_config(
    ci_doc: dict[str, Any],
    sim_start: date,
    rng: np.random.Generator,
    *,
    stochastic_enabled: bool,
) -> RunCiConfig:
    schedule = list(ci_doc["schedule"])
    stochastic = ci_doc.get("stochastic") or {}

    if not stochastic_enabled or not stochastic:
        return RunCiConfig(schedule=schedule)

    mean = float(stochastic.get("pace_factor_mean", 0.70))
    std = float(stochastic.get("pace_factor_std", 0.08))
    pace_factor = float(np.clip(rng.normal(mean, std), 0.45, 1.25))

    adjusted: list[dict[str, Any]] = []
    for entry in schedule:
        target = parse_date(entry["date"])
        days_from_start = max(0, (target - sim_start).days)
        scaled_days = int(days_from_start / pace_factor) if pace_factor > 0 else days_from_start
        adjusted_date = sim_start + timedelta(days=scaled_days)
        adjusted.append({"date": adjusted_date.isoformat(), "ci_level": entry["ci_level"]})

    return RunCiConfig(
        schedule=adjusted,
        pace_factor=pace_factor,
        shock_prob=float(stochastic.get("shock_prob", 0.02)),
        shock_magnitude=float(stochastic.get("shock_magnitude", 0.5)),
    )


def apply_ci_schedule(
    state,
    run_ci: RunCiConfig | list[dict],
    current: date,
    sim_start: date,
    *,
    rng: np.random.Generator | None = None,
) -> None:
    """Raise ci_level to scheduled targets (monotonic)."""
    if isinstance(run_ci, RunCiConfig):
        schedule = run_ci.schedule
        shock_prob = run_ci.shock_prob
        shock_magnitude = run_ci.shock_magnitude
    else:
        schedule = run_ci
        shock_prob = 0.0
        shock_magnitude = 0.5

    for entry in schedule:
        target_date = parse_date(entry["date"])
        if current >= target_date:
            target_ci = float(entry["ci_level"])
            if state.ci_level < target_ci:
                state.ci_level = target_ci
                state.ai_rd_multiplier = max(state.ai_rd_multiplier, 1.0 + 0.35 * target_ci)
                state.tech_level = max(state.tech_level, min(1.0, 0.08 * target_ci))

    if rng is not None and shock_prob > 0 and rng.random() < shock_prob:
        state.ci_level = min(10.0, state.ci_level + shock_magnitude)
        state.ai_rd_multiplier = max(state.ai_rd_multiplier, 1.0 + 0.35 * state.ci_level)
        state.tech_level = max(state.tech_level, min(1.0, 0.08 * state.ci_level))


def sim_dates(start: str, end: str) -> tuple[date, date, int]:
    d0 = parse_date(start)
    d1 = parse_date(end)
    n_days = (d1 - d0).days
    return d0, d1, n_days
