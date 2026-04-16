---
name: dynastie-depot-kalibrierung
version: "3.5"
zieljahr: 2058
system: DEFCON v3.5
stand: "16.04.2026"
description: >
Referenz-Analysen zur Kalibrierung des DEFCON v3.5 Scoring-Systems (AVGO 85, MKL 82, SNPS 76). MUSS vor jeder neuen !Analysiere-Analyse gelesen werden, um konsistente Scores sicherzustellen.
trigger_words:
- Kalibrierung
- Referenz-Analysen
- AVGO
- MKL
- SNPS
- Grenzfall-Referenz
- Score-Kalibrierung
- TMO
- SPGI
- FICO
---
# 🔬 Referenz-Analysen – Analyse-Labor DEFCON v3.5

**Zweck:** Kalibrierungsanker für konsistentes Scoring | **Stand:** 16.04.2026

## 📌 Verwendung dieser Datei

*   **Vor jeder neuen Analyse** kurz die Referenz-Scores checken
*   Eigene Scores gegen AVGO (85) und MKL (82) kalibrieren
*   SNPS (76) als Grenzfall-Referenz für DEFCON 3/4-Entscheidung
*   TMO (62) als Referenz für Wide Moat mit ROIC < WACC + Akquisitionsschulden (⚠️ DEFCON 2)
*   EXPN (61) als Referenz für Watchlist-Kandidaten mit Datenlücken

## 🥇 AVGO – Broadcom Inc. | Score: 85/100 | 🟢 DEFCON 4

**Datum:** 25.03.2026 | **Kurs:** $318.88 | **MC:** $1.51T

| **Kategorie** | **Score** | **Kernbegründung** |
| :---: | :---: | :---: |
| Fundamentals | 43/50 | P/FCF ~22x FY26E, Fabless CapEx/OCF <15%, ROE 56% |
| Moat | 19/20 | Wide Moat (Morningstar-Upgrade), ASIC Lock-In, VMware |
| Technicals | 7/10 | -30% von ATH (3/4), RS vs S&P500 6M +9.84% (2/3), über steigendem 200MA (2/3) |
| Insider | 7/10 | Hock Tan aligned, kein Selling >$20M |
| Sentiment | 9/10 | 44 Analysten Strong Buy, 0% Sell |

**FLAG:** ✅ Kein FLAG (Fabless, CapEx/OCF <15%) **FLAG-Hinweis (post CapEx-FCF-Analyse 25.03.2026):**

⚠️ SBC/Revenue ~11,3% (Q1 FY26) — dilutiv, Non-GAAP verschleiert reale Kosten

⚠️ Tarif-Exposure: ~35% Revenue aus US-Halbleitern, Produktion Malaysia/Thailand

→ Score-Indikation im CapEx-FCF-Excel: 85/100 (–1 gegenüber Vollanalyse)

→ Kalibrierungsanker v3.5: 85 — nächste Vollanalyse bei Q3 FY26 Earnings

**Nächste Aktion:** !CAPEX-FCF-ANALYSIS AVGO Broadcom ✅ (bereits durchgeführt) **Status:** 🟢 Aktiv im Depot – Sparplan läuft

**Scoring-Lektion:** Fabless-Modell = automatisch 9/9 CapEx/OCF. AI-Backlog $73B = Visibility-Bonus bei Sentiment. Referenz für „wie sieht 85/100 aus".

**v3.5-Update (16.04.2026):** PT-Upside aus Technicals entfernt (Double-Counting-Fix). Relative Stärke vs S&P500 +9.84% = 2/3. Score-Shift: 86 → 85. Kalibrierungsanker: 85 = Top-Referenz.

## 🥈 MKL – Markel Group Inc. | Score: 82/100 | 🟢 DEFCON 4

**Datum:** 25.03.2026 | **Kurs:** ~$1.690 | **MC:** $22.1B

| **Kategorie** | **Score** | **Kernbegründung** |
| :---: | :---: | :---: |
| Fundamentals | 42/50 | Fwd PE 12x, Book Value +12% YoY, Float $15B+ |
| Moat | 18/20 | Wide Moat – Specialty Underwriting + Ventures |
| Technicals | 6/10 | +0.61% 6M (in-line), RS vs S&P500 6M -5.34% (0/3), über 200MA (3/3) |
| Insider | 8/10 | Tom Gayner Net Buy Q4 2025, 0.4% Ownership |
| Sentiment | 8/10 | Strong Buy, PT $1.850 (+10%) |

**FLAG:** ✅ Kein FLAG (Versicherung Asset-light) **Nächste Aktion:** !CAPEX-FCF-ANALYSIS MKL Markel (Performance Thread) **Status:** 🟢 BRK.B-Ersatzbank #1 – kein Slot verfügbar (16/16 belegt)

**Scoring-Lektion:** Float-basiertes Modell = CapEx/OCF 9/9 (strukturell). FCF Yield 2/8 durch Float-Logik akzeptiert – Sonderregel Versicherung/Holdings anwenden.

**v3.5-Update:** PT-Upside war +10% (unter beiden Schwellen → 0 Punkte betroffen). RS vs S&P500 6M -5.34% (0.61% MKL vs 5.95% SPY) = 0/3. Score bleibt 82.

## 🥉 SNPS – Synopsys Inc. | Score: 76/100 | 🟡 DEFCON 3

**Datum:** 26.03.2026 | **Kurs:** ~$435 | **MC:** $81B

| **Kategorie** | **Score** | **Kernbegründung** |
| :---: | :---: | :---: |
| Fundamentals | 39/50 | P/FCF ~15x forward, CapEx/OCF 4.1%, Debt $10B Ansys |
| Moat | 18/20 | Wide Moat – EDA-Duopol, Switching Costs maximal |
| Technicals | 4/10 | -33% von ATH (4/4), RS vs S&P500 6M -6.54% (0/3), unter 200MA (0/3) |
| Insider | 7/10 | $2B Buyback autorisiert, kein Selling |
| Sentiment | 8/10 | 14 Analysten Buy-Konsensus |

**FLAG:** ✅ Kein FLAG (CapEx/OCF 4.1%) **Nächste Aktion:** Watchlist – Re-Analyse Q2 FY2026 (Mai 2026) **Status:** 🟡 1 Punkt unter Schwelle – ASML-Ersatzbank #1

**Scoring-Lektion:** Goodwill $26.88B (Ansys) = Bilanz-Malus (-3 Punkte). Non-GAAP bereinigt → 82/100. Primäre Referenz für DEFCON 3/4-Grenzfälle.

**v3.5-Update (16.04.2026):** PT-Upside entfernt (-3). RS vs S&P500 -6.54% = 0/3. Score: 79 → 76. Bleibt DEFCON 3.

## 🔵 SPGI – S&P Global Inc. | Score: 74/100 | 🟡 DEFCON 3

**Datum:** 31.03.2026 | **Kurs:** ~$468 | **MC:** ~$152B

| **Kategorie** | **Score** | **Kernbegründung** |
| :---: | :---: | :---: |
| Fundamentals | 36/50 | P/FCF ~28x fwd, ROIC 7.9-10.4% (Goodwill-verzerrt), Debt/EBITDA ~2.5x |
| Moat | 19/20 | Wide Moat – Ratings-Duopol, Datennetzwerk, regulatorische Moat |
| Technicals | 4/10 | -30% von ATH (3/4), RS vs S&P500 6M -16.20% (0/3), unter 200D-MA (0/3) |
| Insider | 7/10 | Kl. Director-Kauf Feb 2026, kein signifikantes Selling |
| Sentiment | 8/10 | 100% Buy, 0% Sell, Ø PT +36-43% Upside |

**FLAG:** ✅ Kein FLAG (CapEx/OCF strukturell niedrig, Lizenzmodell) **Nächste Aktion:** Re-Analyse nach Q1 2026 Earnings (28.04.2026 – Katalysator) **Status:** 🟡 3 Punkte unter Schwelle – Watchlist

**Scoring-Lektion:** ROIC-Verzerrung durch M&A-Goodwill ($44B IHS Markit 2022) → konservativ 3/8 statt operativer 15-18%. Non-GAAP ROIC bereinigt → ~82/100. Referenz für Goodwill-Bewertungslogik.

**v3.5-Update (16.04.2026):** PT-Upside entfernt (-3). RS vs S&P500 -16.20% = 0/3. Score: 77 → 74. Bleibt DEFCON 3.

## 🔬 TMO – Thermo Fisher Scientific | Score: 62/100 | 🟠 DEFCON 2

**Datum:** 02.04.2026 | **Kurs:** ~$473 (Tariff-Selloff -3.9%) | **MC:** ~$176B

| **Kategorie** | **Score** | **Kernbegründung** |
| :---: | :---: | :---: |
| Fundamentals | 27/50 | Fwd PE 19.2x (verbessert), P/FCF ~27.9x, Net Debt/EBITDA ~3.6x post-Clario, ROIC 9.37% < WACC 9.99%, FCF Yield 3.6% |
| Moat | 17/20 | Wide Moat – PPI-System, Unity Lab ERP Switching Costs, CDMO-Marktführer; konservativ wegen kein frischem Morningstar-Update |
| Technicals | 4/10 | -29.4% von ATH (3/4), RS vs S&P500 6M -7.82% (0/3), unter 200D-MA (0/3) |
| Insider | 4/10 | CEO Casper Verkauf März 2026, niedrige Ownership <0.1% MC; kein bestätigter >$20M-Verkauf in 90T-Fenster |
| Sentiment | 10/10 | 37 Analysten: 23 Buy, 4 Hold, 0 Sell – 0% Sell-Ratio, +41% PT-Upside |

**FLAG:** ✅ Kein FLAG aktiv (CapEx/OCF 18.95%; kein FCF-Negativtrend systemisch; kein bestätigtes Insider-Selling >$20M in 90-Tage-Fenster) ⚠️ **Clario-Beobachtungs-Flag:** Post-Akquisitions-FCF-Stabilität erst nach Q1 Earnings (23.04.2026) verifizierbar **Nächste Aktion:** Re-Analyse nach Q1 Earnings **23. April 2026** — Trigger: FCF-Yield >4% + Net Debt/EBITDA <3.0x = DEFCON 4 möglich **Status:** 🟠 Aktiv im Depot – Score 62 = DEFCON 2 (50% Sparrate). Re-Analyse 23.04.2026 (Q1 Earnings)

**Scoring-Lektion:** ROIC < WACC ist ein harter Malus (2/8), auch bei Wide Moat. M&A-Akquisition ($8.875B Clario, 24.03.2026) verschlechtert Bilanz-Score akut (Net Debt/EBITDA 3.6x = 0/3). CEO-Verkauf senkt Insider-Vertrauen. Fazit: Wide Moat + starkes Sentiment allein retten keinen Fundamentals-Block, der durch Fremdkapital unter Druck steht.

**v3.5-Update (16.04.2026): DEFCON-Wechsel D3→D2 erwartet.** PT-Upside entfernt (-3). RS vs S&P500 -7.82% = 0/3. Score: 65 → 62. TMO war Grenzfall (Schwelle 65). Kein Handlungsbedarf — Q1-Earnings 23.04. triggern ohnehin Re-Analyse.

## 🌍 EXPN – Experian PLC | Score: 61/100 | 🟡 DEFCON 3

**Datum:** 02.04.2026 | **Ticker:** EXPN.L (LSE) | **Kurs:** ~2.759 GBp | **MC:** ~£23 Mrd.

| **Kategorie** | **Score** | **Kernbegründung** |
| :---: | :---: | :---: |
| Fundamentals | 32/50 | Fwd PE 27-33x, ROIC 11.67% (knapp unter 12%-Hürde), Bilanz solide, CapEx asset-light, FCF Cash Conversion 97% |
| Moat | 14/20 | Wide Moat Entry-Level (GuruFocus Score 7) – Datenassets, Switching Costs, regulatorische Barrieren im Kredit-Reporting |
| Technicals | 5/10 | Keine RSI/MACD-Daten verfügbar – konservativ; PT-Spanne 2.878–5.827 GBX, kein Trend-Signal |
| Insider | 3/10 | Kein sauberer 90-Tage-Netto-Kauf/Verkauf-Saldo verifiziert – Pflicht-Malus bis echter Check |
| Sentiment | 7/10 | Ø PT 4.501 GBX (AlphaSpread), 15 Analysten Outperform (Yahoo) |

**FLAG:** ✅ Kein FLAG (Asset-light, kein CapEx-Druck, kein Insider-Selling bestätigt)

**Nächste Aktion:** Watchlist – Live-Prüfung P/FCF + RSI/MACD + 90-Tage-Insider-Check.

Re-Scoring wenn ROIC >12% + PE <25x → Score könnte 74+ erreichen

**Status:** 🟡 Watchlist – kein Einstieg (Score 61 < 80 Minimum, kein freier Slot)

**Scoring-Lektion:** Datenlücken erzwingen konservatives Scoring. Insider 3/10 + Technicals 5/10 trotz gutem Geschäftsmodell, weil unverified = kein Bonus. ROIC 11.67% knapp unter Schwelle kostet -3 Fundamental-Punkte. Referenz für Non-US-Analysen mit unvollständiger Datenbasis.

## 💱 FICO - Fair Isaac Corp. | Score 67/100 | 🟡 DEFCON 3

**Datum:** 03.04.2026 | **Kurs:** $1,089 | **MC:** $25.85B

| **Kategorie** | **Score** | **Begründung/Details** |
| :---: | :---: | :---: |
| Fundamentals | 30/50 | PFCF 34x TTM (verzerrt, Kurscrash -52%), Fwd P/FCF ~19x, ROIC 44-49% Exceptional, CapEx/OCF 4% |
| Moat | 18/20 | Wide Moat — gesetzlicher Standard 90%+ US-Kreditentscheidungen; -2 Pkt reg. Risiko VantageScore |
| Technicals | 4/10 | -52% von ATH (4/4), RS vs S&P500 6M -41.09% (0/3), unter 200D-MA (0/3) |
| Insider | 5/10 | Nur RSU-Grants + Cashless Exercise (erzwungen), kein diskret. Selling |
| Sentiment | 10/10 | 0% Sell-Ratio, Ø PT $2,137 (+100%) |

**FLAG:** ✅ Kein FLAG - CapEx/OCF 4%, kein Insider-Selling

**Nächste Aktion:** Re-Analyse bei VEEV-Schwäche oder Score ≥80

**Status:** 🟡Watchlist Klasse A — VEEV-Ersatz Kandidat #1

**Scoring-Lektion:** TTM-Verzerrung durch -52%-Kurscrash angewendet.

Forward-Metriken deutlich attraktiver (Fwd P/FCF ~19x vs. TTM 34x).

Cashless Exercise (Code M+S, gleicher Tag, Expiry ≤30d) ≠ diskretionärer Verkauf.

**v3.5-Update (16.04.2026):** PT-Upside entfernt (-3). RS vs S&P500 -41.09% = 0/3. Score: 70 → 67. Bleibt DEFCON 3.

## 📊 Score-Kalibrierung auf einen Blick

| **Ticker** | **Score** | **DEFCON** | **Datum** | **Slot** | **Flag** | **Nächste Aktion** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| AVGO | 85/100 | 🟢 4 | 25.03.2026 | Aktiv | ✅ | Sparplan läuft |
| MKL | 82/100 | 🟢 4 | 25.03.2026 | Ersatzbank | ✅ | CapEx-FCF (Perf.) |
| SNPS | 76/100 | 🟡 3 | 26.03.2026 | Ersatzbank | ✅ | Re-Analyse Mai 26 |
| SPGI | 74/100 | 🟡 3 | 31.03.2026 | Watchlist | ✅ | Earnings 28.04.2026 |
| MSFT | 60/100 | 🟡 3 | 26.03.2026 | Aktiv | 🔴 CapEx/OCF 65.3% | Re-Check 29.04.2026 |
| GOOGL | 72/100 | 🟡 3 | 26.03.2026 | — | 🔴 CapEx FY26 ~75% OCF | Kein Einstieg |
| HON | 71/100 | 🟡 3 | 28.03.2026 | — | ✅ | Post-Spinoff 2026 |
| TMO | 62/100 | 🟠 2 | 02.04.2026 | Aktiv | ⚠️ Clario-Watch | Re-Analyse 23.04.2026 |
| EXPN | 61/100 | 🟡 3 | 02.04.2026 | Watchlist | ✅ | P/FCF + Insider-Check |
| FICO | 67/100 | 🟡 3 | 03.04.2026 | Watchlist | ✅ | Re-Analyse VEEV-Schwäche |

*🦅 Beispiele.md | DEFCON v3.5 | Stand: 16.04.2026*

```