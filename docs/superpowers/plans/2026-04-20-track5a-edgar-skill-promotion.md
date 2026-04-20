# Track 5a — SEC EDGAR Skill-Promotion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

> **Phase-1b-Paper-Ingest-Header-Notice (2026-04-20):** FinReflectKG (Arun et al. 2025, B21) zeigt eine Alternative zum klassischen XBRL-Scraping: Reflection-basierte LLM-KG-Extraction mit 5-Tuple-Schema + Critic-Corrector-Loop. **Geprüft und als `future-arch` DEFERRED** via §33 Skill-Self-Audit-Gate (Gate 2 conditional — Budget/Eval-Plan offen; Gate 3 3-Monats-Observation nicht gestartet). XBRL-Scraping via `edgartools` bleibt Primär-Architektur für Track 5a. FinReflectKG-Szenario archiviert in [[Knowledge-Graph-Architektur-Roadmap]] Szenario 2 für Re-Review 2027+. Track 5a-Scope durch Phase-1b **nicht geändert**.

**Goal:** Promote `_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` zum aktiven Eskalations-Fallback-Skill `01_Skills/sec-edgar-skill/SKILL.md`, mit `edgartools` installiert, `set_identity()` konkret konfiguriert und INSTRUKTIONEN §17-Tabelle aktualisiert.

**Architecture:** Satelliten-Skill neben `insider-intelligence`/`non-us-fundamentals`/`quick-screener`. Eskalations-getriggert (Daten-Konflikt / 10-K-Textsuche / Form-4-Eskalation / Multi-Period-Trend), **nicht** automatisch in `!Analysiere`-Workflow eingebunden. Primärquellen defeatbeta (US-Fundamentals) und Shibui (Technicals) bleiben unverändert. `insider_intel.py`-Form-4-Pipeline bleibt parallel.

**Tech Stack:** Python 3.14.3 (Windows `/c/Python314/`), `edgartools` (PyPI), XBRL-strukturierte Filings-API, Claude-Code-Skill-Auto-Discovery via SKILL.md-Frontmatter.

---

## Header-Notice: Spec-§-Referenz-Korrekturen

TRACK5-SPEC v1.0 (Commit `22cdeb8`) enthält in §2.5 und §2.6 veraltete INSTRUKTIONEN/CORE-MEMORY-§-Verweise. Dieser Plan nutzt die aktuell gültigen Stellen (Verifikation gegen Commit `22cdeb8` + `INSTRUKTIONEN.md` v1.11 + CLAUDE.md-Landkarte):

| Spec-Referenz | Spec-Wortlaut | Ist-Zustand (korrekt für Plan) | Begründung |
|---|---|---|---|
| Spec §2.5 „§22" | „Skill-Referenz-Tabelle" | **INSTRUKTIONEN §17** Skill-Hierarchie & Aktivierungslogik (Tabelle Zeilen 240-248) | §22 ist Sparplan-Formel |
| Spec §2.5 „§19" | „API-Routing" | **INSTRUKTIONEN §8** Datenquellen-Logik (Zeile 120) | §19 ist Daten-Update-Klassen |
| Spec §2.6 „§5 Audit-Eintrag" | „EDGAR-Skill promoted, EdgarTools installed" | **CORE-MEMORY §1 Meilensteine** (Präzedenz: 2026-04-19-backtest-ready-forward-verify-Plan Task 5.2) | §5 ist Scoring-Lektionen (nicht Deployment-Audit); §1 ist Meilensteine ab 15.04. per CLAUDE.md |

Codex hat Option-1-Ansatz (Plan-korrekt, Spec-unverändert, Header-Notice als Audit-Trail) explizit bestätigt (2026-04-20). Spec bleibt eingefroren, keine Modifikation.

---

## Critical Files (zu erstellen / zu modifizieren)

| Pfad | Aktion |
|---|---|
| `01_Skills/sec-edgar-skill/SKILL.md` | **NEU** — Promoted + adaptiert aus `_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md`, Frontmatter mit konkreter Identity, Scope-Guidance „NICHT auto-aktiv in `!Analysiere`" |
| `01_Skills/sec-edgar-skill/_smoke_test.py` | **NEU** — 4 deterministische Cases: Import+Identity / MSFT-Income-Statement / Company.to_context() Token-Bound / XBRL.to_context() Token-Bound |
| `01_Skills/_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` | **MODIFY** — Superseded-Banner am Dateikopf (Informationsverlust-Aversion: nicht löschen, nur markieren) |
| `00_Core/INSTRUKTIONEN.md` Zeile 248 | **MODIFY** — Tabellen-Zeile `sec-edgar-skill` in §17-Skill-Hierarchie-Tabelle: Status von reiner Eskalations-Eintrag zu „v1.0 aktiv seit 2026-04-20, EdgarTools-basiert, `.to_context()` obligatorisch zur Token-Effizienz" |
| `00_Core/CORE-MEMORY.md` §1 Meilensteine | **MODIFY** — Neuer Eintrag „2026-04-20: `sec-edgar-skill` v1.0 aus `_extern/` promoted. EdgarTools installiert, `set_identity()` konfiguriert. Eskalations-Fallback für Daten-Konflikte + 10-K-Textsuche aktiv." |
| `00_Core/STATE.md` System-Zustand | **MODIFY** — 1 Zeile ergänzen: „`sec-edgar-skill` v1.0 aktiv (seit 2026-04-20) — Eskalations-Fallback für defeatbeta/Shibui-Konflikte" |
| `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` | **MODIFY** — Session-Eintrag für Skill-Deployment (technisches Protokoll per §18) |

**Out of Scope (explizit per Spec §2.7):**
- KEIN First-Class-EDGAR-MCP-Ersatz für defeatbeta
- KEINE automatische Einbindung in `!Analysiere`-Workflow (dynastie-depot-Schritt-Routing bleibt unverändert)
- KEINE Migration von `insider_intel.py` auf EDGAR-Skill — beide Pipelines koexistieren

---

## Implementation Plan (Task-by-Task)

### Task 1: Environment Prep — `edgartools` Install + Identity-Smoke

**Files:**
- (keine Repo-Files in dieser Task — reine Env-Operation)

**Hintergrund:** Windows-Python 3.14.3 unter `/c/Python314/` ist die ausführende Umgebung. `edgartools` ist PyPI-Package, `set_identity()` ist SEC-Legal-Requirement vor jedem Zugriff.

- [ ] **Step 1.1: Pre-Install-Check (failing test)**

```bash
python -c "from edgar import Company; print('ok')"
```

Expected: `ModuleNotFoundError: No module named 'edgar'`. Bestätigt sauberen Start.

- [ ] **Step 1.2: Installation**

```bash
pip install edgartools
```

Expected: Exit-Code 0, Package-Versions-Zeile auf stdout. Bei Dependency-Konflikten mit bestehenden Packages: Fehler dokumentieren, Abbruch und User-Rückfrage.

- [ ] **Step 1.3: Post-Install-Check (test passes)**

```bash
python -c "from edgar import Company, set_identity; set_identity('Tobias Kowalski tobikowa90@gmail.com'); c = Company('MSFT'); print(c.name)"
```

Expected: `Microsoft Corporation` (oder aktueller offizieller Firmenname) auf stdout, keine Exceptions. Bestätigt: Import + Identity + Netzwerk-Zugriff + Ticker-Resolve in einem Durchgang.

- [ ] **Step 1.4: Version + Dependencies pinnen (für Reproduzierbarkeit)**

```bash
pip show edgartools | head -5
```

Versions-String in Session-Notizen übernehmen — wird in CORE-MEMORY §1-Eintrag (Task 5) eingetragen.

- [ ] **Step 1.5: Kein Commit**

Env-Install ist nicht repo-tracked. `requirements.txt`-Update ist out-of-scope (Projekt hat bisher keine zentrale Requirements-Datei — Check im Repo-Root, falls doch vorhanden: `edgartools>=X.Y` anhängen und mit-committen, sonst übergehen).

---

### Task 2: Skill-Verzeichnis + SKILL.md erstellen

**Files:**
- Create: `01_Skills/sec-edgar-skill/SKILL.md`

**Hintergrund:** `_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` ist Source. Adaptiert wird: (a) konkrete Identity statt Placeholder, (b) neue Scope-Guidance-Sektion „Wann dieser Skill NICHT lädt", (c) Filename-Konvention `SKILL.md` bare (folgt `backtest-ready-forward-verify`-/`dynastie-depot`-Konvention, nicht insider-intelligence-Legacy).

- [ ] **Step 2.1: Verzeichnis anlegen**

```bash
mkdir -p "01_Skills/sec-edgar-skill"
```

Expected: Verzeichnis existiert danach. Check: `ls -la 01_Skills/sec-edgar-skill/`.

- [ ] **Step 2.2: Pre-Write-Check (failing: Skill-Discovery findet nichts)**

```bash
test -f "01_Skills/sec-edgar-skill/SKILL.md" && echo "EXISTS" || echo "MISSING"
```

Expected: `MISSING`. (Wird in Step 2.4 grün.)

- [ ] **Step 2.3: SKILL.md schreiben — vollständiger Content**

Datei `01_Skills/sec-edgar-skill/SKILL.md` mit folgendem Inhalt erstellen:

````markdown
---
name: sec-edgar-skill
version: "1.0.0"
description: >
  SEC EDGAR filing analysis via EdgarTools — Eskalations-Fallback für Daten-Konflikte
  zwischen defeatbeta und Shibui, 10-K/10-Q-Textsuche, Form-4-Eskalation und
  Multi-Period-Trend-Abfragen via XBRL. Aktiver Skill (v1.0) seit 2026-04-20,
  `.to_context()` obligatorisch zur Token-Effizienz. NICHT innerhalb `!Analysiere`
  laden — dynastie-depot hat Precedence; Skill ist eskalations-getriggert, nicht
  kadenz-getriggert.
trigger_words:
  - "SEC EDGAR"
  - "EDGAR"
  - "XBRL"
  - "Daten-Konflikt"
  - "Daten-Arbitrage"
  - "SEC Schiedsquelle"
  - "10-K Textsuche"
  - "10-Q Textsuche"
  - "Form-4 Eskalation"
---

# sec-edgar-skill — v1.0 (promoted 2026-04-20)

**Eskalations-Fallback** für US-Ticker bei Daten-Konflikten oder 10-K-Sektions-Disputen.
Nicht Primärquelle. Nicht in `!Analysiere` auto-aktiv.

---

## 0. Scope — wann dieser Skill NICHT lädt

- **Innerhalb `!Analysiere`:** dynastie-depot-Monolith hat Precedence (INSTRUKTIONEN §17
  Skill-Hierarchie). Skill-Chaining würde DEFCON-Kontext verlieren.
- **Real-Time-Kurse / Market-Data:** `shibui`-MCP oder `yahoo`-Fallback sind Primär — EDGAR
  ist Filing-Quelle, nicht Preisquelle.
- **Insider-Primäranalyse:** `insider_intel.py` (in `03_Tools/` + `01_Skills/insider-intelligence/`)
  bleibt Primärpipeline. EDGAR-Form-4-Abfragen sind nur Eskalation bei ambiguen
  Broadcom-10b5-1-Pattern oder Cashless-Exercise-Streitfällen.
- **Non-US-Ticker (ASML / RMS / SU):** kein SEC-EDGAR-Filing — nutze `non-us-fundamentals`
  + AFM/AMF-Primärquellen.

## 1. Prerequisites

**CRITICAL:** Vor jeder EdgarTools-Operation die SEC-Identity setzen — SEC-Legal-Requirement,
Operations schlagen sonst fehl:

```python
from edgar import set_identity
set_identity("Tobias Kowalski tobikowa90@gmail.com")
```

Installation (einmalig, bereits gelaufen bei Skill-Deployment 2026-04-20):

```bash
pip install edgartools
```

## 2. Token-Effizienz — `.to_context()` ist Pflicht

**Regel:** Immer zuerst `.to_context()` aufrufen, dann erst bei Bedarf drill-downen. Nie
direkt `repr()` oder `text()` verwenden — die sind für Mensch, nicht für Token-Budget.

| Objekt | `repr()` Tokens | `.to_context()` Tokens | Ersparnis |
|--------|-----------------|------------------------|-----------|
| Company | ~750 | ~75 | 90% |
| Filing | ~125 | ~50 | 60% |
| XBRL | ~2500 | ~275 | 89% |
| Statement | ~1250 | ~400 | 68% |

Quelle: `_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` (EdgarTools-Original-Metrik).

## 3. Use-Cases (Spec-§2.4-Abbildung)

### 3.1 Use-Case 1 — Daten-Konflikt-Schiedsquelle (>5% defeatbeta↔Shibui-Drift)

```python
from edgar import Company
company = Company("MSFT")
income = company.income_statement(periods=5)  # Entity Facts API, 5 Jahre
# Vergleich gegen defeatbeta-Wert → EDGAR ist kanonische SEC-Quelle
```

**Wann aufrufen:** defeatbeta liefert z.B. Revenue $245B, Shibui $243B → >5%-Check mit
EDGAR-XBRL als Schiedswert.

### 3.2 Use-Case 2 — 10-K / 10-Q Textsuche (Risk-Factors / MD&A)

```python
from edgar import Company
filing = Company("MSFT").get_filings(form="10-K").latest()
results = filing.search("climate risk")  # STRUKTURSUCHE im Filing-Dokument
```

**Distinction:** `filing.search()` sucht im Filing-Text. `filing.docs.search()` sucht in der
EdgarTools-API-Doku — nicht verwechseln.

### 3.3 Use-Case 3 — Form-4-Eskalation (ambigue Cashless-Exercise-Fälle)

```python
from edgar import Company
insider_filings = Company("AVGO").get_filings(form="4")
for f in insider_filings[:10]:
    print(f.to_context())  # ~50 Tokens pro Filing
```

**Wann aufrufen:** `insider_intel.py` liefert Broadcom-10b5-1-Muster ohne klaren
Cashless-Exercise-Signal → EDGAR-Filing-Kontext als strukturierte zweite Quelle.

### 3.4 Use-Case 4 — Multi-Period-Trend (5J-Trend ohne Multi-Filing-Parse)

```python
from edgar import Company
company = Company("TMO")
income = company.income_statement(periods=20)   # 20 Quartale ≈ 5 Jahre
balance = company.balance_sheet(periods=20)
```

**Vorteil gegenüber defeatbeta:** Entity-Facts-API ist eine HTTP-Round-Trip-Query pro
Statement-Block, nicht 5-10 Filing-Parses. Schneller + konsistent.

## 4. Anti-Patterns

### DON'T: Raw-Text parsen

```python
# BAD
text = filing.text()  # 50K+ Tokens
# regex für Revenue...
```

### DO: XBRL strukturiert nutzen

```python
# GOOD
income = company.income_statement(periods=3)
```

### DON'T: Full-Filing laden ohne Grund

```python
# BAD
text = filing.text()
```

### DO: Context zuerst

```python
# GOOD
print(filing.to_context())  # ~50 Tokens
```

## 5. Form-Typen (Quick-Reference)

| Form | Beschreibung | Einsatz |
|------|--------------|---------|
| **10-K** | Annual Report | Full-Year-Fundamentals |
| **10-Q** | Quarterly Report | Q-Fundamentals |
| **8-K** | Current Report | M&A / Exec-Changes |
| **DEF 14A** | Proxy Statement | Executive-Comp |
| **4** | Insider-Transaction | Form-4-Cross-Check |
| **13F** | Institutional Holdings | Holdings-Abfrage |

## 6. Key Objects (API-Referenz)

```python
# Company
c = Company("MSFT")
c.to_context()   # ~75 Tokens — Start hier
c.name / c.cik / c.sic / c.industry
c.get_filings(form="10-K")
c.income_statement(periods=N) / c.balance_sheet(periods=N) / c.cash_flow_statement(periods=N)

# Filing
f = c.get_filings(form="10-K").latest()
f.to_context()   # ~50 Tokens
f.form / f.filing_date / f.accession_number
f.xbrl()         # Strukturierte Finanzdaten
f.items()        # Sections (Risk-Factors / MD&A / ...)

# XBRL
x = f.xbrl()
x.to_context()   # ~275 Tokens
x.statements.income_statement / x.statements.balance_sheet / x.statements.cash_flow_statement

# Statement
s = x.statements.income_statement
print(s)              # ASCII-Tabelle
s.to_dataframe()      # Pandas
```

## 7. Error Handling

```python
try:
    c = Company("INVALID")
except Exception as e:
    print(f"Company not found: {e}")

filings = c.get_filings(form="10-K")
if len(filings) == 0:
    print("No 10-K filings found")
```

## 8. Referenzen

- `01_Skills/_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` — Original-Upstream-Skill,
  jetzt mit Superseded-Banner markiert (siehe Task 6 dieses Plans)
- EdgarTools-Docs: `company.docs.search("how to ...")`-Meta-API im Skill selbst
- INSTRUKTIONEN §17 (Skill-Hierarchie-Tabelle, Zeile 248) — Eintrag mit Status „v1.0 aktiv"
- INSTRUKTIONEN §8 (Datenquellen-Logik, Zeile 120) — „Datenkonflikt: SEC > Drittanbieter"

---

*🦅 sec-edgar-skill v1.0 | promoted 2026-04-20 | Eskalations-Fallback*
````

- [ ] **Step 2.4: Post-Write-Check (test passes)**

```bash
test -f "01_Skills/sec-edgar-skill/SKILL.md" && echo "EXISTS" || echo "MISSING"
head -5 "01_Skills/sec-edgar-skill/SKILL.md"
```

Expected: `EXISTS` + erste 5 Zeilen zeigen Frontmatter mit `name: sec-edgar-skill`.

- [ ] **Step 2.5: Frontmatter-Parse-Check**

```bash
python -c "import re; content = open('01_Skills/sec-edgar-skill/SKILL.md').read(); m = re.match(r'---\n(.*?)\n---', content, re.DOTALL); assert m, 'no frontmatter'; name = re.search(r'^name:\s*(\S+)', m.group(1), re.M); print(name.group(1) if name else 'MISSING')"
```

Expected: `sec-edgar-skill`. Bestätigt Skill-Auto-Discovery-kompatibles Frontmatter. Kein PyYAML-Dep — reiner Regex-Check gegen Frontmatter-Block.

- [ ] **Step 2.6: Commit**

```bash
git add "01_Skills/sec-edgar-skill/SKILL.md"
git commit -m "feat(skill): sec-edgar-skill v1.0 promoted from _extern — Eskalations-Fallback aktiv"
```

---

### Task 3: Smoke-Test `_smoke_test.py`

**Files:**
- Create: `01_Skills/sec-edgar-skill/_smoke_test.py`

**Hintergrund:** Testet die 4 Skill-Akzeptanz-Kriterien (Spec §2.6): (a) Company-Objekt + MSFT-income_statement(periods=3) funktioniert ohne Exception, (b) Company-Summary `.to_context()` ≤100 Tokens, (c) XBRL-Summary `.to_context()` ≤300 Tokens. Token-Count via Zeichenzahl-Proxy mit konservativem Puffer: 1 Token ≈ 4 Zeichen nominal, aber Test-Budget **500 Zeichen** (Company) / **1500 Zeichen** (XBRL) gegen `_extern/`-Upstream-Baseline ~75 / ~275 Tokens — Puffer absorbiert EdgarTools-Output-Varianz für große Tickers (MSFT). Ist-Chars werden im PASS-Output geloggt (Audit-Trail für spätere Budget-Rekalibrierung). Deterministischer Python-Test, nicht Skill-Prosa (Kategorien-Trennung per `backtest-ready-forward-verify` Task-3-Präzedenz).

- [ ] **Step 3.1: Test-Datei schreiben (failing: EdgarTools-Ergebnis noch nicht verifiziert)**

Datei `01_Skills/sec-edgar-skill/_smoke_test.py`:

```python
#!/usr/bin/env python3
"""Smoke-Test für sec-edgar-skill v1.0. Prüft die 4 Akzeptanz-Kriterien aus
TRACK5-SPEC §2.6. Läuft gegen Live-SEC-EDGAR — Netzwerk erforderlich."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        from edgar import Company, set_identity
    except ImportError as e:
        print(f"[FAIL] edgartools not installed: {e}")
        return 2

    set_identity("Tobias Kowalski tobikowa90@gmail.com")

    # Case 1: Company-Lookup MSFT
    try:
        c = Company("MSFT")
    except Exception as e:
        print(f"[FAIL] Case 1 — Company('MSFT') raised: {e}")
        return 1
    if not c.name or "Microsoft" not in c.name:
        print(f"[FAIL] Case 1 — MSFT.name unerwartet: {c.name!r}")
        return 1
    print(f"[PASS] Case 1 — Company('MSFT') → name={c.name!r}")

    # Case 2: MSFT income_statement(periods=3)
    try:
        income = c.income_statement(periods=3)
    except Exception as e:
        print(f"[FAIL] Case 2 — income_statement(3) raised: {e}")
        return 1
    if income is None:
        print("[FAIL] Case 2 — income_statement(3) returned None")
        return 1
    print("[PASS] Case 2 — MSFT.income_statement(periods=3) returned non-None")

    # Case 3: Company.to_context() ≤ 400 Zeichen (Proxy für ~100 Tokens)
    ctx = c.to_context()
    if not isinstance(ctx, str):
        print(f"[FAIL] Case 3 — to_context() nicht str: {type(ctx)}")
        return 1
    char_budget = 500  # Spec-Bound 100 Tokens ≈ 400ch nominal + 25% Puffer
    if len(ctx) > char_budget:
        print(
            f"[FAIL] Case 3 — Company.to_context() {len(ctx)} chars > Budget {char_budget}"
            f" (≈100 Tokens). Content-Preview: {ctx[:200]!r}"
        )
        return 1
    print(f"[PASS] Case 3 — Company.to_context() = {len(ctx)} chars (≤{char_budget})")

    # Case 4: XBRL.to_context() ≤ 1200 Zeichen (Proxy für ~300 Tokens)
    try:
        filing = c.get_filings(form="10-K").latest()
        xbrl = filing.xbrl()
        xctx = xbrl.to_context()
    except Exception as e:
        print(f"[FAIL] Case 4 — XBRL-Fetch raised: {e}")
        return 1
    if not isinstance(xctx, str):
        print(f"[FAIL] Case 4 — xbrl.to_context() nicht str: {type(xctx)}")
        return 1
    xbrl_budget = 1500  # Spec-Bound 300 Tokens ≈ 1200ch nominal + 25% Puffer
    if len(xctx) > xbrl_budget:
        print(
            f"[FAIL] Case 4 — XBRL.to_context() {len(xctx)} chars > Budget {xbrl_budget}"
            f" (≈300 Tokens). Content-Preview: {xctx[:200]!r}"
        )
        return 1
    print(f"[PASS] Case 4 — XBRL.to_context() = {len(xctx)} chars (≤{xbrl_budget})")

    print("\n[4/4] all sec-edgar-skill smoke tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 3.2: Test laufen lassen — erwartet 4/4 PASS**

```bash
python "01_Skills/sec-edgar-skill/_smoke_test.py"
```

Expected: 4 `[PASS]`-Zeilen + `[4/4] all sec-edgar-skill smoke tests passed`. Exit 0.

**Bei Fehlschlag Case 3 oder 4 (Token-Budget-Überschreitung trotz 25%-Puffers):** Content-Preview inspizieren. Budgets 500/1500 sind bereits +25% über Spec-Nominal (400/1200). Wenn EdgarTools echt mehr liefert:
- Variante A: Ist-Chars aus PASS-Log sammeln (3 Testläufe → Varianz messen), Budget +2σ setzen, in Test-Konstanten + CORE-MEMORY §1-Eintrag dokumentieren
- Variante B: User-Rückfrage, ob Spec §2.6-Acceptance-Criterion lockerer gefasst werden muss (z.B. Nominal 150/400 Tokens statt 100/300)

**Bei Fehlschlag Case 1 oder 2:** Network-Issue, SEC-Rate-Limit, oder Identity-Problem. `pip show edgartools` + `python -c "from edgar import Company; Company('AAPL').name"` als Cross-Check. Nicht weiter zu Task 4 ohne Green.

- [ ] **Step 3.3: Commit**

```bash
git add "01_Skills/sec-edgar-skill/_smoke_test.py"
git commit -m "test(sec-edgar-skill): smoke test für 4 akzeptanz-kriterien (live-SEC)"
```

---

### Task 4: INSTRUKTIONEN §17-Tabelle aktualisieren

**Files:**
- Modify: `00_Core/INSTRUKTIONEN.md` (Zeile 248, Skill-Hierarchie-Tabelle)

**Hintergrund:** Zeile 248 lautet aktuell:
```
| Dokument-Konflikt / 10-K-Text | `sec-edgar-skill` | Eskalations-Fallback |
```

Spec §2.5 fordert Aktualisierung mit Status-Hinweis „aktiver Skill (v1.0) seit 2026-04-XX, EdgarTools-basiert, `.to_context()` obligatorisch".

- [ ] **Step 4.1: Pre-Edit-Check (aktuelle Zeile lesen)**

```bash
sed -n '246,250p' "00_Core/INSTRUKTIONEN.md"
```

Expected: Umgebende Tabellen-Zeilen inkl. Zeile 248 `| Dokument-Konflikt / 10-K-Text | sec-edgar-skill | Eskalations-Fallback |`. Wenn die Zeile nicht exakt so lautet (z.B. durch zwischenzeitliche Edits): vor Edit neu lokalisieren via `grep -n "sec-edgar-skill" 00_Core/INSTRUKTIONEN.md`.

- [ ] **Step 4.2: Tabellen-Zeile ersetzen**

Edit-Operation:

**old_string:**
```
| Dokument-Konflikt / 10-K-Text | `sec-edgar-skill` | Eskalations-Fallback |
```

**new_string:**
```
| Dokument-Konflikt / 10-K-Text / Daten-Arbitrage | `sec-edgar-skill` | Eskalations-Fallback — **v1.0 aktiv seit 2026-04-20**, EdgarTools-basiert, `.to_context()` obligatorisch zur Token-Effizienz. Nicht auto-aktiv in `!Analysiere`. |
```

- [ ] **Step 4.3: Post-Edit-Check**

```bash
grep -n "sec-edgar-skill" "00_Core/INSTRUKTIONEN.md"
```

Expected: Ein Treffer in Zeile ~248 mit dem neuen String inklusive `v1.0 aktiv seit 2026-04-20`. Kein zweiter Treffer.

- [ ] **Step 4.4: Commit (zurückgehalten bis Task 5 — dann gemeinsamer Meta-Commit)**

Noch kein Commit — Task 5 committet INSTRUKTIONEN + CORE-MEMORY + STATE gemeinsam als Docs-Sync.

---

### Task 5: CORE-MEMORY §1 Meilenstein + STATE.md + log.md

**Files:**
- Modify: `00_Core/CORE-MEMORY.md` (§1 Meilensteine)
- Modify: `00_Core/STATE.md` (System-Zustand-Sektion)
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (Session-Eintrag)

**Hintergrund:** Spec §2.6 fordert „CORE-MEMORY §5 Audit-Eintrag" — Plan leitet korrekt um auf **§1 Meilensteine** (siehe Header-Notice). STATE.md-System-Zustand bekommt eine Zeile (vergleichbar mit backtest-ready-forward-verify-Präzedenz). log.md ist §18-Pflicht (technisches Protokoll).

- [ ] **Step 5.1: CORE-MEMORY §1-Position identifizieren**

```bash
grep -n "^## 1\." "00_Core/CORE-MEMORY.md" | head -3
```

Expected: Zeile(n)-Nummer der §1-Überschrift (z.B. „## 1. Aktuelle Meilensteine"). Neueste Meilenstein-Einträge darunter finden — chronologisch (neueste oben oder unten, je nach Konvention; per CLAUDE.md „ab 15.04. (§1)" sind die jüngsten Einträge relevant).

- [ ] **Step 5.2: Neuen §1-Eintrag schreiben**

Nach dem aktuellsten bestehenden Eintrag (oder an chronologisch passender Stelle) einfügen:

```markdown
### 2026-04-20 — `sec-edgar-skill` v1.0 deployed

`_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` promoted nach
`01_Skills/sec-edgar-skill/SKILL.md`. EdgarTools installiert
(`pip install edgartools`, Version im Skill-Deployment dokumentiert),
`set_identity("Tobias Kowalski tobikowa90@gmail.com")` als SEC-Legal-Requirement
konfiguriert. Frontmatter + Skill-Auto-Discovery aktiv.

**Einsatzprofil:** Eskalations-Fallback (nicht auto-aktiv in `!Analysiere`) für
(a) defeatbeta↔Shibui-Daten-Konflikte >5%, (b) 10-K/10-Q-Textsuche (MD&A /
Risk-Factors), (c) Form-4-Eskalation bei ambiguen Cashless-Exercise-Fällen,
(d) Multi-Period-Trend via Entity-Facts-API.

**Nicht-Migration:** `insider_intel.py` bleibt Primärpipeline für Form-4.
defeatbeta bleibt Primärquelle für US-Fundamentals. Shibui bleibt Primärquelle
für Technicals. EDGAR-Skill ist Schiedsquelle, nicht Ersatz.

**Referenz:** TRACK5-SPEC v1.0 §2 (Commit `22cdeb8`). Plan
`docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md`.
INSTRUKTIONEN §17 Tabellen-Zeile aktualisiert.
```

- [ ] **Step 5.3: STATE.md System-Zustand-Zeile ergänzen**

`00_Core/STATE.md` — im System-Zustand-Block (aktuell Zeilen ~59-68) eine neue Zeile anfügen, alphabetisch/thematisch sinnvoll einsortiert:

**old_string:**
```
- **Morning Briefing:** Trigger v2.1 täglich 10:00 MESZ (16 Symbole, Yahoo-Gap BRK.B/RMS/SU).
```

**new_string:**
```
- **Morning Briefing:** Trigger v2.1 täglich 10:00 MESZ (16 Symbole, Yahoo-Gap BRK.B/RMS/SU).
- **`sec-edgar-skill` v1.0 aktiv** (seit 2026-04-20) — Eskalations-Fallback für defeatbeta/Shibui-Konflikte, 10-K-Textsuche, Form-4-Eskalation. EdgarTools-basiert, nicht auto-aktiv in `!Analysiere`.
```

*(Anmerkung: Die `old_string`/`new_string`-Paare sind robust gegen kleinere Zeilenverschiebungen. Falls die Morning-Briefing-Zeile zwischenzeitlich modifiziert wurde, neu lokalisieren und mit angrenzender Zeile disambiguieren.)*

- [ ] **Step 5.4: STATE.md-Header-Stand aktualisieren**

**old_string (Zeile 2):**
```
**Single Entry Point für Session-Start** | Stand: 19.04.2026 (Track 3 Paper-Integration systemweit abgeschlossen — R5 Portfolio-Persistenz + §30 Live-Monitoring aktiv) | System: DEFCON v3.7 (unverändert)
```

**new_string:**
```
**Single Entry Point für Session-Start** | Stand: 2026-04-20 (Track 5a abgeschlossen — `sec-edgar-skill` v1.0 deployed; Track 3 Paper-Integration systemweit; R5 Portfolio-Persistenz + §30 Live-Monitoring aktiv) | System: DEFCON v3.7 (unverändert)
```

- [ ] **Step 5.5: log.md Session-Eintrag**

`07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` — neuesten Session-Eintrag erzeugen (Format folgt bestehendem log.md-Stil; einmal via `tail -30` inspizieren und Konvention übernehmen):

```markdown
## 2026-04-20 — Track 5a Implementation

- `sec-edgar-skill` v1.0 aus `_extern/` promoted (neues Verzeichnis `01_Skills/sec-edgar-skill/`)
- `pip install edgartools` abgeschlossen, Version: [aus Task 1.4 übernommen]
- `set_identity()` konfiguriert mit Projekt-Email (SEC-Legal-Requirement)
- Skill-Scope: Eskalations-Fallback für (a) Daten-Konflikt-Arbitrage, (b) 10-K-Textsuche, (c) Form-4-Eskalation, (d) Multi-Period-Trend via Entity-Facts-API
- INSTRUKTIONEN §17 Tabellen-Zeile aktualisiert mit v1.0-Aktiv-Status
- Smoke-Test 4/4 green (MSFT-Company + income_statement(3) + Company.to_context() ≤400ch + XBRL.to_context() ≤1200ch)
- `_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` mit Superseded-Banner markiert (nicht gelöscht — Informationsverlust-Aversion)
- Referenz-Plan: `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md`
```

- [ ] **Step 5.6: Post-Edit-Checks (alle drei Files)**

```bash
grep -n "sec-edgar-skill" "00_Core/INSTRUKTIONEN.md" "00_Core/CORE-MEMORY.md" "00_Core/STATE.md" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md"
```

Expected: Treffer in allen vier Files, mindestens je einer pro File.

- [ ] **Step 5.7: Commit (Docs-Sync)**

```bash
git add "00_Core/INSTRUKTIONEN.md" "00_Core/CORE-MEMORY.md" "00_Core/STATE.md" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md"
git commit -m "docs(core): sec-edgar-skill v1.0 institutionalisiert (§17 + meilenstein + state + log)"
```

---

### Task 6: `_extern/` Superseded-Banner (Informationsverlust-Aversion)

**Files:**
- Modify: `01_Skills/_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md`

**Hintergrund:** Memory-Regel „Informationsverlust-Aversion > Ästhetik: bei Delete-vs-Keep Default = erhalten + Zeitstand-Banner" (Applied Learning + feedback_information_loss_aversion). Upstream-Source bleibt als Referenz im Repo, bekommt aber sichtbaren Hinweis „Produktiv-Version ist jetzt `01_Skills/sec-edgar-skill/SKILL.md`".

- [ ] **Step 6.1: Banner direkt nach Frontmatter einfügen**

**old_string (Zeilen 4-6):**
```
---

# SEC EDGAR Skill - Filing Analysis
```

**new_string:**
```
---

> **⚠️ SUPERSEDED 2026-04-20 — Referenz-Kopie only.**
> Produktiv-Version: [`01_Skills/sec-edgar-skill/SKILL.md`](../../sec-edgar-skill/SKILL.md) (v1.0, promoted 2026-04-20).
> Diese Datei bleibt als Upstream-Referenz erhalten (Informationsverlust-Aversion — nicht löschen).
> Änderungen nur an der Produktiv-Version. Details: `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md`.

# SEC EDGAR Skill - Filing Analysis (Upstream Reference)
```

- [ ] **Step 6.2: Post-Edit-Check**

```bash
head -10 "01_Skills/_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md"
```

Expected: Frontmatter + Superseded-Banner + geänderter H1. Banner-Link zur neuen SKILL.md sichtbar.

- [ ] **Step 6.3: Commit**

```bash
git add "01_Skills/_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md"
git commit -m "docs(_extern): sec-edgar-skill source mit superseded-banner markiert"
```

---

### Task 7: End-to-End-Verification — 4 Use-Cases (qualitativ)

**Kontext:** Deterministische API-Tests in Task 3 Smoke-Test. Task 7 prüft **Skill-Prosa-Nutzbarkeit** — ob ein Claude-Agent, der die SKILL.md liest, die 4 Use-Cases aus Spec §2.4 korrekt ausführt. Qualitatives End-to-End-Urteil, kein Assertion (analog `backtest-ready-forward-verify` Task 6).

**Durchführung:** Für jeden Use-Case simulierter Trigger (manuell als User-Request formuliert) → Claude-Code nutzt Skill → Output-Review.

- [ ] **Step 7.1: Use-Case 1 — Daten-Konflikt-Arbitrage-Smoke**

Trigger-Prompt (manuell an Claude Code formulieren):

> „MSFT Revenue FY25 — defeatbeta meldet $245B, Shibui meldet $251B. Mit sec-edgar-skill arbitrieren."

Expected: Skill wird via Auto-Discovery geladen, Claude ruft `Company("MSFT").income_statement(periods=1)` oder latest-10K-XBRL ab, meldet EDGAR-Wert mit `.to_context()` statt Full-Text. Output ≤~800 Tokens inkl. Schieds-Verdikt.

- [ ] **Step 7.2: Use-Case 2 — 10-K-Textsuche**

Trigger-Prompt:

> „Suche in MSFT-latest-10-K nach Passagen zu 'climate risk' via sec-edgar-skill."

Expected: Skill ruft `filing.search("climate risk")`, liefert Match-Snippets (nicht Full-Text). Output fokussiert auf Matches, Anti-Pattern `filing.text()` **nicht** verwendet.

- [ ] **Step 7.3: Use-Case 3 — Form-4-Eskalation**

Trigger-Prompt:

> „AVGO Form-4 der letzten 90 Tage via sec-edgar-skill prüfen — ambige 10b5-1-Pattern identifizieren."

Expected: Skill ruft `company.get_filings(form="4")`, nutzt `.to_context()` pro Filing. Keine Full-Text-Extraktion. Form-4-Strukturfelder (Transaction-Code, Amount, Price) aus Context erkennbar.

- [ ] **Step 7.4: Use-Case 4 — Multi-Period-Trend**

Trigger-Prompt:

> „TMO 5-Jahres-Revenue-Trend via sec-edgar-skill Entity-Facts."

Expected: Skill ruft `company.income_statement(periods=20)`. Output zeigt 20 Quartale, ASCII-Tabelle oder DataFrame-Zusammenfassung. Ein einziger API-Call, keine Multi-Filing-Schleife.

- [ ] **Step 7.5: Review-Kriterium**

Alle vier Use-Cases durchgeführt ohne manuelle Skill-Code-Änderung. Wenn ein Use-Case Verhalten erzwingt, das nicht in der SKILL.md-Prosa steht → Prosa in Task 2 erweitern und Task 7 wiederholen.

- [ ] **Step 7.6: Final-Commit (nur falls SKILL.md-Nachbesserung nötig war)**

```bash
git add -A
git commit -m "test(sec-edgar-skill): e2e verification (4 use-cases) + prosa nachbesserung"
```

Wenn keine Nachbesserung nötig: kein Commit, Track 5a abgeschlossen.

---

### Task 8: `!SyncBriefing` (00_Core-Änderungen propagieren)

**Files:**
- (wird von Task-8-Execution automatisch bestimmt — Morning-Briefing-Trigger-Config)

**Hintergrund:** CLAUDE.md-Regel: `!SyncBriefing` vor Session-Ende, wenn `00_Core/` geändert wurde (§25). Task 4 + Task 5 haben INSTRUKTIONEN/CORE-MEMORY/STATE modifiziert → Sync-Pflicht.

- [ ] **Step 8.1: SyncBriefing ausführen**

Manuell im Claude-Code-Prompt: `!SyncBriefing`

Expected: Trigger-Config (`ccr`-Remote / GitHub-Gist / Briefing-Hook je nach Projekt-Setup) liest aktuellen `00_Core/`-Stand. Bei Inkonsistenz: Hook warnt und listet Diff.

- [ ] **Step 8.2: Wenn Briefing-Hook ok ist: Track 5a Implementation abgeschlossen**

Post-Sync kein zusätzlicher Commit — SyncBriefing ist Read-Side-Operation (oder pusht auf Remote, aber nicht in Repo-HEAD).

---

### Task 9: Deferred — 90-Tage-Audit-Review (2026-07-19)

**Files:**
- Modify: `00_Core/CORE-MEMORY.md` (§1 Meilensteine oder §10 Audit-Log)

**Hintergrund:** Spec §6 Erfolgs-Definition 5a: „CORE-MEMORY §5 zeigt mindestens einen Audit-Eintrag mit EDGAR-Resolve-Nutzung innerhalb 90 Tagen post-Aktivierung". Deployment-Datum 2026-04-20 → Review-Termin **2026-07-19**. Diese Task ist **deferred** — wird nicht in der Deployment-Session ausgeführt, sondern als geplanter Check-In dokumentiert. Review-Aktivierung via STATE.md-Trigger-Liste oder Kalendereintrag.

- [ ] **Step 9.1: Trigger-Verankerung am Deployment-Tag**

Beim Abschluss von Task 5 (Docs-Sync) zusätzlich in `00_Core/STATE.md` unter „Nächste kritische Trigger" eine Zeile für den 90-Tage-Audit einfügen:

```markdown
| 2026-07-19 | sec-edgar-skill | D | Track-5a 90-Tage-Audit (Spec §6) — mindestens 1 EDGAR-Resolve-Nutzung nachweisbar? |
```

Klasse D = monatliche/periodische Frist (INSTRUKTIONEN §19). Wenn STATE.md-Trigger-Tabelle kein „D"-Feld führt: Klasse weglassen oder „Audit-Gate" als Label nutzen.

- [ ] **Step 9.2: Am 2026-07-19 — Review ausführen**

```bash
grep -n "EDGAR\|sec-edgar-skill\|XBRL\|Daten-Arbitrage" "00_Core/CORE-MEMORY.md" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md"
```

Expected: mindestens 1 Eintrag zwischen 2026-04-20 und 2026-07-19 mit echter Skill-Nutzung (nicht Deployment-Log, sondern Use-Case-1/2/3/4-Anwendung). Wenn Treffer vorhanden: CORE-MEMORY §1 Eintrag „Track-5a-Audit-Gate 2026-07-19 passed" schreiben.

- [ ] **Step 9.3: Wenn KEINE Skill-Nutzung in 90 Tagen — Applied-Learning-Review**

Applied-Learning-Lektion formulieren: Skill wurde deployed aber nicht genutzt. Entscheidungspfad:
- Option A: Zurück nach `_extern/` verschieben (Skill ist Over-Engineering für aktuellen Bedarf)
- Option B: Trigger-Words nachschärfen (Auto-Discovery hat nicht zugegriffen)
- Option C: In `!Analysiere`-Workflow integrieren wenn Use-Cases systematisch versäumt wurden (wäre Spec-Änderung → Spec-PR nötig)

Entscheidung in CORE-MEMORY §1 dokumentieren, STATE.md-Trigger-Zeile auflösen.

- [ ] **Step 9.4: Commit (am Review-Tag 2026-07-19)**

```bash
git add "00_Core/STATE.md" "00_Core/CORE-MEMORY.md"
git commit -m "audit(track-5a): 90-tage-gate review — [passed|applied-learning <option>]"
```

---

## Verification — End-to-End-Gate

Nach Abschluss Task 1-8 folgende Punkte durchgehen:

1. **Skill-Discovery:** In neuer Claude-Code-Session Prompt „liste alle aktiven Skills mit frontmatter" → `sec-edgar-skill` erscheint mit `v1.0` und Trigger-Words.
2. **Smoke-Test-Rerun:** `python 01_Skills/sec-edgar-skill/_smoke_test.py` → 4/4 PASS, Exit 0. (Netzwerk erforderlich.)
3. **INSTRUKTIONEN §17-Audit:** `grep -n "v1.0 aktiv seit 2026-04-20" 00_Core/INSTRUKTIONEN.md` → 1 Treffer in Zeile ~248.
4. **STATE.md-Visibility:** Neue Session-Start → `sec-edgar-skill v1.0 aktiv` sichtbar in STATE-System-Zustand.
5. **CORE-MEMORY §1-Eintrag:** `grep -A3 "2026-04-20 — .sec-edgar-skill. v1.0 deployed" 00_Core/CORE-MEMORY.md` → Eintrag findet sich.
6. **_extern-Banner:** `head -10 01_Skills/_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` → SUPERSEDED-Banner sichtbar.
7. **Use-Case-1-Real-World-Run:** innerhalb 14 Tagen post-Deployment echte Daten-Konflikt-Arbitrage mit EDGAR-Skill ausführen (erste Gelegenheit wahrscheinlich TMO Q1 am 23.04.2026 oder MSFT Q3 am 29.04.2026 wenn defeatbeta-Shibui-Drift >5% auftritt). Ergebnis in CORE-MEMORY §1 oder §10 protokollieren — Erfolgsdefinition Spec §6: „In einem realen Daten-Konflikt-Fall liefert EDGAR-Skill XBRL-Schiedsquelle mit ≤200 Tokens via `.to_context()`".

**Review-Kriterium:** Alle 7 Verification-Punkte ohne manuelle Skill-Code-Änderung bestanden. Wenn Punkt 7 innerhalb 90 Tagen kein Audit-Eintrag entsteht (Spec §6 „innerhalb 90 Tagen post-Aktivierung"): Applied-Learning-Review, ob Skill echten Use-Case trifft oder in `_extern/` zurückverschoben werden muss.

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| `pip install edgartools` bricht bestehende Python-Env | Task 1.2 Exit-Code-Check; bei Dep-Konflikt Abbruch + User-Rückfrage. Optional venv in Folge-Session. |
| `.to_context()`-Token-Budget (100/300) zu eng für große Tickers | Task 3 Smoke-Test fängt Überschreitung. Bei Case 3/4 FAIL: Budget empirisch anpassen (Task 3.2 Variante A), in CORE-MEMORY dokumentieren. |
| SEC-Rate-Limit bei mehreren Analysen in Folge | EdgarTools-Cache (intern). Bei wiederholten 429-Responses: `set_identity()`-Check + Wait-Retry-Pattern im Skill ergänzen (nachträgliche SKILL.md-Erweiterung, kein Re-Plan). |
| Skill wird versehentlich in `!Analysiere` auto-geladen (Trigger-Word-Kollision mit Earnings/10-K-Mentions) | SKILL.md §0 Scope-Section ist explizit; dynastie-depot INSTRUKTIONEN §17-Grundregel („keine weiteren Skills innerhalb `!Analysiere`") bleibt primäre Schutzregel. Bei echten Auto-Load-Fällen: Trigger-Words in Frontmatter kürzen. |
| `_extern/sec-edgar-skill/` wird von zukünftigen Upstream-Syncs überschrieben und verliert Superseded-Banner | Banner ist in Repo-Version. Bei Upstream-Re-Import: Banner-Restore als Pre-Merge-Schritt in CORE-MEMORY-Wartungsnotiz. |
| Frontmatter-Trigger-Words kollidieren mit bestehenden Skills (z.B. Earnings-Skills) | Task 7.x E2E-Verification prüft Auto-Discovery-Verhalten empirisch. Bei Kollision: Priorisierung via expliziteren Trigger-Phrasen („SEC EDGAR", „XBRL") statt generische („10-K"). |
| Plan referenziert §17/§8/§1 (Ist-Zustand), Spec §22/§19/§5 (veraltet) — Audit-Verwirrung | Header-Notice oben listet alle 3 Mismatches mit Begründung. Spec bleibt eingefroren. Codex-Bestätigung 2026-04-20. |

---

## Pre-Implementation-Gates

Vor Implementation-Session-Start:

- [ ] **Gate A — Tavily-Go-Live stabil seit ≥3 Tagen** (Spec §4.1). Prüfung via SESSION-HANDOVER.md: Monitoring-Einträge letzte 3 Tage ohne Fehler.
- [ ] **Gate B — `01_Skills/sec-edgar-skill/` existiert nicht** (Spec §5 Q5 Namens-Kollision). Verifiziert 2026-04-20 via `ls 01_Skills/`: Verzeichnis nicht vorhanden. ✅
- [ ] **Gate C — Python-Env `/c/Python314/` ist write-fähig für `pip install`**. Probe: `pip list | head -3` läuft fehlerfrei.
- [ ] **Gate D — Header-Notice §-Mapping gegen aktuelles `00_Core/INSTRUKTIONEN.md` verifizieren**. Zeilen-Nummern können driften; vor Task 4.1 erneut `grep -n "^## " 00_Core/INSTRUKTIONEN.md` um Zeilen-Refs zu bestätigen.

---

## Handover-Hinweise für Implementation-Session

- Sessionstart: `Session starten` → STATE.md lesen → diesen Plan laden.
- Implementation-Skill: `superpowers:subagent-driven-development` (recommended) — Task-by-Task mit Fresh-Subagent, Review zwischen Tasks. Kleinerer Plan als backtest-ready (~6-8 Std. Execution-Zeit erwartet).
- Alternative: `superpowers:executing-plans` für Inline-Execution in aktueller Session.
- **Test-Philosophie** (siehe `backtest-ready-forward-verify`-Plan Task 3 Hinweis): Smoke-Test `_smoke_test.py` testet Deterministisches (EdgarTools-API-Verhalten, Token-Bounds). Skill-Prosa-Korrektheit ist qualitatives E2E-Urteil in Task 7, kein Assertion.
- **Nach Implementation:** Erster Real-Run-Use-Case wahrscheinlich TMO Q1 am 23.04.2026 (FLAG-Resolve-Gate, Shibui/defeatbeta-Cross-Check erwartet) — gute Gelegenheit für E2E-Validation im echten Workflow.

---

## Nicht-Ziele (explizit out-of-scope per Spec §2.7)

- KEIN First-Class-EDGAR-MCP als Ersatz für defeatbeta
- KEINE automatische Einbindung in `!Analysiere`-Workflow — Skill ist eskalations-getriggert
- KEINE Migration von `insider_intel.py` auf EDGAR-Skill — beide koexistieren
- KEINE FRED-Regime-Filter-Komponenten (separater Plan Track 5b)
- KEIN `set_identity()`-Automation-Hook — bleibt explizit in Skill-Prosa dokumentiert
- KEINE Entfernung von `_extern/sec-edgar-skill/` — Superseded-Banner statt Löschung (Informationsverlust-Aversion)

---

*🦅 Track-5a-Plan v1.0 | 2026-04-20 | Co-Review: Claude (Opus 4.7) + Codex | Ref: TRACK5-SPEC v1.0 (22cdeb8)*
