# 🎯 STATE.md — Dynasty-Depot Live-Status
**Single Entry Point für Session-Start** | Stand: 21.04.2026 Nachmittag (**Systemhygiene-Sync-Welle Phase A+B+C committed** — CORE-MEMORY Header/§1/§3/§10 nachgezogen + log.md sync-wave Eintrag + **neue Section „🗺 Aktive Pipeline (SSoT)"** unten eingebaut; Phase D (Brainstorming `system_audit.py` Sub-Spec) + Phase E (Plan + TDD-Build) stehen als nächstes an, dann Phase F (Provenance-Plan-Execution) vor TMO Q1 23.04.; **Drift-Migration 12/27 → 27/27 PASS** in `score_history.jsonl` steht; v3.0.4 Briefing-Hotfix weiter pending; v2.1 Prod stable) | System: DEFCON v3.7 (unverändert)

> **Prinzip:** Diese Datei genügt für 90% der Sessions. Tiefere Quellen on-demand:
> - Lektionen/Historie → `CORE-MEMORY.md`
> - Workflows/Scoring-Skalen → `INSTRUKTIONEN.md`
> - Strategie/Allokation → `KONTEXT.md`
> - Score-Detail → `Faktortabelle.md`
> - Last-Session-Handover → `SESSION-HANDOVER.md`

---

## Portfolio-State (11 Satelliten)

| Ticker | Score | DEFCON | Rate | FLAG | Nächster Trigger |
|--------|-------|--------|------|------|------------------|
| AVGO | 84 | 🟢 4 | 35,63€ | ⚠️ Insider-Review (OpenInsider!) | Q3 FY26 |
| BRK.B | 75 | 🟡 3 | 35,63€ | ✅ Insurance Exception | Q-Earnings Mai |
| VEEV | 74 | 🟡 3 | 35,63€ | ✅ | Earnings-Trigger |
| SU | 69 | 🟡 3 | 35,63€ | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | 35,63€ | ✅ Screener-Exception | Q1 FY27 ~Dez |
| RMS | 68 | 🟡 3 | 35,63€ | ✅ Screener-Exception | H1 Juli/Aug |
| ASML | 68 | 🟡 3 | 35,63€ | ✅ | Q2 2026 (Q1 17.04. Vollanalyse ✅) |
| V | **63** | **🟠 2** | **17,81€** | ✅ | **28.04. Q2 FY26 — D2-Entscheidung** |
| TMO | **64** | 🟠 2 | 17,81€ | ✅ (fcf_trend_neg schema-trigger, WC-Noise → **nicht aktiviert**) | **23.04. Q1 — FLAG-Resolve-Gate** |
| APH | 63 | 🟠 2 | **0€** | 🔴 Score-basiert | 23.07. Q2 |
| MSFT | 59 | 🟠 2 | **0€** | 🔴 CapEx/OCF 83.6% | **29.04. Q3 FY26 — FLAG-Review** |

**Sparraten-Nenner:** 7×1.0 + 2×0.5 + 2×0 = **8.0** → 35,63€ volle / 17,81€ D2 / 0€ FLAG. **Summe 285€** ✓

> **18.04.2026 Änderung:** V-Forward-Vollanalyse (63, D2) ersetzt 17.04.-Backfill-Projektion (86, D4) — siehe CORE-MEMORY §11. Gleichzeitig Schema-SKILL-Threshold-Drift gefixt: 5 Tickers (BRK.B/VEEV/SU/COST/RMS) D4→D3 (Label-Fix, Sparrate unverändert), APH D3→D2 (FLAG überschreibt Sparrate weiterhin). Nenner schrumpft von 8.5 auf 8.0, volle Rate steigt 33,53€ → 35,63€.

---

## Aktive Watches

- **V D2-Kritik (NEU 18.04.):** 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA, Crowd-Sell-Ratio 0%. Q2 FY26 am 28.04. entscheidet: Beat + Guidance-Bestätigung → Technicals-Reversal möglich (zurück Richtung D3). Miss → weiterer Downshift Richtung D1.
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- **AVGO Insider $123M (90d)** — wahrscheinlich Post-Vesting (Broadcom-Muster Tan/Brazeal/Spears). Vor FLAG-Aktivierung OpenInsider manuell prüfen.
- **TMO D2-Kritik + FLAG-Resolve-Gate (NEU 18.04.):** Score 64 (Forward), fcf_trend_neg schema-getriggert (FY25 FCF -13,4% YoY, CapEx +8,9%) aber **nicht aktiviert** — WC-Delta FY25 -1766M erklärt FCF-Rückgang vollständig (>Δ FCF -974M), 4J-Trajektorie FY22-25 $6,9→6,9→7,3→6,3B zeigt Plateau, OpInc +5,1%. Q1 23.04. = natürlicher Resolve-Gate: WC-Unwind + FCF-Recovery bestätigt → kein FLAG; fehlende Reversibilität → fcf_trend_neg-Trigger nachtragen. Ersatz-Vorbereitung ZTS aktiv.
- **MSFT FLAG-Auflösungs-Pfad:** Q3 29.04. — bereinigtes CapEx/OCF <60% (Finance Lease $19.5B raus) = Auflösung. Darüber = Veto-Verschärfung.

---

## Nächste kritische Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| **23.04.** | **TMO** | **B** | **Q1 — D2-Entscheidung + fcf_trend_neg Resolve-Gate (WC-Unwind?)** |
| **28.04.** | **V** | **B** | **Q2 FY26 — D2-Entscheidung (Technicals-Reversal?)** |
| 28.04. | SNPS/SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — FLAG-Review** |
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |

---

## 🗺 Aktive Pipeline (SSoT)

> **Zweck:** Single-Source-of-Truth für alle offenen Pläne, Gates und Termine. Ersetzt die bisherige Fragmentierung über STATE.md + SESSION-HANDOVER.md + Plan-Files + Memory (jedes Mal aus 4 Quellen rekonstruiert — exakter Anti-Pattern der 21.04.-Drift-Lesson).
> **Pflege-Pflicht:** Update bei (a) jedem neuen Plan-Commit in `docs/superpowers/plans/`, (b) jedem Gate-Passage, (c) jeder Status-Transition (ready→in-progress→done, deferred→active). Parallel zur §18-Sync-Welle (aber eigener Trigger — Plan-Commit ist nicht automatisch Score-Change).

### 🔴 Unmittelbar / Primär-Track

1. **Systemhygiene-Welle Phase A-E (SSoT-Aufbau + Audit-Tool-Bau)** — Session 21.-22.04.2026. Phase A+B+C (Sync-Sweep) `in_progress`; Phase D (Brainstorming Sub-Spec `system_audit.py`) + Phase E (Plan + TDD-Build) stehen direkt danach. Quell-Dokument: `SESSION-HANDOVER.md`.
2. **Morning Briefing v3.0.4 Hotfix** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks, ~90 Min). Prod läuft v2.1 (Rollback nach Halluzinations-Incident 20.04.). Hotfix ergänzt §3a Anti-Fallback-Guard + neuer Test T5 Adversarial-Stale-Shibui. Gate A erst nach v3.0.4-PASS.
3. **Score-Append Provenance-Gate** — Plan v2 `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (7 Tasks, 40 Steps) + Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`. Critical **vor** TMO Q1 23.04. (erster echter Forward-Run durch neue Pipeline mit P3.5 fail-close). Execution in Phase F dieser Session-Sequenz.
4. **System-Audit-Tool `03_Tools/system_audit.py` + Slash-Command `/SystemAudit`** — Sub-Spec + Plan + Build in Phase D+E dieser Session-Sequenz. Scope: JSONL-Schema + Markdown-Cross-Drift + Existence-Check + Skill-Version + Pipeline-SSoT-Consistency (Kern); Vault-Backlinks + Status-Matrix (Optional mit Timeout).

### 🟠 Portfolio — Kritische Triggers 10 Tage

- **23.04. TMO Q1** — D2-Entscheidung + fcf_trend_neg Resolve-Gate. Erster Live-Test Provenance-Gate + §4-Router Status-Matrix B1-B24 + backtest-ready-forward-verify.
- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal?).
- **29.04. MSFT Q3 FY26** — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung).

### 🟡 Bereit, wartet auf Gate A (~24.04. frühestens nach v3.0.4-Deploy)

5. **Track 5a SEC EDGAR Skill-Promotion** — Plan `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks). Re-Validation-Check nach 6-Paper-Ingest B21-B24 möglicherweise nötig.
6. **Track 5b FRED Macro-Regime-Filter** — Plan `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (15 Tasks). User-Aktion vor Start: FRED-API-Key registrieren. B19 (LLM-Regime-Shift-Bias) stärkt wissenschaftliche Begründung.

### 🔵 Deferred / Explizit zurückgestellt

7. **v3.1 Cache-Refactor** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.1-cache-refactor.md`. Trigger: „262s im Alltag stört" ODER „>400s-Alert wiederholt".
8. **Track 4 ETF+Gold-Erweiterung** — Blockiert auf User-Input (ETF-Ticker IWDA.AS/SWDA.L/EUNL.DE? Gold-Ticker SGLD.DE/4GLD.DE/GC=F?). Gleichzeitig **Open-Backlog-Item Daily-Persist-Stale** auflösen (`portfolio_returns.jsonl` + `benchmark-series.jsonl` je 1 Record seit 17.04. — Cron-/Hook-Mechanismus für Auto-Persist einbauen).
9. **KG-Roadmap v0.1 `draft-frozen`** (`07_Obsidian Vault/.../synthesis/Knowledge-Graph-Architektur-Roadmap.md`). Re-Review-Trigger: Cross-Entity-Bedarf ODER Score-Archiv-Interim-Gate 2026-10-17.

### ⏰ Long-Term-Gates (chronologisch)

| Datum | Gate | Owner-Aktion |
|-------|------|--------------|
| ~28.04.2026 | Tavily Dev-Key Rotation | User: Key `tvly-dev-4PYXp...` in Dashboard rotieren (7-Tage-Uhr ab v3.0.4-Prod-Deploy) |
| 2026-07-19 | Track 5a 90-Tage-Audit | EDGAR-Skill Performance-Review (falls promoted) |
| 2026-10-17 | Score-Archiv-Interim-Gate | 6-Monats-Sanity-Check `score_history.jsonl` (Forward-Window + Duplicate-Guard) |
| 2027-10-19 | R5 Interim-Gate | 18-Mo-Dry-Run `risk-metrics-calculation` + Data-Quality `portfolio_returns.jsonl` (inkl. FX-Conversion-Check) |
| 2028-04-01 | Review-Gate §29.6 | Aktivierung formales 2J-System-Review |
| offen | AVGO OpenInsider Manual-Check | Vor FLAG-Aktivierung (Watch aktiv, kein Termin — $123M/90d Post-Vesting-Verdacht) |

---

## System-Zustand

- **Scoring:** DEFCON v3.7 — Quality-Trap-Interaktionsterm (kein additiver Moat-Malus), OpM max 2Pt., Analyst-Bias-Kalibrierung, Fundamentals-Cap 50. Schema-Thresholds 18.04. auf SKILL.md aligned (≥80 D4 / 65-79 D3 / 50-64 D2 / <50 D1). **INSTRUKTIONEN §27 Scoring-Hygiene neu (18.04.):** Double-Counting-Vermeidung + Bonus-Cap-Check + Projection-Layer-Regel + Multi-Source-Drift-Check. System-Reife ~96%.
- **Live-Verify v3.7:** 5/11 bestätigt — V (18.04. Forward 72→63 nach Advisor-Review), **TMO (18.04. Forward 63→64, fcf_trend_neg struktureller Disclosure)**, ASML ±2, RMS ±2. Rest bei Earnings-Trigger.
- **Allokation:** 65/30/5 (ETF 617,50€ / Satelliten 285€ / Gold 47,50€), US-Cap 63% / Ist ~46%.
- **MCP-Status:** defeatbeta (WSL2 Ubuntu-24.04), Shibui, WebSearch — alle live. Non-US via yfinance.
- **Morning Briefing:** 🔴 **v3.0.3 Manual-Run FAIL → Rollback v2.1 DEPLOYED 20.04.2026 15:13 UTC.** Prod-Trigger `trig_01PyAVAxFpjbPkvXq7UrS2uG` läuft wieder v2.1 (reine Shibui+Yahoo-curl-Kurs-Extraktion, keine Tavily, keine News-Sektion). Grund: Manual-Run 20.04. Nacht-Spät zeigte **schwere Halluzination** — Agent interpretierte Shibui-EOD-Lag (17.04. Karfreitag-Wochenende) fälschlich als "stale data", improvisierte unautorisierten **Yahoo-Intraday-Fallback für US-Ticker** (nicht in Spec), halluzinierte Phantom-Preise (AVGO $317,79 vs. real ~$388 entspr. €337 Broker-Verify) → fabrizierter Markteinbruch -21,8% AVGO / -16% APH / -10% MSFT+TMO, hätte in falsche !Analysiere-Spirale geführt. Runtime 720s+ (>2× Alert-Schwelle). Yahoo-n.v.-deterministic für BRK.B/RMS/SU hat funktioniert; Material-Filter + Slot-Struktur + 8/8 Sektionen korrekt. **Gate A ausgesetzt** bis v3.0.4. Hotfix-Spec in nächster Session: §3a expliziter Guard "Shibui-EOD-Datum = autoritativ, Wochenend-/Feiertags-Lag = NORMAL, KEIN Yahoo-Fallback-Pfad für US-Ticker". v2.1 `03_Tools/morning-briefing-prompt-v2.md` baseline; v3.0.3 `03_Tools/morning-briefing-prompt-v3.md` bleibt als Lesson-Learned. Korrektheits-Prinzip > Laufzeit (memory feedback_correctness_over_runtime) bestätigt.
- **Backtest-Ready (Score-Archiv):** aktiv seit 17.04.2026 — **27 Score-Records** (24 Backfill + 3 Forward: V_vollanalyse 72 + V_rescoring 63 + **TMO_vollanalyse 64**) + 2 FLAG-Events. SKILL.md Schritt 7 Write-Pflicht. Score-Archiv-Review 2028-04-01, Score-Archiv-Interim-Gate **2026-10-17** (6-Monats-Sanity-Check auf score_history.jsonl — abgegrenzt vom R5-Interim-Gate 2027-10-19 weiter unten). **Drift-Migration 21.04.2026:** 12 von 27 Records hatten silent defcon_level-Drift seit 18.04.-Threshold-Migration (alle vor 18.04. mit alten 70/60/50-Bands archiviert; betraf u.a. V_vollanalyse 17.04. Score 72/D4→D3, BRK.B 75/D4→D3). Snap-to-Schema-Migration via `03_Tools/backtest-ready/migrate_defcon_drift.py` (idempotent, atomar) → 27/27 PASS gegen aktuelles Schema.
- **Forward-Verify-Pipeline via Skill** (seit 19.04.2026, v3.7.2): `backtest-ready-forward-verify` kapselt Draft → Freshness + Tripwire + §28.2 Δ-Gate + Dry-Run + Append + git add. Aktiviert aus dynastie-depot Schritt 7 (programmatisch, keine Trigger-Words). First-Run: TMO Q1 23.04.2026.
- **R5 Portfolio-Return-Persistenz aktiv** (seit 19.04.2026, Track 3 Phase 3): `05_Archiv/portfolio_returns.jsonl` + `benchmark-series.jsonl` Daily-Schema v1.0 (trading-date, cashflow-separated post-NAV, equal-weight 11-Satelliten). Erster Record 2026-04-17 (10.173,42 EUR notional, SPY 710,14). Append via `python 03_Tools/portfolio_risk.py --persist daily --cashflow <euro>`.
- **§30 Live-Monitoring aktiv** (seit 19.04.2026, Track 3 Phase 4): Monthly-Refresh pflicht für MSFT CapEx-FLAG (Flint-Vermaak Investment-Half-Life ~1M). TMO Schema-Watch (keine §30-Pflicht). INSTRUKTIONEN v1.11. Erster MSFT-Refresh ~19.05.2026 (Zwischen-Refresh vor Q3 29.04. nicht nötig, Earnings deckt ab).
- **Open Backlog (NEU 21.04.2026, aus System-Drift-Audit):**
  - **Daily-Persist seit 4 Tagen stale** — `portfolio_returns.jsonl` + `benchmark-series.jsonl` haben je nur 1 Record (17.04.). R5-Phase-3 ist seit 19.04. „aktiv" deklariert, aber Daily-Append ist Manual-Trigger via `python 03_Tools/portfolio_risk.py --persist daily --cashflow <eur>` und wurde seit Mo 20.04. nicht durchgeführt. Auflösung: Track 4 (ETF/Gold-Erweiterung) — blockiert ohnehin auf User-Input für ETF/Gold-Ticker; bei Auflösung gleichzeitig Cron-/Hook-Mechanismus für Auto-Persist einbauen.
  - **System-Audit-Tool fehlt** — heutige Drift-Migration deckte auf, dass „Drift-Check" nie kanonisch exhaustive war (Codex-Review 21.04.). Sub-Spec für `03_Tools/system_audit.py` mit Slash-Command `/SystemAudit` + STATE.md-Section „Last Audit: ..." steht in nächster Session an. Quality-Gates: JSONL-Schema + Markdown-Cross-Drift = Kern, Vault-Backlinks = optional/Timeout. Codex-Begründung gegen SessionStart-Hook: kollidiert mit CLAUDE.md SESSION-INITIALISIERUNG-Pflicht „nur STATE.md lesen".
- **Track 5 Pläne bereit** (seit 20.04.2026): `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks) + `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (15 Tasks), beide Codex-reviewed + fix-eingepflegt. **Execution PAUSIERT seit 20.04.2026 Abend** — User-Entscheidung zugunsten 6-Paper-Ingest (siehe nächster Punkt). Re-Validation der Pläne in Phase 3 nach Paper-Ingest-Komplettion.
- **6-Paper-Ingest Phase 1 KOMPLETT + Codex Gate 2 PASS** (20.04.2026 Abend-Spät): B19-B24 als Befunde in Wissenschaftliche-Fundierung-DEFCON (20 Quellen / 24 Befunde); neue Synthesis `Knowledge-Graph-Architektur-Roadmap` v0.1 mit 3 Qualitäts-Gates. **Vault-only**, DEFCON v3.7 unverändert, keine Score/FLAG/Sparraten-Änderungen. Detail in `SESSION-HANDOVER.md` + `log.md`.
- **6-Paper-Ingest-Projekt FORMAL ABGESCHLOSSEN** (20.04.2026 Nacht, Commits `89275e2` + `5f6dc62`): Phase 0 (Codex-Triage Rounds 1+2) + Phase 1a (B19/B20 Severity-🔴) + Phase 1b (B21-B24 Severity-🟡) + Phase 2 (System-Konsequenzen Hybrid A+B+C) + Phase 2.5 (Codex-Layer-Gate PASS) + Final-Discoverability (CLAUDE.md + insider-intelligence + backtest-ready-forward-verify). **Status-Matrix in `Wissenschaftliche-Fundierung-DEFCON.md` = kanonische SSoT**; aktiv in !Analysiere (§4 Router + §2 Pipeline + SKILL.md Schritt 2.5 + Output-Block), §28 (Migration), §29 (Retrospective ab 2028), §33 (Skill-Self-Audit). Bewusst passiv in !QuickCheck/!Rebalancing/Screener. **DEFCON v3.7 unverändert**, keine Score/FLAG/Sparraten-Änderung, config.yaml unberührt, §28.3 Nicht-Migration-Trigger bestätigt. Skill bleibt v3.7.2. **Smoke-Test AVGO PASS** (Befunde-Labels traceable, B6 Quality-Trap-Nicht-Aktivierung sauber ausgewiesen). Erster echter Live-Test: TMO Q1 23.04.2026.
- **Interim-Gate 2027-10-19:** 18-Mo-Dry-Run `risk-metrics-calculation` + Data-Quality-Check auf `portfolio_returns.jsonl` (R5 Phase 3, inkl. FX-Conversion-Nachrüstung für Mixed-Currency-Basket). Review-Aktivierung 2028-04-01.
- **KG-Roadmap v0.1 `draft-frozen`** (seit 20.04.2026 Nacht, Codex-Verdikt Option D): `07_Obsidian Vault/.../synthesis/Knowledge-Graph-Architektur-Roadmap.md` — Szenario 1 Form-4 XML bleibt, Szenario 3 Bayesian-RAG-Briefing verworfen, Szenario 2 10-K-KG `future-arch`. Keine v1.0-Ratifikation ohne Usage-Evidence. **Re-Review-Trigger:** konkreter Cross-Entity-/10-K-Narrativ-Bedarf ODER Score-Archiv-Interim-Gate **2026-10-17** (whichever first). Q1-Q3 offen, nicht release-blockierend. Track 5a/5b und v3.0.3-Prod-Deploy nicht blockiert.

---

## Navigation (on-demand)

| Wenn du brauchst… | Lies… |
|-------------------|-------|
| Aktuellen Stand, Trigger, Sparraten | **Diese Datei** |
| Letzte Session-Details, v3.7 Deployment | `SESSION-HANDOVER.md` |
| Scoring-Regeln, Sparplan-Formel, Workflows | `INSTRUKTIONEN.md` |
| Strategie, Allokation, Satelliten-Struktur | `KONTEXT.md` |
| Scoring-Lektionen, Positions-Entscheidungen, Audit-Log | `CORE-MEMORY.md` (Sections 2–10) |
| Meilenstein-Chronik vor 15.04.2026 | `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md` |
| Score-Detail pro Ticker | `Faktortabelle.md` |

**Sync-Pflicht bei Score/FLAG/Sparraten-Änderung:** log.md + CORE-MEMORY.md + Faktortabelle.md + **STATE.md** + **score_history.jsonl** (+ ggf. **flag_events.jsonl**) (§18 INSTRUKTIONEN — alle sechs, immer).
**Briefing-Sync:** `!SyncBriefing` vor Session-Ende, wenn 00_Core/ geändert wurde (§25).

---
*🦅 STATE.md v1.0 | Dynasty-Depot | Entry-Point statt 1.200-Zeilen-Auto-Read*
