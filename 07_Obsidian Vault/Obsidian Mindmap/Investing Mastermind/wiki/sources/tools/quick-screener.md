---
tags: [skill, tool, screener, stufe-0, pipeline]
status: aktiv
version: "1.0"
stand: 2026-04-06
---

# Quick-Screener — Stufe-0 Vorfilter

> Schnell-Screener des Dynastie-Depot Systems. Beantwortet genau eine Frage: Rechtfertigt dieser Ticker eine tiefere Analyse?

## Drei harte Filter

| Filter | 🟢 Grün | 🟡 Gelb | 🔴 Rot |
|--------|---------|---------|--------|
| P/FCF | ≤ 35 | 35–45 | > 45 |
| ROIC | ≥ 15% | 12–15% | < 12% |
| Moat-Proxy | GM > 40% + CAGR > 8% | Eines knapp verfehlt | Eines deutlich verfehlt |

**Morningstar Override:** Wide-Moat-Rating ersetzt Moat-Proxy komplett.

## Gesamtampel-Logik

- **GRÜN** = Alle drei Filter grün ODER max. einer gelb → `!Analysiere` empfohlen
- **GELB** = Zwei Filter gelb (kein Rot) → Watchlist + Re-Screen-Trigger
- **ROT** = Mindestens ein Filter rot → Aussortiert

## Sonderregeln

| Exception | Anpassung |
|-----------|-----------|
| BRK.B, MKL, FFH.TO | P/FCF → Price/Book < 1.5; ROIC → Combined Ratio < 100% |
| COST | Niedrige GM strukturell — Exception aktiv |
| FLAG-Ticker | Warnhinweis im Output — Screener hebt kein FLAG auf |

## Datenquellen

| Metrik | Primär | Fallback |
|--------|--------|---------|
| P/FCF | StockAnalysis, AlphaSpread | Yahoo Finance |
| ROIC | GuruFocus, AlphaSpread | Manuell berechnen |
| Moat-Proxy | Morningstar (wenn verfügbar) | StockAnalysis + Macrotrends |

## Aktivierung

```bash
# Einzel-Screening (Claude-Befehl)
!QuickCheck [TICKER]

# Batch mit CSV (Python)
python 01_Skills/quick-screener/scripts/screen.py --csv [input.csv]

# Template für Batch generieren
python 01_Skills/quick-screener/scripts/screen.py --yaml config.yaml --generate-template output.csv
```

## Verhaltensregeln

1. **Quellenpflicht** — Jede Metrik mit Web-Quelle belegen
2. **Quellen-Divergenz >20%** → User informieren, konservativeren Wert nehmen
3. **Speed over Depth** — Drei Metriken, klare Antwort, keine Value-Legends
4. **Config-Vorschläge, keine Auto-Edits**

## Verlinkungen

- [[Analyse-Pipeline]] — Stufe-0 im Gesamt-Workflow
- [[DEFCON-System]] — Weiterführende Analyse ab Stufe 2
- [[CapEx-FLAG]] — Screener erkennt keine FLAGs, nur DEFCON
- [[OpenInsider]] — Erst in Stufe 2 relevant, nicht im Screener
- [[dynastie-depot-skill]] — Übergeordneter Monolith
