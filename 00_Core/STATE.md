# 🎯 STATE.md — Dynasty-Depot Hub

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — Offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Infrastruktur / Briefing / Backtest-Ready
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13)
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Banner-Chronik

## ⚠️ Critical-Alerts (≤ 10 Tage — handgepflegt)

> **Konvention (11.05.2026 Slim-Refactor):** 1-3-Zeilen-Pointer. Detail → `git log` + `CORE-MEMORY.md §13` + PIPELINE-Item-Body.

- **22.05. (Fr) ✅ FinnHub-Integration v0.1 SPEC→PLAN→BUILD KOMPLETT DONE** (PIPELINE #74, System-Event, scoring-neutral). Shadow-Run-Start 23.05. ~Mittag, Hard-Deadline Reklassifizierungs-Gate **06.07.** (PIPELINE #75 AKTIV; #76 v0.2-Methoden-Discovery DEFERRED). Auch 21.05.: session-closure-Skill v0.2.0 + paragraph-18-sync SPEC v0.3 Build-ready. Detail → SYSTEM.md §Passive Read-Only Data Layer + PIPELINE #74/#75/#76 + git log.
- **18.05. (Mo) 🔴 AMZN Neuaufnahme 12. Satellit — SCORING-RELEVANT** (User-Direktive). Score **42/🔴 D1**, **🔴 CapEx/OCF-FLAG** TTM netto 99,2%, Sparrate **0€ regelkonform**, Slot 11→12 nenner-neutral. PIPELINE #70 xlsx-Struktur-Erweiterung ✅ DONE; #71 GOOGL-Cross-Ref-Erratum aktiv. Detail → CORE-MEMORY §12.12 + PIPELINE #70/#71 + git log.
- **17.05. (So) ✅ Pickup #C pre-commit-Substrate KOMPLETT DONE + akzeptiert** (Pipeline-Event, scoring-neutral). #69 NEU = deferred Operational-Debt-Remediation. Detail → git log + Vault log.md + PIPELINE #69.
- **17.05. (So) ✅ BRK Form-13F #37 RESOLVED** (scoring-neutral, KEIN Score-Move). Apple Q4-25=Q1-26 = 0 Trim. Detail → CORE-MEMORY §12.4 + git log.
- **16.05. (Sa) ✅ Pickup-#C-Vorlauf + System-Cluster DONE** (System-Event). Spec v0.1 + Codex-Sparring-Gate PASS + FlagEvent-Schema + Karpathy-Plugin Upstream-Watch + ecc-Reject. Detail → git log + Vault log.md.
- **16.05. (Sa) ✅ Pickup #B CLAUDE.md-Review + Phase-0b HYBRID-Final + #D Obsidian-Skills DONE** (System-Event). claude-mem additiv read-only / autoMemory kanonisch unberührt; `system_audit --core` 14/15 grün. Detail → CORE-MEMORY §13 + SYSTEM.md §Plugin-Layer + git log.
- **13.–14.05. ✅ Watchlist-Ersatzbank-Refresh v3.2 + #26 MSFT-Insider-Re-Score (Δ=0) + #61 Retro + Plugin-Refactor DONE** (scoring-neutral). Detail → CORE-MEMORY §13 + §12.6 + git log.

**Forward-Triggers (~14 Tage):**
- **27.05.** VEEV Q1 FY27 · **28.05.** COST Q3 FY26 (Klasse-B Earnings)
- **~Ende Juli** AMZN Q2 FY26 — CapEx/OCF-FLAG-Re-Eval + Vollanalyse
- **28.05.** MSFT Insider-Skip-Window nächstes Expiry

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

*🦅 STATE.md Hub v2.5 | Dynasty-Depot | **Stand:** 2026-05-23 (00_Core Slim-Refactor — Critical-Alerts-Block auf eigene Konvention 1-3-Zeilen-Pointer zurückgeführt; kein Info-Verlust, Detail-Quellen via git log + CORE-MEMORY §13 + PIPELINE-Item-Bodies erreichbar)*
