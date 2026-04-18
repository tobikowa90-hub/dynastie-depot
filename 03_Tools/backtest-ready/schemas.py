"""Pydantic v2 schemas for the Dynasty-Depot backtest-ready archive.

Defines the JSONL record shapes for `05_Archiv/score_history.jsonl` and
`05_Archiv/flag_events.jsonl`. Every CLI in this folder imports from here —
do not define record shapes elsewhere.

DEFCON v3.7 alignment:
  - Fundamentals Block Cap 50 (hart, v3.7)
  - Operating-Margin Sub-Score (0-2, v3.7 Fix 2)
  - Sentiment `strong_buy_ratio` ersetzt `konsensus` (v3.7 Fix 3)
  - Quality-Trap-Interaktion (v3.7 Fix 1, Cross-Validator)
  - Technicals-Rename `rel_staerke` / `trend_lage` (v3.5)
"""

from __future__ import annotations

import re
from datetime import date
from typing import Final, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------

FUNDAMENTALS_CAP: Final[int] = 50  # v3.7 hard cap
FUNDAMENTALS_FLOOR: Final[int] = 0  # v3.5 floor

# Quality-Trap thresholds (v3.7 Fix 1)
QT_FWD_PE_HARD: Final[float] = 30.0
QT_FWD_PE_MAX1_LOW: Final[float] = 22.0
QT_P_FCF_HARD: Final[float] = 35.0
QT_P_FCF_MAX1_LOW: Final[float] = 22.0

# FLAG-Typ Schwellen + Verletzungsrichtung (Spec Section 4.2)
FLAG_RULES: Final[dict[str, tuple[float, str]]] = {
    "capex_ocf": (60.0, ">"),
    "fcf_trend_neg": (0.0, "<"),
    "insider_selling_20m": (20_000_000.0, ">"),
    "tariff_exposure": (35.0, ">"),
}

# ID format regexes
RECORD_ID_RE: Final[re.Pattern[str]] = re.compile(
    r"^\d{4}-\d{2}-\d{2}_[A-Z]{1,5}(\.[A-Z]{1,2})?_(vollanalyse|delta|rescoring)$"
)
FLAG_ID_RE: Final[re.Pattern[str]] = re.compile(
    r"^[A-Z]{1,5}(\.[A-Z]{1,2})?_[a-z_0-9]+_\d{4}-\d{2}-\d{2}$"
)


# ---------------------------------------------------------------------------
# Nested structs
# ---------------------------------------------------------------------------


class Kurs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    wert: float
    waehrung: str
    referenz: str
    quelle: str


class MarketCap(BaseModel):
    model_config = ConfigDict(extra="forbid")

    wert: float
    waehrung: str


class Flags(BaseModel):
    model_config = ConfigDict(extra="forbid")

    aktiv_ids: list[str] = Field(default_factory=list)
    bei_analyse_referenziert: list[str] = Field(default_factory=list)


class Quellen(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fundamentals: str
    technicals: str
    insider: str
    moat: str
    sentiment: str


# ---------------------------------------------------------------------------
# Score blocks
# ---------------------------------------------------------------------------


class FundamentalsScore(BaseModel):
    """v3.7: Floor 0, Cap 50 (hart). Sub-Score `operating_margin` neu (0-2)."""

    model_config = ConfigDict(extra="forbid")

    gesamt: int = Field(..., ge=FUNDAMENTALS_FLOOR, le=FUNDAMENTALS_CAP)
    fwd_pe: int = Field(..., ge=0)
    p_fcf: int = Field(..., ge=0)
    bilanz: int = Field(..., ge=0)
    capex_ocf: int = Field(..., ge=0)
    roic: int = Field(..., ge=0)
    fcf_yield: int = Field(..., ge=0)
    operating_margin: int = Field(..., ge=0, le=2)  # v3.7 neu
    sbc_malus: int = Field(..., le=0)
    accruals_malus: int = Field(..., le=0)
    tariff_malus: int = Field(..., le=0)


class MoatScore(BaseModel):
    model_config = ConfigDict(extra="forbid")

    gesamt: int = Field(..., ge=0, le=20)
    rating: Literal["wide", "narrow", "none"]
    quellen: list[str] = Field(default_factory=list)
    gm_trend_delta: int = Field(..., ge=-1, le=1)
    pricing_power_bonus: int = Field(..., ge=0, le=1)


class TechnicalsScore(BaseModel):
    """v3.5: `pt_upside`+`rel_strength_delta` → `rel_staerke`+`trend_lage`. Block-Cap 10 Punkte + DCF-Bonus ±1 (SKILL.md §Technicals)."""

    model_config = ConfigDict(extra="forbid")

    # Block-Cap: 4+3+3 = 10 Sub-Max + DCF-Bonus +1 = 11; DCF-Malus -1 = Floor -1
    gesamt: int = Field(..., ge=-1, le=11)
    ath_distanz: int = Field(..., ge=0, le=4)
    rel_staerke: int = Field(..., ge=0, le=3)
    trend_lage: int = Field(..., ge=0, le=3)
    dcf_relation_delta: int = Field(..., ge=-1, le=1)


class InsiderScore(BaseModel):
    """Block-Cap 10 Punkte: 4+3+3 (SKILL.md §Insider)."""

    model_config = ConfigDict(extra="forbid")

    gesamt: int = Field(..., ge=0, le=10)
    net_buy_6m: int = Field(..., ge=0, le=4)
    ownership: int = Field(..., ge=0, le=3)
    kein_20m_selling: int = Field(..., ge=0, le=3)  # v3.7: max 3 per SKILL.md Z. 489


class SentimentScore(BaseModel):
    """v3.7 Fix 3: `strong_buy_ratio` ersetzt `konsensus`. Block-Cap 10 Punkte Sub-Max + Delta-Bonus ±2 (SKILL.md §Sentiment)."""

    model_config = ConfigDict(extra="forbid")

    # Block-Cap: 4+3+3 = 10 Sub-Max + eps_revision ±1 + pt_dispersion ±1 = Range -2..+12
    gesamt: int = Field(..., ge=-2, le=12)
    strong_buy_ratio: int = Field(..., ge=0, le=4)
    sell_ratio: int = Field(..., ge=0, le=3)
    pt_upside: int = Field(..., ge=0, le=3)  # v3.7: max 3 per SKILL.md Z. 511
    eps_revision_delta: int = Field(..., ge=-1, le=1)
    pt_dispersion_delta: int = Field(..., ge=-1, le=1)


class Scores(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fundamentals: FundamentalsScore
    moat: MoatScore
    technicals: TechnicalsScore
    insider: InsiderScore
    sentiment: SentimentScore


# ---------------------------------------------------------------------------
# Raw metrics
# ---------------------------------------------------------------------------


class MetrikenRoh(BaseModel):
    """Alle Felder Optional — Backfill-tolerant. Point-in-Time Rohwerte."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    # Fundamentals
    fwd_pe: Optional[float] = None
    p_fcf: Optional[float] = None
    net_debt_ebitda: Optional[float] = None
    current_ratio: Optional[float] = None
    goodwill_pct_assets: Optional[float] = None
    capex_ocf_pct_gaap: Optional[float] = None
    capex_ocf_pct_bereinigt: Optional[float] = None
    capex_bereinigung_art: Optional[str] = None
    roic_gaap_pct: Optional[float] = None
    roic_bereinigt_pct: Optional[float] = None
    roic_bereinigungsgrund: Optional[str] = None
    wacc_pct: Optional[float] = None
    fcf_yield_pct: Optional[float] = None
    sbc_revenue_pct: Optional[float] = None
    sbc_ocf_pct: Optional[float] = None
    accruals_ratio_pct: Optional[float] = None
    tariff_exposure_pct: Optional[float] = None
    gm_trend_3j_pct_p_a: Optional[float] = None
    eps_revisions_up_90d: Optional[int] = None
    eps_revisions_down_90d: Optional[int] = None
    pt_dispersion_pct: Optional[float] = None

    # Spec-Feld (v3.4 Name) — primär
    rel_strength_sp500_6m_pct: Optional[float] = Field(
        default=None,
        alias="rel_strength_sp500_6m_pct",
    )
    # v3.5-Rename-Alias (backwards compatibility)
    rel_staerke_sp500_6m_pct: Optional[float] = None

    # v3.5 neu
    kurs_vs_200ma_pct: Optional[float] = None
    ma200_slope: Optional[Literal["rising", "falling", "flat"]] = None

    # v3.7 neu
    operating_margin_ttm_pct: Optional[float] = None

    @model_validator(mode="after")
    def _sync_rel_staerke_alias(self) -> MetrikenRoh:
        """Wenn nur einer der beiden Rel-Staerke-Namen gesetzt ist, spiegele ihn."""
        if self.rel_strength_sp500_6m_pct is None and self.rel_staerke_sp500_6m_pct is not None:
            object.__setattr__(
                self, "rel_strength_sp500_6m_pct", self.rel_staerke_sp500_6m_pct
            )
        elif self.rel_staerke_sp500_6m_pct is None and self.rel_strength_sp500_6m_pct is not None:
            object.__setattr__(
                self, "rel_staerke_sp500_6m_pct", self.rel_strength_sp500_6m_pct
            )
        return self


# ---------------------------------------------------------------------------
# Top-level: ScoreRecord
# ---------------------------------------------------------------------------


class ScoreRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1.0"]
    record_id: str
    source: Literal["forward", "backfill"]
    ticker: str
    score_datum: date
    analyse_typ: Literal["vollanalyse", "delta", "rescoring"]
    defcon_version: str
    kurs: Kurs
    market_cap: MarketCap
    scores: Scores
    score_gesamt: int
    defcon_level: Literal[1, 2, 3, 4]
    flags: Flags
    metriken_roh: MetrikenRoh
    quellen: Quellen
    notizen: Optional[str] = None

    @field_validator("record_id")
    @classmethod
    def _check_record_id(cls, v: str) -> str:
        if not RECORD_ID_RE.match(v):
            raise ValueError(
                f"record_id '{v}' has invalid format; "
                f"expected YYYY-MM-DD_TICKER_TYP (typ in vollanalyse|delta|rescoring)"
            )
        return v

    @model_validator(mode="after")
    def _check_forward_version(self) -> ScoreRecord:
        """Forward-Records müssen v3.7 deklarieren; Backfill ist frei."""
        if self.source == "forward" and self.defcon_version != "v3.7":
            raise ValueError(
                f"forward record must use defcon_version 'v3.7', got '{self.defcon_version}'"
            )
        return self

    @model_validator(mode="after")
    def _check_arithmetic(self) -> ScoreRecord:
        expected = (
            self.scores.fundamentals.gesamt
            + self.scores.moat.gesamt
            + self.scores.technicals.gesamt
            + self.scores.insider.gesamt
            + self.scores.sentiment.gesamt
        )
        if self.score_gesamt != expected:
            raise ValueError(
                f"score_gesamt arithmetic mismatch: expected {expected}, got {self.score_gesamt}"
            )
        return self

    @model_validator(mode="after")
    def _check_defcon_level(self) -> ScoreRecord:
        """DEFCON-Thresholds ausgerichtet an SKILL.md (Neueinstieg + Bestandsueberwachung):
        >=80 -> D4 | 65-79 -> D3 | 50-64 -> D2 | <50 -> D1.
        Fix 2026-04-18: Vorher 70/60/50 (Schema-Drift gegen SKILL), siehe CORE-MEMORY Section 11.
        """
        s = self.score_gesamt
        if s >= 80:
            expected = 4
        elif s >= 65:
            expected = 3
        elif s >= 50:
            expected = 2
        else:
            expected = 1
        if self.defcon_level != expected:
            raise ValueError(
                f"defcon_level inconsistent with score_gesamt={s}: "
                f"expected level {expected}, got {self.defcon_level}"
            )
        return self

    @model_validator(mode="after")
    def _check_quality_trap(self) -> ScoreRecord:
        """v3.7 Fix 1: Bei moat=wide sind fwd_pe/p_fcf-Scores durch Roh-Multiples gedeckelt.

        - fwd_pe_roh > 30 → fundamentals.fwd_pe MUSS 0 sein
        - fwd_pe_roh in 22..=30 → fundamentals.fwd_pe MUSS <= 1 sein
        - analog p_fcf mit Schwellen 35 / 22..=35
        None-tolerant: fehlende Rohwerte → skip.
        """
        if self.scores.moat.rating != "wide":
            return self

        fwd_pe_roh = self.metriken_roh.fwd_pe
        if fwd_pe_roh is not None:
            if fwd_pe_roh > QT_FWD_PE_HARD and self.scores.fundamentals.fwd_pe != 0:
                raise ValueError(
                    f"quality-trap violation: moat=wide and metriken_roh.fwd_pe={fwd_pe_roh} "
                    f"> {QT_FWD_PE_HARD} requires scores.fundamentals.fwd_pe == 0, "
                    f"got {self.scores.fundamentals.fwd_pe}"
                )
            if (
                QT_FWD_PE_MAX1_LOW <= fwd_pe_roh <= QT_FWD_PE_HARD
                and self.scores.fundamentals.fwd_pe > 1
            ):
                raise ValueError(
                    f"quality-trap violation: moat=wide and metriken_roh.fwd_pe={fwd_pe_roh} "
                    f"in [{QT_FWD_PE_MAX1_LOW}, {QT_FWD_PE_HARD}] requires "
                    f"scores.fundamentals.fwd_pe <= 1, got {self.scores.fundamentals.fwd_pe}"
                )

        p_fcf_roh = self.metriken_roh.p_fcf
        if p_fcf_roh is not None:
            if p_fcf_roh > QT_P_FCF_HARD and self.scores.fundamentals.p_fcf != 0:
                raise ValueError(
                    f"quality-trap violation: moat=wide and metriken_roh.p_fcf={p_fcf_roh} "
                    f"> {QT_P_FCF_HARD} requires scores.fundamentals.p_fcf == 0, "
                    f"got {self.scores.fundamentals.p_fcf}"
                )
            if (
                QT_P_FCF_MAX1_LOW <= p_fcf_roh <= QT_P_FCF_HARD
                and self.scores.fundamentals.p_fcf > 1
            ):
                raise ValueError(
                    f"quality-trap violation: moat=wide and metriken_roh.p_fcf={p_fcf_roh} "
                    f"in [{QT_P_FCF_MAX1_LOW}, {QT_P_FCF_HARD}] requires "
                    f"scores.fundamentals.p_fcf <= 1, got {self.scores.fundamentals.p_fcf}"
                )

        return self


# ---------------------------------------------------------------------------
# FlagEvent
# ---------------------------------------------------------------------------


class FlagMetrik(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    wert: Optional[float] = None
    schwelle: float
    definition: str


class FlagEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1.0"]
    flag_id: str
    source: Literal["forward", "backfill"]
    ticker: str
    flag_typ: Literal["capex_ocf", "fcf_trend_neg", "insider_selling_20m", "tariff_exposure"]
    event_typ: Literal["trigger", "resolution"]
    event_datum: date
    metrik: FlagMetrik
    kurs_bei_event: Kurs
    related_score_record_id: Optional[str] = None
    notizen: Optional[str] = None

    @field_validator("flag_id")
    @classmethod
    def _check_flag_id(cls, v: str) -> str:
        if not FLAG_ID_RE.match(v):
            raise ValueError(
                f"flag_id '{v}' has invalid format; expected TICKER_FLAGTYP_YYYY-MM-DD"
            )
        return v

    @model_validator(mode="after")
    def _check_metrik_direction(self) -> FlagEvent:
        """Trigger verletzt die Schwelle, Resolution hält sie ein. Wert=None → skip (Backfill)."""
        if self.metrik.wert is None:
            return self

        expected_schwelle, direction = FLAG_RULES[self.flag_typ]
        # Hard-coded per spec: Schwellen sind Teil des Modells, nicht Input
        if self.metrik.schwelle != expected_schwelle:
            raise ValueError(
                f"flag_typ '{self.flag_typ}' requires schwelle={expected_schwelle}, "
                f"got {self.metrik.schwelle}"
            )

        wert = self.metrik.wert
        if self.event_typ == "trigger":
            violates = (direction == ">" and wert > expected_schwelle) or (
                direction == "<" and wert < expected_schwelle
            )
            if not violates:
                raise ValueError(
                    f"trigger event for '{self.flag_typ}' must violate threshold "
                    f"(wert {direction} {expected_schwelle}), got wert={wert}"
                )
        else:  # resolution
            holds = (direction == ">" and wert <= expected_schwelle) or (
                direction == "<" and wert >= expected_schwelle
            )
            if not holds:
                raise ValueError(
                    f"resolution event for '{self.flag_typ}' must satisfy threshold "
                    f"(wert not {direction} {expected_schwelle}), got wert={wert}"
                )
        return self


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "FLAG_RULES",
    "FUNDAMENTALS_CAP",
    "FUNDAMENTALS_FLOOR",
    "FlagEvent",
    "FlagMetrik",
    "Flags",
    "FundamentalsScore",
    "InsiderScore",
    "Kurs",
    "MarketCap",
    "MetrikenRoh",
    "MoatScore",
    "Quellen",
    "ScoreRecord",
    "Scores",
    "SentimentScore",
    "TechnicalsScore",
]


# ---------------------------------------------------------------------------
# Smoke tests
# ---------------------------------------------------------------------------


def _smoke_tests() -> None:
    from pydantic import ValidationError

    # Case 1: valid forward record (AVGO-style, adapted to v3.7)
    # Sub-scores: 6+7+8+7+8+6 + 2 (op_margin) - 0 - 0 - 0 = 44 fundamentals
    # 44 + 18 (moat) + 10 (tech) + 9 (insider) + 9 (sentiment) = 90 gesamt, defcon 4
    avgo = {
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
                "gesamt": 44,
                "fwd_pe": 6,
                "p_fcf": 7,
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
            "insider": {
                "gesamt": 10,
                "net_buy_6m": 4,
                "ownership": 3,
                "kein_20m_selling": 3,
            },
            "sentiment": {
                "gesamt": 9,
                "strong_buy_ratio": 4,
                "sell_ratio": 3,
                "pt_upside": 2,
                "eps_revision_delta": 0,
                "pt_dispersion_delta": 0,
            },
        },
        "score_gesamt": 90,
        "defcon_level": 4,
        "flags": {
            "aktiv_ids": [],
            "bei_analyse_referenziert": ["GOOGL_capex_ocf_2025-10-28"],
        },
        "metriken_roh": {
            "fwd_pe": 22.1,
            "p_fcf": 19.8,
            "net_debt_ebitda": 1.4,
            "current_ratio": 1.8,
            "goodwill_pct_assets": 55,
            "capex_ocf_pct_gaap": 12,
            "capex_ocf_pct_bereinigt": None,
            "capex_bereinigung_art": None,
            "roic_gaap_pct": 14.2,
            "roic_bereinigt_pct": 28.5,
            "roic_bereinigungsgrund": "goodwill_ausnahme_ma_5b",
            "wacc_pct": 9.1,
            "fcf_yield_pct": 4.2,
            "sbc_revenue_pct": 8,
            "sbc_ocf_pct": 26,
            "accruals_ratio_pct": 2.1,
            "tariff_exposure_pct": 35,
            "gm_trend_3j_pct_p_a": 0.3,
            "eps_revisions_up_90d": 4,
            "eps_revisions_down_90d": 0,
            "pt_dispersion_pct": 22,
            "rel_strength_sp500_6m_pct": 4,
            "kurs_vs_200ma_pct": 12.5,
            "ma200_slope": "rising",
            "operating_margin_ttm_pct": 32.1,
        },
        "quellen": {
            "fundamentals": "defeatbeta",
            "technicals": "shibui",
            "insider": "openinsider+sec_edgar",
            "moat": "gurufocus",
            "sentiment": "zacks+yahoo",
        },
        "notizen": "Smoke-Test AVGO Forward-Record v3.7",
    }

    # NOTE: fwd_pe_roh=22.1 is within [22, 30], and moat=wide → fwd_pe sub-score must be <=1.
    # AVGO example uses fwd_pe=6 which would violate. Adjust to satisfy QT cap before parsing.
    avgo["scores"]["fundamentals"]["fwd_pe"] = 1
    avgo["scores"]["fundamentals"]["p_fcf"] = 1  # p_fcf 19.8 is below 22, so fine — keep defensive
    # Recompute fundamentals.gesamt and score_gesamt accordingly:
    # 1 + 1 + 8 + 7 + 8 + 6 + 2 - 0 - 0 - 0 = 33
    avgo["scores"]["fundamentals"]["gesamt"] = 33
    # 33 + 18 + 10 + 10 + 9 = 80, defcon 4 (>=80 per SKILL-aligned thresholds)
    avgo["score_gesamt"] = 80
    avgo["defcon_level"] = 4

    rec = ScoreRecord.model_validate(avgo)
    assert rec.ticker == "AVGO"
    assert rec.score_gesamt == 80
    print("  [1/6] valid AVGO forward record parsed; score_gesamt=80, defcon=4")

    # Case 2: arithmetic mismatch
    bad_arith = dict(avgo)
    bad_arith = {**avgo, "score_gesamt": 81}  # off by one
    try:
        ScoreRecord.model_validate(bad_arith)
    except ValidationError as e:
        assert "arithmetic mismatch" in str(e), f"wrong error: {e}"
        print("  [2/6] arithmetic mismatch correctly raised")
    else:
        raise AssertionError("expected arithmetic mismatch ValueError")

    # Case 3: DEFCON inconsistency (score 80 → defcon should be 4, set to 3)
    bad_defcon = {**avgo, "defcon_level": 3}
    try:
        ScoreRecord.model_validate(bad_defcon)
    except ValidationError as e:
        assert "defcon_level inconsistent" in str(e), f"wrong error: {e}"
        print("  [3/6] defcon_level inconsistency correctly raised")
    else:
        raise AssertionError("expected defcon inconsistency ValueError")

    # Case 4: Quality-Trap violation — moat=wide, fwd_pe_roh=35, fundamentals.fwd_pe=4
    # Build from scratch to avoid shared nested-dict mutation.
    import copy
    qt = copy.deepcopy(avgo)
    qt["metriken_roh"]["fwd_pe"] = 35.0  # > 30 → fwd_pe score must be 0
    qt["scores"]["fundamentals"]["fwd_pe"] = 4
    # Recompute for valid arithmetic (otherwise arithmetic validator fires first):
    # 4 + 1 + 8 + 7 + 8 + 6 + 2 = 36
    qt["scores"]["fundamentals"]["gesamt"] = 36
    qt["score_gesamt"] = 36 + 18 + 10 + 10 + 9  # 83 (insider gesamt=10 after SKILL-alignment)
    qt["defcon_level"] = 4
    try:
        ScoreRecord.model_validate(qt)
    except ValidationError as e:
        assert "quality-trap violation" in str(e), f"wrong error: {e}"
        print("  [4/6] quality-trap violation correctly raised")
    else:
        raise AssertionError("expected quality-trap ValueError")

    # Case 5: Valid FLAG trigger event (GOOGL capex_ocf)
    googl_flag = {
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
        "notizen": "FY26 Guidance 74-79% OCF, Q3 Earnings Call CFO-Statement",
    }
    fe = FlagEvent.model_validate(googl_flag)
    assert fe.flag_typ == "capex_ocf"
    print("  [5/6] valid GOOGL capex_ocf trigger parsed")

    # Case 6: Invalid FLAG — trigger but wert < schwelle (wert=54, schwelle=60 means rule HELD, not violated)
    bad_flag = {**googl_flag, "metrik": {**googl_flag["metrik"], "wert": 54}}
    try:
        FlagEvent.model_validate(bad_flag)
    except ValidationError as e:
        assert "trigger event" in str(e) and "violate threshold" in str(e), f"wrong error: {e}"
        print("  [6/6] FLAG trigger direction mismatch correctly raised")
    else:
        raise AssertionError("expected FLAG trigger direction ValueError")

    try:
        print("\u2705 all schema smoke tests passed")
    except UnicodeEncodeError:
        # Windows cp1252 console fallback — ASCII-only.
        print("[OK] all schema smoke tests passed")


if __name__ == "__main__":
    import sys
    # Best-effort: upgrade stdout to UTF-8 so the checkmark renders.
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    _smoke_tests()
