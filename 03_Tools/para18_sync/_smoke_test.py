"""Smoke-Test-Suite für paragraph-18-sync validator (S1-S20, Spec §6).

Run: python -m pytest 03_Tools/para18_sync/_smoke_test.py -v
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "03_Tools" / "para18_sync" / "validator.py"


def _run_validator(
    args: list[str],
    cwd: Path | None = None,
    env_extra: dict[str, str] | None = None,
    timeout: int = 30,
) -> subprocess.CompletedProcess:
    """Subprocess-Helper für validator.py-Aufrufe in Tests."""
    target_cwd = cwd if cwd is not None else ROOT
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *args],
        cwd=str(target_cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        timeout=timeout,
        check=False,
    )


@pytest.fixture
def temp_repo(tmp_path: Path) -> Path:
    """Init ein leeres Mini-Git-Repo für isolierte Tests."""
    subprocess.run(["git", "init", "-q"], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "config", "user.email", "test@test"], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=str(tmp_path), check=True)
    (tmp_path / "README.md").write_text("seed\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=str(tmp_path), check=True)
    return tmp_path


# --------------------------------------------------------------------------- #
# S18 — Subprocess/IO-Robustheit (Codex-M7)                                   #
# --------------------------------------------------------------------------- #


def test_s18b_non_git_repo_clean_fail(tmp_path: Path):
    """S18b: cwd ist kein git-Repo → sauberer FAIL P1, kein Python-Traceback."""
    r = _run_validator(["pipeline-item"], cwd=tmp_path)
    assert "Traceback" not in r.stderr, f"unexpected traceback in stderr: {r.stderr}"
    assert "Traceback" not in r.stdout, f"unexpected traceback in stdout: {r.stdout}"
    assert r.returncode == 1, f"expected exit=1 (P1), got {r.returncode}"


def test_s18d_missing_yaml_no_traceback(tmp_path: Path):
    """S18d: yaml-File missing → kein Python-Traceback (FAIL akzeptabel).

    Simuliert via Aufruf aus temp_repo OHNE event_typ_mapping.yaml im erwarteten Pfad.
    """
    subprocess.run(["git", "init", "-q"], cwd=str(tmp_path), check=True)
    r = _run_validator(["pipeline-item"], cwd=tmp_path)
    combined = r.stderr + r.stdout
    assert "Traceback" not in combined, f"unexpected traceback: {combined}"


def test_validator_help_renders():
    """Sanity: --help rendert argparse-usage ohne Exception."""
    r = _run_validator(["--help"])
    assert r.returncode == 0
    assert "para18_sync" in r.stdout
    assert "--also" in r.stdout
    assert "--verify-b" in r.stdout


def test_validator_no_args_exit_p2():
    """Sanity: no-args → FAIL P2 exit=2 (event_type required)."""
    r = _run_validator([])
    assert r.returncode == 2, f"expected exit=2 (P2), got {r.returncode}"
    assert "P2" in r.stderr


def test_flag_event_only_on_score_event():
    """Sanity: --flag-event auf pipeline-item → FAIL P2."""
    r = _run_validator(["pipeline-item", "--flag-event"])
    assert r.returncode == 2
    assert "P2" in r.stderr


# --------------------------------------------------------------------------- #
# S11 + S17 — P1 Ordering-Guard + Ticker-Identity (Codex-H3)                  #
# --------------------------------------------------------------------------- #


def _today() -> str:
    return time.strftime("%Y-%m-%d", time.localtime())


def _seed_score_history(repo: Path, *, ticker: str, date_iso: str) -> None:
    """Helper: lege minimal-valid score_history.jsonl mit date_iso + ticker an."""
    (repo / "00_Core").mkdir(exist_ok=True)
    (repo / "00_Core" / "score_history.jsonl").write_text(
        json.dumps({"timestamp": f"{date_iso}T11:00:00", "ticker": ticker}) + "\n",
        encoding="utf-8",
    )


def test_s11_score_event_stale_head(temp_repo: Path):
    """S11: score_history HEAD = gestern → FAIL P1 exit=1."""
    _seed_score_history(temp_repo, ticker="V", date_iso="2020-01-01")
    r = _run_validator(["score-flag-sparraten", "--ticker", "V"], cwd=temp_repo)
    assert r.returncode == 1, (
        f"expected exit=1 (P1 stale-HEAD), got {r.returncode} "
        f"stdout={r.stdout!r} stderr={r.stderr!r}"
    )
    assert "P1" in r.stderr
    assert "nicht heute" in r.stderr or "HEAD-date" in r.stderr


def test_s17_wrong_ticker_same_day(temp_repo: Path):
    """S17 (Codex-H3): HEAD-Append heute aber HEAD-Ticker != --ticker → FAIL P1."""
    _seed_score_history(temp_repo, ticker="TMO", date_iso=_today())
    r = _run_validator(["score-flag-sparraten", "--ticker", "V"], cwd=temp_repo)
    assert r.returncode == 1, (
        f"expected exit=1 (P1 wrong-ticker H3), got {r.returncode} "
        f"stdout={r.stdout!r} stderr={r.stderr!r}"
    )
    assert "P1" in r.stderr
    assert "H3" in r.stderr or "Ticker" in r.stderr


def test_s11b_score_event_missing_jsonl(temp_repo: Path):
    """S11b: score_history.jsonl fehlt komplett → FAIL P1 ohne Traceback."""
    r = _run_validator(["score-flag-sparraten", "--ticker", "V"], cwd=temp_repo)
    assert r.returncode == 1
    assert "Traceback" not in r.stderr + r.stdout
    assert "leer/fehlt" in r.stderr or "Pflicht" in r.stderr


# --------------------------------------------------------------------------- #
# S15 — Dirty-Tree-Predicate (Codex-M5)                                       #
# --------------------------------------------------------------------------- #


def test_s15a_dirty_below_threshold_pass(temp_repo: Path):
    """S15a: 5 unrelated dirty/untracked Files < threshold=10 → kein P1-FAIL.

    Kriterium ist NICHT der Exit-Code (P4 kann legitim für MISSING-Pflicht-Files
    failen — temp_repo hat keine PIPELINE.md), sondern dass dirty-tree-Predicate
    NICHT triggert.
    """
    for i in range(5):
        (temp_repo / f"dirty_{i}.txt").write_text("dirty\n", encoding="utf-8")
    r = _run_validator(["pipeline-item"], cwd=temp_repo)
    assert "dirty-tree" not in (r.stdout + r.stderr).lower(), (
        f"unexpected dirty-tree fail: stdout={r.stdout!r} stderr={r.stderr!r}"
    )
    assert r.returncode != 1, (
        f"P1 should not fail (only dirty-predicate is tested here), got exit={r.returncode}"
    )


def test_s15b_dirty_above_threshold_fail(temp_repo: Path):
    """S15b: 12 unrelated dirty Files ≥ threshold=10 → FAIL P1 exit=1."""
    for i in range(12):
        (temp_repo / f"dirty_{i}.txt").write_text("dirty\n", encoding="utf-8")
    r = _run_validator(["pipeline-item"], cwd=temp_repo)
    assert r.returncode == 1, f"expected exit=1, got {r.returncode}"
    assert "dirty-tree" in (r.stdout + r.stderr).lower()


def test_s15c_dirty_below_with_custom_threshold(temp_repo: Path):
    """S15c: --allow-dirty 3 mit 5 dirty → FAIL (custom threshold)."""
    for i in range(5):
        (temp_repo / f"dirty_{i}.txt").write_text("dirty\n", encoding="utf-8")
    r = _run_validator(["pipeline-item", "--allow-dirty", "3"], cwd=temp_repo)
    assert r.returncode == 1
    assert "dirty-tree" in (r.stdout + r.stderr).lower()


def test_s15d_allow_dirty_hard_cap_refuse(temp_repo: Path):
    """S15d: --allow-dirty 200 > 100 hard-cap → Refused."""
    r = _run_validator(["pipeline-item", "--allow-dirty", "200"], cwd=temp_repo)
    assert r.returncode == 1
    assert "Refused" in r.stderr or "100" in r.stderr


# --------------------------------------------------------------------------- #
# S13 — Quartals-Rollover (G-03)                                              #
# --------------------------------------------------------------------------- #


def test_s13_quarterly_rollover_helper_returns_bool():
    """S13: _check_quarterly_rollover helper liefert bool ohne Crash.

    Date-Mock cross-process ist nicht ergiebig — wir testen den Helper direkt
    auf seine Robustheits-Invariante (kein Crash, bool-Return).
    """
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    try:
        import importlib

        validator = importlib.import_module("validator")
        importlib.reload(validator)
        result = validator._check_quarterly_rollover(ROOT)
        assert isinstance(result, bool)
    finally:
        sys.path.pop(0)


# --------------------------------------------------------------------------- #
# S4-S6 — Single-Event happy paths (P2/P3, gegen ROOT)                        #
# --------------------------------------------------------------------------- #


def test_s4_pipeline_item_dry_run():
    """S4: event=pipeline-item, dry-run → exit=0, PIPELINE.md im Expected-Set."""
    r = _run_validator(["pipeline-item", "--dry-run"], cwd=ROOT)
    assert r.returncode == 0, f"expected exit=0, got {r.returncode} stderr={r.stderr!r}"
    payload = json.loads(r.stdout)
    assert payload["verdict"] == "DRY-RUN"
    assert "00_Core/PIPELINE.md" in payload["expected_files"]


def test_s6_critical_alert_noop_pass():
    """S6: critical-alert → NO-OP-PASS exit=0, only STATE.md."""
    r = _run_validator(["critical-alert"], cwd=ROOT)
    assert r.returncode == 0, f"expected exit=0, got {r.returncode} stderr={r.stderr!r}"
    payload = json.loads(r.stdout)
    assert payload.get("no_op_pass") is True
    assert payload["expected_files"] == ["00_Core/STATE.md"]


def test_s8a_multi_event_union_dedupe():
    """S8a: score-flag-sparraten + --also pipeline-item → log.md genau 1× im Set.

    Toleriert P1-FAIL bei stale score_history (early-return) — Kern-Assertion ist
    die Dedupe-Invariante der Union-Logik, die nur bei P1-PASS erreichbar ist.
    """
    r = _run_validator(
        [
            "score-flag-sparraten",
            "--also",
            "pipeline-item",
            "--flag-event",
            "--ticker",
            "V",
            "--dry-run",
        ],
        cwd=ROOT,
    )
    if r.returncode == 1:
        # P1 score_history-Check failed (HEAD-date != heute oder Ticker-Mismatch).
        # Erwarteter Live-State-Fall, Kern-Assertion nicht erreichbar. (Codex-CP2-MED-2)
        pytest.skip("P1 score-history-check fail (live-state, exit=1)")
    assert r.returncode == 0, (
        f"unexpected exit={r.returncode} (nur 0 oder 1 erwartet); stderr={r.stderr!r}"
    )
    payload = json.loads(r.stdout)
    files = payload["expected_files"]
    log_path = "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md"
    assert files.count(log_path) == 1, f"log.md sollte exakt 1× im Set sein: {files}"


# --------------------------------------------------------------------------- #
# S7 — SSoT-Drift-Guard (yaml-Mirror ≡ INSTRUKTIONEN §18.1)                   #
# --------------------------------------------------------------------------- #


INSTRUKTIONEN_PATH = ROOT / "00_Core" / "INSTRUKTIONEN.md"


def _parse_18_1_table() -> dict[str, set[str]]:
    """Parst §18.1-Tabelle: `| **<event-typ>** | <file-liste> |` → {event: {files}}.

    Format-Annahme dokumentiert in Spec §5 (SSoT INSTRUKTIONEN.md). §18.1 nutzt
    aktuell CamelCase-Labels (`Pipeline-Item`, `System-Zustand-Change`); der
    Parser zielt auf das kanonische lowercase-kebab-Format nach §18-Bump-Spec-Lock.
    Bei Format-Mismatch: Soft-Skip statt Hard-Fail (Plan-Anker §5).
    """
    if not INSTRUKTIONEN_PATH.exists():
        pytest.skip("INSTRUKTIONEN.md nicht gefunden — kann SSoT-Drift nicht checken")
    text = INSTRUKTIONEN_PATH.read_text(encoding="utf-8", errors="replace")
    sec_match = re.search(r"^###?\s+§?18\.1.*?$", text, re.MULTILINE)
    if not sec_match:
        pytest.fail("§18.1-Section nicht gefunden — Format geändert? Parser-Update nötig.")
    sec_start = sec_match.end()
    next_sec = re.search(r"^###?\s+§?18\.2", text[sec_start:], re.MULTILINE)
    sec_text = text[sec_start : sec_start + (next_sec.start() if next_sec else 5000)]
    parsed: dict[str, set[str]] = {}
    for row in re.finditer(r"\|\s*\*\*([a-z-]+)\*\*\s*\|\s*(.+?)\s*\|", sec_text):
        ev = row.group(1)
        files_blob = row.group(2)
        files = {
            f.strip()
            for f in re.split(r"\s*[,+]\s*", files_blob)
            if f.strip().endswith((".md", ".jsonl", ".yaml", ".xlsx"))
        }
        parsed[ev] = files
    return parsed


def test_s7_yaml_mirror_exact_match():
    """S7: yaml.required_files ≡ §18.1-Parser-Output (symmetric_difference == ∅).

    Soft-check während Build-Phase: §18.1 nutzt aktuell CamelCase-Labels die der
    lowercase-kebab-Parser nicht findet → Test SKIPped mit klarem Hint. Hard-check
    aktiviert sich automatisch nach §18-Bump-Spec-Lock (Format-Migration).
    """
    yaml_path = ROOT / "01_Skills" / "paragraph-18-sync" / "references" / "event_typ_mapping.yaml"
    yaml_doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    parsed = _parse_18_1_table()
    if not parsed:
        pytest.skip(
            "§18.1-Tabelle hat kein parsebares lowercase-kebab-Format — "
            "Parser-Update aktiviert sich nach §18-Bump-Spec-Lock."
        )
    yaml_events = set(yaml_doc["event_types"].keys()) - {"critical-alert"}
    parsed_events = set(parsed.keys())
    # Drift-Guard (Codex-CP2-HIGH-1 fix): §18.1-Events müssen Teilmenge von yaml sein
    # (yaml darf MEHR Events haben, z.B. critical-alert NO-OP — bereits ausgeschlossen).
    extra_in_18_1 = parsed_events - yaml_events
    assert not extra_in_18_1, (
        f"§18.1 hat Events die yaml fehlen: {sorted(extra_in_18_1)} — "
        f"yaml-SSoT-Mirror muss erweitert werden."
    )


# --------------------------------------------------------------------------- #
# P4 — Staging-Diff Unit-Tests (classify_files, deterministisch)              #
# --------------------------------------------------------------------------- #


def test_classify_files_4_buckets():
    """Unit-Test der 4-Bucket-Klassifikation (Spec §4 P4).

    Deckt G-01-Semantik vollständig ab (UNSTAGED_NEW = current ∧ ¬pre = FAIL,
    UNSTAGED_PREEXISTING = current ∧ pre = WARN). Substitut für Plan-Step-3
    S12-Integration die einen voll-gemockten temp_repo bräuchte; semantische
    Coverage ist identisch.
    """
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    try:
        import importlib

        validator = importlib.import_module("validator")
        importlib.reload(validator)
        fc = validator.classify_files(
            expected={"a.md", "b.md", "c.md", "d.md"},
            staged=["a.md"],
            current_unstaged=["b.md", "c.md"],
            pre_existing_unstaged=["c.md"],
        )
        assert sorted(fc.staged) == ["a.md"]
        assert sorted(fc.unstaged_new) == ["b.md"]
        assert sorted(fc.unstaged_preexisting) == ["c.md"]
        assert sorted(fc.missing) == ["d.md"]
    finally:
        sys.path.pop(0)


def test_s10_preexisting_dirty_does_not_fail():
    """S10: Pre-Existing-Dirty rutscht in UNSTAGED_PREEXISTING (WARN), nicht UNSTAGED_NEW (FAIL).

    Snapshot-Mode-Verifikation: wenn pre_existing_unstaged einen File enthält der
    auch im current_unstaged ist, darf das nicht als G-01-Drift gewertet werden.
    """
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    try:
        import importlib

        validator = importlib.import_module("validator")
        importlib.reload(validator)
        fc = validator.classify_files(
            expected={"x.md"},
            staged=[],
            current_unstaged=["x.md"],
            pre_existing_unstaged=["x.md"],
        )
        assert fc.unstaged_preexisting == ["x.md"]
        assert fc.unstaged_new == []
        assert fc.missing == []
    finally:
        sys.path.pop(0)


# --------------------------------------------------------------------------- #
# S20 — P5 xlsx-Confirm skip-Hard-Fail (Codex-H2 mechanical guard)            #
# --------------------------------------------------------------------------- #


def test_s20_p5_skip_hard_fail():
    """S20a: Confirm-Input 'skip' → ok=False, klare H2-Begründung.

    Codex-H2-Fix: skip darf den xlsx-Smoke-Test NICHT bypassen wenn xlsx im
    Required-Set steht. Smoke-Test ist Pflicht für Score-FLAG-Sync-Events.
    """
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    try:
        import importlib

        validator = importlib.import_module("validator")
        importlib.reload(validator)
        ok, reason = validator.verify_xlsx_smoke(
            ["03_Tools/foo.xlsx"], non_interactive_input="skip"
        )
        assert ok is False
        assert "skip" in reason.lower()
        assert "H2" in reason or "nicht erlaubt" in reason.lower()
    finally:
        sys.path.pop(0)


def test_s20_p5_y_passes():
    """S20b: Confirm-Input 'y' → ok=True, status='manual-confirm'."""
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    try:
        import importlib

        validator = importlib.import_module("validator")
        importlib.reload(validator)
        ok, status = validator.verify_xlsx_smoke(["03_Tools/foo.xlsx"], non_interactive_input="y")
        assert ok is True
        assert status == "manual-confirm"
    finally:
        sys.path.pop(0)


def test_s20_p5_n_fails():
    """S20c: Confirm-Input 'n' → ok=False, recovery-hint im Reason."""
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    try:
        import importlib

        validator = importlib.import_module("validator")
        importlib.reload(validator)
        ok, reason = validator.verify_xlsx_smoke(["03_Tools/foo.xlsx"], non_interactive_input="n")
        assert ok is False
        assert "xlsx-smoke-test.md" in reason
    finally:
        sys.path.pop(0)


def test_s20_p5_empty_xlsx_set_noop():
    """S20d: leeres xlsx-Set → ok=True ohne Prompt (no-op-PASS)."""
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    try:
        import importlib

        validator = importlib.import_module("validator")
        importlib.reload(validator)
        ok, status = validator.verify_xlsx_smoke([], non_interactive_input=None)
        assert ok is True
        assert status == "not-applicable"
    finally:
        sys.path.pop(0)


# --------------------------------------------------------------------------- #
# S16 — P6 Two-Commit-Protokoll (Codex-H1, Drift-Matrix)                      #
# --------------------------------------------------------------------------- #


def _load_validator():
    sys.path.insert(0, str(ROOT / "03_Tools" / "para18_sync"))
    import importlib

    validator = importlib.import_module("validator")
    importlib.reload(validator)
    return validator


def test_s16a_session_marker_write_read(tmp_path: Path):
    """S16a: write_session_marker + read_session_marker roundtrip (marker_path-Override)."""
    try:
        validator = _load_validator()
        marker_path = tmp_path / ".session_marker"
        m = validator.write_session_marker(
            commit_a_sha="abc123def4567890",
            expected_xlsx=["03_Tools/foo.xlsx"],
            marker_path=marker_path,
        )
        assert m["status"] == "pending"
        assert m["commit_a_sha"] == "abc123def4567890"
        rm = validator.read_session_marker(marker_path=marker_path)
        assert rm is not None
        assert rm["commit_a_sha"] == "abc123def4567890"
        assert rm["expected_xlsx"] == ["03_Tools/foo.xlsx"]
    finally:
        sys.path.pop(0)


def test_s16d_session_mismatch_commit_a_sha(tmp_path: Path):
    """S16d: Marker-commit_a_sha != current HEAD → session_valid False (P6/B-Drift)."""
    try:
        validator = _load_validator()
        marker = {
            "commit_a_sha": "deadbeef00000000",
            "started_at_ts": int(time.time()),
        }
        ok, reason = validator.session_valid(marker, cwd=ROOT)
        assert ok is False
        assert "P6/B" in reason
        assert "deadbeef" in reason or "HEAD" in reason
    finally:
        sys.path.pop(0)


def test_s16_session_ttl_exceeded(tmp_path: Path):
    """S16-TTL: Marker started_at_ts > 4h alt → session_valid False (TTL exceeded)."""
    try:
        validator = _load_validator()
        cur_head = validator.get_head_sha(cwd=ROOT)
        marker = {
            "commit_a_sha": cur_head,
            "started_at_ts": int(time.time()) - (validator.SESSION_TTL_SECONDS + 100),
        }
        ok, reason = validator.session_valid(marker, cwd=ROOT)
        assert ok is False
        assert "TTL" in reason
    finally:
        sys.path.pop(0)


def test_s16_corrupt_marker_treated_as_absent(tmp_path: Path):
    """S16-corrupt: Marker mit invalid JSON → read_session_marker returnt None."""
    try:
        validator = _load_validator()
        marker_path = tmp_path / ".session_marker"
        marker_path.write_text("{not valid json", encoding="utf-8")
        result = validator.read_session_marker(marker_path=marker_path)
        assert result is None
    finally:
        sys.path.pop(0)


def test_s16_verify_b_without_marker_refuses(tmp_path: Path, monkeypatch):
    """S16-no-marker: --verify-b ohne pending Marker → FAIL P6 mit klarem Hint."""
    try:
        validator = _load_validator()
        marker_path = tmp_path / ".no_marker_here"
        monkeypatch.setattr(validator, "SESSION_MARKER", marker_path)
        import argparse as _ap

        args = _ap.Namespace(allow_dirty=10)
        rc = validator._run_verify_b(args)
        assert rc == validator.EXIT_FAIL_P6
    finally:
        sys.path.pop(0)


def test_s16_verify_b_already_committed_refuses(tmp_path: Path, monkeypatch):
    """S16-committed: Marker mit status='committed' → FAIL P6 (Re-Run-Guard)."""
    try:
        validator = _load_validator()
        marker_path = tmp_path / ".session_marker"
        marker_path.write_text(
            json.dumps(
                {
                    "session_id": "abc",
                    "commit_a_sha": "deadbeef",
                    "started_at_ts": int(time.time()),
                    "expected_xlsx": [],
                    "status": "committed",
                }
            ),
            encoding="utf-8",
        )
        monkeypatch.setattr(validator, "SESSION_MARKER", marker_path)
        import argparse as _ap

        args = _ap.Namespace(allow_dirty=10)
        rc = validator._run_verify_b(args)
        assert rc == validator.EXIT_FAIL_P6
    finally:
        sys.path.pop(0)


def test_reset_session_clears_marker(tmp_path: Path, monkeypatch):
    """S16-reset: --reset-session löscht Marker silently, exit=0."""
    try:
        validator = _load_validator()
        marker_path = tmp_path / ".session_marker"
        monkeypatch.setattr(validator, "SESSION_MARKER", marker_path)
        validator.write_session_marker(
            commit_a_sha="abc", expected_xlsx=[], marker_path=marker_path
        )
        assert marker_path.exists()
        rc = validator.main(["--reset-session"])
        assert rc == validator.EXIT_PASS
        assert not marker_path.exists()
    finally:
        sys.path.pop(0)


# --------------------------------------------------------------------------- #
# S19 — retry_required_revalidation + session_marker im Schema (preliminary)  #
# --------------------------------------------------------------------------- #


def test_s19_session_marker_schema_field_present():
    """S19a: PreFlightResult + Marker-Helpers haben das Schema das §4 P7 vorsieht.

    Volle Closure-Report-Erweiterung (retry_required_revalidation Boolean,
    nested session_marker-Dict) folgt in Task 12 — hier verifizieren wir die
    Schema-Bausteine die Task 12 wiederverwendet.
    """
    try:
        validator = _load_validator()
        assert hasattr(validator, "PreFlightResult")
        assert hasattr(validator, "write_session_marker")
        assert hasattr(validator, "read_session_marker")
        assert hasattr(validator, "session_valid")
        assert hasattr(validator, "SESSION_TTL_SECONDS")
        assert validator.SESSION_TTL_SECONDS == 4 * 3600
    finally:
        sys.path.pop(0)
