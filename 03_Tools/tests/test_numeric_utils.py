"""Tests for _numeric_utils helpers (M2 Float-Tolerance-Gaps)."""

from __future__ import annotations

import math

import pytest

from _numeric_utils import float_close, peak_drawdown


class TestFloatClose:
    def test_exact_equal(self) -> None:
        assert float_close(1.0, 1.0)

    def test_fp_artefact_within_default_tol(self) -> None:
        # 0.1 + 0.2 == 0.30000000000000004 — classic FP artefact
        assert float_close(0.1 + 0.2, 0.3)

    def test_clearly_different(self) -> None:
        assert not float_close(1.0, 1.1)

    def test_abs_tol_override(self) -> None:
        assert float_close(0.0, 1e-12, abs_tol=1e-9)
        assert not float_close(0.0, 1e-8, abs_tol=1e-9)

    def test_rel_tol_override(self) -> None:
        assert float_close(1_000_000.0, 1_000_000.5, rel_tol=1e-6)
        assert not float_close(1_000_000.0, 1_010.0, rel_tol=1e-6)

    def test_nan_returns_false(self) -> None:
        assert not float_close(math.nan, math.nan)
        assert not float_close(1.0, math.nan)

    def test_inf_handling(self) -> None:
        assert float_close(math.inf, math.inf)
        assert not float_close(math.inf, -math.inf)

    def test_signed_zero(self) -> None:
        assert float_close(0.0, -0.0)


class TestPeakDrawdown:
    def test_monotonic_increase_zero_drawdown(self) -> None:
        assert peak_drawdown([1.0, 2.0, 3.0, 4.0]) == pytest.approx(0.0)

    def test_known_drawdown(self) -> None:
        # peak 100 → trough 60 → drawdown = 0.40
        assert peak_drawdown([100.0, 80.0, 60.0, 90.0]) == pytest.approx(0.40)

    def test_recovery_after_drawdown(self) -> None:
        # peak 100 → 50 (drawdown 0.5) → 200 (new peak) → 100 (drawdown 0.5)
        # max running drawdown = 0.5
        assert peak_drawdown([100.0, 50.0, 200.0, 100.0]) == pytest.approx(0.5)

    def test_empty_series_returns_zero(self) -> None:
        assert peak_drawdown([]) == 0.0

    def test_single_element(self) -> None:
        assert peak_drawdown([42.0]) == 0.0

    def test_all_equal(self) -> None:
        assert peak_drawdown([10.0, 10.0, 10.0]) == pytest.approx(0.0)

    def test_zero_peak_guard(self) -> None:
        # Peak == 0 → division-by-zero must be guarded; expect 0.0 or skip
        assert peak_drawdown([0.0, 0.0, -1.0]) == 0.0
