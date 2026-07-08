#!/usr/bin/env python3
"""Add research_ref to each event in config/events.yaml if missing."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / "config" / "events.yaml"


def main() -> None:
    text = EVENTS.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    changed = 0
    for ev in data["events"]:
        eid = ev["id"]
        ref = f"docs/evidence/{eid}.md"
        if ev.get("research_ref") != ref:
            ev["research_ref"] = ref
            changed += 1

    # Preserve header comments manually — rewrite via ruamel or simple dump
    # Use round-trip friendly dump
    header = """# 50+ world events — v1.1
# Probability: schedule.p_cumulative = P(at least once in [start,end]); engine converts to daily hazard
# See docs/PROBABILITY_MODEL.md — do NOT treat p_cumulative as p_per_day
# Evidence: docs/evidence/<event_id>.md

"""
    body = yaml.dump(
        {"mutex_groups": data.get("mutex_groups", {}), "events": data["events"]},
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=120,
    )
    EVENTS.write_text(header + body, encoding="utf-8")
    print(f"Updated research_ref on {changed} events; total {len(data['events'])}")


if __name__ == "__main__":
    main()
