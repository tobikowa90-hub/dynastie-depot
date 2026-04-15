---
name: non-us-fundamentals
description: >
  Dynastie-Depot Non-US Fundamentals Module v1.1.
  Automatisierte DEFCON-Fundamentaldaten fuer ASML, RMS (Hermes), SU (Schneider Electric)
  via Yahoo Finance (yfinance). Kein API-Key noetig. Schliesst die Shibui/defeatbeta-Luecke
  fuer Non-US-Satelliten. EUR-Kurse, IFRS-Daten, vollstaendiger DEFCON-Block.
  Trigger: !NonUSScan, !NonUSDetail [TICKER], !NonUSPrices
---

# Non-US Fundamentals Module — Dynastie-Depot v1.1

**Stand:** 06.04.2026 | **Zweck:** Automatisierte Fundamentaldaten fuer Non-US-Satelliten
**Ersetzt:** Manueller GuruFocus/Macrotrends-Workflow fuer ASML, RMS, SU

## Architektur

```
Yahoo Finance (yfinance) — kostenlos, kein API-Key
         |
    EUR-Ticker abrufen (ASML.AS / RMS.PA / SU.PA)
         |
    DEFCON-Metriken berechnen:
    CapEx/OCF, Bilanz, Valuation, Margen, GM-Trend
    Technicals (200MA), Analysten, Ownership
         |
    FLAG-Detection: CapEx/OCF > 60%
         |
    Output: DEFCON-ready Markdown-Block (EUR, IFRS)
```

**API-Routing-Regel (Gesamt-System):**

```
IF US_Ticker (NYSE/NASDAQ)
    → Shibui Finance SQL (Technicals, CapEx-Quartale)
    → defeatbeta MCP (Fundamentals-Tiefe)
    → insider_intel.py (Form 4 / SEC EDGAR)

IF Non-US-Ticker (ASML, RMS, SU)
    → eodhd_intel.py (dieses Modul, yfinance)
    → Insider: AFM (ASML) / AMF (RMS, SU) — manuell
```

---

## Non-US Satelliten

| Ticker | yfinance Symbol | Boerse | Berichtsfrequenz | Ersatz-Ticker |
|--------|----------------|--------|------------------|---------------|
| ASML | ASML.AS | Amsterdam (Euronext) | Quarterly (IFRS) | SNPS |
| RMS | RMS.PA | Paris (Euronext) | Semi-annual H1/H2 | RACE |
| SU | SU.PA | Paris (Euronext) | Semi-annual H1/H2 | DE |

**Daten-Toleranz:**
- US-Ticker: ±0.5% Abweichung akzeptabel
- Non-US IFRS-Ticker: ±1.5% (unterschiedliche Konsolidierungsstandards)

---

## Befehle

### !NonUSScan [TICKER | ALL]

Scannt alle 3 Non-US-Satelliten oder einzelnen Ticker. Gibt vollstaendigen DEFCON-Block aus.

```bash
# Alle 3 Non-US-Satelliten
python eodhd_intel.py scan

# Einzelner Ticker
python eodhd_intel.py scan ASML

# Mehrere Ticker
python eodhd_intel.py scan RMS SU

# Nur Uebersichtstabelle
python eodhd_intel.py scan --summary
```

**Output:** Vollstaendiger DEFCON-Fundamentals-Block pro Ticker:
- CapEx/OCF Historik (4 Jahre) + FLAG-Status
- Bilanz (Net Debt/EBITDA, Goodwill, Current Ratio)
- Valuation (Fwd P/E, P/FCF, EV/EBITDA, FCF Yield)
- Margen (GM, FCF-Marge, Net Margin, SBC/Revenue)
- GM-Trend 3 Jahre (Moat-Check)
- Technicals (200MA-Lage, 52W-Distanz, Beta)
- Analysten-Konsensus + Ø Kursziel
- Ownership (Insider %, Institutionen %)

### !NonUSDetail [TICKER]

Identisch zu !NonUSScan fuer einen einzelnen Ticker.

```bash
python eodhd_intel.py detail ASML
python eodhd_intel.py detail RMS
python eodhd_intel.py detail SU
```

### !NonUSPrices

Schneller Kurscheck aller 3 Satelliten mit 200MA-Status.

```bash
python eodhd_intel.py prices
```

**Output:** Kompakte Tabelle: Kurs EUR | SMA-200 | vs. 200MA | 52W-Hoch | Distanz 52W

---

## DEFCON-Metriken (was das Modul liefert)

| Kategorie | Metriken | DEFCON-Scoring |
|-----------|----------|----------------|
| **CapEx/OCF** | 4-Jahres-Historie, CapEx/OCF %, FCF-Marge | FLAG wenn >60% |
| **Bilanz** | Net Debt/EBITDA, Goodwill/Assets, Current Ratio | Scoring-Tabelle |
| **Valuation** | Fwd P/E, P/FCF, EV/EBITDA, FCF Yield, PEG | Scoring-Tabelle |
| **Margen** | Gross Margin, FCF-Marge, Net Margin, SBC/Revenue | Moat-Check |
| **GM-Trend** | Gross Margin 3J (steigend/stabil/fallend) | Moat-Bonus/-Malus |
| **ROIC** | Proxy via EBIT/Invested Capital + ROE + ROA | GuruFocus Verifikation |
| **Technicals** | 200MA-Lage, 52W-Distanz, Beta | Trend-Score |
| **Analysten** | Konsensus-Rating, Ø Kursziel, Upside % | Sentiment-Block |
| **Ownership** | Insider %, Institutionen % | Ownership-Score |

---

## FLAG-Regeln (Non-US)

| Trigger | Schwelle | Konsequenz |
|---------|----------|------------|
| CapEx/OCF | > 60% | FLAG aktiv, Sparrate 0 EUR |
| Negativer FCF-Trend | Steigendes CapEx + sinkende OCF | FLAG aktiv |
| Insider-Selling | AFM/AMF manuell pruefen | FLAG bei Muster |

**Hinweis:** Non-US-Insider unterliegen nicht Form-4-Pflicht (SEC EDGAR).
- **ASML:** AFM (Autoriteit Financiele Markten) — meldepflichtige Transaktionen
- **RMS / SU:** AMF (Autorite des marches financiers) — Transactions des dirigeants
- Prüfung bleibt **manuell** — kein automatisiertes Modul verfügbar

---

## Bekannte Daten-Limitierungen

### RMS (Hermes) — IFRS CapEx-Luecke

**Problem:** yfinance liefert fuer RMS.PA in der Jahres-Cashflow-Tabelle
`Free Cash Flow == Operating Cash Flow` (yfinance IFRS-Datenfehler).

**Workaround (implementiert in v1.1):**
- Jahrgang 2025 (neuestes): CapEx wird aus `info.freeCashflow` und
  `info.operatingCashflow` rueckwaerts berechnet (TTM-Werte)
- Aeltere Jahrgaenge (2024, 2023, 2022): zeigen `n/a` fuer CapEx/FCF
- RMS CapEx real: ca. 1.3B EUR (~24% OCF) — veroeffentlicht im Jahresbericht

**Verifikation:** Hermes Rapport Annuel → Flux de Tresorerie

### ROIC — kein direkter Wert

yfinance liefert keinen ROIC direkt. Das Modul berechnet einen Proxy:
`EBIT * 0.75 / (Total Assets - Current Liabilities)`

**Verifikation immer empfohlen:** `gurufocus.com/term/roic/[TICKER]`

### Semi-Annual Reporting (RMS, SU)

yfinance bezieht Fundamentaldaten aus IFRS-Jahresabschluessen.
H1/H2-Berichte fuehren zu staerkerem Lag gegenueber US-Quartalsberichtern.
Aktuellsten Bericht immer auf IR-Website pruefen.

---

## Integration in !Analysiere Workflow

Bei `!Analysiere [Non-US-TICKER]` (ASML, RMS, SU):

1. Claude fuehrt `python eodhd_intel.py detail [TICKER]` aus
2. Output wird als Fundamentals-Block (Abschnitt 1) in die Analyse eingefuegt
3. Valuation-Metriken werden gegen AlphaSpread-DCF verifiziert
4. Insider-Block bleibt manuell (AFM/AMF-Pflicht)
5. Tariff-Exposure-Check: ASML (CN-Exportrestriktionen) manuell via 20-F

**Bei !Analysiere US-Ticker:** Dieses Modul wird NICHT verwendet.
→ Shibui SQL + defeatbeta MCP (siehe mainSKILL-non-us-fundamentals.md)

---

## Setup (einmalig)

```bash
# Voraussetzung: Python 3.10+ mit yfinance
pip install yfinance

# Test: Einzelnen Ticker scannen
cd "01_Skills/non-us-fundamentals"
python eodhd_intel.py scan ASML

# Test: Alle 3 Non-US-Satelliten
python eodhd_intel.py scan

# Test: Kurscheck
python eodhd_intel.py prices
```

Kein API-Key noetig. yfinance nutzt Yahoo Finance ohne Authentifizierung.

**Windows Encoding (bei Emoji-Ausgabe):**
```bash
PYTHONIOENCODING=utf-8 python eodhd_intel.py scan
```

---

## EODHD-Hinweis (warum nicht EODHD)

EODHD Free-Tier (`subscriptionType: free`) hat **keinen Zugriff auf den
Fundamentals-Endpoint** — 403 Forbidden. Nur Real-Time + EOD Historical Data
sind im Free-Plan enthalten.

yfinance ist die kostenlose Alternative mit vollstaendiger Coverage
fuer EUR-Ticker (ASML.AS, RMS.PA, SU.PA) und liefert alle benoetigten
DEFCON-Metriken ohne API-Key.

---

## Wartung

**Bei Slot-Tausch (Non-US-Satellit wird ausgetauscht):**
1. Neuen Ticker + yfinance-Symbol in `NON_US_SATELLITES` dict eintragen
2. Alten Ticker entfernen
3. `reporting_freq` pruefen: `quarterly` oder `semi-annual`
4. `substitute` aktualisieren (US-Ticker-Ersatz fuer manuelle Recherche)
5. Symbol-Lookup: Yahoo Finance → Suche nach Unternehmensname → Ticker.Boerse

**Bei yfinance-Namensaenderungen:**
- Row-Namen in Cashflow-Statement aendern sich gelegentlich
- `_get_cf_row()` probiert mehrere Namen (Fallback-Liste)
- Bei neuem Namen: `python -c "import yfinance as yf; t=yf.Ticker('TICKER'); print(list(t.cashflow.index))"` → Namen ueberpruefen

---

*Non-US Fundamentals Module v1.1 | Dynastie-Depot | Stand: 06.04.2026*
*Basiert auf yfinance (Yahoo Finance). Kein API-Key erforderlich.*
