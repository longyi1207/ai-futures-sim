"""Load YAML configuration."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_DIR = PACKAGE_ROOT / "config"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def load_config(config_dir: Path | None = None) -> dict[str, Any]:
    root = config_dir or DEFAULT_CONFIG_DIR
    cfg = {
        "sim": load_yaml(root / "sim.yaml"),
        "variables": load_yaml(root / "variables.yaml"),
        "terminals": load_yaml(root / "terminals.yaml"),
        "spine": load_yaml(root / "spine.yaml"),
        "capability_dynamics": load_yaml(root / "capability_dynamics.yaml"),
        "events": load_yaml(root / "events.yaml"),
    }
    correlations_path = root / "correlations.yaml"
    if correlations_path.exists():
        cfg["correlations"] = load_yaml(correlations_path)
    society_path = root / "society_hazard.yaml"
    if society_path.exists():
        cfg["society_hazards"] = load_yaml(society_path)
    return cfg
