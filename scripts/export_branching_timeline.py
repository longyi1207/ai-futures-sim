#!/usr/bin/env python3
"""Export branching-timeline data for the web explorer (from joint MC runs)."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from calibration_lib import run_calibration  # noqa: E402
from futures_sim.terminals import classify_region  # noqa: E402

REGION_LABELS = {
    "doom": "Doom (~17%)",
    "utopia": "Utopia (~13%)",
    "friction": "Friction (~65%)",
    "severe": "Severe (~5%)",
}

REGION_COLORS = {
    "doom": "#f28b82",
    "utopia": "#81c995",
    "friction": "#fdd663",
    "severe": "#c58af9",
}


def spine_tier(fired_spine: list[str]) -> str:
    if "sp_c9" in fired_spine or "sp_c8" in fired_spine:
        return "high_spine"
    if "sp_c5" in fired_spine:
        return "mid_spine"
    if "sp_c2" in fired_spine:
        return "low_spine"
    return "minimal"


def gov_fork(fired_events: list[str]) -> str:
    pause = "ev_federal_pause_succeeds" in fired_events
    no_pause = "ev_no_pause_2028" in fired_events
    paralysis = "ev_us_paralysis_s2" in fired_events
    if pause:
        return "pause"
    if no_pause and paralysis:
        return "race_paralysis"
    if no_pause:
        return "race"
    if paralysis:
        return "paralysis_only"
    return "gov_quiet"


def align_fork(fired_events: list[str]) -> str:
    return "c10_scare" if "ev_c10_internal_concern" in fired_events else "no_c10"


def build_timeline(n: int, seed: int) -> dict:
    report, results = run_calibration(n, seed)
    terminals_doc = None  # classify_region only needs terminal id from report context

    # Re-load terminals for classify_region
    from futures_sim.config import load_config

    config = load_config()
    terminals_doc = config["terminals"]

    # Aggregate path keys -> region
    path_counts: Counter[tuple[str, ...]] = Counter()
    path_regions: dict[tuple[str, ...], Counter[str]] = defaultdict(Counter)

    for r in results:
        region = classify_region(r.terminal, terminals_doc)
        key = (
            "start",
            spine_tier(r.fired_spine),
            gov_fork(r.fired_events),
            align_fork(r.fired_events),
            region,
        )
        path_counts[key] += 1
        path_regions[key][region] += 1

    total = n

    # Column definitions (narrative phases)
    columns = [
        {"id": 0, "year": "2026", "label": "Today"},
        {"id": 1, "year": "2027–28", "label": "Capability gates"},
        {"id": 2, "year": "2028–29", "label": "Governance fork"},
        {"id": 3, "year": "2029–31", "label": "Alignment scare"},
        {"id": 4, "year": "2050", "label": "Emergent regions"},
    ]

    node_defs = {
        "start": {"col": 0, "label": "Joint MC start", "detail": f"{n} runs, one world each"},
        "high_spine": {"col": 1, "label": "C8–C9 reached", "detail": "Full capability ladder"},
        "mid_spine": {"col": 1, "label": "Stops at C5–C7", "detail": "Mid-ladder plateau"},
        "low_spine": {"col": 1, "label": "Stops at C2–C4", "detail": "Early stall"},
        "minimal": {"col": 1, "label": "Minimal climb", "detail": "Below C2"},
        "race_paralysis": {"col": 2, "label": "Race + paralysis", "detail": "No pause · federal gridlock"},
        "race": {"col": 2, "label": "Race continues", "detail": "No federal pause"},
        "pause": {"col": 2, "label": "Pause succeeds", "detail": "Training halt (tail)"},
        "paralysis_only": {"col": 2, "label": "Paralysis only", "detail": "Gridlock without pause event"},
        "gov_quiet": {"col": 2, "label": "Quiet governance", "detail": "Neither pause nor race signature"},
        "c10_scare": {"col": 3, "label": "C10 concern fires", "detail": "Internal deception flag"},
        "no_c10": {"col": 3, "label": "No C10 scare", "detail": "Oversight stays quiet"},
        "doom": {"col": 4, "label": REGION_LABELS["doom"], "region": "doom"},
        "utopia": {"col": 4, "label": REGION_LABELS["utopia"], "region": "utopia"},
        "friction": {"col": 4, "label": REGION_LABELS["friction"], "region": "friction"},
        "severe": {"col": 4, "label": REGION_LABELS["severe"], "region": "severe"},
    }

    # Node shares: sum over paths containing node at that stage
    node_shares: Counter[str] = Counter()
    for key, count in path_counts.items():
        for node_id in key:
            node_shares[node_id] += count

    nodes = []
    for node_id, meta in node_defs.items():
        share = node_shares[node_id] / total
        if share <= 0:
            continue
        entry = {
            "id": node_id,
            "col": meta["col"],
            "label": meta["label"],
            "share": round(share, 4),
        }
        if "detail" in meta:
            entry["detail"] = meta["detail"]
        if "region" in meta:
            entry["region"] = meta["region"]
            entry["color"] = REGION_COLORS[meta["region"]]
        nodes.append(entry)

    # Links between consecutive stages in path keys
    links: Counter[tuple[str, str]] = Counter()
    for key, count in path_counts.items():
        for i in range(len(key) - 1):
            links[(key[i], key[i + 1])] += count

    link_list = [
        {
            "from": a,
            "to": b,
            "share": round(c / total, 4),
        }
        for (a, b), c in sorted(links.items(), key=lambda x: -x[1])
        if c / total >= 0.005
    ]

    # Top story paths for annotation
    top_paths = []
    for key, count in path_counts.most_common(8):
        if key[-1] == "start":
            continue
        labels = [node_defs.get(k, {}).get("label", k) for k in key[1:]]
        top_paths.append({
            "stages": list(key[1:]),
            "labels": labels,
            "share": round(count / total, 4),
            "region": key[-1],
        })

    return {
        "meta": {
            "runs": n,
            "seed": seed,
            "title": "Branching paths from joint Monte Carlo",
            "subtitle": "Ribbon width = share of simulated runs · not independent scenario weights",
        },
        "regions": report.regions,
        "terminals": dict(sorted(report.terminals.items(), key=lambda x: -x[1])[:8]),
        "path_buckets": report.path_buckets,
        "columns": columns,
        "nodes": nodes,
        "links": link_list,
        "top_paths": top_paths,
        "region_colors": REGION_COLORS,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=600)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", type=Path, default=Path("web/data/branching_timeline.json"))
    args = p.parse_args()

    payload = build_timeline(args.n, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {args.output} ({len(payload['links'])} links, {len(payload['nodes'])} nodes)")


if __name__ == "__main__":
    main()
