# System-Audit-Tool — Design Spec

**Datum:** 2026-04-21 (Nachmittag)
**Status:** draft (Spec-Review pending — User + Codex parallel)
**Scope-ID:** B1 (internes Drift-Audit-Tool, intern gebaut statt codebase-memory-mcp)
**Nachfolge-Artefakt:** Implementation-Plan `docs/superpowers/plans/2026-04-21-system-audit-tool.md` (Phase E dieser Session-Sequenz)

---

## 1. Kontext

### 1.1 Auslöser

**Drift-Incident 21.04.2026 Mittag:** Ein Pre-Check vor Execution des Provenance-Gate-Plans deckte auf, dass 12 von 27 Records in `05_Archiv/score_history.jsonl` silent schema-inkonsistent waren — alle `defcon_level`-Drift seit der 18.04.-SKILL-Threshold-Migration (80/65/50 statt 70/60/50). Spot-Check über STATE.md-Snapshot hatte die Drift nicht gesehen; nur exhaustive Record-Validation fand sie.

Der Incident bewies zwei Dinge:
1. **„Drift-Check" war bisher implizit Spot-Check** (Sampling prominenter Zeilen). Die Systemgröße hat die Grenze eines manuellen Audit-Prozesses überschritten.
2. **Schema-Migrationen ticken vorwärts, Altdaten bleiben silent stale.** Jede spätere Validator-Ausführung wird toxisch verzerrt (Incident-Spiegel: Drift-Migration-Tool entdeckte, was der ursprüngliche Backfill-Run nicht geprüft hatte).

### 1.2 Warum intern gebaut, nicht extern (Verwerfungs-Narrativ)

Parallel zum Drift-Incident evaluierte User das externe Tool `github.com/DeusData/codebase-memory-mcp`. Verwerfung begründet aus 3 Gründen:
1. **Scope-Mismatch:** Tool indexiert Code-ASTs (Python/TS/JS-Symbole). Unsere Drift ist in Markdown/YAML/JSONL — genau den Formaten, die das Tool nicht versteht.
2. **Drift-Ironie:** Externer SQLite-Cache wäre neue Drift-Quelle. Ein Audit-Tool, dessen Index selbst driften kann, ist kein Audit-Tool.
3. **Install-Friction:** Windows-SmartScreen-Install, fremder Update-Zyklus, kein Nutzer-Mandat-Fit.

Ein ~300 LOC Python-Skript adressiert unser Drift-Problem direkter + ohne externe Drift-Fläche.

### 1.3 Belegte Drift-Klassen im Projekt

| Klasse | Beispiel (belegt) | Detection-Pfad |
|---|---|---|
| **Vertikal-Drift** (Schema-Migration auf Altdaten) | 21.04.: 12/27 defcon-Drift post-18.04.-Threshold-Shift | JSONL Schema-Re-Validate |
| **Horizontal-Drift** (Multi-Source-Divergenz) | Hypothetisch: STATE.md ≠ Faktortabelle ≠ config.yaml | Cross-Source-Diff |
| **Header-Stand-Drift** | 21.04. CORE-MEMORY stand 4 Tage hinter Realität | Markdown-Header-Parse vs §1-neuester-Eintrag |
| **Existenz-Drift** | Referenz auf nicht-existierendes `03_Tools/x.py` | Path-Existence-Check |
| **Skill-Version-Drift** | SKILL.md-Frontmatter `v3.7.2` vs ZIP `v3.7.1` | Frontmatter vs Dateiname |
| **Pipeline-SSoT-Drift** (neu 21.04.) | Plan-File existiert, aber nicht in STATE.md-Pipeline-Section | Bidirectional Plan↔STATE-Check |
| **Log-Lag** | log.md letzter Eintrag >1 Tag hinter git HEAD | log.md-Tail-Date vs `git log -1` |

---

## 2. Goal

Ein deterministischer, reproduzierbarer Exhaustive-Drift-Audit, der in <30s läuft und ein `N/M PASS` + Kategorie-FAIL-Bericht produziert. Invokabel via CLI + Slash-Command. Schreibt STATE.md-Section „Last Audit" idempotent selbst. Exit-Codes discriminieren PASS vs Drift-FAIL vs IO-Fehler (CI-ready).

---

## 3. Non-Goals

- **Auto-Fix:** Tool detektiert, fixt nicht. Migration bleibt spezialisierten Tools (`migrate_defcon_drift.py` etc.) vorbehalten.
- **Code-AST-Index:** Python/Markdown-Parsing für Drift reicht; kein tree-sitter / LSP / RAG.
- **Continuous-Monitoring:** Kein Daemon, kein Cron — Audit ist On-Demand (via Slash-Command oder Pre-Plan-Execution-Check).
- **SessionStart-Hook:** Kollidiert mit CLAUDE.md SESSION-INITIALISIERUNG „zuerst nur STATE.md lesen". Codex-bestätigt als Anti-Pattern.
- **Pre-Commit-Hook (Default):** Friction-Risiko. Bleibt optional als opt-in in einer späteren Erweiterung.
- **Vollständige Vault-Link-Graph-Validation:** Zu langsam (130+ Notes). Optional-Subcommand mit Timeout.
- **External API-Validation:** Keine Shibui/defeatbeta/Yahoo-Queries im Audit-Tool — pure File-System-Checks (reproduzierbar, offline-fähig).

---

## 4. Architektur

### 4.1 Top-Level-Modul-Struktur

```
03_Tools/
  system_audit.py          ← Entry-Point (CLI + Orchestrator)
  system_audit/
    __init__.py
    checks/
      __init__.py
      jsonl_schema.py      ← Check-1: Pydantic-Revalidation
      markdown_header.py   ← Check-2: Header-Stand-Drift
      cross_source.py      ← Check-3: STATE↔Faktortabelle↔config↔Vault
      existence.py         ← Check-4: Path-Existence
      skill_version.py     ← Check-5: SKILL.md vs ZIP
      pipeline_ssot.py     ← Check-6: Plans ↔ STATE.md Pipeline-Section
      log_lag.py           ← Check-7: log.md vs git HEAD
      vault_backlinks.py   ← Optional: Wiki-Link-Integrity
      status_matrix.py     ← Optional: B-Nummerierung Sanity
    report.py              ← Structured Output (human + --json)
    state_writer.py        ← Idempotent „Last Audit"-Line in STATE.md
    fixtures/              ← Test-Fixtures (valid + drift-seeded)
```

### 4.2 Daten-Flow

```
CLI args
  │
  ▼
┌───────────────────────────────────┐
│ Orchestrator (system_audit.py)    │
│  - parse --core | --full | --vault│
│  - collect check-registry         │
│  - dispatch (sync, with timeouts) │
└─────────────────┬─────────────────┘
                  │
                  ▼
          ┌───────────────┐
          │ Check-Results │ (N PASS / M FAIL / category / details)
          └───────┬───────┘
                  ▼
          ┌───────────────┐
          │   report.py   │ ← human (default) | --json
          └───────┬───────┘
                  ▼
      ┌──────────────────────────┐
      │ state_writer.py          │
      │  - wenn --write (default)│
      │  - update `## Last Audit"│
      │  - idempotent (replace)  │
      └─────────────┬────────────┘
                    ▼
              Exit-Code
              0: all PASS
              1: ≥1 FAIL
              2: IO/Parse-Error (Tool-intern)
```

### 4.3 Check-Registry-Contract

Jeder Check exportiert eine Funktion mit identischer Signatur:

```python
def run(repo_root: Path, context: AuditContext) -> CheckResult:
    """Execute this check. Return structured result."""
```

Mit:

```python
@dataclass
class CheckResult:
    name: str                 # e.g. "jsonl_schema"
    status: Literal["PASS", "FAIL", "SKIP"]
    n_checked: int
    n_passed: int
    failures: list[FailureDetail]  # empty if status == PASS
    duration_ms: int
    category: Literal["core", "optional"]

@dataclass
class FailureDetail:
    location: str             # file:line or file:record_id
    expected: str             # human-readable what-should-be
    actual: str               # human-readable what-is
    severity: Literal["error", "warning"]  # warning = non-blocking für Exit-Code
    hint: str | None          # suggested remediation (z.B. „run migrate_defcon_drift.py")
```

Dieser Contract ermöglicht: Report-Aggregation uniform, Test-Fixtures uniform, neuer Check = neue Datei + Registry-Eintrag (keine Refactorings am Orchestrator).

---

## 5. Check-Catalogue

### 5.1 Kern (Pflicht, --core Default)

#### Check-1: JSONL Schema-Validation

**Zweck:** Vertikal-Drift-Detection (Präzedenzfall 21.04. 12/27).

**Stores:**
- `05_Archiv/score_history.jsonl` → `schemas.ScoreRecord.model_validate(line)`
- `05_Archiv/flag_events.jsonl` → `schemas.FlagEvent.model_validate(line)`
- `05_Archiv/portfolio_returns.jsonl` → `PortfolioReturnRecord.model_validate(line)` (Schema neu einzuführen — derzeit nur Daily-Schema v1.0 als Docstring in `portfolio_risk.py`)
- `05_Archiv/benchmark-series.jsonl` → `BenchmarkReturnRecord.model_validate(line)` (analog)

**Fail-Mode:**
- Pydantic `ValidationError` pro Zeile → 1 `FailureDetail` mit `location=file:lineno`, `expected=field-error-message`, `hint="re-run backfill oder migration-tool"`.
- Leere Datei: SKIP (nicht FAIL), Warnung im Report.

**Soft-Coupling:** Wenn Pydantic-Modelle für portfolio_returns / benchmark-series noch nicht existieren — **Check-1.3 und Check-1.4 laufen als SKIP mit Warnung**, bis Plan eine Migration nachholt. Verhindert false-negatives durch fehlendes Schema.

#### Check-2: Markdown Header-Stand-Drift

**Zweck:** Dokumentations-Aktualität (21.04. CORE-MEMORY 4 Tage stale).

**Targets:**
- `00_Core/STATE.md` → Header-Zeile Regex `\*\*Stand:\*\*\s*([0-9]{2}\.[0-9]{2}\.[0-9]{4})` vs. jüngste Portfolio-State-Zeile-Implied-Date (aus Commit-Author-Date oder log.md-Tail — whichever ist jünger).
- `00_Core/CORE-MEMORY.md` → `**Stand:**` vs. letzter §1 Tabellen-Eintrag-Datum.
- `00_Core/Faktortabelle.md` → `**Stand:**` vs. jüngstes `Score-Datum`-Feld in Haupttabelle.

**Threshold:** `stand - neueste_event_date > 2 Werktage` → FAIL. (Wochenenden nicht gezählt.)

**Fail-Mode:** 1 FailureDetail pro Datei mit Hint „Header-Zeile aktualisieren".

**Edge-Case:** Wenn kein Parse-Match → FAIL mit „Regex matched 0 Zeilen, Datei-Struktur geändert?"

#### Check-3: Cross-Source Score/DEFCON/Sparrate

**Zweck:** Horizontal-Drift (mehrere SSoTs dürfen sich nicht widersprechen).

**Authoritative Source:** `dynastie-depot/config.yaml` Satelliten-Block (per INSTRUKTIONEN §18).

**Mirror-Sources (müssen mit config.yaml matchen):**
- `00_Core/STATE.md` Portfolio-Tabelle (Ticker | Score | DEFCON | Rate | FLAG).
- `00_Core/Faktortabelle.md` Haupttabelle (Score + DEFCON + FLAG).
- Obsidian-Vault Satellite-Entities (`07_Obsidian Vault/.../entities/<Ticker>.md` Frontmatter `score:` / `defcon:` / `flag:` falls vorhanden).

**Parsing-Strategie:**
- config.yaml: `yaml.safe_load`, iteriere `satelliten`.
- STATE.md: Markdown-Tabelle parse (pipe-split, Header-Match „Ticker | Score | DEFCON | Rate | FLAG").
- Faktortabelle.md: Markdown-Tabelle parse (Header „Position | ... | Score | DEFCON | FLAG | Score-Datum").
- Vault-Entities: Frontmatter (YAML-Block zwischen `---`) parse, nur Felder `score` / `defcon`.

**Fail-Mode:** Pro Ticker eine FailureDetail mit Form `AVGO: config.yaml=84/D4 vs STATE.md=85/D4`.

**Edge-Case:** FLAG-Semantic-Divergence (z.B. config.yaml `flag: false`, STATE.md `🔴 Score-basiert`) — Mapping-Table definieren: `flag:true ↔ 🔴`, `flag:false ↔ ✅|⚠️`, `⚠️` = Warning nicht FAIL.

#### Check-4: Existence-Check (Pfad-Referenzen)

**Zweck:** Verhindert, dass Pläne/Handover auf nicht-existierende Dateien verweisen.

**Scan-Quellen:**
- `CLAUDE.md` (project + user's auto-memory MEMORY.md referenzierte Pfade).
- `00_Core/STATE.md` (alle backtick-wrapped Pfade `\`03_Tools/x.py\``).
- `00_Core/SESSION-HANDOVER.md` (analog).
- `docs/superpowers/plans/*.md` (falls in STATE.md Pipeline-SSoT-Section referenziert).

**Extraction:** Regex ``([^\s`]+\.(py|md|yaml|yml|jsonl|xlsx|zip))``; ignoriere URLs (http*), Wikilinks (`[[...]]`) und Code-Fences.

**Whitelist:** `.gitignore`-Pattern + bekannte Runtime-generated-Paths (z.B. `_drafts/`).

**Fail-Mode:** Pro fehlender Pfad eine FailureDetail mit Hint „Pfad wurde umbenannt/gelöscht? Referenz aktualisieren".

#### Check-5: Skill-Version

**Zweck:** Skill-ZIP-Name-vs-SKILL-Frontmatter-Konsistenz.

**Targets:**
- Alle `01_Skills/<skill>/SKILL.md` mit YAML-Frontmatter-Feld `version:`.
- Korrespondierende `06_Skills-Pakete/<skill>_v<X.Y.Z>.zip`-Dateinamen.

**Regel:** ZIP-Name enthält höchste Version == SKILL.md-Frontmatter-Version. Ältere ZIPs erlaubt (Versions-Historie). Neuere SKILL.md-Version ohne ZIP = WARNING (noch nicht gepackt).

**Fail-Mode:** Pro Skill FailureDetail falls SKILL.md höhere Version als alle ZIPs hat (neuer Code noch nicht released), oder ZIP ohne Parent-SKILL.md existiert (orphan).

**Edge-Case:** `_extern/*` Skills ohne Frontmatter `version:` — SKIP mit Log.

#### Check-6: Pipeline-SSoT-Consistency

**Zweck:** STATE.md-Pipeline-Section muss mit `docs/superpowers/plans/` bidirectional aligned sein.

**Reality-Check:** `docs/superpowers/plans/` enthält heute 11 Plan-Files, davon 6 abgeschlossen/superseded (Apr 15-19) und 5 aktive (Apr 20-21). Ohne formale Status-Labels im Plan-Frontmatter würde eine bidirektionale Prüfung 6 FAIL-Noise produzieren.

**MVP-Scope (Check-6.1 Reverse-Only):**
- **Reverse:** Jede Plan-Referenz in STATE.md-Pipeline-SSoT-Section (Backtick-Pfad im Format `docs/superpowers/plans/YYYY-MM-DD-*.md`) muss einem existierenden Plan-File entsprechen. FAIL wenn Referenz ins Leere zeigt.

**Future-Scope (Check-6.2 Forward, nach Status-Label-Nachrüstung):**
- **Forward:** Jedes Plan-File mit Frontmatter `status: ready|in-progress|deferred` muss in STATE.md-Pipeline-SSoT-Section referenziert sein. Plans mit `status: executed|superseded|deprecated` werden ignoriert.
- **Kategorie-Check:** Plan mit `status: deferred` → muss in STATE.md-Kategorie 🔵 auftauchen; `status: ready` → 🔴/🟡; `in-progress` → 🔴.

**Parser:** STATE.md-Pipeline-Section isolieren durch Regex `## 🗺 Aktive Pipeline` bis nächste `^## ` oder `^---$`; extrahiere alle `docs/superpowers/plans/...` Pfade.

**Fail-Mode (MVP):** Pro broken Reverse-Referenz eine FailureDetail mit `location=STATE.md:N`, `actual="docs/superpowers/plans/X.md existiert nicht"`.

**Plan-Status-Nachrüstung:** Nicht im Scope dieser Spec. Als separater, nicht-blockierender Follow-up-Plan dokumentiert (siehe §10.5). Bis dahin läuft Check-6 Reverse-Only.

#### Check-7: log.md-vs-Git-HEAD-Lag

**Zweck:** Vault-log.md muss rezente Commits reflektieren (INSTRUKTIONEN §18 Position 1).

**Regel:** `log.md`-letztes-Datum (Regex `^## \[([0-9]{4}-[0-9]{2}-[0-9]{2})\]`) >= `git log -1 --pretty=%cd`-Datum - 1 Werktag.

**Threshold:** `git-HEAD-Date - log.md-Last-Date > 1 Werktag` → FAIL.

**Fail-Mode:** „log.md letzter Eintrag YYYY-MM-DD, git HEAD YYYY-MM-DD (Lag N Tage). Sync-Pflicht §18 Position 1 verletzt."

**Edge-Case:** Wenn letzter Commit nur docs/CI/non-code ist, trotzdem FAIL — Sync-Pflicht ist absolut.

### 5.2 Optional (--full aktiviert, --vault separat)

#### Check-8: Vault-Backlink-Integrity

**Zweck:** Obsidian-Wikilinks `[[Seitenname]]` müssen auf existierende Notes zeigen.

**Scope:** Alle `.md` in `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/` ausser `raw/`.

**Timeout:** 20s. Bei Überschreitung → SKIP mit Warnung, kein FAIL.

**Fail-Mode:** Pro broken Link FailureDetail mit `location=file:line`, `actual="[[Missing]]"`.

#### Check-9: Status-Matrix B-Nummerierung

**Zweck:** Wissenschaftliche-Fundierung-DEFCON.md Status-Matrix muss konsistente B1-BN-Nummerierung haben (keine Lücken, keine Duplikate).

**Target:** `07_Obsidian Vault/.../synthesis/Wissenschaftliche-Fundierung-DEFCON.md` Status-Matrix-Section.

**Regel:** Extrahiere alle `B\d+`-Labels, prüfe Monoton-Steigend + Kein-Duplikat.

**Fail-Mode:** „B17 fehlt zwischen B16 und B18" / „B22 erscheint 2× in Matrix".

---

## 6. Invocation & Output

### 6.1 CLI

```bash
# Default: Kern-Checks, human-Output, schreibt STATE.md Last-Audit
python 03_Tools/system_audit.py

# Core only (explicit)
python 03_Tools/system_audit.py --core

# Core + Optional (Vault + Status-Matrix, mit Timeouts)
python 03_Tools/system_audit.py --full

# Only Vault-Optional (für schnellen Vault-Check ohne Core)
python 03_Tools/system_audit.py --vault

# Dry-run (kein STATE.md-Write)
python 03_Tools/system_audit.py --no-write

# JSON-Output (CI-ready)
python 03_Tools/system_audit.py --json

# Verbose (zeigt jede Check-Duration)
python 03_Tools/system_audit.py -v
```

### 6.2 Slash-Command

Datei `.claude/commands/SystemAudit.md`:

```markdown
---
description: Run systemweiten Drift-Audit via 03_Tools/system_audit.py
---

Run the following command and report the N/M PASS result to the user:

```bash
python 03_Tools/system_audit.py $ARGUMENTS
```

If FAIL → list each category with count + first 3 FailureDetails per category.
If PASS → show the one-line summary + Last-Audit-Timestamp.
```

### 6.3 Human-Output-Format

```
🔍 System-Audit — 2026-04-21 14:32 UTC

Check-1  jsonl_schema        ✅ PASS  27/27   (score_history) + 2/2 (flag_events)   |  128ms
Check-2  markdown_header     ✅ PASS  3/3                                           |   42ms
Check-3  cross_source        ❌ FAIL  10/11  →  1 Ticker divergent                  |   91ms
         • AVGO: config.yaml=84/D4 vs STATE.md=85/D4
         • Hint: STATE.md-Zeile aktualisieren, config.yaml ist Wahrheitsquelle
Check-4  existence           ✅ PASS  47/47                                         |   64ms
Check-5  skill_version       ✅ PASS  5/5                                           |   22ms
Check-6  pipeline_ssot       ✅ PASS  11/11                                         |   38ms
Check-7  log_lag             ✅ PASS  log.md 2026-04-21, HEAD 2026-04-21            |   11ms

Summary: 6/7 PASS, 1 FAIL (cross_source)
Duration: 396ms
Exit-Code: 1
```

### 6.4 JSON-Output-Format

```json
{
  "audit_timestamp_utc": "2026-04-21T14:32:41Z",
  "summary": {"total": 7, "passed": 6, "failed": 1, "skipped": 0},
  "exit_code": 1,
  "duration_ms": 396,
  "checks": [
    {"name": "jsonl_schema", "status": "PASS", "n_checked": 29, "n_passed": 29, "failures": [], "duration_ms": 128, "category": "core"},
    {"name": "cross_source", "status": "FAIL", "n_checked": 11, "n_passed": 10, "failures": [
      {"location": "00_Core/STATE.md:18", "expected": "AVGO Score=84", "actual": "Score=85", "severity": "error", "hint": "STATE.md-Zeile aktualisieren"}
    ], "duration_ms": 91, "category": "core"}
  ]
}
```

### 6.5 STATE.md „Last Audit"-Section (idempotent)

Tool fügt (oder ersetzt) am Ende von STATE.md unmittelbar vor dem `*🦅 STATE.md v1.0 ...` Footer:

```markdown
---

## 🔍 Last Audit

**Timestamp (UTC):** 2026-04-21T14:32:41Z
**Result:** 6/7 PASS (1 FAIL: cross_source)
**Run:** `python 03_Tools/system_audit.py --core`
**Full-Report:** stdout (kein Archiv-File)
```

**Idempotenz:** Bei wiederholtem Run → ersetzt bestehenden Block (Marker-Regex `## 🔍 Last Audit` bis nächste `^## ` oder `^---`).

**Opt-Out:** `--no-write` Flag überspringt State-Update.

---

## 7. Testing Strategy

### 7.1 Unit-Tests pro Check

Jeder Check hat `test_<check>.py` mit mindestens 3 Fixtures:
- **PASS-Fixture:** Gesunder Stand, erwartet 0 FailureDetails.
- **FAIL-Fixture:** Bewusst drift-seeded, erwartet ≥1 FailureDetail mit exakter Location.
- **EDGE-Fixture:** Missing-File / Empty-File / Parse-Error → SKIP oder Exit-Code 2.

### 7.2 Integration-Test

`test_integration.py`:
- **Baseline-Run:** Aktueller Repo-Stand → erwartet PASS auf allen Kern-Checks.
- **Seeded-Drift-Run:** Temporäres Repo-Copy mit injizierter Drift (z.B. defcon_level=4 bei Score 70 in `score_history.jsonl`) → erwartet FAIL auf Check-1.

### 7.3 Smoke-Test

`smoke_test.sh`: Lauf gegen aktuellen Repo, erwartet `exit 0` + „Last Audit"-Zeile in STATE.md geschrieben.

### 7.4 Regression-Guard

Nach jedem `migrate_*.py` muss `system_audit.py --core` PASS zeigen — explizite Regel in INSTRUKTIONEN §27.4.

---

## 8. Error Handling

### 8.1 Tool-interne Errors (Exit-Code 2)

| Szenario | Verhalten |
|---|---|
| `FileNotFoundError` auf Repo-Root-Erwartung | Exit 2, Fehler-Message „Nicht im Repo-Root ausgeführt?" |
| Pydantic-Import-Fehler | Exit 2, Fehler-Message „Dependencies fehlen: pip install pydantic" |
| Permission-Denied auf STATE.md-Write | Warning (nicht Exit 2), Report trotzdem auf stdout, Write skipped |
| Unknown Flag / CLI-Syntax | Exit 2, argparse-Fehler |

### 8.2 Check-interne Errors (Status SKIP)

Einzelne Check-Failures (z.B. Parse-Error in einer spezifischen Markdown-Datei) werden als CheckResult mit `status="SKIP"` und `failures=[FailureDetail(severity="warning", ...)]` zurückgegeben. Tool exited nicht; Summary zeigt SKIP-Count.

### 8.3 Concurrent Runs

Kein Lock-File (Tool ist schnell genug, dass parallele Runs unwahrscheinlich sind). State-Write verwendet `atomic_write` (tmp + os.replace) — letzter Write gewinnt, kein Korruptionsrisiko.

---

## 9. Governance

### 9.1 Run-Gelegenheiten (empfohlen)

1. **Vor jedem Plan-Execution-Start** (manueller `/SystemAudit`-Aufruf, analog Provenance-Plan Task 0 Baseline-Check).
2. **Nach jedem `migrate_*.py`-Lauf** (als Post-Migration-Verifikation).
3. **Wöchentlich** ad-hoc (User-Disziplin, kein Automatismus).
4. **Vor größeren Commits** als spontaner Vorcheck.

### 9.2 Nicht-Automatismus-Entscheidung (Codex-bestätigt)

Kein SessionStart-Hook, kein Cron, kein Pre-Commit-Default. User-Agency bleibt zentral.

### 9.3 Pflege-Pattern

- **Neuer Check:** Datei in `03_Tools/system_audit/checks/` + Registry-Eintrag + Unit-Test. Kein Orchestrator-Touch.
- **Schema-Migration:** Nach jedem neuen Schema-Shift `system_audit.py --core` als Regression-Test — muss PASS zeigen, sonst Migration unvollständig.
- **Plan-Lifecycle:** Plan abgeschlossen? Status in STATE.md-Pipeline von 🔴/🟡 nach ✅ oder Archiv. Pipeline-SSoT-Check fängt Drift.

---

## 10. Open Questions (für Spec-Review)

1. **Portfolio-Returns-Schema:** Soll Spec vorschreiben, dass Plan zuerst `PortfolioReturnRecord`-Pydantic-Modell in `schemas.py` hinzufügt (bevor Check-1.3/1.4 aus SKIP-Zustand kommen)? **Vorschlag:** Ja, als Task 1 im Plan. Alternative: Als Future-Work separat planen.

2. **Vault-Backlinks Timeout:** 20s wie spezifiziert, oder flexibler (env-var `SYSTEM_AUDIT_VAULT_TIMEOUT`)? **Vorschlag:** Start-hardcoded 20s, später flexibilisieren falls echte Vault-Größe Problem macht.

3. **Status-Matrix-Check:** Gehört in Kern oder Optional? **Vorschlag:** Optional, weil Status-Matrix inhaltlich weniger kritisch als JSONL-Drift ist — wenn B-Nummerierung driftet, ist das eine Doku-Inkonsistenz, kein Scoring-Risk.

4. **STATE.md-Last-Audit-Update bei FAIL:** Soll die Last-Audit-Zeile auch bei FAIL geschrieben werden? **Vorschlag:** Ja (Transparenz > Cosmetics) — Zeile zeigt dann „❌ 6/7 PASS, 1 FAIL". Alternative: Nur bei PASS schreiben (dann weiß man, dass letzte grüne Audit-Zeit älter ist als hier behauptet).

5. **Check-6 Plan-Status-Label:** MVP läuft Reverse-Only (Spec-§5.1 Check-6 reflektiert das). Status-Label-Nachrüstung für alle 11 bestehenden Pläne + Forward-Direction als separater Follow-up-Plan — wahrscheinlich ~45 Min Edit-Aufwand (11 Dateien × Frontmatter-Addition) + Check-6.2-Implementation. **Vorschlag:** Follow-up nicht in dieser Phase-E-Plan, sondern in einer späteren Session nach Phase-G-Abschluss (keine Blockade für TMO Q1).

6. **Pydantic-Models-Location:** Neue Models (PortfolioReturnRecord, BenchmarkReturnRecord) nach `03_Tools/backtest-ready/schemas.py` (bestehender Hub) oder separate Datei? **Vorschlag:** schemas.py (bestehender Hub, INSTRUKTIONEN §18 referenziert dort).

7. **CI-Integration:** Exit-Code 1 bei FAIL ist CI-ready — aber gibt es aktuell keinen CI-Runner. Soll Plan GitHub-Actions-Workflow als Task 10/11 nachziehen? **Vorschlag:** Nein (YAGNI), erst wenn GitHub-Actions tatsächlich genutzt werden. Exit-Code bleibt.

---

## 11. Referenzen

- **Drift-Incident-Quelle:** `00_Core/CORE-MEMORY.md` §1 2026-04-21-Mittag-Eintrag + §10 Drift-Audit-Sweep.
- **§27.4 Vertikal-Drift-Klausel:** `00_Core/INSTRUKTIONEN.md`.
- **Existing Pydantic-Hub:** `03_Tools/backtest-ready/schemas.py`.
- **Pipeline-SSoT-Target:** `00_Core/STATE.md` Section „🗺 Aktive Pipeline (SSoT)" (eingebaut Phase C 21.04. Nachmittag).
- **Tool-Präzedenzfall:** `03_Tools/backtest-ready/migrate_defcon_drift.py` (idempotent, atomar, ~70 LOC) — Zielgröße für `system_audit.py` ~300-400 LOC.
- **Memory:** `feedback_exhaustive_drift_check.md` (Tier 1, 21.04.).

---

## 12. Acceptance-Kriterien (für Implementation-Plan)

- [ ] Tool läuft gegen aktuellen Repo-Stand mit `exit 0` (Baseline).
- [ ] `/SystemAudit` Slash-Command funktional, STATE.md-„Last Audit"-Zeile geschrieben.
- [ ] Alle 7 Kern-Checks implementiert mit ≥ 3 Unit-Test-Fixtures pro Check (PASS / FAIL / EDGE).
- [ ] Integration-Test PASS (Baseline + Seeded-Drift).
- [ ] Exit-Codes 0/1/2 korrekt differenziert (Smoke-Test).
- [ ] INSTRUKTIONEN §27.4 um Regression-Guard-Regel ergänzt („nach jedem migrate_*.py → system_audit.py --core PASS").
- [ ] Optional-Checks (Vault + Status-Matrix) implementiert mit Timeout-Handling.
- [ ] Duration <30s bei --core auf aktuellem Repo-Stand (Performance-Budget).

---

*Spec v0.1 draft | Spec-Review: User + Codex parallel | Nach Approval → Plan-Writing Phase E*
