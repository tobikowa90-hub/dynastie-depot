# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-21 Abend (**Phase E 12/19 Tasks committed + Codex-Review-Härtungswelle** in Session 21.04. Nachmittag-Abend — siehe Commit-Graph `f0f707e..7cea0e0`, 23 Commits auf main. **Next: Phase E fortsetzen ab Task 13 (CLI-Orchestrator)** — Opus-Implementer, einziger Koppelpunkt des Audit-Tools.)
**Vorherige Aktualisierungen:** 2026-04-21 Nachmittag-Spät — Spec v0.2 ratified + Plan v0.2 Codex-reviewed · 2026-04-21 Abend — Fix-Welle A committed (`7cea0e0`).

> **Progress-Banner (Phase A-G):** ✅ A+B+C (Sync-Welle `8acb13c`) · ✅ D (Spec v0.2 `82482d7`) · 🟡 **E 12/19** (Tasks 1-12 done, 13-19 open) · ⏳ F (Provenance-Plan-Execution) · ⏳ G (TMO Q1 23.04.).

## 🚀 NÄCHSTE SESSION — Direkter Einstieg

**Trigger:** `Session starten` → STATE.md lesen → `superpowers:subagent-driven-development`-Skill aktivieren → TodoWrite zeigt 12 completed, 7 pending → **Task 13 in_progress setzen** → Plan-Lesen Zeilen 2641-2827.

**Command zur schnellen Lageprüfung:**
```bash
cd "C:\Users\tobia\OneDrive\Desktop\Claude Stuff"
python 03_Tools/system_audit/_smoke_test.py    # muss 11 [OK]-Zeilen zeigen
git log --oneline f0f707e..HEAD | head -25     # 23 Commits
git status --short                              # clean
```

---

## 📋 Was in Session 21.04. Abend passiert ist

**Phase E Tasks 1-12 vollständig umgesetzt** nach superpowers:subagent-driven-development — pro Task Implementer-Subagent + Spec-Reviewer + Code-Quality-Reviewer (Codex-Rescue wo Architektur-Entscheidungen anstanden):

| Task | Commits | Inhalt |
|------|---------|--------|
| 1 | `404b057` + `e673916` + `afbf52c` | PortfolioReturnRecord + BenchmarkReturnRecord (schemas.py) |
| 2 | `fa3d10a` + `cb44af7` + `651b1cc` | system_audit-Package + types.py + Registry-Skeleton |
| 3 | `5d4cc44` + `47e0695` | Check-1 JSONL-Schema (+ robustness fixes: sys.path idempotent, structured errors, stores_override filter) |
| 4 | `ab58c12` + `dbaba27` | Check-1.5 Store-Freshness (WARN-Severity) |
| 5 | `5c969af` + `e065f6a` | Check-2 Markdown-Header-Drift (event-date-based, Codex-P6) |
| 6 | `f0e89fd` + `aa010c7` | Check-3 Cross-Source (header-driven Faktortabelle-Parser nach Codex-Live-Find) |
| 7 | `d8f046f` + `67fefc2` | Check-4 Existence (Backtick-path-refs + Codex-P3 scope-limit) |
| 8 | `8a37b24` | Check-5 Skill-Version (4 fixture-tests, Codex-P4) |
| 9 | `4d94932` | Check-6 Pipeline-SSoT + `extract_plan_refs` (Forward-Dep für Check-4) |
| 10 | `f813c2c` | Check-7 log.md-vs-git-HEAD (+ 3rd candidate path für Live-Repo) |
| 11 | `1066bce` | report.py render_human + render_json + compute_exit_code |
| 12 | `c8900bd` | state_writer.py idempotent (HTML-Marker, atomic, Codex-P5) |
| Fix-A | `7cea0e0` | Robustness-Härtung nach Codex-Full-Review (82%→~93% Confidence) |

**Codex-Sparring-Review nach Task 12 identifizierte 5 messbare Confidence-Gaps** → Fix-Welle A committed:
- `errors="replace"` in allen `read_text`-Aufrufen (BOM/weird encoding tolerant)
- cross_source.py: `yaml.YAMLError`-catch + Satelliten-KeyError/TypeError-guard per-entry
- state_writer.py: Duplicate-Marker-Detection (n_start/n_end > 1 = RuntimeError)
- existence.py: PATH_RE Space-Rejection explizit dokumentiert + 1 neuer smoke-test
- markdown_header.py: `n_checked == 0` → SKIP (vorher fälschlich PASS)

---

## 🎯 Live-Audit-Probelauf (21.04. Abend) — ECHTE Drift-Findings

```
PASS  jsonl_schema         31/31          84ms
PASS  store_freshness       2/2             0ms
FAIL  markdown_header       1/3   (2 err)   6ms   ← 2/3 Core-Files Stand-Drift
WARN  cross_source         22/22  (1 warn) 172ms  ← AVGO ⚠️ Insider-Review (benign)
FAIL  existence            70/231 (161 err) 13ms  ← massive Backtick-path-Drift
WARN  skill_version         1/2  (1 warn)    3ms  ← backtest-ready ungepackt (bekannt)
PASS  pipeline_ssot         3/3             0ms
PASS  log_lag               1/1            19ms
```

**161 existence-FAILs sind ECHTE Drift, nicht Bugs** — genau der Tool-Zweck. Mehrheit: veraltete Backtick-Referenzen in CLAUDE.md/STATE.md/SESSION-HANDOVER + Pipeline-Plans, die nicht mehr existieren (Track-4-Notizen, alte Tool-Pfade).

**Bekanntes Terminal-Encoding-Problem:** `render_human`-`print` crashed in Windows cp1252 wegen 🔍-Emoji. Tool-Output selbst OK (String wird korrekt erzeugt). **Task 13 muss `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` in main() setzen.**

---

## 🔨 Task 13 — Opus-Task, Pre-Notes aus Codex-Review

**Task 13:** `03_Tools/system_audit.py` CLI-Orchestrator. Plan Zeilen 2641-2827. **Opus-Implementer** (einziger Task mit Design-Judgement-Koppelung — Exit-Code-Kontrakt + Timeout-Dispatch + argparse).

**Pre-besorgte Entscheidungen aus Codex-Review vor Task 13 Dispatch:**

1. **`sys.stdout.reconfigure(encoding="utf-8", errors="replace")`** direkt in `main()` vor Rendering, mit Fallback wenn stdout kein reconfigure hat (`hasattr`-Check).
2. **Per-Check-Timeouts via `ThreadPoolExecutor(max_workers=1)` + `future.result(timeout=...)`.** Timeout = synthetischer `CheckResult(status="FAIL", severity="error")`. Interne Tool-Exception getrennt als rc=2.
3. **Exit-Code-Trennung (Codex-P1):**
   - Orchestrator sammelt `internal_errors: list[Exception]`
   - Nicht leer → rc=2 (tool bug)
   - Sonst `report.compute_exit_code(results)` → rc=1 bei FAIL, rc=0 bei PASS/WARN/SKIP
4. **Argparse-Design:**
   - Mutually-exclusive Scope-Group: `--core` default, `--full`, `--minimal-baseline`
   - `--format human|json`, `--timeout-per-check=20`, `--write-state/--no-write-state`
   - `--minimal-baseline` = nur jsonl_schema + pipeline_ssot + log_lag (für Task-17-Gate, wenn Drift-Aufräumung noch nicht passiert ist)
5. **STATE.md-Write default on** (Spec §6.5), aber bei rc=2 NICHT schreiben (corrupted tool-state soll keine STATE.md dirty machen). Bei rc=1 schreiben — echte Drift soll sichtbar bleiben.
6. **Importlib-based Registry-Dispatch:** `"module:function"` string → `importlib.import_module(module)` → `getattr(fn)` → call.

**Task-17-Baseline-Scope-Entscheidung (aus Codex-Review, von User noch nicht bestätigt):** Mit 161 echten existence-FAILs erreicht Live-Baseline heute nicht Exit-Code 0. Zwei Optionen:
- **A)** Task 17 nutzt `--minimal-baseline` als Gate (nur strukturelle Integrity — kein content-drift). Die 161 Findings werden mit dem Tool systematisch abgearbeitet, dann `--core` als Ziel.
- **B)** Die 161 Drifts jetzt als separate Aufräum-Welle vor Task 17 abarbeiten (~30-60 Min).

Empfehlung: A pragmatisch. B auf die Nachsession-Liste.

---

## 🧠 Deferred: Skill-Frage für nach Task 19

User hat parallel mit Opus an anderer Stelle philosophiert, ob aus dem System-Audit-Python-Code ein **Housekeeping-Skill `system-state-guardian`** (Name Opus-Vorschlag) gebaut werden sollte — analog zur `backtest-ready-forward-verify`-Kapsel.

**Kernpunkte aus dem Opus-Gespräch (per User-Einlage):**

- **Kategorie:** Housekeeping-Skill (Meta-Ebene, analog zu `skill-creator`), NICHT Analyse-Pipeline-Skill wie backtest-ready.
- **Strikte Trennung:** Housekeeping wartet State, Analyse-Skills benutzen State. Keine Rückkopplung in Analyse-Pipelines (sonst Zirkular-Abhängigkeit).
- **Aktivierungspfade:** (a) Session-Start Silent-Mode, (b) `!HygieneCheck` manuell Vollreport, (c) nach skill-creator-Modifikationen. **NICHT** aus dynastie-depot heraus.
- **Auto-Fix-Whitelist** vs. **User-Eskalation** hart definiert (Auto nur bei reinem Informations-Erhalt).
- **Audit-Trail** `hygiene_log.jsonl` mit Action/Target/Hash-Pre/Post/Grund.
- **Dry-Run-Pflicht** erste 2-4 Wochen.
- **Kritisch:** „Baue den Skill erst, wenn der Python-Code stabil ist" (Opus-Einwand). Faustregel: Erst Python-API eingefroren → SKILL.md als dünne Kapsel drüber.

**Entschieden:** Skill-Entscheidung **auf nach Task 19 aufgehoben.** Wenn das Tool operational ist + erste Woche Live-Probeläufe gezeigt haben, welche Aktivierungspfade tatsächlich gebraucht werden → dann v1.0-SKILL.md.

Dieser Handover persistiert die Opus-Gesprächs-Kernpunkte für die nachfolgende Skill-Session. Vollständiger Brainstorm-Text liegt in der User-Message dieser Session (ggf. vor Kontext-Cut abspeichern).

---

## 📊 Commit-Graph (23 Commits)

```
7cea0e0 refactor(system-audit): robustness hardening pre-Task-13 (Codex-Review)
c8900bd feat(system-audit): state_writer idempotent HTML-marker block
1066bce feat(system-audit): report.py human + JSON renderer
f813c2c feat(system-audit): Check-7 log.md vs git-HEAD lag
4d94932 feat(system-audit): Check-6 pipeline-ssot reverse-only + parser golden tests
8a37b24 feat(system-audit): Check-5 skill-version (SKILL.md vs ZIP)
67fefc2 fix(system-audit): Check-4 n_checked counts legacy SESSION-HANDOVER hits
d8f046f feat(system-audit): Check-4 existence (backtick-wrapped paths)
aa010c7 fix(system-audit): Check-3 Faktortabelle parser header-driven + live-structure
f0e89fd feat(system-audit): Check-3 cross-source (config↔STATE↔Faktortabelle↔Vault)
e065f6a test(system-audit): Check-2 WARN fixture + path consistency
5c969af feat(system-audit): Check-2 markdown header-stand drift (event-date based)
dbaba27 refactor(system-audit): Check-1.5 defensive parse + test comment
ab58c12 feat(system-audit): Check-1.5 store freshness (WARN, non-blocking)
47e0695 refactor(system-audit): Check-1 robustness fixes (quality review)
5d4cc44 feat(system-audit): Check-1 JSONL schema revalidation + 3 fixtures
651b1cc refactor(system-audit): relative import + docstring fix + test coverage
cb44af7 style(system-audit): __future__ annotations consistency in __init__.py
fa3d10a feat(system-audit): package skeleton + CheckResult/FailureDetail contract
afbf52c refactor(schemas): Remove redundant inline import copy in _smoke_tests
e673916 fix(schemas): __all__ alphabetische Reihenfolge PortfolioReturnRecord/Position
404b057 feat(schemas): PortfolioReturnRecord + BenchmarkReturnRecord nachgeruestet
f0f707e (baseline) handover-sync(phase-d-closure): Pre-/clear Handover-Update
```

---

## 🎯 Remaining Tasks 13-19 (Phase E Abschluss)

- **13 CLI-Orchestrator** `system_audit.py` — **Opus**-Implementer, Codex-Pre-Notes oben
- **14 Optional Check-8/9** — Vault-Backlinks + Status-Matrix (20s Timeout, 6 Fixtures Codex-P5)
- **15 Smoke-Test temp-repo-copy** — strict rc=0 gegen Repo-Baseline-Kopie (Codex-P2)
- **16 Slash-Command** `.claude/commands/SystemAudit.md` — dünner Wrapper
- **17 INSTRUKTIONEN §27.5 + Live-Baseline-Run** — **Task-17-Scope-Frage (A vs B) mit User klären vor Dispatch**
- **18 Pipeline-SSoT + Memory-Sync** — STATE.md Pipeline-#4 → ✅-Archiv, CORE-MEMORY §10, log.md, !SyncBriefing
- **19 Acceptance-Matrix Spec §12** — Verification-Before-Completion

**Geschätzter Aufwand Tasks 13-19:** ~90-120 Min in nächster Session (Task 13 ist der größte, ~30-45 Min inkl. Review-Loop; 14-18 je 10-20 Min; 19 ~15-20 Min Acceptance-Walkthrough).

---

## 📎 Fortlaufende Kontext-Erinnerungen

- **User-Consent für Main-direct-Commits** ist für diese Execution-Sequenz erteilt. Atomare Task-Commits gewünscht. Kein Worktree.
- **Modell-Plan C** aktiv: Sonnet 4.6 für alle Subagents (Implementer + Reviewer), Opus 4.7 nur für Task 13 Orchestrator + Final-Review falls Acceptance-Matrix Unklarheiten.
- **Codex statt Advisor** für Second-Opinion (Memory `feedback_codex_over_advisor.md`).
- **Applied Learning §Exhaustive-Drift-Check** hat bei Task 6 direkt gegriffen — Live-Faktortabelle-Parser-Fix war ein echter Treffer gegen die 21.04.-Lesson.
- **Python 3.14.3 / PyYAML 6.0.3** — Keine neuen Dependencies eingeführt. `types.py` shadowed stdlib `types` bei Direct-Script-Invocation → `sys.path.pop`-Guard in _smoke_test.py bleibt (Python-3.14-Specific, dokumentiert).

---

## Referenzen

- Plan v0.2: `docs/superpowers/plans/2026-04-21-system-audit-tool.md` (Commit `7218a85` + Codex-Patches in `82482d7`)
- Spec v0.2: `docs/superpowers/specs/2026-04-21-system-audit-tool-design.md`
- Aktives Package: `03_Tools/system_audit/`
- Live-Smoke: `03_Tools/system_audit/_smoke_test.py` (11 Groups)
- Archiv-Stores: `05_Archiv/score_history.jsonl` (27 Records), `flag_events.jsonl` (2 Records), `portfolio_returns.jsonl` + `benchmark-series.jsonl` (je 1 Record, 17.04. stale)
