"""Static cross-reference integrity for config/*.yaml.

These catch typo'd ids that would otherwise fail silently: `unlock`/`lock`/
`modify_hazard`/precondition lists are just string sets in the engine
(see effects.py, events.py, spine.py) — a misspelled id is never eligible
and never raises, it just silently does nothing.
"""

from __future__ import annotations

from pathlib import Path

from futures_sim.config import load_config

REPO_ROOT = Path(__file__).resolve().parents[1]


def _event_id_refs(ev: dict) -> set[str]:
    refs: set[str] = set()
    for key in ("unlock", "lock"):
        refs |= set(ev.get(key, []) or [])
        of = ev.get("on_fire") or {}
        refs |= set(of.get(key, []) or [])
    of = ev.get("on_fire") or {}
    refs |= set((of.get("modify_hazard") or {}).keys())
    for terminal_key in ("force_terminal",):
        refs |= set(of.get(terminal_key, []) or [])
    pre = ev.get("preconditions", {}) or {}
    refs |= set(pre.get("events_fired", []) or [])
    refs |= set(pre.get("events_not_fired", []) or [])
    return refs


def test_event_cross_references_resolve():
    config = load_config()
    events = config["events"]["events"]
    ids = {e["id"] for e in events}
    terminal_ids = set(config["terminals"]["terminals"].keys())

    missing: dict[str, set[str]] = {}
    for e in events:
        refs = _event_id_refs(e)
        of = e.get("on_fire") or {}
        force_terminal_refs = set(of.get("force_terminal", []) or [])
        unresolved = (refs - force_terminal_refs - ids) | (force_terminal_refs - terminal_ids)
        if unresolved:
            missing[e["id"]] = unresolved

    assert not missing, f"undefined ids referenced from events.yaml: {missing}"


def test_event_precondition_spine_references_resolve():
    config = load_config()
    events = config["events"]["events"]
    spine_ids = {m["id"] for m in config["spine"]["milestones"]}

    missing: dict[str, set[str]] = {}
    for e in events:
        pre = e.get("preconditions", {}) or {}
        refs = set(pre.get("spine_fired", []) or []) | set(pre.get("spine_not_fired", []) or [])
        unresolved = refs - spine_ids
        if unresolved:
            missing[e["id"]] = unresolved

    assert not missing, f"undefined spine ids referenced from events.yaml preconditions: {missing}"


def test_spine_cross_references_resolve():
    config = load_config()
    milestones = config["spine"]["milestones"]
    spine_ids = {m["id"] for m in milestones}
    event_ids = {e["id"] for e in config["events"]["events"]}

    missing: dict[str, set[str]] = {}
    for m in milestones:
        pre = m.get("preconditions", {}) or {}
        refs = set(pre.get("spine_fired", []) or []) | set(pre.get("spine_not_fired", []) or [])
        unresolved = refs - spine_ids
        ev_refs = set(pre.get("events_fired", []) or []) | set(pre.get("events_not_fired", []) or [])
        unresolved |= ev_refs - event_ids
        if unresolved:
            missing[m["id"]] = unresolved

    assert not missing, f"undefined ids referenced from spine.yaml preconditions: {missing}"


def test_terminal_event_references_resolve():
    config = load_config()
    event_ids = {e["id"] for e in config["events"]["events"]}
    terminals_doc = config["terminals"]

    missing: dict[str, set[str]] = {}

    def check(label: str, cond: dict) -> None:
        refs = set(cond.get("events_all", []) or []) | set(cond.get("events_any", []) or [])
        unresolved = refs - event_ids
        if unresolved:
            missing[label] = unresolved

    for rule in terminals_doc.get("event_forced", []):
        if rule["event"] not in event_ids:
            missing[f"event_forced:{rule['event']}"] = {rule["event"]}
    for i, rule in enumerate(terminals_doc.get("horizon_default", [])):
        check(f"horizon_default[{i}]", rule.get("conditions", {}))
    for tid, spec in terminals_doc.get("terminals", {}).items():
        check(tid, spec.get("conditions", {}))

    assert not missing, f"undefined event ids referenced from terminals.yaml: {missing}"


def test_state_variable_references_resolve():
    """Every var name touched by config (preconditions/on_fire/terminals/society_hazard/
    capability_dynamics inputs) must be a real WorldState field — else it silently
    KeyErrors at runtime deep in a Monte Carlo run, or (for society_hazard.yaml reads
    via state.get()) crashes mid-sweep instead of at config load."""
    from futures_sim.state import WorldState

    config = load_config()
    valid = set(WorldState().__dict__.keys())

    referenced: set[str] = set()
    for e in config["events"]["events"]:
        pre = e.get("preconditions", {}) or {}
        referenced |= set((pre.get("vars") or {}).keys())
        of = e.get("on_fire") or {}
        for bucket in ("set_vars", "add_vars", "floor_vars"):
            referenced |= set((of.get(bucket) or {}).keys())
    for m in config["spine"]["milestones"]:
        pre = m.get("preconditions", {}) or {}
        referenced |= set((pre.get("vars") or {}).keys())
        of = m.get("on_fire") or {}
        for bucket in ("set_vars", "add_vars", "floor_vars"):
            referenced |= set((of.get(bucket) or {}).keys())
    for name in config["variables"].get("initial", {}):
        referenced.add(name)
    for name in config["variables"].get("daily_drift", {}):
        referenced.add(name)
    for name in (config.get("society_hazards") or {}):
        referenced.add(name)
    for spec in (config.get("capability_dynamics") or {}).get("inputs", {}):
        referenced.add(spec)

    terminals_doc = config["terminals"]

    def collect_vars(cond: dict) -> set[str]:
        return set((cond.get("vars") or {}).keys())

    for rule in terminals_doc.get("horizon_default", []):
        referenced |= collect_vars(rule.get("conditions", {}))
    for spec in terminals_doc.get("terminals", {}).values():
        referenced |= collect_vars(spec.get("conditions", {}))

    unresolved = referenced - valid
    assert not unresolved, f"config references unknown WorldState variables: {unresolved}"


def test_event_research_refs_exist_on_disk():
    config = load_config()
    missing = []
    for e in config["events"]["events"]:
        ref = e.get("research_ref")
        if not ref:
            missing.append((e["id"], "no research_ref"))
            continue
        if not (REPO_ROOT / ref).exists():
            missing.append((e["id"], ref))
    assert not missing, f"events with missing/dangling research_ref: {missing}"
