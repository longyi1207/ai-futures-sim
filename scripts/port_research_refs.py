#!/usr/bin/env python3
"""Port and validate research_ref paths for OSS release.

Usage:
  python scripts/port_research_refs.py --check
  python scripts/port_research_refs.py --copy [--notes-root ../notes]
  python scripts/port_research_refs.py --rewrite-links [--dry-run]
  python scripts/port_research_refs.py --rewrite-research-links [--dry-run]
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "docs" / "research"
EVIDENCE = ROOT / "docs" / "evidence"
MANIFEST = RESEARCH / "MANIFEST.md"

PORT_HEADER = (
    "> **Ported from:** `{src}` · snapshot from private monorepo · "
    "canonical edit in private monorepo until OSS lock\n\n"
)

# source (under notes/) -> dest (under docs/research/)
COPY_MAP: list[tuple[str, str]] = [
    ("timeline_prediction/node1_evidence_rationale.md", "spine/node1_evidence_rationale.md"),
    ("timeline_prediction/node2_evidence_rationale.md", "spine/node2_evidence_rationale.md"),
    ("timeline_prediction/node3_evidence_rationale.md", "spine/node3_evidence_rationale.md"),
    ("timeline_prediction/node4_evidence_rationale.md", "spine/node4_evidence_rationale.md"),
    ("timeline_prediction/node5_evidence_rationale.md", "spine/node5_evidence_rationale.md"),
    ("timeline_prediction/node6_evidence_rationale.md", "spine/node6_evidence_rationale.md"),
    ("timeline_prediction/node7_evidence_rationale.md", "spine/node7_evidence_rationale.md"),
    ("timeline_prediction/node8_evidence_rationale.md", "spine/node8_evidence_rationale.md"),
    ("timeline_prediction/node9_evidence_rationale.md", "spine/node9_evidence_rationale.md"),
    ("timeline_prediction/node9_multilateral_governance.md", "spine/node9_multilateral_governance.md"),
    ("timeline_prediction/node10_evidence_rationale.md", "spine/node10_evidence_rationale.md"),
    ("timeline_prediction/node10_disclosure_gap.md", "spine/node10_disclosure_gap.md"),
    ("timeline_prediction/node11_evidence_rationale.md", "spine/node11_evidence_rationale.md"),
    ("timeline_prediction/node12_evidence_rationale.md", "spine/node12_evidence_rationale.md"),
    ("timeline_prediction/node_physical_ai_evidence_rationale.md", "spine/node_physical_ai_evidence_rationale.md"),
    ("timeline_prediction/c8_society_snapshot_by_ci.md", "spine/c8_society_snapshot_by_ci.md"),
    ("timeline_prediction/correlation_matrix.md", "spine/correlation_matrix.md"),
    ("timeline_prediction/crosscut_us_governance_capacity.md", "spine/crosscut_us_governance_capacity.md"),
    ("timeline_prediction/crosscut_secondary_cruxes.md", "spine/crosscut_secondary_cruxes.md"),
    ("timeline_prediction/crosscut_physical_economy_limits.md", "spine/crosscut_physical_economy_limits.md"),
    ("timeline_prediction/crosscut_x3_laws_evidence_rationale.md", "spine/crosscut_x3_laws_evidence_rationale.md"),
    ("timeline_prediction/crosscut_x4_education_evidence_rationale.md", "spine/crosscut_x4_education_evidence_rationale.md"),
    ("timeline_prediction/crosscut_x5_admin_evidence_rationale.md", "spine/crosscut_x5_admin_evidence_rationale.md"),
    ("timeline_prediction/crosscut_x6_science_evidence_rationale.md", "spine/crosscut_x6_science_evidence_rationale.md"),
    ("timeline_prediction/hanson_variant_human_action.md", "spine/hanson_variant_human_action.md"),
    ("timeline_prediction_utopia/node_u1_alignment_symbiosis_evidence_rationale.md", "utopia/node_u1_alignment_symbiosis_evidence_rationale.md"),
    ("timeline_prediction_utopia/node_u2_distribution_evidence_rationale.md", "utopia/node_u2_distribution_evidence_rationale.md"),
    ("timeline_prediction_utopia/node_u3_science_abundance_evidence_rationale.md", "utopia/node_u3_science_abundance_evidence_rationale.md"),
    ("timeline_prediction_utopia/node_u6_multilateral_beneficial_evidence_rationale.md", "utopia/node_u6_multilateral_beneficial_evidence_rationale.md"),
    ("timeline_prediction_utopia/node_u7_meaning_institutions_evidence_rationale.md", "utopia/node_u7_meaning_institutions_evidence_rationale.md"),
    ("ai_futures_archive_2026-07/03_ci_spine.md", "reference/03_ci_spine.md"),
    ("ai_futures_archive_2026-07/05_crux_registry.md", "reference/05_crux_registry.md"),
    ("ai_futures_archive_2026-07/08_parallel_spines.md", "reference/08_parallel_spines.md"),
    ("timeline_prediction_node2_cbrn_full.md", "supplements/node2_cbrn_full.md"),
    ("research_ai_pause_advocacy_playbook.md", "supplements/ai_pause_advocacy_playbook.md"),
    ("ai_2027_tracker_scorecard_2026-06.md", "supplements/tracker_scorecard.md"),
    ("research_us_china_ai_dialogues.md", "supplements/us_china_ai_dialogues.md"),
    ("research_ai_medicine_longevity/10_biosecurity_evo_dual_use.md", "supplements/biosecurity_evo_dual_use.md"),
]

NOTES_TO_RESEARCH = {
    "notes/timeline_prediction/": "docs/research/spine/",
    "notes/timeline_prediction_utopia/": "docs/research/utopia/",
    "notes/ai_futures_archive_2026-07/": "docs/research/reference/",
    "notes/ai_futures/": "docs/research/reference/",
    "notes/timeline_prediction_node2_cbrn_full.md": "docs/research/supplements/node2_cbrn_full.md",
    "notes/research_ai_pause_advocacy_playbook.md": "docs/research/supplements/ai_pause_advocacy_playbook.md",
    "notes/ai_2027_tracker_scorecard_2026-06.md": "docs/research/supplements/tracker_scorecard.md",
    "notes/research_us_china_ai_dialogues.md": "docs/research/supplements/us_china_ai_dialogues.md",
    "notes/research_ai_medicine_longevity/10_biosecurity_evo_dual_use.md": "docs/research/supplements/biosecurity_evo_dual_use.md",
    "notes/my_pdoom.md": "docs/research/supplements/pdoom_methodology.md",
}

# Single-file rewrites (applied after prefix map) — evidence + research
FILE_REWRITES = {
    "notes/ai_futures/04_events_registry.md": "`config/events.yaml` (canonical event registry)",
    "notes/ai_futures/05_crux_registry.md": "docs/research/reference/05_crux_registry.md",
    "notes/ai_futures/03_ci_spine.md": "docs/research/reference/03_ci_spine.md",
    "notes/ai_futures/08_parallel_spines.md": "docs/research/reference/08_parallel_spines.md",
}

# notes/ path -> path under docs/research/ (no leading docs/research/)
RESEARCH_TARGET_MAP: dict[str, str] = {
    "notes/timeline_prediction_node2_cbrn_full.md": "supplements/node2_cbrn_full.md",
    "notes/research_ai_pause_advocacy_playbook.md": "supplements/ai_pause_advocacy_playbook.md",
    "notes/ai_2027_tracker_scorecard_2026-06.md": "supplements/tracker_scorecard.md",
    "notes/research_us_china_ai_dialogues.md": "supplements/us_china_ai_dialogues.md",
    "notes/research_ai_medicine_longevity/10_biosecurity_evo_dual_use.md": "supplements/biosecurity_evo_dual_use.md",
    "notes/my_pdoom.md": "supplements/pdoom_methodology.md",
    "notes/my_putopia.md": "utopia/node_u1_alignment_symbiosis_evidence_rationale.md",
    "notes/timeline_prediction_human_action.md": "reference/03_ci_spine.md",
    "notes/timeline_prediction_utopia_human_action.md": "reference/08_parallel_spines.md",
    "notes/timeline_prediction_nodes_1_3_expanded.md": "spine/node1_evidence_rationale.md",
    "notes/timeline_prediction/node_physical_ai_embodied.md": "spine/node_physical_ai_evidence_rationale.md",
    "notes/timeline_prediction/cross_node_evidence_rationale.md": "spine/crosscut_physical_economy_limits.md",
    "notes/timeline_prediction/crosscut_x4_education_reskilling.md": "spine/crosscut_x4_education_evidence_rationale.md",
    "notes/timeline_prediction/node5_open_weights_tamper.md": "spine/node5_evidence_rationale.md",
    "notes/timeline_prediction/node12_rsi_locus_takeoff.md": "spine/node12_evidence_rationale.md",
    "notes/ai_futures/04_events_registry.md": "config/events.yaml",
    "notes/ai_futures/05_crux_registry.md": "reference/05_crux_registry.md",
    "notes/ai_futures/03_ci_spine.md": "reference/03_ci_spine.md",
    "notes/ai_futures/08_parallel_spines.md": "reference/08_parallel_spines.md",
}

SKIP_RESEARCH_REWRITE = {RESEARCH / "README.md", RESEARCH / "MANIFEST.md"}

PUBLIC_URL_MAP: dict[str, str] = {
    "notes/Anthropic_When_AI_Builds_Itself_2026.md": "https://www.anthropic.com/institute/recursive-self-improvement",
    "notes/Anthropic_Fable_Mythos_export_ban_2026_深度解读.md": "https://www.anthropic.com/news/fable-mythos-access",
    "notes/AI_biorisk_landscape_primer.md": "https://www.rand.org/pubs/research_briefs/RBA4087-1.html",
    "notes/evaluation_awareness_llms.md": "https://arxiv.org/abs/2310.11436",
    "notes/research_recursive_self_improvement_SOTA_2026.md": "https://www.anthropic.com/institute/recursive-self-improvement",
    "notes/research_public_attitudes_toward_ai.md": "https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/",
    "notes/research_ai_employment_landscape_2026.md": "https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/",
}

EXCLUDED_MARKERS = (
    "中文",
    "深度解读",
    "导读",
    "大事记",
    "entity_master_list",
    "research_us_ai_policy_primer_zh",
    "my_alignment_position",
    "my_putopia",
    "people/",
    "transcripts/",
    "utopia_study/",
    "code/",
    "typebits",
    "qwen_harmbench",
    "dual_use_interpretability",
    "AI_security_landscape",
    "ai_meltdown_ghost_gdp",
    "ai_governance_political_strategy",
    "ai_agent_stablecoin",
    "research_tech_doomsayers",
    "research_capitalism_consumerism",
    "research_international_ai_governance",
    "research_ai_governance_landscape",
    "research_robotics",
    "research_ai_medicine_longevity/",
    "research_ai_economy_article",
    "happy_path_with_ai",
    "UBI_post_work_meaning",
    "values_psychology_map",
    "superintelligence_physical_limits",
    "agi_timeline_mathematical",
    "doom_debates",
)

NOTES_REF_RE = re.compile(r"notes/[^\s`\)\]\|>]+")
PORTED_FROM_RE = re.compile(r"^> \*\*Ported from:\*\*")
PRIVATE_PLACEHOLDER = "<!-- private monorepo only -->"


def _redact_notes_paths(text: str) -> str:
    return NOTES_REF_RE.sub("[private note]", text)


def copy_files(notes_root: Path) -> int:
    n = 0
    for src_rel, dest_rel in COPY_MAP:
        src = notes_root / src_rel
        dest = RESEARCH / dest_rel
        if not src.exists():
            print(f"SKIP missing: {src}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8")
        if not text.startswith("> **Ported from:**"):
            text = PORT_HEADER.format(src=f"notes/{src_rel}") + text
        dest.write_text(text, encoding="utf-8")
        print(f"COPIED {src_rel} -> docs/research/{dest_rel}")
        n += 1
    return n


def research_rel_link(from_file: Path, target_under_research: str) -> str:
    """Relative markdown link from from_file to docs/research/<target>."""
    if target_under_research.startswith("config/"):
        rel = os.path.relpath(ROOT / target_under_research, from_file.parent)
        return rel.replace("\\", "/")
    dest = RESEARCH / target_under_research
    rel = os.path.relpath(dest, from_file.parent)
    return rel.replace("\\", "/")


def _is_excluded(notes_ref: str) -> bool:
    return any(m in notes_ref for m in EXCLUDED_MARKERS)


def _target_for_notes_ref(notes_ref: str) -> str | None:
    if notes_ref in RESEARCH_TARGET_MAP:
        return RESEARCH_TARGET_MAP[notes_ref]
    if notes_ref in PUBLIC_URL_MAP:
        return PUBLIC_URL_MAP[notes_ref]
    for old, repl in FILE_REWRITES.items():
        if notes_ref == old:
            if repl.startswith("`"):
                return repl
            return repl.replace("docs/research/", "")
    for prefix, _ in sorted(NOTES_TO_RESEARCH.items(), key=lambda x: -len(x[0])):
        if not prefix.endswith("/"):
            continue
        if notes_ref.startswith(prefix):
            suffix = notes_ref[len(prefix) :]
            subdir = prefix.replace("notes/", "").rstrip("/")
            mapping = {
                "timeline_prediction": "spine",
                "timeline_prediction_utopia": "utopia",
                "ai_futures_archive_2026-07": "reference",
                "ai_futures": "reference",
            }
            folder = mapping.get(subdir, "supplements")
            return f"{folder}/{suffix}"
    if notes_ref.startswith("notes/") and not _is_excluded(notes_ref):
        name = notes_ref.removeprefix("notes/")
        return f"supplements/{Path(name).name}"
    return None


def _replace_notes_ref_in_line(line: str, notes_ref: str, replacement: str) -> str:
    if notes_ref not in line:
        return line
    # Prefer backtick-wrapped form
    if f"`{notes_ref}`" in line:
        return line.replace(f"`{notes_ref}`", f"`{replacement}`")
    if f"]({notes_ref})" in line:
        return line.replace(f"]({notes_ref})", f"]({replacement})")
    return line.replace(notes_ref, replacement)


def _handle_excluded_ref(line: str, notes_ref: str) -> tuple[str, int]:
    """Return (new_line, fixes_count)."""
    if notes_ref in PUBLIC_URL_MAP:
        return _replace_notes_ref_in_line(line, notes_ref, PUBLIC_URL_MAP[notes_ref]), 1
    if notes_ref in RESEARCH_TARGET_MAP:
        return line, 0  # handled elsewhere
    stripped = line.strip()
    # Inline replacement when the line has other substantive content
    without_ref = line.replace(f"`{notes_ref}`", "").replace(notes_ref, "").strip()
    has_other = len(without_ref) > 20 and not without_ref.startswith("<!--")
    if has_other:
        new = _replace_notes_ref_in_line(line, notes_ref, PRIVATE_PLACEHOLDER)
        return new, 1
    if stripped.startswith("- ") or (stripped.startswith("|") and notes_ref in line):
        if "<!-- private monorepo only" in line:
            return line, 0
        return f"<!-- private monorepo only: {_redact_notes_paths(stripped)} -->", 1
    new = _replace_notes_ref_in_line(line, notes_ref, PRIVATE_PLACEHOLDER)
    return new, 1 if new != line else 0


def rewrite_line_research(line: str, from_file: Path) -> tuple[str, int]:
    if PORTED_FROM_RE.match(line):
        # Preserve source path; drop second `notes/` in canonical-edit suffix
        return line.replace("canonical edit in `notes/`", "canonical edit in private monorepo"), (
            1 if "canonical edit in `notes/`" in line else 0
        )

    fixes = 0
    new_line = line
    refs = list(dict.fromkeys(NOTES_REF_RE.findall(line)))
    for notes_ref in refs:
        if notes_ref in PUBLIC_URL_MAP:
            new_line = _replace_notes_ref_in_line(new_line, notes_ref, PUBLIC_URL_MAP[notes_ref])
            fixes += 1
            continue
        target = _target_for_notes_ref(notes_ref)
        if target is not None:
            if target.startswith("`") or target.startswith("http"):
                repl = target
            elif target.startswith("config/"):
                repl = research_rel_link(from_file, target)
            else:
                dest = RESEARCH / target
                if dest.exists() or target.endswith(".md"):
                    repl = research_rel_link(from_file, target)
                else:
                    repl = research_rel_link(from_file, target)
            new_line = _replace_notes_ref_in_line(new_line, notes_ref, repl)
            fixes += 1
            continue
        if _is_excluded(notes_ref):
            new_line, n = _handle_excluded_ref(new_line, notes_ref)
            fixes += n
            continue
        # Unknown private note — comment bullet or placeholder
        new_line, n = _handle_excluded_ref(new_line, notes_ref)
        fixes += n

    return new_line, fixes


def _subdir_prefix(from_file: Path, subdir: str) -> str:
    rel = os.path.relpath(RESEARCH / subdir, from_file.parent)
    prefix = rel.replace("\\", "/")
    if not prefix.endswith("/"):
        prefix += "/"
    return prefix


LEGACY_BARE_FILES: dict[str, str] = {
    "timeline_prediction_human_action.md": "reference/03_ci_spine.md",
    "timeline_prediction_utopia_human_action.md": "reference/08_parallel_spines.md",
    "timeline_prediction_node2_cbrn_full.md": "supplements/node2_cbrn_full.md",
    "timeline_prediction_nodes_1_3_expanded.md": "spine/node1_evidence_rationale.md",
    "node_physical_ai_embodied.md": "spine/node_physical_ai_evidence_rationale.md",
    "crosscut_x4_education_reskilling.md": "spine/crosscut_x4_education_evidence_rationale.md",
    "crosscut_x5_political_administration_ai.md": "spine/crosscut_x5_admin_evidence_rationale.md",
    "crosscut_x6_adjacent_science_enablers.md": "spine/crosscut_x6_science_evidence_rationale.md",
    "crosscut_x3_laws_battlefield_autonomy.md": "spine/crosscut_x3_laws_evidence_rationale.md",
    "crosscut_x7_ubi_distribution_variants.md": "utopia/node_u2_distribution_evidence_rationale.md",
    "node12_rsi_locus_takeoff.md": "spine/node12_evidence_rationale.md",
    "node5_open_weights_tamper.md": "spine/node5_evidence_rationale.md",
    "cross_node_evidence_rationale.md": "spine/crosscut_physical_economy_limits.md",
    "my_putopia.md": "utopia/node_u1_alignment_symbiosis_evidence_rationale.md",
    "node_u4_physical_deployment_evidence_rationale.md": "spine/node_physical_ai_evidence_rationale.md",
}


def fix_legacy_research_paths(text: str, from_file: Path) -> str:
    """Rewrite pre-port relative links (../timeline_prediction/...) to OSS tree."""
    new = text
    spine_p = _subdir_prefix(from_file, "spine")
    utopia_p = _subdir_prefix(from_file, "utopia")
    ref_p = _subdir_prefix(from_file, "reference")
    new = new.replace("../timeline_prediction/", spine_p)
    new = new.replace("../timeline_prediction_utopia/", utopia_p)
    new = new.replace("../ai_futures/", ref_p)
    for bare, target in LEGACY_BARE_FILES.items():
        link = research_rel_link(from_file, target)
        for prefix in ("../", "./", ""):
            old = f"{prefix}{bare}"
            new = new.replace(f"]({old})", f"]({link})")
            new = new.replace(f"`{old}`", f"`{link}`")
            if old in new and f"({old})" not in new:
                new = new.replace(old, link)
    return new


def rewrite_research_links(dry_run: bool) -> tuple[int, int]:
    total_fixes = 0
    files_changed = 0
    for path in sorted(RESEARCH.rglob("*.md")):
        if path in SKIP_RESEARCH_REWRITE:
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        out: list[str] = []
        fixes = 0
        for line in lines:
            ending = "\n" if line.endswith("\n") else ""
            body = line[:-1] if ending else line
            new_body, n = rewrite_line_research(body, path)
            out.append(new_body + ending)
            fixes += n
        new_text = "".join(out)
        # Second pass: redact any notes/ left inside private comments
        redacted = re.sub(
            r"(<!-- private monorepo only:[^-]*?-->)",
            lambda m: _redact_notes_paths(m.group(1)),
            new_text,
        )
        redacted = fix_legacy_research_paths(redacted, path)
        if redacted != text:
            files_changed += 1
            total_fixes += fixes
            if not dry_run:
                path.write_text(redacted, encoding="utf-8")
            print(f"{'DRY' if dry_run else 'WROTE'} {path.relative_to(ROOT)} ({fixes} link fixes)")
        new_text = redacted
    return files_changed, total_fixes


def count_notes_refs_in_research() -> int:
    n = 0
    for path in RESEARCH.rglob("*.md"):
        n += len(re.findall(r"notes/", path.read_text(encoding="utf-8")))
    return n


def check_refs() -> list[str]:
    errors: list[str] = []
    pattern = re.compile(r"notes/[^\s`\)\]]+")
    for path in sorted(EVIDENCE.glob("ev_*.md")):
        for match in pattern.findall(path.read_text(encoding="utf-8")):
            mapped = _map_notes_path(match)
            if mapped is None:
                continue  # excluded / external — manual review
            target = ROOT / mapped
            if not target.exists():
                errors.append(f"{path.name}: missing {mapped} (from {match})")
    return errors


def _map_notes_path(notes_ref: str) -> str | None:
    if notes_ref.endswith("/"):
        return None
    for prefix, repl in NOTES_TO_RESEARCH.items():
        if notes_ref.startswith(prefix):
            return notes_ref.replace(prefix, repl, 1)
    if notes_ref.startswith("notes/timeline_prediction/"):
        return notes_ref.replace("notes/timeline_prediction/", "docs/research/spine/", 1)
    excluded = ("my_pdoom", "中文", "深度解读", "导读", "大事记", "ai_futures/04", "AI_biorisk")
    if any(x in notes_ref for x in excluded):
        return None
    return notes_ref.replace("notes/", "docs/research/supplements/", 1)


def rewrite_links(dry_run: bool) -> int:
    count = 0
    targets = list(EVIDENCE.glob("ev_*.md")) + [ROOT / "config" / "events.yaml"]
    for path in sorted(targets):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new = text
        for old, repl in sorted(FILE_REWRITES.items(), key=lambda x: -len(x[0])):
            new = new.replace(old, repl)
        for prefix, repl in sorted(NOTES_TO_RESEARCH.items(), key=lambda x: -len(x[0])):
            new = new.replace(prefix, repl)
        new = new.replace("notes/timeline_prediction/", "docs/research/spine/")
        new = new.replace("notes/timeline_prediction_utopia/", "docs/research/utopia/")
        if new != text:
            count += 1
            if not dry_run:
                path.write_text(new, encoding="utf-8")
            print(f"{'DRY' if dry_run else 'WROTE'} {path.name}")
    return count


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--copy", action="store_true")
    p.add_argument("--check", action="store_true")
    p.add_argument("--rewrite-links", action="store_true")
    p.add_argument("--rewrite-research-links", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--notes-root", type=Path, default=ROOT.parent / "notes")
    args = p.parse_args()

    if args.copy:
        n = copy_files(args.notes_root)
        print(f"Copied {n} files.")
    if args.check:
        errs = check_refs()
        if errs:
            print("MISSING:")
            for e in errs:
                print(f"  {e}")
            raise SystemExit(1)
        print("All mappable research refs resolve in-repo (or are on exclude list).")
    if args.rewrite_links:
        n = rewrite_links(args.dry_run)
        print(f"Updated {n} evidence files.")
    if args.rewrite_research_links:
        files_changed, fixes = rewrite_research_links(args.dry_run)
        remaining = count_notes_refs_in_research()
        print(f"Updated {files_changed} research files, {fixes} link fixes.")
        print(f"Remaining notes/ refs in docs/research/: {remaining}")


if __name__ == "__main__":
    main()
