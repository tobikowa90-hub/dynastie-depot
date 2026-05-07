"""Smoke-Test für flag_event_study.py — verifiziert Pipeline #46 + #47-Cluster-C-Critical-#4.

TEST 1 (Pipeline #46): max_drawdown_pct nutzt running-peak-scan (peak-to-trough),
        nicht (min-trigger)/trigger. Recovery-Spike-Reihe diskriminiert beide Algos.
TEST 2 (Pipeline #47-C-#4): closest_close_on_or_after-Forward-Fallback durch `today`
        gekappt — Look-Ahead-Bias-Prevention (§29.5 Sin #2).

Standalone: python _smoke_test_event_study.py
Exit 0 bei PASS, exit 1 bei FAIL.
"""

from __future__ import annotations

import contextlib
import math
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import flag_event_study as fes
from schemas import FlagEvent, FlagMetrik, Kurs


def _make_event(ticker: str, event_datum: date) -> FlagEvent:
    return FlagEvent(
        schema_version="1.0",
        flag_id=f"{ticker}_capex_ocf_{event_datum.isoformat()}",
        source="forward",
        ticker=ticker,
        flag_typ="capex_ocf",
        event_typ="trigger",
        event_datum=event_datum,
        metrik=FlagMetrik(name="capex_ocf", wert=65.0, schwelle=60.0, definition="smoke"),
        kurs_bei_event=Kurs(wert=100.0, waehrung="USD", referenz="EOD", quelle="smoke"),
        notizen="smoke-test",
    )


def _patch_fetch(price_table: dict[str, dict[date, float]]):
    """Monkey-patch fes.fetch_history_window, lookup per ticker; ignoriert start/end.

    CR 2026-05-07: KeyError-fail-fast statt None-Default — bei Typo / fehlendem
    Ticker (z.B. BENCHMARK_TICKER-Rename) sofort diagnose-bare Fehlermeldung
    statt opaker AttributeError downstream.
    """
    # Note (CR 2026-05-07): Monkey-patching via attribute reassignment
    # (`fes.fetch_history_window = ...` unten) ist hier korrekt, weil
    # `fetch_history_window` IM SELBEN Modul wie `compute_event_result`
    # definiert ist (kein `from <other> import` Late-Bind-Risk). Mock.patch
    # wäre alternativ idiomatischer, aber funktional äquivalent.
    def _fake(ticker, _start, _end):
        if ticker not in price_table:
            raise KeyError(
                f"_patch_fetch: ticker {ticker!r} not in fixture — "
                f"add to price_table (known: {sorted(price_table)})"
            )
        return price_table[ticker]
    return _fake


def test_max_drawdown_running_peak_scan() -> tuple[bool, str]:
    """trigger=100, dann 90, peak-Spike 110, dann 95. Echter Max-DD = (95-110)/110 = -13.636%."""
    event = _make_event("TEST", date(2026, 1, 1))
    prices = {
        date(2026, 1, 1): 100.0,
        date(2026, 1, 2): 90.0,
        date(2026, 1, 3): 110.0,
        date(2026, 1, 4): 95.0,
    }
    bench = {d: 1000.0 for d in prices}  # Benchmark flat — nicht Test-relevant
    today = date(2026, 1, 4)

    table = {"TEST": prices, fes.BENCHMARK_TICKER: bench}
    orig = fes.fetch_history_window
    fes.fetch_history_window = _patch_fetch(table)
    try:
        er = fes.compute_event_result(event, today)
    finally:
        fes.fetch_history_window = orig

    if er.max_drawdown_pct is None:
        return False, "max_drawdown_pct ist None (Fenster sollte 4 Items haben)"

    expected = (95.0 - 110.0) / 110.0 * 100.0  # -13.6363...%
    if not math.isclose(er.max_drawdown_pct, expected, rel_tol=1e-6, abs_tol=1e-6):
        return False, f"max_drawdown_pct={er.max_drawdown_pct:.4f}%, expected≈{expected:.4f}%"

    if er.max_drawdown_window_end != date(2026, 1, 4):
        return False, f"trough_date={er.max_drawdown_window_end}, expected 2026-01-04"

    # Diskriminations-Sanity: der ALTE Algo hätte (90-100)/100 = -10% geliefert.
    if math.isclose(er.max_drawdown_pct, -10.0, abs_tol=0.1):
        return False, "max_drawdown_pct sieht aus wie alter (min-trigger)/trigger Algo"

    return True, f"max_dd={er.max_drawdown_pct:.4f}% trough={er.max_drawdown_window_end}"


def test_forward_fallback_today_cap() -> tuple[bool, str]:
    """target_date=2025-10-31, today=2025-11-01: Forward-Fallback darf NICHT auf 2025-11-05 (post-today) springen.

    Vor fix: closest_close_on_or_after liefert (2025-11-05, 105.0) → hr.status='observed' mit Look-Ahead.
    Nach fix: max_fwd=1, max_days=min(7,1)=1 → nur 10-31 + 11-01 geprüft, beide miss → hr.status='n.a.'.
    """
    event = _make_event("TEST", date(2025, 10, 1))
    prices = {
        date(2025, 10, 1): 100.0,   # Trigger-Day-Preis
        date(2025, 11, 5): 105.0,   # Look-Ahead-Preis (post-today)
    }
    # CR 2026-05-07: bench flat — würde sonst Look-Ahead-Daten enthalten
    # (dict(prices) inkludierte 2025-11-05). Test asserted nur ticker-side,
    # aber sauber ist sauber: bench-Look-Ahead nicht Teil dieses Tests.
    # Sparsity-Sicherheit: closest_close_on_or_before/after returnen None bei
    # missing dates (KEIN KeyError) → b_hit=None → benchmark-fields bleiben
    # None. Verified gegen flag_event_study.closest_close_on_or_after (Z.138).
    bench = {date(2025, 10, 1): 1000.0}
    today = date(2025, 11, 1)

    table = {"TEST": prices, fes.BENCHMARK_TICKER: bench}
    orig = fes.fetch_history_window
    fes.fetch_history_window = _patch_fetch(table)
    try:
        er = fes.compute_event_result(event, today)
    finally:
        fes.fetch_history_window = orig

    # CR 2026-05-07: defensive .get() statt direct-index — bei Schema-Drift
    # (z.B. HORIZONS-Erweiterung) klare Fehlermeldung statt opaker KeyError.
    h30 = er.horizons.get(30)
    if h30 is None:
        return False, f"+30d horizon key missing (keys={list(er.horizons)})"
    if h30.status != "n.a.":
        return False, (
            f"+30d status={h30.status} (kurs_target_date={h30.kurs_target_date}, "
            f"raw_return_pct={h30.raw_return_pct}); expected 'n.a.' (Look-Ahead-gekappt)"
        )

    # +90d und höher müssen 'pending' sein (target>today)
    h90 = er.horizons.get(90)
    if h90 is None:
        return False, f"+90d horizon key missing (keys={list(er.horizons)})"
    if h90.status != "pending":
        return False, f"+90d status={h90.status}, expected 'pending'"

    return True, f"+30d=n.a. (gekappt), +90d=pending"


def main() -> int:
    # CR 2026-05-07: UTF-8-stdout setup inline — vermeidet Abhängigkeit auf
    # private API fes._ensure_utf8_stdout (würde bei Rename/Inline silent break).
    if hasattr(sys.stdout, "reconfigure"):
        with contextlib.suppress(Exception):
            sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    tests = [
        ("Pipeline #46 max_drawdown running-peak-scan", test_max_drawdown_running_peak_scan),
        ("Pipeline #47-C-#4 forward-fallback today-cap", test_forward_fallback_today_cap),
    ]
    fail = 0
    for name, fn in tests:
        try:
            ok, detail = fn()
        except Exception as exc:  # noqa: BLE001
            ok, detail = False, f"EXCEPTION {type(exc).__name__}: {exc}"
        marker = "PASS" if ok else "FAIL"
        print(f"[{marker}] {name} — {detail}")
        if not ok:
            fail += 1
    print(f"\n{len(tests) - fail}/{len(tests)} passed.")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
