# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-26 — **Phase-2 system-audit MERGED auf main** (`ac43929`, --no-ff). 14 Commits gebündelt: 6 neue Core-Checks + PyYAML-Preflight + Final-Review-Pass (Codex 3 Important-Fixes + CodeRabbit 2 In-Scope-Nits) + Smoke 26 Cases. Post-Merge-Audit auf main 9/14 PASS — alle FAIL/WARN sind jetzt sichtbare pre-existing Drifts. **Nächste Session: Deferred-Liste systematisch durchgehen.**

### 🟢 Resume-Stand

**Branch:** `main` (post-merge), 14 Commits seit `1fada16` integriert. Working Tree dirty: `00_Core/STATE.md` (Last-Audit-Stamp 2026-04-26T19:16:11Z von Post-Merge-Verifikation) + `00_Core/SESSION-HANDOVER.md` (dieser Block) — beide werden mit dem Handover-Commit auf main eingecheckt.

**Pre-Resume-Checks:**
1. `git status --short` — sollte nur die 2 Files zeigen, plus pre-existing dirty (stash + xlsx + .code-workspace)
2. `git log --oneline -3` — Top-Commit ist Handover-Commit (kommt gleich)
3. `python "03_Tools/system_audit/_smoke_test.py"` → 26 [OK]
4. `python "03_Tools/system_audit.py" --core --no-write` → 9/14 PASS, 2 FAIL, 3 WARN (Drift-Liste unten)

### 🎯 Hauptauftrag: Deferred-Liste systematisch durchgehen

Phase-2 hat den **Drift sichtbar** gemacht. Jetzt geht's an die Bereinigung. Drei Dimensionen, priorisiert:

#### A) Audit-Drifts (durch Phase-2 Sweep-Driver belegt)

**Core-FAILs (2):**
- `markdown_header` — pre-existing
- `existence` — pre-existing (~54 CLAUDE.md-Pfad-Refs Drift seit Phase-A — siehe PIPELINE #1 Codex-Follow-up (a))

**Core-WARNs (3):**
- `cross_source` — pre-existing
- `skill_frontmatter`: 3 Skills mit fehlenden Frontmatter-Feldern:
  - `01_Skills/dynastie-depot/SKILL.md` — `description` fehlt/leer
  - `01_Skills/insider-intelligence/SKILL.md` — `version` fehlt
  - `01_Skills/non-us-fundamentals/SKILL.md` — `version` fehlt
- `header_freshness`: 4 Skills mit fehlendem Stand-Header:
  - `01_Skills/non-us-fundamentals/SKILL.md`
  - `01_Skills/dynastie-depot/SKILL.md`
  - `01_Skills/quick-screener/SKILL.md`
  - `01_Skills/backtest-ready-forward-verify/SKILL.md`

**Optional-FAILs (Vault-Drift, via `--full` oder `--vault`):**
- `vault_backlinks`: 11 broken Backlinks (allesamt erkannt durch neue Reverse-Driver-Logik):
  - `[[ETF-Core]]` × 2 (Palomar-Methods, steuer-architektur)
  - `[[transcript]]` × 3 (alle drei Video-Notes aus updating-system/)
  - `[[News Sentiment Analysis]]`, `[[Fabrizio Dimino]]`, `[[Chain-of-Thought Prompting]]`, `[[Alexander Pearson Sheppert]]`, `[[defcon-system]]`, `[[Steuer-Architektur]]`, `[[insider-intelligence-skill]]`
  - **`[[BRKB\]]`** in `wiki/sources/tools/insider-intelligence.md:33` — Pipe-Escape-Problem, eigene Subkategorie (CodeRabbit hatte das im MD-Out-of-Scope auch erwähnt für `Depot-State-April-2026.md:51`)
- `status_matrix`: 4 duplicate B-Nummern in `wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` (B1, B11, +2 weitere — siehe Live-Output)

#### B) Phase-2 interne Defer-Liste (aus den Subagent-Reviews, nicht commit-blockierend)

- **Task 8 NEVER STARTED** — Plan §2123-Ende (`docs/superpowers/plans/2026-04-25-system-audit-rework.md`): Defer-Doku in PIPELINE.md + Live-Drift-Cleanup. Geht natürlich in (A) auf.
- **Task 4 header_freshness:** 2 Important regex-cosmetics deferred
- **Task 5 governance_parity:** 5 Minor deferred
- **Task 7 pointer_completeness:** 5 Minor cosmetic deferred
- **Codex-Phase-2-Final-Review-Minor:** Mixed diagnostic vocabulary (`warning`/`WARN`), brittle 12-line frontmatter window in `header_freshness:34,48`, malformed-vs-absent-frontmatter folding in `skill_frontmatter:29-36,71-78`, duplicated `satelliten/satelliten/` path-segment in `cross_source_reverse:119`

#### C) Pre-existing PIPELINE-Deferreds (chronologisch, alle separat dokumentiert in PIPELINE.md)

- **#14 Vault-Discoverability für INSTRUKTIONEN.md §§** (NEU 26.04.) — Vault-side Index oder Reverse-Backlink-Block. Bequemlichkeits-Optimierung, nicht systemkritisch.
- **#13 Sub-Drift `Backtest-Ready-Infrastructure.md`** 4-Layer→5-Layer Sync mit DEFCON-System.md ausstehend (Mini-PR-Kandidat)
- **#11 Atomic-Write-Härtung Follow-ups:** Recovery-Script `03_Tools/repair_daily_persist.py` für Split-State-Heilung; Atomic-Write erst bei Incident
- **#10 KG-Roadmap v0.1 `draft-frozen`** — Re-Review-Trigger: Cross-Entity-Bedarf ODER Score-Archiv-Interim-Gate 2026-10-17
- **#8 v3.1 Cache-Refactor** — Trigger: 262s-Schmerz oder >400s-Alert wiederholt
- **#9 Track 4 ETF+Gold-Erweiterung** — User-Input-Pflicht (ETF/Gold-Ticker)
- **SKILL.md §215 Snapshot-First-Block-Review** — Backlog seit 00_Core-Refactor Tier 2 Schluss (out-of-scope-Markierung)
- **#1 Codex-Follow-ups aus System-Audit-Phase-A:** (a) Check-3 future-date-exclude + existence-Cleanup (~54 Pfad-Refs), (b) Check-10 status_matrix Regex-Scope einengen, (c) §27.5-Kommentar-Update — wahrscheinlich teilweise schon durch Phase-2-Sweep adressiert, prüfen

### 💡 Vorschlag für die Session-Strategie

1. **Erst (A) Core-FAILs/-WARNs durchgehen** — die sind im Hot-Pfad jeder Routine und mit kleinen Edits behebbar (`description`/`version`/`Stand` in 3-4 SKILL.md ergänzen, broken backlinks fixen). Das holt das Audit auf 14/14 PASS und gibt sofortige Validation, dass das Tool korrekt findet, was es findet.
2. **Dann (A) Vault-Optional-FAILs** — die `vault_backlinks` sind echte Wiki-Bugs (Notes umbenannt/gelöscht ohne Backlink-Update). Status-Matrix-Duplikat-Bs sind ein Schema-Drift.
3. **Dann (B) Phase-2-Internal-Defers** durcharbeiten als kleinen Cleanup-Branch — die Codex-Minors sind alle 1-2-Zeilen-Fixes.
4. **Erst danach (C)** — größere PIPELINE-Items, die teils User-Input brauchen (Track 4) oder Strategy-Calls (KG-Roadmap, v3.1).

### ⚠️ Wichtige Notizen

**Pending stash:** `stash@{0}: On main: pre-phase2-resume vault drift + xlsx 26.04.` — bleibt unangetastet. Inhalt: Vault-Concept-File-Drifts (PORTFOLIO/STATE/SYSTEM/PIPELINE in `wiki/concepts/`) + Investing-Mastermind/index.md+log.md + xlsx + .obsidian/app.json + 4 Vault-Deletes. **Beim Drift-Cleanup nach (A.2) prüfen, ob der Stash echte Sync-Pflicht-Items enthält** — dann selektiv apply, sonst archivieren/löschen.

**Standing-Pre-existing-Dirty:**
- `03_Tools/Rebalancing_Tool_v3.4.xlsx` (im Stash)
- `07_Obsidian Vault/Obsidian Mindmap/.obsidian/app.json` + 4 Vault-Deletes (im Stash)
- `Claude-Stuff.code-workspace` — IDE-Setup, gitignore-Kandidat (untracked)

**System-Audit-Tool-Stand:**
- Smoke 26/26 [OK]
- Core 14 Checks: 9/14 PASS (oben Liste)
- Optional 2 Checks (vault_backlinks, status_matrix): 0/2 PASS (oben)
- `--minimal-baseline` Regression-Gate: **3/3 PASS** (Pflicht-Erhalt!)
- Slash-Doc `/SystemAudit` synchronisiert mit allen 8 Flags inkl. `-v/--verbose` und `--timeout-per-check`
- STATE.md Last-Audit-Block-Writer funktional verifiziert (Test #7 vom 26.04.19:13Z)

**Calibration-Notiz (unverändert seit Phase-2 Start):**
F3 (`_forward_verify_helpers.py:25, 257-259`) bleibt **INFO, nicht FIX** — Teil-Gate-Trade-off, Codex-RECONCILED VALID. Nicht als §18-Verletzung oder score_event_parity-Failure re-klassifizieren.

---

## Standing-Focus 30 Tage (unverändert)

- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal-Gate)
- **29.04. MSFT Q3 FY26** — FLAG-Review (CapEx/OCF bereinigt <60%)

---

## 📜 Handover-Policy (seit 2026-04-25 — Tier 2 Follow-up)

Nur **aktiver** RESUME-INPUT-Block in dieser Datei. Historie kanonisch in:
- **`git log`** — jeder Session-Ende-`handover:`-Commit ist die Banner-Chronik
- **`CORE-MEMORY.md` §13** — System-Lifecycle-History
- **`PIPELINE.md`** — Strikethrough-DONE-Items mit Datum + Commit-Hash

Pflege-Pflicht: Bei Session-Ende den aktiven Block durch den neuen ersetzen — nicht anhängen.

---

*🔁 SESSION-HANDOVER.md v2.0 | Dynasty-Depot | Slim-Resume — Policy B*
