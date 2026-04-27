# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-27 sehr spät (Folge-Session) — **v3.0.5 Implementation-Plan SCHRIFTLICH DONE + codex-reviewed** (10 Findings, 2 HIGH/5 MEDIUM/3 LOW, alle inline gefixt). Execution-Phase startet in nächster Session mit frischem Context bei **Phase 1** des Plans.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `22c057c` (writing-plans v3.0.5 complete + codex-pass + handover). Vorgänger-Commit `9b5f954` (v3.0.5-Spec foundation).

**Plan-File:** `docs/superpowers/plans/2026-04-27-briefing-v3.0.5-implementation.md` (~1320 Zeilen, 8 Phasen, 38 Tasks/Phase-Header).

**NEXT-SESSION-RESUME — Execution Phase 1:**

1. Standard Session-Start: STATE.md + PORTFOLIO.md.
2. **Skill: superpowers:executing-plans** ODER **superpowers:subagent-driven-development** (User-Wahl, beide laden Plan-File und gehen task-by-task durch).
3. Plan-File `docs/superpowers/plans/2026-04-27-briefing-v3.0.5-implementation.md` lesen — speziell den Plan-Header (Trigger-IDs, Pre-existing-Dirty-Liste, HARTER STAGING-CONTRACT) und Phase 1 (Tasks 1.1-1.8).
4. **Phase 1 ausführen:** 6 Prompt-Edits in `03_Tools/morning-briefing-prompt-v3.md` (Changelog v3.0.4+v3.0.5 / FIELD→SOURCE-MAP / SCHRITT 3a Anti-Fallback / Critical-Guards-Erweiterung / §6F-Tabelle + SCHRITT 4.8 / Output-Tag-Direktive in KURS-CHECK+NEWS-SIGNAL+Earnings) — jede Edit-Operation einzeln mit grep-Verify nach OneDrive-Persistenz. Dann Commit + Push (Task 1.7 + Task 1.8). Phase-1-Estimate: 35-50 Min.
5. **Phase 2-6:** Probe-Update / T-Stale-Shibui / T6 Provenance / T1+T3+T4 Retest / Prod-Deploy. Estimate: 60-70 Min für Phase 2-6 zusammen.
6. **Phase 7-8:** Tag-1-Cron-Review (Folgetag, 5 Min) + Sync-Pflicht (15 Min, log + CORE-MEMORY + SYSTEM + PIPELINE + SESSION-HANDOVER in einem Commit; Plan-File separater Commit gemäß Plan Task 8.6 Step 3).

**Codex-Review-Pass (siehe Plan-File Sektion „Codex-Review-Pass (2026-04-27)"):**
- HIGH #5 T-Numbering: Phase 3 Test heißt **T-Stale-Shibui** (NICHT T5), um Drift mit Spec-T5 (Post-Update-Content-Verify) zu vermeiden.
- HIGH #9 Self-Check-Gate-Marker: bei nicht-zugänglicher Run-Trace ist Status **UNVERIFIED**, NICHT PASS — Phase-7+-Monitoring greift.
- MEDIUM #3a Push: neuer Task 1.8 (Spec §10 Schritt 3) zwischen Phase-1-Commit und Phase-2-Update.
- weitere 7 Findings (3 MEDIUM, 3 LOW, 1 LOW) inline gefixt.

**Codex-Sparring-Option (siehe Auto-Memory `feedback_codex_sparring_heuristic.md`):**
Falls Phase-1-Execution drift produziert (Edit-Anker schlagen fehl) oder Phase 3/4 unerwartete Failure-Modi zeigen, ist `SendMessage` an Agent-ID **`a26d1ecda8d7ae53b`** der billigste Re-Review-Schritt (~5-10k Tokens statt 50-65k Volltext, weil Spec + Plan bereits im Reviewer-Kontext). Single-Pass-Default greift sonst — kein automatischer Sparring-Loop.

**Diese Session committed:**

```
9b5f954  docs(spec): v3.0.5 Bucket-B Provenance-Architecture — §3.0 + §6F + §9 T6
```

**Codex-Trace dieser Session (insgesamt 7 Codex-Subagent-Runden):**
- Q1 Aufteilung D⁺ — B0=§3.0 / B0.5=§6F / B0.6=§9-T6
- Q2 Scope B — 5 Felder (Kurs / Delta multi-source / News-Headline / News-Domain / Earnings-Datum), Source-Klassen `external` vs. `file-read-derived`
- Q3 Mechanik B+C — Map + 5-Zeilen-Self-Check-Gate (SCHRITT 4.8) + Tag-Pflicht `[source_ref@source_date]`
- Q4 §6F-Klassen-Achse A' — 6 Klassen flach mit §6F→§6E Cross-Ref
- Q5 Detailfragen — Delta dual-tagged, Earnings-Tag voll, Mismatch-`source_date` = Ist-Wert
- Final-Review (Round 5) — 5 Findings (2 HIGH, 3 MEDIUM), alle gefixt
- Sanity-Check (Round 6) — 2 echte FAIL gefunden (Implementation-Status SCHRITT 4.8 nicht klar als Pending markiert; §10 Tag-Format-Bullet widersprach §3.0(c) für file-read-Tags), beide gefixt

### 🟢 NEXT-SESSION-RESUME — v3.0.5 Implementation-Plan

**Trigger:** "writing-plans v3.0.5 starten" oder "Implementation-Plan für v3.0.5 schreiben" oder "weiter mit v3.0.5 implementation".

**Was dann zu tun ist:**

1. STATE.md + PORTFOLIO.md lesen (Standard Session-Start).
2. **Nicht** dynastie-depot-Skill als ersten Schritt — Implementation-Phase ist Plan-Schreiben, nicht DEFCON-Analyse.
3. **superpowers:writing-plans** Skill aktivieren.
4. **3 Files lesen für Kontext:**
   - `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` (v3.0.5-Spec, HEAD `9b5f954`) — speziell §3.0, §6F, §9 T6, Revision-Log v3.0.5-Eintrag
   - `03_Tools/morning-briefing-prompt-v3.md` (aktiver Prompt v3.0.3 Rollback-Stand — wird zu v3.0.5 gebumpt mit BEIDEN Layern: v3.0.4-Hotfix-Wording UND v3.0.5-Provenance-Layer)
   - `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (alter 13-Task-Hotfix-Plan — wird vom neuen v3.0.5-Plan ERSETZT, nicht ergänzt)
5. **Plan-Scope-Wording:** ein einziger Implementation-Plan, der v3.0.4-Hotfix-Wording UND v3.0.5-Provenance-Layer gemeinsam in einem Prompt-Bump v3.0.3→v3.0.5 einspielt. Spec §3.0 Implementation-Status-Bullet ist Anker.

**v3.0.5-Implementation-Plan-Struktur (Empfehlung, vom writing-plans-Skill final geschnitten):**

| Phase | Inhalt |
|-------|--------|
| 1. Prompt-Bump v3.0.3 → v3.0.5 | (a) §3.0-Field→Source-Map als embedded Markdown-Tabelle vor SCHRITT 3; (b) SCHRITT 4.8 Self-Check-Gate-Block; (c) Tag-Format-Direktive in KURS-CHECK + NEWS-SIGNAL + Earnings-Output; (d) v3.0.4 CRITICAL GUARDS Anti-Fallback-Wording integrieren (war nie deployed); (e) §6F-Klassen-Tabelle als embedded Block nach SCHRITT 4.5(E); (f) Critical-Guards-Erweiterung um Self-Check-Gate-Bullet |
| 2. Probe-Trigger Update + Verify | RemoteTrigger update auf Probe `trig_01XYuQ5mugsvZGZD4K52rjXh` mit v3.0.5-Content; POST-UPDATE VERIFY mit den 3 v3.0.5-Asserts (`SCHRITT 4.5` + `SCHRITT 4.8` + `Provenance-Self-Check`, NOT `Keine News-Suche`) |
| 3. T5 Adversarial-Stale-Shibui (v3.0.4-Hotfix-Plan-Migration) | T5-Run unter natürlicher Stale-Source-Bedingung, Anti-Fallback-Wording-Verifikation |
| 4. T6 Adversarial-Provenance-Test (v3.0.5 NEU) | Probe-Run unter Stale-Source; manueller Tag-Authentizitäts-Cross-Check via `RemoteTrigger get`-Tool-Response-History; 5-Punkt-Assertion-Liste aus §9 T6 |
| 5. T1/T3/T4-Retest | Happy-Path / Symbol-Trap / Fehler-Klassen weiter PASS |
| 6. Prod-Deploy v3.0.5 | RemoteTrigger update auf Prod `trig_01PyAVAxFpjbPkvXq7UrS2uG`; POST-UPDATE VERIFY; Manual-Run-Validierung |
| 7. Gate-A-Tag-1 Cron | Nächster Werktag 10:00 MESZ Cron-Lauf, Output-Review |
| 8. Sync-Pflicht | log.md + CORE-MEMORY (Lifecycle-Eintrag v3.0.5-Deploy) + SYSTEM.md §Briefing-Status |

**Was NICHT verloren gehen darf:**

- **v3.0.5-Spec ist Architektur-Foundation, nicht Implementation.** Plan muss Spec lesen + Tasks ableiten, nicht Spec neu schreiben.
- **v3.0.4-Hotfix-Wording wurde nie deployed** — gemeinsamer Bump v3.0.3→v3.0.5 macht beide Layer gleichzeitig live (Defense-in-Depth, beide bewusst integriert).
- **T6 ist manuell** in v3.0.5 (Auto-Capture-Diff = v3.1-Backlog). Reviewer-Schritt: `RemoteTrigger get` öffnen + Output-Tags vs. Tool-Response-Datums-Felder vergleichen.
- **Bucket-B B1-B7 in altem Handover** sind großteils obsolet — B0/B0.5/B0.6 sind in v3.0.5 strukturell adressiert; B1 (News-Feature ship/cut/trim) ist nicht mehr blockiert; B2 (Anti-Fallback-Guard-Perimeter) ist via §3.0-Map gelöst; B5 (T-Numbering) bleibt offener Bucket-A.3-Cleanup im v3.1-Backlog. B3/B4 (Audit-Checks/Monitoring-Redesign) und B6 (Process-Refs) bleiben offene v3.1-Themen.
- **Codex-Reviews via `codex:codex-rescue`-Subagent** (nicht advisor) — Memory-Feedback im User-Profil.
- **Prod läuft v2.2** (Rollback-Stand seit 20.04.), nicht v2.1. Hotfix-Plan-File hatte falsches v2.1-Label, lokal gefixt aber gitignored.
- **OneDrive Edit-Collision-Memory** beachten — Spec ist im OneDrive-Pfad, Edit-Persistenz immer mit `git diff --stat` verifizieren.
- **Pre-Commit-Diff-Inspection-Memory** beachten — pre-existing dirty in Vault-Files (PORTFOLIO.md / Accruals-Anomalie-Sloan / app.json + 3 deleted) ist nicht v3.0.5-Scope; nur Plan-File staging beim Commit.
- **CodeRabbit verzichtet für Spec**, sinnvoller in Implementation-Phase (Prompt-Edits + Plan-File). Memory-Reference: `feedback_review_via_codex_not_advisor.md` + `reference_coderabbit_via_wsl.md`.

---

### 📜 Vorherige Session (27.04. später Tagesabschnitt) — Schema-Drift Phase 2 vault-wide

Vorgänger-Stand (vor dieser Session):

```
11a1b69  fix(wiki): schema-drift cleanup phase 2 — 34 vault-wide pages YAML-Array
737d647  chore(pipeline): tavily rotation #1 fully verified — old key revoked
f51b94a  feat(analyses): pre-earnings briefs V (28.04.) + MSFT (29.04.)
531f459  fix(wiki): schema-drift cleanup phase 1 — sources/related YAML-Array
```

Damals abgeschlossen (Ausschnitt — siehe Git-History für volle Chronik):

- **Schema-Drift Phase 2 DONE (vault-wide)**: 34 drifted Pages konvertiert (15 concepts + 18 sources/papers + 1 sources/references) — Phase-1-Pattern (Block-Form `related:` + `sources: []`-Insert wenn fehlend) via neuem Tool `03_Tools/schema_drift_phase2.py` (line-end-preserving, regex-basiert, Dry-Run + Apply). 220 Wikilinks konvertiert, 33/34 `sources: []`-Inserts (Moat-Taxonomie hatte schon `sources:`). PyYAML-Bulk-Validation vault-weit 185/0 (367 Wikilinks in Arrays). Diffstat +287/-34. PIPELINE #15 → DONE. **Limitation:** 8 concept-pages mit `source:` (singular) bleiben unverändert (Phase-1 hat das auch nicht migriert; kein Pflicht-Feld, keine Backlink-Auswirkung).

**Vorgänger-Session (27.04. spät) abgeschlossen:**

- **Pre-Earnings-Briefs**: `02_Analysen/V_pre-earnings_2026-04-28.md` + `02_Analysen/MSFT_pre-earnings_2026-04-29.md` via `anthropic-skills:earnings-preview` (yfinance). V-Setup: technisch angeschlagen (-7,2 % unter 200MA, RelStärke -14pp), Konsens $3,099 EPS / $10,75 Mrd Rev, 4/4 Beats aber Surprise-Magnitude decel auf <1 %. MSFT-Setup: Recovery (+10,5 % in 2W, über 50DMA), Konsens $4,065 EPS / $81,40 Mrd Rev, 4/4 Beats +8,5 % Schnitt. Beide Briefs enthalten Bull/Base/Bear-Decision-Matrix + Schritt-für-Schritt-Earnings-Tag-Workflow inkl. Sync-Pflicht §18 für FLAG-Auflösungs-Szenario MSFT.
- **Tavily-Key-Rotation DONE**: alter Key `tvly-dev-4PYXp...` ersetzt. PROD-Connector (Claude.ai Web-UI) via Delete+Recreate (URL read-only) — Connector-Name bleibt `tavily`, friendly-name-Resolution `mcp__tavily__tavily_search` unverändert, **Repo-Prompts brauchen keinen Edit**. Lokal `~/.claude.json:777` editiert + Trailing-Space-Fix. **TODO User:** alten Key auf tavily.com revoken nach Smoke-Test (~10:00 MESZ Briefing-Cron). Claude Code lädt neuen Key erst nach Restart.
- **Schema-Drift-Cleanup Phase 1 DONE** (`531f459`, 16 Files, +222/-18): 14 Phase-A-Source-Pages + Synthesis-Page `Wissenschaftliche-Fundierung-DEFCON.md` von quoted-string `related: "[[A]], [[B]]"` auf YAML-Block-Array konvertiert + fehlendes `sources: []` ergänzt. Pattern an McLean-Pontiff validiert (Karpathy-Surgical), Block-Form gewählt für Konsistenz mit bereits bestehender `aliases:`-Struktur. PyYAML-Bulk-Validation 14/14 PASS, Synthesis-Page 74 Wikilinks (sources 34 + concepts 23 + related 6 + entities 11) intakt. **Codex-Final-Run M1 closed.**
- **PIPELINE-Sync DONE**: Item #15 Phase-2-Schema-Drift (vault-wide ~30 weitere Pages) als Deferred angelegt + Long-Term-Gates Tavily-Entry auf Rotation #2 ~04.05.2026 aktualisiert.
- **Standing-Dirty unverändert** (gleiche Liste seit 26.04.): app.json, wiki/concepts/PORTFOLIO.md, gelöschte canvas/base/2026-04-23.md.

### 🎯 Nächster Task — Earnings-First

**Priorität 1 (operativ, zeitkritisch — verdrängt alles andere):**

- **28.04.** V Q2 FY26 (after market close, ~22:00 MEZ) — D2-Entscheidung (Technicals-Reversal?). Brief liegt: `02_Analysen/V_pre-earnings_2026-04-28.md` §6 Decision-Matrix, §7 Schritt-für-Schritt-Workflow.
- **29.04.** MSFT Q3 FY26 (after market close, ~22:30 MEZ) — FLAG-Review CapEx/OCF (bereinigt <60 % = Auflösung). Brief liegt: `02_Analysen/MSFT_pre-earnings_2026-04-29.md` §6 + §7. Wichtig: **finale FLAG-Entscheidung erst mit 10-Q** (Press-Release reicht nicht für Finance-Lease-Bereinigung).

**Priorität 2 (Tech-Debt, deferred):**

- ~~**Schema-Drift-Cleanup Phase 2 (vault-wide)**~~ **DONE 27.04. später Tagesabschnitt** (siehe oben + PIPELINE #15). Pre-Validation User-Sichtprüfung: Obsidian-Backlinks der Phase-2-Pages bei nächstem Vault-Open kurz checken (Phase-1-Pattern war 5h+ live ohne Bug-Report; konservative Annahme).
- **Backtest-Strategie mit Inhalt füllen** (User-Initiative 27.04. spät) — Brainstorm angefangen aber zugunsten Tavily/Schema-Drift vertagt. Status: 28 score_history-Records (24 Backfill-Stubs ohne metriken_roh + 4 Forward), 2 FLAG-Events, 5 Tage portfolio_returns. Infrastructure groß, analytischer Output dünn. Frage offen: welche Backtest-Frage soll der erste Substantielle-Output beantworten? (Score-Predictiveness, FLAG-Event-Study, Sparraten-Kaskade-Sim, Real-Backfill, ...). **Trigger:** eigener Slot, brainstorming-Skill startet von vorn.
- **Morning Briefing v3.0.4 Architektur-Phase** (PIPELINE #2 — **scope erweitert** vs. Hotfix-Plan, siehe NEXT-SESSION-RESUME oben) — gates Dashboard v2 + Track 5a/5b. **Foundation A1-A14 done (`7514ba7`)**. Eigener ungestörter Slot mit frischem Context-Window empfohlen — Brainstorming-Skill, B0 Provenance-Contract first, ~90-180 Min je nach Bucket-B-Reichweite.

### 🚨 Standing-Focus (operativ, unverändert)

- 28.04. V Q2 FY26 — D2-Entscheidung (Technicals-Reversal?) — Brief ready
- 29.04. MSFT Q3 FY26 — FLAG-Review (CapEx/OCF bereinigt <60% = Auflösung) — Brief ready

### Wichtige Notizen

- **Score-Archiv unangetastet** — kein DEFCON-Trigger in dieser Session, kein `score_history.jsonl`-Append.
- **DEFCON v3.7 unverändert**, 11 Satelliten-Scores unverändert, Sparraten unverändert, FLAG-Status unverändert.
- **Dynastie-Depot Skill v3.7.3** geladen, aber kein operativer Skill-Call.
- **Tavily-Key**: neuer Key live in PROD + lokal. Alten Key revoken erst nach Smoke-Test morgen.
- **CodeRabbit-CLI** verfügbar via WSL Ubuntu (Memory `feedback_coderabbit_via_wsl.md`).

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `CORE-MEMORY.md §13` + `PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*
