# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-21 Abend-Spät (**Phase E 13/19 Tasks done** — Task 13 CLI-Orchestrator + Fix-Welle B + Pre-Task-14-Hygiene committed. **Next: Task 14** Optional Checks 8/9 Vault-Backlinks + Status-Matrix).
**Vorherige Aktualisierungen:** 2026-04-21 Abend — Fix-Welle A (`7cea0e0`) · 2026-04-21 Nachmittag-Spät — Spec v0.2 ratified (`82482d7`).

> **Progress-Banner (Phase A-G):** ✅ A+B+C (Sync-Welle `8acb13c`) · ✅ D (Spec v0.2 `82482d7`) · 🟡 **E 13/19** (Tasks 1-13 done, 14-19 open) · ⏳ F (Provenance-Plan-Execution) · ⏳ G (TMO Q1 23.04.).

## 🚀 NÄCHSTE SESSION — Direkter Einstieg

**Trigger:** `Session starten` → STATE.md lesen → `superpowers:subagent-driven-development` + `superpowers:test-driven-development` Skills aktivieren → TodoWrite zeigt 13 completed, 6 pending → **Task 14 in_progress setzen** → Plan-Lesen Zeilen 2829-3107.

**Command zur schnellen Lageprüfung:**
```bash
cd "C:\Users\tobia\OneDrive\Desktop\Claude Stuff"
python 03_Tools/system_audit/_smoke_test.py           # muss 12/12 [OK] zeigen
python 03_Tools/backtest-ready/schemas.py             # muss "all schema smoke tests passed"
python 03_Tools/system_audit.py --core --no-write     # rc=1 (echte Drift, nicht Tool-Bug) erwartet
git log --oneline 34090f2..HEAD | head -10            # 3 neue Commits (Task 13 + Fix-B + hygiene)
git status --short                                    # clean auf Tool-Seite
```

---

## 📋 Was in Session 21.04. Abend-Spät passiert ist

**Task 13 vollständig abgeschlossen mit 4-Wege-Review (advisor + Claude + Codex + CodeRabbit-CLI + User-Final)** — ersten echten End-to-End-Test des Review-Stacks nach `feedback_review_stack.md`-Matrix.

| Commit | Inhalt |
|--------|--------|
| `4a9168e` | feat: CLI-Orchestrator `03_Tools/system_audit.py` (advisor-gehärtet, 247 LOC) + 5 Smoke-Tests |
| `4dc8825` | fix: Fix-Welle B — 9 Review-Findings via TDD RED-GREEN-REFACTOR + Red-Green-Verify-Cycle (stash-revert → MUST FAIL → restore → PASS) |
| `0dbd8f2` | chore: Pre-Task-14-Hygiene — 6 CodeRabbit-Quick-Wins + 3 Header/Footer-Stand-Drifts gefixt + fullcode.txt gelöscht |

**Fix-Welle-B-Findings umgesetzt (Details `4dc8825`):** E (rc=2 Partial-Output), A (Thread-Leak-Docstring), B (float vault_timeout_s), F (category aus Registry), C (scope_label-drop), L (datetime.UTC), CR-1 (rc-check vor json.loads), CR-2 (Return-Type-Hint), K (duration-budget rc-assertion).

**Hygiene-Welle (Details `0dbd8f2`):** CodeRabbit-CLI Quick-Wins (`Callable`/`Sequence` aus `collections.abc`, `contextlib.suppress`, unquoted return type, `__all__` alphabetisch, coding-decl raus), Header/Footer-Stand-Drift über 3 `00_Core/`-Files.

---

## 🎯 Task 14 — Pre-Notes + User-5-Punkte-Ausfalloffene

**Task 14 (Plan 2829-3107):** Optional Checks 8/9 — Vault-Backlinks + Status-Matrix. 20s Timeout, 6 Fixtures (Codex-P5).

**Session-Start Pflicht-Quick-Win (User-Finding 2, 2026-04-21):**

`03_Tools/system_audit/checks/jsonl_schema.py:83` nutzt `model.model_validate(json.loads(line))` — doppeltes Parsing-Anti-Pattern. Pydantic v2 `model_validate_json(line)` macht beides rust-nativ in einem Pass. ~2 Min Fix, bestehender Test `test_jsonl_schema_fail_on_bad_fixture` ist das Safety-Net. Bonus: `json.JSONDecodeError` wird zu `ValidationError type='json_invalid'` (einheitliche Fehlerbehandlung).

**Check-8-Time-Monotonic-Gate (User-Finding 3, 2026-04-21):**

Bei Task-14-Implementation Check-8 Vault-Backlinks mit `time.monotonic()` Start-Ende-Messung einbauen. Zwei Pragma-Gates für Live-Run-Entscheidung:
- **<5s live-run** → sync-Implementation bleibt, keine Aktion.
- **>10s** → **Task-15-Backlog: subprocess-Isolation mit hard-kill-Timeout** (deckt sich mit Daemon-Thread-Docstring-Notiz aus Fix-Welle B Finding A).

**Check-10-Kandidat (neu aus Hygiene-Welle 21.04. Abend-Spät):**

`header_footer_stand_consistency` — Scan aller `00_Core/*.md` nach Header-`**Stand:**` und Footer-`Stand:` (unter 🦅-Sentinel), flag wenn beide vorhanden + unterschiedlich. Heutige Drift-Welle deckte 3/5 Files auf (CORE-MEMORY 4d, INSTRUKTIONEN 1d, KONTEXT 13d). Trivial via Regex implementierbar, <50 LOC. Entscheidung: als Check-10 in Task 14 mit einbauen ODER als eigenen Mini-Task nach Task 14.

---

## 🧠 User-5-Punkte-Session-Diskussion (2026-04-21 Abend-Spät)

User brachte 5 technische Punkte nach Task-13-Abschluss ein, validiert via CodeRabbit-CLI-Run gegen `schemas.py` + `jsonl_schema.py` (Commit `0dbd8f2` lesbar).

**Kalibrierungs-Outcome:** CodeRabbit-CLI flaggte weder Punkt 1 noch Punkt 2 — Domain-Pattern-Detection ist schwach bei CLI, stark bei Syntax-Idiomen. Learning in `coderabbit_cli_via_wsl.md` Memory persistiert.

| Punkt | Thema | Status | Handoff-Action |
|-------|-------|--------|----------------|
| 1 | `float → Decimal` für PortfolioReturnRecord + Position + BenchmarkReturnRecord | **Backlog mit Deadline 2027-10-19** (R5-Interim-Gate 18-Mo-Dry-Run braucht exakte Zahlen für Sharpe/Sortino/Beta) | Eigener kurzer Migration-Plan ~1 Session; blockt nicht Task 14-19. STATE.md Long-Term-Gate-Eintrag nachtragen. |
| 2 | `model_validate_json()` statt `json.loads + model_validate` | **Pflicht-Quick-Win Session-Start** | Siehe oben. |
| 3 | Async/Detached für Check-8 (Vault-Scaling) | **Conditional — Time-Monotonic-Gate** | Siehe oben. |
| 4 | Context Eviction + Exit-Code-Kontrakt | Bestätigung meiner Choices, keine Aktion | — |
| 5 | HTML-Marker + frozen=True | Bestätigung meiner Choices, keine Aktion | — |

---

## 📊 Commit-Graph (seit letztem Handover `34090f2`)

```
0dbd8f2 chore(hygiene): pre-Task-14 cleanup — CodeRabbit-CLI Quick-Wins + Stand-Sync
4dc8825 fix(system-audit): Fix-Welle B — Codex + CodeRabbit-CLI 4-Wege-Review-Findings
4a9168e feat(system-audit): CLI orchestrator --core/--full/--vault/--minimal-baseline
34090f2 (baseline) handover(phase-e-mid): Tasks 1-12 + Fix-Welle A
```

---

## 🎯 Remaining Tasks 14-19 (Phase E Abschluss)

- **14 Optional Check-8/9** `vault_backlinks` + `status_matrix` (Plan 2829-3107). Pre-Actions: (a) Session-Start-Quick-Win `model_validate_json`, (b) Time-Monotonic-Gate für Check-8, (c) ggf. Check-10 `header_footer_stand_consistency` mit einbauen.
- **15 Smoke-Test temp-repo-copy** (Plan 3109-3246). Spec §7.4.
- **16 Slash-Command `/SystemAudit`** (Plan 3248-3299).
- **17 INSTRUKTIONEN §27.4 Regression-Guard + Live-Baseline-Run** (Plan 3301-3370). Task-17-Baseline-Scope-Entscheidung (A/B aus ursprünglichem Handover): **A pragmatisch** (`--minimal-baseline` als Gate — 3 Checks strukturelle Integrity). Die ~135 existence-FAILs werden per Tool in Follow-up-Welle aufgeräumt.
- **18 Pipeline-SSoT + CORE-MEMORY + log.md + Briefing-Sync** (Plan 3372-3436).
- **19 Verification-Before-Completion Acceptance-Matrix** (Plan 3438-Ende, Spec §12). **Zweiter obligatorischer 4-Wege-Review-Pass** (Matrix-Zeile "Meilenstein/PR-Abschluss = BEIDE sequenziert").

---

## 🧠 Deferred: Skill-Frage für nach Task 19

Housekeeping-Skill `system-state-guardian` — Opus-Vorschlag aus User-Parallelgespräch 2026-04-21 Abend. Kernpunkte: (a) Kategorie Housekeeping (Meta-Ebene, analog skill-creator), NICHT Analyse-Pipeline. (b) Strikte Trennung: Housekeeping wartet State, Analyse-Skills benutzen State. (c) Aktivierungspfade: Session-Start Silent-Mode, `!HygieneCheck` manuell, nach skill-creator-Modifikationen. NICHT aus dynastie-depot heraus. (d) Auto-Fix-Whitelist vs User-Eskalation hart definiert. (e) Audit-Trail `hygiene_log.jsonl`. (f) Dry-Run-Pflicht erste 2-4 Wochen. (g) Erst Python-API einfrieren → dann SKILL.md als dünne Kapsel drüber.

**Entschieden:** Skill-Entscheidung **auf nach Task 19 aufgehoben.** Ausgelagert in diesen Handover für Persistenz über Sessions.
