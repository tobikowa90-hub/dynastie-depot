import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from patterns import (  # noqa: E402
    RowSet,
    classify_bucket_archive,
    classify_date_cut,
    classify_slim_convention,
    mutate_bucket_archive,
    mutate_date_cut,
    mutate_slim_convention,
)

FIXTURES = Path(__file__).parent / "fixtures"


def _read(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


# ──────────────── Pattern A tests ────────────────


def test_classify_bucket_archive_matches_keywords():
    md = _read("bucket_archive_sample.md")
    cfg_block = {
        "classify": {
            "by": "keyword",
            "keywords": ["Ruflo Sunset", "Ruflo Promotion"],
            "keep_keywords": ["claude-mem v13.2.0"],
            "case_sensitive": True,
        },
    }
    rs = classify_bucket_archive(md, section_anchor="## §13 Lifecycle", cfg=cfg_block)
    assert isinstance(rs, RowSet)
    assert len(rs.archive) == 3
    assert any("Ruflo Sunset begin" in r for r in rs.archive)
    assert any("Ruflo Sunset complete" in r for r in rs.archive)
    assert any("Ruflo Promotion archive" in r for r in rs.archive)
    assert any("claude-mem v13.2.0" in r for r in rs.keep)


def test_classify_bucket_archive_empty_when_no_match():
    md = _read("bucket_archive_sample.md")
    cfg_block = {
        "classify": {
            "by": "keyword",
            "keywords": ["NonExistentKeyword"],
            "keep_keywords": [],
            "case_sensitive": True,
        },
    }
    rs = classify_bucket_archive(md, section_anchor="## §13 Lifecycle", cfg=cfg_block)
    assert len(rs.archive) == 0


def test_mutate_bucket_archive_replaces_with_pointer():
    md = _read("bucket_archive_sample.md")
    cfg_block = {
        "classify": {
            "by": "keyword",
            "keywords": ["Ruflo Sunset", "Ruflo Promotion"],
            "keep_keywords": ["claude-mem v13.2.0"],
            "case_sensitive": True,
        },
        "pointer": {
            "insert_at": "chronological",
            "template": "| {pointer_date} | RUFLO SUNSET archived | {n_rows} rows | [archive]({archive_link}) |",
        },
    }
    rs = classify_bucket_archive(md, section_anchor="## §13 Lifecycle", cfg=cfg_block)
    new_md = mutate_bucket_archive(
        md,
        section_anchor="## §13 Lifecycle",
        rowset=rs,
        cfg=cfg_block,
        pointer_context={
            "pointer_date": "2026-05-23",
            "n_rows": len(rs.archive),
            "archive_link": "../05_Archiv/test-archive.md",
        },
    )
    assert "Ruflo Sunset begin" not in new_md
    assert "Ruflo Promotion archive" not in new_md
    assert "RUFLO SUNSET archived" in new_md
    assert "claude-mem v13.2.0" in new_md


# ──────────────── Pattern B tests ────────────────


def test_classify_slim_convention_detects_fat_rows():
    md = _read("slim_convention_sample.md")
    cfg_block = {
        "fat_threshold_bytes": 3500,
        "exclude_keywords": ["AMZN-Neuaufnahme"],
        "exclude_dates": ["2026-05-23"],
    }
    rs = classify_slim_convention(md, section_anchor="## §13 Slim-Test", cfg=cfg_block)
    assert len(rs.slim_targets) == 2
    assert all(len(r.encode("utf-8")) > 3500 for r in rs.slim_targets)
    assert not any("AMZN-Neuaufnahme" in r for r in rs.slim_targets)


def test_mutate_slim_convention_compresses_fat_rows():
    md = _read("slim_convention_sample.md")
    cfg_block = {
        "fat_threshold_bytes": 3500,
        "exclude_keywords": [],
        "exclude_dates": ["2026-05-23"],
        "slim": {
            "outcome_max_chars": 280,
            "pointer_tail_format": "[Archive]({archive_link}), PIPELINE {pipeline_ids}, git {short_shas}",
            "extract_bold_title": True,
            "extract_pipeline_ids": True,
            "extract_short_shas": True,
        },
    }
    rs = classify_slim_convention(md, section_anchor="## §13 Slim-Test", cfg=cfg_block)
    new_md = mutate_slim_convention(
        md,
        section_anchor="## §13 Slim-Test",
        rowset=rs,
        cfg=cfg_block,
        slim_context={"archive_link": "../05_Archiv/fat-rows.md"},
    )
    assert "Fat Row Alpha" in new_md
    assert "Fat Row Beta" in new_md
    # behavior assert: no remaining line exceeds the fat-threshold (slim succeeded)
    for line in new_md.split("\n"):
        assert len(line.encode("utf-8")) <= 3500, f"line still fat: {line[:80]}..."
    assert "PIPELINE #99" in new_md or "PIPELINE #100" in new_md
    assert "ab12cd3" in new_md or "de45678" in new_md
    assert "../05_Archiv/fat-rows.md" in new_md
    assert "AMZN-Neuaufnahme" in new_md


# ──────────────── Pattern C tests ────────────────


def test_classify_date_cut_separates_pre_post():
    md = _read("date_cut_sample.md")
    cfg_block = {
        "cut_before": "2026-04-01",
        "date_parser": {
            "field": "header",
            "pattern": r"^## (\d{4}-\d{2}-\d{2}) ",
        },
    }
    rs = classify_date_cut(md, section_anchor=None, cfg=cfg_block)
    assert len(rs.archive) >= 3
    assert all("Pre-cut Entry" in entry for entry in rs.archive)
    assert any("2026-01-15" in entry for entry in rs.archive)
    assert any("2026-03-25" in entry for entry in rs.archive)


def test_classify_date_cut_boundary_inclusive():
    md = """## 2026-04-01 Boundary Entry
content here
"""
    cfg_block = {
        "cut_before": "2026-04-01",
        "date_parser": {"field": "header", "pattern": r"^## (\d{4}-\d{2}-\d{2}) "},
    }
    rs = classify_date_cut(md, section_anchor=None, cfg=cfg_block)
    assert len(rs.archive) == 0


def test_mutate_date_cut_replaces_with_boundary_header():
    md = _read("date_cut_sample.md")
    cfg_block = {
        "cut_before": "2026-04-01",
        "date_parser": {"field": "header", "pattern": r"^## (\d{4}-\d{2}-\d{2}) "},
        "pointer": {
            "insert_at": "section_top",
            "template": "> **Pre-{cut_date} entries archived** -> [{archive_path}]({archive_link})\n",
        },
    }
    rs = classify_date_cut(md, section_anchor=None, cfg=cfg_block)
    new_md = mutate_date_cut(
        md,
        section_anchor=None,
        rowset=rs,
        cfg=cfg_block,
        pointer_context={
            "cut_date": "2026-04-01",
            "archive_path": "05_Archiv/test-archive.md",
            "archive_link": "../05_Archiv/test-archive.md",
        },
    )
    assert "Pre-cut Entry 1" not in new_md
    assert "Pre-cut Entry 3" not in new_md
    assert "Post-cut Entry 4" in new_md
    assert "Pre-2026-04-01 entries archived" in new_md
