#!/usr/bin/env python3
"""Export event + spine graph as JSON and Mermaid from config YAML."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from futures_sim.config import load_config  # noqa: E402


def _edges_from_effects(eid: str, on_fire: dict) -> list[dict]:
    edges: list[dict] = []
    for target in on_fire.get("unlock") or []:
        edges.append({"from": eid, "to": target, "type": "unlock"})
    for target in on_fire.get("lock") or []:
        edges.append({"from": eid, "to": target, "type": "lock"})
    for target, spec in (on_fire.get("modify_hazard") or {}).items():
        edges.append({"from": eid, "to": target, "type": "modify_hazard", "mult": spec.get("mult")})
    return edges


def build_graph(config: dict) -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []

    for spec in (config.get("spine") or {}).get("milestones") or []:
        mid = spec["id"]
        nodes.append({
            "id": mid,
            "kind": "spine",
            "name": spec.get("name", mid),
            "ci_level": spec.get("ci_level"),
        })
        for e in _edges_from_effects(mid, spec.get("on_fire") or {}):
            edges.append(e)
        for sf in (spec.get("preconditions") or {}).get("spine_fired") or []:
            edges.append({"from": sf, "to": mid, "type": "requires_spine"})

    for ev in (config.get("events") or {}).get("events") or []:
        eid = ev["id"]
        nodes.append({
            "id": eid,
            "kind": "event",
            "name": ev.get("name", eid),
            "category": ev.get("category"),
            "p_cumulative": (ev.get("schedule") or {}).get("p_cumulative"),
            "research_ref": ev.get("research_ref"),
        })
        pre = ev.get("preconditions") or {}
        for sf in pre.get("spine_fired") or []:
            edges.append({"from": sf, "to": eid, "type": "requires_spine"})
        for ef in pre.get("events_fired") or []:
            edges.append({"from": ef, "to": eid, "type": "requires_event"})
        if ev.get("requires_unlock"):
            edges.append({"from": ev["requires_unlock"], "to": eid, "type": "requires_unlock"})
        for e in _edges_from_effects(eid, ev.get("on_fire") or {}):
            edges.append(e)

    return {"nodes": nodes, "edges": edges, "meta": {"events": len([n for n in nodes if n["kind"] == "event"]), "spine": len([n for n in nodes if n["kind"] == "spine"])}}


def to_mermaid(graph: dict, max_edges: int = 80) -> str:
    lines = ["flowchart LR"]
    spine = [n["id"] for n in graph["nodes"] if n["kind"] == "spine"]
    for i, mid in enumerate(spine):
        label = mid.replace("sp_", "C")
        lines.append(f'  {mid}["{label}"]')
        if i:
            lines.append(f"  {spine[i-1]} --> {mid}")
    shown = 0
    for e in graph["edges"]:
        if e["type"] not in ("unlock", "requires_spine"):
            continue
        if shown >= max_edges:
            lines.append("  %% truncated")
            break
        style = "-->" if e["type"] == "unlock" else "-.->"
        lines.append(f'  {e["from"]} {style}|{e["type"]}| {e["to"]}')
        shown += 1
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--output-json", type=Path, default=Path("web/data/event_graph.json"))
    p.add_argument("--output-mmd", type=Path, default=Path("docs/EVENT_GRAPH.mmd"))
    args = p.parse_args()

    config = load_config(ROOT / "config")
    graph = build_graph(config)

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(graph, indent=2), encoding="utf-8")

    mmd = to_mermaid(graph)
    args.output_mmd.parent.mkdir(parents=True, exist_ok=True)
    args.output_mmd.write_text(mmd + "\n", encoding="utf-8")

    print(f"Wrote {args.output_json} ({graph['meta']['events']} events, {graph['meta']['spine']} spine)")
    print(f"Wrote {args.output_mmd}")


if __name__ == "__main__":
    main()
