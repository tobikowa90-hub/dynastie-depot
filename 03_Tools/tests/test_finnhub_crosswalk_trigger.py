"""finnhub_crosswalk_trigger.py — Schema- + Record-Tests (Spec §5.3 + A6)."""

from __future__ import annotations

import pytest

import finnhub_crosswalk_trigger as cwt


class TestCrosswalkRecord:
    def test_schema_fields_required(self) -> None:
        rec = cwt.CrosswalkRecord(
            timestamp="2026-05-23T10:00:00Z",
            run_id="20260523-MSFT-roic-001",
            batch_id="20260523-daily-crosswalk",
            symbol="MSFT",
            metric="roic",
            defeatbeta_value=27.45,
            finnhub_value=26.91,
            delta=-0.54,
            delta_unit="pp",
            tolerance_used="2pp",
            tolerance_status="within",
            na_reason=None,
            _meta={
                "read_only": True,
                "for_scoring": False,
                "schema_version": "v1",
                "defeatbeta_pulled_at": "2026-05-23T09:59:55Z",
                "finnhub_pulled_at": "2026-05-23T09:59:58Z",
            },
        )
        d = rec.model_dump()
        assert d["_meta"]["for_scoring"] is False
        assert d["_meta"]["read_only"] is True
        assert d["_meta"]["schema_version"] == "v1"

    def test_tolerance_status_enum_validated(self) -> None:
        with pytest.raises(ValueError):
            cwt.CrosswalkRecord(
                timestamp="2026-05-23T10:00:00Z",
                run_id="x",
                batch_id="y",
                symbol="MSFT",
                metric="roic",
                defeatbeta_value=None,
                finnhub_value=None,
                delta=None,
                delta_unit="pp",
                tolerance_used="2pp",
                tolerance_status="GARBAGE",  # invalid enum
                na_reason="both_missing",
                _meta={
                    "read_only": True,
                    "for_scoring": False,
                    "schema_version": "v1",
                    "defeatbeta_pulled_at": "x",
                    "finnhub_pulled_at": "y",
                },
            )

    def test_compute_delta_pp_within(self) -> None:
        delta, status = cwt.compute_delta(27.45, 26.91, "2pp")
        assert pytest.approx(delta, abs=0.001) == -0.54
        assert status == "within"

    def test_compute_delta_pp_warn(self) -> None:
        _delta, status = cwt.compute_delta(20.0, 23.5, "2pp")
        assert status == "warn"

    def test_compute_delta_pct_rel(self) -> None:
        _delta, status = cwt.compute_delta(100.0, 104.0, "5%")
        # 4% diff < 5% tolerance → within
        assert status == "within"

    def test_compute_delta_na_when_missing(self) -> None:
        delta, status = cwt.compute_delta(None, 27.0, "2pp")
        assert delta is None
        assert status == "na"

    def test_compute_delta_pct_rel_zero_divisor_returns_none(self) -> None:
        delta, status = cwt.compute_delta(0.0, 5.0, "5%")
        assert delta is None
        assert status == "na"
