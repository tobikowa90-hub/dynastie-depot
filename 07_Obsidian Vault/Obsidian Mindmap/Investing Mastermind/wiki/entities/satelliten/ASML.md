---
tags: [satellit, aktiv, defcon-3, non-us, ifrs]
ticker: ASML
name: ASML Holding N.V.
sektor: Halbleiter-Equipment / Monopol
ersatz: SNPS
score_aktuell: 68
defcon: 3
flag: "keins"
sparrate: "Volle Rate 33,53€ (Gewicht 1.0, D3 kein FLAG)"
letzteAnalyse: 2026-04-17
score_valid_until: 2026-10-17
naechsterTrigger: "Q2 2026 Earnings + FY27 Fwd-P/E-Watch (30,30 → D3→D4-Pfad bei <30)"
updated: 2026-04-17
scoring_notiz_v37: "v3.7 Post-Q1-Vollanalyse (Pfad B): QT-Interaktionsterm beide Zweige hart 0 (Fwd P/E FY26 30,6x + P/FCF 58,5x). Score 66→68 (+2 Live-Verify-Delta innerhalb Toleranz — GM-Trend-Bonus +1,5pp, EPS-Revision post-Q1)."
waehrung: EUR
ifrs: true
related_concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]]"
---

# ASML — ASML Holding N.V.

> **DEFCON 🟡 3 | Score 68/100 | Kein FLAG** (Stand 17.04.2026, Post-Q1-Vollanalyse Pfad B)
> Sparrate: Volle Rate (D3, Gewicht 1.0) | Non-US / IFRS | Kalibrierungsanker in [[Beispiele.md]] (v3.7-Mechanismus: QT beide Zweige hart 0)

## Aktuelle Lage (Stand: 17.04.2026 — Post-Q1-Vollanalyse Pfad B)

Non-US/IFRS-Kalibrierungsanker v3.7. Score 68 = Wide-Moat-Monopol zu Premium-Bewertung, QT beide Zweige hart 0. Q1 2026 Beat (Rev €8,8B / EPS €7,15 / GM 53,0%), FY26-Guidance auf €36-40B angehoben. Stock -6% post-Earnings trotz Beat (Export-Control-Sorge). China-Systemumsatz strukturell 36% → **19%**. DEFCON 3 trotz perfektem Moat wegen Bewertungsmarge (Fwd P/E 30,6x + P/FCF 58,5x).

## Scoring-Blöcke (17.04.2026, v3.7-frisch)

| Block | Punkte | Max | Kommentar |
|-------|--------|-----|-----------|
| Fundamentals | 28 | 50 | QT beide Zweige hart 0 (Fwd P/E 30,6x + P/FCF 58,5x); Bilanz 8/8, CapEx 8/8, ROIC-Spread +17,19pp 8/8, FCF-Yield 2/8, OpM 2/2 |
| Moat | 20 | 20 | Wide Moat EUV-Monopol + GM-Trend 3J +1,5pp Bonus (Moat-Widening) |
| Technicals | 7 | 10 | -5,3% vom 52W-High 1/4, RS vs. S&P500 3/3, +32,8% über 200D-MA 3/3 |
| Insider | 7 | 10 | Carry-Forward 06.04.: 3 Direktoren-Käufe AFM, keine Verkäufe >€20M (AFM-H1-2026 pending) |
| Sentiment | 6 | 10 | B11-Bias-Malus (35/44 SB = 79,5% → 2/4), Sell 0% Warning 1/3, PT +17,8% 2/3, Dispersion -1, EPS-Rev +1 |

## Wichtige Kennzahlen (17.04.2026, eodhd_intel.py)

- CapEx/OCF: **12,9%** — weit unter FLAG-Schwelle ✅
- China-Systemumsatz: **19%** Q1 (von 36% Q4) — struktureller Shift, weit unter 35%-Schwelle ✅
- FCF-Yield: **1,71%** (Bewertungsproblem, kein Qualitätsproblem)
- FCF-Marge: **33,8%** | ROIC: **26,48%** | WACC: **9,29%** (FRED DGS10 4,29% + 5% ERP) → Spread +17,19pp
- Net Debt/EBITDA: **0,21x** | Goodwill: 9,1% | CR: 1,36
- **Watch:** Fwd P/E FY27 = 30,30 (Grenzfall). <30 → QT-P/E-Zweig deaktiviert → Score +6-8 (D3→D4-Pfad)

## API Sanity Check (abgeschlossen 07.04.2026)

- CapEx-Abweichung: Δ ≤ 3.5% — OK ✅
- OCF-Abweichung: ~10% — strukturell (IFRS 16 vs. ASC 842, Leasingzahlungen)
- Kein API-Drift. FLAG-Schlussfolgerung unter beiden Standards: Clean ✅

## IFRS-Besonderheiten

- Datenquelle: yfinance (ASML.AS) — kein Shibui/defeatbeta für Non-US
- OCF-Toleranz ±15% wenn IFRS-16-Leasingbasis erklärbar
- Insider: AFM-Meldungen (afm.nl) — kein Form 4

## Verlinkungen

- [[DEFCON-System]]
- [[Non-US-Scoring]] — IFRS-Addendum
- [[SNPS]] — Ersatz-Kandidat

## Earnings Preview — Q1 2026 (Stand: 10.04.2026)

**Berichtstag: 15. April 2026** | Quelle: yfinance

### Konsensus-Erwartungen

| Metrik | Konsensus | Low | High | Analysten | Vorjahr | Wachstum |
|--------|-----------|-----|------|-----------|---------|---------|
| EPS | $6,64 | $6,47 | $6,86 | 16 | $6,00 | +10,6% |
| Revenue | $8,65B | $8,10B | $8,91B | 16 | $7,74B | +11,8% |

Enger Spread (~6%) — Markt ist sich relativ einig. Kein hohes Unsicherheitssignal.

### Beat/Miss-Historie (letzte 4 Quartale)

| Quartal | EPS Est | EPS Actual | Surprise | |
|---------|---------|-----------|---------|---|
| Q1 2025 | $5,79 | $6,00 | +3,7% | ✅ Beat |
| Q2 2025 | $5,25 | $5,90 | +12,4% | ✅ Beat |
| Q3 2025 | $5,37 | $5,49 | +2,1% | ✅ Beat |
| Q4 2025 | $7,55 | $7,34 | -2,7% | ❌ Miss |

3 von 4 Quartalen Beat, Ø +4,4%. Q4-Miss war marginal und saisonal erklärbar.

### Analyst-Sentiment

- **44 Analysten:** 84% bullish (37 Buy/Strong Buy), 14% neutral, 2% bearish
- Kursziel Median: **$1.593** (+10% zum Kurs) | Mean: $1.498 | High: $2.000

### Key Watches für 15.04.

1. **High-NA Ramp** — Shipment-Pipeline-Kommentar entscheidender als EPS-Zahl
2. **China-Revenue** (~24%) — jede Aussage zu Exportlizenz-Lage relevant (FLAG-Schwelle >35%)
3. **Gross Margin** — Q1 2025: 54,0% → Q4 2025: 52,1%. Erholung erwartet, >50% = kein Moat-Signal
4. **OCF Q1** — strukturell schwach (Q1 2025: -$58,6M) → nicht als FLAG interpretieren
5. **Backlog** — aktuell ~€36B. Wachsender Backlog > EPS-Beat

### Technicals (10.04.2026)

| | |
|---|---|
| Kurs | $1.448,64 |
| 52W-Range | $614 – $1.547 |
| Abstand ATH | -6,4% |
| 50-Tage-MA | $1.392 (+4,1% darüber) |
| 200-Tage-MA | $1.061 (+36,5% darüber) |

**DEFCON-Kontext:** Q1 ist kein Score-Entscheidungsquartal. Trigger für Re-Analyse: High-NA-Ramp hinter Erwartungen ODER China-Exposure >35%.

## Analyse-Historie

| Datum | Score | DEFCON | Ereignis |
|-------|-------|--------|---------|
| ~März 2026 | 84 | 🟢 4 | Frühere Schätzung |
| 06.04.2026 | 68 | 🟡 3 | Vollanalyse v3.4 — Kalibrierungsanker gesetzt |
| 07.04.2026 | 68 | 🟡 3 | API Sanity Check abgeschlossen ✅ |
| 10.04.2026 | 68 | 🟡 3 | Earnings Preview Q1 2026 erstellt (Berichtstag 15.04.) |
| 17.04.2026 | 66 | 🟡 3 | v3.7 Backtest-Approximation (STATE.md) — Live-Verify ±2 |
| 17.04.2026 | **68** | 🟡 3 | **Post-Q1-Vollanalyse Pfad B (Non-US/IFRS-Workflow-Anker für Beispiele.md).** Daten: eodhd_intel.py + Q1-Actuals. WACC 9,29% (FRED, nicht GuruFocus 18,21%). FCF-Marge 33,8%, ROIC 26,48%, ROIC-WACC-Spread +17,19pp (8/8). QT beide Zweige hart 0 (Fwd P/E FY26 30,6 + P/FCF 58,5). B11 Bias-Malus aktiv (35/44 SB). GM-Trend +1,5pp Bonus. China-Shift 36%→19% post-Q1. Subscores: Fund 28/50 · Moat 20/20 · Tech 7/10 · Insider 7/10 (AFM-H1 pending) · Sent 6/10. FY27-Watch 30,30 → D3→D4 bei <30 (+6-8 Pkt). |

## Wissenschaftliche Basis
- [[5J-Fundamental-Fenster]] — 5J-Perspektive als Pflichtrahmen für alle Fundamentaldaten
- [[FCF-Primacy]] — FCF-Yield und forward P/E als primäre Bewertungsanker; trailing P/E: nur Kontext
- [[Moat-Taxonomie-Morningstar]] — Moat-Prüfung nach 8-Quellen-Schema (Wide/Narrow/None)
- [[Wissenschaftliche-Fundierung-DEFCON]] — 7-Befunde-Matrix: wissenschaftliche Validierung des DEFCON-Systems
