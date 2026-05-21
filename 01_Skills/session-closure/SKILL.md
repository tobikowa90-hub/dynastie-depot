---
name: session-closure
version: "0.2.0"
Stand: "2026-05-21"
description: >
  Orchestriert den Session-End-Workflow im Dynastie-Depot: scannt git-State,
  klassifiziert untracked/modified Files (scoring-relevant vs. doc-only vs.
  code vs. meta), prüft §18-Sync-Coupling, bündelt kohärente Commits mit
  korrekten Banner-Konventionen, führt sie autonom aus, hält STRIKT vor
  `git push` (Hard-Stop, User-Freigabe nötig), pusht nach Approval, verifiziert
  Working-Tree clean + origin-sync, und gibt strukturierten Closure-Report.
  Strict-Trigger: `!SessionClose`. Kein Fuzzy-Match, keine Phrasen-Auto-Activation
  (vgl. CLAUDE.md Trigger-Strictness). Verwende diesen Skill, wenn der User
  `!SessionClose` eingibt — und NUR dann. Bei phrasen-basierten Wünschen wie
  "Session beenden" / "push & weg" / "fertig für heute" zuerst rückfragen, ob
  `!SessionClose` gemeint ist.
trigger_words: ["!SessionClose"]
---

# session-closure — Skill v0.2.0

**Strict-Trigger:** `!SessionClose`. Keine Fuzzy-Matches, keine Phrasen-Aktivierung.
Bei sinngemäßen User-Aussagen ("Session beenden", "push & weg") **zuerst nachfragen**,
ob `!SessionClose` gemeint ist (CLAUDE.md Edge-Case-Regel, identisch zu `!Analysiere`).

**Zweck:** Konsistente, sichere Session-Beendigung — eliminiert das Re-Derivieren
von Commit-Reihenfolge, Banner-Wahl, §18-Sync-Coupling und Push-Sicherheit aus
Memory-Snippets jede Session neu (Reinfall-Doku: `feedback_pre_commit_diff_inspection.md`,
`feedback_multi_commit_wip_resume.md`, `feedback_powershell_herestring_in_bash_tool.md`).

**Sicherheits-Boundary:** Skill macht Commits autonom (lokal reversibel via
`git reset --soft`). Skill macht **niemals** `git push` ohne explizite User-Freigabe
nach Plan-Präsentation.

---

## 1. Authoritative Sources (nicht inlinen)

| Quelle | Verwendung |
|--------|-----------|
| `00_Core/INSTRUKTIONEN.md §18` | Sync-Pflicht-Set bei Score/FLAG/Sparraten-Change (8 Files + xlsx-Tools) |
| `00_Core/INSTRUKTIONEN.md §18.7` | xlsx-Smoke-Test fail-close vor `git add` |
| `00_Core/INSTRUKTIONEN.md §19.1` | Earnings-Call-Wait-Discipline (Tag 0 vs Tag +1) |
| `00_Core/INSTRUKTIONEN.md §25` | Briefing-Sync (`!SyncBriefing` falls 00_Core/ geändert) |
| `references/commit-banners.md` | Banner-Konventionen + Beispiele aus Commit-History |
| `references/file-classification.md` | Klassifikations-Matrix (scoring-relevant/doc-only/code/meta) |
| `references/sync-coupling.md` | §18-Coupling-Check-Regeln + Refuse-Conditions |
| `references/push-safety.md` | Pre-push-Checks (ahead/behind, rebase-in-progress, force-detection) |

**Drift-Prevention:** Sync-Set + Schwellenwerte leben in INSTRUKTIONEN.md (SSoT).
Skill referenziert, dupliziert nicht. Bei INSTRUKTIONEN-Änderung Skill nicht
zwingend mit-anpassen (außer Banner-Konvention oder Coupling-Logik tangiert).

---

## 2. Workflow

### Schritt 0 — Pre-Flight (refuse-conditions)

Vor allem anderen prüfen. Bei Treffer: Skill **bricht ab** mit klarer Begründung,
keine Mutation. Nutzer kann manuell weitermachen oder Bedingung auflösen.

- **Rebase/Merge in progress:** `git status` → `rebase in progress` / `unmerged paths` → REFUSE.
- **Detached HEAD:** Branch-Status nicht `main` und nicht offensichtlich Feature-Branch → REFUSE mit Hinweis.
- **§19.1 Tag-0-Trap:** Wenn `CORE-MEMORY §12.<ticker>` einen Pre-Call-Snapshot heute hat UND `score_history.jsonl` heute mutiert wurde UND es ist **Tag 0** (Call heute Abend, kein Transcript verfügbar) → REFUSE. Tag-0-FLAG-Events ohne Score-Move sind ok.

  **Issuer-Ausnahmen** (Tag 0 = legitime Vollanalyse, KEIN Refuse):
  - **BRK.B** — kein Quarterly Earnings Call; Trigger ist 10-Q-Filing-Tag direkt (Memory `feedback_brk_no_earnings_call.md`).
  - **Non-US mit Trading-Update-Pattern** (z.B. SU/Schneider Electric, RMS/Hermès): Q1/Q3 sind `trading_update`-Releases ohne Call, Q2/Q4 sind volle Half-Year-Reports. Bei `trading_update`-Quarter: Tag 0 = Vollanalyse-Tag (per §19.1 Override-YAML).
  - Konkret prüfen: `01_Skills/dynastie-depot/config.yaml` Feld `earnings_trigger` je Ticker (Werte: `quarterly_call` / `10q_filing` / `trading_update_q*`). Nur bei `quarterly_call` greift die Tag-0-Refuse-Logik.
- **Ahead+behind origin:** Branch ist `ahead N, behind M` → REFUSE (User muss pull/rebase manuell entscheiden, §0 Karpathy-Regel "investigate before destructive").

### Schritt 1 — State-Scan

Parallel ausführen, Output strukturieren:

```bash
git status --short
git log --oneline origin/main..HEAD
git diff --stat HEAD
```

Daraus extrahieren:
- **Unpushed-Commits** (bereits committed, warten auf push)
- **Staged-Files** (im index, noch nicht committed)
- **Modified-Tracked** (geändert, nicht staged)
- **Untracked** (neue Files)

### Schritt 2 — Klassifikation

Für jeden Modified-/Untracked-File die **Kategorie** bestimmen via
`references/file-classification.md`. Vier Kategorien:

1. **scoring-relevant** — `score_history.jsonl`, `PORTFOLIO.md`, `Faktortabelle.md`, `CORE-MEMORY.md`, Vault `log.md`, `01_Skills/dynastie-depot/config.yaml`, `03_Tools/Rebalancing_Tool_v3.4.xlsx`, `03_Tools/Satelliten_Monitor_v2.0.xlsx`, `05_Archiv/flag_events.jsonl`
2. **doc-only** — `02_Analysen/Earnings Reports/**`, Vault-Notes, PDFs, Transkripte, Recherche-Materialien
3. **code** — `03_Tools/**.py`, `01_Skills/**` (außer config.yaml), `06_Skills-Pakete/**`
4. **meta** — `00_Core/**`, `CLAUDE.md`, `INSTRUKTIONEN.md`, `SYSTEM.md`, `PIPELINE.md`, `STATE.md`, `04_Templates/**`

### Schritt 3 — Sync-Coupling-Check

Per `references/sync-coupling.md`:

- Wenn **Score-Event** (`score_history.jsonl` heute mutiert/appended): **alle 8 §18-Sync-Set-Files** müssen entweder im aktuellen Staging oder in unpushed-Commits derselben Session vorliegen. Files 1-6 atomar in einem Commit, xlsx-Tools (7+8) dürfen separater Commit derselben Push-Welle sein. Fehlt einer → REFUSE mit Liste der fehlenden Files. (`PORTFOLIO.md` allein ohne `score_history.jsonl` ist erlaubt — Live-State-Edit ohne Score-Event.)
- Wenn **xlsx** mutiert (egal welches der drei Tools): §18.7 Smoke-Test muss seit letztem `openpyxl`-Write gelaufen sein. Nicht prüfbar deterministisch → **Frage User explizit** ("xlsx-Smoke-Test für `<file>` gelaufen? y/n"). Bei "n" REFUSE.
- Wenn **KONTEXT §6** mutiert: `Watchlist_Ersatzbank_Monitor_v1.1.xlsx` muss mit-mutiert sein (kontext-coupled, nicht Score-coupled). Fehlt → REFUSE.
- Wenn **00_Core/** mutiert UND Briefing-deploy-relevant: erinnere an `!SyncBriefing` (§25), aber blockiere nicht.

### Schritt 4 — Commit-Plan erstellen

Files in **kohärente Commit-Gruppen** bündeln. Eine Gruppe = ein Commit. Heuristik:
- Scoring-relevant + Sync-Set zusammen = **1 Commit** (Score-Event-Bundle).
- xlsx separat möglich, aber **gleiche Session** pflicht (CLAUDE.md §18 ausdrücklich).
- Doc-only-Bundles (z.B. Earnings-Materials für einen Ticker) = **1 Commit pro Bundle**.
- PIPELINE-Items = **1 Commit pro Item** (Numbering-Convention).
- Code-Changes separat von doc-only.

Banner-Wahl per `references/commit-banners.md`. Häufige Pattern:
- `chore(repo): <kurzdesc>` — doc-additions, source-materials
- `chore(meta): PIPELINE #N <action> (scoring-neutral)` — Pipeline-Cleanups
- `chore(meta): §X.Y <action> (scoring-neutral)` — Spec-Edits
- `feat(<scope>): <desc>` — neue Funktionalität
- `fix(<scope>): <desc>` — Bugfix

**Plan dem User präsentieren:** Liste aller geplanten Commits (Banner + File-Count + 1-Liner-Begründung). Bei Multi-Commit-Session ist **eine Plan-Approval ok**, kein Hard-Stop pro Commit nötig. **Aber:** Wenn die Klassifikation unklar oder die Banner-Wahl mehrdeutig, **frage** statt zu raten.

### Schritt 5 — Commits ausführen

Pro Commit-Gruppe:
1. `git add <files>` — exakt die Files der Gruppe, kein `git add -A` (Reinfall-Doku `feedback_pre_commit_diff_inspection.md`).
2. `git diff --cached --stat` — verify staged set matches plan.
3. `git commit -F -` mit Heredoc (Reinfall-Doku `feedback_powershell_herestring_in_bash_tool.md`: `@'...'@` ist PowerShell-only und korrumpiert via Bash-Tool den Subject).
4. Bei pre-commit-hook-Fail: **NIE** `--amend`. Issue fixen, re-stage, **neuen** Commit erstellen (CLAUDE.md git-safety + Memory `feedback_multi_commit_wip_resume.md`).
5. `git log -1 --format='%s' | cat -A` — Byte-Check des Subjects (kein lone `@`, kein CRLF).

Wenn alle Commits durch: weiter zu Schritt 6. Bei Hook-Fail oder unexpected error: **STOP** und User informieren.

### Schritt 6 — HARD-STOP: Push-Plan

Bevor `git push`:

```
PUSH-PLAN
=========
Branch: main → origin/main
Commits to push:
  <sha1> chore(meta): PIPELINE #X ... (scoring-neutral)
  <sha2> chore(repo): ...
Working tree: clean
Pre-push checks: pass (ahead-only, no force, no tags)

Push? [warte auf "go" / "push" / "ja"]
```

**Skill macht KEIN `git push` ohne explizites Go.** "go", "push", "ja", "ok push" zählen. Bei Unsicherheit oder anderen Antworten: nachfragen, nicht pushen.

### Schritt 7 — Push + Verify

Nach User-Go:

```bash
git push origin main
git status                       # expect: nothing to commit, working tree clean
git log --oneline origin/main..HEAD  # expect: empty (synced)
```

Bei push-Fehler (rejected, force needed, network): **STOP**, Output zeigen, User entscheidet.

### Schritt 8 — Closure-Report

```
SESSION CLOSURE COMPLETE
========================
Pushed: <N> commits (<sha-list>)
Working tree: clean
origin/main: synced
Reminders:
  - [ ] !SyncBriefing if 00_Core/ touched and not synced (§25)
  - [ ] CORE-MEMORY §12 update if score event today
  - [ ] /clear approved when ready

Status: ✅ Ready for /clear
```

Falls Reminder-Bedingungen nicht zutreffen, Bullet weglassen. Status-Zeile immer.

---

## 3. Out-of-Scope (bewusst nicht hier)

- **Inhaltliche Commit-Message-Drafts** (außer Banner-Wahl). User formuliert oder Skill macht 1-Liner aus File-Klassifikation. Multi-Paragraph-Bodies nur auf explizite Anfrage.
- **§18-Sync-Set selbst mutieren.** Skill prüft Vollständigkeit, schreibt aber nicht. Sync-Writes laufen via dynastie-depot Schritt 7 + backtest-ready-forward-verify.
- **xlsx-Smoke-Tests selbst ausführen.** Skill fragt nach Bestätigung, ruft `03_Tools/xlsx-smoke-test.md` nicht aktiv auf. (Future-Option: §18.7-Runner-Skill, separater Scope.)
- **Tag-+1-Earnings-Vollanalyse triggern.** Skill refused nur Tag-0-Falle, plant keine Folge-Session.
- **`!SyncBriefing` selbst ausführen.** Skill erinnert nur, falls 00_Core/ touched.

---

## 4. Trigger-Strictness (CLAUDE.md-konform)

| User-Input | Skill-Reaktion |
|------------|----------------|
| `!SessionClose` | Aktivieren, Workflow starten |
| `Session beenden` / `push & weg` / `fertig für heute` / `feierabend` | **Nicht aktivieren**, sondern: "Meintest du `!SessionClose`?" — User muss explizit bestätigen |
| `!Sessionclose` / `!sessionclose` / `!SesionClose` (Case-Drift / Typo) | **Nicht aktivieren**, Rückfrage |
| `!SessionClose <args>` (Argumente) | Aktivieren, Args ignorieren (Skill nimmt keine) |
| Während laufender `!Analysiere`-Session | Nicht aktivieren, bis Analyse abgeschlossen (Conflict-State) |

Begründung: CLAUDE.md "Tippfehler / fast-exakte Trigger / Case-Drift / Sprach-Varianten: Kein Fuzzy-Match" gilt für **alle** `!`-Trigger des Projekts, nicht nur die in der Routing-Table gelisteten.

---

## 5. Versionierung

- **v0.2.0 (2026-05-21):** Gemini-Single-Pass-Review-Iteration. H1-H4-Fixes appliziert:
  - **H1+H2** xlsx-Coupling als Pflicht-Set in `sync-coupling.md` (Files 1-6 atomar, xlsx 7+8 derselbe Push-Welle); SKILL.md Schritt 3 + test-scenarios.md S2 angeglichen, S2b INKOMPLETT-Refuse-Test ergänzt
  - **H3** §19.1 Tag-0-Refuse mit Issuer-Ausnahmen (BRK.B `10q_filing`, Schneider/Hermès `trading_update_q*` via config.yaml `earnings_trigger`); test-scenarios S4b + S4c ergänzt
  - **H4** Watchlist.xlsx-Klassifikations-Drift gefixt — `file-classification.md` aufgesplittet in Sub-Kategorien 1a Score-Event-coupled, 1b FLAG-Event-coupled, 1c KONTEXT-coupled, 1d Live-State-Edit
  - Codex-Review entfiel (siehe Memory `feedback_review_via_codex_not_advisor.md`: ChatGPT-Pro-Auth-Bug ~16-21.05.2026); Single-Pass via Gemini-Agent stattdessen
- v0.1.0 (2026-05-21): Initial-Draft.

**Promotion-Kriterium v1.0.0:** 3 erfolgreiche Real-Sessions ohne Refuse-False-Positive UND alle Test-Szenarien S1-S10 grün UND (falls Codex zurück ist) ein Codex-Cross-Check der Spec.
