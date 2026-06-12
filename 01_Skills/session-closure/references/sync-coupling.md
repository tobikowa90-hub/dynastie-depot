# §18-Sync-Coupling: Refuse/Require/Optional

Bei scoring-relevanten Mutationen ist ein konsistentes File-Set Pflicht. Skill prüft
Vollständigkeit und refused, falls inkohärent.

## Hard-Coupling (REFUSE bei Verstoß)

**Score-Event** (definiert als: `score_history.jsonl` wurde **heute** mutiert ODER
ein neuer Record appended):

Diese **8 Files** MÜSSEN gemeinsam in **derselben Session** committed sein
(per §18.1 v2.4 — Pflicht-Set, nicht konditional):

1. `score_history.jsonl` (Trigger selbst)
2. `00_Core/PORTFOLIO.md` (Score/DEFCON/Rate/FLAG-Felder aktualisiert)
3. `00_Core/Faktortabelle.md` (Per-Ticker Faktor-Werte)
4. `00_Core/CORE-MEMORY.md` (§5 oder §12 Score-Lifecycle-Eintrag)
5. `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (narrative Notiz)
6. `01_Skills/dynastie-depot/config.yaml` (Per-Ticker SSoT)
7. `03_Tools/Rebalancing_Tool` (Sparplan-Tool)
8. `03_Tools/Satelliten_Monitor` (Depot-Übersicht)

**Granularitäts-Klausel:** Files 1-6 müssen **atomar in einem Commit** sein
(§18.3). Files 7-8 (xlsx-Tools) dürfen in einem **separaten Commit derselben
Session** liegen — aber Push-Welle muss beide enthalten. Skill prüft, ob beide
Commits ungepusht im selben State sind.

**Konditional zusätzlich:**

- `05_Archiv/flag_events.jsonl` — falls FLAG getriggert oder resolved (via `archive_flag.py` schon CLI-direkt geschrieben, nicht im Score-Commit-Bundle)

**Refuse-Action:** Wenn auch nur einer der 8 Pflicht-Files fehlt: Skill listet die
fehlenden Files auf und bricht ab. User muss den Sync vervollständigen
(typischerweise durch Re-Run von `dynastie-depot` Schritt 7, manuelle xlsx-Pflege
via `openpyxl`, oder manuelle Edit-Welle).

**Begründung (CLAUDE.md §18 + INSTRUKTIONEN §18.1 v2.4):** xlsx-Tools sind seit
v2.4 (11.05.2026) Score-Event-Pflicht-Sync, nicht "Nice-to-have" (Memory
`feedback_xlsx_tools_in_sync_set.md` belegt Spec-Lücke + Korrektur). Inkohärenter
Sync ist genau das Failure-Pattern, das §18 verhindern soll.

## FLAG-Event-Coupling

**FLAG-Trigger oder Resolve** (definiert als: `flag_events.jsonl` heute mutiert):

- `PORTFOLIO.md` FLAG-Spalte muss konsistent sein (aktive FLAGs sichtbar, resolved entfernt).
- `CORE-MEMORY.md §12.<ticker>` sollte FLAG-Event-Bullet haben.
- Score-Event-Coupling **nicht zwingend** ausgelöst, wenn FLAG ohne Score-Move.

**Refuse-Action:** Nur falls `PORTFOLIO.md` FLAG-Status nicht zu `flag_events.jsonl`
passt. Sonst weich.

## Watchlist-Event-Coupling (KONTEXT §6)

**Watchlist-Refresh** (Drop/Add/Reassign in `00_Core/KONTEXT.md §6`):

Per Memory `feedback_watchlist_xlsx_in_sync_set.md` MÜSSEN dabei sein:

- `00_Core/KONTEXT.md` (Trigger)
- `03_Tools/Watchlist_Ersatzbank_Monitor` (xlsx-Spiegel)

**Refuse-Action:** Wenn nur eines mutiert ist. §18.7 Minimal-Smoke-Test bestätigen.

## xlsx-Smoke-Test-Coupling (§18.7)

Wenn **eine** der drei xlsx-Tool-Files modifiziert ist (Rebalancing, Satelliten-Monitor,
Watchlist):

- §18.7 Smoke-Test muss seit letztem `openpyxl`-Write gelaufen sein.
- Nicht deterministisch prüfbar aus git-State allein.
- **Skill-Action:** Frage User explizit: "xlsx-Smoke-Test für `<file>` gelaufen? y/n"
- Bei "n" → Skill refused, User muss `03_Tools/xlsx-smoke-test.md` ausführen.
- Bei "y" → vertraue, weiter.

## Soft-Coupling (Reminder, keine Refuse)

**00_Core/-Touch außerhalb Score-Event:**

Wenn `INSTRUKTIONEN.md`, `CLAUDE.md`, `PIPELINE.md`, `SYSTEM.md`, `STATE.md` mutiert
und Briefing-deploy-relevant:

- **Soft-Reminder im Closure-Report:** "`!SyncBriefing` nicht vergessen (§25)."
- Keine Refuse. User entscheidet.

**01_Skills/-Touch:**

Wenn Skill-Body geändert (SKILL.md, references/, scripts/):

- Soft-Reminder: "Skill-Version-Bump im Frontmatter prüfen."
- Keine Refuse.

## Edge-Cases

- **xlsx-Tools in separatem Commit derselben Session:** Files 1-6 sind atomar in einem
  Commit (§18.3), Files 7-8 (xlsx) dürfen separater Commit sein — aber beide Commits
  müssen in derselben Push-Welle ungepusht vorliegen. Skill prüft: wenn `score_history.jsonl`
  in unpushed Commit A liegt und xlsx in unpushed Commit B liegt UND beide auf Push warten:
  ok. Wenn xlsx fehlt (nicht modifiziert, nicht in History): REFUSE.
- **Multi-Score-Event in einer Session** (selten): Coupling-Check mehrfach laufen lassen,
  pro Event-Bundle separat verifizieren.
- **Backfill-Run:** Skill aktiviert sich **nicht** bei laufendem Backfill (außerhalb
  §18 Forward-Vertrag). User muss manuell schließen.
- **Atomarität-Strict-Lesart:** §18.3 verlangt wörtlich "alles in einem Commit". Die
  separater-xlsx-Commit-Toleranz lebt von CLAUDE.md "xlsx-Tools können separater
  Tool-Commit sein, aber gleiche Session pflicht". Beide Lesarten sind project-canonical;
  bei Konflikt entscheidet CLAUDE.md (operativ) gegen wörtliches §18.3 (theoretisch).
