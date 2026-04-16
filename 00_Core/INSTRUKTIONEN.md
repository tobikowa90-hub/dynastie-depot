# ⚙️ INSTRUKTIONEN.md — Handlungsanweisungen & Skill-Guidance
**Version:** 1.3 | **Stand:** 16.04.2026
> Dieses Dokument beschreibt das WIE — alle Workflows, Befehle, Regeln.
> Für Strategie → KONTEXT.md | Für Erinnerungen → CORE-MEMORY.md

---

## 1. Befehls-Übersicht

| Befehl | Funktion | Dauer |
|--------|----------|-------|
| `!Analysiere [TICKER]` | 100-Punkte-DEFCON-Vollanalyse | ~20–25 min |
| `!CAPEX-FCF-ANALYSIS [TICKER] [NAME]` | Excel-Tiefenanalyse, 6 Sheets | ~25–30 min |
| `!Rebalancing` | Sparplan-Drift-Check + Vorschlag | ~10 min |
| `!QuickCheck [TICKER\|ALL]` | Ampel-Check, kein Deep Dive | ~3–5 min |
| `!Briefing` | Manuelles Morning Briefing (Kurs-Check, FLAGs, Earnings) | ~3-5 min |

---

## 2. Analyse-Pipeline (Stufe 0 → Entscheidung)

```
Impuls / Idee
     ↓
[STUFE 0]  Quick-Screener     → 🟢 weiter | 🟡 Watchlist | 🔴 aussortieren
     ↓ nur 🟢
[STUFE 1]  Stock Report        → Intelligence-Report (Datei)
     ↓
[STUFE 2]  !Analysiere         → DEFCON 100-Punkte-Score
     ↓ nur Score ≥ 80 + kein FLAG
[STUFE 3]  !CAPEX-FCF-ANALYSIS → Excel-Tiefenanalyse
     ↓
[ENTSCHEIDUNG] Einstieg / Watchlist / Veto
```

**Grundprinzip:** Jede Stufe ist ein Tor. Wer es nicht passiert, kommt nicht weiter.

---

## 3. STUFE 0 — Quick-Screener

### Drei harte Filter:

| Filter | 🟢 Grün | 🟡 Gelb | 🔴 Rot |
|--------|---------|---------|--------|
| P/FCF | ≤ 35 | 35–45 | > 45 |
| ROIC | ≥ 15% | 12–15% | < 12% |
| Moat-Proxy | GM > 40% + CAGR > 8% | Eines knapp verfehlt | Eines deutlich verfehlt |

**Sonderregeln:**
- BRK.B, MKL, FFH.TO → P/B statt P/FCF (Float-Modelle)
- COST → strukturell niedrige GM — Exception aktiv
- Versicherungen → Combined Ratio statt ROIC

---

## 4. STUFE 2 — DEFCON-Scoring (100-Punkte-Matrix)

### Befunde-Priming (Pflicht vor jedem Scoring-Start)

**Lies `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` — Befunde-Matrix B1–B11.**
Benenne im Analyse-Output explizit, welche Befunde auf diesen Ticker zutreffen und wie sie das Scoring beeinflussen.

| Befund | Kern | Wirkt auf |
|--------|------|-----------|
| B1 | 5J-Fenster > Spot-Werte | Fundamentals — Trendperspektive |
| B2 | FCF + GM = stabilste Prädiktoren | Fundamentals — Metrik-Priorisierung |
| B3 | Earnings-Quality > Value (Accrual Ratio) | Fundamentals — Qualitäts-Check |
| B4 | 8 Moat-Quellen operativ | Moat-Block |
| B5 | cheap + safe + quality Dreiklang | Gesamt-Urteil |
| B6 | Moat allein ≠ Excess Return (Quality Trap) | Moat + Bewertung kombiniert |
| B7 | Fundamentals > Sentiment > Technicals | Gewichtungs-Disziplin |
| B8 | ROIC + FCF + OpMargin top-ranked (ML) | ROIC-vs-WACC — Malus zwingend |
| B9 | EPS-Growth + Low Leverage stabil | Bilanz-Block + EPS Revision |
| B10 | Chain-of-Thought vor Scoring → bessere Konsistenz | Workflow — erst Reasoning, dann Score |
| B11 | News-Daten: Positivity-Bias; Analyst 43% Strong Buy | Sentiment-Cap 10 Pt. — Korrektiv |

### Gewichtung:

| Block | Gewicht | Metriken |
|-------|---------|---------|
| 🔢 Fundamentals | 50 Pt. | P/FCF, Fwd P/E, Bilanz, CapEx/OCF, ROIC, FCF Yield |
| 🏰 Economic Moat | 20 Pt. | Wide/Narrow/None + Quellen (Morningstar Primär) |
| 📉 Technicals | 10 Pt. | ATH-Abstand, Relative Stärke vs. S&P500 (scored, 0-3), MA-Lage, DCF-Anker |
| 🔴 Insider | 10 Pt. | Net Buy/Sell, Ownership, diskret. Selling >$20M |
| 📊 Sentiment | 10 Pt. | Analyst-Rating, Ø Price Target, Sell-Ratio |

### DEFCON-Schwellen:

| Score | DEFCON | Neueinstieg | Bestand | Sparrate |
|-------|--------|-------------|---------|----------|
| ≥ 80 | 🟢 4 | ✅ Erlaubt | Sparplan voll aktiv | Volle Rate (Gewicht 1.0) |
| 65–79 | 🟡 3 | ❌ Nein | Sparplan weiter aktiv | Volle Rate (Gewicht 1.0) — These intakt, weiter besparen |
| 50–64 | 🟠 2 | ❌ Nein | 50% Sockelbetrag | Reduzierte Rate (Gewicht 0.5) — Position halten, nicht ausbauen |
| < 50 | 🔴 1 | 🛑 Veto | Sparrate eingefroren | 0 € — Auswechslung einleiten |

> **3-Stufen-Logik:** D4/D3 = volle Rate (1.0), D2 = Sockelbetrag 50% (0.5), D1 = eingefroren (0.0). Budget verteilt sich gewichtet: Σ Gewichte ergibt immer 100% des Aktien-Budgets. 🔴 FLAG überschreibt jeden Score → 0 €.

### Automatische FLAGs (score-unabhängig — heilig!):

| Trigger | Konsequenz |
|---------|------------|
| CapEx/OCF > 60% | 🔴 FLAG — Sparrate komplett gestoppt (auch bei DEFCON 4) |
| Negativer FCF-Trend + steigendes CapEx | 🔴 FLAG — Sparrate gestoppt |
| Insider Net-Selling > $20M / 90 Tage (kein 10b5-1 "M") | 🔴 FLAG — Sparrate gestoppt |

> **FLAG überschreibt jeden Score.** Ein DEFCON 4 mit 🔴 FLAG bekommt 0 €. Ein DEFCON 3 mit 🔴 FLAG ebenfalls 0 €. Nur 🔴 FLAGs stoppen die Sparrate — 🟡/🚩 Warnungen lassen die Rate unverändert.

---

## 5. Fundamentals-Scoring (Detailskalen)

| Metrik | Max | Skala |
|--------|-----|-------|
| Fwd P/E | 8 | <15→8 \| 15–20→6–7 \| 20–25→4–5 \| 25–35→2–3 \| >35→0–1 |
| P/FCF | 8 | <15→8 \| 15–22→5–7 \| 22–30→3–4 \| 30–45→1–2 \| >45→0 |
| CapEx/OCF | 9 | <10%→9 \| 10–20%→7–8 \| 20–40%→4–6 \| 40–60%→1–3 \| >60%→0+FLAG |
| ROIC vs WACC | 8 | ROIC>WACC+5%→8 \| +3–5%→6–7 \| +1–3%→4–5 \| ~WACC→2–3 \| <WACC→0–1 |
| FCF Yield | 8 | >6%→8 \| 4–6%→6–7 \| 2–4%→3–5 \| 1–2%→1–2 \| <1%→0 |
| Bilanz | 9 | Net Debt/EBITDA + Current Ratio kombiniert |

**Bonus-Metriken (v3.1-Upgrades, je max 2 Zusatzpunkte):**
SBC/Revenue, Accrual Ratio, GM-Trend, Pricing Power, 200MA Slope, DCF-Anker, EPS Revision, PT-Dispersion, Tariff Exposure

---

## 6. Insider-Scoring — Pflichtregeln

- **Primärquelle:** openinsider.com/[TICKER] — 10b5-1-Spalte "M" prüfen!
- Verkäufe >$20M: Kein "M" in der Spalte = diskretionär = 🔴 FLAG
- Cashless Exercise (Code M+S, gleicher Tag, Expiry ≤30d) ≠ diskretionäres Selling
- Fallback: SEC EDGAR Form 4 / GuruFocus Insiders

---

## 7. Kalibrierungsanker (vor jeder Analyse pflichtlesen!)

| Ticker | Score | DEFCON | Lektion |
|--------|-------|--------|---------|
| AVGO | 85 | 🟢 4 | Fabless-Modell = CapEx/OCF <15%, Referenz für Top-Score |
| MKL | 82 | 🟢 4 | Float-Modell = FCF-Sonderregel, Versicherungs-Exception |
| SNPS | 76 | 🟡 3 | Goodwill-Malus durch Ansys-Akquisition (-3 Punkte) |
| SPGI | 74 | 🟡 3 | ROIC-Verzerrung durch M&A-Goodwill → Non-GAAP ~82 |
| TMO | 62 | 🟠 2 | ROIC < WACC + Akquisitionsschuld = harter Malus trotz Wide Moat (v3.5: D3→D2 Grenzfall) |
| EXPN | 61 | 🟡 3 | Datenlücken erzwingen konservatives Scoring |
| FICO | 67 | 🟡 3 | TTM-Verzerrung durch Kurscrash (-52%); Forward-Metriken deutlich besser (VEEV-Ersatz-Referenz) |

---

## 8. Datenquellen-Logik

| Ticker-Typ | Primärquelle | Fallback |
|-----------|-------------|---------|
| US (NYSE/NASDAQ) | SEC EDGAR (10-K, 10-Q) | GuruFocus / Macrotrends |
| Non-US (ASML, RMS, SU) | GuruFocus + Macrotrends | Yahoo Finance |
| Datenkonflikte | SEC > Drittanbieter | — |

**Standard-Quellen-Reihenfolge:**
1. Kurs: Yahoo Finance / TradingView
2. P/FCF, FCF Yield: AlphaSpread / StockAnalysis
3. Bilanz: SimplyWallSt / GuruFocus
4. CapEx/OCF: SEC 10-K / StockAnalysis
5. ROIC/WACC: GuruFocus / AlphaSpread
6. Moat: Morningstar (Primär)
7. Insider: openinsider.com (Primär) → SEC EDGAR (Fallback)
8. Sentiment: Yahoo Finance / TipRanks

---

## 9. !Rebalancing — Workflow

1. `config.yaml` lesen → aktuellen Portfolio-State laden
2. Drift prüfen: Weicht eine Position >10% von Zielgewichtung ab?
3. Sparplan-Vorschlag erstellen mit **formeller Berechnungsformel:**

**Gewichte:** D4/D3 (kein 🔴 FLAG) = 1.0 | D2 (kein 🔴 FLAG) = 0.5 | D1 / 🔴 FLAG = 0.0

**Formel:** `Einzelrate = Aktien-Budget (285€) / Σ Gewichte × Eigengewicht`

**Rechenbeispiel (aktueller Stand: 9× D4/D3 aktiv, 2× 🔴 eingefroren):**
- Nenner = (9 × 1.0) + (0 × 0.5) = 9.0
- D4/D3-Einzelrate = 285€ / 9.0 × 1.0 = **31,67€**
- D2-Einzelrate (falls vorhanden) = 285€ / Nenner × 0.5
- 🔴/D1-Rate = **0€**
- Summencheck: 9 × 31,67 = 285€ ✓

4. **Steuer-Bremse**: Niemals durch Verkauf rebalancen → Sparplan umleiten
5. US-Cap prüfen: Bleibt US-Exposure unter 63%?

---

## 10. !QuickCheck — Workflow

Für jede Position:

| Check | Grün | Gelb | Rot |
|-------|------|------|-----|
| Earnings-Drift | Keine Überraschung | Miss <5% | Miss >10% |
| Kurs-Drift | <10% unter 200MA | 10–20% | >20% |
| Konsensus-Drift | Stabil/upgrade | Seitwärts | Downgrade |
| Moat-Drift | Wide bestätigt | Nicht geprüft | Downgrade |
| Score-Alter | <6 Monate (score_valid_until) | 4–6 Monate | >6 Monate / abgelaufen |

**Deep-Dive-Trigger (→ automatisch !Analysiere):**
- ≥1 roter Checkpunkt
- FLAG neu aktiv
- Moat-Downgrade auf Narrow/None
- `score_valid_until` überschritten (180 Tage seit score_datum)

**Moat-Drift — drei objektive Auslöser (sofortiger !Analysiere, score-unabhängig):**
1. **Morningstar-Downgrade** Wide → Narrow (Quelle: GuruFocus term/moat-score/TICKER)
2. **Marktanteilsverlust >10%** im Kernsegment — dokumentiert in Earnings Call oder Pressebericht
3. **Gross Margin Rückgang >5 Prozentpunkte** über 4 aufeinanderfolgende Quartale (Shibui + Macrotrends)

**Rhythmus:**
- `!QuickCheck ALL` → 1× monatlich (erster Montag des Monats)
- `!QuickCheck [TICKER]` → innerhalb 48h nach Earnings

---

## 11. CapEx-FCF-Analyse — 6 Excel-Sheets

Trigger: nur bei Score ≥ 80 aus Stufe 2

1. Executive Summary
2. Historische CapEx/FCF-Daten (5–10 Jahre)
3. Szenario-Analyse (Bull / Base / Bear)
4. DCF-Bewertung
5. Peer-Vergleich
6. Risiko-Dashboard

---

## 12. config-Pflege-Pflicht

Nach **jeder** `!Analysiere`-Analyse, Sparplan-Änderung oder FLAG-Update:
- Score + DEFCON in `mainconfig.md` aktualisieren
- FLAGS setzen oder aufheben
- Watchlist-Status aktualisieren
- Termine eintragen
- Neue Version hochladen

---

## 13. Verhaltensregeln (unantastbar)

1. **Quellenpflicht** — jede Zahl mit Web-Quelle [web:X] belegen
2. **Konservativ scoren** — bei Grenzfällen den niedrigeren Score
3. **Kalibrieren** — vor jeder Analyse Beispiele.md lesen
4. **Kein Raten** — bei Unsicherheit nachfragen
5. **EUR/USD explizit** — Währung immer angeben
6. **FLAG heilig** — überschreibt jeden Score
7. **Steuer-Bewusstsein** — bei Verkaufs-Fragen: Abgeltungsteuer 26,375%, FIFO, Freibeträge

---

## 14. Non-US Scoring Addendum (ASML / RMS / SU)

Europäische Satelliten folgen IFRS — nicht US-GAAP. Abweichungen explizit dokumentieren.

**Datensource:** EODHD API (Euronext-Primär, EUR). Routing: IF Non-US → EODHD (nicht Shibui/defeatbeta).

**IFRS-Anpassungen pro Scoring-Block:**

| Block | IFRS-Besonderheit | Handhabung |
|-------|------------------|------------|
| Bilanz | Goodwill wird unter IFRS nicht amortisiert (anders als altes US-GAAP) — Bilanzbild stabiler | Goodwill-Anteil trotzdem prüfen, Malus-Regel identisch |
| CapEx/OCF | IFRS 16 Leasing-Aktivierung erhöht Bilanzvermögen ohne CF-Ausweis | ROU-Asset-Zugänge nicht als CapEx zählen, nur Cash-CapEx |
| Insider-Scoring | Kein Form 4 / OpenInsider für europäische Titel | AFM-Meldungen (ASML): afm.nl/registers | AMF-Meldungen (RMS, SU): amf-france.org — manueller Check, kein API |
| SBC | Hermès: SBC minimal, strukturell kein Problem | Trotzdem SBC/OCF-Check durchführen |

**Kalibrierungsanker Non-US:** Kein dedizierter Anker etabliert (Stand 06.04.2026). ASML dient nach erster vollständiger DEFCON-Analyse als Referenzpunkt für europäische Wide-Moat-Titel.

**Währung:** Scores und Ratios sind währungsneutral. Absolute Zahlen immer in EUR ausweisen. Kursangabe: Xetra-Kurs (EUR) als Primär, ADR-Kurs (USD) als Kontext.

---

## 15. Tariff Exposure — Pflicht-Quellenreihenfolge

Bei jedem `!Analysiere` für US-notierte Titel:

| Priorität | Quelle | Inhalt |
|-----------|--------|--------|
| 1 (Primär) | SEC EDGAR 10-K / 20-F → Abschnitt "Geographic Revenue" | Exakte Revenue-Anteile CN/TW/MY/TH/VN — maschinenlesbar |
| 2 | defeatbeta `get_quarterly_revenue_by_geography` | API-Abruf, schnell verfügbar |
| 3 | Earnings Call Transcript → Management-Kommentar zu Zöllen | Qualitative Einschätzung Supply-Chain-Risiken |
| 4 (Fallback) | Simply Wall St "Company Analysis" | Schätzung — nur wenn keine Primärdaten verfügbar |

**Schwellen:** <15% = kein FLAG | 15–35% = Notiz Risk Map | >35% = FLAG aktiv (Sparrate 0€, -3 Punkte Fundamentals)

---

## 16. Non-US API Sanity Check — Workflow (OCF/CapEx Kreuzverifikation)

**Auslöser:** Nach jeder DEFCON-Analyse eines Non-US-Satelliten (ASML, RMS, SU) ODER wenn yfinance-Daten aktualisiert wurden (Earnings-Zyklus).

**Toleranz:** ±1.5% für CapEx. OCF-Abweichungen bis ~15% zwischen IFRS-EU und US-GAAP-Quellen sind strukturell (IFRS 16 Leasing) — kein API-Drift.

### Schritt 1 — yfinance-Daten abrufen

```bash
cd "01_Skills/non-us-fundamentals"
python eodhd_intel.py detail ASML   # oder RMS / SU
```
Notiere: OCF, CapEx, FCF, CapEx/OCF % für alle 4 Jahrgänge.

### Schritt 2 — Vergleichsquelle abrufen

| Ticker | Primärquelle (IFRS-PDF) | Fallback (Web) |
|--------|------------------------|----------------|
| ASML | asml.com/investors → Q4 Results → Financial Statements PDF | stockanalysis.com/stocks/asml/financials/cash-flow-statement/ |
| RMS | finance.hermes.com → Résultats semestriels | stockanalysis.com/stocks/rms/financials/cash-flow-statement/ |
| SU | se.com/investors → Half-Year Results | stockanalysis.com/stocks/su/financials/cash-flow-statement/ |

**IFRS-Zeilen pro Ticker** (aus SKILL.md Abschnitt "Quarterly API Sanity Check"):
- **ASML:** OCF = "Net cash flows from operating activities" | CapEx = PP&E + Intangibles + Land use rights (China-Erbpacht addieren!)
- **RMS:** OCF = "Cash flows from operating activities" | CapEx = "Purchases of PP&E and intangible assets" (NICHT "Adjusted FCF" verwenden — enthält IFRS-16-Abzüge)
- **SU:** OCF = "Net cash from operating activities" (NACH Steuern!) | CapEx = PP&E + Intangibles (IFRS-16 ROU-Zugänge nicht mitzählen)

### Schritt 3 — Kreuzverifikation

| Metrik | Δ ≤ ±1.5% | Δ 1.5–15% | Δ > 15% |
|--------|-----------|-----------|---------|
| CapEx | ✅ OK | ⚠️ Prüfen ob Intangibles fehlen | 🔴 API-DRIFT-FLAG |
| OCF | ✅ OK | ⚠️ IFRS 16 Leasingeffekt prüfen | 🔴 API-DRIFT-FLAG |

**Bei API-DRIFT-FLAG:** Alle laufenden Analysen für diesen Ticker pausieren, Quelle manuell verifizieren, Befund in CORE-MEMORY.md eintragen.

### Schritt 4 — Bekannte Strukturunterschiede (kein Fehler)

| Ticker | Erwartete OCF-Abweichung | Ursache |
|--------|--------------------------|---------|
| ASML | ~10–12% (IFRS vs. US GAAP) | IFRS 16: Leasingzahlungen → Finanzierungs-CF. yfinance nutzt IFRS-EU (ASML.AS), StockAnalysis nutzt US GAAP (20-F) |
| RMS | gering (nur IFRS) | Kein US-Listing, einheitlich IFRS |
| SU | gering (nur IFRS) | Kein US-Listing, einheitlich IFRS |

### Schritt 5 — CORE-MEMORY aktualisieren

Eintrag: `API Sanity Check [TICKER] [Datum]: CapEx Δ X%, OCF Δ Y% ([Ursache]). FLAG: Ja/Nein.`

---

## 17. Skill-Hierarchie & Aktivierungslogik (v2.0 — 08.04.2026)

**Grundregel:** `dynastie-depot` ist der Monolith. Innerhalb von `!Analysiere`
werden **keine weiteren Skills geladen** — alle Module (defeatbeta, Shibui,
insider_intel.py, WebSearch) werden direkt als Tool-Calls genutzt.
Jeder zusätzliche Skill-Load kostet Token und verliert DEFCON-Kontext.

### Wann wird welcher Skill eigenständig aktiviert?

| Befehl | Skill | Bedingung |
|--------|-------|-----------|
| `!QuickCheck [TICKER\|ALL]` | `quick-screener` | Stufe-0-Vorfilter oder monatlicher Check |
| `!EarningsPreview [TICKER]` | `earnings-preview` | 48h vor Earnings |
| `!EarningsRecap [TICKER]` | `earnings-recap` | 48h nach Earnings |
| `!EarningsCalendar` | `earnings-calendar` | Wöchentlicher Überblick |
| `!InsiderScan` | `insider-intelligence` | Standalone-Scan ohne !Analysiere |
| `!PortfolioRisk` | `risk-metrics-calculation` | Quartalsweise (ab Mai 2026) |
| Moat-Grenzfall (Score 77–82) | `qualitative-valuation` | Optional, wenn Moat entscheidend |
| Dokument-Konflikt / 10-K-Text | `sec-edgar-skill` | Eskalations-Fallback |

### Warum kein Skill-Chaining innerhalb !Analysiere?

Ein Skill-Load liest die jeweilige SKILL.md ohne Kenntnis von:
- DEFCON-Scoring-Skalen und Kalibrierungsankern
- FLAG-Logik und deren Überschreibungsregeln
- config.yaml (aktuelle Positionen, DEFCON-Status)
- Kontext der laufenden Analyse (welcher Ticker, welche Daten schon geladen)

→ Ergebnis wäre generische Analyse statt kontextbewusster DEFCON-Score.
→ Vollständige Dokumentation: `01_Skills/dynastie-depot/PIPELINE.md`

---

## 18. Sync-Pflicht: log.md + CORE-MEMORY.md + Faktortabelle

**Trigger:** Score/FLAG-Änderung, neue Analyse, Systemänderung.

**Reihenfolge (alle drei, immer):**
1. `log.md` (Vault) — technisches Protokoll
2. `CORE-MEMORY.md` (00_Core) — strategisches Gedächtnis (Section 1: Analysen, Section 3: FLAGs, Section 4: Scores)
3. `Faktortabelle.md` — Score + FLAG aktualisieren. Bei FLAG-Änderung: config.yaml manuell sync.

**Nie nur eine der drei Dateien aktualisieren.**

---

## 19. Daten-Update-Klassen (wissenschaftlich fundiert)

| Klasse | Trigger | Frequenz | Felder | Halbwertszeit |
|--------|---------|----------|--------|---------------|
| **A** | Quartalsweise | ~90 Tage | FCF, ROIC, GM, Debt/EBITDA | 18–33 Monate |
| **B** | Earnings-getriggert | 14 Tage nach Earnings | Alle Fundamentals, Score, Guidance | 60% Verfall Monat 1 |
| **C** | Event-getriggert | Sofort | Insider >$20M, Moat-Downgrade, Makro >50 Bps | — |
| **D** | Monatlich | 1×/Monat | Sentiment, Short Interest | — |

Basis: SSRN 2022. 80% DEFCON-Score >12 Monate Halbwertszeit.

---

## 20. Ersatzbank-Aktivierungsprotokoll

| Phase | Trigger | Aktion |
|-------|---------|--------|
| Vorbereiten | DEFCON 2 (Score <65) | Ersatz identifizieren + analysieren |
| Ausführen | DEFCON 1 (<50) ODER Veto | Sparplan umleiten |
| Bedingung | — | Ersatz Score ≥80 + kein FLAG |
| Fallback | Kein geeigneter Ersatz | ETF-Budget erhöhen |

---

## 21. Non-US Scoring Kurzreferenz

ASML/RMS/SU — IFRS-Besonderheiten:
- **IFRS 16 Leasing:** ROU-Asset-Zugänge nicht als CapEx zählen — nur Cash-CapEx
- **RMS:** "Adjusted FCF" ≠ Shibui free_cash_flow — TTM-Backrechnung aus info.freeCashflow
- **SU:** "Net cash from operations" (nach Steuern!) — IFRS-16 ROU-Zugänge nicht mitzählen
- **Insider:** AFM (ASML) / AMF (RMS, SU) — manuell, kein Form 4
- **Toleranz:** ±1,5% CapEx, bis ~15% OCF (IFRS 16-Effekt)

---

## 22. Sparplan-Formel (aktuell 15.04.2026)

**Formel:** `Einzelrate = 285€ / Σ Gewichte × Eigengewicht`
**Gewichte:** D4/D3 (kein 🔴)=1,0 | D2 (kein 🔴)=0,5 | D1/🔴 FLAG=0,0

| Position | Gewicht | Grund |
|----------|---------|-------|
| AVGO | 1,0 | D4 + Clean |
| ASML | 1,0 | D3 (kein 🔴) → volle Rate |
| MSFT | 0,0 | 🔴 FLAG (CapEx) + D2 |
| RMS | 1,0 | D4 + Clean |
| VEEV | 1,0 | D4 + Clean |
| SU | 1,0 | D4 + Clean |
| BRK.B | 1,0 | D4 + Clean |
| V | 1,0 | D4 + Clean |
| TMO | 1,0 | D3 (kein 🔴) → volle Rate |
| APH | 0,0 | 🔴 FLAG |
| COST | 1,0 | D4 + Clean |

**Summe:** 9×1,0 = 9,0 | **Volle Rate:** 31,67€ | **Eingefroren:** 0€
**Check:** 9×31,67 = 285€ ✓

---

## 23. Tariff Exposure Scoring

**Quelle:** 10-K "Geographic Revenue" + Manufacturing Locations
**Malus:** -1 Punkt Fundamentals bei >20% Revenue CN/TW/MY/TH/VN
**FLAG:** >35% → 🔴 FLAG aktiv, -3 Punkte, Sparrate 0€

---

## 24. Morning Briefing (Scheduled Trigger v2.1)

**Trigger-ID:** `trig_01PyAVAxFpjbPkvXq7UrS2uG`
**Frequenz:** Taeglich 10:00 Uhr MESZ (Cron `0 8 * * *` UTC, ~10-15 Min Jitter)
**Modell:** claude-sonnet-4-6 | **Repo:** github.com/tobikowa90-hub/dynastie-depot
**Token-Budget:** ~12-18k/Tag (Mo-Fr), ~2-3k/Tag (Sa-So)
**Prompt-Datei:** `03_Tools/morning-briefing-prompt-v2.md` (Single Source of Truth)

**Scope:** 11 Satelliten + 5 Ersatzbank mit Score (MKL, SNPS, SPGI, RACE, ZTS) = 16 Symbole

**Datenquellen (2 Tiers):**

| Tier | Symbole | Quelle | Status |
|------|---------|--------|--------|
| Shibui | ASML, AVGO, MSFT, TMO, VEEV, V, APH, COST, MKL, SNPS, SPGI, RACE, ZTS (13) | `stock_data_query` P1-Pattern mit `g.code IN(...)` | ✅ Live |
| Yahoo curl | BRK.B (`BRK-B`), RMS (`RMS.PA`), SU (`SU.PA`) (3) | `curl` in Bash | ❌ HTTP 403 — Yahoo blockiert Cloud-IPs. V3-Backlog. |

**Critical Guards im Prompt:**
- 🚨 SUNCOR-TRAP: Shibui `code='SU'` = Suncor Energy. Schneider Electric ist NICHT in Shibui. Nie 'SU' in Shibui-Query.
- 🚨 BERKSHIRE-GAP: BRK.B ist nicht in Shibui indexiert (bestaetigt).
- 🚨 HERMES-GAP: RMS ist nicht in Shibui.
- 🚨 ANTI-HALLUCINATION: Bei fehlenden Daten exakter Fehlertext, keine erfundenen Gruende.
- 🚨 KEIN RETRY: Keine Symbol-Varianten bei Query-Fehlschlag.

**Schwellenwerte:**
| Trigger | Schwelle | Empfehlung |
|---------|----------|------------|
| Kurs-Drop | >10% seit Score | !QuickCheck |
| Kurs-Drop | >20% seit Score | !Analysiere |
| Earnings | <7 Tage | Countdown + !QuickCheck |
| Score-Alter | >90 Tage | Update empfohlen |
| Score-Alter | >180 Tage | !Analysiere dringend |

**Manueller Trigger:** `!Briefing` (identischer Output) oder Desktop App → Routines → Jetzt ausfuehren

**Voraussetzung:** Faktortabelle muss aktuell sein (Sync-Pflicht §25). GitHub-Repo muss gepusht sein (`!SyncBriefing`).

**API-Update-Regel (KRITISCH):** RemoteTrigger-Update ersetzt `ccr`-Objekt KOMPLETT (kein Merge). Immer alle 3 Felder (`environment_id`, `session_context`, `events`) zusammen senden. JSON-Nesting: `parent_tool_use_id`, `session_id`, `type`, `uuid` gehoeren auf **data-Level**, NICHT in message.

**Known Limitations v2.1:**
- BRK.B/RMS/SU-Kurse nicht verfuegbar (Yahoo 403 von Cloud-IPs). Zeigt ehrlich "n.v.".
- Push-Notifications: Kein Routines-Toggle in Claude iOS App. Wartet auf Anthropic-Update.
- `RemoteTrigger run` API-Endpoint ist Noop fuer Cron-basierte Trigger — manuell nur via Desktop App "Jetzt ausfuehren".

---

## 25. Briefing-Sync Shortcuts (GitHub ↔ Local)

**Problem:** Der 10:00-Morning-Briefing-Trigger läuft als Remote-Session auf claude.ai und liest `00_Core/` aus dem **GitHub-Repo** — nicht aus dem lokalen Arbeitsverzeichnis. Jede lokale Änderung an Faktortabelle/CORE-MEMORY/SESSION-HANDOVER muss vor 10:00 gepusht sein, sonst analysiert der Trigger veraltete Daten.

### `!BriefingCheck`

**Zweck:** Schneller Vorab-Check: *Liest der Trigger heute aktuelle Daten?*

**Schritte (Claude führt aus):**
1. `git fetch origin main --quiet`
2. `git diff --stat origin/main -- 00_Core/` — zeigt welche Briefing-Quellen lokal vom Remote abweichen
3. Wenn Unterschiede: Liste ausgeben + Empfehlung `!SyncBriefing`
4. Wenn keine Unterschiede: `✅ Trigger liest aktuellen Stand — kein Push nötig`

**Ausgabeformat:**
```
BriefingCheck [Datum HH:MM]
  Faktortabelle.md     [X Zeilen divergent] / [✅ identisch]
  CORE-MEMORY.md       [X Zeilen divergent] / [✅ identisch]
  SESSION-HANDOVER.md  [X Zeilen divergent] / [✅ identisch]
Empfehlung: [!SyncBriefing ausführen] / [Kein Handeln nötig]
```

### `!SyncBriefing`

**Zweck:** Briefing-relevante `00_Core/`-Änderungen ins Repo pushen — mit Review-Gate.

**Schritte (Claude führt aus):**
1. `git status --short 00_Core/` — welche Dateien modified
2. `git diff 00_Core/` — vollständigen Diff anzeigen
3. **Review-Gate:** User bestätigt *explizit* mit `ja`/`push` bevor committed wird — nie automatisch
4. Nach Bestätigung: `git add 00_Core/Faktortabelle.md 00_Core/CORE-MEMORY.md 00_Core/SESSION-HANDOVER.md 00_Core/INSTRUKTIONEN.md`
5. `git commit -m "Briefing-Sync: <kurze Begründung aus Diff abgeleitet>"`
6. `git push origin main`
7. Verifikation: `git log -1 --format="%h %s"` ausgeben

**Wichtig:**
- **Nur `00_Core/` wird synchronisiert** — keine Skills, Tools, Vault
- **Nie `git add .`** — Pfade explizit
- **Review-Gate ist Pflicht** — kein Auto-Commit
- **Commit-Message-Schema:** `Briefing-Sync: <Inhalt>` (z.B. `Briefing-Sync: RMS 71→69, Sparraten-Logik D3=voll`)

### Reminder (Scheduled Task `briefing-sync-reminder`)

- **Frequenz:** Werktags 09:50
- **Verhalten:** Prüft `00_Core/` auf uncommitted/unpushed Änderungen. Bei Treffern: Reminder-Output für nächste Claude-Code-Session. Kein Auto-Push.
- **Warum 09:50:** 10 Minuten Puffer vor Remote-Trigger um 10:00
- **Manueller Start:** `scheduled-tasks → briefing-sync-reminder → Run now`

### Wann `!SyncBriefing` nötig ist

- Nach jeder DEFCON-Analyse (Score/FLAG-Änderung)
- Nach `CORE-MEMORY.md`-Einträgen (institutionelles Gedächtnis)
- Nach Sparraten-Änderungen in `SESSION-HANDOVER.md`
- Spätestens abends vor Session-Ende, wenn Score-Updates vom Tag noch nicht gepusht sind

### Wann **kein** Push nötig ist

- Reine Skill-/Tool-/Vault-Änderungen (`01_Skills/`, `03_Tools/`, `07_Obsidian Vault/`) — Briefing liest diese nicht
- Work-in-Progress-Analysen (Score noch nicht final) — erst nach Abschluss pushen

---
*🦅 INSTRUKTIONEN.md v1.6 | Dynastie-Depot | Stand: 15.04.2026*
