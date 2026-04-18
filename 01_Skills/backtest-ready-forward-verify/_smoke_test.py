"""Smoke tests for backtest-ready-forward-verify helpers.

Tests ONLY the Python helpers in _forward_verify_helpers.py and their interaction
with archive_score.py --dry-run.  Skill prosa (SKILL.md) is NOT tested here —
that is a qualitative end-to-end judgment (Task 6).

Run:
    python 01_Skills/backtest-ready-forward-verify/_smoke_test.py

Expected (before helpers exist): 6/6 FAIL (ImportError on _forward_verify_helpers)
Expected (after helpers): 6/6 PASS
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# sys.path: add 03_Tools/backtest-ready so helpers + schemas are importable
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = REPO_ROOT / "03_Tools" / "backtest-ready"
sys.path.insert(0, str(TOOLS_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

# ---------------------------------------------------------------------------
# STATE.md fixture string — covers all style variants that parse_state_row
# must handle in production.
# ---------------------------------------------------------------------------
STATE_MD_FIXTURE = """\
# STATE.md — Dynasty-Depot Live-Status
**Stand: 18.04.2026**

---

## Portfolio-State (11 Satelliten)

| Ticker | Score | DEFCON | Rate | FLAG | Nächster Trigger |
|--------|-------|--------|------|------|------------------|
| AVGO | 84 | 🟢 4 | 35,63€ | ⚠️ Insider-Review (OpenInsider!) | Q3 FY26 |
| BRK.B | 75 | 🟡 3 | 35,63€ | ✅ Insurance Exception | Q-Earnings Mai |
| VEEV | 74 | 🟡 3 | 35,63€ | ✅ | Earnings-Trigger |
| SU | 69 | 🟡 3 | 35,63€ | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | 35,63€ | ✅ Screener-Exception | Q1 FY27 ~Dez |
| V | **63** | **🟠 2** | **17,81€** | ✅ | **28.04. Q2 FY26 — D2-Entscheidung** |
| TMO | **64** | 🟠 2 | 17,81€ | ✅ (fcf_trend_neg schema-trigger, WC-Noise → **nicht aktiviert**) | **23.04. Q1 — FLAG-Resolve-Gate** |
| APH | 63 | 🟠 2 | **0€** | 🔴 Score-basiert | 23.07. Q2 |
| MSFT | 59 | 🟠 2 | **0€** | 🔴 CapEx/OCF 83.6% | **29.04. Q3 FY26 — FLAG-Review** |
"""

# ---------------------------------------------------------------------------
# Helper: build a minimal-valid ScoreRecord dict for a given ticker/date
# Uses moat.rating="narrow" to sidestep Quality-Trap caps — gives full score freedom.
# ---------------------------------------------------------------------------
def _build_minimal_record(
    ticker: str,
    score_datum_iso: str,
    score_gesamt: int,
    defcon_level: int,
    flags_aktiv_ids: list | None = None,
) -> dict:
    """Build a valid ScoreRecord dict.

    score_gesamt must be consistent with defcon_level (schema validates):
      >=80 → D4 | 65-79 → D3 | 50-64 → D2 | <50 → D1

    Sub-score strategy: put everything into moat.gesamt to hit score_gesamt.
      fundamentals: gesamt=0 (all zeros, sbc_malus/accruals_malus/tariff_malus = 0)
      moat: gesamt = score_gesamt - (tech + insider + sentiment)
      tech: gesamt=0, insider: gesamt=0, sentiment: gesamt=0
    That keeps arithmetic simple for any target total (0..20 range of moat).
    For scores needing more than 20, distribute across blocks.
    """
    if flags_aktiv_ids is None:
        flags_aktiv_ids = []

    # Distribute sub-scores:
    # fund=0, tech=0, insider=0, sentiment=0 → moat must carry everything.
    # moat.gesamt range: 0..20 — for higher totals we add to insider/sentiment/tech.
    remaining = score_gesamt
    moat_g = min(remaining, 20)
    remaining -= moat_g
    insider_g = min(remaining, 10)
    remaining -= insider_g
    tech_g = min(remaining, 10)
    remaining -= tech_g
    sentiment_g = min(remaining, 9)  # sentiment max -2..12; keep simple ≤9
    remaining -= sentiment_g
    fund_g = remaining  # fundamentals carries the rest (capped at 50)

    record_id = f"{score_datum_iso}_{ticker}_vollanalyse"
    return {
        "schema_version": "1.0",
        "record_id": record_id,
        "source": "backfill",  # avoid forward-window date constraint
        "ticker": ticker,
        "score_datum": score_datum_iso,
        "analyse_typ": "vollanalyse",
        "defcon_version": "historical",  # backfill allows any version string
        "kurs": {
            "wert": 100.0,
            "waehrung": "USD",
            "referenz": "backfill_not_available",
            "quelle": "backfill",
        },
        "market_cap": {"wert": 1.0e9, "waehrung": "USD"},
        "scores": {
            "fundamentals": {
                "gesamt": fund_g,
                "fwd_pe": fund_g,  # lump into one sub-score; no QT (moat=narrow)
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
                "gesamt": moat_g,
                "rating": "narrow",  # sidestep QT validator
                "quellen": [],
                "gm_trend_delta": 0,
                "pricing_power_bonus": 0,
            },
            "technicals": {
                "gesamt": tech_g,
                "ath_distanz": min(tech_g, 4),
                "rel_staerke": min(max(tech_g - 4, 0), 3),
                "trend_lage": min(max(tech_g - 7, 0), 3),
                "dcf_relation_delta": 0,
            },
            "insider": {
                "gesamt": insider_g,
                "net_buy_6m": min(insider_g, 4),
                "ownership": min(max(insider_g - 4, 0), 3),
                "kein_20m_selling": min(max(insider_g - 7, 0), 3),
            },
            "sentiment": {
                "gesamt": sentiment_g,
                "strong_buy_ratio": min(sentiment_g, 4),
                "sell_ratio": min(max(sentiment_g - 4, 0), 3),
                "pt_upside": min(max(sentiment_g - 7, 0), 3),
                "eps_revision_delta": 0,
                "pt_dispersion_delta": 0,
            },
        },
        "score_gesamt": score_gesamt,
        "defcon_level": defcon_level,
        "flags": {
            "aktiv_ids": flags_aktiv_ids,
            "bei_analyse_referenziert": [],
        },
        "metriken_roh": {},
        "quellen": {
            "fundamentals": "backfill_not_available",
            "technicals": "backfill_not_available",
            "insider": "backfill_not_available",
            "moat": "backfill_not_available",
            "sentiment": "backfill_not_available",
        },
        "notizen": "smoke_test fixture",
    }


# ---------------------------------------------------------------------------
# Import helpers (expected to fail until Step 3.4)
# ---------------------------------------------------------------------------
try:
    from _forward_verify_helpers import (
        build_migration_event,
        check_freshness,
        parse_state_row,
        parse_wrapper,
    )
    HELPERS_AVAILABLE = True
except ImportError as _imp_err:
    HELPERS_AVAILABLE = False
    _IMPORT_ERROR = _imp_err


def _require_helpers() -> None:
    if not HELPERS_AVAILABLE:
        raise ImportError(f"_forward_verify_helpers not found: {_IMPORT_ERROR}")


# ---------------------------------------------------------------------------
# Case 1: parse_wrapper basic + archive_score.py --dry-run
# ---------------------------------------------------------------------------
def case_1() -> None:
    """Wrapper-Parse-Helper basic: hand-built draft dict → dry-run exit 0."""
    _require_helpers()

    # Use a ticker unlikely to collide with existing archive records.
    # score_datum = today's date to satisfy forward-window — but we use
    # source=backfill so the date window check is skipped entirely.
    ticker = "ZTS"
    score_datum = "2026-03-01"  # fixed past date — safe as backfill
    record = _build_minimal_record(ticker, score_datum, score_gesamt=65, defcon_level=3)
    draft = {"record": record, "skill_meta": {}}

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tf:
        json.dump(draft, tf)
        tmpfile = tf.name

    # parse_wrapper should return (record_dict, {})
    rec_dict, skill_meta = parse_wrapper(tmpfile)
    assert skill_meta == {}, f"expected empty skill_meta, got {skill_meta!r}"
    assert rec_dict["ticker"] == ticker, f"ticker mismatch: {rec_dict.get('ticker')!r}"

    # Write record to tempfile for archive_score dry-run
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tf2:
        json.dump(rec_dict, tf2)
        rec_tmpfile = tf2.name

    archive_score_path = str(TOOLS_DIR / "archive_score.py")
    result = subprocess.run(
        [sys.executable, archive_score_path, "--file", rec_tmpfile, "--dry-run"],
        capture_output=True,
        encoding="utf-8",
        cwd=str(TOOLS_DIR),
    )
    assert result.returncode == 0, (
        f"archive_score.py --dry-run returned {result.returncode}\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


# ---------------------------------------------------------------------------
# Case 2: Wrapper + MigrationEvent injection — accepted (|Δ|=1)
# ---------------------------------------------------------------------------
def case_2() -> None:
    """Draft + skill_meta(algebra=63) → forward=64 → outcome=accepted, delta=1.0."""
    _require_helpers()

    ticker = "ZTS"
    score_datum = "2026-03-02"
    record = _build_minimal_record(ticker, score_datum, score_gesamt=64, defcon_level=2)
    skill_meta = {
        "expected_algebra_score": 63,
        "migration_from_version": "v3.5",
        "migration_to_version": "v3.7",
    }

    event, signal = build_migration_event(skill_meta, forward_score=64)
    assert event.outcome == "accepted", f"expected accepted, got {event.outcome!r}"
    assert event.delta == 1.0, f"expected delta=1.0, got {event.delta}"
    assert signal == "", f"expected empty signal for accepted, got {signal!r}"

    # Inject into record and dry-run validate
    record["migration_event"] = event.model_dump()

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tf:
        json.dump(record, tf)
        tmpfile = tf.name

    archive_score_path = str(TOOLS_DIR / "archive_score.py")
    result = subprocess.run(
        [sys.executable, archive_score_path, "--file", tmpfile, "--dry-run"],
        capture_output=True,
        encoding="utf-8",
        cwd=str(TOOLS_DIR),
    )
    assert result.returncode == 0, (
        f"dry-run failed: rc={result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}"
    )


# ---------------------------------------------------------------------------
# Case 3: Outcome log_only grenzfall (|Δ|=4)
# ---------------------------------------------------------------------------
def case_3() -> None:
    """algebra=63, forward=67 → outcome=log_only, delta=4.0. Dry-run green."""
    _require_helpers()

    ticker = "ZTS"
    score_datum = "2026-03-03"
    record = _build_minimal_record(ticker, score_datum, score_gesamt=67, defcon_level=3)
    skill_meta = {
        "expected_algebra_score": 63,
        "migration_from_version": "v3.5",
        "migration_to_version": "v3.7",
    }

    event, signal = build_migration_event(skill_meta, forward_score=67)
    assert event.outcome == "log_only", f"expected log_only, got {event.outcome!r}"
    assert event.delta == 4.0, f"expected delta=4.0, got {event.delta}"
    assert "PFLICHT" in signal, f"expected PFLICHT signal for log_only, got {signal!r}"

    record["migration_event"] = event.model_dump()

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tf:
        json.dump(record, tf)
        tmpfile = tf.name

    archive_score_path = str(TOOLS_DIR / "archive_score.py")
    result = subprocess.run(
        [sys.executable, archive_score_path, "--file", tmpfile, "--dry-run"],
        capture_output=True,
        encoding="utf-8",
        cwd=str(TOOLS_DIR),
    )
    assert result.returncode == 0, (
        f"dry-run failed: rc={result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}"
    )


# ---------------------------------------------------------------------------
# Case 4: Outcome block (|Δ|=23)
# ---------------------------------------------------------------------------
def case_4() -> None:
    """algebra=86, forward=63 → outcome=block, delta=-23. STOP signal present.
    Dry-run still green (archive accepts; block is fan-out signal only).
    """
    _require_helpers()

    ticker = "ZTS"
    score_datum = "2026-03-04"
    record = _build_minimal_record(ticker, score_datum, score_gesamt=63, defcon_level=2)
    skill_meta = {
        "expected_algebra_score": 86,
        "migration_from_version": "v3.5",
        "migration_to_version": "v3.7",
    }

    event, signal = build_migration_event(skill_meta, forward_score=63)
    assert event.outcome == "block", f"expected block, got {event.outcome!r}"
    assert event.delta == -23.0, f"expected delta=-23.0, got {event.delta}"
    assert signal.startswith("STOP:"), f"expected STOP: signal for block, got {signal!r}"

    record["migration_event"] = event.model_dump()

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tf:
        json.dump(record, tf)
        tmpfile = tf.name

    archive_score_path = str(TOOLS_DIR / "archive_score.py")
    result = subprocess.run(
        [sys.executable, archive_score_path, "--file", tmpfile, "--dry-run"],
        capture_output=True,
        encoding="utf-8",
        cwd=str(TOOLS_DIR),
    )
    assert result.returncode == 0, (
        f"dry-run failed: rc={result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}"
    )


# ---------------------------------------------------------------------------
# Case 5: parse_state_row — all style variants
# ---------------------------------------------------------------------------
def case_5() -> None:
    """parse_state_row extracts correct {score, defcon, flags_active} for all variants."""
    _require_helpers()

    # AVGO: score=84, defcon=4, ⚠️ = watch (not hard flag) → flags_active=False
    avgo = parse_state_row("AVGO", STATE_MD_FIXTURE)
    assert avgo == {"score": 84, "defcon": 4, "flags_active": False}, (
        f"AVGO mismatch: {avgo}"
    )

    # V: bold-wrap **63** / **🟠 2** / ✅ → flags_active=False
    v = parse_state_row("V", STATE_MD_FIXTURE)
    assert v == {"score": 63, "defcon": 2, "flags_active": False}, f"V mismatch: {v}"

    # APH: 🔴 → flags_active=True
    aph = parse_state_row("APH", STATE_MD_FIXTURE)
    assert aph == {"score": 63, "defcon": 2, "flags_active": True}, f"APH mismatch: {aph}"

    # MSFT: 🔴 → flags_active=True
    msft = parse_state_row("MSFT", STATE_MD_FIXTURE)
    assert msft == {"score": 59, "defcon": 2, "flags_active": True}, f"MSFT mismatch: {msft}"

    # TMO: **64** / 🟠 2 / ✅ (...) → flags_active=False
    tmo = parse_state_row("TMO", STATE_MD_FIXTURE)
    assert tmo == {"score": 64, "defcon": 2, "flags_active": False}, f"TMO mismatch: {tmo}"

    # BRK.B: ticker with dot
    brkb = parse_state_row("BRK.B", STATE_MD_FIXTURE)
    assert brkb == {"score": 75, "defcon": 3, "flags_active": False}, f"BRK.B mismatch: {brkb}"

    # UNKNOWN → ValueError
    try:
        parse_state_row("UNKNOWN", STATE_MD_FIXTURE)
        raise AssertionError("expected ValueError for unknown ticker")
    except (ValueError, KeyError) as exc:
        assert "UNKNOWN" in str(exc), f"error message should mention ticker, got: {exc}"


# ---------------------------------------------------------------------------
# Case 6: check_freshness — git status based detection
# ---------------------------------------------------------------------------
def case_6() -> None:
    """check_freshness detects which of 3 required files are not modified."""
    _require_helpers()

    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create the required directories
        core_dir = tmppath / "00_Core"
        core_dir.mkdir()

        # Create the required files
        state_md = core_dir / "STATE.md"
        faktor_md = core_dir / "Faktortabelle.md"
        log_md = core_dir / "log.md"
        core_memory_md = core_dir / "CORE-MEMORY.md"
        config_yaml = tmppath / "config.yaml"

        for f in [state_md, faktor_md, log_md, core_memory_md, config_yaml]:
            f.write_text("initial content\n", encoding="utf-8")

        # Init git repo and make initial commit
        subprocess.run(["git", "init", "-b", "main"], cwd=tmpdir, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=tmpdir, capture_output=True)
        subprocess.run(
            ["git", "-c", "user.email=t@t.t", "-c", "user.name=t",
             "commit", "-m", "initial"],
            cwd=tmpdir,
            capture_output=True,
        )

        # Sub-case A: all 3 required files modified → returns []
        state_md.write_text("modified\n", encoding="utf-8")
        faktor_md.write_text("modified\n", encoding="utf-8")
        log_md.write_text("modified\n", encoding="utf-8")
        result_a = check_freshness(repo_root=tmpdir)
        assert result_a == [], f"Sub-case A: expected [], got {result_a}"

        # Reset files (git checkout)
        subprocess.run(
            ["git", "checkout", "--", "00_Core/STATE.md", "00_Core/Faktortabelle.md", "00_Core/log.md"],
            cwd=tmpdir,
            capture_output=True,
        )

        # Sub-case B: only STATE + Faktor modified, log untouched → returns ["log.md"]
        state_md.write_text("modified\n", encoding="utf-8")
        faktor_md.write_text("modified\n", encoding="utf-8")
        result_b = check_freshness(repo_root=tmpdir)
        assert result_b == ["log.md"], f"Sub-case B: expected ['log.md'], got {result_b}"

        # Reset
        subprocess.run(
            ["git", "checkout", "--", "00_Core/STATE.md", "00_Core/Faktortabelle.md"],
            cwd=tmpdir,
            capture_output=True,
        )

        # Sub-case C: none modified → returns all three required files
        result_c = check_freshness(repo_root=tmpdir)
        assert sorted(result_c) == sorted(["STATE.md", "Faktortabelle.md", "log.md"]), (
            f"Sub-case C: expected all 3 required, got {result_c}"
        )

        # Sub-case D: modify conditional files (CORE-MEMORY + config.yaml) only
        # → they must NOT appear in check_freshness return
        core_memory_md.write_text("changed\n", encoding="utf-8")
        config_yaml.write_text("changed\n", encoding="utf-8")
        result_d = check_freshness(repo_root=tmpdir)
        # Still missing all 3 required (the conditional files are tracked but not checked)
        assert sorted(result_d) == sorted(["STATE.md", "Faktortabelle.md", "log.md"]), (
            f"Sub-case D: conditional files must be ignored, got {result_d}"
        )
        # Verify CORE-MEMORY and config are NOT in the result
        assert "CORE-MEMORY.md" not in result_d, "CORE-MEMORY.md must not appear in freshness result"
        assert "config.yaml" not in result_d, "config.yaml must not appear in freshness result"


# ---------------------------------------------------------------------------
# Harness
# ---------------------------------------------------------------------------
CASES = [
    (1, "Wrapper-Parse-Helper basic", case_1),
    (2, "MigrationEvent injection — accepted (delta=1)", case_2),
    (3, "MigrationEvent log_only grenzfall (delta=4)", case_3),
    (4, "MigrationEvent block (delta=-23) + STOP signal", case_4),
    (5, "parse_state_row — all style variants", case_5),
    (6, "check_freshness — git status detection", case_6),
]


def run_all() -> None:
    passed = 0
    failed = 0
    for n, label, fn in CASES:
        try:
            fn()
            print(f"[{n}/6] PASS: {label}")
            passed += 1
        except Exception as exc:
            print(f"[{n}/6] FAIL: {label} — {type(exc).__name__}: {exc}")
            failed += 1

    print()
    if failed == 0:
        print(f"✅ all {passed}/6 cases passed")
    else:
        print(f"❌ {failed} case(s) failed, {passed}/{len(CASES)} passed")
        sys.exit(1)


if __name__ == "__main__":
    run_all()
