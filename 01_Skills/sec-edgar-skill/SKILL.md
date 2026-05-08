---
name: sec-edgar-skill
version: "1.1"
Stand: "2026-05-08"
description: >
  Dynastie-Depot SEC-EDGAR-Skill v1.1.
  Eskalations-Fallback für US-SEC-Filings via EdgarTools (XBRL-strukturiert).
  Use-Cases: 10-K/10-Q-Section-Search, Form-13F-Holdings-Pull, 8-K-Material-Events,
  Multi-Period-Trend, Daten-Konflikt-XBRL-Schiedsquelle.
  ERSETZT NICHT: insider-intelligence (Form-4 Primärpipeline für 8 US-Satelliten),
  non-us-fundamentals (ASML/RMS/SU). NICHT auto-aktiv in !Analysiere.
  Trigger: !EdgarLookup, !EdgarFiling, !Edgar13F.
---

# SEC-EDGAR-Skill — Dynastie-Depot v1.1

**Stand:** 2026-05-08 | **Zweck:** Eskalations-Fallback für US-SEC-Filings (10-K/10-Q/13F/8-K)
**Pipeline-Position:** Sekundär — `insider-intelligence` (Form-4 Primary) + `non-us-fundamentals` (ASML/RMS/SU) bleiben Primary für die jeweiligen Domänen.

---

## §0 Scope-NICHT-Liste (Was dieser Skill NICHT macht)

- **Innerhalb `!Analysiere`** — `dynastie-depot`-Monolith hat Precedence (INSTRUKTIONEN §17 Skill-Hierarchie). Skill-Chaining würde DEFCON-Kontext verlieren.
- **Real-Time-Kurse / Market-Data** — Shibui (US) / yfinance (Non-US) sind Primär. EDGAR ist Filing-Quelle, nicht Preisquelle.
- **Insider-Primäranalyse** — `insider-intelligence`/`insider_intel.py` ist Primärpipeline für 8 US-Satelliten (CIK hardcoded). UC3 hier nur bei Reviewer-Eskalation.
- **Non-US-Ticker (ASML / RMS / SU)** — `non-us-fundamentals`/yfinance ist Primärpipeline.
  - **ASML-FPI-Klausel:** ASML als **Foreign-Private-Issuer (FPI)** hat **kein 10-Q-Pflicht-Filing**. ASML reicht **20-F (Annual)** bei der SEC ein, plus **6-K** bei material events. **Mid-Quarter-Trading-Updates / Pre-Announcements sind kein SEC-Filing** und werden über IR-Calendar (`03_Tools/earnings_schedule_overrides.yaml`) getrackt, NICHT über diesen Skill. **Konsequenz:** PIPELINE.md Item #43 trägt einen Cross-Reference auf diese Klausel statt der ursprünglichen „Kandidat für SEC-EDGAR-Skill-Promotion"-Notiz (factually wrong, durch Track-5a-Refresh korrigiert).
  - **RMS / SU:** Hermès und Schneider Electric sind Euronext-gelistet (RMS.PA / SU.PA), reichen KEINE Filings bei der SEC ein. Insider via AMF (`Transactions des dirigeants`), Fundamentals via yfinance.

---

## Pflicht-Setup (CRITICAL)

EdgarTools verlangt für **jede** SEC-API-Operation eine Identity (SEC-Legal-Requirement, kein Workaround):

```python
from edgar import set_identity
set_identity("Tobias Kowalski tobikowa90@gmail.com")
```

Ohne `set_identity()` werfen alle nachfolgenden Calls (`Company(...)`, `get_filings(...)`, etc.) eine `IdentityNotSetError` (oder gleichwertig).

**Hinweis zu `Company.name`:** SEC EDGAR liefert die Registrar-Legal-Form, z.B. `Company("MSFT").name == "MICROSOFT CORP"` (nicht „Microsoft Corporation"). Smoke-Test asserts darum case-insensitive Substring-Match.

---

## Token-Effizienz-Regel

**ALWAYS `.to_context()` first** — liefert kompakte Summaries mit 56-89% weniger Tokens vs. `repr()`/`text()`:

| Object | `repr()` Tokens | `.to_context()` Tokens | Savings |
|--------|-----------------|------------------------|---------|
| Company | ~750 | ~75 | 90% |
| Filing | ~125 | ~50 | 60% |
| XBRL | ~2,500 | ~275 | 89% |
| Statement | ~1,250 | ~400 | 68% |

(Tabelle übernommen aus `_extern/sec-edgar-skill/SKILL.md` Z.31-43, edgartools-Version Stand 2026-05-08: `5.31.0`. Live-Smoke-Stand 2026-05-08: `Company.to_context() = 402 chars` ≈ 80 Tokens, gut innerhalb Budget 500.)

**Regel:** Erst `.to_context()` aufrufen, dann gezielt drill-downen (statements / facts / items). Niemals `filing.text()` (50K+ Tokens) ohne expliziten Section-Bedarf.

---

## §1 Architektur

```
EdgarTools (PyPI: edgartools)
         |
    set_identity() Pflicht
         |
    Drei Zugangswege:
    (a) Company(ticker_or_cik) — Single-Entity
    (b) get_filings(form="10-K", year=...) — Bulk Cross-Company
    (c) get_current_filings() — RSS-Feed Real-Time Monitoring
         |
    Drill-down: filing.xbrl().statements / .facts / .items()
         |
    Output: kompakter Markdown-Block für Reviewer-Hand-off
```

**API-Routing-Regel (Gesamt-System):**

```
IF Insider-Form-4-Scoring (DEFCON-Block, 8 US-Satelliten)
    → insider-intelligence/insider_intel.py (Primary)
    → SEC-EDGAR-Skill UC3 NUR bei Reviewer-Eskalation aus Form-4-Befund
       (z.B. ambiger Cashless-Exercise-Pattern mit nicht-eindeutigem 10b5-1-Status)

IF Non-US-Ticker (ASML / RMS / SU)
    → non-us-fundamentals/eodhd_intel.py (Primary, yfinance)
    → SEC-EDGAR-Skill NICHT (ASML-FPI / RMS / SU haben keine SEC-Filings im Sinne dieses Skills)

IF US-Ticker + 10-K/10-Q-Section-Search / 13F-Holdings-Pull / 8-K-Material-Events
    → SEC-EDGAR-Skill UC2/UC5/UC6 (dieser Skill, Primary)

IF Datenkonflikt defeatbeta vs Shibui >5%
    → SEC-EDGAR-Skill UC1 (XBRL als Schiedsquelle)

IF Multi-Period-Fundamentals-Trend (5J / 20Q)
    → SEC-EDGAR-Skill UC4 (Entity-Facts-API)
```

---

## §2 Use-Cases (4 Original + 2 NEU für v1.1)

### UC1 — Daten-Konflikt-XBRL-Schiedsquelle

**Trigger:** Drift zwischen defeatbeta und Shibui >5% bei zentralen Metriken (Revenue, FCF, OCF, CapEx, Net Income).
**Action:** XBRL als kanonische SEC-bestätigte Quelle ziehen, Drift dokumentieren, primary-source-Wert erzwingen.
**Real-Run-Beispiel:** PIPELINE #21 (defeatbeta-ROIC-V-Methodology-Watch) — bei Q3 FY26 V-Earnings (~Ende Juli), `mcp__defeatbeta-api__get_stock_quarterly_roic` Roh-Output gegen XBRL-NOPAT/IC-Calc abgleichen.

```python
from edgar import Company
c = Company("V")
filing = c.get_filings(form="10-Q").latest()
xbrl = filing.xbrl()
print(xbrl.to_context())  # ~275 Tokens — Übersicht
# Drill-down nur bei Bedarf
income = xbrl.statements.income_statement
print(income)
```

### UC2 — 10-K/10-Q Section-Search (Risk-Factors / MD&A / Notes)

**Trigger:** Reviewer-Frage zu narrativem Filing-Inhalt (z.B. „Was sagt das 10-Q zum KHC-OTTI-Risk?", „PacifiCorp-Wildfire-unpaid-Liability Q2-Stand?").
**Action:** Latest-Filing holen, `.items()` für Section-Liste, gezielt drill-down (nicht `text()` global).
**Real-Run-Trigger:** **02./03.08.2026 BRK Q2 10-Q** mit 5 expliziten Sub-Watches (alle in PIPELINE #36-#41):
- **#36** KHC-OTTI-Note (FV vs Carrying)
- **#37** Form-13F separater UC5-Trigger (~14.05.)
- **#38** BHE Effective Tax Rate Reconciliation Q2
- **#39** OxyChem Goodwill-vs-Identifiable-Assets Allocation
- **#40** Buyback Cashflow vs Press-Release Reconciliation
- **#41** GEICO UW Decel-Asymmetry Note 24

```python
from edgar import Company
c = Company("BRK.B")
filing = c.get_filings(form="10-Q").latest()
print(filing.to_context())  # ~50 Tokens
sections = filing.items()
# Spezifische Section: KHC-OTTI typ. in „Equity Method Investments Note"
results = filing.search("Kraft Heinz")
```

### UC3 — Form-4-**Eskalations-only**

**Trigger:** ambige Form-4-Befunde aus `insider-intelligence/insider_intel.py` (z.B. nicht-eindeutiger 10b5-1-Plan-Status, Cashless-Exercise-Disambiguation, Footnote-Indizien gegen XML-Feld).
**Action:** EDGAR-Form-4-Filing direkt lesen, Footnotes manuell prüfen, Reviewer-Block mit Original-Filing-URL liefern.
**NICHT-Aktion:** Bulk-Insider-Scoring (das macht `insider_intel.py`); Non-US-Insider (AMF/AFM, manuell).

```python
from edgar import Company
c = Company("AVGO")
form4 = c.get_filings(form="4")[:3]  # latest 3 Form-4
for f in form4:
    print(f.to_context())
```

### UC4 — Multi-Period-Trend via Entity-Facts-API

**Trigger:** Methodology-Watch-Befund (z.B. defeatbeta-Inkonsistenz V/MSFT, PIPELINE #21/#25), 5J/20Q-Verifikation gegen XBRL.
**Action:** `Company.income_statement(period=..., periods=N)` / `.balance_sheet(...)` / `.cash_flow_statement(...)`.

**API-Hinweis (context7-validiert 2026-05-08, edgartools 5.31.0):** `period`-Parameter steuert Annual/Quarterly/TTM. **Default ist `period='annual'`** — `periods=20` ohne `period=`-Parameter liefert **20 Annual periods (kapped auf verfügbare ~6)**, NICHT 20 Quartale. Für 5J-Quarterly explizit `period='quarterly', periods=20` setzen. Legacy: `annual=False` als Synonym für `period='quarterly'`.

```python
from edgar import Company
c = Company("MSFT")

# 5J quarterly (20 Quartale) — Methodology-Watch-Default
income = c.income_statement(period='quarterly', periods=20)
print(income)

# Alternative: TTM (rolling 4 quarters) für aktuellen Trend
ttm = c.income_statement(period='ttm')

# Alternative: Annual (Default) für Long-Range-Trend
annual = c.income_statement(periods=10)  # 10J annual

# Convenience: as_dataframe=True für Pandas-Pipeline
df = c.income_statement(period='quarterly', periods=20, as_dataframe=True)
```

### UC5 — Form-13F Holdings-Pull (NEU für v1.1)

**Trigger:** **14.05.2026 BRK Apple-Trim-Magnitude** (PIPELINE #37) — Form-13F Q1-26 Filing typisch ~mid-Mai (45 Tage nach Quartalsende). Per-Holding-Share-Count-Δ Q4-25 → Q1-26.
**Action:** BRK CIK 0001067983, Form 13F-HR holen, Holdings-Tabelle parsen.

```python
from edgar import Company
brk = Company("0001067983")  # BRK CIK
f13f = brk.get_filings(form="13F-HR").latest()
print(f13f.to_context())
# Holdings-Section
print(f13f.search("Apple"))
```

**Verifikations-Anker:** Cost-Basis-Trim Q1-26 Consumer-Products $11,90B → $8,85B = -$3,05B (-25,6%, PIPELINE §12.4 BRK-Pre-Brief §2). UC5-Run sollte Apple-Share-Count-Δ liefern und das gegen Cost-Basis-Δ gegenrechnen.

### UC6 — 8-K Material-Events-Read (NEU für v1.1)

**Trigger:** Earnings-Calendar-Stufe-2-Drift-Detection (z.B. Pre-Earnings-Pre-Announcement, M&A-Event-Filing, ad-hoc Material-Events). Earnings-Calendar pulse via `03_Tools/earnings_calendar.py` flaggt Drift; UC6 verifiziert über 8-K.
**Action:** `get_filings(form="8-K").latest()` + `filing.items` (attribute, kein method-call) zur Material-Event-Klassifikation.

**API-Hinweis (live-validiert 2026-05-08, edgartools 5.31.0):** `filing.items` ist **attribute** (string mit Item-Numbers wie `"5.07"` / `"8.01"` / `"5.02"`), KEIN method. `filing.items()` würde `TypeError: 'str' object is not callable` werfen.

```python
from edgar import Company
c = Company("AVGO")
recent_8k = c.get_filings(form="8-K")[:5]
for f in recent_8k:
    print(f.to_context())
    print(f"Items: {f.items}  (Filing: {f.filing_date})")
# Beispiel-Live-Output 2026-05-08 für AVGO 3 latest:
#   2026-04-21 → Items: 5.07  (Submission of Matters to a Vote of Security Holders)
#   2026-04-06 → Items: 8.01  (Other Events)
#   2026-04-02 → Items: 5.02  (Departure/Election of Directors / Officers)
```

---

## §3 Smoke-Test (`_smoke_test.py`)

Datei: `01_Skills/sec-edgar-skill/_smoke_test.py` (analog `01_Skills/backtest-ready-forward-verify/_smoke_test.py`-Pattern).

6 Cases:

| # | Case | Verifiziert |
|---|------|-------------|
| 1 | Identity-Pre-Check Failure-Path | `Company("MSFT")` ohne `set_identity()` wirft Error (SEC-Legal-Requirement-Verify) |
| 2 | MSFT-Lookup | `"MICROSOFT" in c.name.upper()`, `cik`-Padding == "0000789019" |
| 3 | MSFT-income_statement Annual+Quarterly-Regression | (a) Default `periods=3` liefert 3 FY-prefixed Annual-Columns (b) Explicit `period='quarterly', periods=4` liefert Q-prefixed Quarterly-Columns. Schützt vor UC4-Comment-vs-Code-Mismatch (post-context7-Validation 2026-05-08). |
| 4 | Company.to_context() Char-Budget | `len(c.to_context()) ≤ 500 chars` (≈100 Tokens nominal +25% Puffer); Live-Char-Wert wird in PASS-Output geloggt für Audit |
| 5 | XBRL.to_context() Char-Budget | `len(xbrl.to_context()) ≤ 1500 chars` (≈300 Tokens nominal +25% Puffer); Live-Char-Wert geloggt |
| 6 | edgartools-Version-Sanity | `pip show edgartools` Version-String erfasst und in PASS-Output geloggt (Drift-Buffer-Audit) |

Run:
```bash
python 01_Skills/sec-edgar-skill/_smoke_test.py
```
Expected (post-edgartools-Install + Identity): `OK all 6/6 cases passed` (ASCII-Output-Pattern für Windows-Console-Encoding-Robustheit; identische Semantik zum Plan-Original `✅`).

---

## §4 Setup (einmalig)

```bash
# Voraussetzung: Python 3.10+ mit pip
pip install edgartools

# Verify (ohne set_identity wirft IdentityNotSetError):
python -c "from edgar import set_identity, Company; set_identity('Tobias Kowalski tobikowa90@gmail.com'); print(Company('MSFT').name)"
```

Expected: `MICROSOFT CORP` (SEC-Registrar-Legal-Form; nicht `Microsoft Corporation`).

---

## §5 Verhältnis zu insider-intelligence + non-us-fundamentals

| Aufgabe | sec-edgar-skill (dieser) | insider-intelligence | non-us-fundamentals |
|---------|--------------------------|----------------------|---------------------|
| Insider Form-4 Bulk-Scoring | — | **Primary** (insider_intel.py, 8 US-Satelliten CIK hardcoded) | — |
| Insider Form-4 Eskalation (ambige Pattern) | **Primary** (UC3) | Primary (Bulk), eskaliert hierhin bei Disambiguation-Bedarf | — |
| FLAG-Detection ($20M-Schwelle 90d) | — | **Primary** | — |
| 10-K/10-Q Section-Search | **Primary** (UC2) | — | — |
| 8-K Material-Events | **Primary** (UC6) | — | — |
| Form-13F Holdings | **Primary** (UC5) | — | — |
| Multi-Period-Trend (5J/20Q XBRL) | **Primary** (UC4) | — | — |
| Daten-Konflikt-Schiedsquelle (XBRL) | **Primary** (UC1) | — | — |
| Insider Non-US (ASML AFM / RMS+SU AMF) | — | — | **Primary** (manuell, kein Form-4-Pflicht für FPI) |
| Fundamentals Non-US (ASML/RMS/SU) | — | — | **Primary** (eodhd_intel.py, yfinance) |

**Kein Cross-Hop:** Wenn `!Analysiere AVGO` läuft, wird dieser Skill **nicht** aufgerufen — `dynastie-depot` orchestriert direkt `insider_intel.py` + Shibui + defeatbeta. Eskalation erfolgt **manuell durch den Reviewer**, nicht automatisch durch Skill-Chaining.

---

## §6 Wartung

**Bei edgartools-API-Drift / Major-Version-Bump:**
- Smoke-Test `_smoke_test.py` Case 6 erfasst Version-String — bei Drift gegen Plan-Stand-Version (`5.31.0`) STOP + Plan-Header-Notice schreiben
- Method-Renames (z.B. `to_context()` → `summary()`-Drift) → Token-Tabelle nachziehen + alle UC-Beispiele anpassen
- 10b5-1 XML-Feld-Drift (SEC Amendment 2023+) → `insider-intelligence/SKILL.md`-Dokumentation parallel updaten

**Bei Slot-Tausch (US-Satellit wird ausgetauscht):**
- Kein Skill-File-Edit nötig (Skill operiert ticker-agnostisch via `Company(ticker)`-Lookup)
- `insider-intelligence` CIK-Tabelle muss separat aktualisiert werden — orthogonaler Workflow

---

## §7 Anti-Patterns (vermeiden)

### DON'T: `filing.text()` für Übersichts-Operationen
```python
# BAD — 50K+ Tokens
text = filing.text()
```

### DO: `.to_context()` first, dann gezielt Section
```python
# GOOD — ~50 Tokens
print(filing.to_context())
# bei Bedarf: filing.search("specific keyword")
```

### DON'T: Bulk-Form-4-Scan via diesen Skill
```python
# BAD — duplicates insider_intel.py
form4_all = c.get_filings(form="4")[:100]  # gehört in insider_intel.py
```

### DO: nur Eskalations-Form-4 manuell ad-hoc
```python
# GOOD — UC3 only, Reviewer-Eskalation
form4 = c.get_filings(form="4")[:3]
for f in form4:
    print(f.to_context())
```

---

*🦅 sec-edgar-skill v1.1 | Dynastie-Depot | Stand: 2026-05-08 | edgartools 5.31.0 | Auto-Discovery via description-Frontmatter (Trigger: !EdgarLookup, !EdgarFiling, !Edgar13F)*
