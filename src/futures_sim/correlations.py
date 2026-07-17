"""Latent cluster shocks — correlated event hazards within clusters."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class ClusterSpec:
    cluster_id: str
    rho: float
    hazard_sensitivity: float
    events: list[str]


@dataclass
class CorrelationModel:
    clusters: dict[str, ClusterSpec]
    event_to_clusters: dict[str, list[str]] = field(default_factory=dict)
    ar1_phi: float = 0.98
    init_std: float = 1.0
    hazard_sensitivity_scale: float = 1.0

    @classmethod
    def from_config(cls, doc: dict[str, Any] | None) -> CorrelationModel | None:
        if not doc or not doc.get("clusters"):
            return None

        model = doc.get("model", {})
        default_sens = float(model.get("default_hazard_sensitivity", 0.18))
        clusters: dict[str, ClusterSpec] = {}
        event_to_clusters: dict[str, list[str]] = {}

        for cluster_id, spec in doc["clusters"].items():
            events = list(spec.get("events", []))
            clusters[cluster_id] = ClusterSpec(
                cluster_id=cluster_id,
                rho=float(spec.get("rho", 0.45)),
                hazard_sensitivity=float(spec.get("hazard_sensitivity", default_sens)),
                events=events,
            )
            for eid in events:
                event_to_clusters.setdefault(eid, []).append(cluster_id)

        return cls(
            clusters=clusters,
            event_to_clusters=event_to_clusters,
            ar1_phi=float(model.get("ar1_phi", 0.98)),
            init_std=float(model.get("init_std", 1.0)),
            hazard_sensitivity_scale=float(model.get("hazard_sensitivity_scale", 1.0)),
        )

    def init_latents(self, rng: np.random.Generator) -> dict[str, float]:
        return {cid: float(rng.normal(0.0, self.init_std)) for cid in self.clusters}

    def step_latents(self, latents: dict[str, float], rng: np.random.Generator) -> dict[str, float]:
        phi = self.ar1_phi
        noise_scale = math.sqrt(max(0.0, 1.0 - phi * phi))
        return {
            cid: phi * latents[cid] + noise_scale * float(rng.normal())
            for cid in self.clusters
        }

    def adjust_hazard(
        self,
        event_id: str,
        base_hazard: float,
        cluster_latents: dict[str, float],
    ) -> float:
        """Modulate hazard via shared cluster latents (log-linear)."""
        cluster_ids = self.event_to_clusters.get(event_id)
        if not cluster_ids:
            return base_hazard

        log_mult = 0.0
        for cid in cluster_ids:
            spec = self.clusters[cid]
            log_mult += (
                self.hazard_sensitivity_scale
                * spec.hazard_sensitivity
                * cluster_latents.get(cid, 0.0)
            )

        adjusted = base_hazard * math.exp(log_mult)
        return float(np.clip(adjusted, 0.0, 1.0))
