# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner:**
- **Datum:** 2026-05-16 (Sa) Europe/Berlin — **Phase-0a KOMPLETT: Tasks 0-8 DONE, Gate ✅ PASS.** Burn-in ~48h: `hook-errors.log` Δ=0 vs Baseline 0 (Schwelle 0-5 ✅) + Performance User-bestätigt unauffällig. Commit `0468ac5` (PIPELINE #64 Numbering-Removal + STATE Critical-Alert + Vault log.md, scoring-neutral). **Phase 0b freigegeben** (Tag-3 ~2026-05-16, Plan-konform) — als User-getriggerter Pickup, nicht auto-eingestiegen (Phasengrenze-Pause). Latency-Mess-Quelle option-b `03_Tools/hook-latency-probe.py`. Rollback-Artefakte intakt (nicht getriggert). Vorgänger-Commit `6f75a52` (hook-latency-probe.py + .gitignore). DEFCON v3.7 + 11 Scores + Sparraten 285€ unverändert.

## 🎯 Resume-Anweisung für nächste Session

**Primär-Track: Phase 0b Plugin-Onboarding (User-getriggert).**

1. **Pickup #A — Phase 0a Gate-Check ✅ DONE 2026-05-16** (Commit `0468ac5`). Burn-in PASS (hook-errors.log Δ=0, ~48h, Performance User-bestätigt) + Task-8-Gate-Stempel komplett (PIPELINE #64 Numbering-Removal + STATE Critical-Alert + Vault log.md). **→ Nachfolge: Phase 0b Plugin-Onboarding** (Plan `docs/superpowers/plans/2026-05-14-plugin-integration.md` v1.3 R3-konvergent, Tasks 9-20). **Achtung Task 9** (claude-mem Stop-Haiku Throwaway-Verify): braucht 3-4 manuelle interaktive Claude-Code-Sessions im Throwaway-Projekt `~/throwaway-claudemem-verify` — **nicht agent-autonom durchlaufbar**, User-Hands-on. **Memory-Guard-Rail wird ab Phase 0b in `CLAUDE.md` aktiv** (Plan-Invariante: Live-State PORTFOLIO.md/STATE.md/INSTRUKTIONEN.md hat absolute Priorität über jeden Memory-Inject; aktuell noch NICHT in CLAUDE.md verankert — Phase-0b-Task). **Trigger:** „Phase 0b starten" — User-initiiert. **Bei Burn-in-Spät-FAIL** (hook-errors >5 / persistent slow nachträglich): STOP, Rollback via Tarball `~/.claude/helpers-pre-sunset-2026-05-14.tar.gz` + `~/.claude/settings.json.pre-plugin-integration-2026-05-14.bak` (intakt).

2. **Pickup #B — Root `CLAUDE.md`-Review & Verbesserung** (Sekundär, deferred aus 13.05.). Audit auf Post-Ruflo-Residuals + Optimierungspotenzial + Lazy-Load-Disziplin. Read-only Audit + Verbesserungs-Diff + USER-Decision-Gate. Trigger: „Pickup #B CLAUDE.md-Review".

3. **Pickup #C — pre-commit-Substrate (Plugin-Layer-Phase-0b-Erweiterung)** (Tertiär, vorbereitet 14.05. spätabends, USER-OK). **Vorbedingung: Phase-0a Gate ✅ PASS.** Bei PASS im selben Commit-Set wie Gate-DONE: (a) Spec `docs/superpowers/specs/2026-05-15-pre-commit-substrate.md` v0.1 — voll ausgearbeitet, alle Sektionen (Hook-Inventar, Validator-Pseudocode für `xlsx_smoke_test.py` + `validate_score_history.py` + `validate_flag_events.py`, Pre-Existing-CRLF-Cleanup-Migration, Akzeptanzkriterien, Risiken, Rollback); (b) PIPELINE #62 OPEN-Item mit Spec-Pointer + Aufwand-Schätzung ~3-4h Setup + 1-2 Cleanup-Sessions. **Codex-Sparring auf Spec** vor Execution (Heuristik Memory `feedback_codex_sparring_heuristic.md` — Single-Pass-Default). Execution als separate Session. Motivation: pre-commit als git-Gate adressiert Cluster dokumentierter Friction-Patterns (CRLF-Text-Mode-Trap, Pre-Commit-Diff-Inspection, xlsx-Smoke-Test §18.7 Manual→Auto, JSONL-Schema-Drift-Detection für `score_history.jsonl` + `flag_events.jsonl`). Drop-in zu existing Ruff-Workflow, kein Konflikt zu CR/Codex (verschiedene Defect-Klassen). Trigger: „Pickup #C pre-commit-Spec".

**Default-Trigger:** „Session starten" → STATE.md + PORTFOLIO.md auto-load. Pickup #A triggert User explizit per „Phase 0a Gate-Check".

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
