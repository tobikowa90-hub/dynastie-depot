#!/usr/bin/env python3
"""finnhub_crosswalk_trigger.py — Crosswalk-Logging-Runner.

Pulls Metriken parallel via defeatbeta-WSL-Bridge + FinnHub get_metrics(),
schreibt Pro-Symbol-Pro-Metrik einen Record nach 03_Tools/finnhub_crosswalk_log.jsonl
gemaess Spec §5.3 (Schema-Contract).

Usage:
    python 03_Tools/finnhub_crosswalk_trigger.py --symbols MSFT,V,ASML
    python 03_Tools/finnhub_crosswalk_trigger.py --symbols MSFT,V,ASML --force

Spec: docs/superpowers/specs/2026-05-22-finnhub-integration-design.md v0.3.
"""

from __future__ import annotations

import argparse
import contextlib
import logging
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "03_Tools"))

import defeatbeta_subprocess  # noqa: E402
import finnhub_client  # noqa: E402
from _atomic_io import atomic_jsonl_append  # noqa: E402

LOG_FILE = ROOT / "03_Tools" / "finnhub_crosswalk_log.jsonl"
log = logging.getLogger(__name__)

ToleranceStatus = Literal["within", "warn", "crit", "na"]

# Spec §5.1 Toleranz-Tabelle — wird in Task 12 vollstaendig vom Trigger-Run konsumiert
METRIC_TOLERANCES: dict[str, str] = {
    "peTTM": "5%",
    "roe": "2pp",
    "roic": "2pp",  # WARN-Tier; CRIT-Tier in Task 12 separat
    "grossMargin5Y": "2pp",
    "debtToEquity": "10%",
    "epsGrowth5Y": "3pp",
    "capexCagr5Y": "3pp",
    "fcfPerShareTTM": "5%",
}


class CrosswalkRecord(BaseModel):
    timestamp: str
    run_id: str
    batch_id: str
    symbol: str
    metric: str
    defeatbeta_value: float | None
    finnhub_value: float | None
    delta: float | None
    delta_unit: Literal["pp", "pct_rel"]
    tolerance_used: str
    tolerance_status: ToleranceStatus
    na_reason: str | None = None
    # pydantic v2 erlaubt _ prefix nur via Field-Alias bzw. ConfigDict; wir nutzen meta (umbenannt)
    # Spec §5.3 verlangt aber "_meta" als JSONL-Output-Key — daher Field alias
    meta: dict = Field(..., alias="_meta", serialization_alias="_meta")

    model_config = {"populate_by_name": True, "serialize_by_alias": True, "strict": True}


def compute_delta(
    defeatbeta_value: float | None,
    finnhub_value: float | None,
    tolerance: str,
) -> tuple[float | None, ToleranceStatus]:
    """Return (delta, status). delta=None wenn N/A."""
    if defeatbeta_value is None or finnhub_value is None:
        return None, "na"
    delta = finnhub_value - defeatbeta_value
    # 'crit' status is produced by the Task-12 multi-tier comparator, not here.
    if tolerance.endswith("pp"):
        thresh = float(tolerance[:-2])
        status: ToleranceStatus = "within" if abs(delta) <= thresh else "warn"
    elif tolerance.endswith("%"):
        thresh = float(tolerance[:-1]) / 100.0
        if defeatbeta_value == 0:
            return None, "na"
        rel = abs(delta) / abs(defeatbeta_value)
        status = "within" if rel <= thresh else "warn"
    else:
        raise ValueError(f"unknown tolerance format: {tolerance}")
    return delta, status


# FinnHub-Key-Mapping Spec §5.1 → finnhub_client-Subset-Keys (Task 6 keep_keys)
# defeatbeta-Keys sind die Klar-Namen, FinnHub-Keys können abweichen (z.B. roeTTM vs roe)
FINNHUB_KEY_MAP: dict[str, str] = {
    "peTTM": "peTTM",
    "roe": "roeTTM",
    "roic": "roiTTM",
    "grossMargin5Y": "grossMargin5Y",
    "debtToEquity": "totalDebt/totalEquityQuarterly",
    "epsGrowth5Y": "epsGrowth5Y",
    "capexCagr5Y": "capexCagr5Y",
    "fcfPerShareTTM": "fcfPerShareTTM",
}


def _now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _delta_unit_for(tolerance: str) -> str:
    return "pp" if tolerance.endswith("pp") else "pct_rel"


def _na_reason(defeatbeta_value, finnhub_value, finnhub_data) -> str | None:
    if defeatbeta_value is None and finnhub_value is None:
        return "both_missing"
    if defeatbeta_value is None:
        return "defeatbeta_missing"
    if finnhub_value is None:
        # finnhub_data is None means get_metrics() failed (401/403/429-exhausted/timeout/network);
        # finnhub_data is dict but metric absent means upstream returned partial payload
        if finnhub_data is None:
            return "finnhub_unavailable"
        return "finnhub_missing"
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="FinnHub Crosswalk-Trigger (Spec §5)")
    ap.add_argument("--symbols", required=True, help="comma-sep ticker list, e.g. MSFT,V,ASML")
    ap.add_argument("--force", action="store_true", help="bypass FinnHub-cache for fresh-pull")
    ap.add_argument("--batch-tag", default="daily-crosswalk")
    args = ap.parse_args(argv)

    with contextlib.suppress(Exception):
        sys.stdout.reconfigure(encoding="utf-8")

    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    if not symbols:
        print("ERROR no symbols", file=sys.stderr)
        return 1

    today = datetime.now(UTC).strftime("%Y%m%d")
    batch_id = f"{today}-{args.batch_tag}"
    record_counter = 0

    for sym in symbols:
        db_data = defeatbeta_subprocess.pull_metrics(sym)
        defeatbeta_pulled_at = _now_iso()
        fh_data = finnhub_client.get_metrics(sym, force=args.force)
        finnhub_pulled_at = _now_iso()

        for metric, tolerance in METRIC_TOLERANCES.items():
            db_val = db_data.get(metric) if db_data else None
            fh_key = FINNHUB_KEY_MAP.get(metric, metric)
            fh_val = fh_data.get("metrics", {}).get(fh_key) if fh_data else None
            delta, status = compute_delta(db_val, fh_val, tolerance)
            na_reason = _na_reason(db_val, fh_val, fh_data)

            record_counter += 1
            rec = CrosswalkRecord(
                timestamp=_now_iso(),
                run_id=f"{today}-{sym}-{metric}-{record_counter:03d}",
                batch_id=batch_id,
                symbol=sym,
                metric=metric,
                defeatbeta_value=db_val,
                finnhub_value=fh_val,
                delta=delta,
                delta_unit=_delta_unit_for(tolerance),
                tolerance_used=tolerance,
                tolerance_status=status,
                na_reason=na_reason,
                _meta={
                    "read_only": True,
                    "for_scoring": False,
                    "schema_version": "v1",
                    "defeatbeta_pulled_at": defeatbeta_pulled_at,
                    "finnhub_pulled_at": finnhub_pulled_at,
                },
            )
            atomic_jsonl_append(LOG_FILE, rec)
            if status == "warn":
                log.warning("Crosswalk WARN %s/%s: delta=%s tol=%s", sym, metric, delta, tolerance)

    print(f"OK {record_counter} records written → {LOG_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
