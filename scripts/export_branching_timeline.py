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

REGION_COLORS = {
    "doom": "#f28b82",
    "utopia": "#81c995",
    "friction": "#fdd663",
    "severe": "#c58af9",
}

LOCALES: dict[str, dict] = {
    "en": {
        "columns": [
            {"id": 0, "year": "2026", "label": "Today"},
            {"id": 1, "year": "2027–28", "label": "Capability gates"},
            {"id": 2, "year": "2028–29", "label": "Governance fork"},
            {"id": 3, "year": "2029–31", "label": "Alignment scare"},
            {"id": 4, "year": "2050", "label": "Emergent regions"},
        ],
        "nodes": {
            "start": {"label": "Joint MC start", "detail": "{n} runs, one world each"},
            "high_spine": {"label": "C8–C9 reached", "detail": "Full capability ladder"},
            "mid_spine": {"label": "Stops at C5–C7", "detail": "Mid-ladder plateau"},
            "low_spine": {"label": "Stops at C2–C4", "detail": "Early stall"},
            "minimal": {"label": "Minimal climb", "detail": "Below C2"},
            "race_paralysis": {"label": "Race + paralysis", "detail": "No pause · federal gridlock"},
            "race": {"label": "Race continues", "detail": "No federal pause"},
            "pause": {"label": "Pause succeeds", "detail": "Training halt (tail)"},
            "paralysis_only": {"label": "Paralysis only", "detail": "Gridlock without pause event"},
            "gov_quiet": {"label": "Quiet governance", "detail": "Neither pause nor race signature"},
            "c10_scare": {"label": "C10 concern fires", "detail": "Internal deception flag"},
            "no_c10": {"label": "No C10 scare", "detail": "Oversight stays quiet"},
        },
        "region_names": {
            "doom": "Doom",
            "utopia": "Utopia",
            "friction": "Friction",
            "severe": "Severe",
        },
        "meta_title": "Branching paths from joint Monte Carlo",
        "meta_subtitle": "Ribbon width = share of simulated runs · not independent scenario weights",
        "path_buckets": {
            "c9_no_whistle": "c9 no whistle chain",
            "paralysis_mid_ladder": "paralysis mid-ladder",
            "pause_stall": "pause stall",
            "full_alignment_chain": "full alignment chain",
            "stops_before_c5": "stops before c5",
            "full_spine": "full spine c1→c9",
        },
    },
    "zh": {
        "columns": [
            {"id": 0, "year": "2026", "label": "当下"},
            {"id": 1, "year": "2027–28", "label": "能力门"},
            {"id": 2, "year": "2028–29", "label": "治理分叉"},
            {"id": 3, "year": "2029–31", "label": "对齐恐慌"},
            {"id": 4, "year": "2050", "label": "涌现四分区"},
        ],
        "nodes": {
            "start": {"label": "联合 MC 起点", "detail": "{n} 次运行，每次一个世界"},
            "high_spine": {"label": "达 C8–C9", "detail": "完整能力脊柱"},
            "mid_spine": {"label": "止于 C5–C7", "detail": "中阶平台"},
            "low_spine": {"label": "止于 C2–C4", "detail": "早期停滞"},
            "minimal": {"label": "最低爬升", "detail": "低于 C2"},
            "race_paralysis": {"label": "竞赛+瘫痪", "detail": "无暂停 · 联邦僵局"},
            "race": {"label": "竞赛继续", "detail": "无联邦训练暂停"},
            "pause": {"label": "暂停成功", "detail": "训练暂停（尾部）"},
            "paralysis_only": {"label": "仅瘫痪", "detail": "僵局但未触发暂停事件"},
            "gov_quiet": {"label": "治理平淡", "detail": "无暂停/竞赛典型信号"},
            "c10_scare": {"label": "C10 担忧触发", "detail": "内部欺骗信号"},
            "no_c10": {"label": "无 C10 恐慌", "detail": "监督保持安静"},
        },
        "region_names": {
            "doom": "末日",
            "utopia": "繁荣",
            "friction": "摩擦",
            "severe": "严重",
        },
        "meta_title": "联合蒙特卡洛分叉路径",
        "meta_subtitle": "丝带宽度 = 模拟运行份额 · 非独立情景权重",
        "path_buckets": {
            "c9_no_whistle": "C9 无吹哨链",
            "paralysis_mid_ladder": "瘫痪·中阶脊柱",
            "pause_stall": "暂停后停滞",
            "full_alignment_chain": "完整对齐链",
            "stops_before_c5": "止于 C5 前",
            "full_spine": "全脊柱 c1→c9",
        },
    },
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


def region_label(region: str, share: float, lang: str) -> str:
    name = LOCALES[lang]["region_names"][region]
    pct = round(100 * share)
    if lang == "zh":
        return f"{name}（~{pct}%）"
    return f"{name} (~{pct}%)"


def build_timeline(n: int, seed: int, lang: str = "en") -> dict:
    if lang not in LOCALES:
        raise ValueError(f"Unknown lang: {lang}")

    loc = LOCALES[lang]
    report, results = run_calibration(n, seed)

    from futures_sim.config import load_config

    config = load_config()
    terminals_doc = config["terminals"]

    path_counts: Counter[tuple[str, ...]] = Counter()

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

    total = n
    columns = loc["columns"]
    node_meta = loc["nodes"]
    col_map = {
        "start": 0,
        "high_spine": 1, "mid_spine": 1, "low_spine": 1, "minimal": 1,
        "race_paralysis": 2, "race": 2, "pause": 2, "paralysis_only": 2, "gov_quiet": 2,
        "c10_scare": 3, "no_c10": 3,
    }
    node_defs: dict[str, dict] = {}
    for node_id, col in col_map.items():
        node_defs[node_id] = {**node_meta[node_id], "col": col}

    for region in ("doom", "utopia", "friction", "severe"):
        node_defs[region] = {
            "col": 4,
            "label": region_label(region, report.regions.get(region, 0), lang),
            "region": region,
        }

    start_detail = node_defs["start"]["detail"].format(n=n)
    node_defs["start"]["detail"] = start_detail

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

    links: Counter[tuple[str, str]] = Counter()
    for key, count in path_counts.items():
        for i in range(len(key) - 1):
            links[(key[i], key[i + 1])] += count

    link_list = [
        {"from": a, "to": b, "share": round(c / total, 4)}
        for (a, b), c in sorted(links.items(), key=lambda x: -x[1])
        if c / total >= 0.005
    ]

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

    path_buckets = {
        loc["path_buckets"].get(k, k): v
        for k, v in report.path_buckets.items()
    }

    return {
        "meta": {
            "runs": n,
            "seed": seed,
            "lang": lang,
            "title": loc["meta_title"],
            "subtitle": loc["meta_subtitle"],
        },
        "regions": report.regions,
        "terminals": dict(sorted(report.terminals.items(), key=lambda x: -x[1])[:8]),
        "path_buckets": path_buckets,
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
    p.add_argument("--lang", choices=("en", "zh"), default="en")
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    output = args.output
    if output is None:
        output = (
            Path("web/data/branching_timeline_zh.json")
            if args.lang == "zh"
            else Path("web/data/branching_timeline.json")
        )

    payload = build_timeline(args.n, args.seed, args.lang)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {output} ({len(payload['links'])} links, {len(payload['nodes'])} nodes)")


if __name__ == "__main__":
    main()
