# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-21 Nacht (**Phase E 14/19 Tasks done** — Task 14 Optional Checks 8/9 + Fix-Welle C committed; 2 Blocker + 1 Important aus Code-Review behoben, 4 Important-Findings deferred als Follow-up-Task).
**Vorherige Aktualisierungen:** 2026-04-21 Abend-Spät — Task 13 (`4a9168e`/`4dc8825`/`0dbd8f2`) · 2026-04-21 Abend — Fix-Welle A (`7cea0e0`) · 2026-04-21 Nachmittag-Spät — Spec v0.2 ratified (`82482d7`).

> **Progress-Banner (Phase A-G):** ✅ A+B+C (Sync-Welle `8acb13c`) · ✅ D (Spec v0.2 `82482d7`) · 🟡 **E 14/19** (Tasks 1-14 done, 15-19 open) · ⏳ F (Provenance-Plan-Execution) · ⏳ G (TMO Q1 23.04.).

## 🚀 NÄCHSTE SESSION — Direkter Einstieg

**Trigger:** `Session starten` → STATE.md lesen → `superpowers:subagent-driven-development` + `superpowers:test-driven-development` Skills aktivieren → **Task 15 in_progress setzen** → Plan-Lesen Zeilen 3117-3246 (Smoke-Test gegen temp-repo-copy, Spec §7.4).

**Command zur schnellen Lageprüfung:**
```bash
cd "C:\Users\tobia\OneDrive\Desktop\Claude Stuff"
python 03_Tools/system_audit/_smoke_test.py           # muss 14/14 [OK] zeigen (Task 14: vault_backlinks + status_matrix dazugekommen)
python 03_Tools/backtest-ready/schemas.py             # muss "all schema smoke tests passed"
python 03_Tools/system_audit.py --full --no-write     # rc=1 (echte Drift), Check-1..10 alle laufen
git log --oneline 34090f2..HEAD | head -15            # 6 neue Commits (Task 13 + Fix-B + hygiene + Task 14 + Fix-C + state-long-term-gate)
git status --short                                    # clean auf Tool-Seite (Vault-Noise kann bleiben)
```

---

## 📋 Was in Session 21.04. Nacht passiert ist (Task 14 done)

**Task 14 vollständig abgeschlossen mit 3-Wege-Review (Implementer-Subagent + Spec-Review + Code-Quality-Review → Fix-Welle C → Re-Review APPROVED).** TDD RED→GREEN durchgezogen auch in Fix-Welle (failing regression tests first).

| Commit | Inhalt |
|--------|--------|
| `6926f58` | docs(state): float→Decimal Migration Long-Term-Gate 2027-10-19 (User-Punkt 1) |
| `68d58ab` | fix: Fix-Welle C — Code-Review Blocker #1 (Status-Matrix Prose-Match false-negative, jetzt Header-anchored + level-aware terminator) + Blocker #2 (n_passed = len(numbers) - len(dup_numbers) statt - len(failures)) + Important #3 (jsonl_schema json_invalid-Hint differenziert gegen Schema-Drift). 4 neue Regression-Tests (smoke 14/14). |
| `510cbbf` | feat: Check-8 vault_backlinks + Check-9 status_matrix (optional) — TDD RED-GREEN via Implementer-Subagent. Live duration Check-8 = 29ms → <5s-Gate PASS. Orchestrator `--vault`-Filter-Bug (pre-existing) als Korrektheits-Prereq mit-gefixt. jsonl_schema model_validate_json-Quick-Win (Task-1 Pflicht) gebundled. |

**Session-Start Pflicht-Quick-Win (Task-1) erledigt:** `json.loads + model_validate` → `model_validate_json` in `jsonl_schema.py`. Bonus-Fix in Fix-Welle C: `json_invalid` type-branch für differenzierten Hint.

**Code-Review-Outcome:** 2 Blocker + 5 Important/Nit gefunden. 2 Blocker + Important #3 sofort gefixt. Important #4-7 (vault_backlinks: stem-collisions / timeout-granularity / SKIP+warning-Mix / dedup) deferred als Task #4 `Follow-up: vault_backlinks Robustness-Pass` — einzeln deferrable, nicht Task-14-blocking.

**Deferred-Entscheidung Check-10 `header_footer_stand_consistency`:** NICHT in Task 14 gebundled — bleibt Mini-Task nach Task 19. Begründung: Task 14 Scope ist in Spec §5.2 auf Checks 8/9 gepinnt, Check-10 wäre Spec-Drift ohne neuen Advisor-Durchgang.

**Fix-Welle-C-Details (`68d58ab`):**
- Blocker #1: `HEADER_RE = r"^#{1,6}\s+...Status-Matrix...$"` + `term_pattern` dynamisch level-aware (Heading-Level aus matched line extrahiert, Terminator matched nur gleiche-oder-höhere Levels ohne "Status-Matrix").
- Blocker #2: `n_passed = len(numbers) - len(dup_numbers)` (gap-failures referenzieren B-Nummern die gar nicht in `numbers` sind → dürfen nicht abziehen). `collections.Counter` ersetzt O(n²)-count-Loop.
- Important #3: `is_json_error = errs[0].get("type") == "json_invalid"` → hint differenziert "Record manuell pruefen / entfernen" vs "Migration-Helper".
- 4 neue Regression-Fixtures: `test_status_matrix_header_anchored_not_prose_match`, `test_status_matrix_subsections_are_scanned`, `test_status_matrix_n_passed_arithmetic_with_gaps`, `test_jsonl_schema_malformed_json_hint`.

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

## 🎯 Remaining Tasks 15-19 (Phase E Abschluss)

- ✅ **14 Optional Check-8/9** `vault_backlinks` + `status_matrix` — committed `510cbbf` (TDD-Build) + `68d58ab` (Fix-Welle C: 2 Blocker + Important #3 aus Code-Review). Live-duration Check-8 = 29-32ms → Task-15-subprocess-isolation NICHT nötig (<5s-Gate). Deferred: Task #4 (vault_backlinks Robustness-Pass für Important #4-7 aus Code-Review — stem-collisions, timeout-granularity, SKIP+warning semantics, dedup — einzeln deferrable).
- **15 Smoke-Test temp-repo-copy** (Plan 3109-3246). Spec §7.4.
- **16 Slash-Command `/SystemAudit`** (Plan 3248-3299).
- **17 INSTRUKTIONEN §27.4 Regression-Guard + Live-Baseline-Run** (Plan 3301-3370). Task-17-Baseline-Scope-Entscheidung (A/B aus ursprünglichem Handover): **A pragmatisch** (`--minimal-baseline` als Gate — 3 Checks strukturelle Integrity). Die ~135 existence-FAILs werden per Tool in Follow-up-Welle aufgeräumt.
- **18 Pipeline-SSoT + CORE-MEMORY + log.md + Briefing-Sync** (Plan 3372-3436).
- **19 Verification-Before-Completion Acceptance-Matrix** (Plan 3438-Ende, Spec §12). **Zweiter obligatorischer 4-Wege-Review-Pass** (Matrix-Zeile "Meilenstein/PR-Abschluss = BEIDE sequenziert").

---

## 🧠 Deferred: Skill-Frage für nach Task 19

Housekeeping-Skill `system-state-guardian` — Opus-Vorschlag aus User-Parallelgespräch 2026-04-21 Abend. Kernpunkte: (a) Kategorie Housekeeping (Meta-Ebene, analog skill-creator), NICHT Analyse-Pipeline. (b) Strikte Trennung: Housekeeping wartet State, Analyse-Skills benutzen State. (c) Aktivierungspfade: Session-Start Silent-Mode, `!HygieneCheck` manuell, nach skill-creator-Modifikationen. NICHT aus dynastie-depot heraus. (d) Auto-Fix-Whitelist vs User-Eskalation hart definiert. (e) Audit-Trail `hygiene_log.jsonl`. (f) Dry-Run-Pflicht erste 2-4 Wochen. (g) Erst Python-API einfrieren → dann SKILL.md als dünne Kapsel drüber.

**Entschieden:** Skill-Entscheidung **auf nach Task 19 aufgehoben.** Ausgelagert in diesen Handover für Persistenz über Sessions.
