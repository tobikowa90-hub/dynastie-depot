"""v0.2.0 SESSION-HANDOVER Worked-Example Integration-Test -- Spec SS4, AC8/AC8b.

Schliesst P4-LOW-2 Coverage-Gap (Q4-Header-Mode-Byte-Identity).

Tests:
  1. dry-run: target + config unveraendert, kein Archive
  2. live-run: archive vorhanden, Resume-Anweisung im keep (NICHT im archive),
               executed populated mit commit_sha=pending
  3. Q4-byte-identity: header-mode mutate_date_cut output ist byte-identisch
                        mit und ohne explizites field=header (v0.1.x vs v0.2.0)

Invocation-Disziplin (empirisch 2026-05-24):
  - positionales Arg, kein '--config'-Prefix (argparse ist positional)
  - CORE_SLIM_REFACTOR_SKIP_GATE=1 erforderlich (P7-§18-Gate bypassen in Test)
  - encoding='utf-8', errors='replace' (Windows cp1252 Guard)
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "core_slim_refactor.py"
WORKED_CFG = SKILL_ROOT / "references" / "configs" / "session-handover-banner-list-cut.yaml"

# ---------------------------------------------------------------------------
# Shared subprocess helper (mirrors test_v0_2_0_executed_auto_populate.py pattern)
# ---------------------------------------------------------------------------


def _run(cfg: Path, *extra: str) -> subprocess.CompletedProcess:
    """Subprocess-Run mit P7-Gate-Bypass (CORE_SLIM_REFACTOR_SKIP_GATE=1)."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(cfg), *extra],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "CORE_SLIM_REFACTOR_SKIP_GATE": "1"},
        check=False,
    )


# ---------------------------------------------------------------------------
# Sandbox fixture: minimal SESSION-HANDOVER with 7 bullet-entries
# ---------------------------------------------------------------------------

# 3 entries before cut_before (2026-05-17), 4 on-or-after; plus a trailing section
# that MUST NOT collapse into the last bullet body (MEDIUM-9 Risk-Mitigation).
_SH_BODY = (
    "# SESSION-HANDOVER\n"
    "\n"
    "## Banner-Chronik\n"
    "\n"
    "- **Datum:** 2026-05-10 -- Session Alpha\n"
    "  Body line Alpha 1\n"
    "  Body line Alpha 2\n"
    "\n"
    "- **Datum:** 2026-05-12 -- Session Beta\n"
    "  Body line Beta 1\n"
    "\n"
    "- **Datum:** 2026-05-15 -- Session Gamma\n"
    "  Body line Gamma 1\n"
    "\n"
    "- **Datum:** 2026-05-17 -- Session Delta\n"
    "  Body line Delta 1\n"
    "\n"
    "- **Datum:** 2026-05-19 -- Session Epsilon\n"
    "  Body line Epsilon 1\n"
    "\n"
    "- **Datum:** 2026-05-21 -- Session Zeta\n"
    "  Body line Zeta 1\n"
    "\n"
    "- **Datum:** 2026-05-23 -- Session Eta\n"
    "  Body line Eta 1\n"
    "\n"
    "## Resume-Anweisung\n"
    "\n"
    "DO NOT collapse into last banner body.\n"
)


@pytest.fixture()
def sandbox_sh(tmp_path: Path):
    """Erstellt Sandbox mit SH-Fixture + gepatchter Worked-Example-Config.

    Gibt (cfg_path, sh_path, archive_path) zurueck.
    """
    sh_path = tmp_path / "SESSION-HANDOVER.md"
    sh_path.write_text(_SH_BODY, encoding="utf-8", newline="\n")
    archive_path = tmp_path / "archive.md"

    # Worked-Example-Config lesen + absolute Pfade einsetzen
    cfg_raw = WORKED_CFG.read_text(encoding="utf-8")

    # Pfad-Substitutionen (target file + archive path)
    cfg_raw = cfg_raw.replace(
        '"00_Core/SESSION-HANDOVER.md"',
        f'"{sh_path.as_posix()}"',
    )
    cfg_raw = cfg_raw.replace(
        '"05_Archiv/session-handover-bis-2026-05-16-archiv.md"',
        f'"{archive_path.as_posix()}"',
    )

    # Backlink-Scan deaktivieren (scan_paths enthalten Repo-Pfade, nicht vorhanden im tmp)
    # Ersetze scan_paths-Block mit leerem Array
    cfg_raw = cfg_raw.replace(
        "  scan_paths:\n"
        '    - "00_Core/"\n'
        '    - "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/"\n',
        "  scan_paths: []\n",
    )

    cfg_path = tmp_path / "cfg.yaml"
    cfg_path.write_text(cfg_raw, encoding="utf-8", newline="\n")
    return cfg_path, sh_path, archive_path


# ---------------------------------------------------------------------------
# Task 6.2 -- Test 1: dry-run unveraendert (AC8b)
# ---------------------------------------------------------------------------


def test_sh_worked_example_dry_run(sandbox_sh):
    """Dry-run: target + config unveraendert, kein Archive (AC8b)."""
    cfg, sh, archive = sandbox_sh
    before_sh = sh.read_bytes()
    before_cfg = cfg.read_bytes()

    res = _run(cfg, "--dry-run")

    assert res.returncode == 0, f"stderr={res.stderr!r}\nstdout={res.stdout!r}"
    assert sh.read_bytes() == before_sh, "target darf bei --dry-run NICHT veraendert werden"
    assert not archive.exists(), "archive darf bei --dry-run NICHT erstellt werden"
    assert cfg.read_bytes() == before_cfg, "config darf bei --dry-run NICHT veraendert werden"


# ---------------------------------------------------------------------------
# Task 6.2 -- Test 2: live-run (AC8)
# ---------------------------------------------------------------------------


def test_sh_worked_example_live_run(sandbox_sh):
    """Live-run: archive vorhanden, Resume-Anweisung im keep NICHT im archive,
    executed populated mit commit_sha='pending' (AC8)."""
    cfg, sh, archive = sandbox_sh

    res = _run(cfg)

    assert res.returncode == 0, f"stderr={res.stderr!r}\nstdout={res.stdout!r}"
    assert archive.exists(), "archive muss nach live-run existieren"

    archive_text = archive.read_text(encoding="utf-8")
    sh_text = sh.read_text(encoding="utf-8")

    # Resume-Anweisung muss im keep-Teil des Targets bleiben
    assert "Resume-Anweisung" not in archive_text, (
        "Resume-Anweisung darf NICHT im Archive landen (trailing_boundary-Stop pruefen)"
    )
    assert "Resume-Anweisung" in sh_text, "Resume-Anweisung muss im gekuerzten Target verbleiben"

    # Eintraege vor cut_before muessen archiviert sein
    assert "2026-05-10" in archive_text
    assert "2026-05-12" in archive_text
    assert "2026-05-15" in archive_text

    # Eintraege ab cut_before muessen im Target verbleiben
    assert "2026-05-17" in sh_text
    assert "2026-05-23" in sh_text

    # executed muss populated sein (P7b auto-writeback)
    data = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    assert data["executed"] is not None, "executed muss nach live-run populated sein"
    assert data["executed"]["commit_sha"] == "pending"
    assert data["executed"]["timestamp"] is not None
    assert data["executed"]["reference_archive_sha"] is not None


# ---------------------------------------------------------------------------
# Task 6.2 -- Test 3: Q4 Byte-Identity -- header-mode field=implicit vs explicit
#
# Schliesst P4-LOW-2 Coverage-Gap: test_v0_2_0_pattern_c_bullet.py prueft nur
# Klassifikations-Aequivalenz. Hier: voller mutate_date_cut-Byte-Identity-Beweis.
# v0.1.x-Style (kein 'field'-Key = implizit header) und v0.2.0-Style
# (explizit field='header') muessen byte-identischen Output liefern.
# ---------------------------------------------------------------------------


def test_header_mode_byte_identity_q4():
    """Q4-Header-Mode-Byte-Identity (Spec SS3.1 + AC1d).

    Beweist dass v0.2.0-runtime classify_date_cut + mutate_date_cut fuer
    header-mode byte-identischen Output liefert -- unabhaengig davon ob
    field-Key fehlt (v0.1.x-Stil) oder explizit auf 'header' gesetzt ist.
    """
    sys.path.insert(0, str(SKILL_ROOT / "scripts"))
    from patterns import classify_date_cut, mutate_date_cut

    # Fixture: repraesentatives Subset des log.md-Formats (## DATE oder ## [DATE])
    md = (
        "## 2026-05-10\n"
        "Entry A body\n"
        "## [2026-05-14]\n"
        "Entry B body\n"
        "## 2026-05-17\n"
        "Entry C body\n"
        "## [2026-05-20]\n"
        "Entry D body\n"
    )
    date_pattern = r"^## \[?(\d{4}-\d{2}-\d{2})\]?"
    pointer_ctx = {
        "cut_date": "2026-05-17",
        "archive_path": "05_Archiv/test-archiv.md",
        "archive_link": "../../05_Archiv/test-archiv.md",
    }

    # v0.1.x-style: kein 'field'-Key (impliziter header-Default)
    cfg_v1 = {
        "cut_before": "2026-05-17",
        "date_parser": {"pattern": date_pattern},
        "archive": {"path": "05_Archiv/test-archiv.md", "header_template": "X"},
        "pointer": {"insert_at": "section_top", "template": "POINTER_{cut_date}"},
    }
    rs_v1 = classify_date_cut(md, section_anchor=None, cfg=cfg_v1)
    out_v1 = mutate_date_cut(
        md, section_anchor=None, rowset=rs_v1, cfg=cfg_v1, pointer_context=pointer_ctx
    )

    # v0.2.0-style: explizit field='header'
    cfg_v2 = {
        "cut_before": "2026-05-17",
        "date_parser": {"field": "header", "pattern": date_pattern},
        "archive": {"path": "05_Archiv/test-archiv.md", "header_template": "X"},
        "pointer": {"insert_at": "section_top", "template": "POINTER_{cut_date}"},
    }
    rs_v2 = classify_date_cut(md, section_anchor=None, cfg=cfg_v2)
    out_v2 = mutate_date_cut(
        md, section_anchor=None, rowset=rs_v2, cfg=cfg_v2, pointer_context=pointer_ctx
    )

    # Byte-Identity-Beweis
    assert out_v1.encode("utf-8") == out_v2.encode("utf-8"), (
        "Q4-Verletzung: header-mode implicit vs explicit liefert unterschiedliche Bytes\n"
        f"v1 bytes: {out_v1.encode('utf-8')!r}\n"
        f"v2 bytes: {out_v2.encode('utf-8')!r}"
    )

    # Sanity: richtige Entries archiviert/behalten
    assert rs_v1.archive == rs_v2.archive
    assert rs_v1.keep == rs_v2.keep
    # pre-cut entries archiviert
    assert any("2026-05-10" in r for r in rs_v1.archive)
    assert any("[2026-05-14]" in r or "2026-05-14" in r for r in rs_v1.archive)
    # cut_before und post-cut entries behalten
    assert any("2026-05-17" in r for r in rs_v1.keep)
    assert any("2026-05-20" in r or "[2026-05-20]" in r for r in rs_v1.keep)
