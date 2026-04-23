"""Smoke tests for the system_audit package.

Run: python 03_Tools/system_audit/_smoke_test.py
"""
from __future__ import annotations

import sys

# Python auto-inserts the script's directory (03_Tools/system_audit/) at
# sys.path[0] on launch.  That shadows the stdlib 'types' module with our
# package-local types.py, breaking the stdlib import chain before any user
# code runs.  Pop it when detected; the explicit sys.path.insert below
# re-adds 03_Tools so 'system_audit.types' still resolves as a qualified
# sub-module (no conflict with stdlib 'types').
# NOTE: resolve()-variant (Path(__file__).resolve().parent) was tested and
# breaks on Python 3.14.3 — 'from pathlib import Path' itself triggers
# functools → types → shadow before the pop runs.  Keeping endswith-guard.
if sys.path and sys.path[0].endswith("system_audit"):
    sys.path.pop(0)

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "03_Tools"))

from system_audit.types import AuditContext, CheckResult, FailureDetail


def test_check_result_pass_semantics() -> None:
    r = CheckResult(
        name="demo", status="PASS", n_checked=3, n_passed=3,
        failures=[], duration_ms=10, category="core",
    )
    assert r.status == "PASS"
    assert not r.failures

def test_check_result_fail_error() -> None:
    r = CheckResult(
        name="demo", status="FAIL", n_checked=3, n_passed=2,
        failures=[FailureDetail(
            location="x.md:1", expected="a", actual="b",
            severity="error", hint=None,
        )],
        duration_ms=10, category="core",
    )
    assert any(f.severity == "error" for f in r.failures)

def test_check_result_warn_is_not_fail() -> None:
    r = CheckResult(
        name="demo", status="WARN", n_checked=3, n_passed=2,
        failures=[FailureDetail(
            location="x.md:1", expected="fresh", actual="stale",
            severity="warning", hint=None,
        )],
        duration_ms=10, category="core",
    )
    assert r.status == "WARN"
    assert all(f.severity == "warning" for f in r.failures)

def test_audit_context_repo_root() -> None:
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False, vault_timeout_s=20)
    assert ctx.repo_root == REPO_ROOT
    assert ctx.include_optional is False


def test_failure_detail_is_frozen() -> None:
    import dataclasses
    f = FailureDetail(
        location="x", expected="a", actual="b",
        severity="error", hint=None,
    )
    try:
        f.location = "y"
    except dataclasses.FrozenInstanceError:
        return
    raise AssertionError("FailureDetail should be frozen")


def test_check_result_skip_status() -> None:
    r = CheckResult(
        name="demo", status="SKIP", n_checked=0, n_passed=0,
        duration_ms=0, category="core",
    )
    assert r.status == "SKIP"
    assert r.failures == []


def test_check_result_failures_mutable() -> None:
    r = CheckResult(
        name="demo", status="FAIL", n_checked=1, n_passed=0,
        duration_ms=0, category="core",
    )
    r.failures.append(FailureDetail(
        location="x", expected="a", actual="b",
        severity="error", hint=None,
    ))
    assert len(r.failures) == 1


def test_jsonl_schema_pass_on_good_fixture() -> None:
    from system_audit.checks.jsonl_schema import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "jsonl_schema"
    result = run(REPO_ROOT, ctx, stores_override={
        "score_history": fx / "good_score.jsonl",
        "flag_events": fx / "empty.jsonl",
        "portfolio_returns": fx / "empty.jsonl",
        "benchmark_series": fx / "empty.jsonl",
    })
    assert result.status in ("PASS", "WARN", "SKIP"), f"expected PASS/WARN/SKIP, got {result.status}"
    assert all(f.severity != "error" for f in result.failures)

def test_jsonl_schema_fail_on_bad_fixture() -> None:
    from system_audit.checks.jsonl_schema import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "jsonl_schema"
    result = run(REPO_ROOT, ctx, stores_override={
        "score_history": fx / "bad_score.jsonl",
        "flag_events": fx / "empty.jsonl",
        "portfolio_returns": fx / "empty.jsonl",
        "benchmark_series": fx / "empty.jsonl",
    })
    assert result.status == "FAIL"
    assert any(f.severity == "error" for f in result.failures)
    assert any("bad_score.jsonl:1" in f.location for f in result.failures)

def test_jsonl_schema_skip_on_missing_file(tmp_path=None) -> None:
    from system_audit.checks.jsonl_schema import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, stores_override={
        "score_history": REPO_ROOT / "does" / "not" / "exist.jsonl",
        "flag_events": REPO_ROOT / "no.jsonl",
        "portfolio_returns": REPO_ROOT / "no.jsonl",
        "benchmark_series": REPO_ROOT / "no.jsonl",
    })
    assert result.status == "SKIP"
    assert all(f.severity == "warning" for f in result.failures)


def test_store_freshness_warn_on_stale() -> None:
    import tempfile, json, datetime
    from system_audit.checks.store_freshness import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        pr = tdp / "portfolio_returns.jsonl"
        bs = tdp / "benchmark-series.jsonl"
        # 14 calendar days = ≥10 business days, robust to long-weekend execution
        stale = (datetime.date.today() - datetime.timedelta(days=14)).isoformat()
        pr.write_text(json.dumps({"schema_version":"1.0","date":stale}) + "\n", encoding="utf-8")
        bs.write_text(json.dumps({"schema_version":"1.0","date":stale}) + "\n", encoding="utf-8")
        ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
        result = run(REPO_ROOT, ctx, stores_override={
            "portfolio_returns": pr,
            "benchmark_series": bs,
        })
    assert result.status == "WARN"
    assert all(f.severity == "warning" for f in result.failures)
    assert len(result.failures) == 2

def test_store_freshness_pass_on_fresh() -> None:
    import tempfile, json, datetime
    from system_audit.checks.store_freshness import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        pr = tdp / "portfolio_returns.jsonl"
        bs = tdp / "benchmark-series.jsonl"
        today = datetime.date.today().isoformat()
        pr.write_text(json.dumps({"schema_version":"1.0","date":today}) + "\n", encoding="utf-8")
        bs.write_text(json.dumps({"schema_version":"1.0","date":today}) + "\n", encoding="utf-8")
        ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
        result = run(REPO_ROOT, ctx, stores_override={
            "portfolio_returns": pr, "benchmark_series": bs,
        })
    assert result.status == "PASS"
    assert result.failures == []

def test_store_freshness_skip_on_missing() -> None:
    from system_audit.checks.store_freshness import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, stores_override={
        "portfolio_returns": REPO_ROOT / "does-not-exist-1.jsonl",
        "benchmark_series": REPO_ROOT / "does-not-exist-2.jsonl",
    })
    assert result.status == "SKIP"


def test_markdown_header_pass_on_aligned() -> None:
    from system_audit.checks.markdown_header import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "markdown_header"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, targets_override=[
        (fx / "state_ok.md", "state"),
        (fx / "core_memory_ok.md", "core_memory"),
        (fx / "faktortabelle_ok.md", "faktortabelle"),
    ])
    assert result.status == "PASS", f"got {result.status}, failures={result.failures}"

def test_markdown_header_fail_on_stale() -> None:
    from system_audit.checks.markdown_header import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "markdown_header"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, targets_override=[
        (fx / "state_stale.md", "state"),
    ])
    assert result.status == "FAIL"
    assert any(f.severity == "error" for f in result.failures)

def test_markdown_header_warn_on_lag() -> None:
    from system_audit.checks.markdown_header import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "markdown_header"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, targets_override=[
        (fx / "state_warn.md", "state"),
    ])
    assert result.status == "WARN"
    assert all(f.severity == "warning" for f in result.failures)
    assert len(result.failures) == 1


def test_markdown_header_excludes_future_dates() -> None:
    """Long-Term-Gates (2028-04-01) + Earnings-Dates (next-week) must not count
    as 'newest event' — Stand is journal-catch-up, not future-planning-foresight."""
    import datetime as _dt
    import tempfile
    from system_audit.checks.markdown_header import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        doc = tdp / "state_with_future.md"
        doc.write_text(
            "# STATE\n"
            "**Stand:** 23.04.2026\n\n"
            "Latest update was 23.04.2026. Pipeline contains 2028-04-01 Review-Gate "
            "and 29.04.2026 MSFT earnings as future planning markers.\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        # Freeze "today" to 2026-04-23 so both 29.04.2026 and 2028-04-01 are future
        result = run(tdp, ctx,
                     targets_override=[(doc, "state")],
                     today=_dt.date(2026, 4, 23))
    assert result.status == "PASS", f"got {result.status}, failures={result.failures}"
    assert result.failures == []


def test_cross_source_pass_on_aligned() -> None:
    from system_audit.checks.cross_source import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "cross_source"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, sources_override={
        "config": fx / "config.yaml",
        "state": fx / "state.md",
        "faktortabelle": fx / "faktortabelle.md",
        "vault_entities_dir": None,
    })
    assert result.status in ("PASS", "WARN"), f"got {result.status}, failures={result.failures}"
    assert all(f.severity != "error" for f in result.failures)

def test_cross_source_fail_on_divergence() -> None:
    import shutil, tempfile
    from system_audit.checks.cross_source import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "cross_source"
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        shutil.copy(fx / "config.yaml", tdp / "config.yaml")
        shutil.copy(fx / "faktortabelle.md", tdp / "faktortabelle.md")
        state = (fx / "state.md").read_text(encoding="utf-8").replace("AVGO | 84", "AVGO | 85")
        (tdp / "state.md").write_text(state, encoding="utf-8")
        ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
        result = run(REPO_ROOT, ctx, sources_override={
            "config": tdp / "config.yaml",
            "state": tdp / "state.md",
            "faktortabelle": tdp / "faktortabelle.md",
            "vault_entities_dir": None,
        })
    assert result.status == "FAIL"
    assert any("AVGO" in f.actual for f in result.failures)

def test_flag_parser_all_six_variants() -> None:
    """Spec §7.3 Parser-Golden-Test: alle 6 beobachteten FLAG-Strings."""
    from system_audit.checks.cross_source import parse_flag_icon
    assert parse_flag_icon("✅") == ("ok", None)
    assert parse_flag_icon("⚠️ Insider-Review") == ("warn", "Insider-Review")
    assert parse_flag_icon("✅ Insurance Exception") == ("ok", "Insurance Exception")
    assert parse_flag_icon("✅ Screener-Exception") == ("ok", "Screener-Exception")
    assert parse_flag_icon("🔴 Score-basiert") == ("flag", "Score-basiert")
    assert parse_flag_icon("🔴 CapEx/OCF 83.6%") == ("flag", "CapEx/OCF 83.6%")

def test_flag_mismatch_matrix() -> None:
    """Spec §5.1 Check-3 FLAG-Matrix."""
    from system_audit.checks.cross_source import compare_flag
    assert compare_flag(False, "ok") == "match"
    assert compare_flag(False, "warn") == "warning"
    assert compare_flag(False, "flag") == "error"
    assert compare_flag(True, "flag") == "match"
    assert compare_flag(True, "ok") == "error"
    assert compare_flag(True, "warn") == "error"


def test_existence_pass_on_existing_paths() -> None:
    import tempfile
    from system_audit.checks.existence import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "target.py").write_text("", encoding="utf-8")
        (tdp / "doc.md").write_text("Siehe `target.py` und `absent.py`.", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx, scan_files_override=[tdp / "doc.md"])
    assert result.status == "FAIL"
    assert any("absent.py" in f.actual for f in result.failures)
    assert not any("target.py" in f.actual for f in result.failures)


def test_existence_ignores_paths_with_spaces() -> None:
    """PATH_RE by design ignores space-containing paths (e.g. '07_Obsidian Vault/...')."""
    import tempfile
    from system_audit.checks.existence import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "doc.md").write_text(
            "Backtick ref without spaces: `foo.py`\n"
            "Backtick ref WITH spaces: `07_Obsidian Vault/log.md`\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx, scan_files_override=[tdp / "doc.md"])
    # foo.py is missing → 1 error; space-ref is not detected at all → no second error
    assert result.status == "FAIL"
    assert len([f for f in result.failures if f.severity == "error"]) == 1
    assert any("foo.py" in f.actual for f in result.failures)
    assert not any("Obsidian" in f.actual for f in result.failures)


def _make_skill(root: Path, name: str, version: str) -> None:
    d = root / "01_Skills" / name
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\nversion: {version}\n---\n\n# {name}\n",
        encoding="utf-8",
    )

def _make_zip(root: Path, name: str, version: str) -> None:
    (root / "06_Skills-Pakete").mkdir(parents=True, exist_ok=True)
    (root / "06_Skills-Pakete" / f"{name}_v{version}.zip").write_text("", encoding="utf-8")

def test_skill_version_pass_fixture() -> None:
    """PASS: SKILL.md == ZIP version."""
    import tempfile
    from system_audit.checks.skill_version import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        _make_skill(tdp, "demo", "1.0.0")
        _make_zip(tdp, "demo", "1.0.0")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status == "PASS", f"got {result.status}, failures={result.failures}"
    assert result.failures == []

def test_skill_version_warn_on_unpacked_newer_fixture() -> None:
    """WARN: SKILL.md v2.0.0 aber hoechste ZIP nur v1.9.0 (ungepackt)."""
    import tempfile
    from system_audit.checks.skill_version import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        _make_skill(tdp, "demo", "2.0.0")
        _make_zip(tdp, "demo", "1.9.0")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status == "WARN"
    assert any("1.9.0" in f.actual for f in result.failures)

def test_skill_version_warn_on_orphan_zip_fixture() -> None:
    """WARN: ZIP ohne passendes 01_Skills/<name>/."""
    import tempfile
    from system_audit.checks.skill_version import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "01_Skills").mkdir()
        (tdp / "06_Skills-Pakete").mkdir()
        (tdp / "06_Skills-Pakete" / "ghost_v1.0.0.zip").write_text("", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status == "WARN"
    assert any("orphan" in (f.actual + (f.hint or "")).lower() or "ghost" in f.location for f in result.failures)

def test_skill_version_pass_on_bare_zip_fixture() -> None:
    """PASS: SKILL.md vN.N.N + non-versioned <name>.zip (accepted convention)."""
    import tempfile
    from system_audit.checks.skill_version import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        _make_skill(tdp, "demo", "1.0.0")
        (tdp / "06_Skills-Pakete").mkdir(parents=True, exist_ok=True)
        (tdp / "06_Skills-Pakete" / "demo.zip").write_text("", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status == "PASS", f"got {result.status}, failures={result.failures}"
    assert result.failures == []


def test_skill_version_warn_on_orphan_bare_zip_fixture() -> None:
    """WARN: bare-name ZIP ohne passendes 01_Skills/<name>/ oder _extern/<name>/."""
    import tempfile
    from system_audit.checks.skill_version import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "01_Skills").mkdir()
        (tdp / "06_Skills-Pakete").mkdir()
        (tdp / "06_Skills-Pakete" / "ghost-bare.zip").write_text("", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status == "WARN"
    assert any("ghost-bare" in f.location for f in result.failures)


def test_skill_version_pass_on_extern_bare_zip_fixture() -> None:
    """PASS: bare-ZIP deren Name = _extern/<name>/-Subfolder matcht → kein Orphan."""
    import tempfile
    from system_audit.checks.skill_version import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "01_Skills" / "_extern" / "external-skill").mkdir(parents=True)
        (tdp / "06_Skills-Pakete").mkdir()
        (tdp / "06_Skills-Pakete" / "external-skill.zip").write_text("", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status == "PASS", f"got {result.status}, failures={result.failures}"
    assert result.failures == []


def test_skill_version_skip_on_missing_frontmatter_fixture() -> None:
    """EDGE: SKILL.md ohne version-Frontmatter -> nicht gecheckt, kein Fail."""
    import tempfile
    from system_audit.checks.skill_version import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        d = tdp / "01_Skills" / "demo"
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text("# demo — no frontmatter\n", encoding="utf-8")
        (tdp / "06_Skills-Pakete").mkdir()
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status in ("PASS", "SKIP"), f"got {result.status}"
    assert not any(f.severity == "error" for f in result.failures)


def test_pipeline_ssot_parser_three_variants() -> None:
    """Spec §7.3 Parser-Golden-Test."""
    from system_audit.checks.pipeline_ssot import extract_plan_refs
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "pipeline_ssot"
    full = extract_plan_refs((fx / "state_full.md").read_text(encoding="utf-8"))
    assert set(full) == {
        "docs/superpowers/plans/2026-04-21-foo.md",
        "docs/superpowers/plans/2026-04-20-bar.md",
        "docs/superpowers/plans/2026-04-20-baz.md",
    }
    empty = extract_plan_refs((fx / "state_empty.md").read_text(encoding="utf-8"))
    assert empty == []
    broken = extract_plan_refs((fx / "state_broken.md").read_text(encoding="utf-8"))
    assert broken == ["docs/superpowers/plans/2099-12-31-nonexistent.md"]

def test_pipeline_ssot_pass_on_live_state() -> None:
    from system_audit.checks.pipeline_ssot import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx)
    assert result.status == "PASS", f"failures={result.failures}"

def test_pipeline_ssot_fail_on_broken_ref() -> None:
    from system_audit.checks.pipeline_ssot import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "pipeline_ssot"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, state_path_override=fx / "state_broken.md")
    assert result.status == "FAIL"
    assert any("nonexistent.md" in f.actual for f in result.failures)


def test_log_lag_live_repo_pass() -> None:
    from system_audit.checks.log_lag import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx)
    assert result.status in ("PASS", "SKIP"), f"failures={result.failures}"

def test_log_lag_fail_on_stale() -> None:
    import tempfile, subprocess
    from system_audit.checks.log_lag import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        subprocess.run(["git", "init", "-q"], cwd=tdp, check=True)
        subprocess.run(["git", "-c", "user.name=T", "-c", "user.email=t@t", "commit",
                        "--allow-empty", "-m", "init"], cwd=tdp, check=True, capture_output=True)
        vault = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki"
        vault.mkdir(parents=True)
        (vault / "log.md").write_text("## [2020-01-01] historical\n", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx)
    assert result.status == "FAIL"


def test_report_human_format_contains_summary() -> None:
    from system_audit.report import render_human
    results = [
        CheckResult(name="jsonl_schema", status="PASS", n_checked=27, n_passed=27,
                    failures=[], duration_ms=128, category="core"),
        CheckResult(name="cross_source", status="FAIL", n_checked=11, n_passed=10,
                    failures=[FailureDetail(
                        location="00_Core/STATE.md:18",
                        expected="AVGO Score=84", actual="Score=85",
                        severity="error", hint="STATE.md-Zeile aktualisieren",
                    )], duration_ms=91, category="core"),
    ]
    text = render_human(results, timestamp_utc="2026-04-21T14:32:41Z")
    assert "Check-1" in text or "jsonl_schema" in text
    assert "✅" in text or "PASS" in text
    assert "❌" in text or "FAIL" in text
    assert "AVGO" in text
    assert "Exit-Code: 1" in text

def test_report_human_severity_icons_and_grouping() -> None:
    """Regression-gate: WARN-Semantik pro-failure (⚠️/🔴/ℹ️) + Batch-Output
    gruppiert nach Sektion bei >3 Failures mit mind. einer Section-Count>1.
    Singleton-only-Gruppierung faellt auf Flat zurueck (keine verbose Wrapper).
    """
    from system_audit.report import render_human

    mixed = [
        FailureDetail(location="STATE.md: A", expected="x", actual="y",
                      severity="error", hint=None),
        FailureDetail(location="STATE.md: B", expected="x", actual="y",
                      severity="warning", hint=None),
    ]
    grouped = [
        FailureDetail(location=f"CLAUDE.md:{i}", expected="x", actual=f"p{i}",
                      severity="error", hint=None)
        for i in range(5)
    ] + [
        FailureDetail(location="STATE.md:1", expected="x", actual="z",
                      severity="error", hint=None)
    ]
    singletons = [
        FailureDetail(location=f"pkg/{name}.zip", expected="x", actual="orphan",
                      severity="warning", hint=None)
        for name in ("a", "b", "c", "d")
    ]
    results = [
        CheckResult(name="c1", status="FAIL", n_checked=2, n_passed=0,
                    failures=mixed, duration_ms=1, category="core"),
        CheckResult(name="c2", status="FAIL", n_checked=6, n_passed=0,
                    failures=grouped, duration_ms=1, category="core"),
        CheckResult(name="c3", status="WARN", n_checked=4, n_passed=4,
                    failures=singletons, duration_ms=1, category="core"),
    ]
    text = render_human(results, timestamp_utc="2026-04-23T20:00:00Z")

    # Pro-failure severity-icons (Check-4 WARN-Semantik)
    assert "🔴 STATE.md: A" in text, "error failure must carry 🔴"
    assert "⚠️ STATE.md: B" in text, "warning failure must carry ⚠️"

    # Grouping when section-count > 1 exists (Check-5 Batch-Output)
    assert "[CLAUDE.md] 5 finding(s) — 5🔴" in text
    assert "[STATE.md] 1 finding(s)" in text
    assert "... 3 more in [CLAUDE.md]" in text

    # Fallback to flat when all groups would be singletons
    assert "[pkg/a.zip]" not in text, "singleton-only groups must render flat"
    assert "⚠️ pkg/a.zip" in text


def test_report_json_format_is_valid() -> None:
    import json
    from system_audit.report import render_json
    results = [
        CheckResult(name="a", status="PASS", n_checked=1, n_passed=1,
                    failures=[], duration_ms=10, category="core"),
    ]
    text = render_json(results, timestamp_utc="2026-04-21T14:32:41Z")
    data = json.loads(text)
    assert data["summary"]["passed"] == 1
    assert data["exit_code"] == 0
    assert data["checks"][0]["name"] == "a"


def test_main_rc2_emits_partial_json_and_preserves_diagnosis() -> None:
    """Info-preservation: when a check raises an uncaught exception, main() must
    (a) still render JSON on stdout with partial=True + internal_errors[],
    (b) emit traceback on stderr, (c) return rc=2, (d) NOT write STATE.md
    (corrupted state must not be persisted). Regression-gate for Codex Finding E."""
    import contextlib
    import importlib.util
    import io
    import json as _json
    import types as stdlib_types

    main_spec = importlib.util.spec_from_file_location(
        "_sa_main_under_test", str(REPO_ROOT / "03_Tools" / "system_audit.py"),
    )
    assert main_spec is not None and main_spec.loader is not None
    main_mod = importlib.util.module_from_spec(main_spec)
    main_spec.loader.exec_module(main_mod)

    broken_mod = stdlib_types.ModuleType("_sa_broken_check_under_test")
    def _boom(_root, _ctx):
        raise RuntimeError("synthetic boom for rc=2 test")
    broken_mod.run = _boom  # type: ignore[attr-defined]
    sys.modules["_sa_broken_check_under_test"] = broken_mod

    from system_audit import checks as checks_mod
    original_core = dict(checks_mod.CORE)
    checks_mod.CORE.clear()
    checks_mod.CORE["broken_test"] = "_sa_broken_check_under_test:run"

    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout_buf), contextlib.redirect_stderr(stderr_buf):
            rc = main_mod.main(["--core", "--no-write", "--json"])
        assert rc == 2

        data = _json.loads(stdout_buf.getvalue())
        assert data["partial"] is True
        assert data["exit_code"] == 2
        assert len(data["internal_errors"]) == 1
        ierr = data["internal_errors"][0]
        assert ierr["check"] == "broken_test"
        assert ierr["type"] == "RuntimeError"
        assert "synthetic boom" in ierr["msg"]

        stderr_out = stderr_buf.getvalue()
        assert "synthetic boom" in stderr_out, "traceback with exception msg must reach stderr"
    finally:
        checks_mod.CORE.clear()
        checks_mod.CORE.update(original_core)
        sys.modules.pop("_sa_broken_check_under_test", None)


def test_render_json_partial_flag_emits_internal_errors() -> None:
    """With internal_errors supplied, render_json marks payload partial, overrides
    exit_code to 2, and attaches the error list for automation consumers."""
    import json as _json
    from system_audit.report import render_json
    from system_audit.types import CheckResult
    results = [CheckResult(name="dummy", status="PASS", n_checked=1, n_passed=1)]
    out = render_json(
        results,
        timestamp_utc="2026-04-21T00:00:00Z",
        internal_errors=[("broken_check", "ImportError", "No module named 'nope'")],
    )
    data = _json.loads(out)
    assert data["partial"] is True
    assert data["exit_code"] == 2
    assert data["internal_errors"] == [
        {"check": "broken_check", "type": "ImportError", "msg": "No module named 'nope'"}
    ]
    # Existing results must still be present (info preservation).
    assert len(data["checks"]) == 1


def test_render_json_without_internal_errors_is_non_partial() -> None:
    """Backward-compat: absence of internal_errors must yield partial=False and no
    internal_errors key. Exit-code remains 0/1 per existing FAIL semantics."""
    import json as _json
    from system_audit.report import render_json
    from system_audit.types import CheckResult
    results = [CheckResult(name="dummy", status="PASS", n_checked=1, n_passed=1)]
    out = render_json(results, timestamp_utc="2026-04-21T00:00:00Z")
    data = _json.loads(out)
    assert data["partial"] is False
    assert "internal_errors" not in data
    assert data["exit_code"] == 0


def test_state_writer_first_run_inserts_before_footer() -> None:
    import tempfile
    from system_audit.state_writer import write_last_audit
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "STATE.md"
        p.write_text(
            "# STATE\n\n## Section A\nContent\n\n---\n*🦅 STATE.md v1.0 | Footer*\n",
            encoding="utf-8",
        )
        write_last_audit(p, timestamp_utc="2026-04-21T14:32:41Z",
                         summary="7/7 PASS", run_cmd="python 03_Tools/system_audit.py --core")
        text = p.read_text(encoding="utf-8")
    assert "<!-- system-audit:last-audit:start -->" in text
    assert "<!-- system-audit:last-audit:end -->" in text
    assert "## 🔍 Last Audit" in text
    assert "2026-04-21T14:32:41Z" in text
    assert text.index("<!-- system-audit:last-audit:end -->") < text.index("🦅 STATE.md v1.0")

def test_state_writer_second_run_replaces_block() -> None:
    import tempfile
    from system_audit.state_writer import write_last_audit
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "STATE.md"
        p.write_text(
            "# STATE\n\n---\n*🦅 STATE.md v1.0*\n",
            encoding="utf-8",
        )
        write_last_audit(p, timestamp_utc="2026-04-21T14:32:41Z",
                         summary="7/7 PASS", run_cmd="x")
        write_last_audit(p, timestamp_utc="2026-04-22T09:00:00Z",
                         summary="6/7 PASS (1 FAIL)", run_cmd="x")
        text = p.read_text(encoding="utf-8")
    assert text.count("<!-- system-audit:last-audit:start -->") == 1
    assert "2026-04-22T09:00:00Z" in text
    assert "2026-04-21T14:32:41Z" not in text
    assert "6/7 PASS" in text

def test_orchestrator_dry_run_on_live_repo() -> None:
    """Dev-Smoke: akzeptiert rc in {0, 1} weil Live-Repo noch Drift haben kann
    (pre-Task-17 existence-Cleanup). Hard-Baseline-Gate ist Task 17/15."""
    import json
    import subprocess
    out = subprocess.run(
        [sys.executable, "03_Tools/system_audit.py", "--core", "--no-write", "--json"],
        cwd=str(REPO_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
    )
    assert out.returncode in (0, 1), (
        f"rc={out.returncode} (2=tool-bug)\nstdout={out.stdout[:500]}\nstderr={out.stderr[:500]}"
    )
    data = json.loads(out.stdout)
    assert "summary" in data
    assert "checks" in data
    assert len(data["checks"]) >= 7, f"expected >=7 core checks, got {len(data['checks'])}"


def test_orchestrator_duration_budget_core() -> None:
    """Spec §12 Acceptance: <30s auf --core. Guards against silent rc=2 false-pass:
    if the orchestrator crashes immediately, the duration assertion alone would
    pass misleadingly (CodeRabbit-subagent Finding K)."""
    import subprocess
    import time
    t0 = time.monotonic()
    out = subprocess.run(
        [sys.executable, "03_Tools/system_audit.py", "--core", "--no-write"],
        cwd=str(REPO_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=45,
    )
    elapsed = time.monotonic() - t0
    assert out.returncode in (0, 1), (
        f"rc={out.returncode} (2=tool-bug), stderr={out.stderr[:500]}"
    )
    assert elapsed < 30.0, f"took {elapsed:.1f}s, budget 30s"


def test_orchestrator_minimal_baseline_scope() -> None:
    """--minimal-baseline runs exactly jsonl_schema + pipeline_ssot + log_lag."""
    import json
    import subprocess
    out = subprocess.run(
        [sys.executable, "03_Tools/system_audit.py", "--minimal-baseline", "--no-write", "--json"],
        cwd=str(REPO_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30,
    )
    assert out.returncode in (0, 1), f"rc={out.returncode}\nstderr={out.stderr[:500]}"
    data = json.loads(out.stdout)
    names = {c["name"] for c in data["checks"]}
    assert names == {"jsonl_schema", "pipeline_ssot", "log_lag"}, f"got {names}"


def test_orchestrator_vault_runs_optional_checks() -> None:
    """Post-Task-14: OPTIONAL registry has vault_backlinks + status_matrix; --vault must
    run exactly those two checks. rc in {0, 1} because live vault may have real drift.

    rc-check precedes json.loads so an unexpected rc=2 surfaces the real failure
    instead of a confusing JSONDecodeError on stderr content (CodeRabbit-CLI CR-1).
    """
    import json
    import subprocess
    out = subprocess.run(
        [sys.executable, "03_Tools/system_audit.py", "--vault", "--no-write", "--json"],
        cwd=str(REPO_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
    )
    assert out.returncode in (0, 1), f"rc={out.returncode}, stderr={out.stderr[:500]}"
    data = json.loads(out.stdout)
    names = {c["name"] for c in data["checks"]}
    assert names == {"vault_backlinks", "status_matrix"}, f"got {names}"
    assert len(data["checks"]) == 2


def test_orchestrator_invalid_timeout_rejected() -> None:
    """--timeout-per-check <= 0 must return rc=2."""
    import subprocess
    out = subprocess.run(
        [sys.executable, "03_Tools/system_audit.py",
         "--core", "--no-write", "--timeout-per-check", "0"],
        cwd=str(REPO_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20,
    )
    assert out.returncode == 2, f"rc={out.returncode}, stderr={out.stderr[:200]}"


def test_state_writer_raises_on_orphan_start_marker() -> None:
    import tempfile
    from system_audit.state_writer import write_last_audit
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "STATE.md"
        p.write_text(
            "# STATE\n<!-- system-audit:last-audit:start -->\n(missing end)\n*🦅 Footer*\n",
            encoding="utf-8",
        )
        try:
            write_last_audit(p, timestamp_utc="x", summary="x", run_cmd="x")
        except RuntimeError as e:
            assert "inkonsistent" in str(e).lower() or "marker" in str(e).lower()
        else:
            raise AssertionError("expected RuntimeError on orphan marker")


def test_vault_backlinks_pass_fixture() -> None:
    """PASS: [[Note]] zeigt auf existierende Note."""
    import tempfile
    from system_audit.checks.vault_backlinks import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        vault = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind"
        (vault / "notes").mkdir(parents=True)
        (vault / "notes" / "Alpha.md").write_text("content", encoding="utf-8")
        (vault / "notes" / "Beta.md").write_text("Siehe [[Alpha]] für mehr.", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=True, vault_timeout_s=10)
        result = run(tdp, ctx)
    assert result.status == "PASS", f"failures={result.failures}"

def test_vault_backlinks_fail_on_missing() -> None:
    """FAIL: [[Missing]] hat keinen Target."""
    import tempfile
    from system_audit.checks.vault_backlinks import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        vault = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind"
        (vault / "notes").mkdir(parents=True)
        (vault / "notes" / "A.md").write_text("Link zu [[Nonexistent]].", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=True, vault_timeout_s=10)
        result = run(tdp, ctx)
    assert result.status == "FAIL"
    assert any("Nonexistent" in f.expected or "Nonexistent" in f.actual for f in result.failures)

def test_status_matrix_pass_fixture() -> None:
    """PASS: B1-B5 lückenlos, keine Duplikate."""
    import tempfile
    from system_audit.checks.status_matrix import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        target = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
        target.parent.mkdir(parents=True)
        target.write_text(
            "# Doc\n\n## Status-Matrix\n\n- B1 first\n- B2 second\n- B3 third\n- B4 fourth\n- B5 fifth\n\n## Anderer Abschnitt\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=True)
        result = run(tdp, ctx)
    assert result.status == "PASS", f"failures={result.failures}"

def test_status_matrix_fail_on_gap() -> None:
    """FAIL: B3 fehlt zwischen B2 und B4."""
    import tempfile
    from system_audit.checks.status_matrix import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        target = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
        target.parent.mkdir(parents=True)
        target.write_text(
            "## Status-Matrix\n\n- B1\n- B2\n- B4\n- B5\n\n## Other\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=True)
        result = run(tdp, ctx)
    assert result.status == "FAIL"
    assert any("B3" in f.actual for f in result.failures)

def test_status_matrix_fail_on_duplicate() -> None:
    """FAIL: B2 erscheint 2×."""
    import tempfile
    from system_audit.checks.status_matrix import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        target = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
        target.parent.mkdir(parents=True)
        target.write_text(
            "## Status-Matrix\n\n- B1\n- B2\n- B2\n- B3\n\n## Other\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=True)
        result = run(tdp, ctx)
    assert result.status == "FAIL"
    assert any("B2" in f.actual and "2" in f.actual for f in result.failures)


def test_vault_backlinks_skip_on_missing_vault() -> None:
    """EDGE: Kein Vault-Verzeichnis → SKIP ohne Failures."""
    import tempfile
    from system_audit.checks.vault_backlinks import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        ctx = AuditContext(repo_root=tdp, include_optional=True, vault_timeout_s=10)
        result = run(tdp, ctx)
    assert result.status == "SKIP"


def test_status_matrix_header_anchored_not_prose_match() -> None:
    """Code-Review Blocker #1: Section-isolation muss auf Header anker, nicht Prosa-Match.
    Pathologie: 'Status-Matrix' taucht in Prosa VOR dem echten Header auf — der alte
    Plain-Match würde section_start auf die Prosa setzen, der next-heading-Cut kappt
    VOR dem echten Header, und die Status-Matrix wird nie gescannt → silent PASS.
    """
    import tempfile
    from system_audit.checks.status_matrix import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        target = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
        target.parent.mkdir(parents=True)
        target.write_text(
            "# Titel\n\nDiese Seite enthält eine **Status-Matrix** mit B-Nummern.\n\n"
            "## Einleitung\n\nVorbemerkung.\n\n"
            "## Status-Matrix\n\n- B1\n- B3\n\n## Andere Sektion\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=True)
        result = run(tdp, ctx)
    assert result.status == "FAIL", f"prose-match-false-negative: status={result.status}"
    assert any("B2" in f.actual for f in result.failures), (
        f"echte Status-Matrix muss gescannt + Gap B2 gefunden werden; failures={result.failures}"
    )


def test_status_matrix_subsections_are_scanned() -> None:
    """Regression: Subsections unterhalb des Status-Matrix-Headers (tiefer level)
    müssen IN der Section bleiben — sonst kappt '### Legende' direkt hinter
    dem '## Status-Matrix'-Header den eigentlichen B-Label-Scan weg.
    """
    import tempfile
    from system_audit.checks.status_matrix import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        target = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
        target.parent.mkdir(parents=True)
        target.write_text(
            "## Status-Matrix\n\n"
            "### Legende\n\nDoc.\n\n"
            "### Matrix\n\n- B1\n- B2\n- B3\n\n"
            "## Nachfolgender Abschnitt\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=True)
        result = run(tdp, ctx)
    assert result.status == "PASS", f"failures={result.failures}"
    assert result.n_checked == 3, f"alle 3 B-Labels aus Subsection erwartet, got {result.n_checked}"


def test_status_matrix_n_passed_arithmetic_with_gaps() -> None:
    """Code-Review Blocker #2: n_passed = len(numbers) - len(failures) ist falsch,
    weil gap-failures B-Nummern referenzieren, die gar nicht in 'numbers' sind.
    Beispiel B1 B3 B5 → numbers=[1,3,5] (3 unique), 2 gaps (B2,B4).
    Alt: n_passed = 3 - 2 = 1 (falsch, alle 3 sind unique/well-formed).
    Richtig: n_passed = |numbers| - |duplicates| = 3 - 0 = 3.
    """
    import tempfile
    from system_audit.checks.status_matrix import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        target = tdp / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
        target.parent.mkdir(parents=True)
        target.write_text(
            "## Status-Matrix\n\n- B1\n- B3\n- B5\n\n## Other\n",
            encoding="utf-8",
        )
        ctx = AuditContext(repo_root=tdp, include_optional=True)
        result = run(tdp, ctx)
    assert result.status == "FAIL"
    assert result.n_checked == 3, f"expected 3 unique B-numbers, got {result.n_checked}"
    assert result.n_passed == 3, (
        f"alle 3 sind unique (keine dups) → n_passed muss 3 sein, got {result.n_passed}"
    )


def test_jsonl_schema_malformed_json_hint() -> None:
    """Code-Review Important #3: nach model_validate_json-Refactor muss malformed JSON
    den alten 'Record manuell pruefen' hint kriegen, nicht den
    'Migration-Helper'-hint (der für echte Schema-Drift gedacht ist).
    Pydantic v2 type='json_invalid' markiert JSON-Parse-Fehler.
    """
    import tempfile
    from system_audit.checks.jsonl_schema import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        bad = tdp / "bad.jsonl"
        bad.write_text("{not valid json\n", encoding="utf-8")
        empty = tdp / "empty.jsonl"
        empty.write_text("", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx, stores_override={
            "score_history": bad,
            "flag_events": empty,
            "portfolio_returns": empty,
            "benchmark_series": empty,
        })
    assert result.status == "FAIL"
    json_failures = [f for f in result.failures if f.severity == "error"]
    assert len(json_failures) >= 1
    assert any(
        f.hint is not None and "manuell" in f.hint.lower()
        for f in json_failures
    ), f"malformed JSON erwartet 'manuell pruefen/entfernen' hint; got hints={[f.hint for f in json_failures]}"


if __name__ == "__main__":
    test_check_result_pass_semantics()
    test_check_result_fail_error()
    test_check_result_warn_is_not_fail()
    test_audit_context_repo_root()
    test_failure_detail_is_frozen()
    test_check_result_skip_status()
    test_check_result_failures_mutable()
    print("[OK] types smoke tests passed")
    test_jsonl_schema_pass_on_good_fixture()
    test_jsonl_schema_fail_on_bad_fixture()
    test_jsonl_schema_skip_on_missing_file()
    test_jsonl_schema_malformed_json_hint()
    print("[OK] jsonl_schema smoke tests passed")
    test_store_freshness_warn_on_stale()
    test_store_freshness_pass_on_fresh()
    test_store_freshness_skip_on_missing()
    print("[OK] store_freshness smoke tests passed")
    test_markdown_header_pass_on_aligned()
    test_markdown_header_fail_on_stale()
    test_markdown_header_warn_on_lag()
    test_markdown_header_excludes_future_dates()
    print("[OK] markdown_header smoke tests passed")
    test_cross_source_pass_on_aligned()
    test_cross_source_fail_on_divergence()
    test_flag_parser_all_six_variants()
    test_flag_mismatch_matrix()
    print("[OK] cross_source smoke tests passed")
    test_existence_pass_on_existing_paths()
    test_existence_ignores_paths_with_spaces()
    print("[OK] existence smoke tests passed")
    test_skill_version_pass_fixture()
    test_skill_version_warn_on_unpacked_newer_fixture()
    test_skill_version_warn_on_orphan_zip_fixture()
    test_skill_version_pass_on_bare_zip_fixture()
    test_skill_version_warn_on_orphan_bare_zip_fixture()
    test_skill_version_pass_on_extern_bare_zip_fixture()
    test_skill_version_skip_on_missing_frontmatter_fixture()
    print("[OK] skill_version smoke tests passed")
    test_pipeline_ssot_parser_three_variants()
    test_pipeline_ssot_pass_on_live_state()
    test_pipeline_ssot_fail_on_broken_ref()
    print("[OK] pipeline_ssot smoke tests passed")
    test_log_lag_live_repo_pass()
    test_log_lag_fail_on_stale()
    print("[OK] log_lag smoke tests passed")
    test_report_human_format_contains_summary()
    test_report_json_format_is_valid()
    test_render_json_partial_flag_emits_internal_errors()
    test_render_json_without_internal_errors_is_non_partial()
    print("[OK] report smoke tests passed")
    test_state_writer_first_run_inserts_before_footer()
    test_state_writer_second_run_replaces_block()
    test_state_writer_raises_on_orphan_start_marker()
    print("[OK] state_writer smoke tests passed")
    test_orchestrator_dry_run_on_live_repo()
    test_orchestrator_duration_budget_core()
    test_orchestrator_minimal_baseline_scope()
    test_orchestrator_vault_runs_optional_checks()
    test_orchestrator_invalid_timeout_rejected()
    test_main_rc2_emits_partial_json_and_preserves_diagnosis()
    print("[OK] orchestrator smoke tests passed")
    test_vault_backlinks_pass_fixture()
    test_vault_backlinks_fail_on_missing()
    test_vault_backlinks_skip_on_missing_vault()
    print("[OK] vault_backlinks smoke tests passed")
    test_status_matrix_pass_fixture()
    test_status_matrix_fail_on_gap()
    test_status_matrix_fail_on_duplicate()
    test_status_matrix_header_anchored_not_prose_match()
    test_status_matrix_subsections_are_scanned()
    test_status_matrix_n_passed_arithmetic_with_gaps()
    print("[OK] status_matrix smoke tests passed")
