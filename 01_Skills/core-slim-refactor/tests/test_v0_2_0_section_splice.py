"""v0.2.0 Section-Splice - Spec 3.4, AC5/AC6/AC6b/AC6c/AC6d, F-05+F-06+F-08."""

import difflib
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from patterns import (  # noqa: E402
    _build_line_byte_offsets,
    _splice_section,
    classify_bucket_archive,
    mutate_bucket_archive,
)

FIXTURES = ROOT / "tests" / "fixtures"


# ───────────────── AC6d - Byte-Offset-Map Invariants ─────────────────


def test_build_line_byte_offsets_basic_invariants():
    md = "line1\nline2\nline3\n"
    offsets = _build_line_byte_offsets(md)
    md_bytes = md.encode("utf-8")
    assert offsets[0] == 0
    assert offsets[-1] == len(md_bytes)
    # n newlines + 1 EOF sentinel + 1 initial zero = count("\n") + 2
    assert len(offsets) == md.count("\n") + 2


def test_build_line_byte_offsets_unicode_safe():
    md = "header\nUmlaut: äöü\n§-Sign\nemoji \U0001f468‍\U0001f469\n"
    offsets = _build_line_byte_offsets(md)
    md_bytes = md.encode("utf-8")
    assert offsets[-1] == len(md_bytes)
    # Decode line 1 (Umlaut) correctly reconstructable
    line1 = md_bytes[offsets[1] : offsets[2]].decode("utf-8")
    assert "ä" in line1


def test_build_line_byte_offsets_empty_string():
    md = ""
    offsets = _build_line_byte_offsets(md)
    assert offsets[0] == 0
    assert offsets[-1] == 0
    # 0 newlines + 2 = 2 entries
    assert len(offsets) == 2


def test_build_line_byte_offsets_no_trailing_newline():
    md = "line1\nline2"
    offsets = _build_line_byte_offsets(md)
    md_bytes = md.encode("utf-8")
    assert offsets[0] == 0
    assert offsets[-1] == len(md_bytes)
    # 1 newline + 2 = 3 entries
    assert len(offsets) == md.count("\n") + 2


# ───────────────── AC6 - No-Op Byte-Stability ─────────────────


def test_splice_no_op_byte_stable():
    md = "header\n\n## section\nkeep1\nkeep2\n\n## next\ntail\n"
    offsets = _build_line_byte_offsets(md)
    # Section identified: lines starting at index 2 ("## section") through index 4 inclusive
    # offsets[2] = byte start of "## section\n", offsets[5] = byte start of "\n## next"
    start = offsets[2]
    end = offsets[5]
    same_section = md.encode("utf-8")[start:end].decode("utf-8")
    out = _splice_section(md, start, end, same_section)
    assert out.encode("utf-8") == md.encode("utf-8")


def test_splice_replaces_section_content():
    md = "header\n## section\nold-body\n## next\ntail\n"
    offsets = _build_line_byte_offsets(md)
    # "## section\n" starts at line 1, "old-body\n" at line 2; next section at line 3
    # Section span [offsets[1], offsets[3])
    start = offsets[1]
    end = offsets[3]
    new_section = "## section\nnew-body\n"
    out = _splice_section(md, start, end, new_section)
    assert "new-body" in out
    assert "old-body" not in out
    assert out.startswith("header\n")
    assert out.endswith("## next\ntail\n")


# ───────────────── AC6c - Splice-Boundary-Assert (F-05) ─────────────────


def test_splice_boundary_assert_on_non_line_aligned():
    md = "line1\nline2\nline3\n"
    with pytest.raises(ValueError, match="splice_boundary_not_line_aligned"):
        _splice_section(md, start_byte=3, end_byte=10, new_section_text="X\n")


def test_splice_boundary_start_ok_end_bad():
    md = "line1\nline2\nline3\n"
    offsets = _build_line_byte_offsets(md)
    good_start = offsets[0]  # 0 is always valid
    bad_end = offsets[1] + 1  # mid-line
    with pytest.raises(ValueError, match="splice_boundary_not_line_aligned"):
        _splice_section(md, start_byte=good_start, end_byte=bad_end, new_section_text="X\n")


# ───────────────── AC6b - Unicode-Grapheme-Integrity (F-05) ─────────────────


def test_splice_outside_section_unicode_byte_identical():
    pre = "Pre-Umlaut ä ö ü\n§ sign\n"
    middle = "## section\nold-body\n"
    tail = "## next\n\U0001f468‍\U0001f469 family\n\U0001f1e9\U0001f1ea flag\n"
    md = pre + middle + tail
    offsets = _build_line_byte_offsets(md)
    pre_lines = pre.count("\n")
    sec_lines = middle.count("\n")
    start = offsets[pre_lines]
    end = offsets[pre_lines + sec_lines]
    new_section = "## section\nnew-body\n"
    out = _splice_section(md, start, end, new_section)
    out_bytes = out.encode("utf-8")
    md_bytes = md.encode("utf-8")
    # Pre-area byte-identical
    assert out_bytes[:start] == md_bytes[:start]
    # Post-area (tail) byte-identical
    new_end = start + len(new_section.encode("utf-8"))
    assert out_bytes[new_end:] == md_bytes[end:]
    # Emoji-Family + Flag intact in tail
    assert "\U0001f468‍\U0001f469" in out
    assert "\U0001f1e9\U0001f1ea" in out


# ───────────────── Task 4.3 - half-open invariant roundtrip ─────────────────


def test_iter_section_rows_half_open_interval_roundtrip_via_byte_offsets():
    """Anchors the half-open semantics of _iter_section_rows (patterns.py docstring).

    If _iter_section_rows returns (lines, start, end_exclusive), then:
    md_bytes[offsets[start]:offsets[end]].decode() == '\\n'.join(lines) + '\\n'
    (with trailing-newline correction when original section had trailing newline).

    Breaks if someone silently changes _iter_section_rows semantics to inclusive.
    """
    from patterns import _iter_section_rows

    md = "header\n## section A\nA-line-1\nA-line-2\n## section B\nB-line\n"
    section_lines, start, end = _iter_section_rows(md, "## section A")
    offsets = _build_line_byte_offsets(md)
    extracted = md.encode("utf-8")[offsets[start] : offsets[end]].decode("utf-8")
    expected = "\n".join(section_lines) + "\n"
    assert extracted == expected, f"half-open invariant broken: got={extracted!r} want={expected!r}"


# ───────────────── AC5 - T2-section-13-Replay Diff exactness ─────────────────


def _load_yaml_cfg(path: Path) -> dict:
    """Load bucket-archive config from YAML fixture, mapping to flat cfg dict."""
    try:
        import yaml
    except ImportError:
        pytest.skip("PyYAML not available")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    ba = raw["bucket_archive"]
    return {
        "classify": ba["classify"],
        "pointer": ba["pointer"],
        "section_anchor": raw["target"]["section"],
    }


def _diff_counts(before: str, after: str) -> tuple[int, int]:
    """Return (removed, added) line counts between before and after."""
    d = list(difflib.unified_diff(before.splitlines(), after.splitlines(), lineterm=""))
    removed = sum(1 for ln in d if ln.startswith("-") and not ln.startswith("---"))
    added = sum(1 for ln in d if ln.startswith("+") and not ln.startswith("+++"))
    return removed, added


def test_ac5_t2_section13_replay_diff_exactness():
    """AC5 - T2-Empirie-Test #2 replay: v0.2.0 splice produces -26/+1 vs pre-state.

    Source: T2-Empirie commit 359c296 (v0.1.1 T2-Empirie 2 Live-Runs DONE).
    Pattern: Pattern-A bucket-archive on CORE-MEMORY §13 System-Lifecycle-History.
    Config: core-memory-s13-lifecycle-pre-may-10-bucket.yaml (26 rows archived).

    v0.2.0 (splice) produces -26/+1 vs pre — exactly 26 rows removed, 1 pointer
    row added. Byte-precise splice means no reflow of non-section content.
    """
    pre_file = FIXTURES / "v0_2_0_t2_section_13_pre.md"
    cfg_file = FIXTURES / "v0_2_0_t2_section_13_cut_config.yaml"
    expected_file = FIXTURES / "v0_2_0_t2_section_13_v0_2_0_expected_post.md"

    if not pre_file.exists() or not cfg_file.exists():
        pytest.skip("T2-section-13 fixtures not present")

    cfg_data = _load_yaml_cfg(cfg_file)
    cfg = {k: v for k, v in cfg_data.items() if k != "section_anchor"}
    section_anchor = cfg_data["section_anchor"]

    pointer_context = {
        "n_rows": 26,
        "archive_link": "05_Archiv/CORE-MEMORY-ss13-Lifecycle-23.04.-09.05.2026-archiv.md",
        "cut_date": "2026-05-24",
        "archive_basename": "CORE-MEMORY-ss13-Lifecycle-23.04.-09.05.2026-archiv",
        "archive_relpath": "05_Archiv/CORE-MEMORY-ss13-Lifecycle-23.04.-09.05.2026-archiv.md",
        "target_file": "00_Core/CORE-MEMORY.md",
        "section": section_anchor,
        "timestamp": "2026-05-24",
    }

    pre_md = pre_file.read_text(encoding="utf-8")

    rs = classify_bucket_archive(pre_md, section_anchor, cfg)
    assert len(rs.archive) == 26, f"Expected 26 archived rows, got {len(rs.archive)}"

    out = mutate_bucket_archive(pre_md, section_anchor, rs, cfg, pointer_context)

    removed, added = _diff_counts(pre_md, out)
    assert removed == 26, f"AC5: expected 26 removed lines, got {removed}"
    assert added == 1, f"AC5: expected 1 added line (pointer), got {added}"

    # Pointer must appear BEFORE the footer line (splice preserves position)
    pointer_marker = "Pre-2026-05-10 Lifecycle-Cut"
    footer_marker = "CORE-MEMORY.md v1.27"
    out_lines = out.splitlines()
    ptr_indices = [i for i, ln in enumerate(out_lines) if pointer_marker in ln]
    ftr_indices = [i for i, ln in enumerate(out_lines) if footer_marker in ln]
    assert ptr_indices, "AC5: pointer row not found in output"
    assert ftr_indices, "AC5: footer line not found in output"
    assert ptr_indices[0] < ftr_indices[0], (
        f"AC5: pointer (line {ptr_indices[0]}) must precede footer (line {ftr_indices[0]}) "
        "— splice preserves section boundary, list-rebuild did not"
    )

    # Output must match the pre-generated expected fixture (reproducibility)
    if expected_file.exists():
        expected = expected_file.read_text(encoding="utf-8")
        assert out == expected, "AC5: v0.2.0 output does not match expected fixture"


def test_ac5_t2_section13_v011_vs_v020_position_regression():
    """AC5b - v0.1.1 placed pointer AFTER footer (reflow-noise bug).

    Fixture-documented: v0.1.1 baseline_post has pointer on line 48, footer on line 47.
    v0.2.0 expected_post has pointer on line 46, footer on line 48.
    This test anchors the regression so it cannot silently re-appear.
    """
    v011_file = FIXTURES / "v0_2_0_t2_section_13_v0_1_1_baseline_post.md"
    v020_file = FIXTURES / "v0_2_0_t2_section_13_v0_2_0_expected_post.md"

    if not v011_file.exists() or not v020_file.exists():
        pytest.skip("T2-section-13 baseline/expected fixtures not present")

    pointer_marker = "Pre-2026-05-10 Lifecycle-Cut"
    footer_marker = "CORE-MEMORY.md v1.27"

    v011_lines = v011_file.read_text(encoding="utf-8").splitlines()
    v020_lines = v020_file.read_text(encoding="utf-8").splitlines()

    ptr011 = next(i for i, ln in enumerate(v011_lines) if pointer_marker in ln)
    ftr011 = next(i for i, ln in enumerate(v011_lines) if footer_marker in ln)
    ptr020 = next(i for i, ln in enumerate(v020_lines) if pointer_marker in ln)
    ftr020 = next(i for i, ln in enumerate(v020_lines) if footer_marker in ln)

    # v0.1.1 had pointer AFTER footer (the documented reflow-noise bug)
    assert ptr011 > ftr011, (
        f"Fixture integrity: v0.1.1 baseline should have pointer after footer "
        f"(ptr={ptr011}, ftr={ftr011})"
    )
    # v0.2.0 must have pointer BEFORE footer
    assert ptr020 < ftr020, (
        f"AC5b regression: v0.2.0 must have pointer before footer (ptr={ptr020}, ftr={ftr020})"
    )
