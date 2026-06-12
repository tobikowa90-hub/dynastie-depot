# Test-Szenarien (Regression-Check)

Manuelle Test-Szenarien für `!SessionClose`-Skill. Bei Skill-Änderungen
diese Szenarien gegen-prüfen (kein Auto-Run, qualitative Review).

## S1: Saubere Session, nur unpushed Commits

**State:** Working tree clean, 2 Commits vor origin/main (z.B. Pipeline-Cleanups).
**Erwartet:**
- Schritt 0: pre-flight pass
- Schritt 1: State-Scan zeigt 2 unpushed commits, 0 modified, 0 untracked
- Schritt 2-4: keine Klassifikation nötig, kein Commit-Plan, direkt zu Push-Plan
- Schritt 6: Hard-Stop mit Push-Plan
- Schritt 7-8: Push + clean Verify + Closure-Report

**Fail-Signal:** Skill versucht zu committen obwohl nichts staged → Banner-Wahl-Logik fehlerhaft.

## S2: Score-Event mit vollständigem §18-Sync (8-File-Set)

**State:** Modified: `PORTFOLIO.md`, `Faktortabelle.md`, `CORE-MEMORY.md`, Vault `log.md`,
`01_Skills/dynastie-depot/config.yaml`, `03_Tools/Rebalancing_Tool`,
`03_Tools/Satelliten_Monitor`. Untracked: 1 neuer `score_history.jsonl`-Append
(über `archive_score.py` schon gestaged).
**Erwartet:**
- Schritt 3: Coupling-Check pass (alle 8 Pflicht-Files da)
- Schritt 3 xlsx-Frage: "xlsx-Smoke-Test gelaufen? y/n" → User-Bestätigung
- Schritt 4: 2-Commit-Plan (Files 1-6 in einem Score-Event-Commit, xlsx 7-8 in separatem Commit derselben Push-Welle — §18.1 Granularitäts-Klausel)
- Banner Commit-1: `score(<ticker>): Q<n> FY<YY> <delta>`
- Banner Commit-2: `chore(xlsx): refresh Rebalancing + Satelliten-Monitor (post <ticker> Score-Event)`

**Fail-Signal:** Skill akzeptiert nur 6 base files ohne xlsx (alte v0.1.0-Drift), oder bündelt xlsx zwingend in Score-Commit (zu strikt — Granularitäts-Klausel verletzt).

## S2b: Score-Event INKOMPLETT — xlsx fehlt (Refuse-Test)

**State:** Wie S2, aber xlsx-Tools nicht modifiziert (vergessen).
**Erwartet:**
- Schritt 3: Coupling-Check **REFUSE** mit Liste der fehlenden xlsx-Files
- Hinweis: "xlsx-Tools sind §18.1 v2.4 Pflicht-Set-Mitglieder. Bitte via `openpyxl` mit-syncen + §18.7-Smoke-Test, dann erneut."

**Fail-Signal:** Skill committed 6-File-Bundle ohne xlsx-Hinweis.

## S3: Score-Event INKOMPLETT (Refuse-Test)

**State:** Nur `score_history.jsonl` + `PORTFOLIO.md` modifiziert, andere Sync-Files fehlen.
**Erwartet:**
- Schritt 3: Coupling-Check **REFUSE** mit Liste der fehlenden Files
- Kein Commit ausgeführt
- Skill schlägt Re-Run von dynastie-depot Schritt 7 vor

**Fail-Signal:** Skill committed unvollständigen Sync.

## S4: Tag-0-Earnings-Falle (Refuse-Test, US-Satellit mit `quarterly_call`)

**State:** Heute ist Earnings-Tag eines US-Satelliten mit `earnings_trigger: quarterly_call`
(z.B. AMZN, MSFT, V) — Call heute Abend, kein Transcript verfügbar.
`CORE-MEMORY §12.<ticker>` hat Pre-Call-Snapshot von heute. `score_history.jsonl` hat
unsanctioned Score-Move-Record von heute.
**Erwartet:**
- Schritt 0: REFUSE mit §19.1-Begründung
- Skill listet Optionen: (a) Score-Record zurückrollen, Tag +1 wiederholen, (b) FLAG-only behalten

**Fail-Signal:** Skill committed Tag-0-Score-Move ohne Warnung.

## S4b: BRK.B 10-Q-Filing-Tag (KEINE Refuse — Issuer-Ausnahme)

**State:** Heute ist BRK.B 10-Q-Filing-Tag. `config.yaml` zeigt `earnings_trigger: 10q_filing`.
Pre-Call-Snapshot in `CORE-MEMORY §12.BRK.B` von heute. `score_history.jsonl`-Record von heute.
**Erwartet:**
- Schritt 0: pre-flight pass (Issuer-Ausnahme greift, kein Refuse)
- Workflow läuft normal weiter Richtung §18-Coupling-Check + Commit-Plan

**Fail-Signal:** Skill refused BRK.B mit §19.1-Begründung obwohl Issuer-Ausnahme greift.

## S4c: Non-US Trading-Update-Quarter (Schneider/Hermès Q1 oder Q3)

**State:** Heute Trading-Update-Release von SU oder RMS. `config.yaml` zeigt
`earnings_trigger: trading_update_q1` oder `_q3`. Score-Record von heute.
**Erwartet:**
- Schritt 0: pre-flight pass (Trading-Update = Vollanalyse-Tag, kein Call)
- Workflow läuft normal weiter

**Fail-Signal:** Skill refused obwohl trading_update-Quarter explizit Tag-0-Analyse erlaubt.

## S5: Mixed doc-only + Code

**State:** Untracked: Earnings-PDFs in `02_Analysen/Earnings Reports/`. Modified: Bugfix in
`03_Tools/backtest-ready/archive_score.py`. Kein Score-Event.
**Erwartet:**
- Schritt 4: 2 separate Commits geplant
  - `chore(repo): add <ticker> Q<n> earnings materials`
  - `fix(backtest-ready): <bugfix-desc>`
- Schritt 5: beide ausgeführt
- Schritt 6: Push-Plan mit beiden

**Fail-Signal:** Skill bündelt doc + code in einen Commit.

## S6: Vollständig sauber (No-Op)

**State:** Working tree clean, origin synced.
**Erwartet:**
- Schritt 1: nichts zu tun
- Closure-Report sofort: "Nothing to commit, nothing to push, ready for /clear."

**Fail-Signal:** Skill versucht trotzdem Commits oder Push.

## S7: Trigger-Strictness (Phrase ohne `!SessionClose`)

**State:** User sagt "Session beenden" ohne `!SessionClose`.
**Erwartet:**
- Skill aktiviert sich **nicht** automatisch (Description-Wortlaut).
- Falls aktiviert: Rückfrage "Meintest du `!SessionClose`?"

**Fail-Signal:** Skill fängt Workflow ohne explizite Bestätigung an.

## S8: Rebase-in-progress

**State:** `git status` zeigt "rebase in progress".
**Erwartet:**
- Schritt 0: REFUSE
- Hinweis: "Rebase abschließen oder abbrechen (`git rebase --continue|--abort`), dann erneut versuchen."

**Fail-Signal:** Skill ignoriert Rebase-State.

## S9: Ahead+behind divergiert

**State:** `git rev-list --left-right origin/main...HEAD` = `3 2` (3 behind, 2 ahead).
**Erwartet:**
- Schritt 0: REFUSE
- Hinweis: pull/rebase manuell entscheiden.

**Fail-Signal:** Skill versucht push und scheitert outbound.

## S10: Multi-Commit-Session mit PIPELINE-Cleanups

**State:** Untracked + Modified mix mehrerer PIPELINE-Items + doc-only-Recherche.
**Erwartet:**
- Schritt 4: Plan listet z.B. 4 separate Commits:
  - `chore(meta): PIPELINE #X ... (scoring-neutral)`
  - `chore(meta): PIPELINE #Y ... (scoring-neutral)`
  - `chore(repo): add <topic>`
  - `chore(meta): §X.Y ... (scoring-neutral)`
- **Eine** Plan-Approval, dann auto-execute aller 4 Commits
- Hard-Stop nur vor Push

**Fail-Signal:** Skill macht 4× Approval-Loop (Workload-Reinfall) ODER bündelt PIPELINE-Items in einen Commit.
