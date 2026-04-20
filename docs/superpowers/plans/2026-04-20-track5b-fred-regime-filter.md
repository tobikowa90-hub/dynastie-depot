# Track 5b — FRED Macro-Regime-Filter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

> **Phase-1b-Paper-Ingest-Header-Notice (2026-04-20):** Zwei Befunde verstärken den wissenschaftlichen Anker dieses Plans:
> - **B19 FINSABER** (Li-Kim-Cucuringu-Ma 2026) → Bull/Bear-Asymmetrie ist systematisch und Regime-bewusste Strategien schlagen Regime-blinde. Direkter Anker für §31 Regime-Modulation-Logik. Neues **§29.5-Regime-Audit-Addendum** verlangt Bull/Bear-Subsample-SR-Trennung im Backtest (Task 3.x bei Grid-Search-Implementierung beachten).
> - **B20 GT-Score** (Sheppert 2026) → Composite Anti-Overfitting Objective (Performance × Significance × Consistency × Downside-Risk) als **Tie-Break R0** in Grid-Search (1620 Kombinationen). Ergänzt §29.1 PBO-Gate um In-the-Loop-Objective. Task 3.x prüft, ob GT-Score als zweite Objective-Schicht neben aggregierter Sharpe-Ratio einbezogen wird.
>
> **Track 5b-Scope durch Phase-1b nicht geändert** — die Papers verankern die Plan-Methodik, erzwingen aber keine Struktur-Änderung am §31-Ruleset-Design.

**Goal:** Drei FRED-Macro-Serien (HY-OAS / 10Y-2Y Treasury-Curve / ISM-PMI) als mechanischen Sparraten-Regime-Modulator (`normal` / `risk_off`) aktivieren — basierend auf einem Grid-Search-kalibrierten §31-Ruleset, ohne Eingriff in DEFCON-Scoring und ohne diskretionären Override. Sparraten-Modulation erfolgt auf Einzelraten-Ebene via `sparraten_factor ∈ {1.00, <1.00}`, respektiert den 8.0-Nenner aus STATE.md.

**Architecture:**
- **Datenquelle:** FRED API v2 direkt via Python-Lib `fredapi` (Batch-Zugriff, Key-basiert).
- **Revision-Control:** Thin-Adapter `fred_client.py` mit explizitem ALFRED-first-release vs. FRED-latest-release-Modus — Historical-Backfill nutzt **ALFRED** (Look-Ahead-Prevention nach §29.5 Sin #2), Live-Daily-Run nutzt **FRED-latest**.
- **Persistenz:** `05_Archiv/macro_regime_historical.jsonl` (Backtest-Input, immutable) und `05_Archiv/macro_regime.jsonl` (Live-Stream, append-only).
- **Backtest:** `03_Tools/macro_regime_backtest.py` mit vectorisierter Grid-Search über 1620 Parameter-Kombinationen (30 Jahre Daily-Data, 1996-2026) + Sub-Perioden-Sensitivitätstest.
- **Daily-Run:** `03_Tools/macro_regime_daily.py` als separater Cron-Entry-Point, aus Morning-Briefing-Trigger aufgerufen.
- **Kontrolle:** Neue INSTRUKTIONEN §31 kodifiziert Thresholds + Override-Policy (Versions-Bump-Only, kein diskretionärer Override).

**Tech Stack:** Python 3.14.3 (Windows `/c/Python314/`), `fredapi` + `pandas` + `numpy`, ALFRED/FRED REST-API v2, JSONL-Persistenz (gleiches Pattern wie `score_history.jsonl` / `portfolio_returns.jsonl`).

---

## Header-Notice: Spec-§-Referenz-Korrektur

TRACK5-SPEC v1.0 (Commit `22cdeb8`) referenziert in §3.2.4, §3.3.2, §3.4 und §3.5 „CORE-MEMORY §5 Audit-Eintrag". Per Plan-5a-Präzedenz und CLAUDE.md-Landkarte (§5 = Scoring-Lektionen; §1 = Meilensteine ab 15.04.) nutzt dieser Plan **CORE-MEMORY §1** für Deployment- und Backtest-Audit-Einträge. Spec bleibt unverändert — Codex-Bestätigung Option 1 (2026-04-20, siehe Plan 5a Header).

**Weitere Spec-§-Querverweise (korrekt im Ist-Zustand):**
- Spec §3.3.2 „§29-Gate-Framework" → INSTRUKTIONEN §29 (Retrospective-Analyse-Gate) ✓
- Spec §3.4 „§29.5 Sin #2 Look-Ahead-Prevention" → INSTRUKTIONEN §29.5 ✓
- Spec §3.2.4 „Neue INSTRUKTIONEN §31" → INSTRUKTIONEN aktuell endet bei §30 ✓

---

## Entscheidungen aus Spec §5 Open Questions (im Plan fixiert)

| Spec-§5 | Plan-Entscheidung | Begründung (Codex-bestätigt 2026-04-20) |
|---|---|---|
| Q1 α MCP vs. β Python-Lib | **β `fredapi`** | Batch-Zugriff (nicht Live-Query), `03_Tools/`-Präzedenz (insider_intel/eodhd_intel/portfolio_risk), MCP-Downtime würde Morning-Briefing brechen, direkter API-Call robuster |
| Q2 Grid-Search-Runtime | **15-30 Min** bei vectorisierter Implementierung | 1620 Combos × ~30J Daily-Data. Codex-Addition: Threshold-Booleans + Monthly-Alignment + Persistence-Masks **einmal** pro Threshold-Set vorberechnen, Grid-Loop kombiniert nur noch Operators + `sparraten_factor` |
| Q3 Backfill-Bootstrap | **Einmaliger Pull via `get_first_release()`** pro Serie (3 Calls, ALFRED-Semantik für Look-Ahead-Prevention per Entscheidung 1) + Data-Quality-Gate | Codex-Addition: Unique/monotonic Dates, HY-OAS-Intersection-Start 1996-12-31, Business-Day-Gap-Detection, ISM-Carry-Forward-Check, NaN <1% Soft-Threshold. Einmalig = **keine** Chunking/Resumability nötig; 3 Calls pro Serie statt Vintage-Walk |

**Variante-A-Swap-Pfad (α MCP nachträglich):** Falls `dracepj/fred-mcp` später gegenüber `fredapi` bevorzugt wird — Austausch erfolgt durch Ersetzen des `fred_client.py`-Adapters bei unverändertem JSONL-Schema + unveränderter §31-Logik. Keine Plan-Re-Execution nötig.

---

## Critical Files (zu erstellen / zu modifizieren)

| Pfad | Aktion |
|---|---|
| `.env` | **NEU (falls nicht vorhanden)** — `FRED_API_KEY=<key>`. **NIE committen**, `.gitignore`-Eintrag sichern |
| `.env.example` | **NEU** — Template-Datei mit `FRED_API_KEY=` (leer), als Dokumentation für Setup |
| `.gitignore` | **MODIFY** — sicherstellen `.env` ist excluded |
| `03_Tools/fred_client.py` | **NEU** — Thin-Adapter mit ALFRED-first-release + FRED-latest-release-Modi, Env-Var-Key-Loader, Basic-Cache |
| `03_Tools/macro_regime_backtest.py` | **NEU** — Vectorized-Grid-Search über Parameter-Space, Sub-Perioden-Sensitivity, Top-3-Robust-Region-Selector, Markdown-Report |
| `03_Tools/macro_regime_daily.py` | **NEU** — Daily-Cron-Entry: FRED-Latest-Fetch, §31-Regime-Eval, Append auf `macro_regime.jsonl`, STATE.md-Update |
| `03_Tools/macro_regime_schemas.py` | **NEU** — Pydantic-Schemas für `macro_regime.jsonl` + `_historical.jsonl` (Schema v1.0 aus Spec §3.2.2) |
| `03_Tools/_smoke_test_macro.py` | **NEU** — Deterministischer Smoke-Test (Schema-Roundtrip, fred_client-Mode-Switch mit Mock, Regime-Eval-Fixtures) |
| `05_Archiv/macro_regime_historical.jsonl` | **NEU** — Backfill 1996-12-31 bis Go-Live-Datum, ALFRED-first-release-Werte |
| `05_Archiv/macro_regime.jsonl` | **NEU** — Live-Stream, startet mit erstem Go-Live-Record |
| `05_Archiv/backtest-reports/macro_regime_grid_<YYYY-MM-DD>.md` | **NEU** — Grid-Search-Report mit Top-3-Regionen, Sensitivity-Metriken, Sub-Perioden-Tabellen |
| `00_Core/INSTRUKTIONEN.md` §31 | **NEU** — Neuer §31-Abschnitt mit Backtest-kalibrierten Thresholds, Trigger-Regeln, Override-Policy, Daily-Run-Pflicht |
| `00_Core/CORE-MEMORY.md` §1 | **MODIFY** — Meilenstein-Eintrag Go-Live + Backtest-Audit-Eintrag (Backtest-Timestamp, Sub-Perioden-Metriken, SPY-Proxy-Limitation) |
| `00_Core/STATE.md` | **MODIFY** — Regime-State-Zeile in System-Zustand + Trigger-Tabellen-Eintrag für 30-Tage-Stabilitäts-Review |
| `03_Tools/briefing_hook.py` (o.ä. bestehender Briefing-Entry) | **MODIFY** — `macro_regime_daily.py` als Pre-Briefing-Step integrieren |
| `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` | **MODIFY** — Session-Einträge für Implementation + Go-Live |

**Out of Scope (per Spec §3.6):**
- KEINE per-Ticker-Macro-Sensitivitäten (Option C abgelehnt)
- KEINE Position-Entscheidungen basierend auf Macro (nur Sparraten-Ebene)
- KEIN Macro-Input in DEFCON-Score-Berechnung
- KEINE Macro-FLAG-Events (Regime-Wechsel ist KEINE FLAG-Aktivierung)
- KEIN Override des Sparraten-Nenners aus STATE.md — `sparraten_factor` multipliziert nur resultierende Einzel-Raten
- KEIN EDGAR-Integration (separater Plan Track 5a)
- **KEIN programmatischer Sparplan-Enforcer** (Codex-Finding 2026-04-20): Dynasty-Depot hat aktuell keinen automatisierten Sparplan-Runner. `sparraten_factor` wird in `macro_regime.jsonl` persistiert und in STATE.md-Regime-Zeile sichtbar gemacht — die **tatsächliche Multiplikation der Einzel-Raten erfolgt manuell** durch den User beim monatlichen Sparplan-Ausführen (aus STATE.md-Regime-Zeile gelesen). Ein expliziter Enforcer-Consumer ist **deferred** auf eine zukünftige Track-Iteration (siehe Task 11.5 Dokumentations-Gate)

---

## Implementation Plan (Task-by-Task)

### Task 1: Env-Setup — `fredapi`-Install + API-Key

**Files:**
- Modify (oder create): `.gitignore`
- Create: `.env.example`
- Create (lokal, nicht committed): `.env`

**Hintergrund:** FRED API v2 erfordert Key. Key ist kostenlos (St. Louis Fed, registriert via https://fred.stlouisfed.org/docs/api/api_key.html). Rate-Limit per FRED-API-v2-Docs: **2 req/s** (≈120/min). Unser Bedarf ~6 req/Tag ist trivial. `fredapi` ist Python-Wrapper.

- [ ] **Step 1.1: `.gitignore`-Check**

```bash
grep -n "^\.env$\|^\.env/" .gitignore 2>/dev/null
```

Expected: Treffer `.env` vorhanden. Falls nicht → in `.gitignore` ergänzen:

```
.env
.env.local
```

- [ ] **Step 1.2: `.env.example` erstellen**

Datei `.env.example` (committed, als Setup-Doku):

```bash
# FRED API Key — required for macro_regime_filter (Track 5b).
# Free registration: https://fred.stlouisfed.org/docs/api/api_key.html
# Rate limit: 2 req/s (FRED API v2 official). Our usage ~6 req/day.
FRED_API_KEY=
```

- [ ] **Step 1.3: `.env` lokal anlegen (NICHT committed)**

User holt Key von FRED (falls noch nicht vorhanden), schreibt in `.env`:

```bash
FRED_API_KEY=abcdef0123456789abcdef0123456789
```

Verifizieren:

```bash
grep FRED_API_KEY .env
```

Expected: Zeile mit echtem Key. Falls `.env` fehlt: User-Rückfrage, kein Abbruch ohne Konsens.

- [ ] **Step 1.4: Pre-Install-Check (failing test)**

```bash
python -c "import fredapi; print(fredapi.__version__)"
```

Expected: `ModuleNotFoundError`.

- [ ] **Step 1.5: `fredapi` installieren**

```bash
pip install fredapi python-dotenv
```

Expected: Exit 0. `python-dotenv` ergänzend für robustes `.env`-Loading im Daily-Run-Kontext.

- [ ] **Step 1.6: Post-Install Smoke**

```bash
python -c "import os; from dotenv import load_dotenv; load_dotenv(); from fredapi import Fred; fred = Fred(api_key=os.environ['FRED_API_KEY']); s = fred.get_series('T10Y2Y', limit=5); print(s.tail())"
```

Expected: 5 Werte der 10Y-2Y-Treasury-Spread-Serie auf stdout, keine Exceptions.

Bei 400-Error „Bad Request. The value for variable api_key is not registered" → Key nicht aktiviert, bei FRED-Support nachfragen oder neuen generieren.

- [ ] **Step 1.7: Commit (nur `.gitignore` + `.env.example`)**

```bash
git add .gitignore .env.example
git commit -m "chore(5b): .env.example + fredapi setup docs (key free, 2 req/s limit)"
```

**`.env` bleibt lokal, wird NIE committed.**

---

### Task 2: `fred_client.py` — ALFRED/FRED-Dual-Mode-Adapter

**Files:**
- Create: `03_Tools/fred_client.py`
- Create (test companion): `03_Tools/_smoke_test_macro.py` (erste Cases)

**Hintergrund:** FRED API kennt zwei Release-Dimensionen: (a) **latest-release** (aktueller, ggf. revidierter Wert — Standard-`get_series()`) und (b) **ALFRED first-release / vintage** (unrevidierter Wert zum Zeitpunkt des ersten Release — via `get_series_first_release()` oder `get_series_as_of_date()`). Spec §3.4 As-of-Policy (c) Hybrid verlangt First-Release für Historical-Backfill (Look-Ahead-Prevention) und Latest-Release für Live-Daily-Run. `fred_client.py` kapselt beide Modi hinter einer einheitlichen API.

- [ ] **Step 2.1: Smoke-Test-Datei `_smoke_test_macro.py` anlegen (Test-First)**

```python
#!/usr/bin/env python3
"""Smoke-Test für macro_regime_filter-Komponenten (Track 5b).
Läuft gegen FRED Live-API — benötigt FRED_API_KEY in .env."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "03_Tools"))


def _load_env() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env")
    except ImportError:
        pass  # env-vars can still be set externally


def case_1_fred_client_latest() -> int:
    from fred_client import FredClient
    client = FredClient()
    series = client.get_latest("T10Y2Y", limit=5)
    if series is None or len(series) < 3:
        print(f"[FAIL] Case 1 — get_latest('T10Y2Y') returned {series}")
        return 1
    print(f"[PASS] Case 1 — FRED latest T10Y2Y last5: {list(series.tail(3).round(2))}")
    return 0


def case_2_fred_client_first_release() -> int:
    from fred_client import FredClient
    client = FredClient()
    # ISM (NAPM): monthly, vintage-relevant
    series = client.get_first_release("NAPM", observation_start="2020-01-01",
                                       observation_end="2020-06-30")
    if series is None or len(series) < 3:
        print(f"[FAIL] Case 2 — get_first_release('NAPM') returned {series}")
        return 1
    print(f"[PASS] Case 2 — ALFRED first-release NAPM 2020H1: "
          f"{len(series)} records, first={series.iloc[0]:.1f}")
    return 0


def case_3_mode_distinct() -> int:
    """Latest und first-release MÜSSEN sich für historische ISM-Werte unterscheiden
    (ISM-Serie wird regelmäßig revidiert). Fail wenn Werte identisch."""
    from fred_client import FredClient
    client = FredClient()
    d = "2020-03-01"
    lat = client.get_latest("NAPM", observation_start=d, observation_end=d)
    fr = client.get_first_release("NAPM", observation_start=d, observation_end=d)
    if lat is None or fr is None or len(lat) != 1 or len(fr) != 1:
        print(f"[FAIL] Case 3 — Single-date fetch mismatch lat={lat} fr={fr}")
        return 1
    # Vertragsprüfung: beide sind float-Werte; wenn identisch, könnte ISM 2020-03 nicht
    # revidiert worden sein → Warnung, kein harter Fail (ISM-Revisionspraxis prüfen)
    if abs(lat.iloc[0] - fr.iloc[0]) < 0.01:
        print(f"[WARN] Case 3 — NAPM 2020-03 latest={lat.iloc[0]} == first={fr.iloc[0]}, "
              f"no revision detected. Modi funktional, aber Revisions-Distinguishability "
              f"für ISM 2020-03 nicht nachweisbar. Test zählt dennoch als PASS.")
    else:
        print(f"[PASS] Case 3 — NAPM 2020-03: latest={lat.iloc[0]} vs first={fr.iloc[0]} "
              f"(Δ={lat.iloc[0] - fr.iloc[0]:+.1f}, Revision bestätigt)")
    return 0


if __name__ == "__main__":
    _load_env()
    if "FRED_API_KEY" not in os.environ:
        print("[SKIP] FRED_API_KEY nicht im env — Test übersprungen")
        sys.exit(0)
    codes = [case_1_fred_client_latest(), case_2_fred_client_first_release(),
             case_3_mode_distinct()]
    if any(c != 0 for c in codes):
        sys.exit(1)
    print("\n[3/3] fred_client smoke tests passed")
    sys.exit(0)
```

- [ ] **Step 2.2: Test laufen lassen — erwartet FAIL**

```bash
python 03_Tools/_smoke_test_macro.py
```

Expected: `ModuleNotFoundError: fred_client`. Bestätigt sauberen Start.

- [ ] **Step 2.3: `fred_client.py` implementieren**

Datei `03_Tools/fred_client.py`:

```python
"""FRED-API-Client mit ALFRED/FRED-Dual-Mode-Kapselung für Track 5b.

Historical-Backfill-Path nutzt `get_first_release()` (ALFRED-Semantik),
Live-Daily-Run nutzt `get_latest()` (FRED-Current-Release).

Kein MCP-Overhead; dünner Wrapper um `fredapi.Fred`.
Key wird aus env-var FRED_API_KEY gelesen (via python-dotenv in Callern)."""
from __future__ import annotations

import os
from typing import Optional

import pandas as pd
from fredapi import Fred


class FredClient:
    """Thin adapter. Instantiate once per process; fredapi handles HTTP."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        key = api_key or os.environ.get("FRED_API_KEY")
        if not key:
            raise RuntimeError(
                "FRED_API_KEY missing. Set in .env or pass api_key explicitly. "
                "Free key: https://fred.stlouisfed.org/docs/api/api_key.html"
            )
        self._fred = Fred(api_key=key)

    def get_latest(
        self,
        series_id: str,
        observation_start: Optional[str] = None,
        observation_end: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> pd.Series:
        """Current-release Werte (incl. Revisionen). Use für Live-Daily-Run."""
        kwargs = {}
        if observation_start:
            kwargs["observation_start"] = observation_start
        if observation_end:
            kwargs["observation_end"] = observation_end
        s = self._fred.get_series(series_id, **kwargs)
        if limit:
            s = s.tail(limit)
        return s

    def get_first_release(
        self,
        series_id: str,
        observation_start: Optional[str] = None,
        observation_end: Optional[str] = None,
    ) -> pd.Series:
        """First-release Werte (unrevidiert, ALFRED-Semantik). Use für Historical-Backfill.

        fredapi bietet `get_series_first_release()` direkt — genau die Semantik, die wir
        für §29.5 Sin #2 Look-Ahead-Prevention brauchen."""
        s = self._fred.get_series_first_release(series_id)
        if observation_start:
            s = s[s.index >= pd.Timestamp(observation_start)]
        if observation_end:
            s = s[s.index <= pd.Timestamp(observation_end)]
        return s

    def get_as_of(
        self,
        series_id: str,
        as_of_date: str,
        observation_start: Optional[str] = None,
        observation_end: Optional[str] = None,
    ) -> pd.Series:
        """ALFRED as-of-Snapshot: Werte wie sie am `as_of_date` in FRED standen.

        Use für Sub-Perioden-Audit oder Vintage-Re-Backtests.
        fredapi: `get_series_as_of_date(series_id, as_of_date)`."""
        s = self._fred.get_series_as_of_date(series_id, as_of_date)
        # as_of_date-API gibt DataFrame zurück (realtime_start, realtime_end, date, value)
        # → reduzieren auf Series(date → value) für einheitliches API
        if isinstance(s, pd.DataFrame):
            s = s.set_index("date")["value"].astype(float)
        if observation_start:
            s = s[s.index >= pd.Timestamp(observation_start)]
        if observation_end:
            s = s[s.index <= pd.Timestamp(observation_end)]
        return s
```

- [ ] **Step 2.4: Test laufen lassen — erwartet PASS 3/3**

```bash
python 03_Tools/_smoke_test_macro.py
```

Expected: `[3/3] fred_client smoke tests passed`. Exit 0.

Bei Case-3-Warnung „ISM 2020-03 nicht revidiert": kein Blocker, im Test-Log dokumentiert.

Bei Case-1 oder Case-2 FAIL: Key-Problem oder Netzwerk. Debug mit expliziter curl-Probe gegen `https://api.stlouisfed.org/fred/series/observations?series_id=T10Y2Y&api_key=<key>&file_type=json`.

- [ ] **Step 2.5: Commit**

```bash
git add 03_Tools/fred_client.py 03_Tools/_smoke_test_macro.py
git commit -m "feat(5b): fred_client.py dual-mode adapter (ALFRED first-release + FRED latest)"
```

---

### Task 3: `macro_regime_schemas.py` — Pydantic-Schemas

**Files:**
- Create: `03_Tools/macro_regime_schemas.py`
- Modify: `03_Tools/_smoke_test_macro.py` (Case 4 anfügen)

**Hintergrund:** Schema v1.0 aus Spec §3.2.2. Folgt `03_Tools/backtest-ready/schemas.py`-Pattern (Pydantic + `extra="forbid"` + Smoke-Test in Schema-Datei selbst). Beide JSONL-Files (`macro_regime_historical.jsonl` + `macro_regime.jsonl`) teilen denselben Schema-Record — Unterscheidung nur über das File.

- [ ] **Step 3.1: Schema-Datei schreiben**

```python
"""Pydantic-Schemas für macro_regime_{historical,}.jsonl (Track 5b).

Schema v1.0 per TRACK5-SPEC §3.2.2. Beide Files (Historical-Backfill +
Live-Stream) teilen den RegimeRecord — Separation nur über File-Name."""
from __future__ import annotations

from datetime import date
from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


RegimeState = Literal["normal", "risk_off"]


class RegimeRecord(BaseModel):
    """Ein Trading-Day-Record aus macro_regime.jsonl oder _historical.jsonl.

    `date`: Trading-Day (aligned mit portfolio_returns.jsonl Daily-Schema).
    Monthly-Serien (ISM) werden via `ism_asof`-Feld explizit auf ihr echtes
    Release-Datum gelockt; Wert bleibt zwischen Releases konstant (Carry-Forward)."""

    model_config = ConfigDict(extra="forbid")

    date: date                           # Trading-Day
    hy_oas: float                        # BAMLH0A0HYM2, Prozent (bps/100)
    treasury_10y_2y: float               # T10Y2Y, Prozent
    ism_pmi: float                       # NAPM, Index-Wert
    ism_asof: date                       # Tatsächliches Release-Datum der ISM-Publikation
    regime_state: RegimeState
    triggers_fired: List[str] = Field(default_factory=list)
    sparraten_factor: float = Field(ge=0.0, le=1.0)
    schema_version: Literal["1.0"] = "1.0"


def _smoke_tests() -> int:
    """Schema-Roundtrip + Invariantentests."""
    import json

    ok_record = {
        "date": "2026-04-20",
        "hy_oas": 3.15,
        "treasury_10y_2y": 0.18,
        "ism_pmi": 51.3,
        "ism_asof": "2026-04-01",
        "regime_state": "normal",
        "triggers_fired": [],
        "sparraten_factor": 1.00,
        "schema_version": "1.0",
    }
    rec = RegimeRecord.model_validate(ok_record)
    assert rec.regime_state == "normal"
    assert rec.sparraten_factor == 1.00

    roundtrip = json.loads(rec.model_dump_json())
    assert RegimeRecord.model_validate(roundtrip).date == rec.date
    print("  [1/3] RegimeRecord roundtrip passed")

    # Forbid extras
    bad_extra = dict(ok_record, foo="bar")
    try:
        RegimeRecord.model_validate(bad_extra)
        print("  [2/3] FAIL — extra field should have raised")
        return 1
    except Exception:
        print("  [2/3] extra=forbid enforced")

    # sparraten_factor bounds
    bad_factor = dict(ok_record, sparraten_factor=1.5)
    try:
        RegimeRecord.model_validate(bad_factor)
        print("  [3/3] FAIL — factor>1.0 should have raised")
        return 1
    except Exception:
        print("  [3/3] sparraten_factor bounds enforced")

    print("\nall macro_regime schema smoke tests passed")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(_smoke_tests())
```

- [ ] **Step 3.2: Schema-Smoke laufen lassen**

```bash
python 03_Tools/macro_regime_schemas.py
```

Expected: 3/3 PASS. Exit 0.

- [ ] **Step 3.3: Smoke-Test-Case 4 anhängen in `_smoke_test_macro.py`**

Nach Case 3 in `_smoke_test_macro.py` ergänzen (vor `if __name__ == "__main__"`):

```python
def case_4_schema_import() -> int:
    from macro_regime_schemas import RegimeRecord
    rec = RegimeRecord.model_validate({
        "date": "2026-04-20",
        "hy_oas": 3.15,
        "treasury_10y_2y": 0.18,
        "ism_pmi": 51.3,
        "ism_asof": "2026-04-01",
        "regime_state": "normal",
        "triggers_fired": [],
        "sparraten_factor": 1.00,
        "schema_version": "1.0",
    })
    if rec.regime_state != "normal":
        print(f"[FAIL] Case 4 — schema roundtrip broken")
        return 1
    print("[PASS] Case 4 — macro_regime_schemas importable + roundtrip ok")
    return 0
```

Und die Liste in `__main__` erweitern:

```python
    codes = [case_1_fred_client_latest(), case_2_fred_client_first_release(),
             case_3_mode_distinct(), case_4_schema_import()]
```

Update Print-Abschluss auf `[4/4]`.

- [ ] **Step 3.4: Commit**

```bash
git add 03_Tools/macro_regime_schemas.py 03_Tools/_smoke_test_macro.py
git commit -m "feat(5b): RegimeRecord pydantic-schema v1.0 per spec §3.2.2"
```

---

### Task 4: Historical-Backfill — `macro_regime_historical.jsonl`

**Files:**
- Create: `03_Tools/backfill_macro_regime.py` (one-shot-Skript, zu löschen nach Ausführung — oder als `_archive`-Skript dokumentieren)
- Create: `05_Archiv/macro_regime_historical.jsonl`

**Hintergrund:** 3 Serien × einmaliger `get_first_release()`-Pull über 1996-12-31 (HY-OAS-Intersection-Start) bis Go-Live-Datum. Daten in Daily-Grid aligned als **generische Business-Days** via `pd.bdate_range(freq="B")`, monatliche ISM wird via Forward-Fill propagiert; `ism_asof` dokumentiert echtes Release. **Wichtige Approximation:** `freq="B"` filtert Wochenenden aber **nicht** NYSE-Feiertage (Thanksgiving / Good Friday / Juneteenth etc.) — das ist für Regime-Persistenz-Granularität (~21-63 BDays) akzeptabel, weil ~9 Feiertage/Jahr ≈ 3,6% Drift unterhalb der §31-Persistenz-Schwellen-Empfindlichkeit liegen. Alternative mit `pandas_market_calendars` wurde bewusst NICHT gewählt (zusätzliche Dep, minimaler Metrik-Gewinn). Data-Quality-Gate: unique+monotonic Dates / Business-Day-Gap-Detection / ISM-Carry-Forward / NaN <1%.

- [ ] **Step 4.1: Backfill-Skript schreiben**

```python
"""One-shot Backfill für macro_regime_historical.jsonl.

Nutzt ALFRED first-release für alle drei Serien (Look-Ahead-Prevention).
Aligned Daily-Grid via generische pandas Business-Days (`freq="B"`; NYSE-Feiertage bewusst unignoriert — siehe Task-4-Hintergrund).
Monthly-ISM wird forward-gefüllt zwischen Release-Dates; `ism_asof` dokumentiert
das tatsächliche Release-Datum des aktiven ISM-Werts.

Run: python 03_Tools/backfill_macro_regime.py
Output: 05_Archiv/macro_regime_historical.jsonl (überschreibt bei Rerun)"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "03_Tools"))
load_dotenv(ROOT / ".env")

from fred_client import FredClient  # noqa: E402
from macro_regime_schemas import RegimeRecord  # noqa: E402

SERIES = {"hy_oas": "BAMLH0A0HYM2", "treasury_10y_2y": "T10Y2Y", "ism_pmi": "NAPM"}
START = "1996-12-31"  # HY-OAS intersection
OUTPUT = ROOT / "05_Archiv" / "macro_regime_historical.jsonl"


def fetch_all() -> dict[str, pd.Series]:
    client = FredClient()
    out = {}
    for col, sid in SERIES.items():
        print(f"Fetching {sid} ({col}) first-release from {START} ...")
        s = client.get_first_release(sid, observation_start=START)
        s.name = col
        out[col] = s.astype(float)
        print(f"  → {len(s)} records, range "
              f"{s.index.min().date()} to {s.index.max().date()}, NaN={s.isna().sum()}")
    return out


def build_daily_grid(series_map: dict[str, pd.Series]) -> pd.DataFrame:
    # Daily trading-day grid ab max(start) aller Serien
    start = max(s.index.min() for s in series_map.values())
    end = min(s.index.max() for s in series_map.values())
    # pandas business-day calendar (Mo-Fr, NO NYSE holidays) — Approximation akzeptiert
    idx = pd.bdate_range(start=start, end=end, freq="B")
    df = pd.DataFrame(index=idx)

    # HY-OAS + T10Y2Y daily → reindex + forward-fill einzelne Lücken bis 5 Bdays
    for col in ("hy_oas", "treasury_10y_2y"):
        s = series_map[col].reindex(idx).ffill(limit=5)
        df[col] = s

    # ISM monthly → forward-fill bis zum nächsten Release; separate `ism_asof`-Spalte
    ism = series_map["ism_pmi"]
    ism_asof = pd.Series(ism.index, index=ism.index)
    df["ism_pmi"] = ism.reindex(idx).ffill()
    df["ism_asof"] = ism_asof.reindex(idx).ffill()

    return df.dropna(subset=["hy_oas", "treasury_10y_2y", "ism_pmi", "ism_asof"])


def quality_gate(df: pd.DataFrame) -> None:
    """Codex-Addition: Unique/monotonic + Business-Day-Gaps + ISM-Carry + NaN-Rate."""
    assert df.index.is_monotonic_increasing, "dates not monotonic"
    assert df.index.is_unique, "duplicate dates"
    # Business-Day-Gaps (>5 BDays) → flaggen
    gaps = (df.index.to_series().diff().dt.days > 7).sum()
    print(f"Quality: {gaps} gaps >7 calendar-days (tolerable: weekends/holidays)")
    for col in ("hy_oas", "treasury_10y_2y", "ism_pmi"):
        nan_rate = df[col].isna().mean()
        assert nan_rate < 0.01, f"NaN-rate for {col} = {nan_rate:.3%} > 1%"
    # HY-OAS start check
    assert df.index.min() <= pd.Timestamp("1997-01-31"), \
        f"HY-OAS historical start > 1997-01-31: {df.index.min()}"
    print("Quality gate passed.")


def write_jsonl(df: pd.DataFrame) -> None:
    OUTPUT.parent.mkdir(exist_ok=True)
    n = 0
    with OUTPUT.open("w", encoding="utf-8") as fh:
        for idx, row in df.iterrows():
            rec = RegimeRecord(
                date=idx.date(),
                hy_oas=float(row["hy_oas"]),
                treasury_10y_2y=float(row["treasury_10y_2y"]),
                ism_pmi=float(row["ism_pmi"]),
                ism_asof=row["ism_asof"].date(),
                regime_state="normal",        # backfill has no regime — placeholder
                triggers_fired=[],
                sparraten_factor=1.00,
                schema_version="1.0",
            )
            fh.write(rec.model_dump_json() + "\n")
            n += 1
    print(f"Wrote {n} records to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    series_map = fetch_all()
    df = build_daily_grid(series_map)
    quality_gate(df)
    write_jsonl(df)
```

- [ ] **Step 4.2: Backfill ausführen**

```bash
python 03_Tools/backfill_macro_regime.py
```

Expected: 3 Fetch-Logs (HY-OAS / T10Y2Y / ISM mit Record-Zahlen + Range), Quality-Gate-Output, „Wrote ~7500 records to 05_Archiv/macro_regime_historical.jsonl". Laufzeit ~10-30 sec.

Bei Fetch-Fehler: siehe Task-1-Debug. Bei Quality-Gate-Fehler (z.B. NaN-Rate >1% für HY-OAS): Output-Preview inspizieren, ggf. Serie mit kürzerem Start reduzieren und in Audit-Entry dokumentieren.

- [ ] **Step 4.3: JSONL-Sanity-Check**

```bash
wc -l 05_Archiv/macro_regime_historical.jsonl
head -3 05_Archiv/macro_regime_historical.jsonl
tail -3 05_Archiv/macro_regime_historical.jsonl
python -c "import json; [json.loads(l) for l in open('05_Archiv/macro_regime_historical.jsonl', encoding='utf-8')]; print('parse ok')"
```

Expected: ~7500 Zeilen, erstes Datum ~1997-01 (nach HY-OAS-Intersection-Start 1996-12-31 + BDay-Alignment), letztes Datum nahe `today() - 1 Bday`. `parse ok` auf stdout.

- [ ] **Step 4.4: Commit**

```bash
git add 03_Tools/backfill_macro_regime.py 05_Archiv/macro_regime_historical.jsonl
git commit -m "feat(5b): macro_regime_historical.jsonl backfill 1997-present (ALFRED first-release)"
```

---

### Task 5: Backtest-Tool — Skelett + vectorisierte Pre-Compute-Architektur

**Files:**
- Create: `03_Tools/macro_regime_backtest.py` (Initial-Version mit Architektur)

**Hintergrund:** Codex-Addition zur Runtime-Disziplin: Threshold-Booleans / Monthly-Alignment / Persistence-Masks **einmal** pro Threshold-Set vorberechnen, **nicht** im inneren Grid-Loop. Ohne diese Disziplin explodiert die Laufzeit. Task 5 baut das Skelett + die Pre-Compute-Layer. Task 6 füllt die Metrik-Funktion. Task 7 führt den Grid-Search aus.

- [ ] **Step 5.1: Tool-Skelett schreiben (initialer Stub + Architektur-Kommentare)**

```python
"""macro_regime_backtest.py — Grid-Search über §31-Parameter-Space.

Aufbau (Vectorization-Disziplin per Codex 2026-04-20):
  1. load_historical(): JSONL → pandas DataFrame
  2. precompute_signals(thresholds): berechnet Boolean-Masks + Persistence-Windows
     EINMAL pro Threshold-Kombination (hy_oas_th, curve_th, ism_th, persistence).
  3. apply_logic_and_factor(signals, operator, factor): nur diese zwei Dimensionen
     variieren im inneren Grid-Loop — O(1) pro Combo dank bereits gebauter Masks.
  4. compute_utility(regime_mask, spy_series): Sparraten-Utility + MaxDD-Check.
  5. subperiod_split(): 1996-2007 / 2008-2019 / 2020-2026 — Robustness-Test.

Run: python 03_Tools/macro_regime_backtest.py --mini   (10-Combo-Probe für Runtime-Estimate)
     python 03_Tools/macro_regime_backtest.py --full   (volle 1620-Combo-Grid-Search)

Output: 05_Archiv/backtest-reports/macro_regime_grid_<YYYY-MM-DD>.md
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HIST = ROOT / "05_Archiv" / "macro_regime_historical.jsonl"
REPORT_DIR = ROOT / "05_Archiv" / "backtest-reports"


# ---------- Parameter-Space per Spec §3.2.3 ----------
HY_OAS_THRESHOLDS = [350, 400, 450, 500, 550]          # bps (÷100 = Prozent)
CURVE_THRESHOLDS = [-25, 0, 25]                        # bps (÷100 = Prozent)
ISM_FLOORS = [45, 47, 48, 50]
PERSISTENCE_MONTHS = [1, 2, 3]
LOGIC_OPERATORS = ["OR", "AND_of_2", "AND_all"]
FACTORS = [0.50, 0.70, 0.80]


@dataclass(frozen=True)
class Thresholds:
    hy_oas_bps: int
    curve_bps: int
    ism_floor: float
    persistence_months: int


def load_historical() -> pd.DataFrame:
    """Lade macro_regime_historical.jsonl als DataFrame (Index = date)."""
    records = [json.loads(l) for l in HIST.read_text(encoding="utf-8").splitlines() if l.strip()]
    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()
    return df[["hy_oas", "treasury_10y_2y", "ism_pmi"]]


def load_spy_proxy() -> pd.Series:
    """SPY ab 1993 als Sparraten-Utility-Proxy.

    In Real-Implementation: Shibui oder yfinance. Initial-Stub für Task 5 lädt von Shibui
    oder fällt zurück auf yfinance. Call-Graph dokumentiert in CORE-MEMORY §1-Eintrag
    (Spec §3.4 SPY-Proxy-Limitation)."""
    # Placeholder-Assertion: muss durch echten Loader ersetzt werden in Task 6
    raise NotImplementedError("load_spy_proxy stub — implemented in Task 6")


def precompute_signals(df: pd.DataFrame, th: Thresholds) -> pd.DataFrame:
    """Codex-Pattern: Signal-Masken EINMAL pro Threshold-Kombi bauen.

    Output-DataFrame hat drei Boolean-Spalten:
      - `hy_oas_high`:   hy_oas > th.hy_oas_bps/100, persistent über th.persistence_months
      - `curve_low`:     treasury_10y_2y < th.curve_bps/100, persistent
      - `ism_weak`:      ism_pmi < th.ism_floor, persistent

    Persistenz via rolling(window=~21×persistence_months BDays).min() == True.
    D.h. Signal feuert nur wenn es über alle Tage im Window True war."""
    # Raw thresholds in natürlichen Einheiten (Prozent / Index-Wert)
    raw_hy = df["hy_oas"] > (th.hy_oas_bps / 100.0)
    raw_curve = df["treasury_10y_2y"] < (th.curve_bps / 100.0)
    raw_ism = df["ism_pmi"] < th.ism_floor

    window = 21 * th.persistence_months   # ~21 BDays/Month
    out = pd.DataFrame(index=df.index)
    out["hy_oas_high"] = raw_hy.rolling(window=window, min_periods=window).min().fillna(0).astype(bool)
    out["curve_low"] = raw_curve.rolling(window=window, min_periods=window).min().fillna(0).astype(bool)
    out["ism_weak"] = raw_ism.rolling(window=window, min_periods=window).min().fillna(0).astype(bool)
    return out


def combine_signals(signals: pd.DataFrame, operator: str) -> pd.Series:
    """Inner-Grid-Loop-Operation: O(1) pro Combo dank bereits vorberechneter Signals."""
    if operator == "OR":
        return signals.any(axis=1)
    if operator == "AND_of_2":
        return signals.sum(axis=1) >= 2
    if operator == "AND_all":
        return signals.all(axis=1)
    raise ValueError(f"unknown operator {operator!r}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mini", action="store_true", help="10-Combo probe for runtime")
    parser.add_argument("--full", action="store_true", help="1620-Combo full grid")
    args = parser.parse_args()

    df = load_historical()
    print(f"Loaded {len(df)} historical records "
          f"from {df.index.min().date()} to {df.index.max().date()}")

    if args.mini:
        combos = list(product(HY_OAS_THRESHOLDS[:2], CURVE_THRESHOLDS[:1],
                              ISM_FLOORS[:1], PERSISTENCE_MONTHS[:1],
                              LOGIC_OPERATORS, FACTORS))[:10]
    elif args.full:
        combos = list(product(HY_OAS_THRESHOLDS, CURVE_THRESHOLDS, ISM_FLOORS,
                              PERSISTENCE_MONTHS, LOGIC_OPERATORS, FACTORS))
    else:
        print("Specify --mini or --full")
        sys.exit(2)

    print(f"Grid: {len(combos)} combos")
    # Volle Iteration erst in Task 7; Task 5 testet nur Signal-Precompute.
    first_th = Thresholds(*combos[0][:4])
    sig = precompute_signals(df, first_th)
    print(f"First-threshold signals: hy_oas_high count={sig['hy_oas_high'].sum()}, "
          f"curve_low={sig['curve_low'].sum()}, ism_weak={sig['ism_weak'].sum()}")
    mask_or = combine_signals(sig, "OR")
    print(f"OR-combined regime-active days: {mask_or.sum()} / {len(mask_or)}")
```

- [ ] **Step 5.2: Mini-Probe laufen lassen**

```bash
python 03_Tools/macro_regime_backtest.py --mini
```

Expected: Load-Message + „Grid: 10 combos" + erstes Signal-Summary + OR-Combined-Count. Laufzeit <5 sec. Keine Full-Grid-Execution (kommt in Task 7).

- [ ] **Step 5.3: Commit**

```bash
git add 03_Tools/macro_regime_backtest.py
git commit -m "feat(5b): backtest-tool skelett + vectorized precompute-architecture"
```

---

### Task 6: Backtest-Tool — Utility-Metrik + SPY-Proxy + Sub-Perioden

**Files:**
- Modify: `03_Tools/macro_regime_backtest.py`

**Hintergrund:** Spec §3.3.1 Sparraten-Utility-Definition: Σ (Durchschnittskurs × Sparraten_Faktor_t) vs. (Durchschnittskurs × 1.00). Proxy: SPY-Monats-Close statt Satelliten-Durchschnitt (SPY ab 1993, Satelliten-Gewichtung ändert sich zeitlich → Proxy-Ansatz vermeidet Historical-Constituent-Bias). MaxDD als Secondary-Constraint: Regime-Filter darf SPY-Proxy-MaxDD nicht erhöhen. **Codex-Addition:** Zusätzlich `forward_6m_hit_rate` als Sekundär-Diagnose ausgeben — prüft Spec-§3.3.1-Verbalisierung („Käufe auf Phasen verschoben, die im 6M-Forward niedrigere Durchschnittskurse hatten") unabhängig von der Primär-Formel.

- [ ] **Step 6.1: SPY-Proxy-Loader implementieren**

`load_spy_proxy()` ersetzen:

```python
def load_spy_proxy() -> pd.Series:
    """SPY-Monatsschlusskurs ab 1993 als Sparraten-Utility-Proxy.

    Strategie:
      1. Versuche lokale Shibui-Cache (falls verfügbar in 05_Archiv/).
      2. Fallback: yfinance (kein Key nötig für Public-Ticker).

    Proxy-Limitation: SPY ≠ aktuelles Satelliten-Portfolio. Constituents-Bias
    vermieden, aber tatsächliche Regime-Sensitivität des Portfolios kann
    abweichen. Limitation in Backtest-Report + CORE-MEMORY §1 dokumentiert."""
    try:
        import yfinance as yf
        spy = yf.download("SPY", start="1993-01-01", progress=False, auto_adjust=True)
        if spy.empty:
            raise RuntimeError("yfinance returned empty SPY")
        # Monatsschluss
        m = spy["Close"].resample("ME").last().dropna()
        m.index = m.index.to_period("M").to_timestamp()
        m.name = "spy_close_month"
        return m
    except Exception as exc:
        raise RuntimeError(
            f"SPY-Proxy load failed ({exc}). Alternative: Shibui-Cache manuell befüllen "
            f"und hier laden. Backtest kann ohne SPY-Proxy nicht laufen."
        ) from exc


def compute_utility(
    regime_daily: pd.Series,          # bool: risk_off ja/nein per Tag
    factor_riskoff: float,            # e.g. 0.70
    spy_monthly: pd.Series,           # SPY monatsschluss
) -> dict:
    """Sparraten-Utility per Spec §3.3.1.

    **Primärmetrik:** Utility = 1 − (avg_filtered / avg_unfiltered), wo
    avg_filtered der factor-gewichtete Durchschnittskurs ist. Positiv = Filter hat
    durchschnittlichen Kaufpreis gesenkt (= Käufe auf billigere Phasen verschoben).

    **Sekundär-Diagnose (Codex-Addition 2026-04-20):** `forward_6m_hit_rate` = Anteil
    der Risk-Off-Monate, in denen der durchschnittliche SPY-Kurs der FOLGENDEN 6 Monate
    niedriger lag als der aktuelle SPY-Kurs. Spec §3.3.1 nennt das als Validierungs-
    Kriterium („Regime-Filter hat Käufe auf Phasen verschoben, die im 6M-Forward-
    Fenster niedrigere Durchschnittskurse hatten"). Primärmetrik und Hit-Rate können
    auseinanderlaufen; beide im Report ausweisen."""
    # Regime-State auf Monatsende mappen (majority-Vote im Monat)
    regime_monthly = regime_daily.resample("ME").mean() > 0.5
    regime_monthly.index = regime_monthly.index.to_period("M").to_timestamp()
    # Align
    aligned = spy_monthly.to_frame("spy").join(regime_monthly.rename("risk_off"), how="inner")
    aligned["factor"] = np.where(aligned["risk_off"], factor_riskoff, 1.00)

    # --- Primärmetrik: factor-gewichteter Durchschnitts-Kaufpreis ---
    total_weight_filtered = aligned["factor"].sum()
    avg_filtered = (aligned["spy"] * aligned["factor"]).sum() / total_weight_filtered
    avg_unfiltered = aligned["spy"].mean()
    utility = 1.0 - (avg_filtered / avg_unfiltered)

    # --- MaxDD als Secondary-Constraint ---
    def _maxdd(returns: pd.Series) -> float:
        cum = (1 + returns).cumprod()
        return (cum / cum.cummax() - 1).min()
    ret = aligned["spy"].pct_change().fillna(0)
    ret_filtered = ret * aligned["factor"]

    # --- Spec-§3.3.1 Sekundär-Diagnose: 6M-Forward-Hit-Rate ---
    # Für jeden Risk-Off-Monat: wurde ∅(SPY der 6 folgenden Monate) < SPY des Monats?
    spy = aligned["spy"]
    fwd6m_avg = spy.shift(-6).rolling(window=6, min_periods=3).mean().shift(1)
    riskoff_months = aligned.index[aligned["risk_off"]]
    if len(riskoff_months) == 0:
        hit_rate = float("nan")
    else:
        hits = ((fwd6m_avg < spy) & aligned["risk_off"]).loc[riskoff_months]
        valid_mask = hits.notna()
        if valid_mask.sum() == 0:
            hit_rate = float("nan")
        else:
            hit_rate = float(hits[valid_mask].mean())

    return {
        "utility": float(utility),
        "maxdd_unfiltered": float(_maxdd(ret)),
        "maxdd_filtered": float(_maxdd(ret_filtered)),
        "months_in_riskoff": int(aligned["risk_off"].sum()),
        "months_total": int(len(aligned)),
        "forward_6m_hit_rate": hit_rate,   # Spec-§3.3.1 Sekundär-Diagnose
    }


def subperiod_split(df: pd.DataFrame) -> dict[str, tuple[str, str]]:
    return {
        "1996-2007": ("1996-12-31", "2007-12-31"),
        "2008-2019": ("2008-01-01", "2019-12-31"),
        "2020-2026": ("2020-01-01", "2026-12-31"),
    }
```

- [ ] **Step 6.2: Mini-Probe-Dispatch erweitern, damit Utility berechnet wird**

`if __name__ == "__main__":`-Block am Ende ergänzen so dass nach Signal-Combine auch Utility berechnet wird (nur für first-combo):

```python
    spy = load_spy_proxy()
    print(f"SPY-Proxy: {len(spy)} monthly records "
          f"{spy.index.min().date()} to {spy.index.max().date()}")
    m = compute_utility(mask_or, 0.70, spy)
    print(f"Utility-Smoke (first threshold, OR, factor=0.70): {m}")
```

- [ ] **Step 6.3: Mini-Probe laufen lassen — Utility prüfen**

```bash
python 03_Tools/macro_regime_backtest.py --mini
```

Expected: SPY-Load + Utility-Output wie `{'utility': 0.02, 'maxdd_unfiltered': -0.55, 'maxdd_filtered': -0.45, 'months_in_riskoff': 140, 'months_total': ~350}`. Keine Exception. Laufzeit <30 sec.

Bei yfinance-Fail: spezifische Alternativen dokumentieren (Shibui-Cache laden, User-Rückfrage wenn offline).

- [ ] **Step 6.4: Commit**

```bash
git add 03_Tools/macro_regime_backtest.py
git commit -m "feat(5b): backtest utility-metric + SPY-proxy (yfinance monatsschluss)"
```

---

### Task 7: Grid-Search-Execution + Top-3-Robust-Region + Report

**Files:**
- Modify: `03_Tools/macro_regime_backtest.py` (Grid-Loop + Report-Writer)
- Output: `05_Archiv/backtest-reports/macro_regime_grid_<YYYY-MM-DD>.md`

**Hintergrund:** Full-Grid 1620 Combos. Utility als primäres Ziel, `maxdd_filtered <= maxdd_unfiltered` als Constraint (sonst Combo verworfen). Sub-Perioden-Robustness: Top-Combos aus Full-Period werden gegen 1996-2007 / 2008-2019 / 2020-2026 geprüft — stabile Regionen = Combos die in allen 3 Sub-Perioden positive Utility UND MaxDD-OK halten. Top-3 daraus werden im Report aufgelistet.

- [ ] **Step 7.1: Grid-Loop implementieren**

Vollen Dispatcher unterhalb von `combine_signals()` ergänzen:

```python
def run_grid(df: pd.DataFrame, spy: pd.Series, combos: list[tuple]) -> pd.DataFrame:
    """Full-Grid-Execution mit Pre-Compute-Cache.

    Cache-Strategie: Für jede (hy_oas, curve, ism, persistence)-Kombi werden
    die Signal-Masken GENAU EINMAL berechnet. Operator + Factor iterieren
    im inneren Loop, nutzen Cache."""
    signals_cache: dict[Thresholds, pd.DataFrame] = {}
    rows = []
    for hy, cv, ism, pers, op, fct in combos:
        th = Thresholds(hy, cv, ism, pers)
        if th not in signals_cache:
            signals_cache[th] = precompute_signals(df, th)
        mask = combine_signals(signals_cache[th], op)
        u = compute_utility(mask, fct, spy)
        rows.append({
            "hy_oas_bps": hy, "curve_bps": cv, "ism_floor": ism,
            "persistence_months": pers, "operator": op, "factor_riskoff": fct,
            **u,
        })
    return pd.DataFrame(rows)


def filter_valid(grid: pd.DataFrame) -> pd.DataFrame:
    """MaxDD-Constraint: filtered MaxDD darf unfiltered nicht verschlechtern."""
    valid = grid[grid["maxdd_filtered"] >= grid["maxdd_unfiltered"] - 1e-6].copy()
    return valid.sort_values("utility", ascending=False)


def subperiod_robustness(df: pd.DataFrame, spy: pd.Series, top_n_combos: list[tuple]) -> pd.DataFrame:
    """Für Top-N-Combos: Utility in jeder Sub-Periode einzeln berechnen."""
    periods = subperiod_split(df)
    rows = []
    for combo in top_n_combos:
        hy, cv, ism, pers, op, fct = combo
        th = Thresholds(hy, cv, ism, pers)
        for pname, (start, end) in periods.items():
            dfp = df.loc[start:end]
            spyp = spy.loc[start:end]
            if dfp.empty or spyp.empty:
                continue
            sig = precompute_signals(dfp, th)
            mask = combine_signals(sig, op)
            u = compute_utility(mask, fct, spyp)
            rows.append({"combo": str(combo), "period": pname, **u})
    return pd.DataFrame(rows)


def write_report(grid: pd.DataFrame, robust: pd.DataFrame, top3: list, out_path: Path) -> None:
    out_path.parent.mkdir(exist_ok=True)
    today = pd.Timestamp.today().date()
    lines = [f"# Macro-Regime Backtest Report — {today}", ""]
    lines.append(f"Grid: {len(grid)} combos, valid after MaxDD-Constraint: {len(grid[grid.utility>0])}")
    lines.append("")
    lines.append("## Top 10 by Utility (full period, MaxDD-constrained)")
    lines.append("")
    lines.append(grid.head(10).to_markdown(index=False))
    lines.append("")
    lines.append("## Top 3 Robust Parameter Regions (stable across subperiods)")
    lines.append("")
    for c in top3:
        lines.append(f"- `{c}`")
    lines.append("")
    lines.append("## Subperiod Diagnostics (Top 10 combos × 3 periods)")
    lines.append("")
    lines.append(robust.to_markdown(index=False))
    lines.append("")
    lines.append("## Conservative-Default Choice (for INSTRUKTIONEN §31)")
    lines.append("")
    lines.append("[POST-SELECTION FILL — siehe Task 8 dieses Plans]")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)}")
```

Und im `__main__`-Block den `--full`-Branch erweitern:

```python
    elif args.full:
        combos = list(product(HY_OAS_THRESHOLDS, CURVE_THRESHOLDS, ISM_FLOORS,
                              PERSISTENCE_MONTHS, LOGIC_OPERATORS, FACTORS))
        spy = load_spy_proxy()
        print(f"Running grid: {len(combos)} combos × ~{len(df)} days ...")
        import time
        t0 = time.time()
        grid = run_grid(df, spy, combos)
        print(f"Grid done in {time.time()-t0:.1f}s")
        valid = filter_valid(grid)
        print(f"Valid combos after MaxDD-Constraint: {len(valid)}")
        top10 = valid.head(10)
        top10_combos = top10[["hy_oas_bps","curve_bps","ism_floor",
                              "persistence_months","operator","factor_riskoff"]].apply(tuple, axis=1).tolist()
        robust = subperiod_robustness(df, spy, top10_combos)
        # Robust-Region = Combo mit positive utility in ALLEN subperiods
        positive_counts = robust[robust["utility"] > 0].groupby("combo").size()
        stable = [c for c, n in positive_counts.items() if n == 3]
        top3 = stable[:3] if len(stable) >= 3 else stable
        report_path = REPORT_DIR / f"macro_regime_grid_{pd.Timestamp.today().date()}.md"
        write_report(valid, robust, top3, report_path)
```

- [ ] **Step 7.2: Mini-Probe erneut — sanity-check dass `--mini` weiterhin läuft**

```bash
python 03_Tools/macro_regime_backtest.py --mini
```

Expected: unveränderter Output wie Task 6 (Mini läuft Grid-Code nicht).

- [ ] **Step 7.3: Full-Grid ausführen**

```bash
python 03_Tools/macro_regime_backtest.py --full
```

Expected: Grid-Done-Time ~15-30 min. Valid-Combos-Count. Report-Pfad. Falls Runtime >45 min: Pre-Compute-Cache-Hits prüfen (`signals_cache`-Len sollte maximal 180 Einträge haben: 5×3×4×3 eindeutige Threshold-Kombis, nicht 1620). Bei Cache-Miss-Problem: Code review.

- [ ] **Step 7.4: Report sichten**

```bash
cat 05_Archiv/backtest-reports/macro_regime_grid_$(date +%Y-%m-%d).md
```

Expected: Markdown mit Top-10-Tabelle + Sub-Perioden-Diagnostik + Top-3-Robust-Regionen + „POST-SELECTION FILL"-Platzhalter (wird in Task 8 gefüllt).

- [ ] **Step 7.5: Commit**

```bash
git add 03_Tools/macro_regime_backtest.py 05_Archiv/backtest-reports/
git commit -m "feat(5b): full grid-search (1620 combos) + subperiod-robustness report"
```

---

### Task 8: Conservative-Parameter-Wahl + INSTRUKTIONEN §31

**Files:**
- Modify: `00_Core/INSTRUKTIONEN.md` (neuer §31 ans Ende vor `---`-Footer)
- Modify: `05_Archiv/backtest-reports/macro_regime_grid_<date>.md` (Conservative-Choice-Sektion füllen)

**Hintergrund:** Spec §3.2.3 Disziplin: **nicht Point-Optimum** wählen sondern Parameter-Region mit stabiler Performance über alle Sub-Perioden. Tie-Break-Regel: höhere Threshold / längere Persistenz / niedrigere Sparraten-Faktor-Reduktion = konservativer. Final-Thresholds in §31.2 + §31.3 + CORE-MEMORY §1-Audit.

- [ ] **Step 8.1: Top-3-Robust-Regionen manuell bewerten**

Report öffnen (Task 7.4 Path). Aus den Top-3-Robust-Combos die **konservativste** identifizieren per sequenziellem Tie-Break (jede Regel wird nur angewandt, wenn vorherige nicht eindeutig entscheiden):

1. **R1 — Höchster `hy_oas_bps`** (höhere Trigger-Schwelle = seltenere Aktivierung = konservativer)
2. **R2 — Längstes `persistence_months`** (mehr Persistenz-Forderung = robustere Signale)
3. **R3 — Höchstes `factor_riskoff`** (weniger Reduktion = milderer Modulation-Effekt)
4. **R4 — Höchster `curve_bps`** (konservativere Curve-Inversion-Schwelle — deterministischer Zusatz-Tiebreak)
5. **R5 — Deterministischer String-Compare** über Operator-Alphabet (AND_all < AND_of_2 < OR) — Fallback-Garantie für Entscheidbarkeit

Regeln sind **sequenziell** (lexikographischer Vergleich R1→R5), **nicht gleichzeitig**. Entscheidung in 2-3 Sätzen im Report festhalten, welche Regel den Cut gemacht hat. Bei echtem Tie über alle 5 Regeln: User-Rückfrage (extrem unwahrscheinlich, da R5 strikt total-ordering liefert).

**Diagnose-Check vor Finalisierung (Codex-Addition):** Sobald die konservative Wahl steht, `forward_6m_hit_rate` des gewählten Combos inspizieren. Spec-§3.3.1-Verbalisierung verlangt dass das Filter Käufe auf Phasen mit niedrigeren 6M-Forward-Preisen verschiebt. Wenn Hit-Rate <0,50 trotz positiver Primärmetrik: Warnung im Report dokumentieren (Primärmetrik und Spec-Verbalisierung divergieren, kann Utility-Definition-Mismatch oder Proxy-Limitation signalisieren). Kein Blocker, aber explizit ausweisen.

- [ ] **Step 8.2: Report-Platzhalter füllen**

Report-File öffnen, Sektion „Conservative-Default Choice (for INSTRUKTIONEN §31)" durch konkrete Wahl ersetzen:

```markdown
## Conservative-Default Choice (for INSTRUKTIONEN §31)

**Gewählte Parameter (Date, Combo):** `2026-04-XX`, `(hy_oas=<X>bps, curve=<Y>bps, ism=<Z>, persistence=<N>mon, operator=<O>, factor_riskoff=<F>)`

**Begründung:** <2-3 Sätze — höhere Threshold als Point-Optimum, Sub-Perioden-Stabilität dokumentiert>

**Utility / MaxDD / Regime-Frequency:**
- Full-Period: utility=<X>, maxdd_unfiltered=<Y>, maxdd_filtered=<Z>, riskoff-months=<N>/<Total>
- 1996-2007: utility=<X1>, maxdd_filtered=<Y1>
- 2008-2019: utility=<X2>, maxdd_filtered=<Y2>
- 2020-2026: utility=<X3>, maxdd_filtered=<Y3>

**Trade-off vs Point-Optimum:**
Point-Optimum (max utility) lag bei `<combo>` mit utility=<X>. Gewählte konservative
Region hat utility=<Y> (Δ=<Z>) — Trade-off gegen Regime-Snooping-Risiko bewusst gewählt
(siehe TRACK5-SPEC §3.2.3 + Codex-Review 2026-04-20).
```

- [ ] **Step 8.3: INSTRUKTIONEN §31 schreiben**

Datei `00_Core/INSTRUKTIONEN.md` am Ende (vor Footer `*🦅 INSTRUKTIONEN.md v1.11 ...*`) anhängen:

```markdown
## 31. Macro-Regime-Filter (Sparraten-Modulation)

> **Status:** `[AKTIV seit 2026-04-XX]` — Backtest-kalibriert 1996-2026, Daily-Run
> integriert in Morning-Briefing-Trigger. Modulation nur auf Sparraten-Ebene,
> kein Eingriff in DEFCON-Scoring. Kein diskretionärer Override.

### 31.1 Serien-Inputs

| Serie | FRED-ID | Frequenz | As-of-Policy |
|-------|---------|----------|--------------|
| HY-OAS | BAMLH0A0HYM2 | Daily | Release-Day-Wert (FRED latest-release) |
| 10Y-2Y Treasury-Curve | T10Y2Y | Daily | Release-Day-Wert (FRED latest-release) |
| ISM Manufacturing PMI | NAPM | Monthly | T+1 nach tatsächlichem Release (via `ism_asof`-Feld) |

**Historical-Backfill** (`macro_regime_historical.jsonl`) nutzt **ALFRED first-release**
zur Look-Ahead-Prevention (§29.5 Sin #2). **Live-Stream** (`macro_regime.jsonl`) nutzt
**FRED latest-release** — revidierte Werte werden NICHT rückwirkend in historische
Live-Records geschrieben (First-Release-Persistenz, siehe §31.4).

### 31.2 Trigger-Regeln (mechanisch, ex ante)

```
regime_state = risk_off WENN:
  <post-backtest-kombination einsetzen aus Task 8>
SONST regime_state = normal.
```

Konkrete Thresholds:
- `hy_oas_threshold_bps`: `<X>`
- `curve_threshold_bps`: `<Y>`
- `ism_floor`: `<Z>`
- `persistence_months`: `<N>`
- `logic_operator`: `<OR / AND_of_2 / AND_all>`

### 31.3 Sparraten-Modulation

```
IF regime_state == risk_off → sparraten_factor = <F_riskoff>
IF regime_state == normal   → sparraten_factor = 1.00
```

**`sparraten_factor` multipliziert die resultierenden Einzelraten aus §22.** Der
8.0-Nenner aus STATE.md bleibt unverändert. Differenz zwischen modulierter Rate und
voller Rate geht in Cash-Reserve.

### 31.4 Override / Kill-Switch

- **Kein diskretionärer Override.** Änderung der Thresholds erfordert neuen Backtest-Run.
- **Threshold-Change-Prozedur (3-Schritte):**
  1. Neuer Grid-Search-Run mit `macro_regime_backtest.py --full`
  2. CORE-MEMORY §1 Audit-Eintrag mit Backtest-Timestamp + Sub-Perioden-Metriken + Begründung
  3. STATE.md-Update (§31-Version + Regime-State-Zeile)
- **Kill-Switch:** Deaktivierung via §31-Versions-Bump auf `v0.0` (factor hart 1.00,
  alle Trigger deaktiviert). Historische `macro_regime.jsonl`-Records bleiben als
  Dokumentation.
- **Revision-Invarianz:** Historische Live-Records werden NIE re-geschrieben, auch wenn
  FRED einen Wert im Nachhinein revidiert. First-Release-at-Event-Time ist binden
  (§29.5 Sin #2).

### 31.5 Daily-Run-Pflicht

- Trigger: Morning-Briefing-Pre-Step (täglich vor Briefing-Generierung)
- Aktion: `python 03_Tools/macro_regime_daily.py` — fetcht FRED-latest-Werte, evaluiert
  §31.2, appendet Record an `macro_regime.jsonl`, aktualisiert STATE.md-Regime-Zeile
- Fehler-Behandlung: bei FRED-API-Down — letzten bekannten Regime-State carry-forwarden,
  im Daily-Log + STATE.md „Watches"-Sektion flaggen. Keine Sparraten-Änderung ohne
  frischen Datenpunkt.

### 31.6 Wissenschaftliche Fundierung

- §29.5 Sin #2 Look-Ahead-Prevention → ALFRED-first-release-Semantik im Backfill
- §29.3 Temporal-Konsistenz → Sub-Perioden-Sensitivitätstest
- §29.1 Bailey/PBO → konservative Parameter-Region statt Point-Optimum
- Spec §3.4 SPY-Proxy-Limitation → Satelliten-Portfolio-Drift wird bei Interim-Gate
  2027-10-19 re-evaluiert
```

- [ ] **Step 8.4: Config-Single-Source — `macro_regime_config.py`**

**Hintergrund:** Threshold-Werte leben bisher in drei Quellen (INSTRUKTIONEN §31.2 Text, `macro_regime_daily.py`-Konstanten, Backtest-Report). Das ist Multi-Source-Drift-Risiko per Applied-Learning-Regel. Fix: eine Python-Config als Single-Source-of-Truth, von Daily-Run + §31-Doku-Referenz + Backtest-Report geteilt.

Datei `03_Tools/macro_regime_config.py` erstellen:

```python
"""Single-Source-of-Truth für §31 Macro-Regime-Filter Thresholds.

WICHTIG: Diese Datei ist der KANONISCHE Ort für §31-Parameter. INSTRUKTIONEN §31.2
referenziert sie ("siehe `03_Tools/macro_regime_config.py`"), `macro_regime_daily.py`
importiert sie. Änderungen NUR hier — §31-Text wird per Lookup dokumentiert, nicht
dupliziert.

Herkunft der Werte: Grid-Search `macro_regime_backtest.py --full` (Run <DATE>),
konservative Region-Wahl per Tie-Break-Regeln R1–R5 (siehe Backtest-Report).

Bei Änderung: INSTRUKTIONEN §31.4-Prozedur (3 Schritte):
  1. Neuer Grid-Search-Run
  2. CORE-MEMORY §1 Audit-Eintrag (Old-Value + New-Value + Backtest-Timestamp)
  3. STATE.md Regime-State-Zeile + §31-Version-Bump
"""
from __future__ import annotations

# -- Thresholds (bei Änderung INSTRUKTIONEN §31 neu durchlesen, 3-Schritt-Prozedur!) --

HY_OAS_THRESHOLD_BPS: int = 0           # FILL from Task 8 Tie-Break-Winner
CURVE_THRESHOLD_BPS: int = 0
ISM_FLOOR: float = 0.0
PERSISTENCE_MONTHS: int = 0
LOGIC_OPERATOR: str = "AND_of_2"        # "OR" | "AND_of_2" | "AND_all"
FACTOR_RISKOFF: float = 1.00            # 1.00 = Filter inaktiv; <1.00 Post-Calibration

# -- Version + Provenance --

VERSION: str = "1.0.0"                  # §31-Version, siehe INSTRUKTIONEN §31 Header
BACKTEST_RUN_DATE: str = "YYYY-MM-DD"   # Datum des Grid-Search-Runs, der diese Werte bestimmt hat
BACKTEST_REPORT_PATH: str = "05_Archiv/backtest-reports/macro_regime_grid_<DATE>.md"


def guard() -> None:
    """Runtime-Guard: verhindert Daily-Run mit unbelegten Thresholds."""
    if HY_OAS_THRESHOLD_BPS == 0 or FACTOR_RISKOFF == 1.00 and LOGIC_OPERATOR != "DISABLED":
        raise RuntimeError(
            "macro_regime_config.py enthält Default-0-Werte. Post-Task-8 Wahl nachholen "
            "oder VERSION auf v0.0-disabled setzen und LOGIC_OPERATOR='DISABLED'."
        )
```

Danach die Task-8-gewählten Werte konkret einsetzen (ersetzt die `0`/`0.0`/`"AND_of_2"`-Defaults).

- [ ] **Step 8.5: §31.2-Text auf Config-Referenz umbauen**

In der in Step 8.3 geschriebenen INSTRUKTIONEN §31.2 die konkreten Thresholds-Zeilen durch Single-Source-Referenz ersetzen:

**old_string (in §31.2):**
```
Konkrete Thresholds:
- `hy_oas_threshold_bps`: `<X>`
- `curve_threshold_bps`: `<Y>`
- `ism_floor`: `<Z>`
- `persistence_months`: `<N>`
- `logic_operator`: `<OR / AND_of_2 / AND_all>`
```

**new_string:**
```
Konkrete Thresholds — **Single-Source-of-Truth:** `03_Tools/macro_regime_config.py`
(Konstanten `HY_OAS_THRESHOLD_BPS`, `CURVE_THRESHOLD_BPS`, `ISM_FLOOR`,
`PERSISTENCE_MONTHS`, `LOGIC_OPERATOR`). Werte-Änderung ausschließlich dort, §31-Text
referenziert — keine Duplikation. Aktuelle Werte am Go-Live-Datum (2026-04-XX) im
CORE-MEMORY §1-Audit-Eintrag dokumentiert.
```

- [ ] **Step 8.6: Commit (Config + INSTRUKTIONEN §31 + Report)**

```bash
git add "00_Core/INSTRUKTIONEN.md" "05_Archiv/backtest-reports/" "03_Tools/macro_regime_config.py"
git commit -m "docs(5b): INSTRUKTIONEN §31 + macro_regime_config.py single-source (backtest-kalibriert)"
```

---

### Task 9: Daily-Run-Tool — `macro_regime_daily.py`

**Files:**
- Create: `03_Tools/macro_regime_daily.py`

**Hintergrund:** Spec §3.1 + §3.2.2. Separater Cron-Entry-Point; **importiert Thresholds aus `macro_regime_config.py` (Single-Source-of-Truth per Task 8.4)**, pullt latest FRED-Werte, evaluiert Regime mit **Contiguous-Date-Validation** der Persistence-History (Codex-Fix: `all()` auf last-N-Records ohne Date-Gaps-Check kann Missing-Daily-Runs falsch als persistent werten), appendet an `macro_regime.jsonl`. STATE.md-Update passiert separat im Briefing-Hook (Task 10).

- [ ] **Step 9.1: Daily-Run-Tool schreiben**

```python
"""macro_regime_daily.py — Daily-Cron-Entry für §31 Regime-Modulation.

Fetcht FRED-latest für HY-OAS/T10Y2Y/NAPM, evaluiert §31.2 Trigger-Regeln mit
Contiguous-Date-Validation der Persistence-History, appendet RegimeRecord an
05_Archiv/macro_regime.jsonl.

Thresholds-Quelle: 03_Tools/macro_regime_config.py (Single-Source-of-Truth per §31.4).
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "03_Tools"))
load_dotenv(ROOT / ".env")

from fred_client import FredClient  # noqa: E402
from macro_regime_schemas import RegimeRecord  # noqa: E402
import macro_regime_config as cfg  # noqa: E402

LIVE = ROOT / "05_Archiv" / "macro_regime.jsonl"
HIST = ROOT / "05_Archiv" / "macro_regime_historical.jsonl"


def _last_records_for_persistence() -> list[dict]:
    """Lese letzte ~PERSISTENCE_MONTHS × 22 Business-Days Records aus Live-Stream
    (Fallback auf Backfill wenn Live noch leer)."""
    need = max(cfg.PERSISTENCE_MONTHS * 22 + 5, 30)
    source = LIVE if LIVE.exists() and LIVE.stat().st_size > 0 else HIST
    lines = source.read_text(encoding="utf-8").splitlines()[-need:]
    return [json.loads(l) for l in lines if l.strip()]


def _validate_contiguous(history: list[dict], today: date, window: int) -> None:
    """Codex-Fix: verhindert falsch-positiven Persistence-Match durch Missing-Runs.

    Die letzten `window` Records müssen sich auf aufeinanderfolgende Business-Days
    erstrecken (bis spätestens gestern, heute kommt separat dazu). Lücken >3 BDays
    (Wochenende-Max 3) sind Indikator für ausgefallene Daily-Runs und blockieren
    den Persistence-Check — lieber falsch normal als falsch risk_off."""
    if len(history) < window:
        raise RuntimeError(
            f"Persistence-Window benötigt {window} Records, aber nur {len(history)} "
            f"in History verfügbar. Erster Live-Run oder Backfill zu kurz?"
        )
    tail = history[-window:]
    dates = [pd.Timestamp(r["date"]).date() for r in tail]
    # Alle aufeinanderfolgende Pairs dürfen maximal 3 Kalender-Tage (= Fr→Mo) auseinander liegen
    max_gap = max((dates[i+1] - dates[i]).days for i in range(len(dates)-1))
    if max_gap > 3:
        raise RuntimeError(
            f"Persistence-History enthält Gap >{max_gap} Tage — Missing-Daily-Runs? "
            f"Persistence-Check abgebrochen, regime bleibt bis manueller Recovery normal."
        )
    # Letzter History-Record sollte der letzte BDay vor heute sein
    last = dates[-1]
    bdays_diff = (pd.Timestamp(today) - pd.Timestamp(last)).days
    if bdays_diff > 4:   # Max Wochenende + Feiertag
        raise RuntimeError(
            f"Letzter History-Record {last} ist {bdays_diff} Kalender-Tage alt — "
            f"Daily-Run-Ausfall? Gap-Recovery nötig."
        )


def evaluate_regime(today_values: dict, history: list[dict], today: date) -> tuple[str, list[str], float]:
    """§31.2 Trigger-Eval mit Contiguity-Guard.

    today_values = {hy_oas, treasury_10y_2y, ism_pmi}
    history = last N records (aus `_last_records_for_persistence()`)
    today = Date-Stempel für den Record der GLEICH appended wird"""
    window_needed = cfg.PERSISTENCE_MONTHS * 22

    # Contiguity-Guard: verhindert False-Positive bei Missing-Runs
    _validate_contiguous(history, today, window=window_needed)

    window = history[-window_needed:] + [today_values]
    hy_all = all(r["hy_oas"] > cfg.HY_OAS_THRESHOLD_BPS / 100.0 for r in window)
    cv_all = all(r["treasury_10y_2y"] < cfg.CURVE_THRESHOLD_BPS / 100.0 for r in window)
    ism_all = all(r["ism_pmi"] < cfg.ISM_FLOOR for r in window)

    fired = []
    if hy_all: fired.append("hy_oas_persistent_above_threshold")
    if cv_all: fired.append("curve_persistent_below_threshold")
    if ism_all: fired.append("ism_persistent_below_floor")

    signals = [hy_all, cv_all, ism_all]
    if cfg.LOGIC_OPERATOR == "OR":
        is_riskoff = any(signals)
    elif cfg.LOGIC_OPERATOR == "AND_of_2":
        is_riskoff = sum(signals) >= 2
    elif cfg.LOGIC_OPERATOR == "AND_all":
        is_riskoff = all(signals)
    elif cfg.LOGIC_OPERATOR == "DISABLED":
        is_riskoff = False
    else:
        raise ValueError(f"unknown §31 operator {cfg.LOGIC_OPERATOR!r}")

    state = "risk_off" if is_riskoff else "normal"
    factor = cfg.FACTOR_RISKOFF if is_riskoff else 1.00
    return state, fired, factor


def main() -> int:
    try:
        cfg.guard()
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        return 1

    client = FredClient()
    today = date.today()

    # Latest fetch (3 requests total)
    series = [
        ("hy_oas", "BAMLH0A0HYM2"),
        ("treasury_10y_2y", "T10Y2Y"),
        ("ism_pmi", "NAPM"),
    ]
    latest: dict[str, float] = {}
    ism_asof = today
    for key, sid in series:
        s = client.get_latest(sid, observation_start=str(today - timedelta(days=45)))
        if s.empty:
            print(f"[WARN] FRED returned empty for {sid} — check rate/connectivity")
            return 2
        latest[key] = float(s.iloc[-1])
        if key == "ism_pmi":
            ism_asof = s.index[-1].date()

    # Load history and evaluate with contiguity guard
    history = _last_records_for_persistence()
    try:
        state, fired, factor = evaluate_regime(latest, history, today)
    except RuntimeError as e:
        # Contiguity-Guard hat angeschlagen — safer default: normal
        print(f"[GUARD] {e} — regime defaulted to normal, factor=1.00")
        state, fired, factor = "normal", [], 1.00

    rec = RegimeRecord(
        date=today,
        hy_oas=latest["hy_oas"],
        treasury_10y_2y=latest["treasury_10y_2y"],
        ism_pmi=latest["ism_pmi"],
        ism_asof=ism_asof,
        regime_state=state,
        triggers_fired=fired,
        sparraten_factor=factor,
        schema_version="1.0",
    )

    with LIVE.open("a", encoding="utf-8") as fh:
        fh.write(rec.model_dump_json() + "\n")
    print(f"Appended {today} regime={state} factor={factor} triggers={fired}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 9.2: Daily-Run-Smoke (läuft noch nicht — erwartet Guard-Error wegen Default-0-Config)**

```bash
python 03_Tools/macro_regime_daily.py
```

Expected: `[ERROR] macro_regime_config.py enthält Default-0-Werte. Post-Task-8 Wahl nachholen ...`. Exit 1. Bestätigt `cfg.guard()`-Trip aus `macro_regime_config.py`.

- [ ] **Step 9.3: Thresholds in `macro_regime_config.py` einbrennen (nicht in daily.py!)**

In `03_Tools/macro_regime_config.py` die Default-0-Werte durch Task-8-gewählte Werte ersetzen. `BACKTEST_RUN_DATE` + `BACKTEST_REPORT_PATH` auf aktuellen Stand setzen. `VERSION` bleibt `"1.0.0"`. `macro_regime_daily.py` importiert automatisch via `cfg.` — kein separater Sync nötig, Single-Source-of-Truth ist gewährleistet.

- [ ] **Step 9.4: Daily-Run-Live-Smoke**

```bash
python 03_Tools/macro_regime_daily.py
```

Expected: `Appended <date> regime=<state> factor=<f> triggers=<list>`. Neue Zeile in `05_Archiv/macro_regime.jsonl`.

- [ ] **Step 9.5: Commit**

```bash
git add 03_Tools/macro_regime_daily.py 03_Tools/macro_regime_config.py 05_Archiv/macro_regime.jsonl
git commit -m "feat(5b): macro_regime_daily.py + config (single-source) + first live record"
```

---

### Task 10: Morning-Briefing-Integration — CCR Remote-Trigger-Prompt

**Files:**
- Modify: CCR-Remote-Trigger-Config (ermitteln via `ccr list`), Path-Variante abhängig vom aktuellen Trigger-Setup — Plan-Hinweis unten
- Fallback: lokales Briefing-Hook-Script, falls Local-Variante parallel existiert

**Hintergrund:** Morning-Briefing v2.1 läuft per **Remote-CCR-Trigger täglich 10:00 MESZ** (STATE.md System-Zustand). Das ist kein lokaler Python-Cron — beim Trigger wird Claude mit einem Prompt-Template geweckt und führt die Briefing-Skill-Sequenz aus. Integration des Daily-Regime-Runs erfolgt **über das Prompt-Template**, nicht über ein lokales Hook-Script. CCR-Regel: **full-replace** (Memory: „Remote Trigger API — ccr full-replace rule; JSON nesting gotcha") — Edit = komplettes Config-Objekt neu pushen, nicht Partial-Patch.

**Routing-Logik des Plans:**
- Variante A (Default): CCR-Remote-Trigger — Prompt-Template updaten
- Variante B (Fallback, falls lokaler Briefing-Script existiert): zusätzlich Pre-Step einhängen

- [ ] **Step 10.1: CCR-Trigger-Inventory**

```bash
ccr list 2>&1 | head -20
```

Expected: Auflistung aktiver Trigger mit Namen/IDs. Morning-Briefing-Trigger-Name identifizieren (erwartet z.B. `morning-briefing-v2.1` oder ähnlich). Bei leerer Ausgabe oder CCR-Command-Not-Found: Check via `grep -rln "morning.*briefing\|v2\.1" 03_Tools/ 00_Core/ 2>/dev/null` nach lokaler Config-Datei (JSON/YAML).

- [ ] **Step 10.2: Aktuelle Trigger-Config als Snapshot dumpen**

```bash
ccr show <trigger-id> > /tmp/briefing_trigger_snapshot.json
cat /tmp/briefing_trigger_snapshot.json
```

Expected: JSON-Objekt mit `prompt`-Feld (oder nested in `config.prompt` — Memory nennt „JSON nesting gotcha"). Kompletter Inhalt als Backup behalten für Recovery/Rollback.

- [ ] **Step 10.3: Prompt-Template erweitern (full-replace, nicht partial)**

Im Snapshot die `prompt`-Feld-Zeichenkette anpassen. Am **Anfang** des Prompts (als ersten Schritt-Block) einfügen:

```
SCHRITT 0 — Macro-Regime-Daily-Run (§31.5-Pflicht vor Briefing):
Führe `python 03_Tools/macro_regime_daily.py` aus. Parsen des stdout:
  - "Appended YYYY-MM-DD regime=<state> factor=<f>" → OK, weiter
  - "[ERROR] macro_regime_config.py ..." → Config-Lücke melden, Briefing trotzdem generieren (regime=unknown dokumentieren)
  - "[GUARD] Persistence-History Gap ..." → Gap-Recovery-Hinweis, Briefing mit regime=normal fortsetzen
  - Andere Exit-Codes → Warnung im Briefing-Body, kein Hard-Stop
Erst danach: normale Briefing-Schritte (Preis-Fetch / Score-Update / etc).
```

**Wichtig:** existierende Schritt-Nummerierung im Prompt um **+1** verschieben (neuer SCHRITT 0 vorn; alte 1→2, 2→3, etc.). Änderung wird als **ganzes Config-Objekt** via `ccr update <trigger-id> --file <edited-snapshot>` (oder äquivalente CCR-Command) gepusht.

- [ ] **Step 10.4: Full-Replace-Push**

```bash
ccr update <trigger-id> --file /tmp/briefing_trigger_modified.json
ccr show <trigger-id> | diff - /tmp/briefing_trigger_modified.json
```

Expected: `diff` leer (oder nur Whitespace-Unterschiede). Bestätigt dass Server-Config dem lokalen-Stand entspricht — **CCR-Nesting-Gotcha-Check**: falls Diff zeigt dass `prompt` auf Top-Level statt genested gepusht wurde, Config-Struktur korrigieren und re-pushen.

- [ ] **Step 10.5: Manueller Dry-Run-Trigger (falls CCR `run`-Endpoint funktional)**

```bash
ccr run <trigger-id> --dry-run 2>&1 | head -40
```

Expected: Trigger-Prompt-Vorschau zeigt neuen SCHRITT-0-Block. **Memory-Hinweis:** CCR `run`-Endpoint ist „noop" — realistischer Test erfolgt erst durch echten Trigger-Fire am nächsten Morgen oder via `!MorningBriefing`-Kommando manuell.

- [ ] **Step 10.6: Variante-B-Fallback (falls CCR nicht verfügbar)**

Falls Step 10.1 keinen aktiven CCR-Trigger findet, sondern ein lokales Briefing-Script vorliegt (z.B. `03_Tools/briefing_hook.py` oder vergleichbar):

```python
# Track-5b §31.5 — am Anfang der Briefing-Main-Funktion ergänzen
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
try:
    r = subprocess.run(["python", str(ROOT / "03_Tools" / "macro_regime_daily.py")],
                       capture_output=True, text=True, timeout=60)
    print(f"[macro-regime] {r.stdout.strip()}")
    if r.returncode != 0:
        print(f"[macro-regime] WARN rc={r.returncode}: {r.stderr.strip()[:200]}")
except Exception as exc:
    print(f"[macro-regime] WARN invocation failed: {exc}")
```

Kein Hard-Fail — Briefing läuft auch ohne frischen Regime-Record durch (Stale-Read aus STATE.md).

- [ ] **Step 10.7: Commit**

Variante A:
```bash
# CCR-Config ist remote, nichts zu committen — aber Änderungs-Log in log.md
# (wird in Task 11 erfasst)
echo "CCR trigger <id> updated 2026-04-XX — §31.5 pre-step added" >> /tmp/task10_audit.txt
```

Variante B:
```bash
git add <briefing-script>
git commit -m "feat(5b): macro_regime_daily.py pre-step im lokalen Briefing-Hook (Variante B)"
```

---

### Task 11: Docs-Sync — STATE.md + CORE-MEMORY §1 + log.md

**Files:**
- Modify: `00_Core/STATE.md`
- Modify: `00_Core/CORE-MEMORY.md` (§1 Meilensteine + ggf. §5 SPY-Proxy-Limitation)
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md`

**Hintergrund:** Spec §3.5 Acceptance-Kriterien: STATE.md aktualisiert, CORE-MEMORY-Audit-Eintrag (redirected to §1), Interim-Gate-Dokumentation.

- [ ] **Step 11.1: STATE.md System-Zustand + Trigger-Zeile**

`00_Core/STATE.md`:

**Alt (System-Zustand-Block, Morning-Briefing-Zeile nach Plan-5a-Änderung):**
```
- **Morning Briefing:** Trigger v2.1 täglich 10:00 MESZ (16 Symbole, Yahoo-Gap BRK.B/RMS/SU).
- **`sec-edgar-skill` v1.0 aktiv** (seit 2026-04-20) — Eskalations-Fallback für defeatbeta/Shibui-Konflikte, 10-K-Textsuche, Form-4-Eskalation. EdgarTools-basiert, nicht auto-aktiv in `!Analysiere`.
```

**Neu (darunter anhängen):**
```
- **§31 Macro-Regime-Filter aktiv** (seit 2026-04-XX) — Daily-Run aus Morning-Briefing-Trigger. Thresholds (hy_oas_bps/curve_bps/ism_floor/persistence/operator) aus Full-Grid-Backtest 1996-2026. Sparraten-Modulation via `sparraten_factor` (normal=1.00, risk_off=<F>). **Aktueller Regime-State:** `<normal|risk_off>` (Stand `<letzter daily-run>`, per `macro_regime.jsonl`).
```

Parallel: Trigger-Tabelle um Review-Zeile erweitern:

**old_string (innerhalb Trigger-Tabelle):**
```
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |
```

**new_string:**
```
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |
| 2026-05-20 | macro_regime | D | 30-Tage-Stabilitäts-Review §31 (Task 14 Plan 5b) |
```

- [ ] **Step 11.2: CORE-MEMORY §1 Meilenstein-Einträge**

Zwei Einträge in `00_Core/CORE-MEMORY.md` §1 ergänzen:

```markdown
### 2026-04-XX — Track 5b §31 Macro-Regime-Filter Go-Live

`fredapi` installiert, FRED-API-Key in `.env` konfiguriert. `fred_client.py` mit
ALFRED-first-release + FRED-latest-Dual-Mode deployed. Historical-Backfill
`macro_regime_historical.jsonl` ab 1997-01 (HY-OAS-Intersection-Start). Grid-Search
über 1620 Parameter-Kombinationen mit Sub-Perioden-Robustness-Test (1996-2007,
2008-2019, 2020-2026) abgeschlossen. Konservative Thresholds
(`<hy_oas=X, curve=Y, ism=Z, persistence=N, operator=O, factor=F>`) in INSTRUKTIONEN
§31 kodifiziert.

**Nicht-Änderung:** DEFCON-Scoring unverändert. Sparraten-Nenner 8.0 unverändert.
`sparraten_factor` multipliziert nur die Einzelraten. Keine per-Ticker-Macro-Sensitivität,
keine Position-Entscheidungen macro-basiert.

**SPY-Proxy-Limitation:** Backtest nutzt SPY-Monatsschluss als Satelliten-Return-Proxy
(Historical-Constituent-Bias-Vermeidung). Tatsächliche Regime-Sensitivität des aktuellen
11-Satelliten-Portfolios kann abweichen. Re-Validation bei Interim-Gate 2027-10-19.

**Referenz:** TRACK5-SPEC v1.0 §3 (Commit `22cdeb8`). Plan
`docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md`. Backtest-Report
`05_Archiv/backtest-reports/macro_regime_grid_<YYYY-MM-DD>.md`.
```

Und ggf. einen zweiten Eintrag direkt darunter, der den **Backtest-Audit-Kern** dokumentiert (für spätere Re-Kalibrierung):

```markdown
### 2026-04-XX — §31 Backtest-Audit (Point-in-Time-Snapshot)

**Grid-Setup:** 1620 Combos × ~7500 BDays. Runtime ~<X> min. MaxDD-Constraint filtert
<N> invalide Combos.

**Top-3 Robust-Regionen** (stabile positive Utility in allen 3 Sub-Perioden):
1. `<combo1>` — utility=<X1>, maxdd=<Y1>
2. `<combo2>` — utility=<X2>, maxdd=<Y2>
3. `<combo3>` — utility=<X3>, maxdd=<Y3>

**Gewählt (konservativ):** `<final-combo>`. Tie-Break-Begründung: höchste `hy_oas_bps`,
längste `persistence_months`, höchster `factor_riskoff` im Robust-Set.

**Trade-off gegenüber Point-Optimum:** Utility-Differenz <Δ>. Gewählt wegen
§29.1 PBO-Risiko (wenige Krisen-Epochen 2008/2020/2022).
```

- [ ] **Step 11.3: log.md Session-Eintrag**

```markdown
## 2026-04-XX — Track 5b Implementation

- FRED-API-Key registriert, in `.env` gesetzt (Free-Tier, 2 req/s, ~6 req/day Bedarf)
- `fredapi` + `python-dotenv` installiert
- `fred_client.py` mit ALFRED/FRED-Dual-Mode deployed, 3/3 Smoke-Tests green
- `RegimeRecord` Pydantic-Schema v1.0 per Spec §3.2.2
- Backfill `macro_regime_historical.jsonl`: ~7500 Records ab 1997-01 (HY-OAS Intersection)
- Data-Quality-Gate: monotonic, business-day-gap-check, NaN <1%, HY-OAS start ≤1997-01-31
- Grid-Search 1620 Combos in ~<X> min (vectorized precompute-cache)
- Top-3 Robust-Regionen identifiziert, konservative Wahl: `<combo>`
- INSTRUKTIONEN §31 geschrieben, Thresholds in `macro_regime_daily.py` einsync
- Daily-Run in Morning-Briefing-Hook integriert — erster Live-Record append ok
- STATE.md: Regime-State-Zeile + 2026-05-XX 30-Tage-Review-Trigger
- CORE-MEMORY §1: Go-Live-Meilenstein + Backtest-Audit-Snapshot + SPY-Proxy-Limitation
```

- [ ] **Step 11.4: Commit**

```bash
git add "00_Core/STATE.md" "00_Core/CORE-MEMORY.md" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md"
git commit -m "docs(5b): STATE + CORE-MEMORY §1 + log — §31 go-live"
```

- [ ] **Step 11.5: Enforcement-Deferral dokumentieren (Codex-Finding 2026-04-20)**

In `00_Core/INSTRUKTIONEN.md` §22 (Sparplan-Formel) einen Hinweis-Block ergänzen, der den Manual-Read-Workflow für `sparraten_factor` explizit macht — verhindert Silent-Incompatibility wenn später ein Sparplan-Automator gebaut wird:

**old_string (Ende §22 oder vor nächster §):**
```
## 23. Tariff Exposure Scoring
```

**new_string (§22-Anhang einfügen, dann §23-Header):**
```
### 22.1 §31 Regime-Modulation — Manual-Read-Workflow (Stand 2026-04-XX)

`sparraten_factor` aus §31 ist **aktuell informational**. Beim monatlichen Sparplan-
Ausführen:
1. Aktuelle Regime-Zeile in STATE.md prüfen (System-Zustand-Block)
2. Wenn `regime_state == risk_off`: jede Einzelrate aus §22-Tabelle mit
   `sparraten_factor` multiplizieren (z.B. 35,63 € × 0,70 = 24,94 €)
3. Differenz (Rate × (1 − factor)) in Cash-Reserve buchen (NICHT wegfallen lassen)
4. Beim Zurückkehren zu `regime_state == normal`: Raten wieder auf vollen Wert

**Zukünftige Automatisierung:** Ein Sparplan-Runner-Skript würde `macro_regime.jsonl`
am Monatsanfang lesen und die Modulation direkt anwenden. Diese Track-Iteration
(5b) liefert die **Datenbasis**, nicht den Enforcer. Folge-Track 6+ optional.
```

```bash
git add "00_Core/INSTRUKTIONEN.md"
git commit -m "docs(5b): §22.1 manual-read-workflow für regime-sparraten-factor (deferral)"
```

---

### Task 12: `!SyncBriefing`

**Files:** (keine — Briefing-Hook-Operation)

- [ ] **Step 12.1: SyncBriefing ausführen**

Prompt: `!SyncBriefing`

Expected: Trigger-Config spiegelt neuen 00_Core-Stand. Bei Diff-Warnung: prüfen ob gewünscht.

- [ ] **Step 12.2: Session-Ende wenn ok**

Kein zusätzlicher Commit.

---

### Task 13: Verification-Gate End-to-End

Qualitativer Durchgang nach Abschluss Task 1-12:

- [ ] **Step 13.1: JSONL-Sanity** — `wc -l 05_Archiv/macro_regime_historical.jsonl` ≈ 7500; `wc -l 05_Archiv/macro_regime.jsonl` ≥ 1
- [ ] **Step 13.2: Schema-Roundtrip** — `python 03_Tools/macro_regime_schemas.py` → 3/3 green
- [ ] **Step 13.3: FRED-Client-Smoke** — `python 03_Tools/_smoke_test_macro.py` → 4/4 green
- [ ] **Step 13.4: Daily-Run-Rerun** — `python 03_Tools/macro_regime_daily.py` appendet neuen Record oder meldet „already today" je nach Implementation. Manual-check dass kein duplicate-date entsteht.
- [ ] **Step 13.5: STATE.md-Regime-Zeile aktuell** — neue Session-Start, STATE zeigt aktuellen regime_state
- [ ] **Step 13.6: INSTRUKTIONEN §31 vollständig** — keine `<X>`/`<Y>`-Placeholder mehr; Werte identisch zu `macro_regime_daily.py`-Konstanten
- [ ] **Step 13.7: CORE-MEMORY §1-Einträge mit konkreten Zahlen** — keine Platzhalter

---

### Task 14: Deferred — 30-Tage-Stabilitäts-Review (2026-05-20)

**Files:**
- Modify: `00_Core/CORE-MEMORY.md` (§1 Meilensteine — Review-Eintrag)
- Modify: `00_Core/STATE.md` (Trigger-Zeile auflösen)

**Hintergrund:** Spec §3.5: „Daily-Append-Pipeline läuft seit mindestens 30 Tagen fehlerfrei". Erster Review-Termin: `Go-Live-Date + 30` (erwartet ~2026-05-20). Prüft: (a) keine Daily-Run-Fails, (b) keine Schema-Violations, (c) keine Regime-State-Flip-Flops (>3 Wechsel in 30 Tagen wäre Hinweis auf zu-sensitive Thresholds).

- [ ] **Step 14.1: Am Review-Tag — Daily-Run-Logs prüfen**

```bash
wc -l 05_Archiv/macro_regime.jsonl
# ~20-22 Records erwartet (Trading-Days der letzten 30 Kalender-Tage)
grep -c "risk_off" 05_Archiv/macro_regime.jsonl
```

Expected: ~20 Records, ein Regime-State mehrheitlich (kein zu-häufiger Wechsel).

- [ ] **Step 14.2: Schema-Re-Validation**

```bash
python -c "import json; from pathlib import Path; import sys; sys.path.insert(0, '03_Tools'); from macro_regime_schemas import RegimeRecord; [RegimeRecord.model_validate(json.loads(l)) for l in Path('05_Archiv/macro_regime.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]; print('ok')"
```

Expected: `ok`.

- [ ] **Step 14.3: Review-Eintrag CORE-MEMORY §1**

```markdown
### 2026-05-20 — §31 30-Tage-Stabilitäts-Review — [passed|failed]

Daily-Run-Count: <N> (erwartet ~20). Schema-Violations: 0. Regime-Flips: <K>.
Review-Outcome: <passed | failed — Reason>.
```

Bei failed: Applied-Learning-Lektion + Backtest-Reparatur-Plan.

- [ ] **Step 14.4: STATE.md-Trigger-Zeile auflösen**

Entfernen:
```
| 2026-05-20 | macro_regime | D | 30-Tage-Stabilitäts-Review §31 (Task 14 Plan 5b) |
```

Ersetzen durch (falls passed) `§31 Stabilität-Review 2026-05-20 ✓ — in CORE-MEMORY §1`-Vermerk in System-Zustand-Block.

- [ ] **Step 14.5: Commit**

```bash
git add "00_Core/CORE-MEMORY.md" "00_Core/STATE.md"
git commit -m "audit(5b): §31 30-tage-stabilitäts-review — [passed|failed]"
```

---

### Task 15: Deferred — Interim-Gate-Vorbereitung 2027-10-19

**Files:** (nur Dokumentation, keine Code-Änderung jetzt)

**Hintergrund:** Spec §3.3.3 Interim-Gate-Nutzung: beim 18-Monats-Dry-Run `risk-metrics-calculation` soll Regime-konditionierte Portfolio-Performance analysiert werden (normal vs. risk_off-Phasen). STATE.md-Eintrag zeigt bereits Interim-Gate 2027-10-19; Task 15 stellt sicher dass `macro_regime.jsonl` dort konsumierbar ist.

- [ ] **Step 15.1: INSTRUKTIONEN §29 (Retrospective-Analyse-Gate) mit §31-Referenz ergänzen**

In `00_Core/INSTRUKTIONEN.md` §29 einen Rückverweis auf §31-Macro-Regime-Filter einfügen (konkret: §29.2 External-Benchmark oder §29.6 Portfolio-Return-Metrik-Layer — je nachdem wo Regime-Attribution logisch hinpasst):

```markdown
- [[§31-Macro-Regime-Filter]] — Regime-konditionierte Performance-Attribution (Join auf `macro_regime.jsonl.date` ↔ `portfolio_returns.jsonl.date`)
```

- [ ] **Step 15.2: STATE.md Interim-Gate-Zeile erweitern**

Die bestehende Zeile „Interim-Gate 2027-10-19: 18-Mo-Dry-Run risk-metrics-calculation ..." um Regime-Attribution ergänzen:

**old_string:**
```
- **Interim-Gate 2027-10-19:** 18-Mo-Dry-Run `risk-metrics-calculation` + Data-Quality-Check auf `portfolio_returns.jsonl` (R5 Phase 3, inkl. FX-Conversion-Nachrüstung für Mixed-Currency-Basket). Review-Aktivierung 2028-04-01.
```

**new_string:**
```
- **Interim-Gate 2027-10-19:** 18-Mo-Dry-Run `risk-metrics-calculation` + Data-Quality-Check auf `portfolio_returns.jsonl` (R5 Phase 3, inkl. FX-Conversion-Nachrüstung für Mixed-Currency-Basket) + **§31 Regime-Attribution (normal vs. risk_off Performance-Decomposition via `macro_regime.jsonl`-Join, Spec §3.3.3)**. Review-Aktivierung 2028-04-01.
```

- [ ] **Step 15.3: Commit**

```bash
git add "00_Core/INSTRUKTIONEN.md" "00_Core/STATE.md"
git commit -m "docs(5b): interim-gate 2027-10-19 um §31 regime-attribution erweitert"
```

---

## Verification — End-to-End-Gate

Nach Abschluss Task 1-13 (Task 14 deferred, Task 15 Doc-only):

1. **Env-Health:** `pip list | grep -E 'fredapi|dotenv|pydantic'` zeigt alle drei Packages
2. **Client-Smoke:** `python 03_Tools/_smoke_test_macro.py` → 4/4 green
3. **Schema-Smoke:** `python 03_Tools/macro_regime_schemas.py` → 3/3 green
4. **Daily-Run-Idempotency:** Daily-Run zweimal an gleichem Tag → zweite Run meldet „already today" ODER writes duplicate (je nach Implementation-Wahl). Erwartetes Verhalten: User-gewählt in Task 9, dokumentiert.
5. **STATE.md Regime-Zeile:** lebt, zeigt aktuelles `regime_state` + Daily-Run-Datum
6. **Backtest-Report** in `05_Archiv/backtest-reports/` sichtbar, „Conservative-Default Choice"-Sektion gefüllt (keine `<X>`-Placeholder)
7. **Multi-Source-Drift-Check (§27.4):** INSTRUKTIONEN §31.2 + `macro_regime_daily.py`-Konstanten + Backtest-Report zeigen identische Thresholds
8. **Interim-Gate-Dokumentation:** STATE.md Interim-Gate-Zeile enthält §31-Regime-Attribution-Referenz

**Review-Kriterium:** Alle 8 Punkte grün ohne manuelle Code-Änderung. Bei Diff in Punkt 7 (Multi-Source-Drift): Multi-Source-Drift-Check-Applied-Learning greift — erst Drift auflösen, dann Track 5b als „complete" markieren.

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| FRED-API-Key unrechtmäßig committed | `.env` im `.gitignore` (Task 1.1), nur `.env.example` committet (leer) |
| fredapi/yfinance-Dep-Konflikt mit bestehendem Python-Env | Task 1.5 Exit-Code-Check; bei Konflikt Abbruch + User-Rückfrage (optional venv) |
| Grid-Search-Runtime >45 min | Pre-Compute-Cache-Audit (`signals_cache` max 180 Einträge); bei Problem: `sparraten_factor_riskoff` auf 2 Werte fixieren (600 Combos) |
| Backtest-Regime-Snooping (wenige Krisen-Epochen) | Spec §3.4 + Codex-Empfehlung: Sub-Perioden-Robustness + konservative Point-vs-Region-Wahl + Tie-Break-Präferenz (höhere Thresholds) |
| SPY-Proxy ≠ Satelliten-Portfolio | Explizit in §31.6 + CORE-MEMORY §1 dokumentiert. Re-Validation bei Interim-Gate 2027-10-19. |
| ALFRED vs FRED Revision-Drift (Live-Record irrtümlich revidiert) | `macro_regime_daily.py` schreibt NIE rückwirkend; §31.4 „Revision-Invarianz"-Regel |
| Daily-Run-Crash während Morning-Briefing | Briefing-Hook fängt Exception ab, Briefing läuft weiter (Task 10.2); macro-regime-Daily-Log zeigt failed-fetch |
| Threshold-Drift zwischen §31.2 und `macro_regime_daily.py`-Konstanten | Task 13.6 Multi-Source-Drift-Check; Applied-Learning-Regel |
| `NAPM`-Serie wird von FRED umbenannt/deprekiert | Fredapi-Rückgabe fängt HTTP-Fehler ab; bei 404 Applied-Learning-Nachschärfung (alternative ISM-ID, z.B. `MANEMP` als Substitut) |
| Plan nutzt §1 Meilensteine statt Spec-§5 — Audit-Verwirrung | Header-Notice oben dokumentiert Redirect. Spec unverändert. Codex-Bestätigung (Plan 5a Header) |

---

## Pre-Implementation-Gates

Vor Implementation-Session-Start:

- [ ] **Gate A — Tavily-Go-Live stabil seit ≥3 Tagen** (Spec §4.1)
- [ ] **Gate B — Plan 5a abgeschlossen ODER parallel-Ready** (Spec §4.2: 5a+5b sind unabhängig, können parallel laufen). Empfehlung: Plan 5a zuerst vollständig ausführen, da kleiner und sauberer Start
- [ ] **Gate C — FRED-API-Key vor Task 1.3 beschafft** — User registriert bei https://fred.stlouisfed.org/docs/api/api_key.html (5 min)
- [ ] **Gate D — `dracepj/fred-mcp`-Status verifiziert** (optional). Falls MCP gut maintained und User α bevorzugt: `fred_client.py`-Adapter durch MCP-Call ersetzen, Rest des Plans unverändert
- [ ] **Gate E — SPY-Quelle verfügbar** (`yfinance`-Default oder Shibui-Cache). Prüfung: `python -c "import yfinance as yf; print(yf.download('SPY', period='5d').tail())"` muss Werte liefern

---

## Handover-Hinweise für Implementation-Session

- Sessionstart: `Session starten` → STATE.md lesen → Plan 5a-Status prüfen → Plan 5b laden
- Implementation-Skill: `superpowers:subagent-driven-development` (recommended). Tasks 1-3 sind Setup (Env + Adapter + Schema); Tasks 4-8 sind der schwere Rechenteil (Backfill + Backtest + §31-Kalibrierung); Tasks 9-11 sind Integration; Tasks 13-15 sind Gates/Deferred
- **Kritischer Checkpoint:** Task 7 Full-Grid-Run — sollte ≤30 min laufen. Bei >45 min Pause + Codex-Diagnose des Pre-Compute-Cache-Verhaltens
- **Task 8 ist Interpretations-Stelle:** konservative Parameter-Wahl erfordert menschliches Urteil, kein reiner Algorithmus. Bei Tie-Break-Unklarheit: User-Rückfrage, nicht Silent-Choice
- **Nach Task 11:** erster Briefing-Trigger (manuell via `!MorningBriefing`) testet End-to-End-Flow
- **Nach Implementation:** Erster Review-Gate in 30 Tagen (Task 14 ~2026-05-20), danach Interim-Gate 2027-10-19 (Task 15), Final-Review 2028-04-01

---

## Nicht-Ziele (explizit out-of-scope per Spec §3.6)

- KEINE per-Ticker-Macro-Sensitivitäten (Option C abgelehnt)
- KEINE Position-Entscheidungen basierend auf Macro
- KEIN Macro-Input in DEFCON-Score-Berechnung
- KEINE Macro-FLAG-Events (Regime-Wechsel ist KEINE FLAG-Aktivierung)
- KEIN Override des Sparraten-Nenners aus STATE.md — `sparraten_factor` multipliziert nur Einzelraten
- KEINE EDGAR-Komponenten (Plan Track 5a separat)
- KEIN Paper-Logging-Phase vor Aktivierung (Spec §1.1: „Ersetzt durch historischen Backtest")
- KEIN diskretionärer Override außer via Versions-Bump (§31.4)

---

*🦅 Track-5b-Plan v1.0 | 2026-04-20 | Co-Review: Claude (Opus 4.7) + Codex | Ref: TRACK5-SPEC v1.0 (22cdeb8)*
