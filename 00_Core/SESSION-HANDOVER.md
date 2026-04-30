# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-30 (post PIPELINE #28 QT-Methodology-Review DONE + Sync-Commit `e1fa603`). Nächster primärer Resume-Trigger: **PIPELINE #24 Earnings-Calendar-Auto-Pull-Tool** (Stufe 1 yfinance) — danach **Phase 1.2 Ruflo Memory-Bridge** nach User-Schlafphase morgens 01.05.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `e1fa603` (skill(QT): v3.7.5→v3.7.6 B6 Drawdown-Modulator — PIPELINE #28 DONE). Vorhergehende Commits derselben Session-Welle: `462afe3` (handover MSFT-Done), `5396803` (score(MSFT) Q3 FY26), `88a267b` (xlsx APH-Sync), `a144c60` (score(APH) Q1 FY26). Working tree dirty mit pre-existing-Garbage (Shell-Escape-Anomalie-Files vom 28.04.+ und gelöschten 02_Analysen-PDFs vom Earnings-Reports-Folder-Move) — bewusst aus QT-Sync-Commit ausgelassen, separat zu cleanen.

**Skill-Paket-Stand:** v3.7.5 → **v3.7.6** (B6 Drawdown-Modulator, forward-only, Codex-R1→R4 96% Confidence). DEFCON-System v3.7 unverändert.

**Portfolio-State unverändert:** AVGO 84/D4-FLAG/0€ | BRK.B 75/D3/38,00€ | VEEV 74/D3/38,00€ | SU 69/D3/38,00€ | COST 69/D3/38,00€ | RMS 68/D3/38,00€ | ASML 68/D3/38,00€ | TMO 67/D3/38,00€ | V 64/D2/19,00€ | APH 61/D2-FLAG/0€ | MSFT 50/D2-FLAG/0€. Nenner 7,5. Summe 285€.

**STATE.md Critical-Alerts:** 30.04. PIPELINE #28 QT DONE | 30.04. MSFT/APH DONE | 14.05. MSFT Insider-Block-Re-Score post-14d-Skip-Window (#26) | **02.05. BRK.B Q1 (in 2 Tagen!)**.

---

### 🎯 Nächster Schritt — PIPELINE #24 Earnings-Calendar-Auto-Pull-Tool **[NEUE SESSION PRIORITÄT 1]**

**Resume-Trigger:** „PIPELINE #24 starten" oder „Earnings-Calendar-Tool implementieren".

**Kontext:** APH-Calendar-Drift-Lehre 29.04. — APH Q1 nicht im Trigger-Stand, weil 4 Files manuell gepflegt + FLAG-Mental-Off-Switch + kein Auto-Cross-Check Session-Start. yfinance-Probe 11/11 PASS für alle 11 Satelliten inkl. Non-US (`.AS`/`.PA`). Free, kein API-Key.

**Action (Stufe 1, ~45-60 Min):** `03_Tools/earnings_calendar.py` mit (a) Watchlist-Lese aus `01_Skills/dynastie-depot/config.yaml` (11 Satelliten), (b) `yfinance.Ticker(t).earnings_dates` future-Filter primär + `calendar` Fallback, (c) Diff-Report gegen PORTFOLIO „Nächster Trigger" + STATE Critical-Alerts + PIPELINE Kritische-Triggers-10d/30d, (d) Output stdout + optional `00_Core/SYSTEM.md §Earnings-Calendar-Status` (neue Sub-Sektion).

**BRK.B-Cross-Check ALS PFLICHT-SMOKE-TEST:** Tool muss vor Commit verifizieren, dass BRK-B Q1 Earnings-Datum 02.05.2026 (Saturday) korrekt gepullt wird. Bei Drift gegen aktuellen Stand → manuell ziehen + STATE/PORTFOLIO/PIPELINE-30d updaten.

**Stufenplan-Nachgang:**
- Stufe 2 (separater Slot): `system_audit.py`-Integration als 15. Check
- Stufe 3 (separater Slot): SessionStart-Hook (Drift-Warnung im Banner)

**Sync-Set (Stufe 1):** `03_Tools/earnings_calendar.py` (neu) + `00_Core/SYSTEM.md` (neue §Earnings-Calendar-Status) + `00_Core/INSTRUKTIONEN.md` (kurze Verweis-Klausel) + log.md (System-Event). Stage **#5 Sync-Set commit** in TaskList offen.

---

### 🌅 Slot +1 (User-Schlafphase, morgens 01.05.) — PIPELINE #20 Ruflo Phase 1.2

**Trigger:** „Ruflo Phase 1.2 starten" oder „Memory-Bridge aktivieren".

**Kontext:** User-OK explizit erteilt 30.04.; Earnings-Window 01.05. (Tag der Arbeit DE-Feiertag, keine US-Earnings) ist sauberer Slot vor BRK.B Sa 02.05.

**Memory-Pflicht-Reminder (KRITISCH):**
1. **OneDrive-Pfad-Pitfall** (Memory `feedback_ruflo_memory_bridge_onedrive_pitfall.md`): vor `npx ruflo memory init` zwingend `npx ruflo memory configure --backend-path %LOCALAPPDATA%/...` — sonst landet AgentDB im OneDrive-Sync und sync-zerschneidet sich selbst.
2. **NIEMALS `import-all`**: 4 Project-Namespaces, 37 Files würden Code-Domain-Pattern in Dynastie-Recall mischen. Nur **path-scoped Import** auf `C--Users-tobia-OneDrive-Desktop-Claude-Stuff` + Post-Verifikation per `memory list`.
3. **Codex-Nits-Nachfix** aus Phase 1.1 Round-2 (offen): (a) Hintertür-Klausel #5 in CLAUDE.md streichen, (b) Memory-Bridge-Tools `memory_import_claude` / `memory_search_unified` als allowed-tools explizit gating'd in CLAUDE.md.
4. **SYSTEM.md §Ruflo-Status** neu anlegen (Phase-1.2-Sync-Pflicht erstmals greifend).

**Sync-Set bei Phase 1.2:** CLAUDE.md (Nits-Nachfix) + SYSTEM.md §Ruflo-Status (neu) + log.md + PIPELINE.md (#20 Phase-Status).

---

### 📋 Backlog (post-#24/#20)

1. **PIPELINE #2** Morning Briefing v3.0.6 Phase 4-6 Re-Test + Prod-Deploy (Earnings-Window-Gate offen post-#28-DONE, blockt Dashboard v2 + Track 5a/5b)
2. **PIPELINE #17** Beispiele.md 5-Anker-Refactor — Drift-Audit-Bedingung diskutabel: MSFT-R1+R2-Doppel-Review war Methodology-Sparring, kein Skill-Wortlaut-Drift im V-Q2-Stil → Item könnte trigger-ready sein. Vor Execution Codex-Round-4 auf 5-Anker-Variante + Coverage-Matrix
3. **PIPELINE #18** AVGO 27.04. ScoreRecord-Backfill (rescoring-Append, ~30 Min)
4. **PIPELINE #16** INSTRUKTIONEN.md Slim-Refactor Variante A
5. **PIPELINE #22+#23** Helper `--porcelain -z` + Insider-Carryover-Discipline-Note (Konsolidierungs-Slot)
6. **Pre-existing dirty cleanup:** Shell-Escape-Anomalie-Files in Repo-Root + `01_Skills/insider-intelligence/`; `02_Analysen/Earnings Reports/`-Folder-Move sauber

**02.05. BRK.B Tag-0** earnings-recap-Skill + FLAG-Quick-Check (Klasse-B), Tag-+1 03./04.05.

---

### 🛠 System-State

**Tools-Status:**
- `backtest-ready-forward-verify`-Skill v1.0.1 funktional (P1-P6 PASS V/MSFT/APH 28.-30.04.)
- Provenance-Gate v3.7.4 fail-close (8 Checks aktiv)
- defeatbeta-MCP funktional (latest_data_date 24.04.)
- yfinance funktional (Pre-Brief + 11/11 Probe-PASS)

**FLAG-State (aktiv):** AVGO (insider_selling_20m) | APH (Score-basiert <65) | MSFT (CapEx/OCF, Bull-Case nicht vollumfänglich Trigger B FAIL Q3)

**Methodology-Watches offen (3 nach #28-DONE):**
- #21 V defeatbeta-ROIC-Methodology (Trigger Q3 FY26 ~Juli)
- #25 MSFT defeatbeta-WACC-Methodology FRED-Baseline (Trigger Q4 FY26 ~Juli)
- #26 MSFT Insider-Block-Backfill-Wert (Trigger 14.05.)

---

### 🧠 Memory-Hinweise (aus Auto-Memory relevant für nächste Session)

- `feedback_ruflo_memory_bridge_onedrive_pitfall` — OneDrive-Pfad + path-scoped Import (Phase 1.2)
- `feedback_pre_commit_diff_inspection` — Pre-existing dirty separat halten
- `feedback_review_via_codex_not_advisor` — Im Dynastie-Depot immer Codex, nie advisor
- `feedback_codex_sparring_heuristic` — Single-Pass Default, Sparring-Loop bei HIGH ≥2

---

*🦅 SESSION-HANDOVER.md | Dynasty-Depot | Stand: 30.04.2026 nach PIPELINE #28 QT-Methodology-Review DONE (Commit `e1fa603`, Skill-Paket v3.7.5→v3.7.6 B6 Drawdown-Modulator, Codex-R1→R4 96%). Resume-Trigger: PIPELINE #24 Earnings-Calendar-Tool, danach Slot +1 morgens 01.05. PIPELINE #20 Ruflo Phase 1.2.*
