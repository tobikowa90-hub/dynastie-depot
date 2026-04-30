# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-30 (Welle 0 WSL-Setup DONE + Persistierungs-Commit). Nächster primärer Resume-Trigger: **Phase 1.2-1.7 §18-Sync-Welle in NEUER Session post-Claude-Restart** (heute fortgesetzt nach MCP-Switch). Earnings-Pflichtslot **02.05. (Sa) BRK.B Q1 FY26 Tag-0** earnings-recap-Skill + FLAG-Quick-Check; Tag-+1 03./04.05.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `213b198` (chore(cleanup): CodeRabbit-Restbefund-Welle + Earnings-Reports-Folder-Move). Vorhergehende Commits derselben Session: `0253813` (feat(earnings) #24 Stufe 1 DONE), `aede0c2` (rules(§0) v1.11→v1.12), `6c729ed` (sync skill frontmatter), `12537e8` (handover post-#28).

**Working tree:** clean bis auf 2 unstaged anomalies (`CheckResult` 0-byte + `.claude/scheduled_tasks.lock`) — kein Blocker, beim nächsten Cleanup mit erledigen.

**Tools-Stand:**
- `03_Tools/earnings_calendar.py` v1.0 deployed (yfinance, kein API-Key, ~225 LOC). 11/11 PASS, BRK.B-Smoke ✅. CLI: `python 03_Tools/earnings_calendar.py --check --smoke-test`. Skip-if-past-Anker (post-02.05. manuell auf nächsten BRK.B-Q-Termin nachziehen).
- `03_Tools/system_audit/checks/cross_source_reverse.py` + `markdown_header.py` mit `# noqa: ARG001`-Stil-Konsistenz analog `status_matrix.py` + doubled-Pfad-Bug gefixt.

**Skill-Paket-Stand:** v3.7.6 unverändert (B6 Drawdown-Modulator). DEFCON-System v3.7 unverändert.

**Portfolio-State unverändert (Stand 30.04.):** AVGO 84/D4-FLAG/0€ | BRK.B 75/D3/38,00€ | VEEV 74/D3/38,00€ | SU 69/D3/38,00€ | COST 69/D3/38,00€ | RMS 68/D3/38,00€ | ASML 68/D3/38,00€ | TMO 67/D3/38,00€ | V 64/D2/19,00€ | APH 61/D2-FLAG/0€ | MSFT 50/D2-FLAG/0€. Nenner 7,5. Summe 285€.

**STATE.md Critical-Alerts:**
- **02.05. (Sa) BRK.B Q1 FY26** Tag-0 earnings-recap-Skill + FLAG-Quick-Check (Insurance-Exception, Score 75/D3, kein FLAG, Sparrate 38,00€); Tag-+1 Vollanalyse 03./04.05. — Drift detektiert via earnings_calendar.py 30.04.
- 30.04. PIPELINE #24 Stufe 1 DONE
- 30.04. PIPELINE #28 QT-DONE
- 14.05. MSFT Insider-Block-Re-Score post-14d-Skip-Window (#26)

---

### 🚀 Resume-Trigger NEUE SESSION (post-Claude-Restart heute) — Phase 1.2-1.7 §18-Sync-Welle [PRIORITÄT 1]

**Trigger-Phrase im neuen Chat:** „Ruflo Phase 1.2-1.7 Sync-Welle starten" oder „Phase 1.2 aktivieren". STATE+PORTFOLIO+dieses HANDOVER auto-load via Routing-Table (Resume-Fall).

**Kontext (was VOR Restart in dieser Session passiert ist):**
- **Welle 0 WSL-Foundation DONE 30.04. ~13:55** — WSL Ubuntu-24.04 nodejs 20.20.2 + npm 10.8.2 + ruflo v3.6.11 als root installiert (`/usr/bin/ruflo`). ONNX-Native-Binding lädt unter Linux sauber. Doctor-Baseline 5 PASS / 9 WARN / 0 FAIL.
- **Win32-`npx ruflo` gescheitert** — `ERR_DLOPEN_FAILED` auf `onnxruntime_binding.node`. VC++ Redist v14.50 IST installiert; Defender-Realtime-Block wahrscheinlichste Ursache (Win32-Reparatur deferred, WSL-Pfad ist die Lösung).
- **Codex-Plan-Review (codex:codex-rescue) PASS WITH NITS** — 0 HIGH / 5 MEDIUM / 2 LOW; 5 Δ-Adjustments im Plan eingebaut.
- **Backups in `05_Archiv/ruflo-phase1.2-backups/`** — CLAUDE.md + settings.json + settings.local.json + env (Rollback-Anker für gesamte Sync-Welle).
- **MCP-Switch erfolgte VOR Restart:** `claude mcp remove claude-flow` + `claude mcp add ruflo -s user -- wsl -d Ubuntu-24.04 bash -c "/usr/bin/ruflo mcp start"` (siehe PIPELINE #20 Status-Update).

**Erste Schritte in der neuen Session:**
1. **Verify Tools registriert:** `ToolSearch +ruflo` zeigt `mcp__ruflo__memory_*` etc. (kritisch: claude-flow MCP exportierte vor dem Switch keine Tools — neue Ruflo-MCP-Verbindung muss das ändern).
2. **`claude mcp list`** sollte ruflo connected zeigen (claude-flow entfernt).
3. **Falls Verify FAIL:** Rollback via `claude mcp remove ruflo` + `claude mcp add claude-flow -- cmd /c npx -y @claude-flow/cli@latest mcp start` und Phase 1.2 deferred bis Diagnose. Backups sind unangetastet.

**§18-Sync-Welle Phase 1.2-1.7 (atomar in einem Commit, ~40-50 min):**
1. **CLAUDE.md Codex-Nits-Nachfix:**
   - Hard-Conflict-#5 (Zeile 97): Hintertür-Klausel „Erlaubt nur bei explizitem User-Trigger... Positivliste: aktuell nur Phase-3 `!BatchScan`" streichen → ersetzen durch hartes „**Kein Swarm/Hive-Mind in Phase 1 oder 2** — keine Ausnahme, keine User-Trigger-Hintertür. Aktivierung erst durch expliziten Phase-3-Plan-Schritt mit Trigger-Definition (heute nicht aktiv)."
   - Compatible-Liste Zeile 113: ergänzen Memory-Bridge-Tools-Gating: „**Gating:** `memory_import_claude` ausschließlich path-scoped (`allProjects=false`); niemals `allProjects=true` / `import-all` (würde 4 Project-Namespaces / 37 Files Code-Domain-Pattern in Dynastie-Recall mischen, siehe Memory `feedback_ruflo_memory_bridge_onedrive_pitfall.md`). Backend-Path muss vor `memory init` auf Linux-FS umkonfiguriert sein, nicht `/mnt/c/...`-Pfade."
2. **Backend-Path konfigurieren in WSL:** `wsl -d Ubuntu-24.04 -u root -e bash -lc 'cd ~ && ruflo memory configure --backend-path /home/tobia/.local/share/ruflo/memory'` (Pitfall-Schutz, NICHT OneDrive-Pfad).
3. **Memory init:** `wsl -d Ubuntu-24.04 -u root -e bash -lc 'cd ~ && ruflo memory init --force'`. **NICHT** `import-all`/`allProjects=true`.
4. **Path-scoped Import** der Auto-Memory: `wsl ... bash -lc 'ruflo memory import --path "/mnt/c/Users/tobia/.claude/projects/C--Users-tobia-OneDrive-Desktop-Claude-Stuff/memory"'` (oder vergleichbarer ruflo-Subcommand) + `ruflo memory list` Verify.
5. **settings.json Edits** (Win32-Seite, `.claude/settings.json` oder `.claude/settings.local.json` je nach Persistenz):
   - Tool-Mode: `"toolGroups": ["memory", "monitor"]` oder env `CLAUDE_FLOW_TOOL_GROUPS=memory,monitor`
   - Intelligence-Loop: `"intelligence": {"topK": 3}`
   - Context-Autopilot: `"contextAutopilot": {"warnThreshold": 0.70, "pruneThreshold": 0.85}`
   - Statusline: `"statusLine": {...ohne DDD-Component...}`
   - Hooks-Subset: 6 enabled (session-start/end, pre/post-task, pattern-store/search), 21 explizit `enabled: false`
6. **SYSTEM.md §Ruflo-Status anlegen:** neue Sub-Sektion mit Aktivierungs-Datum, Pfade, Tool-Mode, Hooks aktiv, Doctor-Baseline-Referenz, Bridge-Status.
7. **log.md Append** (Vault `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md`): System-Event Phase 1.2-1.7 aktiviert.
8. **PIPELINE.md Item #20** Status-Update auf „Phase 1.2-1.7 ACTIVATED 30.04. (Sync-Commit `<sha>`); Phase 1.8 Doctor-Snapshot post-Activation; Phase 1.9 Welle 3; Phase 2 Eval ab ~05.05. passiv".
9. **Optional Codex-Review** der Sync-Welle (Single-Pass per Sparring-Heuristik) → Bei HIGH ≥2 zusätzliche Round.
10. **Commit „feat(ruflo): Phase 1.2-1.7 atomare §18-Sync-Welle (post-MCP-Switch)"**.

**Welle 1 redux Slot „AVGO 27.04. ScoreRecord-Backfill" (Task #8) wurde verschoben auf Welle 3** (post-BRK.B ≥05.05.) — Token-Bewusstsein 30.04. Codex-Round-2 98% Confidence bleibt gültig, Trigger jederzeit erfüllbar.

---

### 📅 Earnings-Pflichtslot 02.05. (Sa) — BRK.B Q1 FY26 [PRIORITÄT 2]

**Klasse-B-Pfad (Insurance-Exception, Score 75/D3, kein FLAG):**
- **Tag 0 (Sa 02.05.):** `earnings-recap`-Skill für Press-Release-Recap + manueller FLAG-Quick-Check (FLAG-Trigger/Resolve via `archive_flag.py` sofort, Score unverändert) + Pre-Call-Snapshot in CORE-MEMORY §12.7. Kein Score-Move, kein 8-File-Sync (siehe §19.1 Earnings-Call-Wait-Discipline).
- **Tag +1 (So 03.05. oder Mo 04.05. morgens):** Klasse-B-Vollanalyse via defeatbeta-MCP-Transcript-Read + dynastie-depot SKILL Schritt 7 → backtest-ready-forward-verify ScoreRecord-Append.

**Watch-Punkte:** Float-Modell ($686B Q1-Update), BNSF/BHE-CapEx-Track-Record (CapEx/OCF 45,6% historisch, kein FLAG), Greg Abel Insider-Block-Refresh (90d-Window), ROIC GAAP 5,6-7,8% (Screener-Exception, kein WACC-Vergleich nötig).

---

### 📋 Backlog (post-#20/02.05.)

1. **PIPELINE #29** CodeRabbit-Restbefund-Cleanup-Welle Kategorie-D — ~40+ Vault-Wiki-Findings (concepts/entities/sources/synthesis + 2 chapters.json + 1 transcript.md). Wiki-Konsolidierungs-Slot, ~2-3h via WIKI-SCHEMA.md-Workflows.
2. **PIPELINE #29** Kategorie-A Refactor-Entscheidung Faktortabelle „Offene Scores"-Tabelle: synchronisieren ODER löschen (Header sagt „0 von 11 — ALLE VOLLSTÄNDIG", Tabelle redundant zur Haupttabelle, mehrere stale Zeilen 17.04.).
3. **PIPELINE #2** Morning Briefing v3.0.6 Phase 4-6 Re-Test + Prod-Deploy (blockt Dashboard v2 + Track 5a/5b)
4. **PIPELINE #17** Beispiele.md 5-Anker-Refactor — Drift-Audit-Bedingung diskutabel; vor Execution Codex-Round-4 + Coverage-Matrix
5. **PIPELINE #18** AVGO 27.04. ScoreRecord-Backfill (rescoring-Append, ~30 Min)
6. **PIPELINE #16** INSTRUKTIONEN.md Slim-Refactor Variante A
7. **PIPELINE #22+#23** Helper `--porcelain -z` + Insider-Carryover-Discipline-Note (Konsolidierungs-Slot)
8. **earnings_calendar.py Stufe 2** (`system_audit.py`-Integration als 15. Check) + **Stufe 3** (SessionStart-Hook) — Re-Activation bei weiterem Drift trotz Stufe-1-Tool ODER Konsolidierungs-Slot
9. **earnings_calendar.py LOW-Hardening:** column-header-driven `portfolio_trigger_cell()` (statt 6-Spalten-Position-Lock) — Codex-Round-3 LOW-Finding aus #24-Review
10. **Pre-existing dirty cleanup (Rest):** `CheckResult` 0-byte (neue Anomalie) + `.claude/scheduled_tasks.lock`

---

### 🛠 System-State

**Last-Audit:** 2026-04-30T10:00:16Z (`--minimal-baseline` 3/3 PASS, STATE.md Last-Audit-Block auto-injected).

**Tools-Status:**
- `backtest-ready-forward-verify`-Skill v1.0.1 funktional (P1-P6 PASS V/MSFT/APH 28.-30.04.)
- Provenance-Gate v3.7.4 fail-close (8 Checks aktiv)
- defeatbeta-MCP funktional (latest_data_date 24.04.)
- yfinance funktional (Pre-Brief + 11/11 Probe-PASS + earnings_calendar.py Stufe 1)
- system_audit.py funktional (3/3 minimal-baseline PASS)

**FLAG-State (aktiv):** AVGO (insider_selling_20m) | APH (Score-basiert <65) | MSFT (CapEx/OCF, Bull-Case nicht vollumfänglich Trigger B FAIL Q3)

**Methodology-Watches offen (3, unverändert):**
- #21 V defeatbeta-ROIC-Methodology (Trigger Q3 FY26 ~Juli)
- #25 MSFT defeatbeta-WACC-Methodology FRED-Baseline (Trigger Q4 FY26 ~Juli)
- #26 MSFT Insider-Block-Backfill-Wert (Trigger 14.05.)

---

### 🧠 Memory-Hinweise (aus Auto-Memory relevant für nächste Session)

- `feedback_ruflo_memory_bridge_onedrive_pitfall` — OneDrive-Pfad + path-scoped Import (Phase 1.2 KRITISCH)
- `feedback_pre_commit_diff_inspection` — Pre-existing dirty separat halten (heute eingehalten: 2 Commits sauber separiert)
- `feedback_review_via_codex_not_advisor` — Im Dynastie-Depot immer Codex, nie advisor
- `feedback_codex_sparring_heuristic` — Single-Pass Default, Sparring-Loop bei HIGH ≥2 (heute Single-Pass, alle HIGH/MEDIUM gefixt)
- `feedback_earnings_call_wait_discipline` — Tag-0/Tag-+1-Split (BRK.B 02.05. → 03./04.05.)

---

*🦅 SESSION-HANDOVER.md | Dynasty-Depot | Stand: 30.04.2026 nach Welle 0 WSL-Setup + Persistierungs-Commit + MCP-Switch. Resume-Trigger: NEUE SESSION post-Claude-Restart → Phase 1.2-1.7 §18-Sync-Welle atomar; Earnings-Pflichtslot 02.05. (Sa) BRK.B Q1 FY26 Tag-0.*
