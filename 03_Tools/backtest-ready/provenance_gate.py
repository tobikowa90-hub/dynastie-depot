"""Dynasty-Depot v3.7 Backtest-Ready: provenance_gate (Schicht B).

Pipeline-Gate P3.5 fuer backtest-ready-forward-verify Skill. Fail-close.
Prueft Provenance-Behauptungen (analyse_typ, kurs.referenz, defcon_version,
Quellen-Vollstaendigkeit) gegen Pipeline-Evidenz (freshness_missing,
skill_meta-Konsistenz).

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §5.2

Nicht direkt CLI-aufrufbar — Library-Funktion fuer SKILL.md-Orchestrator.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Final

sys.path.insert(0, str(Path(__file__).parent))

from versions import DEFCON_ACTIVE_VERSION

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PLATZHALTER_BLACKLIST: Final[frozenset[str]] = frozenset({
    "unknown", "tbd", "todo", "placeholder", "none", "na", "n/a", "?",
})

# Source-Tokens single-word: muessen als Whole-Word im Stem vorkommen (split auf "_")
CARRYOVER_SOURCE_TOKENS: Final[frozenset[str]] = frozenset({
    "gurufocus", "defeatbeta", "shibui", "openinsider",
    "yahoo", "zacks", "yfinance", "alphaspread", "tavily",
    "stocktitan", "benzinga", "afm", "amf", "eodhd",
})

# Source-Tokens multi-word: muessen mit "_"-Boundary im Stem stehen
# (Whole-Word-Match ueber stem.split("_") funktioniert nicht, da multi-Tokens
# selbst Underscores enthalten — Codex-Round-3-MEDIUM 28.04.)
CARRYOVER_SOURCE_TOKENS_MULTI: Final[frozenset[str]] = frozenset({
    "sec_edgar",
})

# Source-Prefixes: dynamische Source-Familien (Company-IR-Pages)
CARRYOVER_SOURCE_PREFIXES: Final[tuple[str, ...]] = ("ir_",)

# Reason-Tokens: Workflow-Begruendungen, muessen am Stem-Ende stehen (terminal)
CARRYOVER_REASON_TERMINAL: Final[frozenset[str]] = frozenset({
    "skip_window", "pre_score", "pre_gate", "bridge", "carry_from",
})

QUELLEN_PFLICHT_FELDER: Final[tuple[str, ...]] = (
    "fundamentals", "technicals", "insider", "moat", "sentiment",
)

_RE_QUESTION_MARKS = re.compile(r"\?+")


def _is_placeholder(value: str) -> bool:
    """True wenn value ein Platzhalter ist. Carryover-Whitelist v2 (Codex-Round-1-HIGH).

    Empty-String-Fix v2.1 (Codex-Round-2-HIGH-2 28.04.): Fruehreturn schliesst
    Bypass-Luecke `quellen.{field}=""` an Helper-Semantik (root cause).

    - Empty / Whitespace-only -> True (NEU v2.1).
    - PLATZHALTER_BLACKLIST -> True.
    - Pure `?+` -> True.
    - `*_carryover` -> False (akzeptiert) NUR wenn:
      (a) Stem enthaelt Source-Token Single-Word als Whole-Word (split auf `_`); ODER
      (a-multi) Stem enthaelt Source-Token Multi-Word mit `_`-Boundary; ODER
      (b) Stem startet mit Source-Prefix; ODER
      (c) Stem endet auf Reason-Token (terminal).
    """
    stripped = value.strip().lower()
    if not stripped:
        return True  # NEU v2.1: empty/whitespace-only -> Platzhalter
    if stripped in PLATZHALTER_BLACKLIST:
        return True
    if _RE_QUESTION_MARKS.fullmatch(stripped):
        return True
    if not stripped.endswith("_carryover"):
        return False  # kein Carryover, kein Platzhalter

    stem = stripped[: -len("_carryover")]
    if not stem:
        return True  # bare "_carryover"

    # (a) Source-Token Single-Word als Whole-Word
    stem_tokens = stem.split("_")
    if any(t in CARRYOVER_SOURCE_TOKENS for t in stem_tokens):
        return False

    # (a-multi) Source-Token Multi-Word mit "_"-Boundary
    for multi in CARRYOVER_SOURCE_TOKENS_MULTI:
        if (
            stem == multi
            or stem.startswith(multi + "_")
            or stem.endswith("_" + multi)
            or ("_" + multi + "_") in stem
        ):
            return False

    # (b) Source-Prefix
    if any(stem.startswith(p) for p in CARRYOVER_SOURCE_PREFIXES):
        return False

    # (c) Reason-Token terminal
    for r in CARRYOVER_REASON_TERMINAL:
        if stem == r or stem.endswith("_" + r):
            return False

    return True  # Carryover ohne anerkannten Stamm


def check_provenance(
    record_dict: dict,
    freshness_missing: list[str],
    skill_meta: dict | None,
) -> tuple[bool, list[str]]:
    """Pipeline-Gate P3.5. Fail-close bei erster Verletzung.

    Args:
        record_dict: ScoreRecord als dict (vor Pydantic-Validation).
        freshness_missing: Liste der nicht-modifizierten REQUIRED_TOUCH_FILES
            aus check_freshness() in P2a (PORTFOLIO.md / Faktortabelle.md / log.md).
        skill_meta: optional dict mit migration-Info; None oder {} = leer.

    Returns:
        (passed, reasons). passed=False -> Caller muss FAIL phase=P3.5 emitten
        und Pipeline abbrechen. reasons enthaelt genau eine Begruendung
        (fail-close: Stop bei erster Verletzung).
    """
    source = record_dict.get("source")
    analyse_typ = record_dict.get("analyse_typ")
    skill_meta_norm = skill_meta or {}

    # Check #1: Backfill skip
    if source == "backfill":
        return True, []

    # Check #2: vollanalyse braucht frische Pflicht-Touch-Dateien
    if analyse_typ == "vollanalyse" and freshness_missing:
        return False, [
            f"vollanalyse requires fresh session (missing: {freshness_missing}); "
            f"reclassify as rescoring or complete workflow"
        ]

    # Check #3: vollanalyse braucht frischen Kurs (referenz=close_of_score_datum)
    if analyse_typ == "vollanalyse":
        kurs_referenz = (record_dict.get("kurs") or {}).get("referenz")
        if kurs_referenz != "close_of_score_datum":
            return False, [
                f"vollanalyse requires fresh kurs (referenz='{kurs_referenz}')"
            ]

    # Check #4: rescoring braucht skill_meta fuer Δ-Gate
    if analyse_typ == "rescoring" and not skill_meta_norm:
        return False, ["rescoring requires skill_meta for Δ-Gate"]

    # Check #5: delta ist forward-only
    if analyse_typ == "delta" and source != "forward":
        return False, ["delta is forward-only"]

    # Check #6: defcon_version-Drift gegen aktive Version
    record_version = record_dict.get("defcon_version")
    if record_version != DEFCON_ACTIVE_VERSION:
        return False, [
            f"defcon_version '{record_version}' drift vs. active '{DEFCON_ACTIVE_VERSION}'"
        ]

    # Check #7: Platzhalter in den 5 Pflicht-quellen-Feldern (mit Carryover-Whitelist)
    quellen = record_dict.get("quellen") or {}
    for field in QUELLEN_PFLICHT_FELDER:
        value = quellen.get(field, "")
        if not isinstance(value, str) or _is_placeholder(value):
            return False, [
                f"placeholder source '{value}' in quellen.{field}"
            ]

    # Check #8: skill_meta.migration_to_version inconsistent mit record.defcon_version
    if skill_meta_norm:
        meta_to_version = skill_meta_norm.get("migration_to_version")
        if meta_to_version is not None and meta_to_version != record_version:
            return False, [
                f"skill_meta.migration_to_version='{meta_to_version}' "
                f"inconsistent with record.defcon_version='{record_version}' "
                f"(recycled skill_meta)"
            ]

    return True, []


__all__ = [
    "CARRYOVER_REASON_TERMINAL",
    "CARRYOVER_SOURCE_PREFIXES",
    "CARRYOVER_SOURCE_TOKENS",
    "CARRYOVER_SOURCE_TOKENS_MULTI",
    "DEFCON_ACTIVE_VERSION",
    "PLATZHALTER_BLACKLIST",
    "QUELLEN_PFLICHT_FELDER",
    "check_provenance",
]


# ---------------------------------------------------------------------------
# Smoke tests
# ---------------------------------------------------------------------------


def _build_valid_vollanalyse() -> dict:
    """Minimal-valid vollanalyse-Record fuer Provenance-Gate-Tests.
    Enthaelt explizit alle Felder, die die 8 Checks lesen."""
    return {
        "source": "forward",
        "analyse_typ": "vollanalyse",
        "defcon_version": DEFCON_ACTIVE_VERSION,
        "kurs": {
            "wert": 100.0,
            "waehrung": "USD",
            "referenz": "close_of_score_datum",
            "quelle": "yahoo_eod",
        },
        "quellen": {
            "fundamentals": "defeatbeta",
            "technicals": "shibui",
            "insider": "openinsider+sec_edgar",
            "moat": "gurufocus",
            "sentiment": "zacks+yahoo",
        },
    }


def _smoke_tests() -> None:
    # Case 1: Valid vollanalyse, freshness_missing=[], fresh kurs -> pass
    rec = _build_valid_vollanalyse()
    passed, reasons = check_provenance(rec, [], None)
    assert passed and reasons == [], f"[1] expected pass, got {passed} {reasons}"
    print("  [1/9] valid vollanalyse + fresh session -> pass")

    # Case 2: vollanalyse + freshness_missing=["PORTFOLIO.md"] -> fail
    rec = _build_valid_vollanalyse()
    passed, reasons = check_provenance(rec, ["PORTFOLIO.md"], None)
    assert not passed, "[2] expected fail"
    assert "vollanalyse requires fresh session" in reasons[0], f"[2] {reasons}"
    assert "PORTFOLIO.md" in reasons[0], f"[2] PORTFOLIO.md not in reason: {reasons}"
    print("  [2/9] vollanalyse + missing PORTFOLIO.md -> fail")

    # Case 3: vollanalyse + kurs.referenz='close_2026-04-15' (stale) -> fail
    rec = _build_valid_vollanalyse()
    rec["kurs"]["referenz"] = "close_2026-04-15"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[3] expected fail"
    assert "vollanalyse requires fresh kurs" in reasons[0], f"[3] {reasons}"
    print("  [3/9] vollanalyse + stale kurs.referenz -> fail")

    # Case 4: rescoring ohne skill_meta -> fail
    rec = _build_valid_vollanalyse()
    rec["analyse_typ"] = "rescoring"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[4] expected fail"
    assert "rescoring requires skill_meta" in reasons[0], f"[4] {reasons}"
    print("  [4/9] rescoring ohne skill_meta -> fail")

    # Case 5: delta + source!='forward' -> fail
    rec = _build_valid_vollanalyse()
    rec["analyse_typ"] = "delta"
    rec["source"] = "forward"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[5a] forward-delta should pass, got {reasons}"
    rec["source"] = "manual"  # hypothetical 3rd source value
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[5b] expected fail for delta+source!=forward"
    assert "delta is forward-only" in reasons[0], f"[5b] {reasons}"
    print("  [5/9] delta + source!='forward' -> fail")

    # Case 6: Backfill-Record -> pass (skip in Check #1)
    rec = _build_valid_vollanalyse()
    rec["source"] = "backfill"
    rec["analyse_typ"] = "vollanalyse"
    passed, reasons = check_provenance(rec, ["PORTFOLIO.md", "log.md"], None)
    assert passed and reasons == [], f"[6] backfill should skip, got {passed} {reasons}"
    print("  [6/9] backfill skipped -> pass")

    # Case 7: defcon_version='v3.5' aber active='v3.7' -> fail
    rec = _build_valid_vollanalyse()
    rec["defcon_version"] = "v3.5"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[7] expected fail"
    assert "drift vs. active" in reasons[0] and "v3.5" in reasons[0], f"[7] {reasons}"
    print("  [7/9] defcon_version drift -> fail")

    # Case 8: Platzhalter-Tests inkl. Carryover-Whitelist (Codex-HIGH-Hardening)
    # 8a: 'unknown' -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["insider"] = "unknown"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8a] expected fail"
    assert "placeholder source" in reasons[0] and "insider" in reasons[0], f"[8a] {reasons}"

    # 8b: Variants TBD/?/N/A/PLACEHOLDER -> all fail
    for placeholder in ("TBD", "?", "  N/A  ", "PLACEHOLDER"):
        rec_v = _build_valid_vollanalyse()
        rec_v["quellen"]["fundamentals"] = placeholder
        passed_v, reasons_v = check_provenance(rec_v, [], None)
        assert not passed_v, f"[8b:{placeholder!r}] expected fail"

    # 8c: 'gurufocus_carryover' (legitimer Source-Token whole-word) -> pass
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "gurufocus_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[8c] gurufocus_carryover should pass, got {reasons}"

    # 8d: 'xyzzy_carryover' (kein anerkannter Stamm) -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "xyzzy_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8d] xyzzy_carryover should fail"
    assert "placeholder source" in reasons[0], f"[8d] {reasons}"

    # 8e: 'skip_window_delta_lt_14d_pre_score_carryover' (Reason terminal) -> pass
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "skip_window_delta_lt_14d_pre_score_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[8e] reason-terminal carryover should pass, got {reasons}"

    # 8f: 'pre_gate_xyzzy_carryover' (Reason NICHT terminal — Codex-HIGH-Bypass-Test) -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "pre_gate_xyzzy_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8f] reason-not-terminal carryover should FAIL (Codex-HIGH bypass)"

    # 8g: 'bridge_carryover' (Reason als kompletter Stem) -> pass
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "bridge_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[8g] bridge_carryover should pass, got {reasons}"

    # 8h: 'ir_apple_carryover' (Source-Prefix) -> pass
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "ir_apple_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[8h] ir_-prefix carryover should pass, got {reasons}"

    # 8i: 'gurufocusxyz_carryover' (kein Whole-Word-Match) -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "gurufocusxyz_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8i] gurufocusxyz_carryover should fail (no whole-word match)"

    # 8j: '' (empty string — Codex-Round-2-HIGH-2 Bypass-Test v2.1) -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = ""
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8j] empty string should fail (Codex-HIGH-2 bypass)"
    assert "placeholder source" in reasons[0], f"[8j] {reasons}"

    # 8k: '   ' (whitespace-only — empty after strip, v2.1) -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["fundamentals"] = "   "
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8k] whitespace-only should fail (empty after strip)"

    # 8l: 'sec_edgar_carryover' (Multi-Word-Source-Token, Codex-Round-3-MEDIUM) -> pass
    rec = _build_valid_vollanalyse()
    rec["quellen"]["insider"] = "sec_edgar_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[8l] sec_edgar_carryover should pass (multi-word whole), got {reasons}"

    # 8m: 'sec_edgarxyz_carryover' (Multi-Word ohne Boundary) -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["insider"] = "sec_edgarxyz_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8m] sec_edgarxyz_carryover should fail (no _-boundary)"

    # 8n: 'myir_sec_edgar_carryover' (Multi-Word terminal mit Boundary) -> pass
    rec = _build_valid_vollanalyse()
    rec["quellen"]["insider"] = "myir_sec_edgar_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[8n] myir_sec_edgar_carryover should pass (terminal multi), got {reasons}"

    # 8o: 'sec_carryover' (partial multi-Token, kein single match) -> fail
    rec = _build_valid_vollanalyse()
    rec["quellen"]["insider"] = "sec_carryover"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8o] sec_carryover should fail (partial multi, no single match)"

    print("  [8/9] placeholder + carryover whitelist (8a-8o) -> all checks pass")

    # Case 9: skill_meta.migration_to_version inconsistent -> fail
    rec = _build_valid_vollanalyse()
    bad_meta = {
        "expected_algebra_score": 63,
        "migration_from_version": "v3.5",
        "migration_to_version": "v3.6",  # mismatch vs record=v3.7
    }
    passed, reasons = check_provenance(rec, [], bad_meta)
    assert not passed, "[9] expected fail"
    assert "skill_meta.migration_to_version" in reasons[0], f"[9] {reasons}"
    assert "recycled skill_meta" in reasons[0], f"[9] {reasons}"
    print("  [9/9] recycled skill_meta (migration_to_version inconsistent) -> fail")

    print("[OK] all provenance_gate smoke tests passed (9/9)")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    _smoke_tests()
