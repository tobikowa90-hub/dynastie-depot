---
title: "backtest-ready-forward-verify (Skill)"
type: source
medium: tool
aliases:
  - "backtest-ready-forward-verify"
  - "Backtest-Ready-Forward-Verify"
tags: [skill, persistence, scoring, forward-run]
created: 2026-04-23
updated: 2026-04-23
sources: [backtest-ready-forward-verify]
related: [dynastie-depot-skill, defcon-system, Backtest-Ready-Infrastructure]
---

# backtest-ready-forward-verify (Skill v1.0)

## Rolle

Persistence-Pipeline-Satellit für jede `!Analysiere`-Forward-Vollanalyse. Wird **programmatisch** aus dem [[dynastie-depot-skill]] aufgerufen (Schritt 7) — keine eigenen Trigger-Words.

## Aufgaben

1. Konsumiert ScoreRecord-Draft (JSON) aus dynastie-depot Schritt 7
2. Validiert gegen JSON-Schema + STATE.md-Tripwire
3. Führt §28.2 Algebra-Δ-Gate (conditional) aus
4. Dry-Run + Append an `score_history.jsonl`
5. Gibt strukturierten Report an Aufrufer zurück

## Pfad zur Quelldatei

`C:\Users\tobia\OneDrive\Desktop\Claude Stuff\01_Skills\backtest-ready-forward-verify\`

## Status

**Aktiv seit 19.04.2026** — ersetzt frühere CLI-direkte Score-Persistence. `flag_events.jsonl`-Writes weiterhin direkt via `03_Tools/backtest-ready/archive_flag.py`.

## Verwandte Pages

- [[dynastie-depot-skill]] — Aufrufer
- [[Backtest-Ready-Infrastructure]] — Konzept
- [[defcon-system]] — Scoring-System dahinter
