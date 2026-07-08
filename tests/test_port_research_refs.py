"""Tests for port_research_refs link rewriting."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import port_research_refs as prr  # noqa: E402


def test_research_rel_link_same_dir(tmp_path: Path):
    root = tmp_path / "sim"
    research = root / "docs" / "research"
    spine = research / "spine"
    spine.mkdir(parents=True)
    from_file = spine / "node1_evidence_rationale.md"
    from_file.write_text("# test\n")
    prr.ROOT = root
    prr.RESEARCH = research
    link = prr.research_rel_link(from_file, "spine/node2_evidence_rationale.md")
    assert link == "node2_evidence_rationale.md"


def test_research_rel_link_cross_subdir(tmp_path: Path):
    root = tmp_path / "sim"
    research = root / "docs" / "research"
    utopia = research / "utopia"
    spine = research / "spine"
    utopia.mkdir(parents=True)
    spine.mkdir(parents=True)
    from_file = utopia / "node_u1_alignment_symbiosis_evidence_rationale.md"
    from_file.write_text("# test\n")
    prr.ROOT = root
    prr.RESEARCH = research
    link = prr.research_rel_link(from_file, "spine/node2_evidence_rationale.md")
    assert link == "../spine/node2_evidence_rationale.md"


def test_rewrite_line_maps_timeline_prediction():
    root = Path(__file__).resolve().parents[1]
    prr.ROOT = root
    prr.RESEARCH = root / "docs" / "research"
    from_file = prr.RESEARCH / "spine" / "node1_evidence_rationale.md"
    line = "- see `notes/timeline_prediction/node2_evidence_rationale.md` for bio"
    new, fixes = prr.rewrite_line_research(line, from_file)
    assert fixes == 1
    assert "notes/" not in new
    assert "node2_evidence_rationale.md" in new


def test_preserve_ported_from_header():
    root = Path(__file__).resolve().parents[1]
    prr.ROOT = root
    prr.RESEARCH = root / "docs" / "research"
    from_file = prr.RESEARCH / "spine" / "node1_evidence_rationale.md"
    line = "> **Ported from:** `notes/timeline_prediction/node1_evidence_rationale.md` · canonical edit in `notes/` until OSS lock"
    new, _ = prr.rewrite_line_research(line, from_file)
    assert "notes/timeline_prediction/node1_evidence_rationale.md" in new
    assert "canonical edit in private monorepo" in new
