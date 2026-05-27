"""Hook-Latency p95-Probe für Phase-0a Burn-in Validation.

Liest plugin-seitige Hook-Logs (context-mode, claude-mem) und berechnet p50/p95/p99
Latency-Verteilung. Schreibt JSONL nach 03_Tools/hook-latency-history/<UTC-date>.jsonl.

R2 Codex MEDIUM-1: Pfade werden via Env-Vars HOOK_LATENCY_CTX_LOG +
HOOK_LATENCY_MEM_LOG überschreibbar — Default-Pfade sind Pre-Flight-verifiziert,
aber bei Abweichungen aus Pre-Flight-Verdict-File entsprechende Env-Vars setzen.
"""

from __future__ import annotations

import json
import os
import statistics
import sys
from datetime import UTC, datetime
from pathlib import Path

CTX_LOG = Path(
    os.environ.get(
        "HOOK_LATENCY_CTX_LOG", Path.home() / ".claude" / "context-mode" / "hook-timing.log"
    )
)
MEM_LOG = Path(
    os.environ.get("HOOK_LATENCY_MEM_LOG", Path.home() / ".claude-mem" / "logs" / "hook-timing.log")
)
OUT_DIR = Path("03_Tools/hook-latency-history")


def parse_log(p: Path) -> list[float]:
    if not p.exists():
        return []
    latencies = []
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
            ms = rec.get("duration_ms") or rec.get("latency_ms")
            if isinstance(ms, (int, float)):
                latencies.append(float(ms))
        except json.JSONDecodeError:
            continue
    return latencies


def percentile(data: list[float], pct: float) -> float:
    """Robust percentile berechnung. Für kleine N (Burn-in early hours) fallback
    auf sorted-data-index interpolation; nur bei N>=100 statistics.quantiles."""
    if not data:
        return 0.0
    if len(data) == 1:
        return data[0]
    if len(data) < 100:
        sorted_data = sorted(data)
        idx = min(len(sorted_data) - 1, int(len(sorted_data) * pct / 100))
        return sorted_data[idx]
    return statistics.quantiles(data, n=100, method="exclusive")[int(pct) - 1]


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ctx = parse_log(CTX_LOG)
    mem = parse_log(MEM_LOG)
    combined = ctx + mem
    if not combined:
        # R1 Codex MEDIUM-3 / Gemini LOW-3: persistiere no-data-Record statt silent-exit
        no_data_record = {
            "ts_utc": datetime.now(UTC).isoformat(),
            "status": "no_data",
            "ctx_log_exists": CTX_LOG.exists(),
            "mem_log_exists": MEM_LOG.exists(),
        }
        out_file = OUT_DIR / f"{datetime.now(UTC).strftime('%Y-%m-%d')}.jsonl"
        with out_file.open("a", encoding="utf-8", newline="") as f:
            f.write(json.dumps(no_data_record) + "\n")
        print(json.dumps(no_data_record, indent=2), file=sys.stderr)
        print(
            "WARN: no hook timing data — record persisted as 'no_data' for audit trail",
            file=sys.stderr,
        )
        return 2
    record = {
        "ts_utc": datetime.now(UTC).isoformat(),
        "ctx_samples": len(ctx),
        "mem_samples": len(mem),
        "combined_samples": len(combined),
        "p50_ms": round(percentile(combined, 50), 2),
        "p95_ms": round(percentile(combined, 95), 2),
        "p99_ms": round(percentile(combined, 99), 2),
        "max_ms": round(max(combined), 2),
        "threshold_300ms_pass": percentile(combined, 95) <= 300.0,
    }
    out_file = OUT_DIR / f"{datetime.now(UTC).strftime('%Y-%m-%d')}.jsonl"
    with out_file.open("a", encoding="utf-8", newline="") as f:
        f.write(json.dumps(record) + "\n")
    print(json.dumps(record, indent=2))
    return 0 if record["threshold_300ms_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
