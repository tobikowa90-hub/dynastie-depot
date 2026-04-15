---
name: insider-intelligence
description: >
  Dynastie-Depot Insider Intelligence Module v1.0.
  Automatisiertes Form-4-Scanning der 8 US-Satelliten via SEC EDGAR API.
  Ersetzt den generischen sec-edgar-skill fuer den DEFCON-Insider-Scoring-Block.
  Trigger: !InsiderScan, !FlagCheck, !InsiderDetail [TICKER]
---

# Insider Intelligence Module — Dynastie-Depot v1.0

**Stand:** 06.04.2026 | **Zweck:** Automatisierter DEFCON-Insider-Block (10 Punkte)
**Ersetzt:** Generischer sec-edgar-skill (bleibt als Recherche-Fallback)

## Architektur

```
SEC EDGAR API (kostenlos, User-Agent-only)
         |
    Form 4 XML abrufen + parsen
         |
    Transaktions-Klassifikation
    (Diskretionaer / 10b5-1 / Cashless Exercise / Grant)
         |
    DEFCON Insider-Score berechnen (7/10 automatisch)
    + FLAG-Detection (>$20M diskretionaer in 90d)
         |
    Output: DEFCON-ready Markdown-Block
```

**Was automatisiert wird:**
- Form-4-Abruf fuer alle 8 US-Satelliten (CIK hardcoded)
- Transaktionscode-Analyse: S (diskretionaer) vs. 10b5-1 Plan vs. Cashless Exercise
- Net Buy/Sell Berechnung (90d / 180d / 12M Fenster)
- FLAG-Erkennung: >$20M diskretionaere Verkaeufe in 90 Tagen
- DEFCON-Scoring: 7 von 10 Punkten (Net Buy + No-FLAG)

**Was manuell bleibt:**
- Ownership-Score (3/10) — benoetigt Market Cap via Shibui `share_stats.percent_insiders`
- Non-US Insider (ASML, RMS, SU) — keine Form-4-Pflicht, weiter manuell via AFM/AMF
- OpenInsider Gegencheck bei Grenzfaellen — bleibt HEILIG als Verifikationsquelle

---

## CIK-Tabelle (8 US-Satelliten)

| Ticker | CIK | Unternehmen | Boerse |
|--------|-----|-------------|--------|
| AVGO | 0001730168 | Broadcom Inc. | NASDAQ |
| MSFT | 0000789019 | Microsoft Corporation | NASDAQ |
| V | 0001403161 | Visa Inc. | NYSE |
| BRK.B | 0001067983 | Berkshire Hathaway Inc. | NYSE |
| TMO | 0000097745 | Thermo Fisher Scientific | NYSE |
| VEEV | 0001393052 | Veeva Systems Inc. | NYSE |
| APH | 0000820313 | Amphenol Corporation | NYSE |
| COST | 0000909832 | Costco Wholesale Corporation | NASDAQ |

**Bei Slot-Tausch:** CIK des neuen Tickers in `SATELLITES_CIK` dict im Python-Script aktualisieren.
CIK-Lookup: `https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=[TICKER]&action=getcompany`

---

## Befehle

### !InsiderScan [TICKER | ALL]

Scannt Form-4-Filings der letzten 180 Tage und berechnet DEFCON-Metriken.

```bash
# Alle 8 US-Satelliten scannen
python insider_intel.py scan

# Nur bestimmte Ticker
python insider_intel.py scan AVGO MSFT TMO

# JSON-Output (fuer programmatische Weiterverarbeitung)
python insider_intel.py scan --json
```

**Output:** DEFCON-Insider-Block pro Ticker mit:
- FLAG-Status (aktiv/inaktiv)
- Zeitfenster-Tabelle (90d / 180d / 12M)
- Transaktions-Zusammenfassung
- Scoring-Komponenten (7/10 automatisch)
- FLAG-relevante Einzeltransaktionen (>$1M diskretionaer)
- Top Insider Holdings

### !FlagCheck

Schneller FLAG-Status aller 8 Satelliten — nur 90-Tage-Fenster.

```bash
python insider_intel.py flag-check
```

**Output:** Kompakte Tabelle mit FLAG/Clean-Status pro Ticker.
**Laufzeit:** ~30-45 Sekunden (8 Ticker × ~4 API-Calls)

### !InsiderDetail [TICKER]

Vollstaendiger 12-Monats-Report mit allen Einzeltransaktionen.

```bash
python insider_intel.py detail AVGO
python insider_intel.py detail MSFT --days 365
```

**Output:** DEFCON-Block + vollstaendige Transaktionsliste.

---

## Transaktions-Klassifikation (DEFCON-Logik)

Das Modul klassifiziert jede Form-4-Transaktion in eine DEFCON-Kategorie:

| Code | Klassifikation | DEFCON-Wirkung | FLAG-relevant? |
|------|---------------|----------------|----------------|
| P | OPEN_MARKET_BUY | Positiv (Scoring +) | Nein |
| S + 10b5-1 | PLAN_SALE_10B51 | Neutral | Nein |
| S ohne 10b5-1 | DISCRETIONARY_SALE | Negativ | **Ja (>$20M = FLAG)** |
| M+S gleicher Tag | CASHLESS_EXERCISE_SALE | Neutral | Nein |
| M (Preis $0) | RSU_VESTING | Neutral | Nein |
| M (mit Preis) | OPTION_EXERCISE | Neutral | Nein |
| A | GRANT_AWARD | Neutral | Nein |
| F | TAX_WITHHOLDING | Neutral | Nein |
| G | GIFT | Neutral | Nein |
| D + 10b5-1 | PLAN_DISPOSAL_10B51 | Neutral | Nein |
| D ohne 10b5-1 | DISCRETIONARY_DISPOSAL | Negativ | **Ja (>$20M = FLAG)** |

### 10b5-1 Erkennung (drei Ebenen)

1. **XML-Feld** (SEC Amendment April 2023+): Direktes Boolean-Feld in `<transactionCoding>`
2. **Footnote-Analyse**: Suche nach "10b5-1", "trading plan", "pre-arranged" in Filing-Footnotes
3. **OpenInsider Gegencheck** (manuell): Spalte "X"/"M" — bleibt Pflicht bei Grenzfaellen

### Cashless Exercise Erkennung

Code M + Code S am gleichen Tag + gleicher Insider = erzwungener Verkauf.
Wird automatisch als CASHLESS_EXERCISE_SALE klassifiziert (kein FLAG).

---

## DEFCON Insider-Scoring (10 Punkte)

| Komponente | Max | Automatisiert? | Quelle |
|-----------|-----|---------------|--------|
| Net Buy (6 Monate) | 4 | Ja | SEC EDGAR Form 4 |
| Management Ownership >1% | 3 | Nein* | Shibui / GuruFocus |
| Kein diskr. Selling >$20M (90d) | 3 | Ja | SEC EDGAR Form 4 |

*Ownership-Score muss manuell ergaenzt werden (3 Punkte) — der automatische Subtotal ist /7.

### Net Buy Score (max 4)

| Netto-Volumen (180d) | Score |
|----------------------|-------|
| > $5M Net Buy | 4 |
| > $1M Net Buy | 3 |
| > $0 Net Buy | 2 |
| Keine Aktivitaet / leicht negativ | 1 |
| > $50M Net Sell | 0 |

### No-FLAG Score (max 3)

| Diskr. Verkaeufe (90d) | Score |
|------------------------|-------|
| < $5M | 3 (clean) |
| $5M – $10M | 2 (moderat) |
| $10M – $20M | 1 (erhoehtes Volumen) |
| > $20M | 0 + FLAG aktiv |

### Ownership Score (max 3, extern)

| Direct Ownership | Score |
|-----------------|-------|
| > 5% | 3 |
| 1% – 5% | 2 |
| 0.1% – 1% | 1 |
| < 0.1% | 0 |

Quelle: Shibui `share_stats.percent_insiders` oder GuruFocus insiders/[TICKER]

---

## FLAG-Regeln (aus INSTRUKTIONEN.md — unveraendert)

| Trigger | Schwelle | Konsequenz |
|---------|----------|------------|
| Diskretionaere Verkaeufe | > $20M in 90 Tagen | FLAG aktiv, Sparrate 0 EUR |
| Kein 10b5-1-Plan | Bei Verkaeufen >$20M | FLAG aktiv |
| Cashless Exercise | M+S gleicher Tag | KEIN FLAG |
| 10b5-1 Plan-Verkaeufe | Beliebig | KEIN FLAG |

**FLAG ueberschreibt jeden Score — auch DEFCON 4 mit FLAG bekommt 0 EUR.**

---

## Integration in !Analysiere Workflow

Bei jedem `!Analysiere [US-TICKER]`:

1. Claude fuehrt `python insider_intel.py scan [TICKER]` aus
2. Output wird direkt als Insider-Block (Abschnitt 4) in die Analyse eingefuegt
3. Ownership-Score wird via Shibui `share_stats.percent_insiders` ergaenzt
4. FLAG-Status wird in Gesamt-Score und Risk Map uebernommen

Bei `!QuickCheck ALL` (monatlich):

1. Claude fuehrt `python insider_intel.py flag-check` aus
2. Ergebnis wird in FLAG-Status-Zeile des QuickCheck eingetragen
3. Bei neuem FLAG → automatischer Deep-Dive-Trigger

### Snapshot-First Workflow (Chat + Cowork + Code)

1. **Faktortabelle laden** → Insider + FLAG Status pruefen
2. `score_datum` < 14 Tage → Insider-Daten aus Faktortabelle uebernehmen
3. `score_datum` ≥ 14 Tage → `!InsiderScan` + `--update-faktortabelle`

**Bei !QuickCheck ALL:**
```bash
python insider_intel.py flag-check --update-faktortabelle
```

**Bei Einzelanalyse:**
```bash
python insider_intel.py scan [TICKER] --update-faktortabelle
```

**3-Wege-Sync (config.yaml + Faktortabelle + Live):**
```bash
python insider_intel.py factor-sync
```

### Vault-Integration

Nach jedem Scan mit `--update-faktortabelle`:
- `wiki/entities/satelliten/[TICKER].md` → FLAG-Status in YAML aktualisieren
- `00_Core/Faktortabelle.md` → Haupttabelle aktualisieren (automatisch via Kommentar-Anker)
- `config.yaml` → **Nur manuell** (Warnung wird ausgegeben)

### BRK.B Sonderregel (Entity-Level-Exception)

**Problem:** Berkshire Hathaway Inc. filed als "10% Owner" Form-4-Transaktionen
fuer eigene Aktien (Rueckkauf-Reporting, Portfolio-Rebalancing). Diese Entity-
Level-Dispositionen loesen technisch die $20M-FLAG-Schwelle aus, sind aber
kein klassisches Insider-Selling.

**Loesung:** `insider_intel.py` filtert bei BRK.B alle Transaktionen von
"BERKSHIRE HATHAWAY INC" (Entity) heraus. Nur Named Executives (Buffett, Abel,
Jain etc.) werden fuer FLAG-Detection und Scoring gezaehlt.

**Kaeufe:** Alle zaehlen (inkl. Entity-Kaeufe) — nur Verkaeufe werden gefiltert.

---

## Verhaeltnis zum generischen sec-edgar-skill

| Aufgabe | Neues Modul | Generischer Skill |
|---------|-------------|-------------------|
| Insider Form 4 Scoring | **Primaer** | — |
| FLAG-Detection | **Primaer** | — |
| 10-K / 10-Q Lesen | — | **Primaer** (Eskalation) |
| Earnings Call Text | — | **Primaer** |
| 8-K Events | — | **Primaer** |
| Datenkonflikt-Verifikation | — | **Primaer** (XBRL) |

Der generische sec-edgar-skill bleibt als Recherche-Tool fuer narrative Inhalte.
Das Insider-Intelligence-Modul uebernimmt den automatisierten Scoring-Block.

---

## Setup (einmalig)

```bash
# Voraussetzung: Python 3.10+ mit requests
pip install requests

# Test: Einzelnen Ticker scannen
cd "01_Skills/insider-intelligence"
python insider_intel.py scan AVGO

# Test: FLAG-Check aller Satelliten
python insider_intel.py flag-check
```

Kein API-Key noetig. SEC EDGAR verlangt nur den User-Agent-Header:
`User-Agent: Tobias tobikowa90@gmail.com`
Bereits im Script hardcoded.

---

## Wartung

**Bei Slot-Tausch:**
1. Neuen Ticker + CIK in `SATELLITES_CIK` dict eintragen
2. Alten Ticker entfernen
3. CIK-Lookup: SEC EDGAR Company Search

**Bei SEC-API-Aenderungen:**
- Endpunkt `data.sec.gov/submissions/CIK{}.json` ist seit 2020 stabil
- Form-4-XML-Schema ist seit 2003 stabil (Namespace gelegentlich angepasst)
- 10b5-1-Feld (2023 Amendment) wird automatisch erkannt

---

*Insider Intelligence Module v1.0 | Dynastie-Depot | Stand: 06.04.2026*
