"""v0.1.2 HIGH-1 regression — P7 §18-validator path-resolution + fail-close.

Discovered via T2-Empirie 2026-05-24 (§6 Versionsverlauf + §13 Lifecycle live runs).
Pre-fix: skill probed `01_Skills/paragraph-18-sync/scripts/p18_sync.py` (spec-stub,
never landed) then bare `paragraph-18-sync` (not on PATH) → FileNotFoundError →
silent WARNING-skip. Real validator lives at `03_Tools/para18_sync/validator.py`.
"""

import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_DIR / "scripts"))

from core_slim_refactor import _resolve_p18_command  # noqa: E402
from patterns import _insert_after_last_table_row  # noqa: E402


def test_real_validator_picked_when_present(tmp_path):
    """Primary candidate `03_Tools/para18_sync/validator.py` wins."""
    real = tmp_path / "03_Tools" / "para18_sync" / "validator.py"
    real.parent.mkdir(parents=True)
    real.write_text("# stub\n", encoding="utf-8")

    cmd = _resolve_p18_command(tmp_path)
    assert cmd[0] == sys.executable
    assert cmd[1] == str(real)
    assert cmd[2:] == ["system-zustand", "--dry-run", "--json"]


def test_legacy_alias_used_when_only_legacy_present(tmp_path):
    """Forward-compat: legacy `01_Skills/.../p18_sync.py` resolves if validator absent."""
    legacy = tmp_path / "01_Skills" / "paragraph-18-sync" / "scripts" / "p18_sync.py"
    legacy.parent.mkdir(parents=True)
    legacy.write_text("# stub\n", encoding="utf-8")

    cmd = _resolve_p18_command(tmp_path)
    assert cmd[1] == str(legacy)


def test_real_validator_preferred_over_legacy(tmp_path):
    """When both exist, real validator wins (priority order)."""
    real = tmp_path / "03_Tools" / "para18_sync" / "validator.py"
    real.parent.mkdir(parents=True)
    real.write_text("# real\n", encoding="utf-8")
    legacy = tmp_path / "01_Skills" / "paragraph-18-sync" / "scripts" / "p18_sync.py"
    legacy.parent.mkdir(parents=True)
    legacy.write_text("# legacy\n", encoding="utf-8")

    cmd = _resolve_p18_command(tmp_path)
    assert cmd[1] == str(real)


def test_bare_path_fallback_when_neither_present(tmp_path):
    """Fallback to PATH-bare command. Subprocess will raise FileNotFoundError if
    the binary is not on PATH — phase_p7 catches that and fail-closes via
    SystemExit(EXIT_GATE_FAIL) (v0.1.2 HIGH-1: previously silent WARNING-skip)."""
    cmd = _resolve_p18_command(tmp_path)
    assert cmd == ["paragraph-18-sync", "system-zustand", "--dry-run", "--json"]


# v0.1.2 MEDIUM-2 regression — pointer must land BEFORE trailing footer/notes


def test_pointer_inserted_before_footer_bullet():
    """Real-world case from CORE-MEMORY.md L425: section ends with a
    `> Note:` footer bullet — pointer must land BEFORE it, not after."""
    lines = [
        "| 2026-05-01 | row-a |",
        "| 2026-05-15 | row-b |",
        "> Note: footer prose (must stay last visible)",
    ]
    out = _insert_after_last_table_row(lines, "| 2026-05-24 | POINTER |")
    assert out == [
        "| 2026-05-01 | row-a |",
        "| 2026-05-15 | row-b |",
        "| 2026-05-24 | POINTER |",
        "> Note: footer prose (must stay last visible)",
    ]


def test_pointer_inserted_before_trailing_blank_and_prose():
    """Footer can be blank-prose-blank — pointer still lands after last table row."""
    lines = [
        "| 2026-05-01 | row-a |",
        "",
        "Some footer prose.",
        "",
    ]
    out = _insert_after_last_table_row(lines, "| 2026-05-24 | POINTER |")
    assert out == [
        "| 2026-05-01 | row-a |",
        "| 2026-05-24 | POINTER |",
        "",
        "Some footer prose.",
        "",
    ]


def test_pointer_appended_when_no_table_rows():
    """Safe fallback: section with no table rows → plain append."""
    lines = ["Just prose.", "More prose."]
    out = _insert_after_last_table_row(lines, "| 2026-05-24 | POINTER |")
    assert out == ["Just prose.", "More prose.", "| 2026-05-24 | POINTER |"]


def test_pointer_appended_when_last_line_is_table_row():
    """No footer case: pointer lands as new last line."""
    lines = ["| 2026-05-01 | row-a |", "| 2026-05-15 | row-b |"]
    out = _insert_after_last_table_row(lines, "| 2026-05-24 | POINTER |")
    assert out == [
        "| 2026-05-01 | row-a |",
        "| 2026-05-15 | row-b |",
        "| 2026-05-24 | POINTER |",
    ]
