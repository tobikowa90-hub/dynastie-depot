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

import logging
import sys
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "03_Tools"))

import defeatbeta_subprocess  # noqa: E402, F401
import finnhub_client  # noqa: E402, F401
from _atomic_io import atomic_jsonl_append  # noqa: E402, F401

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

    model_config = {"populate_by_name": True, "serialize_by_alias": True}


def compute_delta(
    defeatbeta_value: float | None,
    finnhub_value: float | None,
    tolerance: str,
) -> tuple[float | None, ToleranceStatus]:
    """Return (delta, status). delta=None wenn N/A."""
    if defeatbeta_value is None or finnhub_value is None:
        return None, "na"
    delta = finnhub_value - defeatbeta_value
    if tolerance.endswith("pp"):
        thresh = float(tolerance[:-2])
        status: ToleranceStatus = "within" if abs(delta) <= thresh else "warn"
    elif tolerance.endswith("%"):
        thresh = float(tolerance[:-1]) / 100.0
        if defeatbeta_value == 0:
            return delta, "na"
        rel = abs(delta) / abs(defeatbeta_value)
        status = "within" if rel <= thresh else "warn"
    else:
        raise ValueError(f"unknown tolerance format: {tolerance}")
    return delta, status
