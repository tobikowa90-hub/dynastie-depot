#!/usr/bin/env python3
"""defeatbeta_subprocess.py — WSL-Subprocess-Bridge gegen defeatbeta-api-Package.

Crosswalk-Trigger nutzt diese Bridge für Primary-Pull (defeatbeta-Seite),
weil das defeatbeta-api-Package nur in WSL-Env /home/tobia/.defeatbeta-env/ verfügbar ist.

Spec: docs/superpowers/specs/2026-05-22-finnhub-integration-design.md v0.3 §5.
Semantische Äquivalenz zu defeatbeta-MCP-Path verifiziert in Acceptance A12 (Task 10).
"""

from __future__ import annotations

import json
import logging
import subprocess
from typing import Any

log = logging.getLogger(__name__)

WSL_PYTHON = "/home/tobia/.defeatbeta-env/bin/python"
WSL_DISTRO = "Ubuntu-24.04"
SUBPROCESS_TIMEOUT_SEC = 30

# Mapping: Crosswalk-Metric-Name (Spec §5.1) → defeatbeta-api callable + Result-Aggregator
# Inline-Script läuft in WSL, importiert defeatbeta_api, ruft die jeweiligen Methoden,
# serialisiert als JSON nach stdout.
#
# WICHTIG (Codex-CP0-HIGH-2 + Task 9 Step 4a Decision-Gate):
# Initial-Set umfasst 3 Metriken (roe/peTTM/roic) — der A12 Identity-Check (Task 10) läuft
# darauf. Die restlichen 5 Metriken (grossMargin5Y/debtToEquity/epsGrowth5Y/capexCagr5Y/
# fcfPerShareTTM) werden in Task 9 Step 5 via Live-WSL-Probe auf defeatbeta-api-Methoden-
# Verfügbarkeit getestet und das Script ggf. erweitert. Final-State: alle 8 Metriken im
# Script ODER PIPELINE #76 für gezielte Methoden-Discovery in v0.2 (siehe Decision-Gate
# in Task 9 Step 4a).
_METRIC_PULL_SCRIPT = r"""
import json, sys
from defeatbeta_api.data.ticker import Ticker
symbol = sys.argv[1]
t = Ticker(symbol)
out = {}
try:
    df = t.roe()
    # roe() returns a DataFrame; last row 'roe' column is a decimal ratio — multiply by 100
    out['roe'] = round(float(df.iloc[-1]['roe']) * 100, 4) if df is not None and not df.empty else None
except Exception as e:
    out['roe'] = None
    out['_roe_err'] = str(e)
try:
    df = t.ttm_pe()
    # ttm_pe() returns a DataFrame; last row 'ttm_pe' column is already a ratio
    out['peTTM'] = round(float(df.iloc[-1]['ttm_pe']), 4) if df is not None and not df.empty else None
except Exception as e:
    out['peTTM'] = None
    out['_peTTM_err'] = str(e)
try:
    df = t.roic()
    # roic() returns a DataFrame; last row 'roic' column is a decimal ratio — multiply by 100
    out['roic'] = round(float(df.iloc[-1]['roic']) * 100, 4) if df is not None and not df.empty else None
except Exception as e:
    out['roic'] = None
    out['_roic_err'] = str(e)
# === EXTENSION-POINT (Task 9 Step 4a Decision-Gate) ===
# Step 4a probe result: 2/5 groups YES (grossMargin via quarterly_gross_margin, debtToEquity
# via debt_to_equity). Decision: <3 → keep 3/8 minimal; PIPELINE #76 for v0.2 discovery.
# Ehrlicher Fallback bei Methode-fehlt: out['<metric>'] = None mit
# _<metric>_err = 'method-not-in-defeatbeta-api' → Crosswalk-Record loggt na_reason.
print(json.dumps(out))
"""


def pull_metrics(symbol: str) -> dict[str, Any] | None:
    """Pull defeatbeta-Metriken (DEFCON-relevant Subset) für ein Symbol via WSL.

    Returns: dict mit Metrik-Keys (None bei Sub-Pull-Fail innerhalb der Bridge),
    oder None bei kompletter Subprocess-Failure / Timeout / Invalid-JSON-Output.
    """
    cmd = [
        "wsl.exe",
        "-d",
        WSL_DISTRO,
        "-e",
        WSL_PYTHON,
        "-c",
        _METRIC_PULL_SCRIPT,
        symbol,
    ]
    # wsl.exe -e passes all trailing tokens verbatim to the executable, so `symbol`
    # lands in sys.argv[1] inside the inline Python script.
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=SUBPROCESS_TIMEOUT_SEC,
            check=False,
        )
    except subprocess.TimeoutExpired:
        log.warning(
            "defeatbeta WSL-subprocess timeout for %s after %ds", symbol, SUBPROCESS_TIMEOUT_SEC
        )
        return None
    if result.returncode != 0:
        log.error("defeatbeta WSL-subprocess failed for %s: %s", symbol, result.stderr[:300])
        return None
    # defeatbeta-api prints a banner + INFO logs to stdout before the JSON line.
    # We always print json.dumps(out) last, so take the last non-empty line only.
    last_line = result.stdout.strip().rsplit("\n", 1)[-1].strip()
    try:
        return json.loads(last_line)
    except json.JSONDecodeError:
        log.exception(
            "defeatbeta WSL-output not JSON for %s | stdout=%r", symbol, result.stdout[:300]
        )
        return None
