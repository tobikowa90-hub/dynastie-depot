# Push-Safety: Pre-Push-Checks

Skill macht **nie** `git push` ohne Hard-Stop + User-Approval. Diese Checks laufen
vor dem Stop, damit der Plan im Approval-Prompt vollständig ist.

## Pre-Push-Check-Set

### 1. Branch-State

```bash
git rev-parse --abbrev-ref HEAD
git rev-list --left-right --count origin/main...HEAD
```

Erwartung:
- Branch: `main` (oder explizit Feature-Branch — dann anders behandeln, siehe §6)
- Counts: `0 N` (origin = 0 behind, local = N ahead)

**REFUSE-Conditions:**
- `M 0`: lokal hinter origin — User muss pull/rebase, nicht push
- `M N` (M>0): divergiert — User muss merge/rebase
- Branch nicht `main` und kein bekannter Worktree: Rückfrage

### 2. Force-Detection

Niemals `--force` oder `+main:main` Refspec. Skill verwendet ausschließlich:

```bash
git push origin main
```

Wenn das fehlschlägt: STOP, kein Retry mit Force.

### 3. Working-Tree-Clean

```bash
git status --porcelain
```

Erwartung: leer (alle Commits durch, kein Modified, kein Untracked).

**Nicht-leer-Action:** Skill wirft Hinweis und fragt, ob Push trotzdem (lokale
Files bleiben unbeeinflusst) oder erst auflösen. Default: erst auflösen.

### 4. Tags

Skill pusht **keine** Tags ohne explizite User-Anfrage. `git push --tags` ist
out-of-scope.

### 5. Hook-Aktivierung

Pre-push-Hooks (falls definiert) laufen automatisch. Bei Fehlschlag: STOP, Output
zeigen, kein `--no-verify`-Bypass.

## Push-Plan-Format

Vor dem Hard-Stop diesen Plan dem User präsentieren:

```
PUSH-PLAN
=========
Branch:       main → origin/main
Ahead:        <N> commits
Behind:       0 (clean fast-forward)
Working tree: clean
Hooks:        pre-push pending (auto-run)
Force:        nein
Tags:         keine

Commits to push:
  <sha1-short> <subject>
  <sha2-short> <subject>
  ...

Push? [warte auf go/push/ja]
```

## Post-Push-Verify

Nach erfolgreichem Push:

```bash
git status                       # expect: nothing to commit, working tree clean
git rev-list origin/main..HEAD   # expect: leer
git log -1 --format='%H %s'      # expect: latest commit matches what was pushed
```

Bei Diskrepanz (z.B. push partial): STOP, User informieren.

## Feature-Branch-Sonderfall

Wenn Branch nicht `main`:

- Push-Target ist `origin/<branch-name>` (oder `-u origin <branch>` falls neu).
- Working-Tree-Clean-Check identisch.
- Force-Verbot identisch.
- Merge-/PR-Creation **out-of-scope** für session-closure (würde gh-cli erfordern,
  ist separate User-Aktion).

## Force-Push-Ausnahme

Wenn User explizit Force-Push verlangt (z.B. "force push, rebase fertig"):

- Skill bestätigt: "Force-Push nach origin/main angefordert. Letzte Chance Abbruch? [confirm]"
- Bei "confirm": `git push --force-with-lease origin main` (nie nacktes `--force`).
- `--force-with-lease` schützt vor Überschreiben fremder Commits, falls origin
  zwischenzeitlich avanciert ist.
- Memory `feedback_no_force_push_main` (falls existiert) hat Vorrang — nochmal lesen.
