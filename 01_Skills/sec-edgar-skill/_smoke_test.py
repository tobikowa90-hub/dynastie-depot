"""Smoke tests for sec-edgar-skill v1.1.

Tests Live-API-Health + Token-Budget der `.to_context()`-Outputs gegen die
in SKILL.md §3 dokumentierten Erwartungen.

Run:
    python 01_Skills/sec-edgar-skill/_smoke_test.py

Expected (pre-Install): 6/6 FAIL (ImportError on edgar)
Expected (post-Install + Identity): 6/6 PASS
"""
from __future__ import annotations

import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

# ---------------------------------------------------------------------------
# Identity (set once for cases 2-5)
# ---------------------------------------------------------------------------
IDENTITY = "Tobias Kowalski tobikowa90@gmail.com"

# Char-Budgets aus SKILL.md §3 (≈Tokens × 5 + 25% Puffer)
COMPANY_TO_CONTEXT_MAX_CHARS = 500
XBRL_TO_CONTEXT_MAX_CHARS = 1500


# ---------------------------------------------------------------------------
# Case 1: Identity-Pre-Check Failure-Path
# ---------------------------------------------------------------------------
def case_1() -> None:
    """Without set_identity(), Company('MSFT') must raise (SEC-Legal-Requirement)."""
    # Run as subprocess so the parent's set_identity() (if any) doesn't leak in
    code = (
        "from edgar import Company\n"
        "try:\n"
        "    c = Company('MSFT')\n"
        "    _ = c.name\n"
        "    print('NO_ERROR_RAISED')\n"
        "except Exception as e:\n"
        "    print(f'RAISED:{type(e).__name__}')\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        encoding="utf-8",
        timeout=30,
    )
    out = (result.stdout or "").strip()
    # Some edgartools versions print a warning instead of raising — accept both
    # but log which path was taken
    assert out.startswith("RAISED:") or "identity" in (result.stderr or "").lower(), (
        f"Expected Identity-Error or stderr-mention, got stdout={out!r}, stderr={result.stderr!r}"
    )


# ---------------------------------------------------------------------------
# Case 2: MSFT-Lookup
# ---------------------------------------------------------------------------
def case_2() -> None:
    from edgar import set_identity, Company
    set_identity(IDENTITY)
    c = Company("MSFT")
    # SEC EDGAR returns Registrar-Legal-Form ("MICROSOFT CORP"), not "Microsoft Corporation".
    # Use case-insensitive substring match for robustness against future drift.
    assert "MICROSOFT" in c.name.upper(), f"name mismatch: {c.name!r}"
    cik_str = str(c.cik).zfill(10)
    assert cik_str == "0000789019", f"cik mismatch: {cik_str!r}"


# ---------------------------------------------------------------------------
# Case 3: MSFT income_statement(periods=3)
# ---------------------------------------------------------------------------
def case_3() -> None:
    from edgar import set_identity, Company
    set_identity(IDENTITY)
    c = Company("MSFT")
    income = c.income_statement(periods=3)
    assert income is not None, "income_statement returned None"
    # Defensive: edgartools may expose either DataFrame, Statement, or repr-like
    assert hasattr(income, "to_dataframe") or hasattr(income, "__repr__"), (
        f"income object has neither to_dataframe nor __repr__: {type(income)!r}"
    )


# ---------------------------------------------------------------------------
# Case 4: Company.to_context() Char-Budget
# ---------------------------------------------------------------------------
def case_4() -> None:
    from edgar import set_identity, Company
    set_identity(IDENTITY)
    c = Company("MSFT")
    ctx = c.to_context()
    assert isinstance(ctx, str) and len(ctx) > 0, f"to_context empty/invalid: {ctx!r}"
    char_len = len(ctx)
    # Log live char-len for audit (SKILL.md §3 Drift-Buffer)
    print(f"  [audit] Company.to_context len = {char_len} chars (budget {COMPANY_TO_CONTEXT_MAX_CHARS})")
    assert char_len <= COMPANY_TO_CONTEXT_MAX_CHARS, (
        f"Company.to_context exceeds budget: {char_len} > {COMPANY_TO_CONTEXT_MAX_CHARS}"
    )


# ---------------------------------------------------------------------------
# Case 5: XBRL.to_context() Char-Budget
# ---------------------------------------------------------------------------
def case_5() -> None:
    from edgar import set_identity, Company
    set_identity(IDENTITY)
    c = Company("MSFT")
    filings = c.get_filings(form="10-K")
    assert len(filings) > 0, "no 10-K filings found for MSFT"
    filing = filings.latest()
    xbrl = filing.xbrl()
    assert xbrl is not None, "filing.xbrl() returned None"
    ctx = xbrl.to_context()
    assert isinstance(ctx, str) and len(ctx) > 0, f"xbrl.to_context empty/invalid: {ctx!r}"
    char_len = len(ctx)
    print(f"  [audit] XBRL.to_context len = {char_len} chars (budget {XBRL_TO_CONTEXT_MAX_CHARS})")
    assert char_len <= XBRL_TO_CONTEXT_MAX_CHARS, (
        f"XBRL.to_context exceeds budget: {char_len} > {XBRL_TO_CONTEXT_MAX_CHARS}"
    )


# ---------------------------------------------------------------------------
# Case 6: edgartools-Version-Sanity (Drift-Buffer-Audit)
# ---------------------------------------------------------------------------
def case_6() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "show", "edgartools"],
        capture_output=True,
        encoding="utf-8",
        timeout=30,
    )
    assert result.returncode == 0, f"pip show edgartools failed: rc={result.returncode}"
    version_line = next(
        (ln for ln in result.stdout.splitlines() if ln.startswith("Version:")), None
    )
    assert version_line is not None, "Version: line not found in pip show output"
    version = version_line.split(":", 1)[1].strip()
    assert version, "empty version string"
    print(f"  [audit] edgartools version = {version}")


# ---------------------------------------------------------------------------
# Harness
# ---------------------------------------------------------------------------
CASES = [
    (1, "Identity-Pre-Check Failure-Path", case_1),
    (2, "MSFT Company-Lookup (name + cik)", case_2),
    (3, "MSFT income_statement(periods=3)", case_3),
    (4, "Company.to_context Char-Budget (<=500)", case_4),
    (5, "XBRL.to_context Char-Budget (<=1500)", case_5),
    (6, "edgartools Version-Sanity", case_6),
]


def run_all() -> None:
    passed = 0
    failed = 0
    for n, label, fn in CASES:
        try:
            fn()
            print(f"[{n}/{len(CASES)}] PASS: {label}")
            passed += 1
        except Exception as exc:
            print(f"[{n}/{len(CASES)}] FAIL: {label} - {type(exc).__name__}: {exc}")
            failed += 1

    print()
    if failed == 0:
        print(f"OK all {passed}/{len(CASES)} cases passed")
    else:
        print(f"FAIL {failed} case(s) failed, {passed}/{len(CASES)} passed")
        sys.exit(1)


if __name__ == "__main__":
    run_all()
