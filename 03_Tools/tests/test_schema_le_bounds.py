"""Tests for FundamentalsScore le-Bounds — REVISED Apply-Phase 2026-05-11.

Plan 2026-05-11-codebase-defect-patterns v1.2 Task 3.4 ORIGINAL intent:
per-field le=10 bounds for 6 positive FundamentalsScore sub-fields (M3-T1).

EMPIRICAL FINDING (Apply Phase 4 verification, advisor sparring 2026-05-11):
Legacy v1.0 records stored entire FundamentalsScore.gesamt (range 0-50) into
the `fwd_pe` sub-field (24/34 records have fwd_pe ∈ [29, 44]). Adding le=10
retroactively breaks jsonl_schema-Check Pydantic strict-revalidation.

DECISION: per-field bounds REVERTED in schemas.py; bounds-check deferred to
Audit-Layer with schema_version-Allowlist (parallel to sum_consistency M3-T2
Option C). This test file documents the gap and keeps the block-cap test.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backtest-ready"))

import pytest
from pydantic import ValidationError

from schemas import FundamentalsScore


def _base_kwargs(**overrides):
    base = {
        "fwd_pe": 0,
        "p_fcf": 0,
        "bilanz": 0,
        "capex_ocf": 0,
        "roic": 0,
        "fcf_yield": 0,
        "operating_margin": 0,
        "sbc_malus": 0,
        "accruals_malus": 0,
        "tariff_malus": 0,
        "gesamt": 0,
    }
    base.update(overrides)
    return base


def test_fundamentals_block_cap_still_enforced() -> None:
    """gesamt > FUNDAMENTALS_CAP=50 muss reject — block-cap bounds bleiben."""
    with pytest.raises(ValidationError):
        FundamentalsScore(
            **_base_kwargs(
                fwd_pe=44,
                p_fcf=10,
                bilanz=10,
                capex_ocf=10,
                roic=10,
                fcf_yield=10,
                gesamt=60,  # > 50
            )
        )


def test_fundamentals_accepts_legacy_v1_fwd_pe_high_value() -> None:
    """Legacy v1.0 records mit fwd_pe>10 (z.B. 44 für PEGA) müssen weiterhin
    Pydantic-parsen — Apply-Phase Empirie zeigt 24/34 v1.0-Records mit fwd_pe
    in [29, 44]. Per-field le=10 würde diese alle retro-invalidieren."""
    obj = FundamentalsScore(**_base_kwargs(fwd_pe=44, gesamt=44))
    assert obj.fwd_pe == 44
    assert obj.gesamt == 44


def test_operating_margin_le_bound_still_enforced() -> None:
    """v3.7 sub-field operating_margin behält le=2 (NEU eingeführt; legacy=0)."""
    with pytest.raises(ValidationError):
        FundamentalsScore(**_base_kwargs(operating_margin=3, gesamt=3))


@pytest.mark.parametrize(
    "field,bad_value",
    [
        ("sbc_malus", 1),  # le=0, malus → muss <= 0 sein
        ("accruals_malus", 1),  # le=0
        ("tariff_malus", 1),  # le=0
    ],
)
def test_malus_le_zero_enforced(field: str, bad_value: int) -> None:
    """Malus-Felder behalten le=0 (existing, nicht Plan-Phase-3 changed)."""
    with pytest.raises(ValidationError):
        FundamentalsScore(**_base_kwargs(**{field: bad_value, "gesamt": 0}))
