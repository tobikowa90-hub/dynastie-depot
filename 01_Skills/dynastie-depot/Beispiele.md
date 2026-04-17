---
name: dynastie-depot-kalibrierung
version: "3.7"
zieljahr: 2058
system: DEFCON v3.7
stand: "17.04.2026"
description: >
Referenz-Analysen zur Kalibrierung des DEFCON v3.7 Scoring-Systems. MUSS vor jeder neuen !Analysiere-Analyse gelesen werden, um Workflow-Muster und Mechanismus-Anwendung zu prüfen. Architektur (B-konform, 17.04.2026): v3.7-Voll-Anker AVGO (US/Shibui) + ASML (Non-US/IFRS) als primäre Kalibrierungsquelle. Legacy-Anker (MKL, SNPS, SPGI, TMO-v3.5, EXPN, FICO) bleiben dauerhaft mit v3.5-Zeitstand-Banner als Workflow-Historie — keine Nachkalibrierung. Kanonische Scoring-Regeln liegen in SKILL.md §Scoring-Skalen + §Screener-Exceptions.
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

**Architektur (B-konform, 17.04.2026):**

- **Workflow-Form** = v3.7-Voll-Anker mit vollständigen Subscores und Mechanismus-Anwendung. Primäre Kalibrierungsquelle für neue Analysen.
- **Mechanismen-Form** = SKILL.md §Scoring-Skalen + §Screener-Exceptions. Kanonische Regel-Quelle.
- **Legacy-Form** = v3.5-Anker mit Zeitstand-Banner. Workflow-Historie und Portfolio-Kontext. **Nicht** für Score-Kalibrierung verwenden — nur als Muster-Referenz (M&A-Malus, Goodwill-Bereinigung, Datenlücken-Handling, Insurance-Logik).

**v3.7-Voll-Anker (primär):**

- **AVGO (84)** = Top-D4-Referenz, CapEx-light Fabless, Quality-Trap am P/FCF-Rand differenziert
- **ASML (68)** = Non-US/IFRS-Workflow + D3-Grenzfall, Quality-Trap beide Zweige hart 0, FY27-Watch 30,30 als D3→D4-Pfad

**v3.7-Pending** (folgen bei Earnings-Trigger oder Vollanalyse):
BRK.B, RMS, V, APH, MSFT, TMO, COST — Scoring-Mechanismen jeweils in SKILL.md §Screener-Exceptions dokumentiert; Portfolio-Kontext hier unter Legacy-Ankern oder als Statusnotiz.

## 🧭 Mechanismen-Index

| Mechanismus | Kanonische Regel | Voll-Anker | Legacy-Referenz |
| :--- | :--- | :--- | :--- |
| Quality-Trap Interaktionsterm (B6) | SKILL.md §Scoring-Skalen (Z.359) | AVGO, ASML | — |
| Operating-Margin (B8) | SKILL.md §Fundamentals (Z.349) | AVGO, ASML | — |
| Analyst-Bias-Kalibrierung (B11) | SKILL.md §Sentiment | ASML | — |
| Fundamentals-Cap 50 | SKILL.md §Fundamentals-Cap (Z.373) | ASML | — |
| Anti-Double-Counting | SKILL.md §Scoring-Skalen | AVGO, ASML | — |
| Insurance/Holding Exception | SKILL.md §Screener-Exceptions #1 | BRK.B (pending) | MKL |
| Membership-Yield Exception | SKILL.md §Screener-Exceptions #2 | COST (pending) | — |
| ROIC-Spread-Dominanz | SKILL.md §Screener-Exceptions #3 | RMS (pending) | — |
| QT differenziert (ROIC<WACC) | SKILL.md §Screener-Exceptions #4 | TMO (pending Q1 23.04.) | TMO v3.5 |
| CapEx-FLAG bereinigter Pfad | SKILL.md §Screener-Exceptions #5 | MSFT (pending Q3 29.04.) | — |
| Non-US/IFRS (Pfad B) | SKILL.md §Screener-Exceptions #6 | ASML | EXPN |
| Goodwill-Bereinigung (M&A) | — (Workflow-Pattern) | — | SNPS, SPGI |
| Datenlücken-Handling (Non-US) | — (Workflow-Pattern) | — | EXPN |
| TTM-Verzerrung durch Kurscrash | — (Workflow-Pattern) | — | FICO |

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

## 🔬 ASML – ASML Holding N.V. | Score: 68/100 | 🟡 DEFCON 3

**Datum:** 17.04.2026 (v3.7-Vollanalyse Pfad B, Post-Q1-2026-Earnings) | **Ticker:** ASML.AS / ASML (NASDAQ) | **Kurs:** €1.242,60 | **MC:** €482,3B
**Rolle:** Non-US/IFRS-Workflow-Anker | Quality-Trap **beide Zweige hart 0** | D3-Grenzfall mit D3→D4-Pfad via Fwd P/E FY27

### Scoring-Status (v3.7)

| **Feld** | **Wert** |
| :---: | :--- |
| **Gesamtscore v3.7** | **68/100 — 🟡 DEFCON 3** (Live-Verify 17.04. ✅) |
| Subscore-Breakdown | **v3.7-frisch** — alle 5 Kategorien post-Q1-2026 auditierbar (Ausnahme Insider: AFM-H1-2026 pending, Carry-Forward 06.04.) |
| Delta vs. STATE.md 66 | +2 Pkt (Live-Verify ±2 Toleranz eingehalten — Q1-Beat triggert GM-Trend-Bonus + Sentiment-EPS-Rev-Bonus) |
| Live-Verify v3.7 | ✅ 3/11 (TMO ±1, ASML ±2, RMS ±2) — ASML ist primärer Non-US-Kalibrierungsanker |

### Subscores (v3.7)

| **Kategorie** | **Score** | **Kernbegründung** |
| :---: | :---: | :--- |
| Fundamentals | 28/50 | Fwd P/E 30,6x → **hart 0** (QT B6 P/E-Zweig) · P/FCF 58,5x → **hart 0** (QT B6 P/FCF-Zweig) · Bilanz 8/8 (Net Debt/EBITDA 0,21x, CR 1,36, Goodwill 9,1%) · CapEx/OCF 12,9% → 8/8 · ROIC 26,48% − WACC 9,29% = +17,19pp → 8/8 · FCF Yield 1,71% → 2/8 · OpM strukturell hoch aber B8-Cap → 2/2 |
| Moat | 20/20 | Wide Moat EUV-Monopol (Morningstar bestätigt) · GM-Trend 3J +1,5pp (51,3→51,3→52,8) = Moat-Widening-Bonus · Switching Costs + Netzwerkeffekt Lithographie-Ökosystem |
| Technicals | 7/10 | -5,3% vom 52W-High → 1/4 · RS vs. S&P500 6M positiv → 3/3 · +32,8% über 200D-MA → 3/3 |
| Insider | 7/10 | Carry-Forward 06.04.: 3 Direktoren-Käufe AFM-gemeldet, keine Verkäufe >€20M · AFM-H1-2026-Check **pending** (Formal-Revision bei Veröffentlichung) |
| Sentiment | 6/10 | 35 Analysten Strong-Buy → B11 Malus aktiv (Bias-Warnung: >60% Strong-Buy) → 2/4 · Sell-Ratio 0% → Warning-Flag 1/3 · Ø PT-Upside +17,8% → 2/3 · PT-Dispersion -1 · EPS-Revision post-Q1 +1 |

### v3.7-Mechanismen an ASML (qualitativ)

1. **Quality-Trap-Interaktionsterm (B6) — härteste Aktivierung:** Wide Moat + Fwd P/E 30,6x (≥30) → **P/E-Zweig hart 0**. Wide Moat + P/FCF 58,5x (>35) → **P/FCF-Zweig hart 0**. Beide Zweige gleichzeitig deaktiviert — schärfster Kontrast zu AVGO (nur P/FCF-Zweig am Rand) und TMO (nur P/FCF-Zweig wegen ROIC<WACC-Modifikation). ASML = der einzige Depot-Anker mit beidseitiger QT-Aktivierung.
2. **FY27-Watch als D3→D4-Pfad:** Fwd P/E FY27 liegt bei **30,30** (Grenzfall-Schwelle 30). Bei Rückgang <30 deaktiviert sich der P/E-Zweig → Subscore-Rückgewinn 6-8 Pkt auf Fundamentals → **Score 68 → 74-76, D3 → D4-Kandidat**. Mechanismus demonstriert, wie ein einziger Multiple-Shift eine DEFCON-Stufe heben kann.
3. **Operating-Margin-Scoring (B8):** ASML OpM strukturell >30% → Bonus-Potenzial voll ausgeschöpft → 2/2. B8-Cap greift; zusätzliche OpM-Höhe gibt keine weiteren Pkt. (System-Intention: Qualität belohnen, aber nicht Premium-Bewertung über OpM-Hintertür umgehen.)
4. **Analyst-Bias-Kalibrierung (B11):** 35 von 44 Analysten Strong-Buy (79,5%) → **Bias-Malus aktiv** → Sentiment-Subscore gedeckelt 2/4 (statt 4/4). Sell-Ratio 0% → zusätzliches Warning-Flag. System-Prinzip: einheitliche Bull-Konsensus ist Contrarian-Signal, kein Score-Booster.
5. **Non-US/IFRS-Workflow (Pfad B):** Primär-Datenquelle **eodhd_intel.py** (kein Shibui/defeatbeta für Non-US). WACC via FRED DGS10 (4,29%) + 5% ERP = 9,29% — nicht GuruFocus 18,21% (implausibel, verworfen). IFRS-16-Leasing erklärt strukturelle OCF-Differenz ~10% vs. ASC 842 → OCF-Toleranz ±15% angewandt, kein API-Drift-FLAG.
6. **Anti-Double-Counting:** China-Exposure (19% Q1, von 36% Q4) wirkt als Risk-Map-Notiz, nicht als Moat-Abzug. Tariff-Thema wird auf Fundamentals-Seite nicht doppelt bestraft.

### FLAG-Status (17.04.2026)

- ✅ **Kein CapEx-FLAG:** 12,9% — weit unter 60%-Schwelle.
- ✅ **Kein Tariff-FLAG:** China 19% nach Q1-Earnings — weit unter 35%-Schwelle (Strukturwechsel von 36% Q4 — positiver Shift).
- ✅ **Kein Insider-FLAG:** Keine Verkäufe >€20M in 90T. AFM-H1-2026-Check Routine-Pending, kein Auslöser erwartet.
- ⚠️ **Post-Earnings-Watch:** Kurs -6% am 15.04. trotz Beat + FY26-Guidance-Raise — Markt preist Export-Control-Unsicherheit. Keine FLAG-Aktion, aber Sentiment-Monitor bis Q2-Earnings.

### 🚨 Risk Map

1. **Export-Control-Eskalation:** China-System-Sales 19% (Q1) — jede weitere US/NL-Restriktion trifft direkt. Markt preist Tail-Risk via Post-Earnings-Selloff ein.
2. **High-NA-Ramp-Tempo:** Pipeline-Kommentar in Earnings Calls entscheidender als EPS. Verzögerung >6M = Moat-Relativierung (Konkurrenz-Zeitfenster für Canon Nanoimprint).
3. **Bewertungsmarge — nicht Qualität:** Fwd P/E 30,6x + P/FCF 58,5x sind das Score-Problem, nicht Geschäftsmodell. Multiple-Compression bei Tech-Sektor-Rotation = einziger realistischer Rückschlag-Vektor.

### 🐂 Bull / 🐻 Bear

**🐂 Bull:** Q1-2026 Beat (Rev €8,8B / EPS €7,15 / GM 53,0%) + FY26-Guidance auf €36-40B angehoben. Backlog ~€36B (2+ Jahre Visibility). EUV/High-NA-Monopol strukturell unangefochten. GM-Trend +1,5pp 3J = Moat-Widening. FCF-Marge 33,8%.

**🐻 Bear:** P/FCF 58,5x = bezahlte Perfektion — jeder Beat muss Multiple weiter rechtfertigen. FCF-Yield 1,71% macht Position bei Zinsanstieg bewertungssensitiv. Post-Q1-Selloff (-6% trotz Beat) zeigt Asymmetrie: Geopolitik überstimmt Fundamentals.

### 🎯 Value Legends (qualitativ, nicht punktscored)

- **Buffett:** Wide Moat + ROIC 26,48% + dominante Kapitalposition — ja, aber Preis widerspricht "Fair Price for Great Business"-Heuristik.
- **Lynch:** "Story" klar (Lithographie-Zyklus), aber kein 10-Bagger-Setup mehr — MC €482B.
- **Fisher:** Scuttlebutt konsistent exzellent (Management, F&E, Kundenbindung TSMC/Samsung/Intel).

### Depot-Einordnung

**Status:** 🟢 Aktiv im Depot — Sparplan volle Rate (33,53€, D3 kein FLAG, Gewicht 1,0)
**Nächste Aktion:** Q2-2026-Earnings (Juli) + FY27-Fwd-P/E-Monitoring (<30 = D4-Upgrade-Trigger)
**Ersatzbank:** SNPS (Score 76, Watchlist Ersatz #1)

### 📚 Scoring-Lektion (Anker-Rolle)

**ASML = "So sieht 68/100 unter v3.7 aus":**
- Non-US/IFRS-Pfad: eodhd_intel.py statt Shibui/defeatbeta — WACC via FRED (nicht GuruFocus-Schätzung), OCF-Toleranz ±15% wegen IFRS-16
- Quality-Trap **beidseitig hart 0** → einziger Depot-Anker mit doppelter QT-Aktivierung (Kontrast zu AVGO eins-zu-null und TMO eins-zu-null-differenziert)
- Perfekter Moat-Score (20/20) kompensiert **nicht** doppelte QT-Deckelung → Moat-Maximum garantiert nicht D4
- FY27-Watch 30,30 = quantifizierter D3→D4-Pfad → dokumentiert, wie Multiple-Shift allein Score-Klasse hebt
- B11 Analyst-Bias-Malus aktiv bei Consensus-Tops — 79,5% Strong-Buy wirkt dämpfend, nicht bestätigend
- GM-Trend-Bonus +1,5pp gibt Moat-Widening-Pkt, Offset zur QT-Strafe auf Fundamentals-Seite
- China-Shift 36%→19% post-Q1: struktureller Risk-Abbau, aber Markt preist Export-Control-Tail-Risk trotzdem ein (-6% Selloff)
- **Live-Verify-Delta +2** zeigt Post-Earnings-Refinement (GM-Trend + EPS-Rev) innerhalb v3.7-Toleranz ±2

**Kalibrierungsregel:** Neue Non-US-Analyse mit Wide Moat + Fwd P/E >30 + P/FCF >35 → erwarte Score 65-70, D3 fast garantiert. Fwd P/E <30 bei sonst identischen Werten → +6-8 Pkt, D4-Kandidat. eodhd_intel.py Pflicht-Primärtool für Non-US (nicht Shibui).

## 🥈 MKL – Markel Group Inc. | Score: 82/100 | 🟢 DEFCON 4

> ⚠️ **v3.5-Zeitstand (25.03.2026)** — nicht mehr kanonisch für Scoring. Mechanismen → SKILL.md §Screener-Exceptions #1 (Insurance/Holding). Anker dient als Workflow-Historie und Portfolio-Kontext (BRK.B-Ersatzbank), keine aktuelle v3.7-Score-Aussage.

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

> ⚠️ **v3.5-Zeitstand (26.03.2026, Update 16.04.)** — nicht mehr kanonisch. Scoring-Mechanismen → SKILL.md §Scoring-Skalen. Anker dient als Workflow-Historie und Portfolio-Kontext (ASML-Ersatzbank #1), keine aktuelle v3.7-Score-Aussage. Re-Analyse trigger Q2 FY2026.

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

> ⚠️ **v3.5-Zeitstand (31.03.2026, Update 16.04.)** — nicht mehr kanonisch. Scoring-Mechanismen → SKILL.md §Scoring-Skalen. Anker dient als Workflow-Historie (Goodwill-Bereinigung, Ratings-Duopol) und Portfolio-Kontext (Watchlist), keine aktuelle v3.7-Score-Aussage.

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

> ⚠️ **v3.5-Zeitstand (02.04.2026, Update 16.04.)** — nicht mehr kanonisch. v3.7-Score 63 (Faktortabelle.md). Voll-Analyse v3.7 pending Q1-Earnings 23.04.2026. Mechanismen → SKILL.md §Screener-Exceptions #4 (ROIC<WACC differenzierte QT — nur P/FCF-Zweig). Anker dient als Workflow-Historie (M&A-Bilanz-Malus, Clario-Post-Acq), keine aktuelle v3.7-Score-Aussage.

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

> ⚠️ **v3.5-Zeitstand (02.04.2026)** — nicht mehr kanonisch. Anker dient als Workflow-Historie (Datenlücken-Handling für Non-US-Analysen, konservatives Scoring bei fehlenden Tech-Daten) und Portfolio-Kontext (Watchlist), keine aktuelle v3.7-Score-Aussage. Non-US-Pfad-Mechanismen → SKILL.md §Screener-Exceptions #6.

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

> ⚠️ **v3.5-Zeitstand (03.04.2026, Update 16.04.)** — nicht mehr kanonisch. Anker dient als Workflow-Historie (TTM-Verzerrung durch Kurscrash, Cashless-Exercise ≠ diskretionärer Verkauf) und Portfolio-Kontext (VEEV-Ersatz-Kandidat), keine aktuelle v3.7-Score-Aussage.

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

> ⚠️ **Gemischte Zeitstände:** Nur AVGO (v3.7) und ASML (v3.7) sind aktuelle Scores. Alle anderen Einträge sind v3.5-Legacy-Stände — für aktuelle Portfolio-Scores siehe **Faktortabelle.md** (Single Source of Truth). Tabelle hier dient der Workflow-Kontext-Übersicht.

| **Ticker** | **Score** | **DEFCON** | **Datum** | **Slot** | **Flag** | **Nächste Aktion** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| AVGO | 84/100 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv | ⚠️ Insider-Review | Sparplan voll — OpenInsider-Gegencheck offen |
| ASML | 68/100 | 🟡 3 | 17.04.2026 (v3.7 Pfad B) | Aktiv | ✅ | Q2 2026 + FY27-Fwd-P/E-Watch |
| MKL | 82/100 | 🟢 4 | 25.03.2026 (v3.5) | Ersatzbank | ✅ | CapEx-FCF (Perf.) |
| SNPS | 76/100 | 🟡 3 | 26.03.2026 (v3.5) | Ersatzbank | ✅ | Re-Analyse Mai 26 |
| SPGI | 74/100 | 🟡 3 | 31.03.2026 (v3.5) | Watchlist | ✅ | Earnings 28.04.2026 |
| MSFT | 60/100 | 🟡 3 | 26.03.2026 (v3.5) | Aktiv | 🔴 CapEx/OCF 65.3% | Re-Check 29.04.2026 |
| GOOGL | 72/100 | 🟡 3 | 26.03.2026 (v3.5) | — | 🔴 CapEx FY26 ~75% OCF | Kein Einstieg |
| HON | 71/100 | 🟡 3 | 28.03.2026 | — | ✅ | Post-Spinoff 2026 |
| TMO | 62/100 | 🟠 2 | 02.04.2026 | Aktiv | ⚠️ Clario-Watch | Re-Analyse 23.04.2026 |
| EXPN | 61/100 | 🟡 3 | 02.04.2026 | Watchlist | ✅ | P/FCF + Insider-Check |
| FICO | 67/100 | 🟡 3 | 03.04.2026 | Watchlist | ✅ | Re-Analyse VEEV-Schwäche |

*🦅 Beispiele.md | DEFCON v3.7 | Stand: 17.04.2026*

---

## 🔄 v3.7-Voll-Anker-Status

Architektur-Entscheidung 17.04.2026 (B-konform): **Keine 8-Anker-Vollanalyse erzwungen**. Voll-Form nur bei Earnings-Trigger oder Scoring-Lektion mit neuem Mechanismus-Aspekt. AVGO + ASML genügen als Workflow-Kalibrierung (US/Shibui + Non-US/IFRS). Weitere Voll-Anker entstehen organisch bei regulären Earnings-Analysen.

| Voll-Anker | Trigger | Mechanismus-Fokus |
| :---: | :--- | :--- |
| AVGO ✅ | Q3 FY26 Earnings → Subscore-Re-Audit | Quality-Trap differenziert (P/FCF-Rand) |
| ASML ✅ | abgeschlossen 17.04. (Post-Q1) | QT beide Zweige hart 0, Non-US/IFRS Pfad B |
| TMO ⏳ | Q1 23.04.2026 | QT differenziert (ROIC<WACC) |
| V ⏳ | Q2 FY26 ~22.04.2026 | Fundamentals-Cap 50 |
| MSFT ⏳ | Q3 FY26 29.04.2026 | CapEx-FLAG Auflösungs-Pfad |
| BRK.B ⏳ | Q-Earnings Mai 2026 | Insurance-Exception |
| RMS ⏳ | H1 Juli/Aug 2026 | ROIC-Spread-Dominanz |
| COST ⏳ | Q1 FY27 Dez 2026 | Membership-Yield-Exception |
| APH ⏳ | Q2 23.07.2026 | Score-basierter FLAG |

**Legacy-Anker (MKL, SNPS, SPGI, TMO-v3.5, EXPN, FICO)** bleiben dauerhaft mit v3.5-Zeitstand-Banner als Workflow-Historie — keine Löschung, keine v3.7-Nachkalibrierung. Kanonische Scoring-Regeln liegen in SKILL.md, nicht hier.

```