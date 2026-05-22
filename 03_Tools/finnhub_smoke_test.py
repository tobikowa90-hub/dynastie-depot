#!/usr/bin/env python3
"""finnhub_smoke_test.py — Reproduzierbare 9-Test-Matrix gegen FinnHub Free-Tier.

Spec: docs/superpowers/specs/2026-05-22-finnhub-integration-design.md v0.3 §3.

Usage:
    python 03_Tools/finnhub_smoke_test.py [--verbose] [--json]

Exit-Code 0 wenn 7/9 PASS (Tests 5+6 sind EXPECTED-FAIL).
Schreibt zusätzlich machine-readable Status in 03_Tools/finnhub_health.json (Task 8).
"""

from __future__ import annotations

import argparse
import contextlib
import json
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

import finnhub_client

ROOT = Path(__file__).resolve().parents[1]
HEALTH_FILE = ROOT / "03_Tools" / "finnhub_health.json"

SATELLITES = ["MSFT", "V", "MA", "TMO", "COST", "VEEV", "APH", "AMZN", "AVGO", "ASML"]


def _today_str() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d")


def _days_ago(n: int) -> str:
    from datetime import timedelta

    return (datetime.now(UTC) - timedelta(days=n)).strftime("%Y-%m-%d")


def _days_ahead(n: int) -> str:
    from datetime import timedelta

    return (datetime.now(UTC) + timedelta(days=n)).strftime("%Y-%m-%d")


def test_quote_msft() -> tuple[bool, str]:
    data = finnhub_client.get_quote("MSFT", force=True)
    if data is None or "c" not in data:
        return False, "no data"
    age_h = (time.time() - data.get("t", 0)) / 3600
    return (age_h < 24, f"price={data['c']} age={age_h:.1f}h")


def test_quote_v() -> tuple[bool, str]:
    data = finnhub_client.get_quote("V", force=True)
    if data is None or "c" not in data:
        return False, "no data"
    age_h = (time.time() - data.get("t", 0)) / 3600
    return (age_h < 24, f"price={data['c']} age={age_h:.1f}h")


def test_earnings_bulk_skip() -> tuple[bool, str]:
    # Test 3 in Spec — Bulk-Endpoint liefert 0 Hits (dokumentiert)
    return False, "EXPECTED-FAIL bulk-endpoint not used (per-symbol-iteration in test 4)"


def test_earnings_per_symbol() -> tuple[bool, str]:
    hits = 0
    for sym in SATELLITES:
        events = finnhub_client.get_earnings(sym, _today_str(), _days_ahead(180), force=True)
        if events:
            hits += 1
    return (hits >= 10, f"{hits}/{len(SATELLITES)} satellites with future-earnings")


def test_brk_b() -> tuple[bool, str]:
    # Test 5 in Spec — BRK.B liefert BRK.A-Werte, dokumentiert
    return False, "EXPECTED-FAIL BRK.B liefert BRK.A-Werte (Memory feedback_brk_no_earnings_call)"


def test_europaeer_403() -> tuple[bool, str]:
    # Test 6 in Spec — RMS.PA + SU.PA = 403 expected
    rms = finnhub_client.get_metrics("RMS.PA")
    su = finnhub_client.get_metrics("SU.PA")
    return False, f"EXPECTED-FAIL Europäer Premium: rms={rms is None} su={su is None}"


def test_news_msft() -> tuple[bool, str]:
    items = finnhub_client.get_news("MSFT", _days_ago(7), _today_str(), force=True)
    if not items:
        return False, "no items"
    return (len(items) >= 1, f"{len(items)} news items")


def test_profile_msft() -> tuple[bool, str]:
    # Profile-Endpoint nicht im Wrapper — direkt request via private client
    client = finnhub_client._client()
    data = client._request("/stock/profile2", {"symbol": "MSFT"})
    if data is None:
        return False, "no data"
    return ("name" in data and "ticker" in data, f"name={data.get('name')}")


def test_metric_msft() -> tuple[bool, str]:
    data = finnhub_client.get_metrics("MSFT", force=True)
    if data is None or "metrics" not in data:
        return False, "no data"
    n = len(data["metrics"])
    has_for_scoring_false = data.get("_meta", {}).get("for_scoring") is False
    return (
        n >= 5 and has_for_scoring_false,
        f"metrics={n} for_scoring_guard={has_for_scoring_false}",
    )


TESTS = [
    ("1 /quote MSFT", test_quote_msft, True),  # (name, fn, expected_pass)
    ("2 /quote V", test_quote_v, True),
    ("3 /calendar/earnings bulk", test_earnings_bulk_skip, False),
    ("4 /calendar/earnings per-symbol", test_earnings_per_symbol, True),
    ("5 BRK.B calendar", test_brk_b, False),
    ("6 Europäer 403", test_europaeer_403, False),
    ("7 /company-news MSFT 7d", test_news_msft, True),
    ("8 /stock/profile2 MSFT", test_profile_msft, True),
    ("9 /stock/metric MSFT", test_metric_msft, True),
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="FinnHub Smoke-Test (Spec §3)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    with contextlib.suppress(Exception):
        sys.stdout.reconfigure(encoding="utf-8")

    results = []
    pass_count = 0
    fail_count = 0
    for name, fn, expected_pass in TESTS:
        try:
            ok, msg = fn()
        except Exception as e:  # noqa: BLE001
            ok, msg = False, f"EXCEPTION {type(e).__name__}: {e}"
        status = "PASS" if ok else ("EXPECTED-FAIL" if not expected_pass else "FAIL")
        if ok:
            pass_count += 1
        elif not expected_pass:
            # Expected-fail counts as "ok-in-spec"
            pass
        else:
            fail_count += 1
        results.append({"name": name, "status": status, "msg": msg})
        if args.verbose or not args.json:
            print(f"  [{status:14s}] {name} — {msg}")

    overall = (
        "healthy"
        if fail_count == 0 and pass_count >= 7
        else "degraded"
        if pass_count >= 5
        else "failed"
    )
    exit_code = 0 if overall == "healthy" else 1

    payload = {
        "schema_version": "v1",
        "last_run": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "status": overall,
        "pass": pass_count,
        "fail": fail_count,
        "endpoints": results,
    }

    # Write health-JSON (Task 8 spec)
    HEALTH_FILE.parent.mkdir(parents=True, exist_ok=True)
    HEALTH_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(
            f"\n=== {overall.upper()}: {pass_count} pass, {fail_count} unexpected-fail (exit {exit_code}) ==="
        )
        print(f"Health written: {HEALTH_FILE.relative_to(ROOT)}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
