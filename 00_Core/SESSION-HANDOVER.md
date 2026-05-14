# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner:**
- **Datum:** 2026-05-14 (Do) abends — **Plugin-Integration Spec + Plan R3-konvergent, execution-bereit.** Pickup #1 aus 13.05.-Banner durchgezogen: Spec `docs/superpowers/specs/2026-05-14-plugin-integration-design.md` (5 Sparring-Runden R3+R4+R5, Confidence >97%) + Implementation-Plan `docs/superpowers/plans/2026-05-14-plugin-integration.md` v1.3 (3 R-Runden Codex+Gemini, **Codex 96% APPROVE + Gemini 97% APPROVE**, beide >95%-Gate). 30 Tasks über 4 Phasen + 90-Tage-Review. Plus Spec-Mini-Edit Welle-Definition Präzisierung (R1 Gemini HIGH-1 Anti-Self-Validation). DEFCON v3.7 + 11 Scores + Sparraten unverändert. Beide File-Sets sind gitignored unter `docs/superpowers/` (kein Repo-Commit). Pickup #2 aus 13.05.-Banner (CLAUDE.md-Review) NICHT angefasst — bleibt offen.

## 🎯 Resume-Anweisung für nächste Session

**User-Direktive 14.05. abends — Phase-0a-Execution in neuer Session für kontextfreies Window:**

1. **Pickup #A — Phase 0a Plugin-Integration starten** (Primär-Track). Plan: `docs/superpowers/plans/2026-05-14-plugin-integration.md` v1.3 R3-konvergent. Tasks 0–8 (Pre-Flight Environment + Plugin-Doku-Verify + Ruflo-Sunset-Cleanup + 24h Burn-in + Phase-0a-Gate). Aktive Arbeit ~60 min, danach 24h Burn-in-Wait, dann Phase-0b-Start frühestens 2026-05-15.
   - **Empfohlene Execution-Skill:** `superpowers:executing-plans` (Inline mit Checkpoint-Pause vor Task 7 24h-Burn-in) oder `superpowers:subagent-driven-development` (fresh subagent pro Task, harte Pause bei Burn-in).
   - **Optional Vor-Start:** 5-min Pending-Verify-Folgepass auf Task 6 Step 5b + Task 29 + Probe-Helper-Code für Confidence-Lift auf 99%+. Niedriges Risiko ohne — Gemini hat als „pending-Verify-akzeptabel" markiert.
   - **Pre-Flight Task 0** ist kritisch: 9 Steps die jq/Bash/chmod/Plugin-Pfade verifizieren. Output landet in gitignored `docs/superpowers/plans/2026-05-14-plugin-integration-preflight-notes.md` und ist Quelle für alle Downstream-Pfad-Substitutionen.

2. **Pickup #B — Root `CLAUDE.md`-Review & Verbesserung** (Sekundär, deferred aus 13.05.). Audit auf Post-Ruflo-Residuals + Optimierungspotenzial + Lazy-Load-Disziplin. Read-only Audit + Verbesserungs-Diff + USER-Decision-Gate. Trigger: „Pickup #B CLAUDE.md-Review".

**Default-Trigger:** „Session starten" → STATE.md + PORTFOLIO.md auto-load. Pickup #A triggert User explizit per „Phase 0a starten" oder „Pickup #A Plugin-Integration".

**Wichtig für Phase-0a-Start:** Plan ist gitignored → muss als `docs/superpowers/plans/2026-05-14-plugin-integration.md` direkt gelesen werden (kein git-checkout-Bezug). Spec analog gitignored.

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
