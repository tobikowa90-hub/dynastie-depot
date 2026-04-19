---
title: "Score-Archiv"
type: concept
tags: [defcon, scoring, infrastructure, history, backtest-ready]
created: 2026-04-17
updated: 2026-04-19
version: v3.7.2
sources: []
related: [DEFCON-System, Analyse-Pipeline, FLAG-Event-Log, Backtest-Ready-Infrastructure, Backtest-Methodik-Roadmap]
wissenschaftlicher_anker: "Infrastruktur für spätere Validierung der 4 DEFCON-Fundierungspapers"
konfidenzstufe: operativ
---

# Score-Archiv

> **Append-only JSONL-Historie aller Score-Records. Unveränderliche Basis für 2028+ Backtest.**

## Zweck

Jede `!Analysiere`-Ausgabe (Vollanalyse, Delta, Rescoring) wird als maschinenlesbarer Record in `05_Archiv/score_history.jsonl` angehängt. Das Archiv ist die **einzige Point-in-Time-Wahrheitsquelle** des Systems — Narrative-Layer (log.md, CORE-MEMORY.md) kann nachträglich editiert werden, das Archiv nicht.

## Schema v1.0 (Auszug)

Pro Record: `schema_version`, `record_id` (`YYYY-MM-DD_TICKER_TYP`), `source` (forward|backfill), `ticker`, `score_datum`, `analyse_typ`, `defcon_version`, `kurs`, `market_cap`, vollständige 5-Block-`scores` (Fundamentals 50 / Moat 20 / Technicals 10 / Insider 10 / Sentiment 10), `score_gesamt`, `defcon_level`, `flags` (aktiv_ids + referenziert), `metriken_roh`, `quellen`, `notizen`.

Volldetails: [`03_Tools/backtest-ready/schemas.py`](../../../../../03_Tools/backtest-ready/schemas.py) → `ScoreRecord`.

## Write-Trigger

SKILL.md **Schritt 7 (Archiv-Write Pflicht)** nach jeder `!Analysiere`. **Seit 19.04.2026 (dynastie-depot v3.7.2)** wird die Persistence-Pipeline über den Satelliten-Skill [`backtest-ready-forward-verify`](../../../../../01_Skills/backtest-ready-forward-verify/SKILL.md) orchestriert:

```
Draft → Skill(args=<pfad>) → P1 Schema-Validation → P2a Freshness + P2b STATE.md-Tripwire
      → P3 §28.2 Δ-Gate (conditional, injiziert MigrationEvent) → P4 --dry-run → P5 Append → P6 git add
```

Der Skill ruft intern weiterhin `archive_score.py`; Unterschied zur v3.7.1-Ära: Pipeline-Disziplin (Tripwire, Δ-Gate, Freshness-Warnung) wird mechanisch durchgesetzt statt Prosa-Anweisung.

Validiert via Pydantic: Arithmetik-Check (`score_gesamt` = Summe 5 Blöcke), DEFCON-Konsistenz, Quality-Trap-Interaktionsterm (v3.7), `record_id`-Uniqueness, Forward-Datum-Window (≤3 Tage). Zusätzlich seit v3.7.2: `MigrationEvent._check_delta` + `_check_outcome_bucket` (§28.2 Buckets self-validating).

## Abgrenzung zu Faktortabelle

| Aspekt | Faktortabelle.md | Score-Archiv |
|--------|-------------------|--------------|
| Zweck | Aktueller Zustand | Point-in-Time-Historie |
| Mutation | Überschreiben | Append-only |
| Lesbar für | Mensch (Markdown) | Maschine + Mensch (JSONL) |
| Detail | Score + FLAG pro Ticker | Vollständige Sub-Score-Breakdown + Rohmetriken |

## Backfill-Stand (17.04.2026, einmalig)

24 Backfill-Records aus CORE-MEMORY Section 4 rekonstruiert. Sub-Score-Breakdown nicht rekonstruierbar → Fractional-Split 50/20/10/10/10, Sub-Scores 0 als ehrliche "nicht-rekonstruierbar"-Platzhalter. `defcon_version: "historical"`, `moat.rating: "narrow"` (Quality-Trap-Validator deaktiviert bei Backfill).

## Review 2028-04-01

Wenn Forward-Historie (~15-25 Records pro Jahr) genug Sample-Size erreicht hat: Entscheidung über formalen Backtest — siehe [[Backtest-Methodik-Roadmap]].

## Retrospective-Validation (§29 + Papers)

Das Score-Archiv ist die Datengrundlage für §29-Retrospective-Analysen (ab 2028):

- **§29.1 (PBO/CSCV)** — erfordert score_history.jsonl mit sauberen Forward-Records; PBO<0,05 als Reject-Schwelle, siehe [[Bailey-2015-PBO]] / [[PBO-Backtest-Overfitting]]
- **§29.2 (AQR-Benchmark)** — Aggregiertes Portfolio-SR gegen AQR/Ilmanen-Band, siehe [[Aghassi-2023-Fact-Fiction]]
- **§29.5 (Seven-Sins-Pre-Flight)** — Sin #2 Look-Ahead pflicht via `source="forward"` Records, siehe [[Seven-Sins-Backtesting]]

→ Schema-Disziplin (siehe §18 + §28) schützt die Retrospective-Datenbasis.
