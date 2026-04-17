---
name: dynastie-depot-kalibrierung
version: "3.7"
zieljahr: 2058
system: DEFCON v3.7
stand: "17.04.2026"
description: >
Referenz-Analysen zur Kalibrierung des DEFCON v3.7 Scoring-Systems. MUSS vor jeder neuen !Analysiere-Analyse gelesen werden, um konsistente Scores sicherzustellen. v3.7-Zielstruktur: 8 Portfolio-Anker (V, AVGO, BRK.B, ASML, RMS, TMO, MSFT, APH) — jeder demonstriert einen spezifischen v3.7-Mechanismus. Legacy-Anker (MKL, SNPS, SPGI, EXPN, FICO, GOOGL, HON) bleiben als historische Kalibrierungsreferenz bis zum Sweep-Cleanup.
trigger_words:
- Kalibrierung
- Referenz-Analysen
- AVGO
- ASML
- BRK.B
- Quality-Trap
- Grenzfall-Referenz
- Score-Kalibrierung
- TMO
- RMS
- APH
- Fundamentals-Cap
---
# 🔬 Referenz-Analysen – Analyse-Labor DEFCON v3.7

**Zweck:** Kalibrierungsanker für konsistentes Scoring | **Stand:** 17.04.2026 | **System:** DEFCON v3.7

## 📌 Verwendung dieser Datei

*   **Vor jeder neuen Analyse** kurz die Referenz-Scores checken
*   Portfolio-Anker (v3.7-frisch) sind primäre Kalibrierungsquelle — Legacy-Anker nur ergänzend
*   AVGO (84) = Top-D4-Referenz, CapEx-light Fabless — zeigt Quality-Trap-Interaktionsterm am P/FCF-Rand
*   ASML (66) = Non-US/IFRS-Workflow + D3-Grenzfall, Fwd P/E FY27 30,30 Watch → Muster für eodhd_intel.py-Kette [folgt]
*   TMO (63) = Wide Moat mit ROIC < WACC = Quality-Trap differenziert (nur P/FCF-Zweig) — D2-Referenz
*   RMS (68) = Non-US Screener-Exception (Luxus, Quality without growth) [folgt]
*   APH (63) = Score-basierter FLAG + Tariff-Check-Muster [folgt]
*   MSFT (59) = CapEx-FLAG-Veto, FLAG-Auflösungs-Pfad [folgt — Q3-Earnings 29.04.]
*   BRK.B (75) = Insurance-Exception, Float-Logik [folgt]
*   V (86) = absoluter Top-Anker, Payment-Network — Fundamentals-Cap 50 reached [folgt — Q2-Earnings ~22.04.]

## 🥇 AVGO – Broadcom Inc. | Score: 84/100 | 🟢 DEFCON 4

**Datum:** 17.04.2026 (v3.7-Rekalibrierung, Pfad-A — v3.5-Vollanalyse 25.03. + v3.7-Mechanik-Anwendung auf Top-Level) | **MC:** ~$1.51T (Stand 25.03.)
**Rolle:** Top-D4-Referenz | CapEx-light Fabless | Quality-Trap-Interaktionsterm am P/FCF-Rand

### Scoring-Status (v3.7)

| **Feld** | **Wert** |
| :---: | :--- |
| **Gesamtscore v3.7** | **84/100 — 🟢 DEFCON 4** (verifiziert 17.04.) |
| Subscore-Breakdown | **v3.5-Baseline (25.03.)** — v3.7-Subscore-Re-Audit **pending Q3 FY26 Earnings** |
| Delta v3.5→v3.7 | -1 Pkt (85→84), Quelle: Quality-Trap-Anwendung auf Top-Level-Score |
| Live-Verify v3.7 | ❌ AVGO nicht in 3/11 (TMO/ASML/RMS verifiziert) — Q3 FY26 Earnings triggert volle Sub-Audit |

> **Hinweis:** Einzel-Kategorie-Punkte (Fundamentals/Moat/Technicals/Insider/Sentiment) stammen aus v3.5-Analyse vom 25.03. Die v3.7-Mechanik (Quality-Trap, OpM-Scoring, Fundamentals-Cap) wurde für diesen Anker nur auf Gesamtscore-Ebene angewandt — Sub-Audit folgt bei nächsten Earnings.

### v3.7-Mechanismen an AVGO (qualitativ)

1. **Quality-Trap-Interaktionsterm (B6):** Wide Moat + P/FCF ~22x → Grenzbereich 22-35 → P/FCF-Subscore hart gedeckelt auf max. 1 Pkt. (Regel ist binär an der Bandgrenze, kein weicher Cliff.) Fwd P/E ~25x liegt <30, daher P/E-Zweig **nicht** hart 0 — differenzierte Anwendung nur auf P/FCF-Seite.
2. **Operating-Margin-Scoring (B8):** AVGO strukturell hohe OpM → Bonus-Potenzial vorhanden. Exakte Subscore-Punkte (1/2 vs. 2/2) pending Re-Audit — abhängig von GAAP vs. Non-GAAP OpM-Definition, SBC-Bereinigung.
3. **Anti-Double-Counting (v3.7):** SBC/Revenue + Tariff wirken ausschließlich als Fundamentals-Malus, **nicht** zusätzlich auf Moat-Seite — System-Prinzip, das Premium-Qualitäts-Titel vor Doppel-Bestrafung schützt.
4. **Fundamentals-Cap 50:** Für AVGO nicht bindend (v3.5-Fundamentals war 42, v3.7 liegt darunter). Cap greift erst bei Spitzen-Fabless-Titeln mit niedrigem Multiple (V-Kandidat).
5. **Contrast-Case:** ASML (Fwd P/E >30 → P/E-Zweig hart 0 + P/FCF-Zweig hart 0) und TMO (ROIC<WACC-Modifikation) zeigen schärfere Anwendungen des gleichen Mechanismus — AVGO ist die **weichste** der drei Quality-Trap-Aktivierungen.

### FLAG-Status (17.04.2026)

- ⚠️ **Insider-Review aktiv:** $123M Verkäufe letzte 90 Tage (insider_intel.py scan 06.04.). Vermutlich Post-Vesting (Code F/S am gleichen Tag wie A/M). **OpenInsider-Gegencheck Pflicht** vor FLAG-Aktivierung — bisher kein M/X-Auslöser bestätigt → FLAG nicht aktiv, aber Watch.
- ✅ **Kein CapEx-FLAG:** Fabless-Modell, CapEx/OCF strukturell <15% (in Q3 FY25 <5%).
- ⚠️ **SBC-Aufmerksamkeit:** 11,3% — dilutiv, nicht kritisch. Bei >15% wäre -4 Malus.
- ⚠️ **Tariff-Risk-Map-Notiz:** MY/TH-Produktion 35% Revenue. Kein FLAG (unter 50%-Schwelle).

### 🚨 Risk Map

1. **Hyperscaler-Konzentration:** ~40% Revenue aus Top-3-Kunden (Google, Meta, ByteDance). Custom-ASIC-Verlust eines Tier-1 = -15-20% Revenue.
2. **Tariff-Exposure MY/TH:** Verlagerung Kapazitäten kostet 12-18 Monate. Bei Eskalation: Marge temporär -300-500 bps.
3. **SBC-Dilution:** ~$6-7B p.a. Non-GAAP heilig, GAAP-FCF-Yield liegt tiefer.

### 🐂 Bull / 🐻 Bear

**🐂 Bull:** AI-Backlog $73B (Q1 FY26) = 2+ Jahre Visibility. Wide Moat Switching Costs ASIC+VMware. CapEx-light + 60%+ ROE = Free-Cash-Flow-Maschine. Hock Tan Capital Allocation erstklassig.

**🐻 Bear:** Hyperscaler-Konzentrationsrisiko, Fwd-Multiple nicht günstig (Fwd P/E ~25x, P/FCF ~22x), Post-Vesting-Selling-Muster der C-Suite verwirrt Insider-Signal, Tariff-Eskalationspotenzial.

### 🎯 Value Legends (qualitativ, nicht punktscored)

- **Buffett:** Wide Moat + hoher ROE + disziplinierte Kapitalallokation — ja, aber hoher Preis (Fwd P/E 25x) nicht Graham-kompatibel.
- **Lynch:** "10-Bagger abschließen" eher erreicht als vor uns — AVGO bereits $1.5T Market Cap.
- **Fisher:** Exzellente Managementqualität (Tan), klare Wettbewerbsposition — Scuttlebutt positiv.

### Depot-Einordnung

**Status:** 🟢 Aktiv im Depot — Sparplan volle Rate (33,53€)
**Nächste Aktion:** Q3 FY26 Earnings abwarten + OpenInsider-Gegencheck Insider-$123M-FLAG-Review
**Ersatzbank:** NVDA / MRVL (kein formaler Score)

### 📚 Scoring-Lektion (Anker-Rolle)

**AVGO = "So sieht 84/100 unter v3.7 aus":**
- Fabless-CapEx-Modell → strukturell voller CapEx/OCF-Subscore (v3.5 bestätigt, in v3.7 unverändert)
- Wide Moat + Premium-Valuation → Quality-Trap-Interaktionsterm dämpft, **verhindert aber nicht D4**
- Quality-Trap wirkt **differenziert** am P/FCF-Zweig (Band 22-35), P/E-Zweig <30 bleibt regulär scorebar — schärfster Kontrast zu ASML (beide Zweige hart 0 wegen Fwd P/E >30)
- OpM-Scoring-Bonus wirkt richtungs-kompensierend zum Quality-Trap-Abzug — System-Intention: Qualität belohnen ohne Premium-Multiple-Blindheit
- Insider-$123M **allein** triggert keinen FLAG → Pflicht-Gegencheck OpenInsider auf Code M/X vor FLAG-Aktivierung (siehe CORE-MEMORY §7)
- SBC/Revenue + Tariff wirken nur als Fundamentals-Malus, nicht als Moat-Abzug (Anti-Double-Counting-Prinzip v3.7)
- **Subscore-Transparenz:** Wenn Live-Verify fehlt, wird Breakdown als v3.5-Baseline markiert — keine fabrizierte v3.7-Präzision

**Kalibrierungsregel:** Neue Analyse → AVGO-Vergleich. Wenn Kandidat ähnliche CapEx-Struktur + Wide Moat + Premium-Multiple zeigt, erwarte Score-Range 80-85. Über 85 nur bei niedrigerem Multiple (V mit Fwd P/E ~23x).

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
| AVGO | 84/100 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv | ⚠️ Insider-Review | Sparplan voll — OpenInsider-Gegencheck offen |
| MKL | 82/100 | 🟢 4 | 25.03.2026 | Ersatzbank | ✅ | CapEx-FCF (Perf.) |
| SNPS | 76/100 | 🟡 3 | 26.03.2026 | Ersatzbank | ✅ | Re-Analyse Mai 26 |
| SPGI | 74/100 | 🟡 3 | 31.03.2026 | Watchlist | ✅ | Earnings 28.04.2026 |
| MSFT | 60/100 | 🟡 3 | 26.03.2026 | Aktiv | 🔴 CapEx/OCF 65.3% | Re-Check 29.04.2026 |
| GOOGL | 72/100 | 🟡 3 | 26.03.2026 | — | 🔴 CapEx FY26 ~75% OCF | Kein Einstieg |
| HON | 71/100 | 🟡 3 | 28.03.2026 | — | ✅ | Post-Spinoff 2026 |
| TMO | 62/100 | 🟠 2 | 02.04.2026 | Aktiv | ⚠️ Clario-Watch | Re-Analyse 23.04.2026 |
| EXPN | 61/100 | 🟡 3 | 02.04.2026 | Watchlist | ✅ | P/FCF + Insider-Check |
| FICO | 67/100 | 🟡 3 | 03.04.2026 | Watchlist | ✅ | Re-Analyse VEEV-Schwäche |

*🦅 Beispiele.md | DEFCON v3.7 | Stand: 17.04.2026*

---

## 🚧 Rebuild-Status v3.7 (Transitions-Hinweis)

Diese Datei befindet sich im v3.7-Rebuild. Ziel: 8 Portfolio-Anker (V, AVGO, BRK.B, ASML, RMS, TMO, MSFT, APH), jeder demonstriert einen spezifischen v3.7-Mechanismus.

| Anker | Status | Pfad | Mechanismus |
| :---: | :---: | :---: | :--- |
| AVGO | ✅ 17.04. (Gesamtscore + Narrativ) | A (Rekonstruktion) | Quality-Trap am P/FCF-Rand, Fabless — Subscore-Re-Audit Q3 FY26 |
| ASML | ⏳ nächste Session | B (Voll-Analyse) | Non-US IFRS-Workflow, Fwd P/E FY27 Grenzfall, QT beide Zweige |
| BRK.B | ⏳ folgt | A | Insurance-Exception, Float-Logik |
| RMS | ⏳ folgt | A | Non-US Screener-Exception, Luxus |
| APH | ⏳ folgt | A | Score-basierter FLAG, Tariff-Check |
| TMO | ⏳ Q1-Earnings 23.04. | B | Quality-Trap differenziert (nur P/FCF), D2 |
| MSFT | ⏳ Q3-Earnings 29.04. | B | CapEx-FLAG, FLAG-Auflösungs-Pfad |
| V | ⏳ Q2-Earnings ~22.04. | B | Top-Anker, Fundamentals-Cap 50 |

Legacy-Anker (MKL, SNPS, SPGI, EXPN, FICO, GOOGL, HON, TMO v3.5) bleiben als v3.5-Referenz bis Sweep-Cleanup nach Abschluss aller 8 v3.7-Anker.

```