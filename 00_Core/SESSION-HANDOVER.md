# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 Abend. **Provenance-Gate v3.1 KOMPLETT** + **Beispiele.md 4-Achsen-Architektur entschieden** (Codex 96%, Execution post-MSFT via PIPELINE #17/#18) + **Ruflo Phase 1.1 Override-Block committed** (Codex 2-Round PASS, Phase 1.2 deferred bis post-#17). Pipeline ready für **V Q2 First-Live-Run** (heute 28.04. AMC ~22:00, Auswertung 29.04. morgens). **Resume-Trigger: „!Analysiere V Q2 FY26 — First-Live-Run mit Provenance-Gate + Anker-Promotion (notizen-Hint)"**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `267a216` (Codex-Round-3 sec_edgar Multi-Word + Schritt-7 P3.5). Working tree clean. **9 Commits ahead** seit Handover `889becb`.

**Smoke-Test-Status:** schemas 14/14 ✓ + archive_score 5/5 ✓ + provenance_gate 9/9 ✓ (8a-8o inkl. Multi-Word) + skill 8/8 ✓ = **36/36**. Re-Validate-Sweep jsonl 28/28 PASS.

**Provenance-Gate Plan v3.1 — KOMPLETT** (11 Commits `5d97ddc`…`267a216`, Tasks 0-6.5 + Mini-Patches A/B + V/MSFT-Audit-Klausel + Codex-R3-Sofort-Fixes). Details: `git log --oneline 889becb..267a216` + CORE-MEMORY §10.

---

### 🎯 Nächster Schritt — V Q2 First-Live-Run

**Heute 28.04. AMC ~22:00 MESZ:** V Q2 FY26 Earnings (Quarter ending 31.03.2026). Daten morgen früh verfügbar.

**Pipeline-Erwartung im Erfolgsfall:**
1. Pre-Brief in `02_Analysen/V_pre-earnings_2026-04-28.md` enthält Pre-Append-Audit-Klausel (committed `4ca4654`, Zeile 9).
2. `!Analysiere V` 29.04. morgens via dynastie-depot Skill.
3. dynastie-depot Schritt 6c Pre-Flight-Klausel pro Block durchgehen (Sub-Score!=0 ↔ Rohwert/Carryover-Konsistenz).
4. **NEU — Anker-Promotion-Hint im ScoreRecord setzen** (Beispiele.md-4-Achsen-Architektur, PIPELINE #17): `notizen` enthält `anker_promotion_kandidat=us_voll_anker, mechanismen=[fundamentals_cap_50, forward_vs_backfill_korrektur, provenance_gate_first_run]`. Existierendes Pipeline-Feld, kein Schema-Change. Beim MSFT-Run analog mit `anker_promotion_kandidat=screener_exception_sub5, mechanismen=[capex_flag_bereinigter_pfad, finance_lease_decomposition, provenance_gate_second_run]`.
5. Schritt 7 Archive-Write via backtest-ready-forward-verify Skill — Pipeline-Sequenz: P1 → P2a (alle 3 Pflicht-Files modified) → P2b (V in PORTFOLIO.md) → **P3.5 (NEU, 8 Checks pass)** → P3 (skill_meta=ja → Δ-Gate) → P4/P5/P6 grün.
6. Joint-Confidence 92% → 95%+ erwartet.

**Falls P3.5 FAIL:** Recovery-Pfad via Workflow-Korrektur (Pflicht-Touch-Files berühren / `analyse_typ` umklassifizieren / `quellen` mit echten Quellen oder legitimen `*_carryover`-Suffixen befüllen / Versions-Drift via Migration-Pipeline lösen). Kein `--force`-Bypass.

**Eigener CORE-MEMORY §10-Eintrag** nach erfolgreicher Pipeline-Sequenz: konkrete P3.5-Output + tatsächlicher Δ-Gate-Outcome + Pre-Flight-Audit-Result + Anker-Promotion-Status (notizen-Feld gesetzt ja/nein).

---

### 🟡 Folge-Resume nach V+MSFT-Live-Runs (post-30.04. morgens)

**Resume-Trigger:** „Beispiele.md 4-Achsen-Refactor (PIPELINE #17) starten — V/MSFT-Anker einarbeiten + AVGO-FLAG-Patch + Cross-File-§-Refs"

**Vorbedingung:** V-Vollanalyse 29.04. morgens DONE (ScoreRecord mit Anker-Hint appended) + MSFT-Vollanalyse 30.04. morgens DONE (ScoreRecord mit Anker-Hint appended). Falls eine der beiden FAILed (P3.5 oder anders): Refactor blockiert bis Recovery + erfolgreicher Re-Run.

**Architektur (Codex-Round-1+2 96% Joint-Confidence):**
- **A. US-Pfad** = V (primär, Provenance-Gate-First-Run-Demo, Fundamentals-Cap 50, Forward-vs-Backfill-Korrektur D2-D3-Pfad) → AVGO (sekundär, D4-Range 80-85-Kalibrierung, FLAG-Override-Mechanik) → TMO (tertiär, Cross-Reference auf Sub#4 in C, primäre Beschreibung dort)
- **B. Non-US-IFRS-Pfad** = ASML unverändert (frisch v3.7 17.04., QT beidseitig hart 0, FY27-Watch, eodhd_intel.py + FRED-WACC + IFRS-16-Toleranz)
- **C. Screener-Exception-Katalog** = 6 Sub-Sektionen: #1 MKL (post-MKL-Vollanalyse, falls in dieser Session ausgeführt — sonst Pipeline-Test in Folge-Session) · #2 COST pending Q1 FY27 Dez · #3 RMS pending H1 Juli · **#4 TMO primary** (ROIC<WACC differenzierte QT, Doppelrolle mit A) · **#5 MSFT** (Provenance-Gate-Second-Run, CapEx-FLAG-Auflösungs-/Veto-Pfad) · **#6 ASML Cross-Reference** (Non-US/IFRS Pfad-B → siehe B)
- **D. Live-Disziplin** = bleibt in SKILL.md (Schritt 6c Pre-Flight, ma200_slope-Konvention), in Beispiele.md nur Demo-Block mit Verweis (TMO #28-Verstoß-Beispiel)
- **Legacy-Sektion** „Workflow-Historie" = SNPS, SPGI, EXPN, FICO, MKL-v3.5 — bleiben mit v3.5-Zeitstand-Banner als Workflow-Pattern-Referenzen (Goodwill-Bereinigung, TTM-Verzerrung, Datenlücken-Handling)

**Cross-File-Updates im selben Refactor-Commit:**
- `01_Skills/dynastie-depot/SKILL.md` — AVGO-Score-Erwähnung „85" → „84" + §11→§12/§13 in Zeile :90
- `00_Core/Faktortabelle.md` — §11→§12/§13 in Zeile :74
- `00_Core/PORTFOLIO.md` — §11→§12/§13 in Zeile :30
- `00_Core/STATE.md` — Sync-Kurzregel um config.yaml ergänzen (vs. INSTRUKTIONEN §18 v2.1)
- Vault `07_Obsidian Vault/.../log.md` — §11-Cleanup separat (Wiki-Trennung, eigenes Pipeline-Item ggf.)

**Item-Set:**
- **#17** Beispiele.md-Refactor (primärer Eintrag, ~45-60 Min Refactor + 15-30 Min Cross-File-Patches)
- **#18** AVGO 27.04. ScoreRecord-Backfill (`analyse_typ: rescoring`, Score 84 unverändert, FLAG-Referenz, ~15 Min via backtest-ready-forward-verify-Skill — optional in #17-Session mit-erledigen)
- **#19** Schema `anker_relevanz` deferred (V/MSFT brauchen es nicht)

**Sync-Set §18.2:** Beispiele.md + SKILL.md + Faktortabelle.md + PORTFOLIO.md + STATE.md + score_history.jsonl (nur bei #18-Mit-Erledigung) + log.md.

**MKL-Pipeline-Test-Status:** Bei der Refactor-Vorbereitung in dieser Session (28.04. nachmittags) auf User-Wunsch UNTERBROCHEN — Refactor in neuer Session priorisiert vor MKL-Vollanalyse, weil MKL-Output direkt in Sub#1 fällt. Falls MKL-Pipeline-Test weiterhin gewünscht, in einer der V/MSFT-Refactor-Folgesession nachholen oder als eigener Konsolidierungstag.

**Memory-Hooks für Refactor-Session:**
- `feedback_anchor_promotion_sync_gap.md` (NEU) — 4-Achsen-Pattern + Doppelrolle-via-Cross-Reference + Live-Frische schlägt Legacy + Cross-File-§-Refs prüfen
- `feedback_review_via_codex_not_advisor.md` — falls Refactor-Detail-Frage auftaucht: Codex statt Advisor

---

### 📅 Critical Operational

- **HEUTE 28.04. AMC ~22:00:** V Q2 FY26 — D2-Entscheidung (Technicals-Reversal?).
- **MORGEN 29.04. AMC ~22:30:** MSFT Q3 FY26 — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung). Pre-Append-Audit-Klausel auch in MSFT-Pre-Brief committed.
- **30.04. morgens:** !Analysiere MSFT als Second-Live-Run.
- **01.05.:** Sparplan-Tag (EXUSA 825€ Aufstockung + reguläre Allokation). User-Action.

### 🔵 Deferred / Follow-up (PIPELINE.md)

- **#17/#18 Beispiele.md-4-Achsen-Refactor + AVGO-ScoreRecord-Backfill:** Trigger post-MSFT-Live-Run 30.04.+ (siehe Folge-Resume-Block oben).
- **#19 Schema `anker_relevanz`:** deferred bis nächster Anker-Promotion ohne Pre-Brief-Hint oder Anker-Tickers >5.
- **#16 INSTRUKTIONEN.md Slim-Refactor:** post-V/MSFT-Live-Runs ODER Konsolidierungstag.
- **#15 Pipeline-Test-Architektur-Hardening (Codex-Round-3 MEDIUM #2 + LOW #3):** Case 7+8 sind Stub-Pipeline-Tests, kein echter Python-Entry-Point. Re-Activation-Trigger: nach 3-4 realen Live-Runs P3-vor-P3.5-Bypass-Audit. Mitigation aktiv via Schritt 6c + Pre-Append-Audit.
- **#11 Atomic-Write-Hardening portfolio_risk.py:** frozen, Re-Activation bei Incident oder Track-4-Auto-Hook.
- **#7 Track 5b FRED Macro-Regime-Filter:** deferred bis Sparrate >1.000€/Monat oder Depotwert >50.000€ oder Regime-Aware-Schmerz.
- **#20 Ruflo-Integration Phase 1.2:** Trigger post-#17/#18 (NICHT direkt nach Earnings). Pre-Read: `00_Core/RUFLO-INTEGRATION-PLAN.md` (committed `c9a3ed5`) + `00_Core/RUFLO-PLAN-META-REVIEW.md` (working-tree-Draft 28.04. — 10 Plan-Patches P1-P10 + 9 Pre-Conditions + 8-Schritt-Kickoff-Checkliste). Risiko-Re-Label MITTEL (OneDrive-AgentDB-Backend + Memory-Path-Pollution). Memory: `feedback_ruflo_memory_bridge_onedrive_pitfall.md`.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€ (FLAG-modifiziert), DEFCON v3.7 / Skill-Paket v3.7.4
- AVGO 84 (FLAG Insider seit 27.04., Sparrate→0€), TMO 67 D3, MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.1 | Slim-Resume — Policy B | Stand: 2026-04-28 Abend*
