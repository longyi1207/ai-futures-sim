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


TERMINAL_LABELS = {
    "doom_extinction_misalign": "Extinction (misalign)",
    "doom_extinction_bio": "Extinction (bio)",
    "doom_whimper": "Whimper",
    "severe_cyber_cascade": "Cyber cascade",
    "friction_managed_non_utopia": "Managed, non-utopia",
    "friction_ghost_gdp_no_transfer": "Ghost GDP, no transfer",
    "friction_governance_paralysis": "Governance paralysis",
    "friction_labor_backlash": "Labor backlash",
    "friction_modal": "Modal",
    "friction_surveillance": "Surveillance",
    "friction_pause_stall": "Pause stall",
    "utopia_modest_welfare": "Modest welfare",
    "utopia_golden_age": "Golden age",
    "utopia_symbiosis": "Symbiosis",
    "utopia_radical_abundance": "Radical abundance",
}


def _shade(hex_color: str, factor: float) -> tuple[float, float, float]:
    """factor 1.0 = base color; >1.0 lightens toward white."""
    import matplotlib.colors as mcolors

    r, g, b = mcolors.to_rgb(hex_color)
    clip = lambda x: min(1.0, max(0.0, x))
    return (
        clip(r + (1 - r) * (factor - 1)),
        clip(g + (1 - g) * (factor - 1)),
        clip(b + (1 - b) * (factor - 1)),
    )


def fig_regions() -> None:
    """Two-level sunburst: region (inner) -> terminal (outer). §7.1.

    Inner ring uses the 3-seed headline average; outer ring uses the
    per-terminal breakdown at seed 42, n=600 (the same run already cited
    as "Top terminals (n=600, seed 42)" in the report text) rescaled onto
    each region's headline share, so the two rings are internally
    consistent and both trace to real run output.
    """
    seed_sweep = json.loads((ROOT / "outputs" / "runs" / "seed_sweep.json").read_text())
    per_seed = seed_sweep["seeds"]
    order = ["doom", "utopia", "friction", "severe"]
    region_means = {
        o: sum(s["regions"][o] for s in per_seed) / len(per_seed) for o in order
    }

    calib = json.loads((ROOT / "outputs" / "runs" / "calibration_summary.json").read_text())
    terminals_raw = calib["terminals"]  # seed 42, n=600, sums to 1.0
    regions_raw = calib["regions"]

    # Rescale each terminal's seed-42 share onto the 3-seed headline region
    # total, so outer-ring wedges sum exactly to their parent inner wedge.
    by_region: dict[str, list[tuple[str, float]]] = {o: [] for o in order}
    for term, share in terminals_raw.items():
        region = next(o for o in order if term.startswith(o) or (o == "severe" and term.startswith("severe")))
        by_region[region].append((term, share))
    for o in order:
        raw_total = regions_raw[o]
        scale = region_means[o] / raw_total if raw_total else 0.0
        by_region[o] = [(t, s * scale) for t, s in by_region[o]]
        by_region[o].sort(key=lambda x: -x[1])

    inner_labels = [o.capitalize() for o in order]
    inner_values = [region_means[o] * 100 for o in order]
    inner_colors = [REGION_COLORS[l] for l in inner_labels]

    outer_values: list[float] = []
    outer_colors: list[tuple] = []
    outer_labels: list[str] = []
    for o, label in zip(order, inner_labels):
        terms = by_region[o]
        n = len(terms)
        for i, (term, share) in enumerate(terms):
            outer_values.append(share * 100)
            # Darkest for the largest sub-terminal, lightening toward the tail.
            factor = 1.0 + (i / max(n - 1, 1)) * 1.1
            outer_colors.append(_shade(REGION_COLORS[label], factor))
            outer_labels.append(TERMINAL_LABELS.get(term, term))

    fig, ax = plt.subplots(figsize=(7.2, 7.2), dpi=200)

    ax.pie(
        inner_values,
        radius=0.62,
        colors=inner_colors,
        wedgeprops=dict(width=0.62, edgecolor="white", linewidth=1.5),
        labels=[f"{l}\n{v:.1f}%" for l, v in zip(inner_labels, inner_values)],
        labeldistance=0.62,
        textprops=dict(fontsize=9.5, fontweight="bold", color="white", ha="center"),
    )

    wedges, _ = ax.pie(
        outer_values,
        radius=1.0,
        colors=outer_colors,
        wedgeprops=dict(width=0.38, edgecolor="white", linewidth=1.0),
    )
    # Only label outer wedges above a legibility threshold; small tail
    # terminals stay visible as unlabeled slivers rather than cluttered text.
    for wedge, val, label in zip(wedges, outer_values, outer_labels):
        if val < 2.2:
            continue
        angle = (wedge.theta1 + wedge.theta2) / 2
        import numpy as np

        x = 0.82 * np.cos(np.radians(angle))
        y = 0.82 * np.sin(np.radians(angle))
        rot = angle + 180 if 90 < angle < 270 else angle
        ax.text(
            x,
            y,
            f"{label}\n{val:.1f}%",
            ha="center",
            va="center",
            fontsize=7.2,
            color="#1a1a1a",
            rotation=rot,
            rotation_mode="anchor",
        )

    ax.set(aspect="equal")
    fig.suptitle(
        "Emergent outcome-region distribution, by terminal\n"
        "(inner: 3-seed headline; outer: terminal breakdown, seed 42 n=600)",
        fontsize=10.5,
        fontweight="bold",
        y=0.99,
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
