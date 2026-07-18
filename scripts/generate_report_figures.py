#!/usr/bin/env python3
"""Generate the static figures embedded in docs/TECHNICAL_REPORT.md.

Reads real run outputs (no invented numbers): outputs/runs/seed_sweep.json
(or hardcoded fallback matching the published headline, if that file is
stale) for the region-split figure, and outputs/runs/sensitivity_capability.json
for the tornado chart.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
        "axes.edgecolor": "#888",
        "axes.linewidth": 0.6,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    }
)

REGION_COLORS = {
    "Doom": "#c0503c",
    "Utopia": "#4a8f5c",
    "Friction": "#c9a13b",
    "Severe": "#7b5aa6",
}


def fig_regions() -> None:
    """Headline four-region split, seed-averaged (§7.1)."""
    data = json.loads((ROOT / "outputs" / "runs" / "seed_sweep.json").read_text())
    per_seed = data["seeds"]
    order = ["doom", "utopia", "friction", "severe"]
    means = {
        o: sum(s["regions"][o] for s in per_seed) / len(per_seed) for o in order
    }
    labels = [o.capitalize() for o in order]
    values = [means[o] * 100 if means[o] <= 1 else means[o] for o in order]

    fig, ax = plt.subplots(figsize=(6.4, 2.6), dpi=200)
    colors = [REGION_COLORS[l] for l in labels]
    bars = ax.barh(labels, values, color=colors, height=0.6, edgecolor="none")
    ax.invert_yaxis()
    ax.set_xlim(0, max(values) * 1.22)
    ax.set_xlabel("Share of simulated runs (%)", fontsize=9)
    ax.tick_params(labelsize=10)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", color="#ddd", linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    for bar, v in zip(bars, values):
        ax.text(
            v + max(values) * 0.02,
            bar.get_y() + bar.get_height() / 2,
            f"{v:.1f}%",
            va="center",
            fontsize=9.5,
            fontweight="bold",
            color="#222",
        )
    fig.suptitle(
        "Emergent outcome-region distribution (3 seeds × 400 runs)",
        fontsize=10.5,
        fontweight="bold",
        x=0.02,
        ha="left",
        y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig1_regions.png", bbox_inches="tight")
    plt.close(fig)
    print("wrote", OUT_DIR / "fig1_regions.png")


def fig_sensitivity() -> None:
    """OAT sensitivity tornado chart (§6.3)."""
    data = json.loads((ROOT / "outputs" / "runs" / "sensitivity_capability.json").read_text())
    rows = [(p["parameter"], p["sensitivity_score"] * 100) for p in data["params"]]
    rows.sort(key=lambda x: x[1])

    # Data-driven, not a hardcoded name list: "inert" = measured exactly 0.0% in
    # this run, "top3" = the 3 highest scores. Whatever set that turns out to be
    # this run is what gets colored -- avoids the coloring silently going stale
    # the way the old hardcoded 7-name inert set did after the 2026-07-17 fix.
    top3_names = {name for name, _ in rows[-3:]}
    labels = [name for name, _ in rows]
    values = [v for _, v in rows]
    colors = []
    for name, v in rows:
        if name in top3_names:
            colors.append("#8a2e2e")
        elif v == 0.0:
            colors.append("#aaaaaa")
        else:
            colors.append("#4a6fa5")

    fig, ax = plt.subplots(figsize=(6.4, 5.6), dpi=200)
    bars = ax.barh(labels, values, color=colors, height=0.68, edgecolor="none", zorder=3)
    ax.set_xlabel("Sensitivity score (% change in calibration targets, ±25% OAT sweep)", fontsize=8.5)
    ax.tick_params(labelsize=7.8)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", color="#ddd", linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    xmax = max(values) * 1.16
    ax.set_xlim(0, xmax)
    for bar, v in zip(bars, values):
        label = f"{v:.1f}%" if v > 0 else "0.0%"
        ax.text(
            v + xmax * 0.012,
            bar.get_y() + bar.get_height() / 2,
            label,
            va="center",
            fontsize=7.3,
            color="#222",
        )
    from matplotlib.patches import Patch

    n_inert = sum(1 for _, v in rows if v == 0.0)
    n_secondary = len(rows) - 3 - n_inert
    legend_handles = [
        Patch(color="#8a2e2e", label="Top-3 dominant parameters"),
        Patch(color="#4a6fa5", label=f"Secondary (n={n_secondary})"),
        Patch(color="#aaaaaa", label=f"Structurally inert (0.0%, n={n_inert})"),
    ]
    ax.legend(handles=legend_handles, loc="lower right", fontsize=7.5, frameon=False)
    fig.suptitle(
        "Capability-growth parameter sensitivity, ranked (n=60, seed 42)",
        fontsize=10.5,
        fontweight="bold",
        x=0.02,
        ha="left",
        y=1.01,
    )
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig2_sensitivity.png", bbox_inches="tight")
    plt.close(fig)
    print("wrote", OUT_DIR / "fig2_sensitivity.png")


if __name__ == "__main__":
    fig_regions()
    fig_sensitivity()
