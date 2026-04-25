# Codex-Reconciliation-Report — 00_Core-Refactor Tier 2

**Datum:** 2026-04-25 (Session 7, Step 9.2-9.3)
**Branch:** `refactor/00core-perfect-organization`
**Baseline:** `db50ff0` (= `git merge-base main HEAD`)
**HEAD:** `a094da2`
**Spec:** `docs/superpowers/specs/2026-04-24-00core-perfect-organization-design.md` v0.4
**Plan:** `docs/superpowers/plans/2026-04-24-00core-perfect-organization.md`
**Subagent:** `codex:codex-rescue` (agentId `a8fae07ad0c6c0c47`)

**Commits reviewed (12):**
```
a094da2 handover: Session-6-Ende — Tasks 7+8 CLOSED, Task-9 Resume-Input
7ee1b61 verify(refactor): Task-8 Smoke-Sweep + Artefakt-Gate
0e45989 refactor(narratives): post-migration drift-fix CORE-MEMORY §3 + KONTEXT §Layer
f66b622 build(skills): Task-7 Skill-Paket-Build — Legacy-Archive README-Entry
d5bb4ed handover: Session-5-Ende — Tasks 4+5+6 CLOSED, Task-7 Resume-Input
9cce107 refactor(governance): Task-6 CLAUDE.md + INSTRUKTIONEN §18/§25/§27.3/§27.4
a404012 refactor(skills+peers): Task-5 Content-Patches + Peer-Verweise-Header
469f5af refactor(scripts): Task-4 Tool-Patches für 00_Core-Split
60b2882 handover: Session-3-Ende — Task-3 CORE-MEMORY closed, Task-4 Resume-Input
326fa42 refactor(00core): Task-3 CORE-MEMORY §1→§12/§13 Topic-Auflösung
f798f0a refactor(00core)!: Task-2 STATE-Split (Phase 1/2 des Spec §8.2 Cutovers)
42b9905 feat(00core): Task-1 Satelliten-Skelette (PORTFOLIO/PIPELINE/SYSTEM)
```

---

## VERDICT: RECONCILED_WITH_FOLLOWUPS

## Findings

### F1 [🟡 Should]

**Datei:Zeile:** `00_Core/TOKEN-RULES.md:23-24`; `docs/superpowers/specs/_artifacts/2026-04-24-post-migration-refs.txt:83-85,207,215`

**Problem:** `TOKEN-RULES.md` enthält noch pre-split Operativtext (`STATE.md + Faktortabelle vor API`, `alle sechs … + STATE.md`), obwohl der Refactor `PORTFOLIO.md` als Live-State und §18 v2 als trigger-basiertes Mapping etabliert. Das AC-#15-Artefakt klassifiziert diese Treffer pauschal als erlaubte "Pointer-Refs" und bewertet AC #15 dadurch zu optimistisch.

**Recommended-Fix:** `TOKEN-RULES.md` auf `PORTFOLIO.md`/§18-v2 umstellen und danach `2026-04-24-post-migration-refs.txt` neu erzeugen; AC #15 erst nach korrigierter Deny/Allow-Klassifikation als PASS werten.

---

## Spec-Drift-Summary

Kleine Drift: operative Token-Regel referenziert noch die alte STATE-/6-File-Logik. Die Kernarchitektur aus Spec §§5-8 ist sonst umgesetzt: Hub/PORTFOLIO/PIPELINE/SYSTEM existieren, CORE-MEMORY hat §12/§13 korrekt, CLAUDE/INSTRUKTIONEN §18 v2 sind in der Hauptführung konsistent.

## Info-Loss-Summary

Kein konkreter Info-Loss im Zielstand sichtbar: `PORTFOLIO.md` enthält 11 Satelliten, Watches und 30-Tage-Trigger; `PIPELINE.md` enthält Items #1-#13 plus Long-Term-Gates; `SYSTEM.md` enthält DEFCON/MCP/Briefing/Backtest/R5/§30/Backlog. Vollvergleich gegen `git show db50ff0:00_Core/STATE.md` bleibt **unverified** — Git-Objektzugriff auf den Baseline-Commit war in der Codex-Sandbox blockiert.

## Invariant-Summary

- Hub-Last-Audit-Markers OK (`00_Core/STATE.md:28,38`).
- Footer-Sentinels OK (`00_Core/STATE.md:40`, `PORTFOLIO.md:57`, `PIPELINE.md:63`, `SYSTEM.md:39`, `CORE-MEMORY.md:516`).
- Script-Pfade OK (`03_Tools/backtest-ready/_forward_verify_helpers.py:25`, `03_Tools/system_audit/checks/pipeline_ssot.py:48-54`, `cross_source.py:195,252`, `existence.py:50-53`, `03_Tools/briefing-sync-check.ps1:35-38`).

## AC-Verification

- AC #1 PASS
- AC #2 PASS
- AC #3 PASS
- AC #4 PASS
- AC #5 PASS
- AC #6 PASS
- AC #7 PASS
- AC #8 PASS
- AC #9 PASS
- AC #10 PASS
- AC #11 PASS
- AC #12 PASS
- AC #13 PASS
- AC #14 PASS
- AC #15 **FAIL** — stale `TOKEN-RULES.md`-Zeilen wurden als allow-listed missklassifiziert; tatsächlich Drift zu §18 v2. **Fix in F1 → AC #15 nach TOKEN-RULES-Patch + Refs-Neu-Lauf re-verifiziert.**
- AC #16 **FAIL** — Required review artifacts (`codex-reconciliation-report.md`, `coderabbit-findings.md`, `user-signoff.md`) und Merge-Commit-Evidenz sind noch nicht vollständig in `_artifacts/` vorhanden. **Erwartet:** wird durch Step 9.3 (dieses Artefakt), 9.6 (CR-Findings), 9.7 (Sign-off), 9.9-9.10 (Merge-Commit-Body) sequenziell aufgelöst.
- AC #17 PASS
- AC #18 PASS

---

## Resolution-Plan (Claude, Step 9.4)

- F1 🟡 Should: **inline fixen** (Plan-Konvention für Should-Findings).
  - Patch `00_Core/TOKEN-RULES.md` L23-24 (Snapshot-First → PORTFOLIO; Sync-Pflicht → §18 v2 Trigger-Mapping mit Verweis statt 6er-Liste).
  - Regenerate `docs/superpowers/specs/_artifacts/2026-04-24-post-migration-refs.txt` nach dem Patch.
  - Re-Lauf Codex optional (nur 1 Should-Finding, kein Blocker — Plan: nach Fix-Commit als RECONCILED weiterführen).
- AC #16 wird durch nachfolgende Steps erfüllt (kein Codex-Followup, sondern Plan-Architektur).

**Folgende Commits adressieren F1:**
- `fix(refactor): Codex-F1 TOKEN-RULES §18 v2 + Snapshot-First PORTFOLIO`
