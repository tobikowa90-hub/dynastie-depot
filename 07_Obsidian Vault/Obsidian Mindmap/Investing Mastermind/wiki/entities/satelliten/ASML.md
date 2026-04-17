---
tags: [satellit, aktiv, defcon-3, non-us, ifrs]
ticker: ASML
name: ASML Holding N.V.
sektor: Halbleiter-Equipment / Monopol
ersatz: SNPS
score_aktuell: 66
defcon: 3
flag: "keins"
sparrate: "Volle Rate 33,53€ (Gewicht 1.0, D3 kein FLAG)"
letzteAnalyse: 2026-04-17
score_valid_until: 2026-10-14
naechsterTrigger: "Q1 2026 Earnings 15.04. — QuickCheck nach Zahlen"
updated: 2026-04-17
scoring_notiz_v37: "v3.7 Fix 1 (Interaktionsterm): Wide Moat + Fwd P/E >30 → Fwd-P/E-Subscore hart 0; Wide Moat + P/FCF >35 → P/FCF-Subscore hart 0. Score 68→66, D3 bleibt."
waehrung: EUR
ifrs: true
related_concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]]"
---

# ASML — ASML Holding N.V.

> **DEFCON 🟡 3 | Score 68/100 | Kein FLAG**
> Sparrate: Volle Rate (D3, Gewicht 1.0) | Non-US / IFRS

## Aktuelle Lage (Stand: 06.04.2026)

Erster vollständiger Non-US-Kalibrierungsanker. Score 68 = Wide-Moat-Monopol zu Premium-Bewertung. DEFCON 3 trotz perfektem Moat wegen Bewertungsmarge.

## Scoring-Blöcke (06.04.2026)

| Block | Punkte | Max | Kommentar |
|-------|--------|-----|-----------|
| Fundamentals | 28 | 50 | Fwd P/E 38x, P/FCF ~41x drücken Score |
| Moat | 19 | 20 | Wide Moat — EUV-Monopol, Morningstar bestätigt |
| Technicals | 6 | 10 | Über steigendem 200MA, -15% vom ATH |
| Insider | 7 | 10 | 3 Direktoren-Käufe, keine Verkäufe >€20M |
| Sentiment | 8 | 10 | 11 Buy, 0 Sell, PT-Dispersion -1 |

## Wichtige Kennzahlen

- CapEx/OCF: **12.5%** — weit unter FLAG-Schwelle ✅
- China-Exposure: ~24% — Risk-Map-Notiz, kein FLAG (unter 35%)
- FCF Yield: ~2.4% (Bewertungsproblem, kein Qualitätsproblem)

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

## Wissenschaftliche Basis
- [[5J-Fundamental-Fenster]] — 5J-Perspektive als Pflichtrahmen für alle Fundamentaldaten
- [[FCF-Primacy]] — FCF-Yield und forward P/E als primäre Bewertungsanker; trailing P/E: nur Kontext
- [[Moat-Taxonomie-Morningstar]] — Moat-Prüfung nach 8-Quellen-Schema (Wide/Narrow/None)
- [[Wissenschaftliche-Fundierung-DEFCON]] — 7-Befunde-Matrix: wissenschaftliche Validierung des DEFCON-Systems
