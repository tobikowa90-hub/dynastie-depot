# Plan-Meta-Review — RUFLO-INTEGRATION-PLAN.md

**Status:** Vorarbeit-Draft (working-tree, **uncommitted**)
**Datum:** 2026-04-28
**Plan-Version:** Draft v1.0 / Commit `c9a3ed5`
**Phase 1.1 Status:** DONE (Override-Block Codex 2-Round PASS WITH NITS)
**Reviewer-Pair:** Codex (`codex:codex-rescue`) + Ruflo-Planner (`Agent` subagent_type=`planner`) — beide single-pass, in selber Session, ohne Cross-Kontamination
**Empirische Spikes:** V1/V2/V3/V4/V5 read-only (siehe Abschnitt „Empirische Vorarbeit-Findings")

> **Apply-Sperre:** Bis nach V Q2 (28.04. AMC) + MSFT Q3 (29.04. AMC) Earnings-Window-Schluss. Diese Datei = Pre-Read-Checkliste für Phase-1.2-Kickoff, kein Change-Set.

---

## 1. Convergence (beide Reviewer einig)

- **Phase 1.2 ist NICHT risikolos** — Plan-Label „NIEDRIG" ist falsch. Memory-Bridge auf OneDrive-Vault + AgentDB-State-Backend hat reales Operational-Risiko.
- **Phase 2 ist überladen** für „Eval-Phase mit Pilot-Use-Case" — mehr als 2 Hebel parallel macht Attribution unscharf.
- **§18-Sync-Mechanik nicht pro Phase durchdekliniert** — Plan nennt Ziel-Files generisch („gemäß §18"), aber Union-Regel + Event-Typ-Mix pro Phase fehlen.
- **Kill-Criteria pro Phase fehlen** — Rollback-Pfade beschrieben, aber keine harten Stop-Bedingungen, ab denen man eine Phase als Fehlversuch deklariert.
- **ROI-Abfall ab Phase 3:** Beide bestätigen, dass Phase 1+2 der echte Hebel ist; 3+4 ist Architecture-Astronaut-Risiko.

## 2. Codex-only Findings (Syntax/Doku-Bias)

- **`SYSTEM.md §Ruflo-Status` braucht Minimal-Schema** vor 1.2-Start — sonst Drift zwischen settings.json, AgentDB-Status, Hooks und real aktivierten Features.
- **Stream-Chain (2.5) Doppel-SSoT-Risiko** mit `dynastie-depot` SKILL.md — Skill ist gerade gehärtet (Provenance-Gate, Pre-Flight-Klausel), Stream-Chain führt zweite Orchestrierungs-SSoT ein.
- **Rollback ≠ Exit-without-adoption:** Plan beschreibt nur technischen Zurückrollen, nicht den bewussten „diese Phase als Fehlversuch abschließen, kein Re-Try"-Pfad.
- **STATE.md im Plan als Audit-Begleiter mehrfach genannt**, aber in §18 v2.1 nicht eigener Standard-Event-Typ — muss als Zusatz-Touch begründet werden, nicht implizit mitschwingen.

## 3. Ruflo-Planner-only Findings (Operational/Architektur-Bias)

- **Memory-Path-Pollution-Risk** — `import-all` würde Cross-Project mischen; siehe empirische Korrektur in §6.
- **AgentDB-OneDrive-Backend-Risk** — wenn SQLite-WASM-DB im OneDrive-cwd landet → Sync-Lock-Konflikte (Memory `feedback_onedrive_edit_collision.md`).
- **Phase 2.3 falsch positioniert:** §28.2 Algebra-Gate ist deterministisch (`delta_check.py`), kein Halluzinations-Risiko → Codex-Dual-Mode hier nutzlos. Sinnvoller wäre **§28.1 (Paper-Befund-Auswahl + ExplainableRecall-Trace)**, nicht §28.2.
- **Phase 1.9 Trajectory-Recording zu früh:** `dynastie-depot`-Skill wird gerade umgebaut (Item #17 Beispiele.md 4-Achsen-Refactor läuft post-MSFT). Trajectory-Daten der Pre-Refactor-Ära sind als RL-Training anti-produktiv.
- **Pipeline-Vorrang:** Item #20 (Ruflo) gehört **nach** Item #17 (Beispiele.md), NICHT direkt nach Earnings-Schluss. Konkurrenz: Items #2/#6/#16/#17/#18 + Briefing-v3.0.6-Deploy + V/MSFT-Live-Runs.
- **Codex-Sparring-Heuristik-Selbstwiderspruch:** Phase 2.3 Auto-Codex-Spawn pro Algebra-Gate verletzt Memory `feedback_codex_sparring_heuristic.md` (Single-Pass-Default + 2+ HIGH-Findings).
- **Pending-Insights-Pflege-Regel fehlt** — Buildup-Risiko analog APPLIED-LEARNING-20/20-Cap.
- **ExplainableRecall-Plan-Claim für §28-Score-Begründung überzogen** — passt nur für §28.1 (Paper/Evidence-Trace) + §29.7 (M&P-Discount-Trigger), nicht für §28.2 Algebra.

## 4. Conflict-Resolution-Regel (Ruflo-Planner self-supplied)

- Bei **Syntax-HIGH von Codex**, das Ruflo-Planner nicht sieht → **Codex** hat recht (literal-syntaktischer Bias zahlt sich da aus).
- Bei **Operational-Risiko von Ruflo-Planner**, das Codex nicht sieht → **empirisch validieren** vor Plan-Edit (Spike-statt-Argument).
- Bei **Differential-Frame-Konflikt** (z.B. ExplainableRecall §28 vs §28.1) → Plan-Patch klären, dann re-review.

## 5. Critical-Path-Korrektur Phase 1

**Plan-Default:** 1.1 → 1.2 → 1.3 → … → 1.9 sequenziell.

**Empfehlung:**
1. **1.1 Override-Block** ✅ DONE
2. **1.5 Tool-Mode `dynastie`** — größter Token-Save, reversibel via env-unset, kein State-Touch
3. **1.2 Memory-Bridge `import-all`** — der eigentliche Hebel, ABER: Pre-Conditions vorher (siehe §8)
4. **1.7 Hook-Subset (6 von 27)** — verhindert dass die anderen 21 Hooks später unbeabsichtigt aktivieren
5. **1.8 Doctor-Baseline** ✅ EARLY-DRAWN (siehe §6, baseline schon im Working-Tree-Doku) — sonst Drift unmessbar
6. **1.3/1.4/1.6** — Nice-to-Have, parallel oder dehnbar
7. **1.9 Trajectory-Recording → Phase 1+ verschieben** — erst wenn `dynastie-depot`-Skill nach Item #17 stabil ist

## 6. Empirische Vorarbeit-Findings (V1-V5)

### V1: Memory-Pfad-Inventar (read-only `glob`)

| Project-Pfad | Memory-Files | Domain |
|--------------|--------------|--------|
| `C--Users-tobia` | 3 | Generic Home |
| `C--Users-tobia-Code` | 11 | Code-Tooling (CRLF, WSL, CodeRabbit, OneDrive-Edit-Collision, Codex-Sparring) |
| `C--Users-tobia-OneDrive-Desktop-Claude-Stuff` | **20** | **Dynastie-Depot (eigener Namespace!)** |
| `C--Users-tobia-wiki` | 3 | Wiki/Vault |

**KORREKTUR Ruflo-Planner-Hypothese:** Dynastie ist NICHT empty — hat größten Namespace mit 20 Files. Cross-Project-Pollution-Risk besteht trotzdem (Code-Domain-Pattern landen im Dynastie-Recall), aber die Volumen-Verteilung ist umgekehrt zur Annahme.

**Dynastie-Memory-Inhalt** (eigener Project-Path): coderabbit-cli-via-wsl, context7-availability, data-source-coverage, 7 feedback-Files (correctness, drift, friction, info-loss, multi-source-drift, raw-backlink, review-stack, spec-section-drift), morning-briefing-config, portfolio-state-snapshot, 3 project_*-Files (graphify, system_audit, systemwide_reorg), py314_threadpool_daemon, remote-trigger-api, system-architecture, MEMORY.md.

**Implikation für Phase 1.2:** `import-all` ist falsch. Richtig: **nur Dynastie-Path importieren** + optional separater Namespace für Code-Path mit Filter bei Recall.

### V2: Ruflo-CLI-Surface

- Version: `ruflo v3.6.9`
- `memory init` hat **kein** `--dry-run`-Flag laut `--help`
- `memory configure` existiert als Subcommand → Backend-Path-Config dort
- Subcommands: init, store, retrieve, search, list, delete, stats, configure, cleanup, compress, export, **import** (separat von init!)

**Implikation für Phase 1.2:** Plan sagt `memory init --force` + `auto-memory-hook.mjs import-all`. Zwischen den beiden Schritten muss `memory configure` (Backend-Path setzen) sitzen, sonst landet AgentDB im Default-Pfad (vermutlich `cwd/.claude/`, also OneDrive). Plan-Step fehlt.

### V3: Doctor Pre-Phase-1.2 Baseline (read-only, kein State-Change)

```
✓ Version Freshness: v3.6.9 (up to date)
✓ Node.js: v25.9.0
✓ npm: v11.12.1
✓ Claude Code CLI: v2.1.121
✓ Git: v2.54.0.windows.1
✓ Git Repository: In a git repository
⚠ Config File: No config file (using defaults)
⚠ Daemon Status: Not running
⚠ Memory Database: Not initialized      ← bestätigt: Phase 1.2 noch nicht gestartet
⚠ API Keys: No API keys found
⚠ MCP Servers: No MCP config found       ← Ruflo-MCP separat von claude-flow-MCP
⚠ TypeScript: Not installed locally
⚠ agentic-flow: Not installed (optional)

Summary: 7 passed, 7 warnings (alle als pre-init erwartbar)
```

**Wichtig:** Memory DB **nicht initialisiert** — sauberer Baseline-State. Erste Aktivierung in Phase 1.2 ist genuine first-run, kein State-Carry-over.

### V4: `.claude/settings.json` Pre-Phase-1.2-Stand

```json
{
  "hooks": {
    "SessionStart": [{ "command": "briefing-sync-check.ps1", "timeout": 15 }],
    "SessionEnd":   [{ "command": "briefing-sync-check.ps1", "timeout": 15 }]
  },
  "autoMemoryEnabled": true,
  "autoDreamEnabled": true
}
```

**Wichtig:**
- `autoMemoryEnabled: true` ist **Claude-Code-native**, nicht Ruflo. Pre-existing seit Setup. Bedeutet: Auto-Memory in `~/.claude/projects/.../memory/*.md` läuft bereits, unabhängig von Ruflo-Bridge.
- 2 Hooks aktiv (SessionStart/End → `briefing-sync-check.ps1`). Phase-1.7-Plan (6-Hook-Subset) muss diese 2 als „pre-existing, nicht-Ruflo" markieren — sonst Konflikt-Diagnose.
- `settings.local.json` existiert separat (13.9KB, nicht inspiziert) — vermutlich permission-allowlist. **Pre-Phase-1.7-TODO:** Inspektion + Konflikt-Check mit geplantem 6-Hook-Subset.

### V5: Tool-Mode `dynastie` Trockentest

Env `CLAUDE_FLOW_TOOL_GROUPS=memory,monitor` setzen ist trivial reversibel via unset. CLI-Listing dynamischer Tools funktioniert nur über laufenden MCP-Server (`mcp tools`-Subcommand braucht active server). **Implikation:** Tool-Mode-Filterung ist erst nach Phase-1.2-MCP-Setup empirisch verifizierbar; Trockentest = Plan-Read, nicht Validation.

## 7. Plan-Patch-Liste (für nach Earnings, vor Phase-1.2-Kickoff)

| # | Patch | Section | Confidence |
|---|-------|---------|-----------|
| P1 | Memory-Bridge **NICHT** `import-all`, sondern path-scoped (nur Dynastie-Project-Path) | Phase 1.2 | HIGH |
| P2 | `memory configure` als eigenen Sub-Step zwischen `init --force` und `import` einfügen, AgentDB-Backend-Path explizit auf nicht-OneDrive-Verzeichnis (`%LOCALAPPDATA%/ruflo-dynastie` o.ä.) | Phase 1.2 | HIGH |
| P3 | Phase 1.2 Pre-Flight-Klausel: kein Edit auf Memory-Files in IDE während `import-all` (Memory `feedback_onedrive_edit_collision.md`) | Phase 1.2 | HIGH |
| P4 | Phase 2.3 von §28.2 auf §28.1 umpositionieren, Use-Case = ExplainableRecall-Trace für Paper-Befund-Auswahl + §29.7-M&P-Trigger | Phase 2.3 | HIGH |
| P5 | Phase 1.9 Trajectory-Recording aus Phase 1 streichen → „Phase 1+" oder Phase 2-Slot nach Item #17-Refactor | Phase 1.9 | HIGH |
| P6 | `SYSTEM.md §Ruflo-Status` Minimal-Schema definieren VOR Phase 1.2: Pflicht-Felder = aktivierte_tools, hooks_aktiv, memory_bridge_path, memory_bridge_status, last_doctor_baseline, agentdb_pfad, pending_insights_count | Phase 1.2 Pre-Step | MEDIUM |
| P7 | Pending-Insights-Pflege-Regel ergänzen: monatlicher Review wie APPLIED-LEARNING, sonst Buildup-Risk | Phase 1.2 + ongoing | MEDIUM |
| P8 | Kill-Criteria pro Phase explizit (Phase 1.2: OneDrive-Drift / Bridge-Korruption / >5min Session-Start-Latenz; Phase 2: Codex-Match-Rate <80%; etc.) | Übergreifend | MEDIUM |
| P9 | Phase 2 in 2a (Memory-Controllers + Workers) und 2b (Skill-Refactor Stream-Chain) splitten — 2b ist kein Eval, sondern Architektur-Eingriff | Phase 2 | MEDIUM |
| P10 | Codex-Nits aus Phase 1.1 ergänzen (Hintertür-Klausel #5 streichen + Memory-Bridge-Tools `memory_import_claude` / `memory_search_unified` als „erst-ab-1.2-aktiviert" gating'd) | Phase 1.2 Eröffnungs-Commit | MEDIUM (committed deferred) |

## 8. Phase 1.2 Pre-Conditions (vor Aktivierung erfüllt sein)

1. ✅ Phase 1.1 Override-Block committed
2. ✅ Doctor Pre-Phase-1.2-Baseline gezogen (siehe §6 V3)
3. ✅ Memory-Pfad-Inventar erstellt (siehe §6 V1)
4. ☐ Plan-Patches P1–P10 in `00_Core/RUFLO-INTEGRATION-PLAN.md` eingearbeitet (bumpe Plan auf v1.1)
5. ☐ V/MSFT-Earnings-Live-Runs durch (28./29.04. AMC) + Briefing-v3.0.6-Prod-Deploy nach Item #2
6. ☐ Item #18 AVGO ScoreRecord-Backfill committed (compliance debt closed)
7. ☐ Item #17 Beispiele.md 4-Achsen-Refactor committed (Skill-Pattern stabil für spätere Trajectory-Hooks)
8. ☐ `SYSTEM.md §Ruflo-Status` Minimal-Schema committed (P6) — vor `memory init`, nicht parallel
9. ☐ Codex-Nits aus 1.1 (Hintertür-Klausel + Memory-Bridge-Tools-Gating) im selben 1.2-Eröffnungs-Commit nachgefixt

## 9. Phase 1.2 Kickoff-Checkliste (sequenziell, single-session)

```
[ ] Pre-Flight: Keine OneDrive-Memory-Files im IDE offen
[ ] Pre-Flight: git status clean, kein dirty state
[ ] Pre-Flight: Doctor-Recheck (Baseline-Drift seit Pre-Earnings?)
[ ] Schritt 1: SYSTEM.md §Ruflo-Status anlegen (Stand: pre-init)
[ ] Schritt 2: npx ruflo memory configure --backend-path %LOCALAPPDATA%/ruflo-dynastie
[ ] Schritt 3: npx ruflo memory init --force (Backend-Pfad-Verifikation post-init)
[ ] Schritt 4: Path-scoped import — nur Dynastie-Project-Path, nicht --all
              (eventuell .claude/helpers/auto-memory-hook.mjs --project=onedrive-only)
[ ] Schritt 5: Verifikation — npx ruflo memory list, Anzahl == 20 (Dynastie-only)
[ ] Schritt 6: SYSTEM.md §Ruflo-Status auf „post-init: bridge active, 20 entries, lokaler Backend-Pfad"
[ ] Schritt 7: §18-Sync-Bundle-Commit (CLAUDE.md falls Codex-Nit-Fix + SYSTEM.md + log.md + PIPELINE.md)
[ ] Schritt 8: STOP — kein 1.3 in derselben Session, Review erforderlich
```

## 10. Verdict

**Plan-Verdict:** Substanziell richtig, operational unscharf an 4 Stellen (Memory-Path, AgentDB-Backend, §28.2-Mispositioning, Phase-1.9-Timing). Phase 1 ist zu optimistisch als „risikolos" gelabelt — Phase 1.2 ist real **mittleres Risiko**.

**Vorarbeit-Verdict:** V1–V5 erfolgreich, kein State-Touch, alle Pre-Conditions klarer als vor dieser Session. Plan ist **ready-for-Phase-1.2-Kickoff** SOBALD P1–P10-Patches eingearbeitet sind und Earnings-Window + Pipeline-Konkurrenz (Items #2/#17/#18) abgearbeitet sind.

**Risiko-Klasse Phase 1.2 (re-labeled):** ~~NIEDRIG~~ → **MITTEL** (Memory-Path-Disziplin + AgentDB-Backend-Pfad sind echte Operational-Risiken, nicht Plan-Theorie).

## 11. Nächste Schritte

1. Diese Doku **uncommitted** lassen — wartet auf Earnings-Window-Schluss + User-Review
2. Bei Phase-1.2-Kickoff (post-Item #17): Plan-Patches P1–P10 einarbeiten, Plan auf v1.1 bumpen, dann diese Doku referenzieren als Pre-Read und auf v1.0-Final stempeln
3. Alternativ: Diese Doku selbst committen als Vorarbeit-Artefakt (User-Entscheidung)

---

*Synthese-Doku — beide Reviewer single-pass, kein Sparring-Loop. Differential-Wert > Bestätigungs-Wert. Empirische Spikes V1–V5 als Korrektiv. Kein Apply, keine Ruflo-Aktivierung, keine §18-Sync-Welle.*
