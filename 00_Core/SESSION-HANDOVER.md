# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 Abend. **Provenance-Gate Plan v3.1 KOMPLETT ABGESCHLOSSEN** (Tasks 0-6.5 + Mini-Patches A/B + V/MSFT-Pre-Append-Audit-Notices + Codex-Round-3-Reconcile). Joint-Confidence ~95%. Pipeline ready für **V Q2 First-Live-Run** (heute 28.04. AMC ~22:00, Auswertung 29.04. morgens). **Resume-Trigger nach Pause: „!Analysiere V Q2 FY26 — First-Live-Run mit Provenance-Gate"**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `267a216` (Codex-Round-3 sec_edgar Multi-Word + Schritt-7 P3.5). Working tree clean. **9 Commits ahead** seit Handover `889becb`.

**Smoke-Test-Status:** schemas 14/14 ✓ + archive_score 5/5 ✓ + provenance_gate 9/9 ✓ (jetzt 8a-8o inkl. Multi-Word) + skill 8/8 ✓ = **36/36**. Re-Validate-Sweep jsonl 28/28 PASS.

**Provenance-Gate Plan v3.1 — Commits (chronologisch):**
| Commit | Task | Was |
|---|---|---|
| `5d97ddc` | 0.5 | TMO #28 Block-Coverage-Backfill (Migration-Helper, byte-level Line-Endings, idempotent) |
| `ef6979c` | 1 | versions.py SSoT + schemas Refactor |
| `5f4a6c5` | 2 | Schicht D Block-Coverage-Validator + Tests D1-D4 + archive_score-Fixture-Patch |
| `06ff82c` | A+B | Mini-Patches: Doc-Typo + Plan-File D1-D4 IDs |
| `cacf2a0` | 3 | provenance_gate.py Schicht B — 8 Checks fail-close, Carryover-Whitelist, 9/9 Smoke-Tests |
| `d039a5b` | 4 | forward-verify SKILL.md Phase P3.5 + Authoritative-Sources + FAIL-Phase-Enum |
| `e3547e9` | 5 | _smoke_test.py Case 7 (Integration fail-close) + Case 8 (Pipeline-Sequence-Order) |
| `507eb64` | 6 | SYSTEM.md + INSTRUKTIONEN §18.5 + CORE-MEMORY §10 + log.md Union-Scope |
| `bd83631` | 6.5 | dynastie-depot Schritt 6c Pre-Flight-Klausel + ma200_slope-Threshold |
| `4ca4654` | V/MSFT | Pre-Append-Audit-Klausel in Pre-Earnings-Briefs |
| `267a216` | R3 | Codex-Round-3 Sofort-Fixes (sec_edgar Multi-Word + Schritt-7-Summary) |

---

### 🎯 Nächster Schritt — V Q2 First-Live-Run

**Heute 28.04. AMC ~22:00 MESZ:** V Q2 FY26 Earnings (Quarter ending 31.03.2026). Daten morgen früh verfügbar.

**Pipeline-Erwartung im Erfolgsfall:**
1. Pre-Brief in `02_Analysen/V_pre-earnings_2026-04-28.md` enthält Pre-Append-Audit-Klausel (committed `4ca4654`).
2. `!Analysiere V` 29.04. morgens via dynastie-depot Skill.
3. dynastie-depot Schritt 6c Pre-Flight-Klausel pro Block durchgehen (Sub-Score!=0 ↔ Rohwert/Carryover-Konsistenz).
4. Schritt 7 Archive-Write via backtest-ready-forward-verify Skill — Pipeline-Sequenz: P1 → P2a (alle 3 Pflicht-Files modified) → P2b (V in PORTFOLIO.md) → **P3.5 (NEU, 8 Checks pass)** → P3 (skill_meta=ja → Δ-Gate) → P4/P5/P6 grün.
5. Joint-Confidence 92% → 95%+ erwartet.

**Falls P3.5 FAIL:** Recovery-Pfad via Workflow-Korrektur (Pflicht-Touch-Files berühren / `analyse_typ` umklassifizieren / `quellen` mit echten Quellen oder legitimen `*_carryover`-Suffixen befüllen / Versions-Drift via Migration-Pipeline lösen). Kein `--force`-Bypass.

**Eigener CORE-MEMORY §10-Eintrag** nach erfolgreicher Pipeline-Sequenz: konkrete P3.5-Output + tatsächlicher Δ-Gate-Outcome + Pre-Flight-Audit-Result.

---

### 📅 Critical Operational

- **HEUTE 28.04. AMC ~22:00:** V Q2 FY26 — D2-Entscheidung (Technicals-Reversal?).
- **MORGEN 29.04. AMC ~22:30:** MSFT Q3 FY26 — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung). Pre-Append-Audit-Klausel auch in MSFT-Pre-Brief committed.
- **30.04. morgens:** !Analysiere MSFT als Second-Live-Run.
- **01.05.:** Sparplan-Tag (EXUSA 825€ Aufstockung + reguläre Allokation). User-Action.

### 🔵 Deferred / Follow-up (PIPELINE.md)

- **#15 Pipeline-Test-Architektur-Hardening (Codex-Round-3 MEDIUM #2 + LOW #3):** Case 7+8 sind Stub-Pipeline-Tests, kein echter Python-Entry-Point. Re-Activation-Trigger: nach 3-4 realen Live-Runs P3-vor-P3.5-Bypass-Audit. Mitigation aktiv via Schritt 6c + Pre-Append-Audit.
- **#11 Atomic-Write-Hardening portfolio_risk.py:** frozen, Re-Activation bei Incident oder Track-4-Auto-Hook.
- **#7 Track 5b FRED Macro-Regime-Filter:** deferred bis Sparrate >1.000€/Monat oder Depotwert >50.000€ oder Regime-Aware-Schmerz.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€ (FLAG-modifiziert), DEFCON v3.7 / Skill-Paket v3.7.4
- AVGO 84 (FLAG Insider seit 27.04., Sparrate→0€), TMO 67 D3, MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`

### 📊 Codex-Sparring-Bilanz (Session 28.04.)

- **Round 1** (Single-Pass auf Tasks 0-2): 0 HIGHs, 1 MEDIUM (Plan-File-Drift), 2 LOWs, 4 PASSes.
- **Round 2** (Reconcile + 95%-Frage): 1 NEUER HIGH (Pre-Flight-Klausel war Frame-blind in R1), 1 MEDIUM (Plan-Inline), 1 LOW (ma200_slope), 1 NEUER 4. Punkt (V/MSFT Audit).
- **Round 3** (Single-Pass auf Tasks 3-6.5 + Mini-Patches + Audit-Notices): 0 HIGHs, 2 MEDIUMs (sec_edgar toter Whitelist-Eintrag + Case 7 tautologisch), 2 LOWs (Case 8 Stub + Schritt-7-Summary fehlt P3.5). Variante 1 sofort committed (`267a216`), Variante 2 deferred via PIPELINE #15.
- **Bilanz:** Reconcile-Round-2 fand HIGH dass R1 nicht hatte. Round-3 fand realen Whitelist-Bug (sec_edgar Multi-Word) + Doku-Drift (Schritt-7-Summary). Memory `feedback_codex_sparring_heuristic.md` validiert.

### Memory-Hooks aktiv

- feedback_review_via_codex_not_advisor.md — 3 Codex-Rounds in Session 28.04.
- feedback_codex_sparring_heuristic.md — VALIDIERT Round 3: Single-Pass-Default fand 2 MEDIUM/2 LOW ohne Reconcile-Bedarf.
- feedback_windows_python_crlf_text_mode.md — byte-level Line-Ending-Preservation (0 ungewollte Konvertierungen).
- feedback_pre_commit_diff_inspection.md — alle 11 Commits via `git diff --cached --stat` vor commit verifiziert.
- feedback_onedrive_edit_collision.md — keine Kollisionen.

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B | Stand: 2026-04-28*
