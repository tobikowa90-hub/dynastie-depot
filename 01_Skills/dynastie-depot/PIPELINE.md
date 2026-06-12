# 🦅 Dynastie-Depot – Institutionelle Analyse-Pipeline
**Version:** 2.3 | **Stand:** 2026-06-13 | **Zieljahr:** 2058 | **Scoring:** DEFCON v3.7 | **Skill-Paket:** → `00_Core/SYSTEM.md` (SSoT)

> **Nachgezogen 2026-06-13** auf Umstrukturierung-2027 Phase A: 13-Roster (COST/VEEV exited, NOW/KYCCF/ZETA/AMZN rein), 3-Tier-Rate-Modell (T1 40€/T2 32€/T3 18€ × DEFCON-Modulation), 60/35/5. Script-Pfade auf Skill-Ordner aktualisiert.

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

`!Analysiere` chained **kein** Skill manuell. Spezialisierte Module werden direkt als Tool-Calls genutzt — ohne den Token-Overhead eines Skill-Loads. Eine **dokumentierte Ausnahme**: `backtest-ready-forward-verify` wird in Schritt 7 programmatisch invoked (jsonl-Write-Pipeline-Kapsel, kein Scoring-Kontext nötig).

| Was genutzt wird | Wie genutzt | Skill-Load? |
|------------------|------------|---|
| defeatbeta MCP | MCP-Tool-Calls direkt | ❌ Nein |
| Shibui Finance SQL | MCP-Tool-Calls direkt | ❌ Nein |
| insider_intel.py | Bash → Python direkt | ❌ Nein |
| eodhd_intel.py | Bash → Python direkt | ❌ Nein |
| WebSearch | Tool-Call direkt | ❌ Nein |
| **`backtest-ready-forward-verify`** | **Schritt 7 jsonl-Write** | **⚙️ Programmatisch** (kanonisch) |
| `insider-intelligence` Skill | Nur bei standalone `!InsiderScan` | ⚠️ Optional / Manuell |
| `quick-screener` Skill | Nur bei `!QuickCheck` | ⚠️ Optional / Manuell |
| `_extern/earnings-preview` / `-recap` | Nur bei `!EarningsPreview`/`!EarningsRecap` | ⚠️ Optional / Manuell |
| `03_Tools/earnings_calendar.py` (Tool) | Forward-Earnings-Kalender (SSoT) — ersetzt früheren `earnings-calendar`-Skill | ⚙️ Tool, kein Skill |

**Konsequenz:** Kein **manuelles** Skill-Chaining innerhalb von `!Analysiere`. Jeder Ad-hoc-Skill-Load kostet Token und verliert DEFCON-Kontext (Scoring-Skalen, FLAG-Regeln, Kalibrierungsanker sind nur in der SKILL.md bekannt). Die Step-7-Programmatic-Invocation ist davon ausgenommen, weil sie keinen Scoring-Kontext braucht — sie schreibt einen fertigen `ScoreRecord` deterministisch ins Archiv.

### Wann werden andere Skills eigenständig aktiviert?

| Befehl | Skill | Wann |
|--------|-------|------|
| `!QuickCheck [TICKER\|ALL]` | `quick-screener` | Stufe-0-Vorfilter |
| `!EarningsPreview [TICKER]` | `_extern/earnings-preview` | 48h vor Earnings |
| `!EarningsRecap [TICKER]` | `_extern/earnings-recap` | Tag 0 nach Earnings (Press-Release-Recap, §19.1) |
| Earnings-Termine | `03_Tools/earnings_calendar.py` (Tool) | Forward-Kalender — ersetzt `earnings-calendar`-Skill (deprecated) |
| `!InsiderScan` | `insider-intelligence` | Standalone ohne !Analysiere |
| Portfolio-Risk-Audit | `03_Tools/portfolio_risk.py` (Python-Tool) | Quartalsweise manuell — kein Skill |

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
- COST → GM-Exception (Membership-Modell) — COST seit 06/2026 nicht mehr im Roster; Regel bleibt als Methodik-Anker für Discount-/Membership-Retailer

**Output:** Ampel + 1–2 Sätze + nächster Schritt
**Weitergabe:** Nur 🟢 → Stufe 2. 🟡 → Watchlist. 🔴 → aussortiert.

**Monatlicher Pflicht-Lauf:** Erster Montag des Monats — `!QuickCheck ALL`
für alle 13 Satelliten in Risiko-Reihenfolge (FLAG/DEFCON-2+ zuerst).

---

## STUFE 2 — DEFCON-Vollanalyse

**Skill:** `dynastie-depot` → Befehl: `!Analysiere [TICKER]`
**Trigger:** Nach Stufe 0 🟢, oder direkt bei bekannten Depot-Positionen
**Dauer:** ~20–30 Minuten

### API-Routing (Pflicht vor jedem Datenabruf):

```
PFLICHT ZUERST: get_latest_data_update_date → Referenzdatum feststellen

IF US-Ticker (AVGO, MSFT, V, BRK.B, TMO, APH, AMZN, NOW, ZETA):
    defeatbeta MCP    → annual_cash_flow, balance_sheet, income_statement,
                         quarterly_roic (max. 6Q), wacc (nur neuester Wert),
                         annual_gross_margin, quarterly_revenue_by_geography*,
                         earning_call_transcript
    Shibui SQL        → technical_indicators (2 Zeilen für 200MA-Slope),
                         cash_flow_quarterly (12Q für CapEx-FLAG-Muster)
    insider_intel.py  → python 01_Skills/insider-intelligence/insider_intel.py scan [TICKER]
    Web (Pflicht)     → Live-Kurs (Yahoo), Fwd P/E (AlphaSpread/GuruFocus),
                         Moat (GuruFocus moat-score), OpenInsider (10b5-1 HEILIG),
                         EPS-Revisionen (Zacks)

    *Geography nur bei Produktionsstandorten in CN/TW/MY/TH/VN

IF Non-US-Ticker (ASML, RMS, SU; KYCCF JP → O3-pending, JP/JPY-Support noch nicht im Script):
    eodhd_intel.py    → python 01_Skills/non-us-fundamentals/eodhd_intel.py detail [TICKER]
                         (CapEx/OCF, Bilanz, Valuation, Margen, GM-Trend,
                          Technicals, Analysten, Ownership — EUR, IFRS)
    Web (Pflicht)     → Live-Kurs EUR (Yahoo), AlphaSpread DCF,
                         GuruFocus term/roic (ROIC-Verifikation), Moat
    Insider           → AFM (ASML) / AMF (RMS, SU) — manuell, kein API
    KYCCF (Keyence)   → JPY/IFRS, JP-Support im non-us-fundamentals-Build noch offen (O3-Scoring-Nachzug)
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

| Score | DEFCON | Neueinstieg | Bestand | Gewicht (Sparrate) |
|-------|--------|-------------|---------|--------------------|
| ≥ 80 | 🟢 4 | Einstieg erlaubt | Sparplan voll | **1.0** (volle Rate) |
| 65–79 | 🟡 3 | Kein Einstieg | Halten | **1.0** (volle Rate — v3.4 korrigiert, nicht mehr 50%) |
| 50–64 | 🟠 2 | Kein Einstieg | Halten, reduziert | **0.5** (halbe Rate) |
| < 50 | 🔴 1 | Veto | Auswechslung | **0** (0 €) |

**FLAG-Regel:** Beliebiger 🔴 FLAG (CapEx/OCF >60%, Netto-Selling >$20M, Tariff >35%, etc.) überschreibt das Gewicht auf **0** unabhängig vom DEFCON-Score.

### Automatische FLAGs (score-unabhängig, heilig):

| Trigger | Quelle | Konsequenz |
|---------|--------|-----------|
| CapEx/OCF > 60% | Shibui quarterly / eodhd_intel.py | 🔴 FLAG → Sparrate 0 € |
| Negativer FCF-Trend + steigendes CapEx | defeatbeta CF | 🔴 FLAG → Sparrate 0 € |
| Insider Netto-Selling > $20M / 90d (diskretionär) | insider_intel.py + OpenInsider | 🔴 FLAG → Sparrate 0 € |
| Tariff Exposure > 35% CN/TW/MY/TH/VN | defeatbeta geography | 🔴 FLAG → -3 Pt. + Sparrate 0 € |

### Kalibrierungsanker (vor jeder Analyse pflichtlesen — Beispiele.md):

**Primär (v3.7-Voll-Anker):**

| Ticker | Score | DEFCON | Lektion |
|--------|-------|--------|---------|
| AVGO | 84 (Stand April 2026) | 🟢 4 | Fabless + Wide Moat + Premium-Multiple → QT differenziert am P/FCF-Rand. **Historischer Anker — illustriert „wie 84 aussieht".** AVGO Live seit 30.04.: **56/D2/🔴FLAG** (Quality-Trap-Collapse 84→53→56, selbst Lehr-Case). Live-Score → PORTFOLIO.md/Faktortabelle.md |
| ASML | 68 | 🟡 3 | Non-US/IFRS Pfad B → QT beide Zweige hart 0; FY27-Watch 30,30 als D3→D4-Pfad |

**Kanonische Regeln:** SKILL.md §Scoring-Skalen + §Screener-Exceptions (6 Exceptions: BRK.B / COST / RMS / TMO / MSFT / ASML). Beispiele.md §Mechanismen-Index mappt Mechanismus → Voll-Anker + SKILL-Zeile.

**Legacy (v3.5, mit Zeitstand-Banner):** MKL, SNPS, SPGI, TMO-v3.5, EXPN, FICO — Workflow-Historie für M&A-Goodwill, Insurance-Exception, Datenlücken-Handling. **Nicht** für v3.7-Score-Kalibrierung verwenden.

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

**Kritische Termine** (SSoT: `03_Tools/earnings_calendar.py --check` + `00_Core/PORTFOLIO.md`; Stand 09.06.2026):

| Datum | Ticker | Aktion |
|-------|--------|--------|
| 15.07. | ASML Q2 | Nächstes Roster-Event |
| 22.07. | NOW / TMO Q2 | NOW O3-Vollanalyse · TMO Organic-Akzeleration + Clario |
| 28.07. | V Q3 FY26 | Cross-Border-Velocity + ROIC-Methodology-Verify |
| 29.07. | MSFT Q4 / APH / RMS / KYCCF | MSFT CapEx-Plateau+WACC · APH FLAG-Review · RMS H1 · KYCCF Q1 (O3) |
| 30.07. | SU / AMZN | SU H1 · AMZN CapEx/OCF-FLAG-Re-Eval |
| 01.08. | BRK.B Q2 | 10-Q (KHC-OTTI / GEICO / Apple-Trim) |
| 04.08. | ZETA Q2 | O3-Scoring-Nachzug |
| 03.09. | AVGO Q3 FY26 | Insider-FLAG-Resolve-Gate |

> Live-Terminliste ist volatil — diese Tabelle ist Snapshot. Autoritativ: Tool + PORTFOLIO „Nächster Trigger".

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
**SSoT:** `Rebalancing_Tool_v4.0.xlsx` (value-based, lenkt freies Kapital auf untergewichtete Positionen)

### Formel (3-Tier-Modell, Umstrukturierung-2027 — löst flaches 38/19-Equal-Weight ab):

```
Tier-Basisrate (Optimal-Fall D3/D4 clean):  T1 = 40€ | T2 = 32€ | T3 = 18€
Effektive Rate = Tier-Basis × DEFCON-Modulation × FLAG
  DEFCON 3/4 → ×1,0 | DEFCON 2 → ×0,5 (Sockelbetrag) | DEFCON 1 → 0€ | 🔴 FLAG → 0€ (heilig)
SOLL-Σ = 4×40 + 3×32 + 6×18 = 364€  (== config scalable.sparrate_eur)
Funded-Σ (modulierte Raten) ist transient; Differenz → Rebalancing-Tool value-based
```

### Ablauf:
1. `config.yaml` lesen → Tier + aktuellen DEFCON/FLAG-Status aller 13 Positionen
2. Effektive Raten berechnen (Tier-Basis × Modulation × FLAG) → Funded-Σ ermitteln
3. Sparplan-Vorschlag pro Position ausgeben (SSoT = Rebalancing_Tool_v4.0.xlsx)
4. **Steuer-Bremse:** Niemals durch Verkauf rebalancen → Sparplan umleiten
5. US-Cap prüfen: Bleibt US-Exposure unter 63%?

---

## ERGÄNZUNGS-SKILLS (eigenständig, nicht in !Analysiere integriert)

### Portfolio-Risk-Audit → `03_Tools/portfolio_risk.py` (kein Skill)
**Wann ausführen:** Quartalsweise nach Rebalancing.
**Output:** Correlation Matrix der 13 Satelliten, Component Risk Contribution,
Stress-Test (2020-COVID + 2022-Rate-Hikes). Markdown-Report nach `03_Tools/Output/`.
**Aufruf:** `python 03_Tools/portfolio_risk.py`
**Begründung für Tool statt Skill:** 80% eines Risk-Metrics-Skills (VaR/CVaR/Sharpe/
Rolling-Metriken/Monte-Carlo) ist irrelevant für Buy-and-Hold 33J-Horizont.
Die verbleibenden 3 Funktionen rechtfertigen keinen Skill-Load-Overhead.

> Qualitative-Valuation ist kein Skill mehr — Moat-Analyse ist vollständig in
> DEFCON-Scoring (Moat-Block 20 Pkt.) + GuruFocus Moat-Score + §Screener-Exceptions
> in SKILL.md kodifiziert. ESG bewusst ausgelassen (kein Veto-Kriterium).

### `sec-edgar-skill` v1.1 — Dokumenten-Eskalation
**Wann aktivieren:** Manueller 10-K/10-Q-Textcheck (z.B. Finance-Lease-
Fußnoten wie bei MSFT Pre-Processing Regel 2), XBRL-Datenkonflikte,
8-K-Events zwischen Earnings-Terminen. Trigger `!EdgarLookup`/`!EdgarFiling`/`!Edgar13F`.
**Nicht nötig bei:** Insider-Scoring (→ `insider-intelligence` Skill / `01_Skills/insider-intelligence/insider_intel.py` ist besser).

---

## SYSTEM-STATUS

> **SSoT → `00_Core/SYSTEM.md`** (Skill-Versionen, MCP-Status, Briefing-Status, Backtest-Ready-Status, Backlog). Hier nicht duplizieren, um Drift wie 17.04.→25.04.-Lag zu vermeiden.

## ORDNERSTRUKTUR

> **SSoT → `CLAUDE.md` `## Projektstruktur`.** Diese Datei dokumentiert nur die Pipeline-Stufen + Skill-Architektur.

---

🦅 PIPELINE.md v2.3 | Dynastie-Depot DEFCON v3.7 | Stand: 2026-06-13 (Umstrukturierung-2027 nachgezogen)
