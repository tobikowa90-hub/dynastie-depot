"""Numeric helpers — Float-Tolerance + Drawdown.

Dynastie-Defaults: abs_tol=1e-9, rel_tol=1e-6. Verwendung: bei Float-Compare
zuerst float_close prüfen, dann >/<. Direkter == auf Floats ist Bug-Smell.
"""

from __future__ import annotations

import math
from collections.abc import Sequence

DEFAULT_ABS_TOL = 1e-9
DEFAULT_REL_TOL = 1e-6


def float_close(
    a: float,
    b: float,
    *,
    abs_tol: float = DEFAULT_ABS_TOL,
    rel_tol: float = DEFAULT_REL_TOL,
) -> bool:
    """Return True iff a and b are close within abs_tol or rel_tol.

    Wraps math.isclose with Dynastie defaults. NaN-safe: NaN compares never close.
    """
    if math.isnan(a) or math.isnan(b):
        return False
    return math.isclose(a, b, abs_tol=abs_tol, rel_tol=rel_tol)


def peak_drawdown(series: Sequence[float]) -> float:
    """Return maximum peak-to-trough drawdown as positive fraction.

    Running-peak scan: for each point x_i, drawdown_i = (peak_i - x_i) / peak_i
    where peak_i = max(x_0..x_i). Returns max over all drawdown_i.

    Range: typically [0, 1] for non-negative bounded series (e.g. asset prices,
    scores). For series that go negative below a positive peak, drawdown can
    exceed 1.0 (e.g. peak=10, trough=-10 → dd=2.0). Empty/single-element
    series → 0.0. Peak <= 0 sites contribute 0.0 (no div-by-zero).
    """
    max_dd = 0.0
    peak = float("-inf")
    for x in series:
        if x > peak:
            peak = x
        if peak > 0.0:
            dd = (peak - x) / peak
            if dd > max_dd:
                max_dd = dd
    return max_dd
