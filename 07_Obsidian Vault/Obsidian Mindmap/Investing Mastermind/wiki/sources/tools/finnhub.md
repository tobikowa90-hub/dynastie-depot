---
tags: [quelle, api, us-ticker, real-time, fundamentals-snapshot]
status: aktiv-shadow-run
version: v0.1 (Build-Phase-Done)
stand: 2026-05-22
---

# FinnHub — Real-Time-Layer (Read-Only Surface)

## Was es liefert

- **Quote** (`/quote`) — letzter US-Close, ~2h Lag intraday (löst defeatbeta-Stale-Problem für tagesaktuelle Confirmation)
- **Earnings-Calendar** (`/calendar/earnings`) — per-symbol Earnings-Termine + EPS-Estimates (10/12 Satelliten + ASML; BRK.B liefert BRK.A-EPS) — *Stand vor Umstrukturierung-2027; Roster jetzt 13, Coverage der Owner-Adds NOW/ZETA [US] / KYCCF [JP-OTC] noch nicht re-verifiziert (Earnings-SSoT ist ohnehin `earnings_calendar.py`)*
- **Company-News** (`/company-news`) — bis 249 Items/7d pro Symbol
- **Stock-Metric** (`/stock/metric`) — 21/26 DEFCON-critical TTM-Metriken Free-Tier (peTTM, roe, roic, plus 18 weitere)
- **Stock-Profile** (`/stock/profile2`) — Issuer-Profil

## Rolle im System

**Read-Only Crosswalk-Quelle** — KEIN Scoring-Pfad in v0.1 (Zero-Skill-Refactor-Footprint invariant, technisch hart durch `_meta.for_scoring=False`-Marker + Assertion in `03_Tools/backtest-ready/archive_score.py` Persistenz-Schicht erzwungen). Vergleichsdatenquelle für [[defeatbeta]] zur Stale-Detection + zukünftiger v0.2-Reklassifizierung.

## Konfiguration

- **API-Key:** `.env` (lokaler Pfad außerhalb Repo, `.gitignore` Z.21)
- **Cache:** `~/.dynasty/finnhub_cache/` (außerhalb Repo)
- **Rate-Limit:** 60 Calls/min (Free-Tier), Token-Bucket-Limiter im Wrapper
- **Coverage:** 10/12 US-Satelliten + ASML Quote/Calendar/News/Metrics voll; Europäer RMS.PA/SU.PA = 403 Premium-only → bleibt [[non-us-fundamentals]] (yfinance)

## Artefakte

- `03_Tools/finnhub_client.py` — Wrapper + Token-Bucket + File-Cache + 4 Getters + Retry + _meta-Guardrail
- `03_Tools/finnhub_smoke_test.py` + `finnhub_health.json` — 9-Test-Matrix, dynamic EXPECTED_PASS_COUNT
- `03_Tools/finnhub_crosswalk_trigger.py` — Daily-Pull-CLI + `CrosswalkRecord` pydantic strict-mode
- `03_Tools/defeatbeta_subprocess.py` — WSL-Bridge gegen [[defeatbeta]] (Crosswalk-Primary-Pull, A12 Identity-Check WSL≡MCP bit-perfect)
- `03_Tools/finnhub_a12_identity_check.py` — A12 WSL≡MCP Pairing-Script
- `03_Tools/finnhub_crosswalk_log.jsonl` — Append-Only Crosswalk-Records (24 Records A6-acceptance Stand 22.05.)

## Shadow-Run + Reklassifizierungs-Gate (PIPELINE #75)

- **Start:** 2026-05-23 ~Mittag manueller Day-1-Trigger
- **Hard-Deadline:** 2026-07-06 (+45d from Build-Done)
- **Coverage-Ziele (Spec §8.1):** ≥50 Crosswalk-Records / ≥8 pro Kern-Symbol / ≥40 non-N/A ROIC
- **ROIC-Coverage:** 5 non-N/A/Tag → mind. 8 Daily-Läufe für ≥40-Gate
- **Trigger-Items für v0.2:** Crosswalk-Median-Divergenz / ROIC-CRIT-Tier-Häufigkeit / Europäer-403-Konsistenz / Cache-Hit-Rate / Rate-Limit-Headroom

## Day-1-Trigger-Command

```
python 03_Tools/finnhub_crosswalk_trigger.py --symbols MSFT,V,ASML,TMO,COST --batch-tag shadow-run-day-1
```

## Step 4a Decision (3/8-Minimal-Bridge)

defeatbeta-api-Methoden-Probe für 5 nicht-initial-abgedeckte Metriken → **2/5 vorhanden** (grossMargin5Y, debtToEquity) — <3-Threshold → **3/8-Minimal-Bridge akzeptiert** (peTTM/roe/roic Live + 5/8 systematisch N/A); 5/8-Folge-Recherche als PIPELINE #76 (v0.2-Methoden-Discovery).

## v0.2-Roadmap (bei positivem Gate-Outcome)

1. [[backtest-ready-forward-verify]] `data_source`-Marker
2. [[dynastie-depot-skill]] Earnings-Trigger-Hook
3. [[quick-screener]] Quote-Path
4. Fundamentals-Fallback-Pilot
5. [[insider-intelligence]] optional

## Spec/Plan-Files

- `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` v0.3 LOCKED (untracked per `.gitignore` Z.21)
- `docs/superpowers/plans/2026-05-22-finnhub-integration-build-v0.1.md` v0.1.0 (untracked)

## Methodology-Drift-Schutz

Technische Guardrails statt nur Policy (V-Q2-Präzedenz-Schutz):

- Wrapper-Return-Marker `_meta.for_scoring=False` (jeder Metric-Pull)
- Assertion `_assert_metric_for_scoring()` in [[backtest-ready-forward-verify]] Persistenz-Schicht
- A1 Static-Footprint-Check via Grep (0 matches `finnhub` in `01_Skills/` excl. `_extern/`)

## Verlinkungen

- [[defeatbeta]] — Crosswalk-Vergleichsquelle (Primary-Pull WSL-Subprocess)
- [[backtest-ready-forward-verify]] — Persistenz-Schicht mit R1-Guardrail-Assertion
- [[dynastie-depot-skill]] — v0.2-Integration-Kandidat (Earnings-Trigger-Hook)
- [[quick-screener]] — v0.2-Integration-Kandidat (Quote-Path)
- [[DEFCON-System]] — Scoring-System (in v0.1 NICHT touched)
