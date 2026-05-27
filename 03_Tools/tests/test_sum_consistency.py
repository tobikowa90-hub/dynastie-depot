"""Tests for sum_consistency audit-check (M3-T2 Option C).

Scope: schema_version-Allowlist — v1.0 grandfathered (INFO), v2.0+ strict (FAIL).
MoatScore explicitly skipped (rating-derived .gesamt).
"""

from __future__ import annotations

import json
from pathlib import Path


def _write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")


def _v1_legacy_record(ticker: str = "TEST") -> dict:
    """Schema-v1.0 record with Sub-Sum=0 + gesamt>0 (Legacy-Migration-Artefakt)."""
    return {
        "record_id": f"2026-04-17_{ticker}_vollanalyse",
        "ticker": ticker,
        "schema_version": "1.0",
        "score_datum": "2026-04-17",
        "score_gesamt": 50,
        "scores": {
            "fundamentals": {
                "gesamt": 30,
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
            },
            "moat": {
                "gesamt": 15,
                "rating": "wide",
                "quellen": [],
                "gm_trend_delta": 0,
                "pricing_power_bonus": 0,
            },
            "technicals": {
                "gesamt": 7,
                "ath_distanz": 0,
                "rel_staerke": 0,
                "trend_lage": 0,
                "dcf_relation_delta": 0,
            },
            "insider": {"gesamt": 7, "net_buy_6m": 0, "ownership": 0, "kein_20m_selling": 0},
            "sentiment": {
                "gesamt": 7,
                "strong_buy_ratio": 0,
                "sell_ratio": 0,
                "pt_upside": 0,
                "eps_revision_delta": 0,
                "pt_dispersion_delta": 0,
            },
        },
    }


def _v2_strict_record(
    ticker: str = "TEST",
    *,
    sentiment_gesamt: int = 8,
    sentiment_subs: tuple[int, ...] = (4, 0, 3, 1, 0),
) -> dict:
    """Schema-v2.0 record with proper Sub-Field-Belegung."""
    return {
        "record_id": f"2026-05-11_{ticker}_vollanalyse",
        "ticker": ticker,
        "schema_version": "2.0",
        "score_datum": "2026-05-11",
        "score_gesamt": 60,
        "scores": {
            "fundamentals": {
                "gesamt": 31,
                "fwd_pe": 5,
                "p_fcf": 5,
                "bilanz": 5,
                "capex_ocf": 5,
                "roic": 5,
                "fcf_yield": 5,
                "operating_margin": 1,
                "sbc_malus": 0,
                "accruals_malus": 0,
                "tariff_malus": 0,
            },
            "moat": {
                "gesamt": 15,
                "rating": "wide",
                "quellen": [],
                "gm_trend_delta": 0,
                "pricing_power_bonus": 0,
            },
            "technicals": {
                "gesamt": 11,
                "ath_distanz": 4,
                "rel_staerke": 3,
                "trend_lage": 3,
                "dcf_relation_delta": 1,
            },
            "insider": {"gesamt": 8, "net_buy_6m": 3, "ownership": 2, "kein_20m_selling": 3},
            "sentiment": {
                "gesamt": sentiment_gesamt,
                "strong_buy_ratio": sentiment_subs[0],
                "sell_ratio": sentiment_subs[1],
                "pt_upside": sentiment_subs[2],
                "eps_revision_delta": sentiment_subs[3],
                "pt_dispersion_delta": sentiment_subs[4],
            },
        },
    }


class TestSumConsistency:
    def test_v1_legacy_grandfathered_pass_with_info(self, tmp_path: Path) -> None:
        """v1.0 records with Sub-Sum=0 + gesamt>0 → PASS, but INFO-level note."""
        from system_audit.audit_types import AuditContext
        from system_audit.checks.sum_consistency import run

        store = tmp_path / "score_history.jsonl"
        _write_jsonl(store, [_v1_legacy_record("ASML")])
        ctx = AuditContext(repo_root=tmp_path)

        result = run(tmp_path, ctx, store_override=store)
        assert result.status == "PASS"
        info_findings = [f for f in result.failures if f.severity == "info"]
        assert len(info_findings) >= 1, "Expected INFO-Hint für Legacy v1.0 Sub-Sum-Mismatch"

    def test_v2_strict_sum_match_passes(self, tmp_path: Path) -> None:
        from system_audit.audit_types import AuditContext
        from system_audit.checks.sum_consistency import run

        store = tmp_path / "score_history.jsonl"
        _write_jsonl(store, [_v2_strict_record("ASML")])
        ctx = AuditContext(repo_root=tmp_path)

        result = run(tmp_path, ctx, store_override=store)
        assert result.status == "PASS"
        assert not any(f.severity == "error" for f in result.failures)

    def test_v2_sentiment_sum_mismatch_fails(self, tmp_path: Path) -> None:
        """v2.0 record with sentiment.gesamt != sum(numerics) → FAIL."""
        from system_audit.audit_types import AuditContext
        from system_audit.checks.sum_consistency import run

        store = tmp_path / "score_history.jsonl"
        bad = _v2_strict_record("BAD", sentiment_gesamt=99)
        _write_jsonl(store, [bad])
        ctx = AuditContext(repo_root=tmp_path)

        result = run(tmp_path, ctx, store_override=store)
        assert result.status == "FAIL"
        fails = [f for f in result.failures if f.severity == "error"]
        assert any("sentiment" in f.location.lower() for f in fails)

    def test_moat_explicit_skip_v2(self, tmp_path: Path) -> None:
        """MoatScore.gesamt rating-derived — niemals Sum-Check, auch v2.0."""
        from system_audit.audit_types import AuditContext
        from system_audit.checks.sum_consistency import run

        store = tmp_path / "score_history.jsonl"
        rec = _v2_strict_record("MOAT")
        rec["scores"]["moat"] = {
            "gesamt": 15,
            "rating": "wide",
            "quellen": [],
            "gm_trend_delta": 0,
            "pricing_power_bonus": 0,
        }
        _write_jsonl(store, [rec])
        ctx = AuditContext(repo_root=tmp_path)

        result = run(tmp_path, ctx, store_override=store)
        assert result.status == "PASS"
        moat_fails = [
            f for f in result.failures if f.severity == "error" and "moat" in f.location.lower()
        ]
        assert len(moat_fails) == 0

    def test_mixed_v1_and_v2_records(self, tmp_path: Path) -> None:
        """Gemischtes JSONL: v1.0 Legacy + v2.0 Strict → PASS overall (kein FAIL)."""
        from system_audit.audit_types import AuditContext
        from system_audit.checks.sum_consistency import run

        store = tmp_path / "score_history.jsonl"
        _write_jsonl(
            store,
            [
                _v1_legacy_record("ASML"),
                _v2_strict_record("AVGO"),
            ],
        )
        ctx = AuditContext(repo_root=tmp_path)

        result = run(tmp_path, ctx, store_override=store)
        assert result.status == "PASS"
        info = [f for f in result.failures if f.severity == "info"]
        errs = [f for f in result.failures if f.severity == "error"]
        assert len(info) >= 1
        assert len(errs) == 0

    def test_missing_store_skip(self, tmp_path: Path) -> None:
        """Missing store → SKIP (analog jsonl_schema.py-Pattern)."""
        from system_audit.audit_types import AuditContext
        from system_audit.checks.sum_consistency import run

        store = tmp_path / "absent.jsonl"
        ctx = AuditContext(repo_root=tmp_path)
        result = run(tmp_path, ctx, store_override=store)
        assert result.status in ("SKIP", "WARN")
