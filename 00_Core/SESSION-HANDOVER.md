# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner:**
- **Datum:** 2026-05-13 (Mi) abends — **M001 'Ruflo Full Cleanup' COMPLETE**: S01 (config + 00_Core ruflo-free, commit 7875be9) + S02 (R005-R007 + R013-R019 Auto-Memory + g3_consistency + Cross-Refs + Final-Verify, commit eddee14) + Housekeeping Stray-Files + .gsd.migrating-Untracking (7514ff0) + GSD-Tooling Komplett-Removal (8f7c593). Acceptance-Criteria pass: `rg -i ruflo` nur Allowlist + `system_audit.py --core` 14/15 PASS 0 FAIL Exit 0 + 0 orphan imports. Aktive Plugins: context-mode v1.0.124 + claude-mem v6.5.0 (passive Substrate, integriert in `00_Core/SYSTEM.md §Plugin-Layer`). DEFCON v3.7 + 11 Scores + Sparraten unverändert. Working tree clean nach 4 atomaren Commits dieser Session.

## 🎯 Resume-Anweisung für nächste Session

**User-Direktive 13.05. abends — zwei Pickup-Topics für nächste Session:**

1. **Brainstorming: Optimale + vollumfängliche Integration der aktuellen Plugins context-mode + claude-mem.** Aktuell beide als passive Substrate installiert (nur SYSTEM.md §Plugin-Layer-Dokumentation, keine aktive Workflow-Anbindung). Brainstorm-Trigger: welche Workflows (DEFCON-Vollanalyse / earnings-recap / briefing-sync / system_audit / Wiki-Ingest) profitieren von welchem Plugin-Feature (context-mode Tool-Output-Sandbox + FTS5-Index vs claude-mem Cross-Session-Memory + Chroma)? Mapping → konkrete Routing-Table-Trigger oder SKILL-Phase-Anbindung. Output: spec-Draft + USER-Decision-Gate.

2. **Root `CLAUDE.md`-Review & Verbesserung.** Aktuelle Projekt-CLAUDE.md prüfen auf: (a) post-Ruflo-Sunset-Residuals (Wortlaut-Drift in Routing-Table / Pointer / §-Refs); (b) Optimierungspotenzial — was kann lean-er, klarer, wertvoller? (c) Lazy-Load-Disziplin (Skill-Auto-Trigger seit 09.05. verengt — ist Wortlaut-Tight? Memory `feedback_skill_lazy_load_dual_trigger_source.md`). Vorgehen: read-only Audit + Verbesserungs-Diff-Vorschlag + USER-Decision-Gate vor Apply.

**Default-Trigger:** „Session starten" → STATE.md + PORTFOLIO.md auto-load. Falls direkt einer der beiden obigen Pickups gewünscht: User triggert explizit per "Pickup #1 Plugin-Integration" oder "Pickup #2 CLAUDE.md-Review".

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
