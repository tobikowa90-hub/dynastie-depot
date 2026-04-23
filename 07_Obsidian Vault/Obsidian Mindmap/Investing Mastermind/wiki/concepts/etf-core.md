---
title: "ETF-Core"
type: concept
tags: [etf, kern, allokation, diversifikation, depot, iwda, eimi, exusa]
created: 2026-04-10
updated: 2026-04-10
related: [depot-state-april-2026, steuer-architektur, defcon-system]
aliases:
  - "ETF-Core"

---

# ETF-Core — Fundament des Depots (65%)

> 65% des monatlichen Sparplans (617,50€/Monat) fließen in den ETF-Core bei der ING. Das Fundament — breit diversifiziert, kosteneffizient, ohne aktives Eingreifen.

## ETF-Positionen (ING)

| Ticker | Name | Ziel % | Funktion |
|--------|------|--------|----------|
| **IWDA** | iShares Core MSCI World (Acc) | 30% | Globale Marktdominanz, US-Kern |
| **EIMI** | iShares Core MSCI EM IMI | 10% | Schwellenländer + Small Caps |
| **EXUSA** | Xtrackers MSCI World ex USA | 15% | Geopolitischer US-Hedge |
| **AVGC** | Avantis Global Small Cap Value | 10% | Faktor-Prämien (wissenschaftlich) |
| **EWG2** | EUWAX Gold II | 5% | Krisendämpfer, nach 1 Jahr steuerfrei |

## Gesamtallokation des Sparplans

| Block | Anteil | Betrag/Monat | Broker |
|-------|--------|-------------|--------|
| ETF-Core | 65% | 617,50€ | ING |
| Wide-Moat-Satelliten | 30% | 285,00€ | Scalable Capital |
| Gold | 5% | 47,50€ | Scalable Capital |

**US-Hard-Cap:** max. 63% | Ist: ~46,41% | Ziel: ~49,51%  
**Slots gesamt:** 16 (4 ETFs + 11 Aktien + 1 Gold) — alle vergeben.

## Strategie-Prinzipien

- **Thesaurierend** (IWDA, EIMI, EXUSA, AVGC) → Vorabpauschale nutzbar (ING-Freibetrag 1.500–1.600€)
- **Kein Rebalancing via Verkauf** → Sparplan umlenken (Steuer-Bremse)
- **EXUSA als US-Hedge** → Wenn US-Anteil Richtung Hard-Cap (63%), Sparplan auf EXUSA umlenken
- **EWG2 (Gold)** → Einziger Rohstoff im Depot; nach 1 Jahr Haltefrist steuerfrei

## US-Cap-Management

Wenn US-Anteil > 60% (Warnschwelle):
1. IWDA-Sparrate temporär reduzieren
2. EXUSA-Sparrate erhöhen
3. Keine Verkäufe — reine Sparplan-Umleitung

## Verlinkungen

- [[Depot-State-April-2026]] — Aktueller Snapshot (US-Ist vs. US-Ziel)
- [[Steuer-Architektur]] — Vorabpauschale, FIFO-Klon, Freibeträge
- [[DEFCON-System]] — Satelliten-Block (285€/Monat, separate Logik)
- [[Investing-Mastermind-Index]] — Zentralindex
