# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-22 (**Phase E 18/19 Tasks done** — Tasks 15/16/17/18 committed; nur **Task 19** (Verification-Before-Completion Acceptance-Matrix + 2. obligatorischer 4-Wege-Review-Pass) offen).
**Vorherige Aktualisierungen:** 2026-04-21 Nacht — Task 14 Optional Checks + Fix-Welle C+D (`ab6b3f5`) · 2026-04-21 Abend-Spät — Task 13 (`4a9168e`/`4dc8825`/`0dbd8f2`) · 2026-04-21 Abend — Fix-Welle A (`7cea0e0`) · 2026-04-21 Nachmittag-Spät — Spec v0.2 ratified (`82482d7`).

> **Progress-Banner (Phase A-G):** ✅ A+B+C (Sync-Welle `8acb13c`) · ✅ D (Spec v0.2 `82482d7`) · 🟡 **E 18/19** (Tasks 1-18 done, 19 open) · ⏳ F (Provenance-Plan-Execution) · ⏳ G (TMO Q1 23.04.).

## 🚀 NÄCHSTE SESSION — Direkter Einstieg

**Trigger:** `Session starten` → STATE.md lesen → `superpowers:subagent-driven-development` Skill aktivieren → **Task 19 in_progress setzen** → Plan-Lesen Zeilen 3467-3501 (Acceptance-Matrix) + `docs/superpowers/specs/2026-04-21-system-audit-tool-design.md` §12.

**Command zur schnellen Lageprüfung:**
```bash
cd "C:\Users\tobia\OneDrive\Desktop\Claude Stuff"
python 03_Tools/system_audit/_smoke_test.py          # muss 14/14 [OK]
python 03_Tools/system_audit/_smoke_temp_repo.py     # muss 2× [OK] (baseline + seeded-drift)
python 03_Tools/backtest-ready/schemas.py            # muss "all schema smoke tests passed"
python 03_Tools/system_audit.py --minimal-baseline   # rc=0, 3/3 PASS, schreibt Last-Audit-Block
python 03_Tools/system_audit.py --full --no-write    # rc=1 (known bugs) — NICHT fixen, Context-Info
git log --oneline ab6b3f5..HEAD | head -6            # 4 neue Commits
git status --short                                   # nur Vault-Noise (pre-existing, User-seitig)
```

---

## 📋 Was in Session 22.04. passiert ist (Tasks 15/16/17/18 done)

**4 Commit-Wellen, alle Codex-reviewed bei Spec-Drift, keine Code-Quality-Pässe bei Minor-Tasks (per `feedback_review_stack.md` Matrix). Fix-Pattern für nächste Session: Task 19 braucht BEIDES (Codex + CodeRabbit) als Meilenstein-Abschluss.**

| Commit | Task | Inhalt |
|--------|------|--------|
| `486f2c1` | **15** | Smoke `_smoke_temp_repo.py` (120 LOC) — temp-repo + seeded-drift integration. Codex-Reconciliation Option 2: `rc == 0` → `rc ∈ {0, 1}` (Plan-Header-Notice dokumentiert). 3 Plattform-Fixes (Py 3.14 sys.path-Guard, Windows cp1252 encoding). Live: `[OK]` 2×. |
| `fa238bf` | **16** | `.claude/commands/SystemAudit.md` (15 LOC) — Slash-Command-Wrapper `$ARGUMENTS`-Passthrough, Default `--core`. Interaktiver Slash-Trigger-Test **offen** (kann in nächster Session via `/SystemAudit --minimal-baseline` verifiziert werden). |
| `ab7ae19` | **17** | INSTRUKTIONEN §27.5 Migration-Regression-Guard + initialer Baseline-Run. Scope `--minimal-baseline` statt Plan-ursprünglich `--core` (Plan-Header-Notice dokumentiert Rollback-Pfad an Check-3-Fix + existence-Cleanup). STATE.md bekommt ersten ehrlichen Last-Audit-Block 3/3 PASS. |
| `ca35f62` | **18** | Sync-Welle: STATE.md Banner 18/19 + Pipeline-SSoT Punkt 4 DONE + Backlog „Audit-Tool fehlt" → deployed + Last-Audit refreshed 22:19:55Z; CORE-MEMORY §10 Sub-Section 22.04. mit Check-Status-Tabelle + Plan-Header-Notices-Verweis + Lesson (Fixtures vs Live-Content); log.md Entry `[2026-04-22] deployment`. |

**Baseline-Realität (wichtig für Task 19):**
- `--minimal-baseline` (Check-1 jsonl_schema + Check-6 pipeline_ssot + Check-7 log_lag) = **3/3 PASS, rc=0** — das ist der Regression-Guard-Gate.
- `--core` = 4/8 PASS, rc=1 mit 2 known Tool-Bugs:
  - **Check-3 `markdown_header` Future-Date-Bug** — Long-Term-Gate-Rows (2028-04-01 Review-Gate §29.6, 2027-10-19 R5-Interim, 2026-10-17 Score-Archiv-Interim) werden als "newest event" gewertet → falsches FAIL auf STATE.md + Faktortabelle. Tool-Bug, nicht echte Drift. **Follow-up-Task #2 offen.**
  - **Check-5 `existence`** — 54/186 CLAUDE.md-Pfadreferenzen ohne `00_Core/`-Prefix. Per SESSION-HANDOVER-Vorgänger-Zeile 100 explizit auf **post-Task-17 Follow-up-Welle deferred** (~135 existence-FAILs werden per Tool aufgeräumt, nicht in dieser Session-Sequenz).

**Plan-Header-Notices (Spec-Drift-Dokumentation, Spec v0.2 frozen):** 2 Stück im Plan-File `docs/superpowers/plans/2026-04-21-system-audit-tool.md` (gitignored, liegt on-disk). Keine Spec-v0.3-PR nötig — User-Entscheidung A pragmatisch + Codex-Reconciliation RECONCILED.

---

## 🎯 Task 19 Details — Acceptance-Matrix + 2. 4-Wege-Review-Pass

**Plan 3467-3501 + Spec §12.** Step 19.1 = 11 Acceptance-Items verifizieren, Step 19.2 = Execution-Report an User.

### Acceptance-Matrix (Spec §12) — erwartete Outcomes pro Item

| # | Acceptance | Erwartung 22.04. | Evidence |
|---|---|---|---|
| 1 | `PortfolioReturnRecord` + `BenchmarkReturnRecord` + Tests | ✅ PASS — 8-10/10 | `python 03_Tools/backtest-ready/schemas.py` |
| 2 | Tool Exit-Code 0 auf Baseline | **⚠️ Drift** — `--core` rc=1 wg. Tool-Bugs. `--minimal-baseline` rc=0 ist der pragmatische Gate. | Plan-Header-Notice Task 15 + Task 17 |
| 3 | `/SystemAudit` funktional, STATE.md Last-Audit-Block | ✅ PASS | `grep '<!-- system-audit:last-audit:start -->' 00_Core/STATE.md` |
| 4 | 7 Kern-Checks + 1.5 + ≥3 Fixtures/Check | ✅ PASS | `_smoke_test.py` 14/14 |
| 5 | Parser-Golden-Tests | ✅ PASS | `_smoke_test.py`-Output |
| 6 | Integration (Baseline + Seeded-Drift + temp-repo-Smoke) | ✅ PASS — 2× `[OK]` | `_smoke_temp_repo.py` |
| 7 | Exit-Codes 0/1/2 differenziert | Manuell-Test in 19.1 (für rc=2 Tool-Bug-Injection) | — |
| 8 | INSTRUKTIONEN §27 Regression-Guard | ✅ PASS — §27.5 | `grep -n 'Migration-Regression-Guard' 00_Core/INSTRUKTIONEN.md` |
| 9 | Optional-Checks Vault + Status-Matrix mit Timeout | ✅ PASS | `--full` zeigt 9 Checks (Check-8 29ms, Check-9 grün) |
| 10 | Duration <30s auf `--core` | ✅ PASS — 210ms | Live-Output Task 18 |
| 11 | STATE.md Pipeline-SSoT-Section updatet | ✅ PASS | Commit `ca35f62` |

**Item-2-Handling:** Drift explizit als Acceptance-Note ausweisen: `--core` rc=0 ist aufgeschoben (abhängig von Follow-up-Task #2 Check-3-Fix + existence-Cleanup). `--minimal-baseline` rc=0 erfüllt den strukturellen Invarianten-Gate (jsonl_schema + pipeline_ssot + log_lag). Siehe Plan-Header-Notices + STATE.md Last-Audit-Block.

### 2. 4-Wege-Review-Pass (Meilenstein-Abschluss, `feedback_review_stack.md` Matrix)

**Sequenz:** Codex → CodeRabbit (NICHT invertiert — kein Security-Refactor).

**Codex-Pass (Meilenstein-Reconciliation):** Gegen gesamte Task-15-bis-18-Delta (`git diff ab6b3f5..HEAD`).
- Fokus: Spec-Drift-Dokumentations-Qualität der 2 Plan-Header-Notices, Acceptance-Matrix-Coverage vs Spec §12, §27.5-Klausel-Wortlaut vs §27.4-Präzedenz-Struktur.
- Dispatch via `codex:rescue` mit `--fresh` (neue Thread, nicht Reconciliation-Continuation).

**CodeRabbit-Pass:** `wsl.exe -- bash -lc 'coderabbit review --base ab6b3f5 --plain'` (kanonisch, memory `coderabbit_cli_via_wsl.md`).
- Fokus: Style-/Security-/Correctness-Findings im Code-Delta (`_smoke_temp_repo.py`, `.claude/commands/SystemAudit.md`).
- Erwartung: 2-5 Findings (Task 14 hatte 7 in ähnlichem Scope), wahrscheinlich Minor (nit/warning-Severity).

**Fix-Welle falls Findings:** Separate Fix-Commits `fix(system-audit): Fix-Welle E — ...`, dann Re-Review falls Blocker.

**Final-Commit Task 19:** `log(phase-e-done): Task 19 Acceptance-Matrix PASS + 2. 4-Wege-Review RECONCILED` mit Execution-Report im Commit-Body.

---

## 📊 Commit-Graph (seit letztem Handover `ab6b3f5`)

```
ca35f62 handover(system-audit): Task 18 Sync-Welle — Pipeline-SSoT + §10-Audit + log.md
ab7ae19 chore(docs): Task 17 INSTRUKTIONEN §27.5 Migration-Regression-Guard + Baseline
fa238bf feat(system-audit): Task 16 /SystemAudit slash-command wrapper
486f2c1 test(system-audit): Task 15 temp-repo smoke + seeded-drift integration
ab6b3f5 (baseline) log(task-14): Task 14 System-Audit Optional Checks + Fix-Welle C+D
```

---

## 🎯 Follow-up-Tasks (TodoWrite gepflegt, offen)

- **#2** Check-3 `markdown_header` future-date-exclude (eigener Task, nicht Task-15/17-Bundle). Bug in `03_Tools/system_audit/checks/markdown_header.py:51-63` `_newest_event_date_state` — Future-Dates aus Event-Kandidaten ausschließen. In-process-Fixtures synthetisch → Bug-Trigger erst mit realem Content.
- **#4** vault_backlinks Robustness-Pass (Important #4-7 aus Task-14-Code-Review: stem-collisions, timeout-granularity, SKIP+warning-Mix, dedup). Einzeln deferrable.
- **existence-Cleanup-Welle** (Post-Task-17, ~54 CLAUDE.md-Pfadreferenzen ohne `00_Core/`-Prefix). Quelle: CLAUDE.md oder existence-Check-Logik anpassen.
- **Daily-Persist-Auto-Trigger** (Track 4 ETF/Gold-Erweiterung): Cron/Hook für `portfolio_returns.jsonl` + `benchmark-series.jsonl` — 1 Record seit 17.04. stale.

---

## 🧠 Deferred: Skill-Frage für nach Task 19

Housekeeping-Skill `system-state-guardian` — Opus-Vorschlag 2026-04-21 Abend. Ausgelagert in vorherigen Handover für Persistenz; **Entscheidung weiterhin auf nach Task 19 aufgehoben**.

---

## 🌐 Session-Übergabe-Protokoll

**Vor Session-Clear empfehlenswert:**
1. `!SyncBriefing` ausführen (CLAUDE.md §25) — pushed `00_Core/` ins GitHub-Repo, damit Remote-Trigger (10:00 Morning Briefing) aktuellen Stand liest. **Review-Gate Pflicht** (explizite User-Bestätigung), nicht auto-push. Aktuelle Commits unpushed: `486f2c1`, `fa238bf`, `ab7ae19`, `ca35f62` — und jetziger Handover-Update-Commit.
2. Vault-Noise im Working-Tree bleibt unangetastet (pre-existing `.obsidian/graph.json` + 3 Untracked-Vault-Files vom User).

**Nach Session-Clear — erste Session-Start-Sequenz:**
1. `Session starten` → STATE.md lesen.
2. `superpowers:subagent-driven-development` Skill aktivieren.
3. Handover lesen (diese Datei) — besonders Baseline-Realität + Item-2-Drift-Handling.
4. Plan Task 19 (Plan-Zeilen 3467-3501) lesen.
5. Spec §12 lesen (`docs/superpowers/specs/2026-04-21-system-audit-tool-design.md`).
6. Lageprüfung-Command-Block oben ausführen.
7. Task 19 in_progress setzen.
8. Acceptance-Matrix abhaken (Evidence-Commands pro Item ausführen, Drift-Notes dokumentieren für Item 2).
9. Codex-Pass dispatchen (via `codex:rescue` Fresh-Thread).
10. CodeRabbit-Pass via WSL.
11. Fix-Welle falls Findings.
12. Final-Commit Task 19.
13. Optional: Briefing-Sync abschließen falls noch offen.
