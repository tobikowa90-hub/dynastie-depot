# !CAPEX-FCF-ANALYSIS Master-Vorlage v4.0

**Voraussetzung:** Score >= 80 aus `!Analysiere [TICKER]`
**Stand:** 15.04.2026 | **Kompatibel mit:** DEFCON v3.2, Token-Effizienz v4.0

---

## Schritt 0: Snapshot-First (vor API-Abruf)

1. `00_Core/Faktortabelle.md` laden — Score, FLAG, score_datum pruefen
2. Wenn score_datum < 14 Tage: Fundamentals aus Tabelle uebernehmen, nur Delta abrufen
3. Wenn IFRS-Titel (ASML, RMS, SU): IFRS-Hinweise unten beachten

---

## Auftrag

Erstelle ein vollstaendiges Excel-Dokument (6 Sheets) mit CapEx vs. FCF-Analyse
der letzten 5-6 Geschaeftsjahre.

- **Waehrung:** EUR (aktuelle USD/EUR-Rate via Yahoo Finance ermitteln; Non-US: Xetra-Kurs primaer)
- **Verifizierung:** Quellen gemaess `sources.md` (gleicher Skill-Ordner)
- **Output:** Echte .xlsx-Datei — niemals Markdown-Tabellen
- **Dateiname:** `[TICKER]_CapEx_FCF_Analyse_[YYYY-MM-DD].xlsx`
- **Ablage:** `02_Analysen/`

---

## Sheet-Struktur (exakt nachbilden)

### Sheet 1 — Kerndaten

Spalten: Jahr | Revenue | OpCF | CapEx | FCF | EBIT | NI | SBC | SBC/Revenue % | CapEx/OpCF % | FCF-Marge %

- CAGR (Jahr 1 -> letztes Jahr) fuer alle Kennzahlen als letzte Zeile
- Format: Mio. EUR, Prozente auf 2 Dezimalen
- Highlight: CapEx/OpCF > 25% = gelbe Zelle
- Highlight: SBC/Revenue > 15% = orange Zelle

**IFRS-Titel (ASML, RMS, SU):**
- CapEx = nur Cash-CapEx (PP&E + Intangibles). ROU-Asset-Zugaenge (IFRS 16) NICHT mitzaehlen
- RMS: "Adjusted FCF" != Shibui free_cash_flow — TTM-Backrechnung aus info.freeCashflow
- SU: "Net cash from operations" (nach Steuern!) — IFRS-16 ROU-Zugaenge ausschliessen
- OCF-Toleranz bei Quellenvergleich: +/-15% (IFRS 16 Leasing-Effekt), CapEx-Toleranz: +/-1,5%

### Sheet 2 — Prognose & Szenario (FYn+1 bis FYn+3)

Drei Szenarien. **Branchenspezifisch anpassen** — Defaults nur als Fallback:

| Szenario | Rev-Wachstum | OpCF-Wachstum | CapEx-Wachstum |
|----------|--------------|---------------|----------------|
| Bull     | +8%          | +7%           | +1%            |
| Base     | +5%          | +4%           | +2%            |
| Bear     | +1%          | 0%            | +4%            |

**Anpassungshinweise:**
- Luxury/Consumer Staples (RMS, COST): Rev-Wachstum Bull eher +6%, CapEx stabil
- Halbleiter/Infra (ASML, AVGO, APH): CapEx-Volatilitaet hoeher, Bear CapEx +6-8%
- Software/Asset-light (VEEV, MSFT): CapEx/OpCF strukturell <15%, Sensitivitaet gering
- Versicherung/Holdings (BRK.B, MKL): Float-Logik — FCF-Definition anpassen

Fuer jedes Szenario: Revenue, OpCF, CapEx, FCF und FCF-Marge berechnen.
Wenn Konsensus-Schaetzungen verfuegbar (via Shibui/defeatbeta): diese bevorzugen.

### Sheet 3 — Sensitivitaetstabelle

7x7 Matrix:
- Zeilen: OpCF-Wachstum von -5% bis +8% (in 2%-Schritten + Basis)
- Spalten: CapEx-Wachstum von -5% bis +8% (in 2%-Schritten + Basis)
- Zellwerte: Resultierender FCF in Mio. EUR

Farbampel:
- Gruen: FCF >= Basis +10%
- Gelb: FCF +/-10% um Basis
- Rot: FCF < Basis -10%

### Sheet 4 — Anomalien & Ausreisser

| Jahr | Kennzahl | Wert | Erklaerung |
|------|----------|------|-----------|
| [Jahr] | [Anomalie] | [Wert] | [Ursache, Kontext, ob einmalig oder strukturell] |

Pflicht-Checks:
- CapEx-Spruenge >20% YoY (Akquisitionen? Expansion?)
- FCF-Einbrueche (Working Capital? Einmaleffekte?)
- Revenue-Spruenge (M&A vs. organisch?)
- SBC-Spruenge >3pp YoY (Kompensationsaenderung?)
- IFRS-Titel: Abweichung yfinance vs. IFRS-PDF dokumentieren (Toleranzen siehe Sheet 1)

### Sheet 5 — Charts (eingebettet in Excel)

1. **Stacked Bar Chart:** FCF vs. CapEx (absolute Werte in Mio. EUR)
2. **Dual-Axis Line Chart:** FCF-Marge (%) und CapEx/OpCF-Ratio (%)
3. **SBC-Trend Line:** SBC/Revenue (%) ueber den Zeitraum

Alle Charts: 5-6 Jahre historisch + 3 Jahre Prognose (Base-Szenario).

### Sheet 6 — Executive Summary + DEFCON

DEFCON-Matrix (aus der !Analysiere-Analyse uebernehmen):

| Kategorie | Score | Begruendung |
|-----------|-------|------------|
| Fundamentals (50%) | X/50 | [Kernergebnis] |
| Moat (20%) | X/20 | [Wide/Narrow + Grund] |
| Technicals (10%) | X/10 | [Trend-Zusammenfassung] |
| Insider (10%) | X/10 | [Net Buy/Sell] |
| Sentiment (10%) | X/10 | [Konsensus] |
| **GESAMT** | **X/100** | **DEFCON [1-4]** |

**Zusaetzliche Zeilen:**

| Feld | Wert |
|------|------|
| Depot-Eignung | [Einstiegsreif / Watchlist / Veto] |
| Zielkurs | EUR X (aus DCF oder Konsensus-PT) |
| DEFCON-Status | [1-4 mit Ampel] |
| FLAG | [Kein FLAG / FLAG aktiv: Grund] |
| Tariff Exposure | [X% CN/TW/MY/TH/VN — kein FLAG / Notiz / FLAG aktiv] |
| SBC/Revenue | [X% — unbedenklich / erhoehte Aufmerksamkeit / kritisch] |
| Naechster Trigger | [Earnings-Datum / Event / Quarterly Check] |

---

## Design-Standards

| Element | Formatierung |
|---------|-------------|
| Header | Navy (#1E3A5F), weisser Text, Bold, Schriftgroesse 13 |
| Subheader | Blau (#2E75B6), weisser Text |
| Accent/Positiv | Gruen (#00B050) |
| Warnung/Negativ | Rot (#FF0000) |
| Warnung/Neutral | Gelb (#FFD966) |
| FLAG-Zellen | Rot (#FF0000) Hintergrund, weisser Text |
| Rahmen | Duenn, hellgrau, ueberall |
| Schriftart | Calibri, Groesse 10 |
| Zahlenformat | Alle EUR-Werte mit EUR-Symbol, Prozente mit %-Symbol |
| Spaltenbreite | Auto-Fit, mindestens lesbar |

---

## Daten-Verifizierung (Pflicht)

1. **Primaer:** 10-K / 20-F / Press Releases von Investor Relations
2. **Sekundaer:** AlphaSpread, SimplyWallSt, StockAnalysis, GuruFocus
3. **USD->EUR:** Aktuelle Wechselrate via Yahoo Finance abfragen
4. **CapEx-Definition:** Netto (Kaeufe PP&E - Verkaeufe PP&E)
5. **FCF-Definition:** Operating Cash Flow - CapEx (Standard)
6. **SBC:** Aus Cash Flow Statement oder Notes — nicht aus Income Statement (andere Klassifikation)

Bei Abweichungen zwischen Quellen: konservativsten Wert verwenden und
Abweichung in Sheet 4 (Anomalien) dokumentieren.

**IFRS-Titel:** Zusaetzlich IFRS-PDF als Primaerquelle (siehe INSTRUKTIONEN.md Sec. 14, 16, 21).

---

## Sync-Pflicht nach Abschluss

Nach Erstellung der Excel-Datei:
1. `log.md` (Vault) — Eintrag mit Ticker, Score, Datum
2. `CORE-MEMORY.md` — Score-Register aktualisieren falls geaendert
3. `Faktortabelle.md` — Score + FLAG aktualisieren falls geaendert
