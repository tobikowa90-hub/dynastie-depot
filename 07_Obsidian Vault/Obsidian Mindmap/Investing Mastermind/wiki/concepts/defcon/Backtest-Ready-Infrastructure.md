---
title: "Backtest-Ready-Infrastructure"
type: concept
tags: [defcon, backtest, infrastructure, roadmap, kern]
created: 2026-04-17
updated: 2026-04-17
version: v3.7.1
sources: [arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha]
related: [DEFCON-System, Score-Archiv, FLAG-Event-Log, Backtest-Methodik-Roadmap, Analyse-Pipeline, Wissenschaftliche-Fundierung-DEFCON]
wissenschaftlicher_anker: "Operative Voraussetzung für spätere Validierung aller 14 DEFCON-Befunde (B1–B14)"
konfidenzstufe: operativ
---

# Backtest-Ready-Infrastructure

> **„Backtest-Ready statt Backtest-Done." Jeder Monat ohne Archiv-Infrastruktur ist verlorene Historie.**

## Problem

Das DEFCON-Scoring-System ist wissenschaftlich fundiert (4 Papers, 14 Befunde), hart kalibriert (AVGO 84 / MKL 82 / SNPS 76 nach v3.7) und FLAG-verankert — aber **formal unvalidiert**. Ein statistisch belastbarer Backtest ist heute methodisch unseriös:

- 11 aktive Satelliten, max. 28 inkl. Ersatzbank + Watchlist
- System läuft ~2 Jahre live — zu kurz für Forward-Return-Statistik
- Historische Point-in-Time-Scores existieren nur verstreut in log.md / CORE-MEMORY.md, nicht maschinenlesbar
- Point-in-Time-Moat-Ratings, EPS-Revisionen, Analyst-Konsensus historisch nicht verfügbar

**Jeder heute gebaute "Backtest" würde Rauschen als Signal verkaufen und das gut kalibrierte System an Noise-Overfitting gefährden.**

## Entschiedener Ansatz (2026-04-17)

Statt heute zu validieren → Infrastruktur bauen, die es **2028+ ermöglicht, überhaupt validieren zu können**. Jeder Score und jedes FLAG-Event wird ab sofort unveränderlich archiviert. Parallel läuft eine einmalige deskriptive FLAG-Event-Study als Sanity-Check der Datenmodelle.

## 4-Layer-Architektur

Siehe KONTEXT.md §11 für Details:

1. **State-Layer** — [[Faktortabelle]] (überschrieben)
2. **Narrative-Layer** — log.md, [[CORE-MEMORY]] (menschenlesbar, evolvierend)
3. **History-Layer** — [[Score-Archiv]] + [[FLAG-Event-Log]] (append-only, unveränderlich)
4. **Projection-Layer** — [[STATE]] (Session-Entry, synchron gehalten)

## Komponenten (Stand 17.04.2026)

| Komponente | Ort | Status |
|------------|-----|--------|
| Score-Archiv | `05_Archiv/score_history.jsonl` | ✅ aktiv, Backfill 24 Records |
| FLAG-Event-Log | `05_Archiv/flag_events.jsonl` | ✅ aktiv, Backfill 2 Records (MSFT/GOOGL) |
| Pydantic-Schemas | `03_Tools/backtest-ready/schemas.py` | ✅ 14 Modelle + 4 Validators |
| CLI-Writer | `archive_score.py` + `archive_flag.py` | ✅ Phase 1 deployed |
| Backfill-Tools | `backfill_scores.py` + `backfill_flags.py` | ✅ Einmal-Run durchlaufen |
| Event-Study | `flag_event_study.py` + Report | ✅ Phase 3 Einmal-Analyse (n=2) |
| git-Tracking | `.gitignore`-Whitelist für JSONL | ✅ Forward-Pipeline git-persistiert |

## Schreib-Disziplin

§18 Sync-Pflicht (INSTRUKTIONEN.md v1.7): Nach jeder `!Analysiere` müssen **6 Dateien** im gleichen git-Commit aktualisiert werden — log.md + CORE-MEMORY.md + Faktortabelle + STATE.md + score_history.jsonl + flag_events.jsonl (bei FLAG-Event).

§26 Archiv-Sync (INSTRUKTIONEN.md v1.7): 4-Schritt-Workflow (JSON generieren → archivieren → FLAG-Check → git commit). SKILL.md Schritt 7 ist die kanonische Trigger-Stelle.

## Review-Termin 2028-04-01

Entscheidung über formalen Backtest — erwartete Datenlage:
- ~250-300 Score-Records (28 Ticker × 4-6 Analysen/Jahr × 2 Jahre Forward)
- 15-25 FLAG-Events mit trigger+resolution-Paaren
- Plus Backfill-Historie (limitierte Präzision bei trigger-Datum-Proxies)

Entscheidungsmatrix: [[Backtest-Methodik-Roadmap]].
