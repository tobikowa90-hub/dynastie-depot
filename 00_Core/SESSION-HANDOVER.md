# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner:**
- **Datum:** 2026-05-16 (Sa) Europe/Berlin — **Phase-0b ENTSCHIEDEN via HYBRID (empirisch verifiziert, Codex-gate-konform).** Reise: Task-9-Diagnose ergab claude-mem war **nie in enabledPlugins** (0 Capture, kein Windows-Defekt). User-Direktive „testen statt annehmen" → claude-mem enabled (`~/.claude/settings.json`, Backup `~/.claude/settings.json.pre-claudemem-enable-2026-05-16.bak`), Bun installiert (harte Dependency, Stop-Hook crashte `non-blocking` ohne), Git-Bash-Login-PATH via `~/.bash_profile` gefixt (User-autorisiert, Block-Marker `claude-mem-bun-path 2026-05-16`). 3 isolierte Throwaway-Sessions → `~/.claude-mem/claude-mem.db`: claude-mem capturt SAUBER (11 Obs + 6 Haiku-Summaries, strukturiert, FTS, passiver SessionStart-Summary-Load), Modell = append-only Event-Log (kein hartes Dedup/Merge/Storage-Konflikt-Resolution, ABER Summary-Layer narriert Korrektur-Trajektorie kohärent). User-Einsicht (konzediert): Trajektorie-Memory semantisch reicher + Dynastie-konsistent (score_history.jsonl/git-log-Philosophie). Single-Projekt → Project-Label „Claude Stuff" korrekt, kein Konflikt. **Codex Final-Single-Pass (frischer Thread): Q1 Hybrid JA, Q3 Lean-Formalisierung JA, Q4 93%→>95% via Wortlaut-Verengung der Bun-Invariante (Option a, kein Loop — angewandt).** DEFCON v3.7 + 11 Scores + Sparraten 285€ unverändert (scoring-neutral). **⚠️ Commit `cb58e1a` (CLAUDE.md/SYSTEM.md „claude-mem nicht enabled") ist jetzt STALE — claude-mem IST enabled; Korrektur = Teil der Rest-Formalisierung.**

## 🎯 Resume-Anweisung für nächste Session

**Primär-Track: Phase-0b HYBRID Lean-Formalisierung (agent-fahrbar, frische Session).**

Entscheidung steht (siehe Status-Banner): **autoMemory = kanonisches System-of-Record + Live-State absolute Priorität, unangetastet, KEIN Task 15 / KEIN autoMemory-Disable. claude-mem = rein additiver read-only Augmentation-Layer, enabled, capture-only, nie kanonisch.** Hybrid-Zustand operativ schon erreicht (claude-mem enabled+getestet, autoMemory unberührt, Bun gefixt). Es fehlt nur die Doku-Formalisierung — **kein neuer writing-plans-Zyklus** (Codex Q3 bestätigt). Der alte Plan `docs/superpowers/plans/2026-05-14-plugin-integration.md` + Re-Scope-Plan `2026-05-16-phase0b-optionB-rescope.md` (v1.1) sind **OBSOLET** (reines Option-B = claude-mem-weg, durch Hybrid überholt) → beide mit SUPERSEDED-Header markieren.

**Rest-Formalisierung (5 Schritte, agent-autonom; CLAUDE.md normativ → Diffs vor Commit dem User zeigen):**

1. **CLAUDE.md + `00_Core/SYSTEM.md` §Plugin-Layer → Hybrid-Final-State.** Ersetzt die stale `cb58e1a`-Aussage. Wortlaut: claude-mem additiv-augmentativ enabled (capture-only, nie SSoT), autoMemory kanonisch + Live-State-Priorität, **Bun-Invariante VERENGT** (Codex-Q4-Fix, kein Loop): „Bun/Dependency-Failure = empirisch belegte graceful degradation (beobachtet: Stop-Hook bei fehlendem Bun `non-blocking`, autoMemory+Session unberührt); andere künftige Hook-Failure-Klassen nicht universell garantiert, aber durch additiv/non-kanonisch-Design strukturell eingegrenzt." Bun-PATH-Fix-Hinweis (`~/.bash_profile` Marker `claude-mem-bun-path 2026-05-16`).
2. **Memory-Guard-Rail in CLAUDE.md verankern** (jetzt RELEVANT: claude-mem injiziert Observation-Summary passiv bei SessionStart). Block-Wortlaut = alter Plan `2026-05-14-plugin-integration.md` **Task 18 Step 2** (5-Punkte-Block) + **PF-1 Option-C Semantic-Split** aus `2026-05-14-plugin-integration-pf1-resolution.md` §3.1-§3.4 (Punkt-1-Routing-Inputs = PORTFOLIO/STATE/INSTRUKTIONEN; Punkt-4-Daten-Priorität = SYSTEM/log.md/score_history.jsonl), Wortlaut `claude-mem/semantic injects` → `recalled autoMemory + claude-mem Observation-Summary`. Einfügeposition: CLAUDE.md vor `**Edge-Cases der Match-Regel:**`. Token-Diff-Check (+180…+250 words Budget, TOKEN-RULES).
3. **Cleanup:** `rm -rf ~/throwaway-claudemem-verify` + `~/.claude-mem/`-Test-Records optional behalten (Single-Projekt = kein Pollution; Entscheidung User). `~/.claude-mem` Produktiv-Store NICHT löschen (ist jetzt Live-Augmentation). settings.json-Backups behalten. **Produktiv-Memory-Dir war clean (verifiziert), kein Cleanup nötig.**
4. **Sync (§18 System-Event, scoring-neutral, atomar):** SESSION-HANDOVER (Banner→DONE) + STATE.md Critical-Alert + `00_Core/PIPELINE.md` (Phase-0b-Hybrid-DONE-Item + obsolete Option-B-Items markieren, Numbering-Convention + Footer-Aktivliste — Codex-HIGH-Lehre aus Option-B-Review) + Vault `log.md` + CLAUDE.md + SYSTEM.md = **ein** atomarer Commit. Pre-Commit-Diff-Inspection + STATE.md-pre-existing-dirty-Check (Memory `feedback_pre_commit_diff_inspection`, nicht-interaktiv: bei unrelated → STOP+User). Here-doc Commit-Msg (Memory `feedback_powershell_herestring_in_bash_tool`).
5. **Memory-Lehre:** `feedback_plan_on_runtime_not_doc_assumption.md` (Test-statt-Annahme zahlte sich aus — claude-mem-nie-enabled-Präzedenz; Hybrid-Begründung; verknüpft [[feedback_review_via_codex_not_advisor]] [[feedback_codex_sparring_heuristic]]) + MEMORY.md-Index-Zeile.

**Trigger:** „Hybrid-Formalisierung" oder „Phase 0b ab Schritt 1". **Backups intakt:** `~/.claude/settings.json.pre-claudemem-enable-2026-05-16.bak`. **Codex-Verdikt-Quelle:** dieser Banner (Final-Single-Pass, agentId siehe git log dieser Session; >95% via Bun-Wortlaut-Verengung — KEIN weiterer Codex-Loop nötig, User-Direktive).

2. **Pickup #B — Root `CLAUDE.md`-Review & Verbesserung** (Sekundär, deferred aus 13.05.). Audit auf Post-Ruflo-Residuals + Optimierungspotenzial + Lazy-Load-Disziplin. Read-only Audit + Verbesserungs-Diff + USER-Decision-Gate. Trigger: „Pickup #B CLAUDE.md-Review".

3. **Pickup #C — pre-commit-Substrate (Plugin-Layer-Phase-0b-Erweiterung)** (Tertiär, vorbereitet 14.05. spätabends, USER-OK). **Vorbedingung: Phase-0a Gate ✅ PASS.** **Status-Korrektur 2026-05-16 (Audit-FAIL-Resolve, Pickup-#D-Vorlauf):** Pickup #C wurde **NICHT** ausgeführt — Spec ist **nicht geschrieben** (Commit `36deaa0` = „scheduled post-Gate-PASS"; Phase-0a-Gate-Commit `0468ac5` Sync-Set = nur 3 Files, kein #C-Artefakt). Der Phase-0a-„im selben Commit-Set"-Konditional wurde bewusst nicht eingelöst (Pickup #C ist tertiär, separate Session). Bei Pickup-#C-Execution zu erstellen: (a) Spec v0.1 — Ablage-Verzeichnis `docs/superpowers/specs/`, Arbeitstitel 2026-05-15-pre-commit-substrate; Soll-Inhalt alle Sektionen (Hook-Inventar, Validator-Pseudocode für `xlsx_smoke_test.py` + `validate_score_history.py` + `validate_flag_events.py`, Pre-Existing-CRLF-Cleanup-Migration, Akzeptanzkriterien, Risiken, Rollback); (b) eigenes neues PIPELINE-OPEN-Item (**NICHT #62** — #62 wurde 14.05. dem Watchlist-Refresh SPGI+SNPS zugewiesen; #C bekommt eigene Nummer bei Execution) mit Spec-Pointer + Aufwand-Schätzung ~3-4h Setup + 1-2 Cleanup-Sessions. **Codex-Sparring auf Spec** vor Execution (Heuristik Memory `feedback_codex_sparring_heuristic.md` — Single-Pass-Default). Execution als separate Session. Motivation: pre-commit als git-Gate adressiert Cluster dokumentierter Friction-Patterns (CRLF-Text-Mode-Trap, Pre-Commit-Diff-Inspection, xlsx-Smoke-Test §18.7 Manual→Auto, JSONL-Schema-Drift-Detection für `score_history.jsonl` + `flag_events.jsonl`). Drop-in zu existing Ruff-Workflow, kein Konflikt zu CR/Codex (verschiedene Defect-Klassen). Trigger: „Pickup #C pre-commit-Spec".

4. **Pickup #D — Obsidian-Skills-Vault-Integration ✅ DONE 2026-05-16.** Plan `docs/superpowers/plans/2026-05-16-obsidian-skills-vault-integration.md` (gitignored) via `superpowers:writing-plans` geschrieben, Codex-Single-Pass-Rigor (FAIL→PASS, F-1/F-2 PIPELINE-Footer-Bump-Korrektur gegen #64/#56-Präzedenz + F-4 log.md-Anchor; F-3 self-disclaimed) + Diff-Re-Review PASS, dann inline ausgeführt. WIKI-SCHEMA §Obsidian-Skills-Bindung (nach §Workflows) + SYSTEM §Plugin-Layer + STATE-Alert + Banner + PIPELINE #65 Footer-Bump + Vault log.md in einem atomaren 6-File-Commit; #65 per Numbering-Convention angelegt+entfernt; scoring-neutral, `system_audit --core` 14/15 grün. Vorlauf-Fund: pre-existing Audit-FAIL (SESSION-HANDOVER:21 Dangling-Ref Pickup-#C-Spec) als eigener Commit resolved (siehe Pickup #3-Status-Korrektur oben). Spec `docs/superpowers/specs/2026-05-16-obsidian-skills-vault-integration-design.md`. **Nachfolge:** keine — Pickup-#D-Track geschlossen. Hinweis bleibt gültig: `cc-gemini-plugin`-Bridge defekt (Node-v20 `globSync`-Crash) — Cross-Sync künftig selbst-verifizieren oder Bridge-Fix als separates Item.

**Default-Trigger:** „Session starten" → STATE.md + PORTFOLIO.md auto-load. **Phase-0b via HYBRID entschieden + Codex-gate-konform 2026-05-16** (claude-mem empirisch getestet, funktioniert, additiv enabled; autoMemory kanonisch unberührt). Nächster Schritt = **Hybrid-Lean-Formalisierung 5 Schritte (agent-autonom, oben gelistet)** — kein User-Hands-on, kein neuer Plan-Zyklus, kein Codex-Loop. **Trigger für Agent-Wiedereinstieg:** „Hybrid-Formalisierung" oder „Phase 0b ab Schritt 1". Task 9/10/15/Pre-Flight-Block oben = HISTORIE (Hybrid überholt sie — claude-mem nie disablen, autoMemory nie disablen).

**Wichtig für Re-Entry:** Plan gitignored → muss als `docs/superpowers/plans/2026-05-14-plugin-integration.md` direkt gelesen werden. Pre-Flight-Verdict-File ebenfalls gitignored aber referenziert in Plan-Task-6/7/8.

**Phase-0a Tasks 0-6 In-Session Detail (für Re-Entry-Kontext):**
- Task 0: Verdict-File geschrieben. Findings: chmod-on-NTFS effective (Git-Bash 5.3.9 cygwin emul, Plan-Annahme „no-op" widerlegt); context-mode v1.0.124 outdated → v1.0.130 (deferred); hook-timing/errors.log NOT-PRESENT (Plugin emittiert noch nicht); Web-Viewer-Port `37777` (Windows uid=undefined fallback 77); /ctx-stats hat KEIN p95 + KEINE Tool-Klassen-Decomposition → Task 6 Option (b); context-mode KEIN Env-Disable → Task 23 memory-only-rollback.
- Task 1: settings.json + helpers/-Tarball (42 entries) gesichert.
- Task 2: **Plan-Count-Mismatch:** Plan sagte „4 Hooks" — Realität 13 entfernte helpers-Einträge; 1 context-mode-Hook erhalten; file 6844→3002 bytes.
- Task 3: 41 Files in `~/.claude/helpers/_legacy_2026-05-14/`.
- Task 4: 279MB Recovery (user explicit-auth nach Auto-Mode-Classifier-Block).
- Task 5: **User-Choice option-a Full-Cleanup:** Skills 24 Plan-loop + 5 github-* = 29 in _legacy_; Agents 3 Plan-loop + 20 dirs = 23 in _legacy_. Plus Slash-Commands (Plan adressierte nicht): 10 entries (7 namespaces + 3 .md) → `~/.claude/_legacy_archive_2026-05-14/commands/` (OUTSIDE discovery).
- Task 6: `03_Tools/hook-latency-probe.py` 90 LOC + .gitignore-Eintrag für `03_Tools/hook-latency-history/`. Smoke-Run: no_data-Audit-Record persisted (exit 2, Plan-erwartet). system_audit.py: 14/15 PASS unverändert.

### 📅 Nächste reguläre Termine (chronologisch)

| Datum | Item | Aktion |
|-------|------|--------|
| **14.05.** | Form-13F Apple-Trim (#37) + MSFT Insider-Re-Score (#26) | Form-13F BRK CIK 0001067983 via SEC EDGAR + insider_intel.py MSFT post-14d-Skip-Window |
| **27.05.** | VEEV Q1 FY27 | Klasse-B Earnings (yfinance-Pull 30.04. confirmed) |
| **28.05.** | COST Q3 FY26 | Klasse-B Earnings (Membership-Yield-Watch) |

### 📋 Pending offene Slots (kein fester Termin)

- **PIPELINE #42.3** G3 3-Felder-Konsistenz-Check Tooling — Phase-2a-Slot ab ~13.05.
- **PIPELINE #48** Codebase-Defect-Pattern-Audit (~7-10h, eigene Session) — taxonomische Pattern-Map über 03_Tools/ + 01_Skills/-SKILL.md-Logic
- **PIPELINE #52** Quick-Screener-Refresh deferred bis Use-Case-Trigger (10 Drift-Dimensionen audit'd)
- **PIPELINE #53** ✅ Decision-C USER-APPROVED 10.05. — Weiter beobachten + Re-Audit ~09.07.2026 mit Use-Case-Count-Tracking; Schwellen ≥2/1/0 → ACTIVE/Repeat-C/Archivieren (Memory `project_trigger_landscape_audit_2026-05.md`)

### 🔬 Phase-D-Restbestand (deferred per Cluster-Trigger)

- **Phase-D-2 active-deferred-D2 Cluster:** EP-2013 + EKP-2020 → V Q3 FY26 ROIC-Methodology-Verify ~Ende Juli (PIPELINE #21)
- **Phase-D-2 meta-gate-deferred-D2:** BS-2015 → 2028-Review-Gate ODER nächste DEFCON-Block-Re-Gewichtung
- **Phase-D-3 source-only-deferred-D3:** CPZ-2019 → 2028-Review-Gate Backtest-Validation-Wave
- **Phase-D Reject-Inventarisiert:** BPZ-2023 → Latent für 2028-Review-Gate Backtest-Methodology-Roadmap

## 🔖 Vorgänger-Historie

Vorherige Banner-Versionen + Phase-D-1-Final-Closure 09.05. + Konsolidierungstag-Wave-1/2/3/4 + Cluster-A-#31/#32/#33/#34 + Wiki-Modus-#54 + AVGO/MSFT/V/BRK.B/APH-Vollanalysen → **git log + STATE.md Critical-Alerts (≤10-Tage-Window) + CORE-MEMORY.md §13 (System-Lifecycle) + Vault `log.md` + `archive/log/` (vollständige History; quartalsweise Roll-over per INSTRUKTIONEN §18.6, Initial-Cut 10.05.2026)**.

**Skill-Versions-Stempel:** dynastie-depot v3.7.6 (SKILL §410 + §27.7-Anti-Buyback-Cross-Reference + Bull-DCF-Source-Pflicht + ATH-Distance-Boundaries; keine Versions-Bump bei Confidence-Upgrade-Pass — nur Begründungs-Härtung). User-Manual-Step bei Skill-Edits: `06_Skills-Pakete/dynastie-depot_v3.7.6.zip` neu deployen + Desktop-App-Install.
