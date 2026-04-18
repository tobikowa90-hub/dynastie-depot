---
name: backtest-ready-forward-verify
version: "1.0.0"
description: >
  Orchestriert den Persistence-Teil jeder !Analysiere-Forward-Vollanalyse.
  Konsumiert einen ScoreRecord-Draft (JSON) aus dynastie-depot Schritt 7,
  validiert gegen Schema + STATE.md-Tripwire, führt §28.2 Algebra-Δ-Gate
  (conditional), macht Dry-Run und Append an score_history.jsonl, gibt
  strukturierten Report an Aufrufer zurück. Keine eigenen Trigger-Words —
  aktiviert sich ausschließlich programmatisch aus dynastie-depot.
trigger_words: []
---
# backtest-ready-forward-verify — Skill v1.0.0

**Aktivierung:** Ausschließlich programmatisch aus `dynastie-depot` Schritt 7.
Keine direkten Trigger-Words. Nie manuell aufrufen.

---

## 1. Boundary — Scope dieser Skill

Diese Skill mutiert **ausschließlich** `05_Archiv/score_history.jsonl` (Append-Only).

**In-Scope:**
- Lesen des Draft-JSON (ScoreRecord + optionale `skill_meta`)
- Freshness-Check der drei Pflicht-Touch-Dateien
- STATE.md-Tripwire (Konsistenz-Check Score/DEFCON/FLAG)
- §28.2 Algebra-Δ-Gate (nur bei `skill_meta` vorhanden)
- Dry-Run-Validation via `archive_score.py --dry-run`
- Real-Append via `archive_score.py`
- `git add 05_Archiv/score_history.jsonl` (kein Commit — Sync-Commit folgt in §18)

**Out-of-Scope (Caller-Verantwortung):**
- Narrative Dateien: `STATE.md`, `Faktortabelle.md`, `CORE-MEMORY.md`, `log.md`, `config.yaml`
- Sync-Commit (§18 Pflicht nach Analyse)
- FLAG-Events (`archive_flag.py`, `flag_events.jsonl`)
- Backfill-Runs
- Automatisches CORE-MEMORY §5 schreiben (skill gibt Signal; Caller schreibt)

---

## 2. Authoritative Sources (Punkt-Links — nicht inlinen)

| Quelle | Verwendung |
|--------|-----------|
| `03_Tools/backtest-ready/schemas.py::ScoreRecord` | Record-Schema, MigrationEvent, Validatoren |
| `03_Tools/backtest-ready/schemas.py::MigrationEvent` | §28.2 Δ-Buckets + Self-Validation |
| `03_Tools/backtest-ready/_forward_verify_helpers.py` | Python-Primitives (parse_wrapper, parse_state_row, build_migration_event, check_freshness) |
| `00_Core/INSTRUKTIONEN.md §18` | Sync-Pflicht nach Analyse |
| `00_Core/INSTRUKTIONEN.md §27.4` | Multi-Source-Drift Prevention |
| `00_Core/INSTRUKTIONEN.md §28.2` | Algebra-Δ-Tabelle + Outcome-Buckets |
| `00_Core/STATE.md` (Zeilen 15-27) | Tripwire-Quelle: aktuelle Portfolio-State-Tabelle |

**Drift-Prevention (§27.4):** Bucketing-Logik (|Δ|≤2/3-5/>5) NICHT hier kopieren.
Sie lebt in `schemas.py::MigrationEvent._check_outcome_bucket` und in
`_forward_verify_helpers.py::build_migration_event`. Schema-Validator ist Master.

---

## 3. Invocation

```python
Skill(skill="backtest-ready-forward-verify", args="<pfad-zum-draft>")
```

- `args`: String-Pfad zur Draft-JSON-Datei (relativ zum Repo-Root oder absolut).
- Aufrufer: `dynastie-depot` Schritt 7 — nach abgeschlossener Analyse, vor Sync-Commit.
- Der Draft-Pfad liegt typischerweise in `03_Tools/backtest-ready/_drafts/`.

**Draft-JSON-Format:**
```json
{
  "record": { ...vollständiger ScoreRecord als dict... },
  "skill_meta": {
    "expected_algebra_score": 63,
    "migration_from_version": "v3.5",
    "migration_to_version": "v3.7"
  }
}
```
`skill_meta` ist optional. Fehlt oder ist leer → kein Δ-Gate. Ist vorhanden →
alle drei Keys müssen gesetzt sein, sonst P1 Fehler.

---

## 4. Pipeline Phases P1–P6

### Phase-Tabelle (Kurzreferenz)

| Phase | Name | Helper / Tool | Exit bei Fehler |
|-------|------|---------------|-----------------|
| P1 | Draft-Read + Parse | `parse_wrapper(args)` | FAIL P1 |
| P2a | Freshness-Check | `check_freshness(repo_root)` | Warnung (nicht blockierend) |
| P2b | Tripwire | `parse_state_row(ticker, STATE.md)` | FAIL P2b |
| P3 | Δ-Gate (conditional) | `build_migration_event(skill_meta, forward_score)` | STOP signal (nicht blockierend) |
| P4 | Dry-Run | `archive_score.py --file <draft> --dry-run` | FAIL P4 |
| P5 | Real Append | `archive_score.py --file <draft>` | FAIL P5 |
| P6 | git add | `git add 05_Archiv/score_history.jsonl` | FAIL P6 (manuell recovery) |

### P1 — Draft-Read

Ruf `parse_wrapper(args)` auf. Gibt `(record_dict, skill_meta)` zurück.

- Wenn `skill_meta` nicht leer aber unvollständig → ValueError → `FAIL phase=P1`.
- `record_dict` enthält den vollständigen ScoreRecord-Dict.
- Schreibe ggf. Migrations-Event noch nicht in `record_dict` — das passiert in P3.

### P2a — Freshness-Check (nicht blockierend)

Ruf `check_freshness(repo_root=<repo_root>)` auf. `repo_root` = Verzeichnis des Repos
(Parent von `00_Core/`, `03_Tools/`, etc.).

- Gibt Liste von Dateinamen zurück, die NICHT modifiziert sind.
- Leere Liste → alle drei Pflicht-Dateien (STATE.md, Faktortabelle.md, log.md) wurden
  im Laufe der Analyse berührt. Gut.
- Nicht-leere Liste → Warnung im Output (Line 3+ im Report). KEIN Stopp — die Analyse
  kann trotzdem archiviert werden. Freshness ist Hinweis für Caller.

**Conditional files ignorieren:** CORE-MEMORY.md und config.yaml werden nicht geprüft.
check_freshness gibt sie nie zurück — keine manuelle Filterung nötig.

### P2b — Tripwire (STATE.md Konsistenz)

Lese `00_Core/STATE.md`. Ruf `parse_state_row(ticker, state_md_content)` auf.
Vergleiche Ergebnis `{score, defcon, flags_active}` gegen `record_dict`:

- **Score:** `state_score != record.score_gesamt` → `FAIL phase=P2b reason="score drift: state=<X> vs record=<Y>"`. Exakter Vergleich (beide ints).
- **DEFCON:** Abweichung → `FAIL phase=P2b reason="defcon drift: ..."`.
- **FLAG:** `flags_active=True` aber `aktiv_ids=[]` → `FAIL phase=P2b reason="FLAG-Drift: ..."`. Umgekehrt (neuer FLAG im Record) kein Fehler.
- **Ticker nicht gefunden** → ValueError → `FAIL phase=P2b reason="ticker not found"`.
- **Neu analysierter Ticker** (noch nicht in STATE.md): Tripwire überspringen, Report: `[tripwire: ticker 'XYZ' not in STATE.md — new position]`.

### P3 — Algebra-Δ-Gate (conditional)

Nur ausführen wenn `skill_meta` nicht leer.

Ruf `build_migration_event(skill_meta, forward_score=record_dict["score_gesamt"])` auf.
Injiziere `event.model_dump()` in `record_dict["migration_event"]`.

- `signal == ""` → accepted → weiter zu P4.
- `"PFLICHT:"` in signal → log_only → merke für Report Line 4. **Kein Stopp** — Archivierung läuft durch.
- `signal.startswith("STOP:")` → block → merke für Report Line 5. **Kein Stopp auf Archiv-Ebene** — Record ist Historie-relevant; Fan-Out (STATE.md/Sparrate/CORE-MEMORY) blockiert bis Caller Ursache identifiziert.

`MigrationEvent` self-validiert Δ-Arithmetik + Bucket — Exception-frei = konsistent.

### P4 — Dry-Run Validation

Schreibe `record_dict` (inkl. ggf. `migration_event`) **als bare ScoreRecord** (nicht das Wrapper-Format `{"record": ...}`) als JSON in eine Temp-Datei.

```bash
python 03_Tools/backtest-ready/archive_score.py --file <path> --dry-run
```

- Exit 0 → P5. Exit 1/2 → `FAIL phase=P4 reason="<stderr>"`. Stopp.
- Häufige Fehler: `duplicate record_id` (bereits archiviert — keine Retry), `arithmetic mismatch` (Sub-Score-Fehler im Draft), `defcon_level inconsistent`.

### P5 — Real Append

```bash
python 03_Tools/backtest-ready/archive_score.py --file <path>
```

Exit 0 → P6. Exit 1/2 → `FAIL phase=P5 reason="<stderr>"`. Stopp — keine Retry ohne manuelle Prüfung.

### P6 — git add

```bash
git add 05_Archiv/score_history.jsonl
```

Kein Commit hier — Sync-Commit gemäß §18. Fehler → `FAIL phase=P6 reason="..."`. Recovery: manuell git add.

---

## 5. Exit-Code Convention

`0` = Erfolg (kann STOP/Freshness-Warnungen enthalten). `1` = Validation/Drift/Duplicate. `2` = IO-Fehler.

---

## 6. Stdout-Report Format (Consumer Contract)

Die folgenden Zeilen erscheinen in dieser Reihenfolge. Optionale Zeilen nur wenn
die Bedingung zutrifft.

```
Line 1: OK record_id=<id> score=<n> defcon=<n>
Line 2: [migration_event: from=<v> to=<v> algebra=<n> forward=<n> delta=<n> |Δ|=<n> outcome=<accepted|log_only|block>]
Line 3+: [freshness: <Dateiname> not modified — dynastie-depot Schritt 0-6 vollständig gelaufen?]
Line 4: PFLICHT: CORE-MEMORY §5 Eintrag für Migration-Event (log_only outcome). Siehe INSTRUKTIONEN §28.2.
Line 5: STOP: §28.2 |Δ|=<N> > 5. Fan-Out (7 Oberflächen) blockiert bis Algebra-Ursache identifiziert. Siehe CORE-MEMORY §5. JSONL-Commit läuft durch — Record ist Historie-relevant.
```

- **Line 1** immer bei Erfolg.
- **Line 2** nur bei Migrations-Run (skill_meta vorhanden).
- **Line 3+** einmal pro missing-Datei (0 bis 3 Zeilen).
- **Line 4** nur bei outcome=log_only.
- **Line 5** nur bei outcome=block (schließt Line 4 aus).

**Bei Fehler (Exit 1 oder 2):**
```
FAIL phase=<P1|P2b|P4|P5|P6> reason="<Fehlermeldung>"
```

---

## 7. Recovery — Partieller P5-Abbruch

Wenn P5 (Append) erfolgreich war aber P6 (`git add`) fehlschlägt: **nicht erneut aufrufen** — P4 würde `duplicate record_id` melden (Exit 1). Stattdessen manuell:

```bash
git add 05_Archiv/score_history.jsonl
# Dann Sync-Commit gemäß §18
```

---

## 8. Out-of-Scope (Vollständige Liste)

Diese Aktionen sind bewusst **nicht** Teil dieser Skill:

- **Backfill-Runs** — separate `backfill_scores.py` + `backfill_flags.py`
- **FLAG-Event-Archive** — `archive_flag.py`, `flag_events.jsonl`
- **Multi-File-Tripwire** — Faktortabelle, CORE-MEMORY, log.md, config.yaml werden nicht als Tripwire-Quelle genutzt
- **Automatisches CORE-MEMORY §5 schreiben** — Skill gibt Signal (PFLICHT:/STOP:), Caller schreibt
- **Sync-Commit** — §18 ist Caller-Verantwortung nach Gesamt-Analyse
- **STATE.md + Faktortabelle aktualisieren** — Caller schreibt nach Analyse, vor Commit
- **FLAG-Event-Studies** — `flag_event_study.py`
- **Scoring-Entscheidungen** — Skill persistiert nur, trifft keine inhaltlichen Urteile
