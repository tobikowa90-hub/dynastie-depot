"""Deterministischer Fixture-Generator für die pre-commit-Validatoren (Spec §5.2).

Erzeugt je Validator 1 real-valide + 1 real-invalide Fixture, byte-exakt:
  - CRLF-Fixtures binär (`wb`, NIE Text-Mode — Memory
    feedback_windows_python_crlf_text_mode)
  - JSONL-Fixtures aus den kanonischen schemas.py-Smoke-Wahrheiten
    (Schema-Drift → model_validate wirft hier laut = gewollt, Akzeptanz #2)
  - xlsx-Fixtures via openpyxl (Watchlist-Minimal-Profil — kein fragiler
    CF-Count-Fake)

Namen sind beschreibend (kein generisches `bad_*`/`good_*` — Memory
feedback_cr_convergence_and_project_compat). Idempotent; kein Timestamp/Random.

Lauf: `python 03_Tools/precommit/_fixtures/_generate_fixtures.py`
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_BACKTEST_DIR = _HERE.parent.parent / "backtest-ready"
if str(_BACKTEST_DIR) not in sys.path:
    sys.path.insert(0, str(_BACKTEST_DIR))

import openpyxl  # noqa: E402

from schemas import FlagEvent, ScoreRecord  # noqa: E402

# Kanonisch-valider ScoreRecord (= schemas.py _smoke_tests Case 1 AVGO,
# post-Quality-Trap-adjustiert: fwd_pe/p_fcf=1, fundamentals.gesamt=33,
# score_gesamt=80, defcon 4).
_VALID_SCORE: dict = {
    "schema_version": "1.0",
    "record_id": "2026-04-02_AVGO_vollanalyse",
    "source": "forward",
    "ticker": "AVGO",
    "score_datum": "2026-04-02",
    "analyse_typ": "vollanalyse",
    "defcon_version": "v3.7",
    "kurs": {
        "wert": 1847.32,
        "waehrung": "USD",
        "referenz": "close_of_score_datum",
        "quelle": "yahoo_eod",
    },
    "market_cap": {"wert": 865.4e9, "waehrung": "USD"},
    "scores": {
        "fundamentals": {
            "gesamt": 33,
            "fwd_pe": 1,
            "p_fcf": 1,
            "bilanz": 8,
            "capex_ocf": 7,
            "roic": 8,
            "fcf_yield": 6,
            "operating_margin": 2,
            "sbc_malus": 0,
            "accruals_malus": 0,
            "tariff_malus": 0,
        },
        "moat": {
            "gesamt": 18,
            "rating": "wide",
            "quellen": ["switching_costs", "intangibles"],
            "gm_trend_delta": 0,
            "pricing_power_bonus": 1,
        },
        "technicals": {
            "gesamt": 10,
            "ath_distanz": 4,
            "rel_staerke": 3,
            "trend_lage": 3,
            "dcf_relation_delta": 0,
        },
        "insider": {"gesamt": 10, "net_buy_6m": 4, "ownership": 3, "kein_20m_selling": 3},
        "sentiment": {
            "gesamt": 9,
            "strong_buy_ratio": 4,
            "sell_ratio": 3,
            "pt_upside": 2,
            "eps_revision_delta": 0,
            "pt_dispersion_delta": 0,
        },
    },
    "score_gesamt": 80,
    "defcon_level": 4,
    "flags": {"aktiv_ids": [], "bei_analyse_referenziert": []},
    "metriken_roh": {
        "fwd_pe": 22.1,
        "p_fcf": 19.8,
        "roic_gaap_pct": 14.2,
        "wacc_pct": 9.1,
        "gm_trend_3j_pct_p_a": 0.3,
        "rel_strength_sp500_6m_pct": 4,
        "kurs_vs_200ma_pct": 12.5,
        "ma200_slope": "rising",
        "eps_revisions_up_90d": 4,
        "eps_revisions_down_90d": 0,
        "pt_dispersion_pct": 22,
    },
    "quellen": {
        "fundamentals": "defeatbeta",
        "technicals": "shibui",
        "insider": "openinsider+sec_edgar",
        "moat": "gurufocus",
        "sentiment": "zacks+yahoo",
    },
    "notizen": "Fixture — kanonischer AVGO Forward-Record v3.7",
}

# Kanonisch-valider FlagEvent (= schemas.py _smoke_tests Case 5 GOOGL).
_VALID_FLAG: dict = {
    "schema_version": "1.0",
    "flag_id": "GOOGL_capex_ocf_2025-10-28",
    "source": "forward",
    "ticker": "GOOGL",
    "flag_typ": "capex_ocf",
    "event_typ": "trigger",
    "event_datum": "2025-10-28",
    "metrik": {
        "name": "capex_ocf_pct",
        "wert": 78,
        "schwelle": 60,
        "definition": "annual_cash_flow_fy26_guidance",
    },
    "kurs_bei_event": {
        "wert": 142.30,
        "waehrung": "USD",
        "referenz": "close_of_event_datum",
        "quelle": "yahoo_eod",
    },
    "related_score_record_id": "2025-10-28_GOOGL_vollanalyse",
    "notizen": "Fixture — kanonischer GOOGL capex_ocf trigger",
}


def _write_bytes(name: str, data: bytes) -> None:
    (_HERE / name).write_bytes(data)
    print(f"  wrote {name} ({len(data)} bytes)")


def main() -> int:
    # Fail laut, falls Schema gedriftet ist (Akzeptanz #2).
    ScoreRecord.model_validate(_VALID_SCORE)
    FlagEvent.model_validate(_VALID_FLAG)

    score_line = json.dumps(_VALID_SCORE, ensure_ascii=False)
    flag_line = json.dumps(_VALID_FLAG, ensure_ascii=False)

    # crlf-guard: LF-clean vs CRLF-kontaminiert (byte-exakt).
    _write_bytes("crlf_lf_clean.input", (score_line + "\n").encode("utf-8"))
    _write_bytes(
        "crlf_carriage_return_contaminated.input",
        (score_line + "\r\n").encode("utf-8"),
    )

    # validate-score-history: valider Append vs Schema-Verstoß (extra-Feld,
    # ScoreRecord extra='forbid').
    _write_bytes("score_history_valid_append.input", (score_line + "\n").encode("utf-8"))
    bad_score = {**_VALID_SCORE, "_unexpected_extra_field": True}
    _write_bytes(
        "score_history_schema_violation.input",
        (json.dumps(bad_score, ensure_ascii=False) + "\n").encode("utf-8"),
    )

    # validate-flag-events: valide vs flag_typ außerhalb des Literals.
    _write_bytes("flag_events_valid.input", (flag_line + "\n").encode("utf-8"))
    bad_flag = {**_VALID_FLAG, "flag_typ": "nonexistent_flag_typ"}
    _write_bytes(
        "flag_events_schema_violation.input",
        (json.dumps(bad_flag, ensure_ascii=False) + "\n").encode("utf-8"),
    )

    # xlsx-smoke-test: Watchlist-Minimal-Profil (Name-Prefix matcht
    # _PROFILES["Watchlist_Ersatzbank_Monitor"]). clean = A1 gesetzt → PASS;
    # empty_a1 = A1 leer → FAIL Punkt A.
    wb_ok = openpyxl.Workbook()
    wb_ok.active["A1"] = "fixture"
    wb_ok.save(_HERE / "Watchlist_Ersatzbank_Monitor_fixture_clean.xlsx")
    print("  wrote Watchlist_Ersatzbank_Monitor_fixture_clean.xlsx")

    wb_bad = openpyxl.Workbook()
    wb_bad.active["A1"] = None
    wb_bad.save(_HERE / "Watchlist_Ersatzbank_Monitor_fixture_empty_a1.xlsx")
    print("  wrote Watchlist_Ersatzbank_Monitor_fixture_empty_a1.xlsx")

    print("✅ fixtures generated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
