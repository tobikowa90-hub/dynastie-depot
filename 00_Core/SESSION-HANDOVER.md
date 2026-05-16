# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner:**
- **Datum:** 2026-05-16 (Sa) Europe/Berlin — **Pickup #D Obsidian-Skills-Vault-Bindung ✅ DONE** (5 Skills via WIKI-SCHEMA §Obsidian-Skills-Bindung gebunden, canvas+bases hart exkludiert, 6-File-Footprint atomar, scoring-neutral; davor Audit-FAIL-Resolve SESSION-HANDOVER:21 Dangling-Ref → Audit 14/15 grün). **Phase-0a KOMPLETT (Gate ✅ PASS) + Phase-0b PF-1 ✅ DONE.** Phase-0a-Burn-in ~48h: `hook-errors.log` Δ=0 vs Baseline 0 + Performance User-bestätigt unauffällig (Commit `0468ac5`). **PF-1 entschieden: Option C verbindlich** (Codex-Single-Pass-konvergent, User-bestätigt 2026-05-16) — Decision-Trail + 4 Patch-Drafts (NICHT applied, Apply-Gate Task 18 post-Task-10-PASS) in `docs/superpowers/plans/2026-05-14-plugin-integration-pf1-resolution.md` (gitignored). **PF-2 PASS** (Adherence-only). **Harter Blocker: Task 9** (claude-mem Throwaway-Verify) nicht agent-autonom → User-Hands-on, gated davor. Latency-Mess-Quelle option-b `03_Tools/hook-latency-probe.py`. Rollback-Artefakte intakt. DEFCON v3.7 + 11 Scores + Sparraten 285€ unverändert.

## 🎯 Resume-Anweisung für nächste Session

**Primär-Track: Phase 0b Plugin-Onboarding (User-getriggert).**

1. **Pickup #A — Phase 0a Gate-Check ✅ DONE 2026-05-16** (Commit `0468ac5`). Burn-in PASS (hook-errors.log Δ=0, ~48h, Performance User-bestätigt) + Task-8-Gate-Stempel komplett (PIPELINE #64 Numbering-Removal + STATE Critical-Alert + Vault log.md). **→ Nachfolge: Phase 0b Plugin-Onboarding** (Plan `docs/superpowers/plans/2026-05-14-plugin-integration.md` v1.3 R3-konvergent, Tasks 9-20). **Achtung Task 9** (claude-mem Stop-Haiku Throwaway-Verify): braucht 3-4 manuelle interaktive Claude-Code-Sessions im Throwaway-Projekt `~/throwaway-claudemem-verify` — **nicht agent-autonom durchlaufbar**, User-Hands-on. **Memory-Guard-Rail wird ab Phase 0b in `CLAUDE.md` aktiv** (Plan-Invariante: Live-State PORTFOLIO.md/STATE.md/INSTRUKTIONEN.md hat absolute Priorität über jeden Memory-Inject; aktuell noch NICHT in CLAUDE.md verankert — Phase-0b-Task). **Trigger:** „Phase 0b starten" — User-initiiert. **Bei Burn-in-Spät-FAIL** (hook-errors >5 / persistent slow nachträglich): STOP, Rollback via Tarball `~/.claude/helpers-pre-sunset-2026-05-14.tar.gz` + `~/.claude/settings.json.pre-plugin-integration-2026-05-14.bak` (intakt).

**🛫 Phase-0b Pre-Flight-Checks — ✅ PF-1 + PF-2 DONE 2026-05-16** (Resolution-File `docs/superpowers/plans/2026-05-14-plugin-integration-pf1-resolution.md`). Block unten = Historie/Kontext, nicht mehr abzuarbeiten:

> Verifiziert 2026-05-16: Spec `docs/superpowers/specs/2026-05-14-plugin-integration-design.md` + Plan decken die Memory-Funktion systemweit + phasenrichtig ab; „kein-Parallel-Betrieb" ist zentraler Design-Pfeiler (Spec §1/§2 ablösen·alleinige; Plan **Task 15** autoMemory/Dream-disable nach Verify-Gate Task 9→10; **Task 11/13** Tier-1-Triage+Snapshot gegen Info-Loss; **Task 18** Guard-Rail Anhang B). End-Zustand designed, aber NOCH NICHT in Kraft — natives autoMemory + claude-mem koexistieren aktuell capture-only by-design bis Task-15-Kill-Switch.

- **PF-1 (Caveat-#2, Spec-interne Wortlaut-Drift — vor Task 18 lösen):** Live-State-Absolute-Priority-File-Set ist in Spec **§3 Z.52** = „PORTFOLIO / STATE / **SYSTEM / log.md / score_history.jsonl**", aber im operativen **Anhang-B-Guard-Rail-Block Z.265** (der real in CLAUDE.md landet) = „PORTFOLIO / STATE / **INSTRUKTIONEN**". Vor Task-18-Write entscheiden welches Set autoritativ ist (Empfehlung: Anhang-B-Set ist normativ für den CLAUDE.md-Block, da Routing-Kontext; §3 ist Architektur-Beschreibung — ggf. §3 an Anhang B angleichen oder Guard-Rail-Block um SYSTEM/log/score_history erweitern). Sonst landet ein ambiger normativer Block in CLAUDE.md — exakt die Ambiguität, die vermieden werden soll. ~5 min Spec-Read + USER-Decision.
- **PF-2 (Single-Memory-Kill-Switch-Disziplin):** Task 15 (autoMemory/Dream-disable) ist der EINZIGE Punkt der Parallelität eliminiert — strikt NUR nach Task-10-PASS ausführen; bei Task-9-Verify-FAIL bleibt natives autoMemory aktiv + claude-mem blockiert (Plan Z.710, kein Halb-Parallel-State). Reihenfolge 9→10→(11→13→14)→15 ist gate-kritisch, nicht umstellen.

2. **Pickup #B — Root `CLAUDE.md`-Review & Verbesserung** (Sekundär, deferred aus 13.05.). Audit auf Post-Ruflo-Residuals + Optimierungspotenzial + Lazy-Load-Disziplin. Read-only Audit + Verbesserungs-Diff + USER-Decision-Gate. Trigger: „Pickup #B CLAUDE.md-Review".

3. **Pickup #C — pre-commit-Substrate (Plugin-Layer-Phase-0b-Erweiterung)** (Tertiär, vorbereitet 14.05. spätabends, USER-OK). **Vorbedingung: Phase-0a Gate ✅ PASS.** **Status-Korrektur 2026-05-16 (Audit-FAIL-Resolve, Pickup-#D-Vorlauf):** Pickup #C wurde **NICHT** ausgeführt — Spec ist **nicht geschrieben** (Commit `36deaa0` = „scheduled post-Gate-PASS"; Phase-0a-Gate-Commit `0468ac5` Sync-Set = nur 3 Files, kein #C-Artefakt). Der Phase-0a-„im selben Commit-Set"-Konditional wurde bewusst nicht eingelöst (Pickup #C ist tertiär, separate Session). Bei Pickup-#C-Execution zu erstellen: (a) Spec v0.1 — Ablage-Verzeichnis `docs/superpowers/specs/`, Arbeitstitel 2026-05-15-pre-commit-substrate; Soll-Inhalt alle Sektionen (Hook-Inventar, Validator-Pseudocode für `xlsx_smoke_test.py` + `validate_score_history.py` + `validate_flag_events.py`, Pre-Existing-CRLF-Cleanup-Migration, Akzeptanzkriterien, Risiken, Rollback); (b) eigenes neues PIPELINE-OPEN-Item (**NICHT #62** — #62 wurde 14.05. dem Watchlist-Refresh SPGI+SNPS zugewiesen; #C bekommt eigene Nummer bei Execution) mit Spec-Pointer + Aufwand-Schätzung ~3-4h Setup + 1-2 Cleanup-Sessions. **Codex-Sparring auf Spec** vor Execution (Heuristik Memory `feedback_codex_sparring_heuristic.md` — Single-Pass-Default). Execution als separate Session. Motivation: pre-commit als git-Gate adressiert Cluster dokumentierter Friction-Patterns (CRLF-Text-Mode-Trap, Pre-Commit-Diff-Inspection, xlsx-Smoke-Test §18.7 Manual→Auto, JSONL-Schema-Drift-Detection für `score_history.jsonl` + `flag_events.jsonl`). Drop-in zu existing Ruff-Workflow, kein Konflikt zu CR/Codex (verschiedene Defect-Klassen). Trigger: „Pickup #C pre-commit-Spec".

4. **Pickup #D — Obsidian-Skills-Vault-Integration ✅ DONE 2026-05-16.** Plan `docs/superpowers/plans/2026-05-16-obsidian-skills-vault-integration.md` (gitignored) via `superpowers:writing-plans` geschrieben, Codex-Single-Pass-Rigor (FAIL→PASS, F-1/F-2 PIPELINE-Footer-Bump-Korrektur gegen #64/#56-Präzedenz + F-4 log.md-Anchor; F-3 self-disclaimed) + Diff-Re-Review PASS, dann inline ausgeführt. WIKI-SCHEMA §Obsidian-Skills-Bindung (nach §Workflows) + SYSTEM §Plugin-Layer + STATE-Alert + Banner + PIPELINE #65 Footer-Bump + Vault log.md in einem atomaren 6-File-Commit; #65 per Numbering-Convention angelegt+entfernt; scoring-neutral, `system_audit --core` 14/15 grün. Vorlauf-Fund: pre-existing Audit-FAIL (SESSION-HANDOVER:21 Dangling-Ref Pickup-#C-Spec) als eigener Commit resolved (siehe Pickup #3-Status-Korrektur oben). Spec `docs/superpowers/specs/2026-05-16-obsidian-skills-vault-integration-design.md`. **Nachfolge:** keine — Pickup-#D-Track geschlossen. Hinweis bleibt gültig: `cc-gemini-plugin`-Bridge defekt (Node-v20 `globSync`-Crash) — Cross-Sync künftig selbst-verifizieren oder Bridge-Fix als separates Item.

**Default-Trigger:** „Session starten" → STATE.md + PORTFOLIO.md auto-load. **Phase-0b-Pickup #A + PF-1 + PF-2 ✅ alle DONE 2026-05-16.** Nächster Schritt = **Task 9 (claude-mem Stop-Haiku Throwaway-Verify) — User-Hands-on, nicht agent-autonom** (3-4 interaktive Sessions in `~/throwaway-claudemem-verify` + Web-Viewer `http://127.0.0.1:37777`). User fährt Task 9 Steps 3-7, gibt PASS/WARN/FAIL-Verdikt zurück → Agent übernimmt ab Task 10 (inkl. PF-1-Patch-Apply bei Task 18 post-Task-10-PASS). **Trigger für Agent-Wiedereinstieg:** „Task 9 Verdikt: <PASS/WARN/FAIL> + <Befund>" oder „Phase 0b ab Task 10".

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
