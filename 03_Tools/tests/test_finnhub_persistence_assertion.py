"""Persistence-Layer-Guard gegen FinnHub-Metriken im Scoring-Pfad (Spec §9 R1)."""

from __future__ import annotations

import sys
from pathlib import Path

# Import path: 03_Tools/backtest-ready/ is the package-dir (sibling of tests/).
# conftest.py adds 03_Tools/ but not the backtest-ready subdir.
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "03_Tools" / "backtest-ready"))

import pytest  # noqa: E402  (sys.path setup must precede import)
from archive_score import _assert_metric_for_scoring  # noqa: E402


class TestForScoringAssertion:
    def test_passes_when_meta_for_scoring_true(self) -> None:
        metric = {"value": 27.45, "_meta": {"for_scoring": True, "source": "defeatbeta"}}
        _assert_metric_for_scoring(metric)  # no raise

    def test_passes_when_no_meta_at_all_legacy(self) -> None:
        # Legacy Records ohne _meta-Block = defeatbeta-implicit, dürfen weiter durch
        metric = {"value": 27.45}
        _assert_metric_for_scoring(metric)

    def test_raises_when_for_scoring_false(self) -> None:
        metric = {"value": 27.45, "_meta": {"for_scoring": False, "source": "finnhub"}}
        with pytest.raises(
            AssertionError,
            match=r"FinnHub-Metriken sind in v0.1 NICHT für Scoring zugelassen",
        ):
            _assert_metric_for_scoring(metric)

    def test_non_dict_meta_passes_through_for_pydantic_to_catch(self) -> None:
        """Malformed _meta (non-dict) does NOT crash — defers to pydantic ValidationError."""
        metric = {"value": 27.45, "_meta": "garbage-string-not-a-dict"}
        _assert_metric_for_scoring(metric)  # must not raise AttributeError
        metric_list = {"value": 27.45, "_meta": ["also", "not", "a", "dict"]}
        _assert_metric_for_scoring(metric_list)  # must not raise either
