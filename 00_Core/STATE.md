# 🎯 STATE.md — Dynasty-Depot Hub

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — Offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Infrastruktur / Briefing / Backtest-Ready
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13)
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Banner-Chronik

## ⚠️ Critical-Alerts (≤ 10 Tage — handgepflegt)

> **Konvention (11.05.2026 Slim-Refactor):** Critical-Alerts sind 1-3-Zeilen-Pointer. Sub-Detail-Decomposition (A/B/C/D… + §18-Sync-Set + bewusst-NICHT-angefasst) gehört NICHT hierher — kanonische Archivquelle ist `git log` (Commit-Body) + `CORE-MEMORY.md §13` (Lifecycle) + PIPELINE-Item-Body bei aktiven Items.

- **22.05. (Fr) ✅ FinnHub-Integration v0.1 SPEC→PLAN→BUILD KOMPLETT DONE (PIPELINE #74, System-Event, scoring-neutral).** Real-Time-Layer für defeatbeta-Stale-Mitigation; **Option C Read-Only Surface**, **Zero-Skill-Refactor-Footprint invariant** (A1 Static-Footprint-Check verifiziert). 3-Phasen-Trio in einer Session: Spec v0.3 (Codex-3-Runden) → Plan v0.1.0 (Codex-CP0) → Build (15 Tasks, ~6h, 6 Build-Commits `1a71f0f`→`7cafaa4` + Task-15-Sync). **A1-A12 alle PASS** (A6 24/24 schema-conform; A12 bit-perfect Δ=0.00). **Step 4a Decision:** 3/8-Minimal-Bridge (defeatbeta-Methoden-Probe 2/5 <3-Threshold → peTTM/roe/roic Live + 5 systematisch N/A). **Shadow-Run startet 23.05. ~Mittag** (manueller Day-1-Trigger), Hard-Deadline Reklassifizierungs-Gate **2026-07-06 (+45d)** als **PIPELINE #75 AKTIV**; v0.2-Methoden-Discovery als **#76 DEFERRED**. CP-2-Followups P-3..I-2 als Improvement-Backlog während Shadow-Run an #75 gekoppelt. **PIPELINE #74-Body 22.05. abends massiv geslimmt** (~3000W → ~190W Pointer; Detail-Trail nach SYSTEM.md §Passive Read-Only Data Layer + Vault log.md 3 Einträge + git log + Spec/Plan-Files verlagert; Footer v2.54→v2.55). **Auch:** gestern 21.05. session-closure-Skill v0.2.0 deployed (`42eca7c`, Strict-Trigger `!SessionClose`, INSTRUKTIONEN §25.5 SSoT) + paragraph-18-sync SPEC v0.3 Build-ready (PIPELINE #73a, Codex-3-Runden 30 Befunde adoptiert). Live-Score-Impact NULL. DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert. Detail → CORE-MEMORY §13 + git log + SYSTEM.md §Passive Read-Only Data Layer + Vault log.md + PIPELINE #74/#75/#76.
- **18.05. (Mo) 🔴 AMZN Neuaufnahme 12. Satellit — SCORING-RELEVANT** (User-Direktive „Mein Portfolio, meine Regeln"). Score **42/🔴 D1**, **🔴 CapEx/OCF-FLAG** (TTM netto 99,2% / gross 101,7% ≫60%, schärfer als GOOGL; FCF TTM $1,2B -95%). Sparrate **0€ regelkonform** (User-Entscheidung: kein Owner-Override, FLAG heilig). Slot-Erweiterung **11→12 nenner-neutral** (FLAG=0,0 → Nenner 7,5 unverändert, alle 11 bestehenden Raten 38€/19€/0€ unverändert, Σ285€). §410 N/A (GW 2,6%). §18-Multi-Event-Sync **Commit 1 `a6ed83b` DONE**. **PIPELINE #70 ✅ DONE 18.05. (frische Session):** xlsx-Struktur-Erweiterung Rebalancing+Satelliten-Monitor (`9cde988`) — AMZN exakter Ziel-Anteil wie alle (H equal-split 30%/12=0,025, ΣH=1,00), Bereichs-Formeln 5:20→5:21 + Footer-Shifts + CF/Merged neu, nenner-neutral formel-verifiziert (P FLAG/DEFCON-getrieben, Nenner 7,5/Σ285€ unverändert), §18.7+pre-commit-Smoke PASS (2 Bugs gefixt). Vault-Entity-Page `def0550` (AMZN.md + Backlinks + index/log). Codex-Diff-Re-Review 0H/1M/2L (MED→#71 score_history GOOGL-Cross-Ref-Erratum append-only-immutable; 2 LOW gefixt). Gemini Cross-Sync = Self-Verify-Fallback (Bridge defekt Node-22-Req, SESSION-HANDOVER-dokumentiert). US-Ziel ~49,51%→~50,2% (KONTEXT/config nachgezogen). Excel-Desktop-Sichttest §18.7-E/F bei nächstem Zugriff. Detail → CORE-MEMORY §12.12 + git log + PIPELINE #70/#71.
- **17.05. (So) ✅ Pickup #C pre-commit-Substrate KOMPLETT DONE + akzeptiert** (Pipeline-Event, scoring-neutral). Execution Unit 1+2+3 (Spec v0.1 + non-mutierender Substrate-Build + CRLF-One-Shot) + Akzeptanz-#1-Verifikation: echter Unit-2-xlsx-Validator-Bug gefixt (A1-Check fälschlich vor Profil-Verzweigung → `minimal`-Zweig, Smoke 8/8) + crlf-guard-Scope-Verengung (135→46 CRLF, Spec-§4.3-vs-§5.1-Widerspruch aufgelöst) + `.gitattributes *.yaml`. §5.6-Gate voll (CR „No findings" → Codex-Single-Pass PASS). #68 per Numbering-Convention entfernt; **#69 NEU** = deferred Operational-Debt-Remediation (46 CRLF + 107 Ruff + 55 ruff-format). Commits `3401512`/`c7a1355`/`c86aea3`. DEFCON v3.7 + 11 Scores + Sparraten 285€ unverändert. Detail → git log + Vault log.md + PIPELINE #69 + Spec.
- **17.05. (So) ✅ BRK Form-13F #37 RESOLVED** (Pipeline-Event, scoring-neutral, KEIN Score-Move). Q1-26 13F-HR gefiltert (15.05., BRK-Q1-Pattern bestätigt); Apple **227.917.808 Shares Q4-25 == Q1-26 = 0 Trim** (Value −$4,12B = reiner Kurs-Markdown −6,65%). Pre-Brief-§2-Apple-Trim-Hypothese definitiv = $0; Top-5 65→61% Bank-getrieben. #37 per Numbering-Convention entfernt. BRK.B 71/D3/FLAG ✅/38€ unverändert (Q2-Vollanalyse-gebunden ~02./03.08.; #36/#38-#41 aktiv). Detail → CORE-MEMORY §12.4 + git log.
- **16.05. (Sa) ✅ Pickup-#C-Vorlauf + System-Cluster DONE** (System-Event, scoring-neutral): Pickup #C Spec v0.1 + Codex-Sparring-Gate PASS + FlagEvent-Schema-Vorbedingung ERFÜLLT-verifiziert (Doc-Drift-Fix) + Karpathy-Plugin Upstream-Watch-Anker §0 + ecc-Substrate-Reject/Full-Removal. Detail → git log + Vault log.md + Spec.
- **16.05. (Sa) ✅ Pickup #B CLAUDE.md-Review + Phase-0b HYBRID-Final + Pickup #D Obsidian-Skills-Bindung + Audit-FAIL-Resolve + Phase-0a-Gate PASS DONE** (System-Event, scoring-neutral). claude-mem additiv read-only / autoMemory kanonisch unberührt; `system_audit --core` 14/15 grün. Detail → git log + Vault log.md + CORE-MEMORY §13 + SYSTEM.md §Plugin-Layer.
- **13.–14.05. ✅ Watchlist-Ersatzbank-Refresh v3.2 + PIPELINE #26 MSFT-Insider-Re-Score (Δ=0) + #61 Retro + Plugin-Substrate-Refactor DONE** (scoring-neutral; MSFT 50/D2/FLAG/0€ + 11 Scores + Sparraten unverändert). Detail → CORE-MEMORY §13 + §12.6 + git log.
- **Davor (≤ 11.05., kondensiert per 11.05.-Slim-Präzedenz):** Codebase-Defect-Audit + G3/Sum-Consistency · Briefing v3.2.0 Prod-Cutover · PORTFOLIO/STATE-Slim-Refactor · Audit-Cleanup-Packs · PIPELINE #55 Phase-D-1 · #22/#34/#54 · Wave-1/2/3 (Cluster-A/#16/#23/#30/#31) · Tavily-Connector-Recreation · Doctor-Periodic-Cadence · BRK.B Q1 Tag-+1 Score 75→71. **Kanonische Archivquelle: `git log` + CORE-MEMORY §13 + PIPELINE-Item-Body** (Konvention Z.12).

**Forward-Triggers (~14 Tage):**
- **27.05.** VEEV Q1 FY27 · **28.05.** COST Q3 FY26 (Klasse-B Earnings, yfinance-Pull 30.04.)
- **~Ende Juli** AMZN Q2 FY26 — CapEx/OCF-FLAG-Re-Eval (Resolve-Gate <60%) + Vollanalyse (Score 42/🔴 D1, FLAG seit 15.05.)
- **28.05.** MSFT Insider-Skip-Window nächstes Expiry (post-14.05.-Re-Scan +14d) — nur bei Score-/FLAG-Trigger relevant
- *BRK Form-13F #37 ~15.05. ✅ RESOLVED 17.05. (Apple 0 Trim, siehe Critical-Alert oben + CORE-MEMORY §12.4).*

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

**Timestamp (UTC):** 2026-05-16T14:22:46Z
**Result:** 14/15 PASS (1 WARN)
**Run:** `python 03_Tools/system_audit.py --core`
**Full-Report:** stdout (kein Archiv-File)

<!-- system-audit:last-audit:end -->

*🦅 STATE.md Hub v2.4 | Dynasty-Depot | **Stand:** 2026-05-22 (✅ FinnHub-Integration v0.1 SPEC→PLAN→BUILD KOMPLETT DONE — System-Event scoring-neutral; PIPELINE #74 BUILD-PHASE-DONE + neu #75 Shadow-Run-Tracker AKTIV (Hard-Deadline 06.07.) + neu #76 v0.2-Methoden-Discovery DEFERRED; PIPELINE #74-Body 22.05. abends massiv geslimmt ~3000W → ~190W Pointer, Footer v2.54→v2.55; Detail → SYSTEM.md §Passive Read-Only Data Layer + Vault log.md + git log. Auch 21.05.: session-closure-Skill v0.2.0 + paragraph-18-sync SPEC v0.3 Build-ready. Live-Score-Impact NULL. Davor 18.05.: 🔴 AMZN Neuaufnahme 12. Satellit — Score 42/D1, CapEx/OCF-FLAG, Sparrate 0€ regelkonform, Slot 11→12 nenner-neutral, User-Direktive; §18-Sync DONE. **PIPELINE #70 ✅ DONE: xlsx-Struktur-Erweiterung `9cde988` + Vault-Page `def0550` + Codex-Re-Review 0H/1M/2L + Gemini-Self-Verify (Bridge defekt); #71 NEU GOOGL-Cross-Ref-Erratum append-only-immutable; US-Ziel→~50,2% nachgezogen.** Davor 17.05.: Pickup #C pre-commit-Substrate **KOMPLETT DONE + akzeptiert** — Akzeptanz-#1-Verifikation: echter Unit-2-xlsx-Validator-Bug gefixt + crlf-guard-Scope-Verengung + Spec-§4.3-vs-§5.1 aufgelöst + `.gitattributes *.yaml`; §5.6-Gate voll CR→Codex-PASS; #68 entfernt per Numbering-Convention, #69 NEU = deferred Operational-Debt-Remediation; scoring-neutral. Davor: #C Execution Unit 1+2+3 [Spec v0.1 + Substrate-Build + CRLF-One-Shot] · Karpathy-Plugin Upstream-Watch §0 + ecc-Reject · Pickup #B CLAUDE.md-Review · Phase-0b Memory HYBRID-Final · Pickup #D Obsidian-Skills-Bindung — alle DONE scoring-neutral. Detail-Historie → git log + Vault log.md + CORE-MEMORY §13.)*
