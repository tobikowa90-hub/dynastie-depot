"""Tests for earnings_calendar.py v2.0 — Override-Aggregation + JSON-Output.

Run: python -m pytest 03_Tools/_test_earnings_calendar.py -v
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parent))
from earnings_calendar import (
    EarningsResult,
    evaluate_smoke,
    load_overrides,
    next_earnings,
    portfolio_trigger_cell,
    render_report,
)

# ------------------------------------------------------------
# portfolio_trigger_cell: 6-col (legacy) + 7-col (3-Tier) coverage
# Regression-Guard: 3-Tier-Tabelle mit führender Tier-Spalte brach den
# alten ticker-in-Spalte-1-Anchor (Umstrukturierung 2027, 05.06.).
# ------------------------------------------------------------


def test_trigger_cell_legacy_six_column():
    txt = "| AVGO | x | y | z | w | 30.04. Forward-Vollanalyse DONE |\n"
    assert portfolio_trigger_cell("AVGO", txt) == "30.04. Forward-Vollanalyse DONE"


def test_trigger_cell_three_tier_seven_column():
    txt = "| **T2** | ASML | **68** | 🟡 3 | **32€** | ✅ | **Q2 2026 15.07.** (bmo) |\n"
    assert "15.07." in portfolio_trigger_cell("ASML", txt)


def test_trigger_cell_substring_ticker_does_not_crossmatch():
    # 'V' darf nicht in 'AVGO'/'VEEV' hineinmatchen; jede Row liefert ihre eigene Zelle.
    txt = (
        "| **T1** | AVGO | 56 | 🟠 2 | 0€ | 🔴 | Q3 03.09. |\n"
        "| **T2** | V | 64 | 🟠 2 | 16€ | ✅ | Q3 28.07. |\n"
    )
    assert "28.07." in portfolio_trigger_cell("V", txt)
    assert "03.09." in portfolio_trigger_cell("AVGO", txt)


def test_trigger_cell_empty_last_cell_returns_empty():
    # Leere letzte Zelle -> "" (nicht no-match-Krücke); regression-guard für ([^|\n]*).
    txt = "| **T2** | ASML | **68** | 🟡 3 | **32€** | ✅ |  |\n"
    assert portfolio_trigger_cell("ASML", txt) == ""


# ------------------------------------------------------------
# Test 4d: Broken YAML → load_overrides fail-soft
# ------------------------------------------------------------


def test_load_overrides_broken_yaml_returns_empty(tmp_path):
    """AC4d: Syntax-Error in YAML → returns {}, no exception escapes."""
    bad = tmp_path / "broken.yaml"
    bad.write_text("schedules:\n  SU:\n    events: [unclosed\n", encoding="utf-8")
    result = load_overrides(today=date(2026, 5, 6), path=bad)
    assert result == {}


def test_load_overrides_missing_file_returns_empty(tmp_path):
    """Fail-soft: nicht-existente Datei → {}"""
    missing = tmp_path / "does_not_exist.yaml"
    result = load_overrides(today=date(2026, 5, 6), path=missing)
    assert result == {}


def test_load_overrides_filters_past_dates(tmp_path):
    """Future-only filter: past events werden eliminiert."""
    yml = tmp_path / "ovr.yaml"
    yml.write_text(
        'schema_version: "1.0"\n'
        "schedules:\n"
        "  SU:\n"
        "    ir_calendar_url: 'https://x'\n"
        "    events:\n"
        "      - {date: 2026-01-15, type: trading_update_q1}\n"
        "      - {date: 2026-07-30, type: half_year_h1}\n",
        encoding="utf-8",
    )
    result = load_overrides(today=date(2026, 5, 6), path=yml)
    assert "SU" in result
    assert len(result["SU"]) == 1
    assert result["SU"][0].date == date(2026, 7, 30)
    assert result["SU"][0].type == "half_year_h1"


# ------------------------------------------------------------
# Helpers: yfinance-Mock-Factory
# ------------------------------------------------------------


class _FakeIndex:
    """Minimal pandas-Index-Stand-in: list of date-able objects."""

    def __init__(self, dates: list[date]):
        self._dates = [_FakeTimestamp(d) for d in dates]

    def __iter__(self):
        return iter(self._dates)


class _FakeTimestamp:
    def __init__(self, d: date):
        self._d = d

    def date(self) -> date:
        return self._d


class _FakeDataFrame:
    def __init__(self, dates: list[date]):
        self._dates = dates
        self.index = _FakeIndex(dates)
        self.empty = len(dates) == 0


def make_yf_mock(future_dates: list[date], calendar_date: date | None = None):
    """Returns a callable that mimics yf.Ticker(symbol) with controlled data."""

    def _factory(symbol: str):
        m = MagicMock()
        m.earnings_dates = _FakeDataFrame(future_dates)
        if calendar_date is not None:
            m.calendar = {"Earnings Date": [calendar_date]}
        else:
            m.calendar = None
        return m

    return _factory


# ------------------------------------------------------------
# Test 4a: Aggregation Union (yfinance ∪ override, earliest-wins)
# ------------------------------------------------------------


def test_aggregation_override_earlier_than_yfinance(tmp_path):
    """AC4a: yfinance=[2026-07-30], override=[2026-04-30, 2026-07-30, 2026-10-30],
    today=2026-04-01 → result 2026-04-30, source='override'."""
    yml = tmp_path / "ovr.yaml"
    yml.write_text(
        "schedules:\n"
        "  SU:\n"
        "    events:\n"
        "      - {date: 2026-04-30, type: trading_update_q1}\n"
        "      - {date: 2026-07-30, type: half_year_h1}\n"
        "      - {date: 2026-10-30, type: trading_update_q3}\n",
        encoding="utf-8",
    )
    yf_mock = make_yf_mock(future_dates=[date(2026, 7, 30)])
    result = next_earnings(
        "SU",
        today=date(2026, 4, 1),
        data_source=yf_mock,
        overrides_path=yml,
    )
    assert result.earnings_date == date(2026, 4, 30)
    assert result.source == "override"
    assert result.event_type == "trading_update_q1"


def test_aggregation_same_date_both_sources(tmp_path):
    """Same date in beiden Quellen → source='earnings_dates+override' (alpha-sorted)."""
    yml = tmp_path / "ovr.yaml"
    yml.write_text(
        "schedules:\n  ASML:\n    events:\n      - {date: 2026-07-15, type: half_year_h1}\n",
        encoding="utf-8",
    )
    yf_mock = make_yf_mock(future_dates=[date(2026, 7, 15)])
    result = next_earnings(
        "ASML",
        today=date(2026, 4, 1),
        data_source=yf_mock,
        overrides_path=yml,
    )
    assert result.earnings_date == date(2026, 7, 15)
    assert result.source == "earnings_dates+override"
    assert result.event_type == "half_year_h1"


# ------------------------------------------------------------
# Test 4b: Override-only (yfinance leer)
# ------------------------------------------------------------


def test_aggregation_override_only(tmp_path):
    """AC4b: yfinance=[], override=[2026-10-30], today=2026-09-01 → 2026-10-30, source='override'."""
    yml = tmp_path / "ovr.yaml"
    yml.write_text(
        "schedules:\n  SU:\n    events:\n      - {date: 2026-10-30, type: trading_update_q3}\n",
        encoding="utf-8",
    )
    yf_mock = make_yf_mock(future_dates=[])
    result = next_earnings(
        "SU",
        today=date(2026, 9, 1),
        data_source=yf_mock,
        overrides_path=yml,
    )
    assert result.earnings_date == date(2026, 10, 30)
    assert result.source == "override"
    assert result.event_type == "trading_update_q3"


# ------------------------------------------------------------
# Test 4c: Year-Boundary (deterministische min-Auswahl)
# ------------------------------------------------------------


def test_aggregation_year_boundary(tmp_path):
    """AC4c: override=[2026-12-31, 2027-01-15], today=2026-12-15 → 2026-12-31."""
    yml = tmp_path / "ovr.yaml"
    yml.write_text(
        "schedules:\n"
        "  SU:\n"
        "    events:\n"
        "      - {date: 2026-12-31, type: annual_results}\n"
        "      - {date: 2027-01-15, type: trading_update_q1}\n",
        encoding="utf-8",
    )
    yf_mock = make_yf_mock(future_dates=[])
    result = next_earnings(
        "SU",
        today=date(2026, 12, 15),
        data_source=yf_mock,
        overrides_path=yml,
    )
    assert result.earnings_date == date(2026, 12, 31)
    assert result.source == "override"


# ------------------------------------------------------------
# AC1: Coverage-Test (deterministisch via injizierter today + Override-Fixture)
# ------------------------------------------------------------


def test_ac1_coverage_su_q1_via_override(tmp_path):
    """AC1: today=2026-04-25, SU Override [Q1 2026-04-30, H1 2026-07-30],
    yfinance liefert nur 2026-07-30 → result 2026-04-30 / trading_update_q1 / override."""
    yml = tmp_path / "ovr.yaml"
    yml.write_text(
        "schedules:\n"
        "  SU:\n"
        "    events:\n"
        "      - {date: 2026-04-30, type: trading_update_q1}\n"
        "      - {date: 2026-07-30, type: half_year_h1}\n",
        encoding="utf-8",
    )
    yf_mock = make_yf_mock(future_dates=[date(2026, 7, 30)])
    result = next_earnings(
        "SU",
        today=date(2026, 4, 25),
        data_source=yf_mock,
        overrides_path=yml,
    )
    assert result.earnings_date == date(2026, 4, 30)
    assert result.event_type == "trading_update_q1"
    assert result.source == "override"


# ------------------------------------------------------------
# HIGH-1 Regression: Stale-Calendar-Past-Date darf NIE
# Override-Future-Date in min-Aggregation schlagen.
# (Codex-R5-HIGH-1: ohne diesen Test koennte der Bug silent
# zurueckkehren bei zukuenftigen Refactorings.)
# ------------------------------------------------------------


def test_high1_stale_calendar_does_not_beat_future_override(tmp_path):
    """Regression: yfinance future-leer + calendar zeigt PAST date +
    override hat valid future date -> result MUSS override-Date sein,
    NICHT das stale calendar-past-date.

    Ohne den Fix wuerde min(stale_past, override_future) = stale_past
    zurueckgeben und Tag-+1-Vorbereitungs-Window verfehlen.
    """
    yml = tmp_path / "ovr.yaml"
    yml.write_text(
        "schedules:\n  SU:\n    events:\n      - {date: 2026-07-30, type: half_year_h1}\n",
        encoding="utf-8",
    )
    # yfinance future-leer (RMS.PA/SU.PA-Quirk simulated) + calendar zeigt past
    yf_mock = make_yf_mock(
        future_dates=[],
        calendar_date=date(2026, 2, 15),  # PAST relativ zu today=2026-05-06
    )
    result = next_earnings(
        "SU",
        today=date(2026, 5, 6),
        data_source=yf_mock,
        overrides_path=yml,
    )
    # Override-Future-Date muss gewinnen, NIE stale-past
    assert result.earnings_date == date(2026, 7, 30), (
        f"Expected override 2026-07-30, got {result.earnings_date} (HIGH-1 regression!)"
    )
    assert result.source == "override"
    assert result.event_type == "half_year_h1"


def test_high1_stale_calendar_only_when_no_other_candidates(tmp_path):
    """Komplementär zu HIGH-1: wenn KEINE future candidates da sind
    (yfinance leer + override leer), DARF stale calendar als Degraded-
    Fallback ausgegeben werden — mit source='calendar_stale' und Note.
    """
    yml = tmp_path / "ovr.yaml"
    yml.write_text("schedules: {}\n", encoding="utf-8")
    yf_mock = make_yf_mock(
        future_dates=[],
        calendar_date=date(2026, 2, 15),  # PAST
    )
    result = next_earnings(
        "RMS",
        today=date(2026, 5, 6),
        data_source=yf_mock,
        overrides_path=yml,
    )
    assert result.earnings_date == date(2026, 2, 15)
    assert result.source == "calendar_stale"
    assert "past date 2026-02-15" in (result.note or "")


# ------------------------------------------------------------
# AC2: JSON-Schema-Test
# ------------------------------------------------------------


def test_ac2_json_schema_minimal(tmp_path, monkeypatch):
    """AC2: --json erzeugt valides JSON mit allen Pflichtfeldern.

    Run subprocess wäre teuer; stattdessen direkt build_json_payload() prüfen.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from earnings_calendar import build_json_payload

    fake_results = [
        EarningsResult("AVGO", "AVGO", date(2026, 6, 3), "earnings_dates", event_type=None),
        EarningsResult("BRK.B", "BRK-B", date(2026, 8, 1), "earnings_dates", event_type=None),
    ]
    fake_drifts = {"AVGO"}
    portfolio_text = "| AVGO | x | y | z | w | 30.04. Forward-Vollanalyse DONE |\n"
    payload = build_json_payload(
        results=fake_results,
        drifts=fake_drifts,
        today=date(2026, 5, 6),
        alert_window=10,
        portfolio_text=portfolio_text,
        exit_code=2,
    )

    # Top-level Pflichtfelder
    for k in (
        "schema_version",
        "tool",
        "tool_version",
        "timestamp",
        "summary",
        "exit_code",
        "items",
    ):
        assert k in payload, f"missing top-level key: {k}"
    assert payload["tool"] == "earnings_calendar"
    assert payload["tool_version"].startswith("2.")
    assert payload["exit_code"] == 2

    # Summary-Pflichtfelder
    for k in ("tickers_checked", "drifts"):
        assert k in payload["summary"], f"missing summary key: {k}"
    assert payload["summary"]["tickers_checked"] == 2
    assert payload["summary"]["drifts"] == 1

    # Per-item Pflichtfelder
    avgo = next(it for it in payload["items"] if it["ticker"] == "AVGO")
    for k in ("ticker", "yahoo_symbol", "earnings_date", "source", "drift_status"):
        assert k in avgo, f"missing item key: {k}"
    assert avgo["drift_status"] == "DRIFT"
    assert avgo["earnings_date"] == "2026-06-03"

    # JSON-Roundtrip muss funktionieren
    import json

    blob = json.dumps(payload)
    parsed = json.loads(blob)
    assert parsed["tool"] == "earnings_calendar"


# ------------------------------------------------------------
# Codex-R10-MED-2 Follow-up: Smoke-Anchor-Pfade (PIPELINE #44 Gap a)
# ------------------------------------------------------------


def test_smoke_pass_when_anchor_matches():
    """OK-Pfad: smoke_result.earnings_date == SMOKE_DATE → PASS, failed=False."""
    smoke = EarningsResult(
        "BRK.B",
        "BRK-B",
        date(2026, 8, 1),
        "earnings_dates",
        event_type=None,
    )
    msg, failed = evaluate_smoke(
        today=date(2026, 5, 8),
        smoke_result=smoke,
        smoke_ticker="BRK.B",
        smoke_date=date(2026, 8, 1),
    )
    assert "PASS" in msg
    assert failed is False


def test_smoke_fail_when_anchor_mismatches():
    """FAIL-Pfad: smoke_result.earnings_date != SMOKE_DATE → FAIL, failed=True."""
    smoke = EarningsResult(
        "BRK.B",
        "BRK-B",
        date(2026, 8, 5),
        "earnings_dates",
        event_type=None,
    )
    msg, failed = evaluate_smoke(
        today=date(2026, 5, 8),
        smoke_result=smoke,
        smoke_ticker="BRK.B",
        smoke_date=date(2026, 8, 1),
    )
    assert "FAIL" in msg
    assert "2026-08-05" in msg
    assert "expected 2026-08-01" in msg
    assert failed is True


def test_smoke_skip_when_anchor_in_past():
    """Skip-if-past: today > smoke_date → SKIPPED, failed=False (kein exit 1)."""
    smoke = EarningsResult(
        "BRK.B",
        "BRK-B",
        date(2026, 11, 5),
        "earnings_dates",
        event_type=None,
    )
    msg, failed = evaluate_smoke(
        today=date(2026, 8, 15),  # today > smoke_date
        smoke_result=smoke,
        smoke_ticker="BRK.B",
        smoke_date=date(2026, 8, 1),
    )
    assert "SKIPPED" in msg
    assert "2026-11-05" in msg  # actual yfinance-date im SKIP-Hinweis
    assert failed is False  # Skip darf NIE exit 1 triggern


def test_smoke_fail_when_no_result():
    """Edge-Case: smoke_result=None → FAIL with 'None' actual, failed=True."""
    msg, failed = evaluate_smoke(
        today=date(2026, 5, 8),
        smoke_result=None,
        smoke_ticker="BRK.B",
        smoke_date=date(2026, 8, 1),
    )
    assert "FAIL" in msg
    assert "None" in msg
    assert failed is True


# ------------------------------------------------------------
# PIPELINE #44 Gap b: Alert-Window-Boundary (days==alert_window vs +1)
# ------------------------------------------------------------


def test_alert_window_boundary_drift_at_exact_window():
    """days==alert_window UND nicht im Trigger → DRIFT (inclusive boundary)."""
    today = date(2026, 5, 8)
    earnings_in_10 = EarningsResult(
        "VEEV",
        "VEEV",
        date(2026, 5, 18),  # exactly +10 days
        "earnings_dates",
        event_type=None,
    )
    portfolio = "| VEEV | 74 | 3 | 38€ | ✅ | Q1 ~Ende Mai |\n"
    report, drifts = render_report(
        [earnings_in_10], today, alert_window=10, portfolio_text=portfolio
    )
    assert any(r.ticker == "VEEV" for r in drifts), (
        f"days==10 mit alert_window=10 sollte DRIFT triggern, drifts={drifts}"
    )
    assert "DRIFT" in report


def test_alert_window_boundary_soon_one_day_past_window():
    """days==alert_window+1 → SOON, NICHT DRIFT."""
    today = date(2026, 5, 8)
    earnings_in_11 = EarningsResult(
        "VEEV",
        "VEEV",
        date(2026, 5, 19),  # +11 days
        "earnings_dates",
        event_type=None,
    )
    portfolio = "| VEEV | 74 | 3 | 38€ | ✅ | Q1 ~Ende Mai |\n"
    report, drifts = render_report(
        [earnings_in_11], today, alert_window=10, portfolio_text=portfolio
    )
    assert not drifts, f"days==11 mit alert_window=10 darf NICHT drift sein, drifts={drifts}"
    assert "🟡 soon" in report


def test_alert_window_boundary_in_trigger_suppresses_drift():
    """days==alert_window aber Datum im PORTFOLIO-Trigger → 🟢 in trigger, kein DRIFT."""
    today = date(2026, 5, 8)
    earnings_in_10 = EarningsResult(
        "VEEV",
        "VEEV",
        date(2026, 5, 18),
        "earnings_dates",
        event_type=None,
    )
    # PORTFOLIO-Trigger erwähnt 18.05. explizit → in_trigger=True
    portfolio = "| VEEV | 74 | 3 | 38€ | ✅ | 18.05.2026 Q1 FY27 Earnings |\n"
    report, drifts = render_report(
        [earnings_in_10], today, alert_window=10, portfolio_text=portfolio
    )
    assert not drifts, f"in_trigger=True muss DRIFT suppressen, drifts={drifts}"
    assert "🟢 in trigger" in report


# ------------------------------------------------------------
# PIPELINE #44 Gap c: End-to-End CLI-JSON-Smoke (subprocess + JSON-Roundtrip)
# ------------------------------------------------------------


def test_e2e_cli_json_subprocess_help_exits_clean():
    """E2E: subprocess --help exit 0, kein crash, Help-Text enthält bekannte Flags.

    Schneller proxy für CLI-Wiring (argparse + help-print) ohne yfinance-Network-Call.
    """
    import subprocess

    tool = Path(__file__).resolve().parent / "earnings_calendar.py"
    result = subprocess.run(
        [sys.executable, str(tool), "--help"],
        capture_output=True,
        text=True,
        timeout=15,
        check=False,
    )
    assert result.returncode == 0, f"--help exit_code={result.returncode}, stderr={result.stderr}"
    for flag in ("--check", "--smoke-test", "--alert-window", "--json"):
        assert flag in result.stdout, f"flag {flag!r} fehlt im --help-Output"


def test_e2e_cli_json_subprocess_argparse_rejects_unknown_flag():
    """E2E: subprocess mit unbekanntem Flag → exit 2 (argparse default), error in stderr."""
    import subprocess

    tool = Path(__file__).resolve().parent / "earnings_calendar.py"
    result = subprocess.run(
        [sys.executable, str(tool), "--no-such-flag"],
        capture_output=True,
        text=True,
        timeout=15,
        check=False,
    )
    # argparse default: unknown arg → exit 2 + error stderr
    assert result.returncode != 0, "Unknown flag muss non-zero exit haben"
    assert "no-such-flag" in result.stderr or "no-such-flag" in result.stdout
