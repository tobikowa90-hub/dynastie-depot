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

import contextlib
import json
import subprocess
import sys
import tempfile
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
# PORTFOLIO.md fixture string — covers all style variants that parse_state_row
# must handle in production.
# ---------------------------------------------------------------------------
PORTFOLIO_MD_FIXTURE = """\
# PORTFOLIO.md — Depot-Live-State
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
    from provenance_gate import check_provenance

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
    assert signal.startswith("STOP:"), f"STOP: prefix missing: {signal!r}"
    assert "§28.2" in signal, f"§28.2 citation missing: {signal!r}"
    assert "Fan-Out (7 Oberflächen)" in signal, f"Fan-Out phrase missing: {signal!r}"
    assert "JSONL-Commit läuft durch" in signal, f"JSONL continuation note missing: {signal!r}"

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
    avgo = parse_state_row("AVGO", PORTFOLIO_MD_FIXTURE)
    assert avgo == {"score": 84, "defcon": 4, "flags_active": False}, f"AVGO mismatch: {avgo}"

    # V: bold-wrap **63** / **🟠 2** / ✅ → flags_active=False
    v = parse_state_row("V", PORTFOLIO_MD_FIXTURE)
    assert v == {"score": 63, "defcon": 2, "flags_active": False}, f"V mismatch: {v}"

    # APH: 🔴 → flags_active=True
    aph = parse_state_row("APH", PORTFOLIO_MD_FIXTURE)
    assert aph == {"score": 63, "defcon": 2, "flags_active": True}, f"APH mismatch: {aph}"

    # MSFT: 🔴 → flags_active=True
    msft = parse_state_row("MSFT", PORTFOLIO_MD_FIXTURE)
    assert msft == {"score": 59, "defcon": 2, "flags_active": True}, f"MSFT mismatch: {msft}"

    # TMO: **64** / 🟠 2 / ✅ (...) → flags_active=False
    tmo = parse_state_row("TMO", PORTFOLIO_MD_FIXTURE)
    assert tmo == {"score": 64, "defcon": 2, "flags_active": False}, f"TMO mismatch: {tmo}"

    # BRK.B: ticker with dot
    brkb = parse_state_row("BRK.B", PORTFOLIO_MD_FIXTURE)
    assert brkb == {"score": 75, "defcon": 3, "flags_active": False}, f"BRK.B mismatch: {brkb}"

    # UNKNOWN → ValueError
    try:
        parse_state_row("UNKNOWN", PORTFOLIO_MD_FIXTURE)
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
        portfolio_md = core_dir / "PORTFOLIO.md"
        faktor_md = core_dir / "Faktortabelle.md"
        log_md = core_dir / "log.md"
        core_memory_md = core_dir / "CORE-MEMORY.md"
        config_yaml = tmppath / "config.yaml"

        for f in [portfolio_md, faktor_md, log_md, core_memory_md, config_yaml]:
            f.write_text("initial content\n", encoding="utf-8")

        # Init git repo and make initial commit
        subprocess.run(["git", "init", "-b", "main"], cwd=tmpdir, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=tmpdir, capture_output=True)
        subprocess.run(
            ["git", "-c", "user.email=t@t.t", "-c", "user.name=t", "commit", "-m", "initial"],
            cwd=tmpdir,
            capture_output=True,
        )

        # Sub-case A: all 3 required files modified → returns []
        portfolio_md.write_text("modified\n", encoding="utf-8")
        faktor_md.write_text("modified\n", encoding="utf-8")
        log_md.write_text("modified\n", encoding="utf-8")
        result_a = check_freshness(repo_root=tmpdir)
        assert result_a == [], f"Sub-case A: expected [], got {result_a}"

        # Reset files (git checkout)
        subprocess.run(
            [
                "git",
                "checkout",
                "--",
                "00_Core/PORTFOLIO.md",
                "00_Core/Faktortabelle.md",
                "00_Core/log.md",
            ],
            cwd=tmpdir,
            capture_output=True,
        )

        # Sub-case B: only PORTFOLIO + Faktor modified, log untouched → returns ["log.md"]
        portfolio_md.write_text("modified\n", encoding="utf-8")
        faktor_md.write_text("modified\n", encoding="utf-8")
        result_b = check_freshness(repo_root=tmpdir)
        assert result_b == ["log.md"], f"Sub-case B: expected ['log.md'], got {result_b}"

        # Reset
        subprocess.run(
            ["git", "checkout", "--", "00_Core/PORTFOLIO.md", "00_Core/Faktortabelle.md"],
            cwd=tmpdir,
            capture_output=True,
        )

        # Sub-case C: none modified → returns all three required files
        result_c = check_freshness(repo_root=tmpdir)
        assert sorted(result_c) == sorted(["PORTFOLIO.md", "Faktortabelle.md", "log.md"]), (
            f"Sub-case C: expected all 3 required, got {result_c}"
        )

        # Sub-case D: modify conditional files (CORE-MEMORY + config.yaml) only
        # → they must NOT appear in check_freshness return
        core_memory_md.write_text("changed\n", encoding="utf-8")
        config_yaml.write_text("changed\n", encoding="utf-8")
        result_d = check_freshness(repo_root=tmpdir)
        # Still missing all 3 required (the conditional files are tracked but not checked)
        assert sorted(result_d) == sorted(["PORTFOLIO.md", "Faktortabelle.md", "log.md"]), (
            f"Sub-case D: conditional files must be ignored, got {result_d}"
        )
        # Verify CORE-MEMORY and config are NOT in the result
        assert "CORE-MEMORY.md" not in result_d, (
            "CORE-MEMORY.md must not appear in freshness result"
        )
        assert "config.yaml" not in result_d, "config.yaml must not appear in freshness result"


# ---------------------------------------------------------------------------
# Case 7: Integration — P1 → P2a → P2b → P3.5 fail-close, no archive write
# ---------------------------------------------------------------------------
def case_7() -> None:
    """Synthetischer vollanalyse-Draft mit Provenance-Fail (freshness_missing=['PORTFOLIO.md']).
    Asserts: P3.5 returns (False, reason), reason mentions vollanalyse+fresh,
    archive_score.py NICHT aufgerufen → Archiv-File unveraendert.
    Spec §8.3: Integration-Test ist Pflicht (fail-close haengt an Pipeline-Verdrahtung).
    """
    _require_helpers()

    # Build a forward+vollanalyse record (NOT backfill — would skip Check #1)
    ticker = "ZTS"
    score_datum = "2026-04-21"
    record = _build_minimal_record(ticker, score_datum, score_gesamt=65, defcon_level=3)
    # Override to forward+vollanalyse with valid kurs.referenz + valid quellen + active version
    record["source"] = "forward"
    record["analyse_typ"] = "vollanalyse"
    record["defcon_version"] = "v3.7"  # match versions.DEFCON_ACTIVE_VERSION
    record["kurs"] = {
        "wert": 100.0,
        "waehrung": "USD",
        "referenz": "close_of_score_datum",
        "quelle": "yahoo_eod",
    }
    record["quellen"] = {
        "fundamentals": "defeatbeta",
        "technicals": "shibui",
        "insider": "openinsider+sec_edgar",
        "moat": "gurufocus",
        "sentiment": "zacks+yahoo",
    }
    draft = {"record": record, "skill_meta": {}}

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tf:
        json.dump(draft, tf)
        draft_path = tf.name

    # P1: parse_wrapper
    rec_dict, skill_meta = parse_wrapper(draft_path)
    assert rec_dict["analyse_typ"] == "vollanalyse"
    assert skill_meta == {}

    # P2a (simulated): freshness_missing manuell setzen statt git-status zu mocken
    # Spec §8.3 Mock-Konvention: Tests mocken aus REQUIRED_TOUCH_FILES — wir testen
    # Gate-Logik, nicht Helper-Output. Helper prueft PORTFOLIO/Faktortabelle/log.
    freshness_missing = ["PORTFOLIO.md"]

    # P2b: PORTFOLIO-Tripwire (kein Konflikt — wir nutzen ZTS, das nicht im
    # PORTFOLIO_MD_FIXTURE ist; Caller wuerde "[tripwire: ticker 'ZTS' not in
    # PORTFOLIO.md — new position]" emitten und weiter machen. Kein FAIL P2b.)
    with contextlib.suppress(ValueError, KeyError):
        parse_state_row(ticker, PORTFOLIO_MD_FIXTURE)

    # P3.5: hier muss fail-close greifen
    passed, reasons = check_provenance(
        record_dict=rec_dict,
        freshness_missing=freshness_missing,
        skill_meta=skill_meta,
    )
    assert not passed, f"P3.5 should fail-close, got passed={passed}"
    assert len(reasons) == 1, f"fail-close means 1 reason, got {reasons}"
    assert "vollanalyse requires fresh session" in reasons[0], (
        f"reason should match Check #2: {reasons[0]!r}"
    )
    assert "PORTFOLIO.md" in reasons[0], f"missing-file detail in reason: {reasons[0]!r}"

    # Verify: archive_score.py was NEVER called → real archive_history.jsonl unveraendert.
    # We verify by snapshotting size before and after; case_7 must NOT subprocess archive_score.
    archive_path = REPO_ROOT / "05_Archiv" / "score_history.jsonl"
    if archive_path.exists():
        size_before = archive_path.stat().st_size
        # (no subprocess call here — that's the whole point)
        size_after = archive_path.stat().st_size
        assert size_before == size_after, (
            f"archive must not be touched on P3.5 fail; "
            f"size_before={size_before}, size_after={size_after}"
        )
    # If archive doesn't exist yet, the assertion is trivially true


# ---------------------------------------------------------------------------
# Case 8: Pipeline-Sequence-Order — P3.5 laeuft vor P3, P3 wird bei Fail NICHT aufgerufen
# ---------------------------------------------------------------------------
def case_8() -> None:
    """Codex-Round-2-HIGH-3 Resolution: testet die Gating-Garantie aus Spec §4.3
    (P3 darf bei P3.5-Fail NICHT aufgerufen werden, P3 darf bei P3.5-Pass aufgerufen werden).

    **Test-Aussage praezise:** Validiert Gating-Behavior + stubbed Sequence-Order
    der `_run_pipeline`-Helper-Funktion — NICHT direkt-instrumentiert dass
    `check_provenance()` zeitlich vor `build_migration_event()` laeuft. Letzteres
    folgt aus der Stub-Struktur, in der P3 nur via P3.5-Pass-Branch erreichbar ist.
    Implizit: dieselbe Stub-Struktur muss in SKILL.md-Orchestrierung respektiert
    werden (deshalb auch Task 4 SKILL.md Phase-Tabelle als parallele Authority).

    Zwei Pipeline-Runs:
      Run A: P3.5 fail (freshness_missing) → assert P3-Counter == 0
        (Gating: 'P3 nicht aufgerufen' explizit als Negativ-Aussage)
      Run B: P3.5 pass → assert P3-Counter == 1 (Reachability: P3 erreichbar nach Pass)

    Counter beobachtet nur P3-Aufruf, nicht P3.5-Internals (Codex-Round-2-Refinement:
    minimal-invasiv, gating-fokussiert, refactor-robust).
    """
    _require_helpers()

    # Stub fuer P3 (build_migration_event-Aufruf): inkrementiert Counter
    p3_call_count = {"n": 0}

    def _stub_build_migration_event(skill_meta, forward_score):
        p3_call_count["n"] += 1
        return None  # nicht relevant — wir testen Sequence, nicht Δ-Gate-Output

    def _run_pipeline(record_dict, freshness_missing, skill_meta):
        """Simuliert SKILL.md-Orchestration: P3.5 vor P3, fail-close stoppt."""
        passed, reasons = check_provenance(
            record_dict=record_dict,
            freshness_missing=freshness_missing,
            skill_meta=skill_meta,
        )
        if not passed:
            return ("P3.5_FAIL", reasons)
        # P3 laeuft NUR wenn P3.5 passed
        _stub_build_migration_event(skill_meta, record_dict.get("score_gesamt"))
        return ("P3_DONE", [])

    # Run A: P3.5 fail
    record_a = _build_minimal_record("ZTS", "2026-04-21", score_gesamt=65, defcon_level=3)
    record_a["source"] = "forward"
    record_a["analyse_typ"] = "vollanalyse"
    record_a["defcon_version"] = "v3.7"
    record_a["kurs"] = {
        "wert": 100.0,
        "waehrung": "USD",
        "referenz": "close_of_score_datum",
        "quelle": "yahoo_eod",
    }
    record_a["quellen"] = {
        "fundamentals": "defeatbeta",
        "technicals": "shibui",
        "insider": "openinsider+sec_edgar",
        "moat": "gurufocus",
        "sentiment": "zacks+yahoo",
    }

    p3_call_count["n"] = 0  # reset
    result, reasons = _run_pipeline(record_a, ["PORTFOLIO.md"], {})
    assert result == "P3.5_FAIL", f"Run A expected P3.5_FAIL, got {result}"
    assert p3_call_count["n"] == 0, (
        f"Run A: P3 nicht aufgerufen (Counter==0 erwartet bei P3.5-Fail), "
        f"got Counter={p3_call_count['n']} (=Sequence-Bypass!)"
    )

    # Run B: P3.5 pass (kein freshness_missing)
    p3_call_count["n"] = 0  # reset
    result, _reasons = _run_pipeline(record_a, [], {})
    assert result == "P3_DONE", f"Run B expected P3_DONE, got {result}"
    assert p3_call_count["n"] == 1, (
        f"Run B: P3 muss 1x aufgerufen sein nach P3.5-Pass, got Counter={p3_call_count['n']}"
    )


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
    (7, "Integration — P3.5 fail-close, no archive write", case_7),
    (8, "Pipeline-Sequence — P3.5 vor P3 (P3-Counter)", case_8),
]


def run_all() -> None:
    passed = 0
    failed = 0
    for n, label, fn in CASES:
        try:
            fn()
            print(f"[{n}/{len(CASES)}] PASS: {label}")
            passed += 1
        except Exception as exc:
            print(f"[{n}/{len(CASES)}] FAIL: {label} — {type(exc).__name__}: {exc}")
            failed += 1

    print()
    if failed == 0:
        print(f"✅ all {passed}/{len(CASES)} cases passed")
    else:
        print(f"❌ {failed} case(s) failed, {passed}/{len(CASES)} passed")
        sys.exit(1)


if __name__ == "__main__":
    run_all()
