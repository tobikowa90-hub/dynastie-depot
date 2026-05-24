"""v0.2.0 Pattern-C Bullet-Variante -- Spec SS3.1, AC1/AC1b/AC1c/AC1d."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from patterns import _split_bullet_block, classify_date_cut  # noqa: E402

# ---------------------------------------------------------------------------
# Shared fixture markdown
# ---------------------------------------------------------------------------

BULLET_MD = """\
# Section

- **Datum:** 2026-05-15 -- Banner A
  Body A line 1
  Body A line 2
- **Datum:** 2026-05-17 -- Banner B
  Body B line 1
- **Datum:** 2026-05-20 -- Banner C
  Body C line 1
  Body C line 2

## Trailing Heading

This trailing content must NOT collapse into Banner C body.
"""

_BULLET_REGEX = r"^- \*\*Datum:\*\*\s+(\d{4}-\d{2}-\d{2})"
_TRAILING_BOUNDARY = r"^## "


# ---------------------------------------------------------------------------
# Task 2.1 -- Test 1: happy-path bullet-split
# ---------------------------------------------------------------------------


def test_split_bullet_block_happy_path():
    """_split_bullet_block returns 3 entries, correct dates, body does not spill into trailing."""
    entries = _split_bullet_block(
        BULLET_MD,
        bullet_regex=_BULLET_REGEX,
        trailing_boundary=_TRAILING_BOUNDARY,
    )
    assert len(entries) == 3
    dates = [d for d, _ in entries]
    assert dates == ["2026-05-15", "2026-05-17", "2026-05-20"]
    body_c = entries[-1][1]
    assert "Trailing Heading" not in body_c
    assert "Body C line 2" in body_c


# ---------------------------------------------------------------------------
# Task 2.1 -- Test 2: trailing-boundary-stop
# ---------------------------------------------------------------------------


def test_split_bullet_block_trailing_boundary_stop():
    """Last body ends exactly before the trailing_boundary line."""
    entries = _split_bullet_block(
        BULLET_MD,
        bullet_regex=_BULLET_REGEX,
        trailing_boundary=_TRAILING_BOUNDARY,
    )
    body_c = entries[-1][1]
    assert body_c.rstrip().endswith("Body C line 2")


# ---------------------------------------------------------------------------
# Task 2.1 -- Test 3: classify_date_cut routes to _split_bullet_block (field=bullet)
# ---------------------------------------------------------------------------


def test_classify_date_cut_bullet_branching():
    """classify_date_cut routes to _split_bullet_block when field=bullet.

    cut_before=2026-05-17 -> archive: 2026-05-15; keep: 2026-05-17, 2026-05-20.
    """
    cfg = {
        "cut_before": "2026-05-17",
        "date_parser": {
            "field": "bullet",
            "pattern": _BULLET_REGEX,
            "trailing_boundary": _TRAILING_BOUNDARY,
        },
    }
    rs = classify_date_cut(BULLET_MD, section_anchor=None, cfg=cfg)
    assert len(rs.archive) == 1
    assert len(rs.keep) == 2


# ---------------------------------------------------------------------------
# Task 2.1 -- Test 4: Q4 header-mode regression
# ---------------------------------------------------------------------------


def test_classify_date_cut_header_mode_unchanged_q4_regression():
    """Q4-Verdict: header-mode classification stays equivalent across v0.1.x and v0.2.0.

    Klassifikations-aequivalent (nicht byte-identisch -- mutate_date_cut waere fuer Byte-Test
    noetig, das uebernimmt der Worked-Example-Integration-Test in Phase 6). Hier reicht der
    Smoke: implizites Header-Default (v0.1.x, kein field-Key) und explizites field=header
    (v0.2.0) muessen identische RowSet-Klassifikation liefern.
    """
    md = "## 2026-05-15\nA\n## 2026-05-17\nB\n## 2026-05-20\nC\n"
    # v0.1.x-style: no field key (implicit header)
    cfg_v1 = {
        "cut_before": "2026-05-17",
        "date_parser": {"pattern": r"^## (\d{4}-\d{2}-\d{2})"},
    }
    rs_v1 = classify_date_cut(md, section_anchor=None, cfg=cfg_v1)
    # v0.2.0 explicit field=header
    cfg_v2 = {
        "cut_before": "2026-05-17",
        "date_parser": {"field": "header", "pattern": r"^## (\d{4}-\d{2}-\d{2})"},
    }
    rs_v2 = classify_date_cut(md, section_anchor=None, cfg=cfg_v2)
    # Both paths must produce identical results
    assert rs_v1.archive == rs_v2.archive
    assert rs_v1.keep == rs_v2.keep


# ---------------------------------------------------------------------------
# Codex-MEDIUM-1 Regression: bullet-mode no-match must preserve content
# ---------------------------------------------------------------------------


def test_classify_date_cut_bullet_no_match_preserves_content():
    """Bullet-mode mit Content der KEINE bullet_regex-Matches enthaelt -> ganzer md geht in keep.

    Codex-Review (post d9c3872) MEDIUM-1: stiller Datenverlust wenn _split_bullet_block []
    liefert. Fix: classify_date_cut bullet-branch faengt das ab und preservt den Content
    analog zum Header-Mode (der unmatched Content auch in keep schreibt).
    """
    md_no_bullets = "# Section\n\nNo bullets here, just prose.\n\n## Trailing\nMore prose.\n"
    cfg = {
        "cut_before": "2026-05-17",
        "date_parser": {
            "field": "bullet",
            "pattern": _BULLET_REGEX,
            "trailing_boundary": _TRAILING_BOUNDARY,
        },
    }
    rs = classify_date_cut(md_no_bullets, section_anchor=None, cfg=cfg)
    assert rs.archive == []
    assert rs.keep == [md_no_bullets]
