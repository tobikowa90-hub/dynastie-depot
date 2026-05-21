# Commit-Banner-Konventionen

Basis: Conventional Commits + projektspezifische Erweiterungen aus Commit-History.

## Banner-Wahl-Matrix

| File-Klassifikation | Default-Banner |
|---------------------|----------------|
| doc-only (Earnings, Recap, PDFs, Transkripte) | `chore(repo): <kurzdesc>` |
| meta + scoring-neutral (PIPELINE-Cleanup, §X.Y-Edit, Erratum) | `chore(meta): <subject> (scoring-neutral)` |
| scoring-relevant (Score-Event, Sync-Welle) | `score(<ticker>): <action>` ODER `feat(score): <ticker> <action>` |
| FLAG-Event (Trigger/Resolve ohne Score-Move) | `flag(<ticker>): <trigger\|resolve> <reason>` |
| code (Tool-Refactor, Skill-Update, Bugfix) | `feat(<scope>): <desc>` / `fix(<scope>): <desc>` |
| Sparraten-Refresh (Rebalancing ohne Score-Move) | `chore(rebalance): <desc>` |

## Pattern: PIPELINE-Cleanup

```
chore(meta): PIPELINE #<N> KOMPLETT <action> per Numbering-Convention (scoring-neutral)

<optionaler 1-2-Zeilen Body mit Begründung / Cross-Ref>
```

**Beispiele aus History:**
- `chore(meta): PIPELINE #71 KOMPLETT DONE-Item entfernt per Numbering-Convention — Option (a) Erratum akzeptiert (scoring-neutral)`
- `chore(meta): PIPELINE #70 KOMPLETT DONE-Item entfernt per Numbering-Convention (scoring-neutral)`
- `chore(meta): PIPELINE #72 Rekonziliation + #70(c) echtes Gemini-Verdikt (scoring-neutral)`

## Pattern: §-Spec-Edit (Erratum / Klärung / Wording-Fix)

```
chore(meta): §<X>.<Y>-<Letter> <kurzdesc> — <ergebnis> (scoring-neutral)
```

**Beispiel:**
- `chore(meta): §18.7-E/F Sichttest-Closure — Rebalancing-Tool CF User-bestätigt (scoring-neutral)`

## Pattern: Doc-Addition (Earnings, Research, Onboarding)

```
chore(repo): add <topic> (<scope>)
```

**Beispiel:**
- `chore(repo): add AMZN Q1 FY26 Earnings Release + Call Transcripts (Onboarding-Source-Docs)`

## Pattern: Score-Event-Bundle (§18-Sync-Commit)

```
score(<ticker>): <verdict-shift> Q<n> FY<YY> (<delta>)

DEFCON Score: <alt> → <neu>
FLAG: <status>
Sparrate: <alt>€ → <neu>€
Trigger: <ticker> Q<n> Earnings / Outlook / Filing
Sync-Set: 6 files + xlsx (§18 atomar)
```

**Beispiel (hypothetisch):**
- `score(AMZN): Q1 FY26 Score-Move 87 → 89 (+2 nach AWS-Margin-Beat)`

## Pattern: FLAG-Event

```
flag(<ticker>): <trigger|resolve> — <reason>
```

**Beispiele:**
- `flag(SU): trigger — IFRS-Guidance-Cut > 10% (Q2)`
- `flag(BRK.B): resolve — Cash-Build-Konzern-bestätigt 13F`

## Banner-Anti-Patterns (NICHT verwenden)

- `update`, `misc`, `changes`, `WIP`, `tmp`, `fix`: zu vage
- Lone `chore:` ohne Scope: scoring-Klassifikation unklar
- `feat(repo):` für doc-additions: doc-additions sind `chore(repo)`, kein `feat`
- Multi-Subject in einem Banner: lieber zwei Commits

## Heredoc-Disziplin (Tooling)

Bei Body-Multiline-Messages: **immer** Heredoc, nie inline-Quoting.

**Falsch (PowerShell-only, Bash-Tool korrumpiert via @-Marker):**
```powershell
git commit -m @'
Subject
Body
'@
```

**Richtig (Bash-Tool):**
```bash
git commit -F - <<'MSG'
chore(meta): PIPELINE #X KOMPLETT done (scoring-neutral)

Body line 1.
Body line 2.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
MSG
```

**Post-Commit-Verify (Reinfall-Doku Memory `feedback_powershell_herestring_in_bash_tool.md`):**
```bash
git log -1 --format='%s' | cat -A
```
Erwartung: kein lone `@` am Anfang/Ende, kein `^M$` (CRLF). Bei Defekt: `git commit --amend -F -` mit korrektem Heredoc.
