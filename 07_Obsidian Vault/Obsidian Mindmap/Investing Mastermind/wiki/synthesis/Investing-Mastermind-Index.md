---
tags: [index, home, navigation]
---

# 🦅 Investing Mastermind — Zentralindex

> Zieljahr: 2058 | System: DEFCON v3.7 (Skill-Paket v3.7.2) | Stand: 09.06.2026 (Umstrukturierung-2027 Phase-A Vault-Sync)

## 📊 Depot-State

→ [[Depot-State-April-2026]] — Aktueller Snapshot (immer hier beginnen)

---

## 🛰️ Satelliten (aktive Positionen)

> Quelle: [[PORTFOLIO]] (`00_Core/PORTFOLIO.md`, Live-State-SSoT seit Tier-2-Refactor 25.04.2026; vorher `STATE.md`). DEFCON-Thresholds Schema-aligned seit 18.04.: ≥80 D4 / 65-79 D3 / 50-64 D2 / <50 D1. **Sparraten seit Umstrukturierung-2027 (06/2026): 3-Tier-Conviction** — Effektiv-Rate = Tier-Basis (T1 40€ / T2 32€ / T3 18€) × DEFCON-Faktor (D3/4=1,0 · D2=0,5 · D1/🔴FLAG=0). SOLL-Σ **364€** / Funded-Σ **210€** (vormals Equal-Weight-Nenner 8.0 → 35,63€/17,81€).

| Ticker | Tier | DEFCON | Score | Rate | FLAG |
|--------|------|--------|-------|------|------|
| [[BRKB\|BRK.B]] | T3 | 🟡 3 | 71 | 18€ | Insurance-Exception ✅ |
| [[SU]] | T3 | 🟡 3 | 69 | 18€ | Non-US |
| [[RMS]] | T3 | 🟡 3 | 68 | 18€ | Screener-Exception, Non-US |
| [[ASML]] | T2 | 🟡 3 | 68 | 32€ | Non-US |
| [[TMO]] | T3 | 🟡 3 | 67 | 18€ | fcf_trend_neg Resolve-Gate CLEAR |
| [[V]] | T2 | 🟠 2 | 64 | 16€ | ✅ Clean (T2×D2 0,5) |
| [[APH]] | T3 | 🟠 2 | 61 | 0€ | 🔴 Score-basiert |
| [[AVGO]] | T1 | 🟠 2 | 56 | 0€ | 🔴 Insider-Selling ($106M 90d), Q2 04.06. 53→56 |
| [[MSFT]] | T1 | 🟠 2 | 50 | 0€ | 🔴 CapEx/OCF aktiv |
| [[AMZN]] | T1 | 🔴 1 | 42 | 0€ | 🔴 CapEx/OCF TTM 99,2% |
| [[NOW]] | T1 | 🟡 3\* | — (O3) | 40€ | Owner-Add §6.4 (VEEV-Slot, SaaS) |
| [[KYCCF]] | T2 | 🟡 3\* | — (O3) | 32€ | Owner-Add §6.4 (JP/JPY-IFRS) |
| [[ZETA]] | T3 | 🟡 3\* | — (O3) | 18€ | Owner-Add §6.4 (war QuickScreener-Rot) |

> **Exits 06/2026:** [[COST]] (Score 69 eingefroren, LIMIT @863€) · [[VEEV]] (Score 74 eingefroren, → [[NOW]]). Pages behalten als Illustrations-Anker.

---

## 🏦 Ersatzbank & Watchlist

- [[GOOGL]] — MSFT-Ersatz (FLAG aktiv, kein Einstieg)
- [[ZTS]] — VEEV/TMO-Ersatz (⚠️ VEEV exited 06/2026 — Reassignment pending §6/Watchlist; DEFCON 4, bereit)
- [[PEGA]] — Slot-16-Kandidat (Earnings Mai 2026)
- [[MKL]] — BRK.B-Ersatz (Specialty-Versicherung + Holding)
- [[NVDA]] — AVGO-Ersatz (GPU-Marktführer, KI-Infrastruktur)
- [[SNPS]] — ASML-Ersatz (EDA, Ansys-Goodwill-Risiko)
- [[RACE]] — RMS-Ersatz (Luxus, Wide Moat, Non-US)
- [[DE]] — SU-Ersatz (Landmaschinen, Precision-Ag)
- [[SPGI]] — Watchlist (Finanzinfrastruktur, Q1 Earnings 28.04.)

---

## 🧠 Konzepte

- [[DEFCON-System]] — Scoring-Matrix, Schwellen, Sparplan-Formel
- [[CapEx-FLAG]] — Die heilige Regel
- [[ROIC-vs-WACC]] — Harter Malus
- [[Tariff-Exposure-Regel]] — Post Liberation Day
- [[Non-US-Scoring]] — IFRS-Addendum
- [[Analyse-Pipeline]] — Stufe 0 → Entscheidung

---

## 🛠️ Skills & Module

| Skill | Befehl | Funktion |
|-------|--------|----------|
| [[dynastie-depot-skill]] | `!Analysiere`, `!Rebalancing`, `!CAPEX-FCF-ANALYSIS` | Haupt-Skill DEFCON v3.7 (Paket v3.7.2); alle Scoring-Workflows. Schritt 7 delegiert an backtest-ready-forward-verify |
| [[backtest-ready-forward-verify]] | — (programmatisch aus Schritt 7) | Satellit seit 19.04.2026: Forward-Run Persistence-Pipeline (Freshness / Tripwire / §28.2 Δ-Gate / Dry-Run / Append / git add) |
| [[quick-screener]] | `!QuickCheck [TICKER]` | Stufe-0 Vorfilter (P/FCF, ROIC, Moat) |
| [[insider-intelligence]] | `!InsiderScan`, `!FlagCheck` | Form-4-Automatisierung für 8 US-Satelliten |
| [[non-us-fundamentals]] | `!NonUSScan ASML/RMS/SU` | yfinance für europäische Satelliten |

---

## 📡 Datenquellen

- [[defeatbeta]] — US-Fundamentals (Primär: Income, Cash Flow, ROIC, WACC)
- [[Shibui-SQL]] — Technicals + historische Breite + FLAG-Historik
- [[OpenInsider]] — Insider-Pflichtquelle (Spalte "X"/"M" — Gegencheck)

---

## 💰 Kapitalstruktur

- [[etf-core|ETF-Core]] — 65% (617,50€/Monat bei ING: IWDA, EIMI, EXUSA, AVGC, EWG2)
- [[steuer-architektur|Steuer-Architektur]] — Lombardkredit, FIFO-Klon, 10-Jahres-Kaskade, PKV-Wäsche

---

## 📁 Raw

- `raw/earnings/` — Transkripte, Q-Reports
- `raw/macro/` — Tariff-News, Fed-Daten

---

## 📅 Nächste kritische Termine

| Datum | Event |
|-------|-------|
| **23.04.2026** | TMO Q1 Earnings |
| **28.04.2026** | SPGI Q1 Earnings |
| **29.04.2026** | MSFT Q3 FY26 Earnings (FLAG-Review) |
| **Mai 2026** | PEGA Earnings (Slot-16) |
| **Juni 2026** | Sparplan-Booster 11.500€ |
