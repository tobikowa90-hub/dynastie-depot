# 🦅 Dynastie-Depot – Institutionelle Analyse-Pipeline
**Version:** 2.0 | **Stand:** 08.04.2026 | **Zieljahr:** 2058

---

## Übersicht

Die Pipeline definiert **wann welcher Skill/welches Modul ausgelöst wird**, was
die Übergabepunkte sind und wie ein Ticker vom ersten Impuls bis zur
Kauf- oder Tauschentscheidung durch das System fließt.

**Grundprinzip:** Jede Stufe ist ein Tor. Nur wer es passiert, kommt weiter.
Das schützt vor Zeitverschwendung und emotionalen Entscheidungen.

```
Impuls / Idee
     ↓
[STUFE 0]  !QuickScreen [TICKER]  → 🟢 weiter | 🟡 Watchlist | 🔴 aussortieren
     ↓ nur 🟢
[STUFE 2]  !Analysiere [TICKER]   → DEFCON 100-Punkte-Score
     ↓ nur Score ≥ 80 + kein FLAG
[STUFE 3]  !CAPEX-FCF-ANALYSIS    → Excel-Tiefenanalyse (6 Sheets)
     ↓
[ENTSCHEIDUNG] Einstieg / Watchlist / Veto
```

> **Stufe 1 (generate-stock-reports) wurde entfernt** — deinstalliert am
> 08.04.2026. Qualitative Vorab-Recherche erfolgt jetzt direkt über WebSearch
> im Rahmen von Stufe 2 (Business Snapshot + Moat-Block).

---

## SKILL-ARCHITEKTUR — Monolith vs. Modulare Skills

### Warum `dynastie-depot` als Monolith funktioniert

`!Analysiere` ruft **keinen weiteren Skill explizit auf**. Alle spezialisierten
Module werden direkt als Tool-Calls genutzt — ohne den Token-Overhead eines
Skill-Loads. Das ist bewusst so designed:

| Was genutzt wird | Wie genutzt | Expliziter Skill-Load? |
|------------------|------------|----------------------|
| defeatbeta MCP | MCP-Tool-Calls direkt | ❌ Nein |
| Shibui Finance SQL | MCP-Tool-Calls direkt | ❌ Nein |
| insider_intel.py | Bash → Python direkt | ❌ Nein |
| eodhd_intel.py | Bash → Python direkt | ❌ Nein |
| WebSearch | Tool-Call direkt | ❌ Nein |
| `insider-intelligence` Skill | Nur bei standalone !InsiderScan | ⚠️ Optional |
| `quick-screener` Skill | Nur bei !QuickCheck | ⚠️ Optional |
| `earnings-preview` Skill | Nur bei !EarningsPreview | ⚠️ Optional |
| `earnings-recap` Skill | Nur bei !EarningsRecap | ⚠️ Optional |

**Konsequenz:** Kein Mehrwert durch Skill-Verkettung innerhalb von `!Analysiere`.
Jeder zusätzliche Skill-Load kostet Token und verliert DEFCON-Kontext
(Scoring-Skalen, FLAG-Regeln, Kalibrierungsanker sind nur in der SKILL-dynastie-depot.md bekannt).

### Wann werden andere Skills eigenständig aktiviert?

| Befehl | Skill | Wann |
|--------|-------|------|
| `!QuickCheck [TICKER\|ALL]` | `quick-screener` | Stufe-0-Vorfilter |
| `!EarningsPreview [TICKER]` | `earnings-preview` | 48h vor Earnings |
| `!EarningsRecap [TICKER]` | `earnings-recap` | 48h nach Earnings |
| `!EarningsCalendar` | `earnings-calendar` | Wöchentlicher Überblick |
| `!InsiderScan` | `insider-intelligence` | Standalone ohne !Analysiere |
| `!PortfolioRisk` | `risk-metrics-calculation` | Quartalsweise (ab Mai 2026) |

---

## STUFE 0 — Quick-Screener

**Skill:** `quick-screener` (eigenständig aktiviert)
**Trigger:** `!QuickCheck [TICKER]` oder `!QuickCheck ALL`
**Dauer:** ~3–5 Minuten pro Ticker

### Drei harte Filter:

| Filter | 🟢 Grün | 🟡 Gelb | 🔴 Rot |
|--------|---------|---------|--------|
| P/FCF | ≤ 35 | 35–45 | > 45 |
| ROIC | ≥ 15% | 12–15% | < 12% |
| Moat-Proxy | GM > 40% + CAGR > 8% | Eines knapp verfehlt | Eines deutlich verfehlt |

**Sonderregeln:**
- BRK.B, MKL, FFH.TO → P/B statt P/FCF (Float-Modelle)
- COST → GM-Exception (Membership-Modell, strukturell niedrig)

**Output:** Ampel + 1–2 Sätze + nächster Schritt
**Weitergabe:** Nur 🟢 → Stufe 2. 🟡 → Watchlist. 🔴 → aussortiert.

**Monatlicher Pflicht-Lauf:** Erster Montag des Monats — `!QuickCheck ALL`
für alle 11 Satelliten in Risiko-Reihenfolge (FLAG/DEFCON-2+ zuerst).

---

## STUFE 2 — DEFCON-Vollanalyse

**Skill:** `dynastie-depot` → Befehl: `!Analysiere [TICKER]`
**Trigger:** Nach Stufe 0 🟢, oder direkt bei bekannten Depot-Positionen
**Dauer:** ~20–30 Minuten

### API-Routing (Pflicht vor jedem Datenabruf):

```
PFLICHT ZUERST: get_latest_data_update_date → Referenzdatum feststellen

IF US-Ticker (AVGO, MSFT, V, BRK.B, TMO, VEEV, APH, COST):
    defeatbeta MCP    → annual_cash_flow, balance_sheet, income_statement,
                         quarterly_roic (max. 6Q), wacc (nur neuester Wert),
                         annual_gross_margin, quarterly_revenue_by_geography*,
                         earning_call_transcript
    Shibui SQL        → technical_indicators (2 Zeilen für 200MA-Slope),
                         cash_flow_quarterly (12Q für CapEx-FLAG-Muster)
    insider_intel.py  → python insider_intel.py scan [TICKER]
    Web (Pflicht)     → Live-Kurs (Yahoo), Fwd P/E (AlphaSpread/GuruFocus),
                         Moat (GuruFocus moat-score), OpenInsider (10b5-1 HEILIG),
                         EPS-Revisionen (Zacks)

    *Geography nur bei Produktionsstandorten in CN/TW/MY/TH/VN

IF Non-US-Ticker (ASML, RMS, SU):
    eodhd_intel.py    → python eodhd_intel.py detail [TICKER]
                         (CapEx/OCF, Bilanz, Valuation, Margen, GM-Trend,
                          Technicals, Analysten, Ownership — EUR, IFRS)
    Web (Pflicht)     → Live-Kurs EUR (Yahoo), AlphaSpread DCF,
                         GuruFocus term/roic (ROIC-Verifikation), Moat
    Insider           → AFM (ASML) / AMF (RMS, SU) — manuell, kein API
```

### Pre-Processing Layer (4 Regeln — vor jedem Scoring):

| Regel | Trigger | Aktion |
|-------|---------|--------|
| 1 — SBC-Check | SBC/OCF ≥ 15% | Dokumentationspflicht, kein Score-Malus |
| 2 — Hyperscaler CapEx | Finance Leases > $5B | Manueller 8-K-Check vor FLAG |
| 3 — CapEx-Qualität | Growth vs. Maintenance | Risk-Map-Notiz, kein Veto |
| 4 — M&A ROIC-Proxy | Goodwill > 30% Assets | Proxy-ROIC dokumentieren |

### 100-Punkte-Matrix:

| Block | Gewicht | Primärquelle US | Primärquelle Non-US |
|-------|---------|-----------------|---------------------|
| Fundamentals | 50 Pt. | defeatbeta MCP + Shibui SQL | eodhd_intel.py |
| Moat | 20 Pt. | GuruFocus (Web) | GuruFocus (Web) |
| Technicals | 10 Pt. | Shibui technical_indicators | eodhd_intel.py |
| Insider | 10 Pt. | insider_intel.py + OpenInsider | AFM / AMF (manuell) |
| Sentiment | 10 Pt. | Zacks + Yahoo Finance (Web) | Yahoo Finance EUR |

### DEFCON-Schwellen (Bestand vs. Neueinstieg):

| Score | DEFCON | Neueinstieg | Bestand | Sparrate |
|-------|--------|-------------|---------|----------|
| ≥ 80 | 🟢 4 | Einstieg erlaubt | Sparplan voll | Volle Rate |
| 65–79 | 🟡 3 | Kein Einstieg | Halten | 50% Sockelbetrag |
| 50–64 | 🟠 2 | Kein Einstieg | Sparrate 0 € | 0 € |
| < 50 | 🔴 1 | Veto | Auswechslung | 0 € |

### Automatische FLAGs (score-unabhängig, heilig):

| Trigger | Quelle | Konsequenz |
|---------|--------|-----------|
| CapEx/OCF > 60% | Shibui quarterly / eodhd_intel.py | 🔴 FLAG → Sparrate 0 € |
| Negativer FCF-Trend + steigendes CapEx | defeatbeta CF | 🔴 FLAG → Sparrate 0 € |
| Insider Netto-Selling > $20M / 90d (diskretionär) | insider_intel.py + OpenInsider | 🔴 FLAG → Sparrate 0 € |
| Tariff Exposure > 35% CN/TW/MY/TH/VN | defeatbeta geography | 🔴 FLAG → -3 Pt. + Sparrate 0 € |

### Kalibrierungsanker (vor jeder Analyse pflichtlesen — Beispiele.md):

| Ticker | Score | Lektion |
|--------|-------|---------|
| AVGO | 86 | Fabless = CapEx/OCF <15%, Referenz Top-Score |
| MKL | 82 | Float-Modell, Versicherungs-Exception |
| SNPS | 79 | Goodwill-Malus durch Ansys-Akquisition |
| MSFT | 60 | ROIC < WACC + CapEx-Ramp = DEFCON 2 trotz Wide Moat |
| TMO | 67 | Akquisitionsschuld + ROIC-Grenzfall |
| EXPN | 61 | Datenlücken → konservativ scoren |

**Weitergabe an Stufe 3:** Nur bei Score ≥ 80 + kein aktives FLAG.

---

## STUFE 2.5 — Earnings-Workflow (rund um Reporting-Termine)

**Trigger:** 48h vor / nach Earnings einer Depot-Position

```
48h vor Earnings:  !EarningsPreview [TICKER]  → Skill: earnings-preview
48h nach Earnings: !EarningsRecap [TICKER]    → Skill: earnings-recap
                         ↓
             QuickCheck auf Basis neuer Daten
                         ↓
             Bei Deep-Dive-Trigger: !Analysiere
```

**Kritische Termine 2026:**

| Datum | Ticker | Aktion |
|-------|--------|--------|
| 23.04.2026 | TMO Q1 | FCF >$7.3B → DEFCON 4? Sonst ZTS prüfen |
| 28.04.2026 | SPGI Q1 | QuickCheck → Re-Analyse-Trigger? |
| 29.04.2026 | MSFT Q3 FY26 | FLAG-Auflösung wenn bereinigtes CapEx/OCF <60% |
| Mai 2026 | PEGA | Slot-16-Entscheidung |

---

## STUFE 3 — CapEx-FCF-Tiefenanalyse

**Skill:** `dynastie-depot` → Befehl: `!CAPEX-FCF-ANALYSIS [TICKER] [NAME]`
**Trigger:** Nur bei Score ≥ 80 + kein FLAG aus Stufe 2
**Dauer:** ~20–30 Minuten
**Output:** `TICKER_CapEx_FCF_Analyse_YYYY-MM-DD.xlsx` in `02_Analysen/`

### 6 Excel-Sheets:
1. Executive Summary
2. Historische CapEx/FCF-Daten (5–10 Jahre)
3. Szenario-Analyse (Bull / Base / Bear)
4. DCF-Bewertung
5. Peer-Vergleich
6. Risiko-Dashboard

**Vorlage:** `01_Skills/dynastie-depot/capex-fcf-template.md`

---

## REBALANCING-WORKFLOW

**Skill:** `dynastie-depot` → Befehl: `!Rebalancing`
**Trigger:** Monatlich (erster Sparplan-Eingang) oder Drift > 10%
**Nächster echter Lauf:** 01.05.2026

### Formel:

```
Gewichte: DEFCON-4-Clean = 1.0 | DEFCON-3 = 0.5 | FLAG (beliebig) = 0.0
Einzelrate = 285€ / Σ Gewichte × Eigengewicht
```

### Ablauf:
1. `config.yaml` lesen → aktuellen DEFCON/FLAG-Status aller 11 Positionen
2. Gewichte berechnen → Σ ermitteln
3. Sparplan-Vorschlag pro Position ausgeben
4. **Steuer-Bremse:** Niemals durch Verkauf rebalancen → Sparplan umleiten
5. US-Cap prüfen: Bleibt US-Exposure unter 63%?

---

## ERGÄNZUNGS-SKILLS (eigenständig, nicht in !Analysiere integriert)

### `qualitative-valuation` — Moat-Vertiefung bei Grenzfällen
**Wann aktivieren:** Score 77–82, Moat-Block ist der entscheidende Faktor,
Porter's Five Forces oder Switching-Cost-Tiefe nötig.
**Nicht nötig bei:** Klaren Wide-Moat-Titeln (AVGO, MSFT, ASML) oder
klaren Ablehnungen (Score <65).

### `risk-metrics-calculation` — Portfolio-Risikometrik
**Wann aktivieren:** Quartalsweise nach Rebalancing, oder wenn neue Position
aufgenommen wird und Portfolio-Beta/VaR-Impact bewertet werden soll.
**Nicht nötig bei:** Einzelaktien-Scoring (!Analysiere).
**Geplanter erster Einsatz:** Mai 2026 nach erstem echten Rebalancing-Lauf.

### `sec-edgar-skill` — Dokumenten-Eskalation
**Wann aktivieren:** Manueller 10-K/10-Q-Textcheck (z.B. Finance-Lease-
Fußnoten wie bei MSFT Pre-Processing Regel 2), XBRL-Datenkonflikte,
8-K-Events zwischen Earnings-Terminen.
**Nicht nötig bei:** Insider-Scoring (→ insider_intel.py ist besser).

---

## SYSTEM-STATUS (Stand: 08.04.2026)

| Komponente | Version | Typ | Status |
|------------|---------|-----|--------|
| `dynastie-depot` | 3.4.1 | Haupt-Skill | ✅ Aktiv |
| `quick-screener` | 1.1 | Skill | ✅ Aktiv |
| `insider-intelligence` | 1.0 | Skill + Python | ✅ Aktiv |
| `non-us-fundamentals` | 1.1 | Python-Modul | ✅ Aktiv |
| `earnings-preview` | 1.0 | Skill | ✅ Aktiv |
| `earnings-recap` | 1.0 | Skill | ✅ Aktiv |
| `earnings-calendar` | 1.0 | Skill | ✅ Aktiv |
| `qualitative-valuation` | 1.0 | Skill (optional) | ✅ Aktiv |
| `risk-metrics-calculation` | 1.0 | Skill (geplant) | ✅ Aktiv |
| `sec-edgar-skill` | 1.0 | Skill (Fallback) | ✅ Aktiv |
| defeatbeta MCP | 1.27.0 | MCP-Server | ✅ Aktiv (WSL2) |
| Shibui Finance SQL | — | MCP-Connector | ✅ Aktiv |

**Deinstalliert / entfernt (08.04.2026):**
- `generate-stock-reports` — vollständig durch WebSearch in !Analysiere ersetzt
- `us-stock-analysis` — vollständig durch `dynastie-depot` ersetzt
- `analyzing-financial-statements` — nie produktiv genutzt
- `findata-toolkit-us` — nie produktiv genutzt
- `valuation-calculator` — redundant zu defeatbeta

---

## ORDNERSTRUKTUR

```
Claude Stuff/
├── 00_Core/           → CORE-MEMORY.md | KONTEXT.md | INSTRUKTIONEN.md
├── 01_Skills/         → Skill-Quelldateien (Arbeitsversionen)
│   ├── dynastie-depot/    → SKILL-dynastie-depot.md | config.yaml | Beispiele.md | PIPELINE.md
│   ├── insider-intelligence/ → SKILL-dynastie-depot.md | insider_intel.py
│   ├── non-us-fundamentals/  → SKILL-dynastie-depot.md | eodhd_intel.py
│   └── quick-screener/    → SKILL-dynastie-depot.md
├── 02_Analysen/       → DEFCON-Analysen als Excel (Output Stufe 3)
├── 03_Tools/          → Rebalancing_Tool | Satelliten_Monitor | Watchlist_Monitor
├── 04_Templates/      → Analyse-Template | CAPEX-FCF | Alerts-Log
├── 05_Archiv/         → Historische Dateien
└── 06_Skills-Pakete/  → Installierbare ZIPs (nur aktive Skills)
    ├── dynastie-depot_v3.4.1.zip
    ├── quick-screener.zip
    ├── insider_intel.zip
    ├── earnings-preview.zip
    ├── earnings-recap.zip
    ├── openclaw-earnings-calendar.zip
    ├── adaptationio-fmp-api.zip    ← FMP API Key für earnings-calendar
    ├── defeat-beta-defeatbeta-analyst.zip
    ├── neversight-sec-edgar-skill.zip
    └── qualitative-valuation.zip
```

---

🦅 PIPELINE.md v2.0 | Dynastie-Depot | Stand: 08.04.2026
