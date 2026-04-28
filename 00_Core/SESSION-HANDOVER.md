# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 ~Abend — **Provenance-Gate Plan v3.1 + Spec v2.1 committed & ready for execution.** Plan v3 (Commit `5c48f1c`) wurde von Codex Single-Pass-Review als **B-Verdikt** klassifiziert mit 4× HIGH. Codex-Round-2-Sparring resolvte alle HIGHs, Round-3-Confirm-Pass meldete A+ execution-ready. Plan v3.1 (Commit `47000fc`) integriert alle Patches. **Resume-Trigger ab hier morgen früh: „Provenance-Gate Plan executieren"** (kontextfrei in fresh session, alle Anker im Plan-File selbst).

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `47000fc` (Plan v3.1 + Spec v2.1, refresh). Commit `5c48f1c` davor war Plan v3 + Spec v2 (vor Sparring-Resolution). Working tree clean. Push-Status nach Commit-Block: siehe git log.

**Was Session 28.04. GETAN hat:**
1. Plan v3 + Spec v2 geschrieben (Commit `5c48f1c`) basierend auf Drift-Refresh-Prep aus voriger Session
2. Codex Single-Pass-Review auf Spec v2 → A mit Patches (1× HIGH Carryover-Substring-Bypass via `pre_gate_xyzzy_carryover` → resolved durch Whole-Word-Source-Match + Reason-Terminal + ir_-Prefix)
3. Spec v2 inline gepatcht
4. Codex Single-Pass-Review auf Plan v3 → **B-Verdikt mit 4× HIGH:**
   - HIGH-1+4: TMO #28 hat moat 0/1 + technicals 0/4 (verifiziert via JSONL-Inspect, mein Handover-v3-Banner war faktisch falsch)
   - HIGH-2: `_is_placeholder("") == False` → Empty-String-Bypass von Check #7
   - HIGH-3: Case 7 testet keine Pipeline-Sequence-Order P3.5-vor-P3
5. Codex-Round-2-Sparring confirmed Lösungs-Pfade
6. Spec v2.1 + Plan v3.1 geschrieben mit allen 4 HIGH-Patches + MEDIUMs
7. Codex-Round-3-Confirm-Pass → LOW refinement (2 Edits eingebaut), keine neuen HIGHs, A+ execution-ready (Commit `47000fc`)

**Kein Code geschrieben außer Migration-Helper-Skript-Template (in Plan v3.1 Task 0.5 inline). Plan-Execution erfolgt morgen früh in separater Session.**

---

### 📋 Offene Tasks (fresh-session 29.04. morgens)

Plan v3.1 ist self-contained — alle Anker, Code-Snippets, Tests, Commit-Messages im Plan-File. Tasks-Reihenfolge:

| Task | Was | Tool/Agent | Geschätzte Zeit |
|---|---|---|---|
| 0 | Pre-Check Step 0.1 (`PASS: N >= 28 / FAIL: 0`) | inline bash | 5 min |
| **0.5** | **Migration-Helper TMO #28 Block-Coverage** (Wert-Recherche + Helper-Skript + Idempotenz-Test + Commit) | direkt — **Wert-Recherche human** (siehe unten) | 60-90 min |
| 1 | versions.py SSoT + schemas refactor + Commit | subagent-driven oder direkt | 20 min |
| 2 | Block-Coverage-Validator Schicht D + Tests D1-D4 + Re-Validate-Sweep + Commit | subagent-driven | 30-45 min |
| 3 | provenance_gate.py Schicht B (4 Sub-Steps a-d) + Smoke-Tests 9/9 + Commit | subagent-driven | 45-60 min |
| 4 | SKILL.md Phase P3.5 + Authoritative-Sources + Commit | direkt (Markdown) | 15-20 min |
| 5 | Case 7 Integration-Test + Case 8 Pipeline-Sequence-Order + Commit | subagent-driven | 30-40 min |
| 6 | SYSTEM.md + INSTRUKTIONEN §18.5 + CORE-MEMORY §10 + log.md (4 Files Union-Scope) + Commit | direkt (Markdown) | 20-30 min |
| Verification | VC.1 + VC.2 End-to-End | inline | 10 min |
| First-Live-Run | !Analysiere V Q2 FY26 (Earnings 28.04. AMC ~22:00, Daten morgens verfügbar) | dynastie-depot Skill | ~2-3h |

**Geschätzte Gesamt-Zeit Plan-Execution:** ~4-6h (ohne V-Analyse). V als First-Live-Run gegen 12-13 Uhr realistisch.

---

### 🔧 Wert-Recherche Task 0.5.1 (BLOCKER vor Helper-Schreiben)

Migration-Helper braucht historisch korrekte Werte zum Score-Datum 2026-04-23:

| Feld | Quelle | Notiz |
|---|---|---|
| `gm_trend_3j_pct_p_a` | TMO Q1 FY26 Vollanalyse-Excel im `02_Analysen/` ODER GuruFocus 3j-GM-Historie | Primary: Excel-Datei wenn vorhanden |
| `rel_strength_sp500_6m_pct` | yfinance Pre-Briefing 22.04. ODER `yf.Ticker('TMO').history(period='6mo', end='2026-04-22')` vs SPY | reproduzierbar via fixed end-date |
| `rel_staerke_sp500_6m_pct` | = rel_strength (Alias-Spiegel) | identischer Wert |
| `kurs_vs_200ma_pct` | yfinance dito 22.04. close vs MA200 | reproduzierbar |
| `ma200_slope` | yfinance dito | float oder Enum, je nach `MetrikenRoh`-Schema |

**Pfad-Vermutung:** `02_Analysen/TMO_Q1_FY26_2026-04-23.xlsx` (oder ähnlich). Wenn Datei nicht existiert, dann ausschließlich yfinance + GuruFocus-Reproduktion.

**Fallback wenn Werte nicht reproduzierbar:** TMO #28 retroaktiv auf `analyse_typ="rescoring"` umklassifizieren (semantisch unsauber, mit User abklären). Standard-Pfad: Migration mit echten Werten.

---

### ⚠️ Sicherungspunkte vor Plan-Execution

- **Step 0.1 Pre-Check:** `>= 28 / FAIL: 0` — wenn schon vor Task 0.5 mehr Records FAIL liefern (z.B. weil seit 28.04. neue Vollanalyse appendiert wurde mit ähnlichem Coverage-Defekt): zusätzliche Migration-Steps nötig.
- **Task 0.5.4 Idempotenz:** dry-run #1 == dry-run #2 (byte-identisch). Apply #1 success, Apply #2 = no-op.
- **Codex-Round-3-LOW-Patch:** Helper hat Ellipsis-Sentinel-Guard in `main()` — Subagent kann nicht versehentlich mit `BACKFILL_VALUES = {field: ...}` laufen.
- **Task 2.7 Re-Validate-Sweep:** muss nach Task 0.5 + Task 2 GRÜN sein (post-Migration-State erfüllt Block-Coverage). Falls nicht → weiterer Record hat Coverage-Defekt → manuelle Inspect.

---

### 🚀 Fresh-Session-Workflow morgen früh

1. Session startet: STATE.md + PORTFOLIO.md geladen (default).
2. Diesen Banner lesen.
3. **Trigger: „Provenance-Gate Plan executieren"** ODER falls V-Earnings priorisiert: zuerst V-Pre-Brief lesen, dann Plan-Execution erst nach.
4. TaskList lesen (4 Tasks von Vor-Session sind completed; neue Tasks in fresh session anlegen pro Plan-Phase).
5. Pre-Check Step 0.1 → GRÜN nötig vor Task 0.5.
6. Task 0.5 Wert-Recherche: erst `02_Analysen/`-Excel-Pfad checken, dann Helper-Skript schreiben (Plan v3.1 hat Template), Idempotenz-Test, Commit.
7. Tasks 1-5 via `superpowers:subagent-driven-development` (oder `executing-plans`) — Subagent-Reviews nach jedem Task-Commit.
8. Task 6 direkt (4 Markdown-Files Union-Scope, kein Subagent).
9. Verification VC.1 + VC.2.
10. **!SyncBriefing** vor Session-Ende falls Briefing-Version in SYSTEM.md geändert (siehe CLAUDE.md §25 + Routing-Table).
11. **!Analysiere V Q2 FY26** als First-Live-Run mit aktivem Provenance-Gate.

**Wichtig:** Plan v3.1 ist atomar pro Task — bei FAIL eines Tasks NICHT die folgenden starten. Recovery siehe Plan §Step 0.2 + Spec §7.2.

---

### 📅 Critical Operational

- **HEUTE 28.04. AMC ~22:00:** V Q2 FY26 Earnings — Pre-Brief `02_Analysen/V_pre-earnings_2026-04-28.md`.
- **MORGEN 29.04. AMC ~22:30:** MSFT Q3 FY26 Earnings — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung).
- **30.04. morgens:** !Analysiere MSFT als Second-Live-Run mit Gate (FLAG-Review-Earnings — schwerste Analyse der Woche, Gate ist dann battle-tested durch V).
- **01.05.:** Sparplan-Tag (EXUSA 825€ + reguläre Allokation). User-Action.
- **30.04.+:** 5a Skill-Promotion freigegeben (post-Earnings, separate Session, Plan `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md`).

### Operativ unverändert

- 11 Satelliten, Sparraten 285€, DEFCON v3.7
- AVGO 84 (FLAG Insider seit 27.04.), TMO 67 D3 (post-Q1-Upshift 23.04.), MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`

### Sparring-Bilanz Provenance-Gate (Session 28.04.)

- 5 Codex-Rounds total: 2× Drift-Refresh-Prep (vor-Session) + 1× Spec-Review + 2× Plan-Review-Sparring + 1× Confirm-Pass
- 6 HIGHs gefunden, alle resolved (3 davon faktisch verifiziert via JSONL-Inspect / Code-Re-Read / Test-Bypass-Reproduktion)
- 0 neue HIGHs nach Round 3
- 4 LOW-Refinements eingebaut

### Memory-Hooks aktiv

- feedback_review_via_codex_not_advisor.md — Reviews via Codex (5x in Session 28.04. Single-Pass + Sparring-Loops)
- feedback_codex_sparring_heuristic.md — Single-Pass Default; HIGH-Count ≥2 = Reconcile-Loop. Heute Plan-Review HIGH=4 → 2 Sparring-Rounds + Confirm-Pass nötig (innerhalb der Heuristik-Grenze)
- feedback_tavily_connector_uuid_rotation.md, feedback_onedrive_edit_collision.md, feedback_pre_commit_diff_inspection.md, feedback_windows_python_crlf_text_mode.md — Standing-Practices

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*
