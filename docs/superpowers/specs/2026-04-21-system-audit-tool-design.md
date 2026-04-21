# System-Audit-Tool — Design Spec

**Datum:** 2026-04-21 (Nachmittag)
**Status:** **v0.2 ratified** (User + Codex Joint-Review 2026-04-21 Nachmittag, alle 7 Open Questions resolved, 6 Patches eingepflegt)
**Scope-ID:** B1 (internes Drift-Audit-Tool, intern gebaut statt codebase-memory-mcp)
**Nachfolge-Artefakt:** Implementation-Plan `docs/superpowers/plans/2026-04-21-system-audit-tool.md` (Phase E dieser Session-Sequenz)

### Review-Chronik

| Runde | Reviewer | Verdict | Action |
|---|---|---|---|
| 1 | Claude Opus 4.7 Self-Review | Minor | Check-6 Forward-Direction verworfen (6/11 Plan-Files würden FAIL-Noise produzieren) → MVP Reverse-Only |
| 2 | Codex + User Joint-Review | YELLOW | 6 Patches + 3 Anmerkungen eingepflegt (v0.1 → v0.2) |

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
    status: Literal["PASS", "WARN", "FAIL", "SKIP"]
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
    severity: Literal["error", "warning"]  # error → FAIL-Contribution; warning → WARN-Contribution
    hint: str | None          # suggested remediation (z.B. „run migrate_defcon_drift.py")
```

**Status-Semantik (Codex-Patch v0.2):**
- `PASS` → alle Checks grün, keine Failures mit `severity="warning"`.
- `WARN` → alle `severity="error"` sauber, aber ≥1 `severity="warning"` vorhanden. **Exit-Code bleibt 0** (warnings sind non-blocking), aber Report zeigt WARN-Status explizit.
- `FAIL` → ≥1 Failure mit `severity="error"`. Exit-Code 1.
- `SKIP` → Check konnte nicht laufen (Missing-Dependency, Missing-File, Timeout). Exit-Code bleibt 0, Summary zeigt SKIP-Count.

**Aggregations-Regel:** Tool-Exit-Code = 0 wenn kein Check `status="FAIL"` hat. WARN + SKIP beide exit 0. Nur FAIL → exit 1. IO/Parse-Tool-Error → exit 2.

Dieser Contract ermöglicht: Report-Aggregation uniform, Test-Fixtures uniform, neuer Check = neue Datei + Registry-Eintrag (keine Refactorings am Orchestrator).

---

## 5. Check-Catalogue

### 5.1 Kern (Pflicht, --core Default)

#### Check-1: JSONL Schema-Validation

**Zweck:** Vertikal-Drift-Detection (Präzedenzfall 21.04. 12/27).

**Stores:**
- `05_Archiv/score_history.jsonl` → `schemas.ScoreRecord.model_validate(line)`
- `05_Archiv/flag_events.jsonl` → `schemas.FlagEvent.model_validate(line)`
- `05_Archiv/portfolio_returns.jsonl` → `schemas.PortfolioReturnRecord.model_validate(line)` (**Schema in Plan Task 1 nachzurüsten** — derzeit nur Daily-Schema v1.0 als Docstring in `portfolio_risk.py`)
- `05_Archiv/benchmark-series.jsonl` → `schemas.BenchmarkReturnRecord.model_validate(line)` (analog, Plan Task 1)

**Fail-Mode:**
- Pydantic `ValidationError` pro Zeile → 1 `FailureDetail` mit `severity="error"`, `location=file:lineno`, `expected=field-error-message`, `hint="re-run backfill oder migration-tool"`.
- Missing-File → `status=SKIP` mit `severity="warning"` Notiz „Store nicht vorhanden — Backfill ausstehend?".
- Empty-File → `status=SKIP` mit `severity="warning"` Notiz „Store leer".

**Codex-Patch v0.2 (Q1 resolved YES):** Kein SKIP-Fallback wegen fehlendem Pydantic-Modell. Plan Task 1 rüstet `PortfolioReturnRecord` + `BenchmarkReturnRecord` in `03_Tools/backtest-ready/schemas.py` nach **vor** Check-1-Implementation. SKIP bleibt **ausschließlich** für Missing-File / Empty-File reserviert. Verhindert konservierten Blind-Spot.

#### Check-1.5: Store Freshness (Codex-Patch v0.2, P1)

**Zweck:** Staleness-Detection für Daily-Persist-Stores. STATE-Backlog 21.04. dokumentiert: `portfolio_returns.jsonl` + `benchmark-series.jsonl` seit 17.04. je nur 1 Record — Daily-Append-Cron existiert nicht, Manual-Trigger-Pflicht wurde vergessen. Audit-Tool muss das sichtbar machen, darf aber nicht FAIL werfen, solange Track 4 nicht aufgelöst ist.

**Regel:**
- Extrahiere `date` (oder `timestamp`) des letzten Records aus `portfolio_returns.jsonl` und `benchmark-series.jsonl`.
- Bestimme `last_business_day`: letzter Mon-Fri vor heute (oder heute, wenn Mon-Fri).
- `last_record_date < last_business_day - N Werktage` → `severity="warning"` (WARN, nicht FAIL).
- Initial N = 3 Werktage (Puffer für Karfreitag/Oster-Phänomene).

**Verhalten:**
- `severity="warning"` → Check-1.5 trägt WARN bei. Exit-Code bleibt 0.
- **Eskalations-Trigger für Verschärfung auf error:** Sobald Track 4 ETF+Gold-Erweiterung + Auto-Persist-Cron implementiert ist, severity auf `error` erhöhen (dann FAIL). Bis dahin Persistenz-Pflicht = User-Erinnerung.
- Score-Stores (`score_history.jsonl`, `flag_events.jsonl`) **nicht** in Check-1.5 — diese sind Event-getriggert, nicht Daily-getriggert, Staleness ist dort nicht sinnvoll definiert.

**Fail-Mode (WARN):** „`portfolio_returns.jsonl` letzter Record YYYY-MM-DD, last_business_day YYYY-MM-DD (Lag N Tage). Daily-Append-Cron fehlt — Track 4 öffnet das auf."

**Edge-Case:** Bei US-Feiertagen (Thanksgiving, Christmas) kann 3-Werktage-Puffer zu kurz sein. Puffer ist bewusst großzügig gewählt (3 statt 1); Feiertags-Kalender-Support als Future-Work wenn Noise real wird.

#### Check-2: Markdown Header-Stand-Drift

**Zweck:** Dokumentations-Aktualität (21.04. CORE-MEMORY 4 Tage stale).

**Targets (Codex-Patch v0.2 P6 — Event-Date-aus-Markdown-Content, NICHT commit-author-date):**
- `00_Core/STATE.md` → Header-Zeile Regex `\*\*Stand:\*\*\s*([0-9]{2}\.[0-9]{2}\.[0-9]{4})` vs. jüngste Event-Date aus Markdown-Content (z.B. „Stand:" im Header-Kommentar, oder Pipeline-SSoT-Section-Termine).
- `00_Core/CORE-MEMORY.md` → `**Stand:**` vs. letzter §1 Tabellen-Eintrag-Datum (erste Spalte der §1-Tabelle).
- `00_Core/Faktortabelle.md` → `**Stand:**` vs. jüngstes `Score-Datum`-Feld in Haupttabelle.

**Werktag-Definition (Codex-Patch v0.2 P6):** Mon-Fri. Feiertage werden ignoriert, solange kein Feiertags-Kalender existiert (Future-Work falls Noise real wird). Rationale: Holiday-Calendar wäre US+DE+FR-Hybrid (ASML EU, V US, SU FR) — zu komplex für MVP.

**Threshold:** `stand - neueste_event_date > 2 Werktage` → `severity="error"` (FAIL). 1-2 Werktage Lag = `severity="warning"` (WARN).

**Rationale gegen Commit-Author-Date:** Mass-Edit-Commits (z.B. heutiger A+B+C Sync-Commit berührte 5 Dateien) würden alle Files als „gerade geändert" markieren, ohne dass Content-Stand tatsächlich gepflegt wurde. Event-Date aus parse-barem Markdown-Content ist zuverlässiger.

**Fail-Mode:** 1 FailureDetail pro Datei mit Hint „Header-Zeile aktualisieren auf YYYY-MM-DD".

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

**FLAG-Parsing-Semantik (Codex-Patch v0.2 P3 — präziser als v0.1):**

Beobachtete STATE.md-Werte: `✅`, `⚠️ Insider-Review`, `✅ Insurance Exception`, `✅ Screener-Exception`, `🔴 Score-basiert`, `🔴 CapEx/OCF 83.6%`.

**Parse-Regel:** Icon ist Status, Suffix-Text ist Reason (optional, nicht Teil des Match).

| config.yaml `flag:` | STATE.md Icon | Urteil | Severity |
|---|---|---|---|
| `false` | `✅` (mit oder ohne Exception-Suffix) | Match | — (PASS-Contribution) |
| `false` | `⚠️` | Match (Warning-Watch aktiv) | `warning` (WARN-Contribution) |
| `false` | `🔴` | **Mismatch: config sagt kein FLAG, STATE sagt FLAG** | `error` (FAIL-Contribution) |
| `true` | `🔴` (mit Reason-Suffix) | Match | — (PASS-Contribution) |
| `true` | `✅` oder `⚠️` | **Mismatch: config sagt FLAG, STATE sagt kein FLAG** | `error` (FAIL-Contribution) |

Die Ausnahme-Suffixe (`Insurance Exception`, `Screener-Exception`) sind informationell, werden nicht gegen config.yaml gematcht (bewusst, weil config.yaml keine Exception-Felder führt).

**Edge-Case:** STATE.md zeigt nur Icon ohne Text (z.B. `✅`) — das ist der Normal-Fall und Match-fähig. Text-Extraktion optional für Report-Hint.

#### Check-4: Existence-Check (Pfad-Referenzen)

**Zweck:** Verhindert, dass Pläne/Handover auf nicht-existierende Dateien verweisen.

**Scan-Quellen (Codex-Patch v0.2 — kanonisch qualifiziert):**
- `CLAUDE.md` (project + user's auto-memory MEMORY.md referenzierte Pfade).
- `00_Core/STATE.md` (alle backtick-wrapped Pfade `\`03_Tools/x.py\``).
- `00_Core/SESSION-HANDOVER.md` (kanonischer Pfad — **nicht** Root-Level `SESSION-HANDOVER.md`; wenn Root-File als Alt-Referenz auftaucht, FailureDetail mit Hint „kanonischer Pfad `00_Core/...`").
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

Tool fügt (oder ersetzt) am Ende von STATE.md unmittelbar vor dem `*🦅 STATE.md v1.0 ...` Footer einen durch HTML-Kommentare eingefassten Block:

```markdown
<!-- system-audit:last-audit:start -->
---

## 🔍 Last Audit

**Timestamp (UTC):** 2026-04-21T14:32:41Z
**Result:** 6/7 PASS (1 FAIL: cross_source)
**Run:** `python 03_Tools/system_audit.py --core`
**Full-Report:** stdout (kein Archiv-File)

<!-- system-audit:last-audit:end -->
```

**Idempotenz (Codex-Patch v0.2 P5):** Bei wiederholtem Run → ersetzt bestehenden Block durch **explizite Begin-/End-Marker** statt fragiler Regex `## 🔍 Last Audit bis ^##`. Rationale: Regex-Marker bricht, wenn User später weitere Sections unterhalb einfügt oder den `---`-Separator verschiebt. HTML-Kommentare sind unsichtbar im gerenderten Markdown + definieren einen eindeutigen Ersetzungs-Bereich.

**Algorithmus:**
1. Lese STATE.md.
2. Wenn `<!-- system-audit:last-audit:start -->` vorhanden: finde korrespondierenden End-Marker, ersetze gesamten Block inklusive beider Marker.
3. Wenn nicht vorhanden: erster Run — fügt Block vor dem Footer-Zeile `*🦅 STATE.md v1.0` ein.
4. Atomic-Write (tmp + `os.replace`).

**Fail-Mode:** Wenn Start-Marker vorhanden aber End-Marker fehlt (korrupter Zustand) → Exit-Code 2 mit Fehlermeldung „STATE.md Marker-Block inkonsistent — manuell fixen"; **kein** Blind-Append (würde Duplikate produzieren).

**Opt-Out:** `--no-write` Flag überspringt State-Update komplett.

---

## 7. Testing Strategy

### 7.1 Unit-Tests pro Check

Jeder Check hat `test_<check>.py` mit mindestens 3 Fixtures:
- **PASS-Fixture:** Gesunder Stand, erwartet 0 FailureDetails.
- **FAIL-Fixture:** Bewusst drift-seeded, erwartet ≥1 FailureDetail mit exakter Location.
- **EDGE-Fixture:** Missing-File / Empty-File / Parse-Error → SKIP oder Exit-Code 2.

### 7.2 Integration-Test

`test_integration.py`:
- **Baseline-Run:** Aktueller Repo-Stand → erwartet Exit-Code 0 auf allen Kern-Checks. **Wichtig:** `status="WARN"` für Check-1.5 ist erwartet (Daily-Persist-Stale aus Track-4-Backlog), exit-code trotzdem 0.
- **Seeded-Drift-Run:** Temporäres Repo-Copy mit injizierter Drift (z.B. defcon_level=4 bei Score 70 in `score_history.jsonl`) → erwartet Exit-Code 1 auf Check-1 mit präziser Failure-Location.

### 7.3 Parser-Golden-Tests (Codex-Patch v0.2)

Separate Tests für die brüchigsten Parse-Punkte:
- **STATE-Pipeline-Section-Parser:** Fixtures mit diversen Pipeline-Section-Varianten (leer / nur 🔴 / mit ⏰-Subtabelle / unterbrochen durch Nebensections) → Parser liefert korrekte Plan-Referenz-Liste.
- **FLAG-Variants-Parser:** Alle 6 beobachteten STATE.md-FLAG-Werte (`✅`, `⚠️ Insider-Review`, `✅ Insurance Exception`, `✅ Screener-Exception`, `🔴 Score-basiert`, `🔴 CapEx/OCF 83.6%`) als Input → Icon-Extraktion korrekt.
- **Last-Audit-Idempotenz:** Mehrfacher Run gegen gleiche STATE.md → exakt ein `<!-- system-audit:last-audit:start -->` Block vorhanden; Content wird ersetzt, nicht dupliziert.

### 7.4 Smoke-Test (Codex-Patch v0.2 — temp-repo-copy)

`smoke_test.sh` / `smoke_test.py`: Tool läuft gegen **temp-repo-copy** (kopiert das echte Repo in `tmpdir`, führt `system_audit.py --core --write` dort aus), prüft:
- Exit-Code 0.
- `<!-- system-audit:last-audit:start -->` Block vorhanden in temp-STATE.md.
- Timestamp im Block ist innerhalb der letzten 60 Sekunden.

**Rationale:** Smoke-Test darf **nicht** die echte STATE.md dirtien (sonst muss der Test-Runner jedes Mal reverten). Temp-Copy ist sauber + reproduzierbar + CI-fähig.

### 7.5 Regression-Guard

Nach jedem `migrate_*.py` muss `system_audit.py --core` Exit-Code 0 zeigen — explizite Regel in INSTRUKTIONEN §27.4 nachzutragen (Plan Task 8).

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

## 10. Open Questions — Resolved (Joint-Review 2026-04-21 Nachmittag)

Alle 7 Fragen durch User + Codex **aligned** entschieden. Keine offenen Punkte mehr.

| # | Frage | Resolution | Downstream |
|---|-------|------------|------------|
| **Q1** | PortfolioReturnRecord / BenchmarkReturnRecord Pydantic-Models nachrüsten? | **YES** — Plan Task 1 pflichtig **vor** Check-1-Implementation. SKIP-Fallback bei fehlendem Schema wurde aus §5.1 entfernt (Codex-Patch P2). | Plan Task 1 |
| **Q2** | Vault-Timeout env-var? | **NO** — hardcoded 20s, Future-Work wenn Noise. | §5.2 unverändert |
| **Q3** | Status-Matrix Kern oder Optional? | **Optional** — Doku-Integrität ≠ Scoring-Risk. | §5.2 Check-9 |
| **Q4** | Last-Audit-Zeile auch bei FAIL schreiben? | **YES** — Transparenz > green-only Cosmetics. Zeile zeigt dann exit_code + WARN/FAIL-Counts. | §6.5 |
| **Q5** | Plan-Status-Frontmatter Follow-up-Timing? | **YES defer** — nach Phase-G (TMO Q1 23.04.). Keine Blockade. | Follow-up-Plan TBD |
| **Q6** | Neue Models in schemas.py? | **YES schemas.py** (bestehender Hub, INSTRUKTIONEN §18 referenziert). | Plan Task 1 |
| **Q7** | GitHub-Actions-Workflow? | **NO** YAGNI — kein CI-Runner aktiv, Exit-Codes genügen. | §3 Non-Goal bestätigt |

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

- [ ] **Task 1:** `schemas.PortfolioReturnRecord` + `schemas.BenchmarkReturnRecord` in `03_Tools/backtest-ready/schemas.py` nachgerüstet + Unit-Tests für beide Models.
- [ ] Tool läuft gegen aktuellen Repo-Stand mit Exit-Code 0 (Baseline). Check-1.5 darf `status="WARN"` zeigen (Daily-Persist-Stale), das ist Soll-Zustand bis Track 4.
- [ ] `/SystemAudit` Slash-Command funktional, STATE.md-„Last Audit"-Block (HTML-Comment-Marker) geschrieben.
- [ ] Alle 7 Kern-Checks inkl. Check-1.5 implementiert mit ≥ 3 Unit-Test-Fixtures pro Check (PASS / FAIL / EDGE).
- [ ] Parser-Golden-Tests für STATE-Pipeline-Section, FLAG-Variants, Last-Audit-Idempotenz.
- [ ] Integration-Test (Baseline + Seeded-Drift) + Smoke-Test (temp-repo-copy).
- [ ] Exit-Codes 0/1/2 korrekt differenziert: 0 = all PASS/WARN/SKIP, 1 = ≥1 FAIL, 2 = IO/Tool-Error.
- [ ] INSTRUKTIONEN §27.4 um Regression-Guard-Regel ergänzt („nach jedem migrate_*.py → system_audit.py --core Exit 0").
- [ ] Optional-Checks (Vault + Status-Matrix) implementiert mit Timeout-Handling.
- [ ] Duration <30s bei --core auf aktuellem Repo-Stand (Performance-Budget).
- [ ] STATE.md `🗺 Aktive Pipeline (SSoT)`-Section um Plan-Referenz für dieses Tool updatet, sobald Plan geschrieben (Pipeline-SSoT-Pflege-Pattern).

---

*Spec v0.2 ratified (Codex + User Joint-Review 2026-04-21) | Nächster Schritt: Plan-Writing (Phase E) via `superpowers:writing-plans`-Skill*
