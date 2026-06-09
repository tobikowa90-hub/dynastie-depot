---
title: "ETF-Core"
type: concept
tags: [etf, kern, allokation, diversifikation, depot, iwda, eimi, avgc, jedi, wqtm]
created: 2026-04-10
updated: 2026-06-09
related: [depot-state-april-2026, steuer-architektur, defcon-system]
aliases:
  - "ETF-Core"

---

# ETF-Core — Fundament des Depots (60%)

> 60% des monatlichen Sparplans (~616€/Monat) fließen in den ETF-Core. Das Fundament — breit diversifiziert, kosteneffizient, ohne aktives Eingreifen. *(Seit Umstrukturierung-2027 / 06-2026: Split 65/30/5 → **60/35/5**; EXUSA raus, Themen-Wetten JEDI + WQTM rein; ETF-Core teils ING [IWDA+EIMI], teils Scalable [AVGC+JEDI+WQTM].)*

## ETF-Positionen

| Ticker | Name | ISIN | Rate/Monat | ~% Gesamt | Broker | Funktion |
|--------|------|------|-----------|-----------|--------|----------|
| **IWDA** | iShares Core MSCI World (Acc) | IE00B4L5Y983 | 257€ | ~25% | ING | Globale Marktdominanz, US-Kern |
| **EIMI** | iShares Core MSCI EM IMI | IE00BKM4GZ66 | 123€ | ~12% | ING | Schwellenländer + Small Caps |
| **AVGC** | Avantis Global Small Cap Value | IE0003R87OG3 | 103€ | ~10% | Scalable | Faktor-Prämien (wissenschaftlich) |
| **JEDI** | VanEck Space Innovators | IE000YU9K6K2 | 82€ | ~8% | Scalable | Themen-Wette / Space |
| **WQTM** | WisdomTree Quantum Computing | IE000W8WMSL2 | 51€ | ~5% | Scalable | Themen-Wette / Quantum |
| **EWG2** | EUWAX Gold II *(Gold-Block, separat)* | — | 51€ | ~5% | Scalable | Krisendämpfer, nach 1 Jahr steuerfrei |

> ETF-Core (60%) = IWDA + EIMI + AVGC + JEDI + WQTM ≈ **616€**. EWG2 ist der separate **Gold-Block (5%, 51€)**. EXUSA (Xtrackers MSCI World ex USA) seit 06/2026 raus.

## Gesamtallokation des Sparplans

| Block | Anteil | Betrag/Monat | Broker |
|-------|--------|-------------|--------|
| ETF-Core | 60% | ~616€ | ING (IWDA+EIMI) + Scalable (AVGC+JEDI+WQTM) |
| Wide-Moat-Satelliten | 35% | 364€ (SOLL-Anker, 3-Tier) | Scalable Capital |
| Gold (EWG2) | 5% | 51€ | Scalable Capital |

Gesamt-Sparrate: **~1.031 €/Monat** (Zieljahr 2058).

**US-Hard-Cap:** max. 63% | Ist: ~46,41%  
**Slots gesamt:** 19 (5 ETFs + 13 Aktien + 1 Gold) — alle vergeben.

## Strategie-Prinzipien

- **Thesaurierend** (IWDA, EIMI, AVGC) → Vorabpauschale nutzbar (ING-Freibetrag 1.500€)
- **Kein Rebalancing via Verkauf** → Sparplan umlenken (Steuer-Bremse)
- **US-Cap-Steuerung** → bei US-Anteil Richtung Hard-Cap (63%) IWDA-Sparrate reduzieren (dedizierter Ex-US-Hedge EXUSA seit 06/2026 entfernt; Hedge-Lever in Überarbeitung — vgl. AVD-2027, `00_Core/KONTEXT.md` §4b)
- **EWG2 (Gold)** → Einziger Rohstoff im Depot; nach 1 Jahr Haltefrist steuerfrei

## US-Cap-Management

Wenn US-Anteil > 60% (Warnschwelle):
1. IWDA-Sparrate temporär reduzieren
2. EIMI-/Ex-US-Faktor-Anteil relativ erhöhen (dedizierter EXUSA-Hedge seit 06/2026 entfernt — Lever-Redesign via AVD-2027, KONTEXT §4b)
3. Keine Verkäufe — reine Sparplan-Umleitung

## Verlinkungen

- [[Depot-State-April-2026]] — Aktueller Snapshot (US-Ist vs. US-Ziel)
- [[steuer-architektur|Steuer-Architektur]] — Vorabpauschale, FIFO-Klon, Freibeträge
- [[DEFCON-System]] — Satelliten-Block (364€ SOLL, 3-Tier, separate Logik)
- [[Investing-Mastermind-Index]] — Zentralindex
