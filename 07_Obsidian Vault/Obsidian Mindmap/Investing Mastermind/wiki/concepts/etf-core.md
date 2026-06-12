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

> 60% des monatlichen Sparplans (~616€/Monat) fließen in den ETF-Core. Das Fundament — breit diversifiziert, kosteneffizient, ohne aktives Eingreifen. *(Umstrukturierung-2027 / 06-2026: Split 65/30/5 → **60/35/5**; Themen-Wetten JEDI + WQTM rein. **exUSA-Re-Add 2026-06-12:** EXUS [Xtrackers MSCI World ex USA] @82€ reaktiviert als US-Klumpenrisiko-Hedge, intern aus IWDA/AVGC/JEDI finanziert. ETF-Core teils ING [IWDA+EIMI+EXUS], teils Scalable [AVGC+JEDI+WQTM].)*

## ETF-Positionen

| Ticker | Name | ISIN | Rate/Monat | ~% Gesamt | Broker | Funktion |
|--------|------|------|-----------|-----------|--------|----------|
| **IWDA** | iShares Core MSCI World (Acc) | IE00B4L5Y983 | 206€ | ~20% | ING | Globale Marktdominanz, US-Kern |
| **EIMI** | iShares Core MSCI EM IMI | IE00BKM4GZ66 | 123€ | ~12% | ING | Schwellenländer + Small Caps |
| **EXUS** | Xtrackers MSCI World ex USA | IE0006WW1TQ4 | 82€ | ~8% | ING | Geo-Hedge gegen US-Klumpenrisiko (US-Faktor 0, reaktiviert 12.06.) |
| **AVGC** | Avantis Global Small Cap Value | IE0003R87OG3 | 82€ | ~8% | Scalable | Faktor-Prämien (wissenschaftlich) |
| **JEDI** | VanEck Space Innovators | IE000YU9K6K2 | 72€ | ~7% | Scalable | Themen-Wette / Space |
| **WQTM** | WisdomTree Quantum Computing | IE000W8WMSL2 | 51€ | ~5% | Scalable | Themen-Wette / Quantum |
| **EWG2** | EUWAX Gold II *(Gold-Block, separat)* | — | 51€ | ~5% | Scalable | Krisendämpfer, nach 1 Jahr steuerfrei |

> ETF-Core (60%) = IWDA + EIMI + EXUS + AVGC + JEDI + WQTM ≈ **616€**. EWG2 ist der separate **Gold-Block (5%, 51€)**. **EXUS** (Xtrackers MSCI World ex USA) seit 2026-06-12 wieder drin als US-Hedge (war 04.06.–12.06. gestoppt).

## Gesamtallokation des Sparplans

| Block | Anteil | Betrag/Monat | Broker |
|-------|--------|-------------|--------|
| ETF-Core | 60% | ~616€ | ING (IWDA+EIMI+EXUS) + Scalable (AVGC+JEDI+WQTM) |
| Wide-Moat-Satelliten | 35% | 364€ (SOLL-Anker, 3-Tier) | Scalable Capital |
| Gold (EWG2) | 5% | 51€ | Scalable Capital |

Gesamt-Sparrate: **~1.031 €/Monat** (Zieljahr 2058).

**US-Hard-Cap:** max. 63% | Ist: ~53,4% / Ziel ~52,6% (Tool)  
**Slots gesamt:** 20 (6 ETFs + 13 Aktien + 1 Gold) — alle vergeben.

## Strategie-Prinzipien

- **Thesaurierend** (IWDA, EIMI, AVGC) → Vorabpauschale nutzbar (ING-Freibetrag 1.500€)
- **Kein Rebalancing via Verkauf** → Sparplan umlenken (Steuer-Bremse)
- **US-Cap-Steuerung** → bei US-Anteil Richtung Hard-Cap (63%) IWDA-Sparrate reduzieren; **dedizierter Ex-US-Hedge EXUS** (reaktiviert 12.06., US-Faktor 0) senkt US-Anteil direkt
- **EWG2 (Gold)** → Einziger Rohstoff im Depot; nach 1 Jahr Haltefrist steuerfrei

## US-Cap-Management

Wenn US-Anteil > 60% (Warnschwelle):
1. IWDA-Sparrate temporär reduzieren
2. EIMI-/EXUS-/Ex-US-Faktor-Anteil relativ erhöhen (**EXUS = dedizierter World-ex-USA-Hedge, reaktiviert 12.06.**)
3. Keine Verkäufe — reine Sparplan-Umleitung

## Verlinkungen

- [[Depot-State-April-2026]] — Aktueller Snapshot (US-Ist vs. US-Ziel)
- [[steuer-architektur|Steuer-Architektur]] — Vorabpauschale, FIFO-Klon, Freibeträge
- [[DEFCON-System]] — Satelliten-Block (364€ SOLL, 3-Tier, separate Logik)
- [[Investing-Mastermind-Index]] — Zentralindex
