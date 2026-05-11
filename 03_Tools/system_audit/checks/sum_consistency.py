"""Check: Sum-Consistency intra-Block — schema_version-Allowlist (Option C).

Spec §3 M3 + Plan 2026-05-11-codebase-defect-patterns v1.2.

Logik:
- v1.0 Records: grandfathered. Sub-Sum != gesamt → INFO (informativ, kein FAIL).
- v2.0+ Records: strict. Sub-Sum != gesamt → FAIL.
- MoatScore: immer SKIP (.gesamt rating-derived, nicht summed).

Begründung: empirische Phase-0-Verifikation 2026-05-11 zeigte 24/34 Legacy v1.0
Records in technicals/insider/sentiment mit Sub-Sum=0 + gesamt>0. Strict-Pydantic-
Validator hätte jsonl_schema.py:82 strict-Parse zu 24 FAILs gekippt; Audit-Layer-
Check mit Allowlist erlaubt schrittweise Migration auf v2.0 ohne Production-Block.
"""

from __future__ import annotations

import contextlib
import json
import math
import time
from pathlib import Path
from typing import Any

from system_audit.types import AuditContext, CheckResult, FailureDetail


def _parse_version(v: str) -> tuple[int, ...]:
    """Parse semver-like 'x.y[.z]' string to tuple for proper comparison.

    Lexicographic string compare breaks at v10.0+ (CR-CP2 finding). Falls back
    to (1, 0) on parse error.
    """
    try:
        return tuple(int(part) for part in v.split("."))
    except (ValueError, AttributeError):
        return (1, 0)

# Block-Klassen → Liste numerischer Sub-Field-Namen.
# MoatScore explizit EXKLUDIERT (rating-derived).
BLOCK_NUMERIC_FIELDS: dict[str, tuple[str, ...]] = {
    "fundamentals": (
        "fwd_pe", "p_fcf", "bilanz", "capex_ocf", "roic", "fcf_yield",
        "operating_margin", "sbc_malus", "accruals_malus", "tariff_malus",
    ),
    "technicals": ("ath_distanz", "rel_staerke", "trend_lage", "dcf_relation_delta"),
    "insider": ("net_buy_6m", "ownership", "kein_20m_selling"),
    "sentiment": (
        "strong_buy_ratio", "sell_ratio", "pt_upside",
        "eps_revision_delta", "pt_dispersion_delta",
    ),
    # NOTE: "moat" intentionally absent — MoatScore.gesamt is rating-derived.
}

ABS_TOL = 0.01


def _sum_numerics(block: dict[str, Any], field_names: tuple[str, ...]) -> float:
    # Defensive: skip non-numeric silently — audit-layer is not a validator,
    # jsonl_schema.py-Check owns strict Pydantic-validation upstream.
    total = 0.0
    for name in field_names:
        val = block.get(name, 0)
        with contextlib.suppress(ValueError, TypeError):
            total += float(val)
    return total


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    store_override: Path | None = None,
) -> CheckResult:
    start = time.monotonic()

    store = store_override or (repo_root / "05_Archiv" / "score_history.jsonl")
    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    if not store.exists():
        failures.append(FailureDetail(
            location=f"sum_consistency:{store}",
            expected="score_history.jsonl present",
            actual="missing",
            severity="warning",
            hint="Backfill ausstehend oder Pfad falsch?",
        ))
        return CheckResult(
            name="sum_consistency",
            status="SKIP",
            n_checked=0,
            n_passed=0,
            failures=failures,
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    with store.open("r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.strip():
                continue
            n_checked += 1
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                # Json-Parse-Fehler ist jsonl_schema.py-Domain, hier ignorieren
                continue

            schema_v_str = str(rec.get("schema_version", "1.0"))
            schema_v_parts = _parse_version(schema_v_str)
            scores = rec.get("scores", {})
            rec_id = rec.get("record_id", f"line-{lineno}")
            record_ok = True

            for block_name, field_names in BLOCK_NUMERIC_FIELDS.items():
                block = scores.get(block_name, {})
                if not block:
                    continue
                gesamt = block.get("gesamt")
                if gesamt is None:
                    continue
                try:
                    gesamt_float = float(gesamt)
                except (ValueError, TypeError):
                    # Non-numeric gesamt — jsonl_schema.py-Domain, hier skip
                    continue
                subs_sum = _sum_numerics(block, field_names)
                if math.isclose(gesamt_float, subs_sum, abs_tol=ABS_TOL):
                    continue

                # Mismatch detected
                if schema_v_parts >= (2, 0):
                    record_ok = False
                    failures.append(FailureDetail(
                        location=f"{rec_id}:{block_name}",
                        expected=f"{block_name}.gesamt == sum(numerics)={subs_sum}",
                        actual=f"gesamt={gesamt}",
                        severity="error",
                        hint=f"Schema v{schema_v_str} strict — Sub-Field-Belegung korrigieren",
                    ))
                else:
                    # v1.0 grandfathered — INFO, nicht FAIL
                    failures.append(FailureDetail(
                        location=f"{rec_id}:{block_name}",
                        expected=f"{block_name}.gesamt == sum(numerics)={subs_sum}",
                        actual=f"gesamt={gesamt} (legacy v{schema_v_str})",
                        severity="info",
                        hint="Legacy v1.0 grandfathered; neue Records auf v2.0 bumpen",
                    ))

            if record_ok:
                n_passed += 1

    has_error = any(f.severity == "error" for f in failures)
    status = "FAIL" if has_error else "PASS"

    return CheckResult(
        name="sum_consistency",
        status=status,
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
