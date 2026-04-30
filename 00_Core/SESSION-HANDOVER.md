# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-30 (post PIPELINE #24 Stufe 1 DONE Commit `0253813` + Cleanup-Welle Commit `213b198`). Nächster primärer Resume-Trigger: **Slot +1 morgens 01.05. PIPELINE #20 Ruflo Phase 1.2 Memory-Bridge**. Earnings-Pflichtslot **02.05. (Sa) BRK.B Q1 FY26 Tag-0** earnings-recap-Skill + FLAG-Quick-Check; Tag-+1 03./04.05.

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

### 🌅 Slot +1 (User-Schlafphase, morgens 01.05.) — PIPELINE #20 Ruflo Phase 1.2 [PRIORITÄT 1]

**Trigger:** „Ruflo Phase 1.2 starten" oder „Memory-Bridge aktivieren".

**Kontext:** User-OK explizit erteilt 30.04.; Earnings-Window 01.05. (Tag der Arbeit DE-Feiertag, keine US-Earnings) ist sauberer Slot vor BRK.B Sa 02.05. PIPELINE #24 Stufe 1 + Cleanup-Welle haben den Tag 30.04. abgeschlossen.

**Memory-Pflicht-Reminder (KRITISCH):**
1. **OneDrive-Pfad-Pitfall** (Memory `feedback_ruflo_memory_bridge_onedrive_pitfall.md`): vor `npx ruflo memory init` zwingend `npx ruflo memory configure --backend-path %LOCALAPPDATA%/...` — sonst landet AgentDB im OneDrive-Sync und sync-zerschneidet sich selbst.
2. **NIEMALS `import-all`**: 4 Project-Namespaces, 37 Files würden Code-Domain-Pattern in Dynastie-Recall mischen. Nur **path-scoped Import** auf `C--Users-tobia-OneDrive-Desktop-Claude-Stuff` + Post-Verifikation per `memory list`.
3. **Codex-Nits-Nachfix** aus Phase 1.1 Round-2 (offen): (a) Hintertür-Klausel #5 in CLAUDE.md streichen, (b) Memory-Bridge-Tools `memory_import_claude` / `memory_search_unified` als allowed-tools explizit gating'd in CLAUDE.md.
4. **SYSTEM.md §Ruflo-Status** neu anlegen (Phase-1.2-Sync-Pflicht erstmals greifend).

**Sync-Set bei Phase 1.2:** CLAUDE.md (Nits-Nachfix) + SYSTEM.md §Ruflo-Status (neu) + log.md + PIPELINE.md (#20 Phase-Status).

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

*🦅 SESSION-HANDOVER.md | Dynasty-Depot | Stand: 30.04.2026 nach PIPELINE #24 Stufe 1 DONE (Commit `0253813`) + CodeRabbit-Restbefund-Cleanup-Welle (Commit `213b198`). Resume-Trigger: Slot +1 morgens 01.05. PIPELINE #20 Ruflo Phase 1.2; Earnings-Pflichtslot 02.05. (Sa) BRK.B Q1 FY26 Tag-0.*
