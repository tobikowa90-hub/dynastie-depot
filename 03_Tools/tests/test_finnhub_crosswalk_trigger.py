"""finnhub_crosswalk_trigger.py — Schema- + Record-Tests (Spec §5.3 + A6)."""

from __future__ import annotations

import json
from pathlib import Path

import pydantic
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

    def test_strict_mode_rejects_str_coercion_for_numeric_fields(self) -> None:
        """Spec §5.3 says number|null — strict-mode prevents silent str-to-float coercion."""
        with pytest.raises(pydantic.ValidationError):
            cwt.CrosswalkRecord(
                timestamp="2026-05-23T10:00:00Z",
                run_id="x",
                batch_id="y",
                symbol="MSFT",
                metric="roic",
                defeatbeta_value="27.45",  # str instead of float — must be rejected
                finnhub_value=26.91,
                delta=-0.54,
                delta_unit="pp",
                tolerance_used="2pp",
                tolerance_status="within",
                _meta={
                    "read_only": True,
                    "for_scoring": False,
                    "schema_version": "v1",
                    "defeatbeta_pulled_at": "x",
                    "finnhub_pulled_at": "y",
                },
            )


class TestMainRun:
    def test_a6_24_records_3_symbols_8_metrics(self, tmp_path: Path, monkeypatch) -> None:
        """A6: 3 symbols × 8 metrics = 24 records in JSONL, schema-conform."""
        log_path = tmp_path / "crosswalk_log.jsonl"
        monkeypatch.setattr(cwt, "LOG_FILE", log_path)

        def fake_defeatbeta(sym):
            return {
                "peTTM": 35.0,
                "roe": 27.0,
                "roic": 25.0,
                "grossMargin5Y": 65.0,
                "debtToEquity": 1.5,
                "epsGrowth5Y": 12.0,
                "capexCagr5Y": 8.0,
                "fcfPerShareTTM": 10.0,
            }

        def fake_finnhub(sym, force=False):
            return {
                "metrics": {
                    "peTTM": 35.5,
                    "roeTTM": 27.2,
                    "roiTTM": 25.1,
                    "grossMargin5Y": 65.3,
                    "totalDebt/totalEquityQuarterly": 1.45,
                    "epsGrowth5Y": 12.5,
                    "capexCagr5Y": 8.3,
                    "fcfPerShareTTM": 10.1,
                },
                "_meta": {
                    "read_only": True,
                    "for_scoring": False,
                    "source": "finnhub",
                    "fetched_at": 0.0,
                },
            }

        monkeypatch.setattr(cwt.defeatbeta_subprocess, "pull_metrics", fake_defeatbeta)
        monkeypatch.setattr(cwt.finnhub_client, "get_metrics", fake_finnhub)

        cwt.main(["--symbols", "MSFT,V,ASML"])

        lines = log_path.read_text(encoding="utf-8").splitlines()
        assert len(lines) == 24, f"expected 24 records, got {len(lines)}"
        records = [json.loads(line) for line in lines]
        # Common batch_id
        batch_ids = {r["batch_id"] for r in records}
        assert len(batch_ids) == 1, f"all records must share batch_id, got {batch_ids}"
        # Unique run_ids
        run_ids = [r["run_id"] for r in records]
        assert len(set(run_ids)) == 24, "run_ids must be unique"
        # Schema-Conform _meta
        for r in records:
            assert r["_meta"]["for_scoring"] is False
            assert r["_meta"]["read_only"] is True
            assert r["_meta"]["schema_version"] == "v1"
            assert "defeatbeta_pulled_at" in r["_meta"]
            assert "finnhub_pulled_at" in r["_meta"]
        # Symbol-Coverage
        symbols_in = {r["symbol"] for r in records}
        assert symbols_in == {"MSFT", "V", "ASML"}
        # Metric-Coverage
        metrics_in = {r["metric"] for r in records}
        assert metrics_in == set(cwt.METRIC_TOLERANCES.keys())
