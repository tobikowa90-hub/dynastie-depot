# 🎯 STATE.md — Dynasty-Depot Hub

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — Offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Infrastruktur / Briefing / Backtest-Ready
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13)
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Banner-Chronik

## ⚠️ Critical-Alerts (≤ 10 Tage — handgepflegt)

> **Konvention (11.05.2026 Slim-Refactor):** Critical-Alerts sind 1-3-Zeilen-Pointer. Sub-Detail-Decomposition (A/B/C/D… + §18-Sync-Set + bewusst-NICHT-angefasst) gehört NICHT hierher — kanonische Archivquelle ist `git log` (Commit-Body) + `CORE-MEMORY.md §13` (Lifecycle) + PIPELINE-Item-Body bei aktiven Items.

- **14.05. (Do) ✅ PIPELINE #61 DONE Retrospektive Top-5-Retry-Sessions** (System-Event, scoring-neutral). 5 Transcript-Scans via `ctx_execute_file` (Lean-Context-Pre-Activation eingehalten); Cluster-Decomposition: ~95% der CodeBurn-"retries" sind §18-Sync-Wellen / TaskCreate-Bursts / Bulk-Mut / Multi-Step-Compute — **echte §0.6-Hits ~4–7 Mikro-Cases** über alle 5 Sessions. §0.6-Definition selbst deckt echte Cases sauber → **kein Tweak**, neue Memory `feedback_codeburn_retry_metric_calibration` als Reading-Disziplin-Anker. Detail → CORE-MEMORY §13.
- **13.05. (Mi) ✅ Plugin-Substrate-Refactor DONE** (System-Event, scoring-neutral). Substrate-Layer ausgetauscht, aktive Plugins: context-mode + claude-mem. DEFCON v3.7 + Scores + Sparraten unverändert. Detail → CORE-MEMORY §13.
- **11.05. (Mo) ✅ Codebase-Defect-Pattern-Audit + G3-Tooling + Sum-Consistency DONE** (Spec 2026-05-11 v1.1 + Plan v1.2). M1-M5 + L1-L7 + Z1-Z3 G3-Check + Sum-Consistency-Audit-Check applied (Option C, schema_version-Allowlist). Apply-Phase-Empirie revealed Group-C `le=10` retroactively breaks 24 legacy v1.0 records (fwd_pe ∈ [29, 44]) → bounds REVERTED, bounds-check deferred to audit-layer follow-up. Validation-Matrix 12/15 hard-hit PASS + 2 N/A conditional → ≥12/15 threshold met (`05_Archiv/superpowers-pre-sunset/specs/2026-05-11-codebase-defect-patterns-validation.md`). System-Audit 14/16 → 15/18 PASS (zwei neue Checks `g3_consistency` + `sum_consistency`). CR-CP1 + CP2 applied (5 findings total incl. CRITICAL string-version-compare bug). PIPELINE #48 + #42 DONE — entfernt.
- **11.05. (Mo) ✅ Prod-Cutover Briefing v3.1.1 → v3.2.0 DONE** (D-pre AIDEFENCE-Block + FAIL-OPEN-Pfad live). Probe-Run 11:30 PASS, Prod-Body-Push via UI-Edit 13:56 MESZ, Verify via `RemoteTrigger get` Hash-Match. PIPELINE #51 ✅ DONE final. Nächster Prod-Cron Di 12.05. 10:07 MESZ. **Plus PORTFOLIO.md-Slim-Refactor** (80→65 LOC, ~5k Token Save: Vorgeschichte-Quotes 17.04.→04.05. raus, 2 resolved Watches archiviert, DONE-Trigger-Zeilen entfernt). **Plus STATE.md-Slim-Refactor** (dieser Commit, 11 Mega-Bullets vom 04.-10.05. kondensiert auf 1-3-Zeilen-Pointer, ~22k Token Save). **Plus Doctor-Mo-Anker** Wave-3a Woche 2/4 (7P/7W/0F, Snapshot im Doctor-History-Archiv). Scoring-neutral. Detail → git log + PIPELINE #51 + SYSTEM.md §Briefing-Status v3.2.0.
- **11.05. (Mo) abends ✅ QuickWin-Sweep — System-Audit FAIL-Resolve + PIPELINE #56 Archive** — Slash-Doku-Drift `SystemAudit.md` Count 14→16 (zwei neue Checks `sum_consistency` + `g3_consistency` heute promoted). Re-Run **16/18 PASS, 0 FAIL, 2 WARN** (Check-2/5 Design-akzeptiert). PIPELINE #56 xlsx-Smoke-Test §18 v2.3→v2.4 DONE per Numbering-Convention aus Aktiv-Liste entfernt. Sync-Set 5 Files atomar. Scoring-neutral.
- **10.05. (So) ✅ Audit-Cleanup-Pack** — System-Audit 12/16 → 14/16 PASS, vault_backlinks Tool-Extension (Skip Inline-Backticks + Frontmatter-Aliases-Resolution + archive/log skip). → commits `6cf995b` + `1cc86fa`.
- **10.05. (So) ✅ PIPELINE #51 Cloud-AIDefence Decision USER-APPROVED Option (c) Akzeptanz** + **#53 Trigger-Landschafts-Audit Decision-C USER-APPROVED** (Weiter beobachten, Re-Audit ~09.07.). Decision-Doc `05_Archiv/superpowers-pre-sunset/specs/2026-05-10-cloud-aidefence-decision.md` (gitignored). FAIL-OPEN-Akzeptanz im Cloud-Cron, Memory-Note `project_trigger_landscape_audit_2026-05.md` für Re-Audit-Schwellen. → commit `14b4cde` + PIPELINE #51/#53.
- **10.05. (So) ✅ PIPELINE #55 Phase-D-1 Confidence-Upgrade-Pass** — Voll-PDF-Read von 8 Papers + 9 Sachfehler-Korrekturen B29/B30 + 6 neue Source-Pages (D-2/-3-Stubs + Reject) + 11 Author-Stubs + SKILL §410 3 Präzisierungen + Wiss-Fundierung-Synthesis 8 Vollend-Edits. Codex 2-Round-Sparring 88%→96% PASS. Wiki-only, scoring-neutral. → git log + Vault log.md + PIPELINE #55 (Phase D-2/-3 deferred).
- **09.05. (Sa) ✅ PIPELINE #55 Phase-1 (Gemini-Recherche-Triage)** — 8 Paper-Vorschläge triagiert, 2 Top-Picks Peters/Taylor + DHS als active-scoring-validation persistiert (4 neue Wiki-Pages B29/B30 + 5 Author-Stubs + SKILL §410-Anker-Härtung). Codex 96% APPROVE. → git log + Vault log.md + PIPELINE #55.
- **09.05. (Sa) ✅ PIPELINE #22 Helper `--porcelain -z`-Robust-Refactor** — `_forward_verify_helpers.py::check_freshness` bytes-NUL-Split + Rename/Copy-Two-Path (Quote-Escape / Umlaut / Newline-im-Pfad gefixt). 6 neue Edge-Case-Tests + 14/14 PASS. Codex 96%. → git log + CORE-MEMORY §13.
- **09.05. (Sa) ✅ PIPELINE #34 DCF-Malus Bull-Source-Schema-Pflicht (AVGO-Cluster-A Closure)** — `schemas.py` + `provenance_gate.py` + SKILL.md + INSTRUKTIONEN.md §27.8 NEU. 19/19 Schema-Tests + 10/10 Gate-Tests. Damit alle 5 AVGO-30.04.-Methodology-Watches #30-34 strukturell adressiert. → git log + PIPELINE #34.
- **09.05. (Sa) ✅ PIPELINE #54 Vault-Health-Maintenance** — Index-Drift fix (Quality-Trap + MA-Stub-Refs), RETROSPECTIVE-GATE.md NEU (42 LOC Stub mit 4-Dimensionen-Framework), §29-Backlink-Refresh in 15 Concept-Pages. 0 Orphans nach Auto-Lint. → git log + PIPELINE #54.
- **09.05. (Sa) ✅ Wave-3 PIPELINE #16 INSTRUKTIONEN.md Slim-Refactor (Pointer-Extraction)** — RETROSPECTIVE-GATE.md + morning-briefing-spec.md NEU; INSTRUKTIONEN 1149→960 LOC (-16,4%). Gemini-Cross-Sync 97% GO. → commit `2031ca6` + PIPELINE #16.
- **09.05. (Sa) ✅ Wave-2 Skill-Lazy-Load-Refactor + #23 + #30** — CLAUDE.md/TOKEN-RULES/SKILL.md description+trigger_words rewrite (32→5); INSTRUKTIONEN §27.7 NEU Carryover-Discipline-Asymmetrie (#23); SKILL §410 Tie-Break + Confidence-Caveat + AVGO-Präzedenz (#30). Memory-Doc neu `feedback_skill_lazy_load_dual_trigger_source.md`. → git log + PIPELINE #23/#30.
- **09.05. (Sa) ✅ Welle-1 AVGO-Cluster-A Closure PIPELINE #32 + #33** — Backfill-Eligibility-Klausel (SKILL Schritt 0) + ATH-Distance-Boundaries (SKILL Technicals 5-Bucket-Tabelle mit Window-Scope `period='max'` + Drawdown-Trennungs-Disziplin). Codex-R1+R2 96% Final. → git log + PIPELINE #32/#33.
- **09.05. (Sa) ✅ PIPELINE Cluster-A #31 Methodology-Drift Hard-Ausschluss** — sources.md §7 NEU (StockAnalysis hard-excluded für ROIC/Forward-P/E/Score-Inputs, quarterly-CashFlow-only Cross-Check); INSTRUKTIONEN §27.4 Anker. Plus 2 neue deferred Items #52 (Quick-Screener-Refresh) + #53 (Trigger-Landschafts-Audit). Memory-Doc neu `feedback_skill_refresh_without_usecase_overengineering.md`. → git log + PIPELINE #31/#52/#53.
- **07.05. (Do) ✅ Tavily-Connector-Recreation (PIPELINE #45 RESOLVED)** — Briefing-News-Signal wieder live nach zweistufigem Fix: `allowed_tools`-Patch + Connector-Recreation in Web-UI (neue UUID `21639169-...`). Lesson zwei-stufig dokumentiert in Memory `feedback_tavily_connector_uuid_rotation.md` + neue Memory `feedback_remote_trigger_shallow_partial_update.md`. → git log + SYSTEM §Briefing-Status.
- **05.05. (Di) ✅ Welle-3a Doctor-Periodic-Cadence ACTIVE — Cadence-Anker Mo morgens** (Off-Schedule-Kickoff Di). Snapshot-1 im Doctor-History-Archiv: 6P/8W/0F, 1226ms. Erfolgskriterium ≥4 Wochen ohne FAIL-Drift (heute 11.05. = Woche 2/4 mit 7P/7W/0F). → PIPELINE #20.
- **04.05. (Mo) ✅ BRK.B Q1 FY26 Tag-+1 Vollanalyse — Codex-R1-REJECT-Korrektur Score 75→71** (Δ-4), D3/Sparrate 38€/FLAG ✅ Clean Insurance-Exception unverändert, keine Kaskade. Sub-Karte F=35/M=19/T=1/I=10/S=6. 15/15 Codex-HIGH-Antis pre-empted. 6 Q2-Methodology-Watches PIPELINE #36-#41. ScoreRecord `2026-05-04_BRK.B_vollanalyse` Schritt 7 DONE Tag-+1-Abend. → CORE-MEMORY §12.4 + git log + PIPELINE #36-#41.

**Forward-Triggers (~14 Tage):**
- **14.05.** MSFT Insider-Block-Re-Score post-14d-Skip-Window via `insider_intel.py` (PIPELINE #26)
- **~14.05.** BRK Form-13F Q1-26 Filing → Apple-Trim-Magnitude (PIPELINE #37)

## Navigation (on-demand)
| Wenn du brauchst… | Lies… |
|---|---|
| Scores / FLAGs / Watches / Sparraten / 30-Tage-Trigger | **PORTFOLIO.md** (default-load) |
| Offene Pläne, Gates, Primary-Track | PIPELINE.md |
| System-Versionen, Briefing-Status, Infra | SYSTEM.md |
| Lektionen / Per-Ticker-Chronik / Lifecycle | CORE-MEMORY.md (§5 / §12 / §13) |
| Workflows / Sparraten-Formel / Sync-Pflicht | INSTRUKTIONEN.md |
| Strategie / Allokation | KONTEXT.md (on-demand) |
| Score-Detail pro Ticker | Faktortabelle.md |

**Sync-Pflicht (§18 v2.4):** bei Score/FLAG/Sparraten-Change → PORTFOLIO.md + CORE-MEMORY + Faktortabelle + log.md + score_history.jsonl + `01_Skills/dynastie-depot/config.yaml` + `03_Tools/Rebalancing_Tool_v3.4.xlsx` + `03_Tools/Satelliten_Monitor_v2.0.xlsx` (+ flag_events.jsonl). Nach xlsx-Write **verpflichtender §18.7 Smoke-Test** (`03_Tools/xlsx-smoke-test.md`, fail-close vor `git add`). Details in INSTRUKTIONEN §18 (inkl. Multi-Event-Union-Regel + xlsx-Tools-Pflicht seit v2.3 28.04. spätabends + Smoke-Test seit v2.4 11.05.2026).

<!-- system-audit:last-audit:start -->
---

## 🔍 Last Audit

**Timestamp (UTC):** 2026-05-14T02:10:43Z
**Result:** 14/15 PASS (1 WARN)
**Run:** `python 03_Tools/system_audit.py --core`
**Full-Report:** stdout (kein Archiv-File)

<!-- system-audit:last-audit:end -->

*🦅 STATE.md Hub v2.3 | Dynasty-Depot | **Stand:** 14.05.2026.*
