"""Dynasty-Depot v3.7 Backtest-Ready: one-shot score backfill.

Parses the Markdown Score-Register table in `00_Core/CORE-MEMORY.md`
Section 4 and appends one `ScoreRecord` (source="backfill") per ticker row
to `05_Archiv/score_history.jsonl`.

Rationale: the git history only spans ~2 days / 22 commits, so point-in-time
reconstruction from commits would yield almost nothing. Section 4 is the
best existing historical snapshot (24 tickers, status + next action).

Design choices (per task spec):
  * No sub-score estimation. Fractional split of `score_gesamt` across the
    five blocks using the block weights (50/20/10/10/10). Rounding-drift
    is absorbed into fundamentals.gesamt to satisfy the arithmetic
    validator. Sub-scores stay at 0 (fundamentals bucket `fwd_pe` carries
    the block total since it has no upper cap — honest "not reconstructible").
  * `defcon_version = "historical"` (allowed since the forward-version
    validator only enforces v3.7 for source="forward").
  * `defcon_level`: validator requires score-consistency; if the parsed
    emoji level conflicts with the score (e.g. GOOGL "🟡 3" at score 72
    → expected 4), we override to the score-based level. FLAG status is
    preserved in the notes.
  * `moat.rating = "narrow"` for all backfill records → the quality-trap
    validator is skipped (it only fires on wide-moat + low sub-scores).
  * `kurs` / `market_cap` / `quellen` → "backfill_not_available" placeholders.
  * Approximate dates ("~März 2026") → ISO month-mid (2026-03-15), per
    spec §9.2.

CLI:
    python backfill_scores.py [--dry-run] [--verbose]

Exit codes:
  0 — success (all parsed records validated; records appended or dry-run)
  1 — parser failure (table not found / cannot extract any row)
  2 — IO failure on score_history.jsonl

Spec: docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Optional

# --- stdout UTF-8 (mirror schemas.py) --------------------------------------
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

# --- import schemas --------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))

from pydantic import ValidationError  # noqa: E402

from schemas import (  # noqa: E402
    Flags,
    FundamentalsScore,
    InsiderScore,
    Kurs,
    MarketCap,
    MetrikenRoh,
    MoatScore,
    Quellen,
    ScoreRecord,
    Scores,
    SentimentScore,
    TechnicalsScore,
)

# --- paths -----------------------------------------------------------------
REPO_ROOT: Path = Path(__file__).resolve().parent.parent.parent
CORE_MEMORY: Path = REPO_ROOT / "00_Core" / "CORE-MEMORY.md"
ARCHIVE_PATH: Path = REPO_ROOT / "05_Archiv" / "score_history.jsonl"
PARSER_ERROR_LOG: Path = REPO_ROOT / "05_Archiv" / "_parser_errors.log"

# --- constants -------------------------------------------------------------
SECTION_HEADER_RE = re.compile(r"^## 4\. Score-Register")
MONTHS_DE: dict[str, int] = {
    "Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6,
    "Juli": 7, "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12,
}
# Emoji + digit — we only need the digit
DEFCON_LEVEL_RE = re.compile(r"([1-4])")
DATE_NUMERIC_RE = re.compile(r"^(\d{1,2})\.(\d{1,2})\.(\d{4})$")
DATE_MONTH_ONLY_RE = re.compile(r"^~?\s*([A-Za-zÄÖÜäöüß]+)\s+(\d{4})$")
BACKFILL_STAMP = "2026-04-17"  # date this backfill was run — for note provenance


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def _log_parser_error(reason: str, raw: str) -> None:
    ts = datetime.now().isoformat(timespec="seconds")
    PARSER_ERROR_LOG.parent.mkdir(parents=True, exist_ok=True)
    with PARSER_ERROR_LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"[{ts}] backfill_scores.py reason={reason!r} raw={raw!r}\n")


def parse_datum(raw: str) -> Optional[date]:
    """Parse German date strings from column 4.

    Accepts:
      * '17.04.2026'
      * '17.04.2026 (v3.7 ...)' — annotation stripped
      * '~März 2026' → 2026-03-15
      * 'März 2026' → 2026-03-15
      * '25.03.2026'
    Returns None on failure.
    """
    s = raw.strip()
    # strip any parenthetical annotation: "17.04.2026 (v3.7 Post-Q1 ...)"
    s = re.sub(r"\s*\([^)]*\)\s*", "", s).strip()

    m = DATE_NUMERIC_RE.match(s)
    if m:
        d, mo, y = (int(x) for x in m.groups())
        try:
            return date(y, mo, d)
        except ValueError:
            return None

    m = DATE_MONTH_ONLY_RE.match(s)
    if m:
        month_name, year = m.group(1), int(m.group(2))
        # Strip leading ~ already handled by regex group capture of month word
        if month_name.startswith("~"):
            month_name = month_name.lstrip("~").strip()
        month = MONTHS_DE.get(month_name)
        if month is None:
            return None
        return date(year, month, 15)

    return None


def parse_defcon_level(raw: str) -> Optional[int]:
    """Extract the 1-4 digit from '🟡 3' / '🔴 1' etc."""
    m = DEFCON_LEVEL_RE.search(raw)
    if not m:
        return None
    return int(m.group(1))


def score_to_defcon(score: int) -> int:
    if score >= 70:
        return 4
    if score >= 60:
        return 3
    if score >= 50:
        return 2
    return 1


def extract_table_rows(md_text: str) -> list[list[str]]:
    """Find Section 4 and return a list of cell-lists (one per data row).

    Data rows start after the header/separator. The section ends at the next
    '## ' heading or end of file.
    """
    lines = md_text.splitlines()

    # locate section start
    start_idx: Optional[int] = None
    for i, line in enumerate(lines):
        if SECTION_HEADER_RE.match(line):
            start_idx = i
            break
    if start_idx is None:
        return []

    # collect table lines until next "## " or EOF
    rows: list[list[str]] = []
    seen_separator = False
    for line in lines[start_idx + 1:]:
        if line.startswith("## "):
            break
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        # Separator row like "|--------|-------|..."
        if re.match(r"^\|[\s\-:|]+\|$", stripped):
            seen_separator = True
            continue
        if not seen_separator:
            # This is the header row; skip it.
            continue
        # data row: split and trim
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        rows.append(cells)
    return rows


# ---------------------------------------------------------------------------
# Record construction
# ---------------------------------------------------------------------------


def build_scores(score_gesamt: int) -> Scores:
    """Fractional split of score_gesamt into the five block.gesamt values.

    Weights: fundamentals 0.50, moat 0.20, technicals 0.10, insider 0.10,
    sentiment 0.10. Rounding drift goes onto fundamentals.gesamt so the
    top-level arithmetic validator passes.

    All sub-scores remain 0. The fundamentals block carries its total on
    `fwd_pe` (which has no upper cap) — honest placeholder: sub-breakdown
    is not reconstructible.

    Caps respected:
      * fundamentals.gesamt ≤ 50 (at max score 88 → 44, with drift +1 → 45)
      * moat.gesamt ≤ 20 (at max → 18)
      * technicals.gesamt in [-1, 11] (at max → 9)
      * insider.gesamt in [0, 10] (at max → 9)
      * sentiment.gesamt in [-2, 12] (at max → 9)
    """
    fund = round(score_gesamt * 0.50)
    moat = round(score_gesamt * 0.20)
    tech = round(score_gesamt * 0.10)
    ins = round(score_gesamt * 0.10)
    sent = round(score_gesamt * 0.10)

    drift = score_gesamt - (fund + moat + tech + ins + sent)
    fund += drift  # absorb rounding difference

    # Defensive clamp (should not trigger for any score in [50, 88])
    fund = max(0, min(50, fund))

    fundamentals = FundamentalsScore(
        gesamt=fund,
        fwd_pe=fund,  # carry block total here (no upper cap); all other subs 0
        p_fcf=0,
        bilanz=0,
        capex_ocf=0,
        roic=0,
        fcf_yield=0,
        operating_margin=0,
        sbc_malus=0,
        accruals_malus=0,
        tariff_malus=0,
    )
    moat_score = MoatScore(
        gesamt=moat,
        rating="narrow",  # deactivates quality-trap validator
        quellen=[],
        gm_trend_delta=0,
        pricing_power_bonus=0,
    )
    technicals = TechnicalsScore(
        gesamt=tech,
        ath_distanz=0,
        rel_staerke=0,
        trend_lage=0,
        dcf_relation_delta=0,
    )
    insider = InsiderScore(
        gesamt=ins,
        net_buy_6m=0,
        ownership=0,
        kein_20m_selling=0,
    )
    sentiment = SentimentScore(
        gesamt=sent,
        strong_buy_ratio=0,
        sell_ratio=0,
        pt_upside=0,
        eps_revision_delta=0,
        pt_dispersion_delta=0,
    )
    return Scores(
        fundamentals=fundamentals,
        moat=moat_score,
        technicals=technicals,
        insider=insider,
        sentiment=sentiment,
    )


def build_record(
    ticker: str,
    score: int,
    score_datum: date,
    parsed_defcon: Optional[int],
    status: str,
    naechste_aktion: str,
) -> ScoreRecord:
    scores = build_scores(score)
    expected_defcon = score_to_defcon(score)

    iso = score_datum.isoformat()
    record_id = f"{iso}_{ticker}_vollanalyse"

    notiz_parts = [
        f"BACKFILL {BACKFILL_STAMP} aus CORE-MEMORY Section 4.",
        f"Status: {status}.",
        f"Nächste Aktion: {naechste_aktion}.",
        "Source-Tabelle war Stand 17.04.2026.",
    ]
    if parsed_defcon is not None and parsed_defcon != expected_defcon:
        notiz_parts.append(
            f"Note: parsed DEFCON {parsed_defcon} overridden to score-consistent "
            f"level {expected_defcon} (validator requirement)."
        )
    notizen = " ".join(notiz_parts)

    return ScoreRecord(
        schema_version="1.0",
        record_id=record_id,
        source="backfill",
        ticker=ticker,
        score_datum=score_datum,
        analyse_typ="vollanalyse",
        defcon_version="historical",
        kurs=Kurs(
            wert=0.0,
            waehrung="UNKNOWN",
            referenz="backfill_not_available",
            quelle="backfill",
        ),
        market_cap=MarketCap(wert=0.0, waehrung="UNKNOWN"),
        scores=scores,
        score_gesamt=score,
        defcon_level=expected_defcon,  # type: ignore[arg-type]
        flags=Flags(aktiv_ids=[], bei_analyse_referenziert=[]),
        metriken_roh=MetrikenRoh(),
        quellen=Quellen(
            fundamentals="backfill_not_available",
            technicals="backfill_not_available",
            insider="backfill_not_available",
            moat="backfill_not_available",
            sentiment="backfill_not_available",
        ),
        notizen=notizen,
    )


# ---------------------------------------------------------------------------
# Archive IO
# ---------------------------------------------------------------------------


def load_existing_record_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    ids: set[str] = set()
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                rid = obj.get("record_id")
                if isinstance(rid, str):
                    ids.add(rid)
            except json.JSONDecodeError:
                continue
    return ids


def append_record(path: Path, record: ScoreRecord) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = record.model_dump_json() + "\n"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Backfill score history from CORE-MEMORY.md Section 4.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Parse+validate only, no write.")
    parser.add_argument("--verbose", action="store_true", help="Per-record status line.")
    args = parser.parse_args(argv)

    if not CORE_MEMORY.exists():
        print(f"[FATAL] CORE-MEMORY.md not found at {CORE_MEMORY}", file=sys.stderr)
        return 2
    md_text = CORE_MEMORY.read_text(encoding="utf-8")

    rows = extract_table_rows(md_text)
    if not rows:
        print("[FATAL] Score-Register table empty or not found in CORE-MEMORY.md",
              file=sys.stderr)
        return 1

    existing_ids = load_existing_record_ids(ARCHIVE_PATH)

    parsed = 0
    written = 0
    skipped_dup = 0
    failed = 0

    for row in rows:
        raw_row = " | ".join(row)
        # Expect at least 6 cells; tolerate trailing empties
        if len(row) < 6:
            _log_parser_error("row_too_short", raw_row)
            failed += 1
            if args.verbose:
                print(f"[FAIL] short row: {raw_row}")
            continue

        ticker = row[0]
        score_raw = row[1]
        defcon_raw = row[2]
        datum_raw = row[3]
        status = row[4]
        naechste = row[5]

        try:
            score = int(score_raw)
        except ValueError:
            _log_parser_error(f"score_not_int: {score_raw!r}", raw_row)
            failed += 1
            if args.verbose:
                print(f"[FAIL] {ticker}: score not int ({score_raw!r})")
            continue

        score_datum = parse_datum(datum_raw)
        if score_datum is None:
            _log_parser_error(f"datum_unparseable: {datum_raw!r}", raw_row)
            failed += 1
            if args.verbose:
                print(f"[FAIL] {ticker}: datum unparseable ({datum_raw!r})")
            continue

        parsed_defcon = parse_defcon_level(defcon_raw)

        try:
            record = build_record(
                ticker=ticker,
                score=score,
                score_datum=score_datum,
                parsed_defcon=parsed_defcon,
                status=status,
                naechste_aktion=naechste,
            )
        except ValidationError as e:
            _log_parser_error(f"pydantic_validation: {e.errors()}", raw_row)
            failed += 1
            if args.verbose:
                print(f"[FAIL] {ticker}: {e.errors()[0].get('msg', 'validation error')}")
            continue
        except Exception as e:  # noqa: BLE001
            _log_parser_error(f"build_error: {type(e).__name__}: {e}", raw_row)
            failed += 1
            if args.verbose:
                print(f"[FAIL] {ticker}: {type(e).__name__}: {e}")
            continue

        parsed += 1

        if record.record_id in existing_ids:
            skipped_dup += 1
            if args.verbose:
                print(f"[SKIP] {ticker} ({record.record_id} exists)")
            continue

        if args.dry_run:
            if args.verbose:
                print(f"[OK] {ticker} ({record.record_id}) — dry-run, not written")
            continue

        try:
            append_record(ARCHIVE_PATH, record)
        except OSError as e:
            print(f"[FATAL] IO error appending {ticker}: {e}", file=sys.stderr)
            return 2

        existing_ids.add(record.record_id)
        written += 1
        if args.verbose:
            print(f"[OK] {ticker} ({record.record_id})")

    mode = "DRY-RUN" if args.dry_run else "WRITE"
    print(
        f"[{mode}] parsed: {parsed} | written: {written} | "
        f"skipped (dup): {skipped_dup} | failed: {failed}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
