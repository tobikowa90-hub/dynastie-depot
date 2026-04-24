# 🎯 STATE.md — Dynasty-Depot Live-Status
**Single Entry Point für Session-Start** | Stand: 24.04.2026 Session-2-Ende (**CLAUDE.md Routing-Refactor Tier 1 VOLLSTÄNDIG CLOSED** — Session 1 (16 Commits) + Session 2 Vault-Update `f9d65d1` + CodeRabbit-Pass `4cf0ea9` (3 Fixes + 5 begründete Declines). CR-CLI-Command-Bug im Handover-Block als Zusatz-Fix behoben. **Session 3 offen:** Brainstorm 00_Core Perfect-Organization (STATE-Split Variante B + CORE-MEMORY Restrukturierung + Global-Linking). **Portfolio-State unverändert** seit 23.04. · vorher: 23.04.2026 Nachmittag (**Phase G TMO Q1 FY26 Vollanalyse DONE** — BEAT + Guidance-Raise. Adj EPS $5,44 / Rev $11,01B / GAAP EPS $4,43 (+11%) / FCF $825M (+121% YoY) / OCF $1.192M (+65%) / ΔWC $-1.112M vs $-1.425M. Guidance hochgesetzt: Rev $47,3-48,1B, Adj EPS $24,64-25,12, FCF $6,9-7,4B, Organic 3-4% bestätigt. Clario $8,87B closed. **`fcf_trend_neg` Resolve-Gate CLEAR** (Schema-Watch deaktiviert). Score **64→67**, **D2→D3**, Sparrate **17,81€→33,53€**, Nenner **8,0→8,5** (volle Rate 35,63€→33,53€, V D2-Rate 17,81€→16,76€). Sync-Welle 6 Files Old-Pipeline-Format committed (`620702a`) · **Retro-Audit Option B PASS (23.04. spät)** — `backtest-ready-forward-verify` P1-P4 Post-hoc-Validation sauber, kein Re-Append · XLSX-Tools (Rebalancing_Tool + Satelliten_Monitor) unberührt bis post-Retro-Migration (Vermeidung Doppel-Edit-Churn). **Fr 24.04. Konsolidierungstag-Agenda erweitert um Block 0 Teil 2: Track 5a/5b-Entscheidungspunkt**) · vorher: Phase G Pre-TMO-Briefing bereit via `02_Analysen/TMO_pre-earnings_2026-04-23.md` (earnings-preview-Skill 22.04.) · vorher: **Phase E 19/19 DONE ✅** — Tasks 15-19 committed + Fix-Welle E + CR-Re-Run gegen `e3ba381` = **1 OOS-Nitpick** (`PORTFOLIO-RISK-2026-04-17.md:39` DE/EN-Mix „Risk-Treiber", Auto-Output nicht Phase-E-Scope, dokumentiert + closed). Codex-Pass = **RECONCILED_WITH_FOLLOWUPS** (3 Codex-Follow-ups deferred: Check-3+existence-Cleanup → §27.5-Guard auf `--core` hochziehen, Check-10 Regex-Scope). Acceptance-Matrix 9/11 ✅ + 2 dokumentierte WARNs (Item 2 `--core` rc=1 Tool-Bugs, Item 9 Notation-Drift). **Phase F (Provenance-Plan) deferred per Pfad-2-Entscheidung** — TMO Q1 23.04. 14:30 CEST läuft mit Old-Pipeline im Minimal-Modus (Weekly-Limit 93%, Reset Do 22:00 CEST), Retro-Migration TMO-Record post-Reset. Phase G (TMO Q1) next. Konsolidierungstag Fr 24.04. geplant (Check-3-Fix + existence-Cleanup + v3.0.4-Briefing-Hotfix + Tavily-Key-Rotation). v3.0.4 Briefing-Hotfix weiter pending) | System: DEFCON v3.7 (unverändert)

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
| AVGO | 84 | 🟢 4 | 33,53€ | ⚠️ Insider-Review (OpenInsider!) | Q3 FY26 |
| BRK.B | 75 | 🟡 3 | 33,53€ | ✅ Insurance Exception | Q-Earnings Mai |
| VEEV | 74 | 🟡 3 | 33,53€ | ✅ | Earnings-Trigger |
| SU | 69 | 🟡 3 | 33,53€ | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | 33,53€ | ✅ Screener-Exception | Q1 FY27 ~Dez |
| RMS | 68 | 🟡 3 | 33,53€ | ✅ Screener-Exception | H1 Juli/Aug |
| ASML | 68 | 🟡 3 | 33,53€ | ✅ | Q2 2026 (Q1 17.04. Vollanalyse ✅) |
| **TMO** | **67** | **🟡 3** | **33,53€** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR 23.04.) | **Q2 FY26 ~Ende Juli — Organic-Akzeleration + Clario-Integration-Check** |
| V | 63 | 🟠 2 | **16,76€** | ✅ | **28.04. Q2 FY26 — D2-Entscheidung** |
| APH | 63 | 🟠 2 | **0€** | 🔴 Score-basiert | 23.07. Q2 |
| MSFT | 59 | 🟠 2 | **0€** | 🔴 CapEx/OCF 83.6% | **29.04. Q3 FY26 — FLAG-Review** |

**Sparraten-Nenner:** 8×1,0 + 1×0,5 + 2×0 = **8,5** → 33,53€ volle / 16,76€ D2 / 0€ FLAG. **Summe 285€** ✓ (8×33,53 + 16,76 + 2×0 = 268,24 + 16,76 = 285,00)

> **23.04.2026 Änderung:** TMO Q1 FY26 Forward-Vollanalyse (67, D3) — Beat + Guidance-Raise, `fcf_trend_neg` Resolve-Gate CLEAR. D2→D3, Sparrate 17,81€→33,53€. Kaskade: Nenner 8,0→8,5, volle Rate 35,63€→33,53€ (7 andere D3/D4-Satelliten −2,10€), V D2-Rate 17,81€→16,76€. **18.04.2026 Änderung:** V-Forward-Vollanalyse (63, D2) ersetzt 17.04.-Backfill-Projektion (86, D4) — siehe CORE-MEMORY §11. Gleichzeitig Schema-SKILL-Threshold-Drift gefixt: 5 Tickers (BRK.B/VEEV/SU/COST/RMS) D4→D3 (Label-Fix, Sparrate unverändert), APH D3→D2 (FLAG überschreibt Sparrate weiterhin). Nenner schrumpft von 8.5 auf 8.0, volle Rate steigt 33,53€ → 35,63€.

---

## Aktive Watches

- **V D2-Kritik (NEU 18.04.):** 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA, Crowd-Sell-Ratio 0%. Q2 FY26 am 28.04. entscheidet: Beat + Guidance-Bestätigung → Technicals-Reversal möglich (zurück Richtung D3). Miss → weiterer Downshift Richtung D1.
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- **AVGO Insider $123M (90d)** — wahrscheinlich Post-Vesting (Broadcom-Muster Tan/Brazeal/Spears). Vor FLAG-Aktivierung OpenInsider manuell prüfen.
- ~~**TMO D2-Kritik + FLAG-Resolve-Gate (NEU 18.04.)**~~ **Resolved 23.04.2026:** Q1 FY26 Beat + Guidance-Raise, FCF $825M +121% YoY, WC-Unwind-These bestätigt (ΔWC -1.112M vs -1.425M = +$313M besser), Management FY26-FCF-Guide $6,9-7,4B. `fcf_trend_neg` Resolve-Gate CLEAR, Schema-Watch deaktiviert. Score 64→67, D2→D3, Sparrate 17,81€→33,53€. Neue Watch: **Organic-Akzeleration Q1 +1% → H2 3-4%-Guide** + **Clario-Integration-Execution** (Q2 Ende Juli Re-Check). ZTS-Ersatz-Vorbereitung pausiert.
- **MSFT FLAG-Auflösungs-Pfad:** Q3 29.04. — bereinigtes CapEx/OCF <60% (Finance Lease $19.5B raus) = Auflösung. Darüber = Veto-Verschärfung.

---

## Nächste kritische Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| ~~23.04.~~ | ~~TMO~~ | — | **DONE** Beat + Guidance-Raise, D2→D3, fcf_trend_neg CLEAR. Retro-Audit Option B PASS (23.04. spät — P1-P4 Skill-Validation gegen `620702a`, Real-Append N/A). Nächster: Q2 ~Ende Juli. |
| **28.04.** | **V** | **B** | **Q2 FY26 — D2-Entscheidung (Technicals-Reversal?)** |
| 28.04. | SNPS/SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — FLAG-Review** |
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |

---

## 🗺 Aktive Pipeline (SSoT)

> **Zweck:** Single-Source-of-Truth für alle offenen Pläne, Gates und Termine. Ersetzt die bisherige Fragmentierung über STATE.md + SESSION-HANDOVER.md + Plan-Files + Memory (jedes Mal aus 4 Quellen rekonstruiert — exakter Anti-Pattern der 21.04.-Drift-Lesson).
> **Pflege-Pflicht:** Update bei (a) jedem neuen Plan-Commit in `docs/superpowers/plans/`, (b) jedem Gate-Passage, (c) jeder Status-Transition (ready→in-progress→done, deferred→active). Parallel zur §18-Sync-Welle (aber eigener Trigger — Plan-Commit ist nicht automatisch Score-Change).

### 🔴 Unmittelbar / Primär-Track

1. ~~**Systemhygiene-Welle Phase A-E (SSoT-Aufbau + Audit-Tool-Bau)**~~ **DONE 2026-04-22 Spät-Nacht.** Phase A+B+C+D ✅ committed. Phase E 19/19: Tasks 1-19 substantive + Fix-Welle E `e3ba381` + CR-Re-Run gegen `e3ba381` = 1 OOS-Nitpick (DE/EN-Mix auf 17.04. Auto-Output). Codex RECONCILED_WITH_FOLLOWUPS. **3 Codex-Follow-ups** (bleiben als Backlog-Tasks — werden am Konsolidierungstag Fr 24.04. zusammen mit v3.0.4 + Tavily-Key gelöst): (a) Check-3 future-date-exclude + existence-Cleanup (~54 CLAUDE.md-Pfad-Refs) → §27.5-Guard auf `--core` hochziehen; (b) Check-10 `status_matrix` Regex-Scope auf `### Matrix`-Subsection einengen; (c) §27.5-Kommentar-Update nach (a). **CodeRabbit-OOS** dokumentiert: `flag_events.jsonl:2` null-metrik.wert (pre-existing), `PORTFOLIO-RISK-2026-04-17.md:39` DE/EN-Mix (Auto-Output).
2. **Morning Briefing v3.0.4 Hotfix** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks, ~90 Min). Prod läuft v2.1 (Rollback nach Halluzinations-Incident 20.04.). Hotfix ergänzt §3a Anti-Fallback-Guard + neuer Test T5 Adversarial-Stale-Shibui. Gate A erst nach v3.0.4-PASS. **Gate für Dashboard v2 Tavily-Integration + Track 5a/5b.**
3. **Score-Append Provenance-Gate** — Plan v2 `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (7 Tasks, 40 Steps) + Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`. **Pfad-2-Entscheidung 22.04. Spät-Nacht:** TMO Q1 23.04. läuft mit **Old-Pipeline** (Weekly-Limit 93%, Reset Do 22:00 CEST — kein Raum für 7-Tasks/40-Steps-Execution im Minimal-Modus). TMO-Record im Old-Pipeline-Format archiviert, **Retro-Migration post-Reset** (Do Abend 22:00+ ODER Fr 24.04. Konsolidierungstag). „Critical vor TMO Q1"-Formulierung war Self-Imposed-Gate, kein echter Blocker — Provenance-Gate-Nutzen ist in zukünftigen Appends, nicht retrospektiv.
4. ~~System-Audit-Tool~~ **DONE 2026-04-22** — `03_Tools/system_audit.py` v1.0 + `/SystemAudit` deployed. Baseline `--minimal-baseline` 3/3 PASS (Check-1 jsonl_schema + Check-6 pipeline_ssot + Check-7 log_lag). `--core` 4/8 PASS mit 2 known Tool-Bugs (Check-3 future-date → Follow-up-Task, Check-5 existence → Post-Task-17-Follow-up-Welle). Live-Audit 22.04. bestätigt: 4/8 PASS, 2 FAIL (known), 2 WARN (known). ~~**2 Audit-Tool-Verbesserungen (Opus-Advisory 22.04.) → Konsolidierungstag Fr 24.04. Block 1:** (a) Check-5 Batch-Output gruppiert nach Sektion; (b) Check-4 WARN-Semantik `⚠️ Informativ` vs. `🔴 Funktional` trennen.~~ **→ DONE 23.04.2026 Abend** via Patch in `03_Tools/system_audit/report.py` — pro-failure severity-icons (🔴/⚠️/ℹ️) + gruppiertes Batch-Output (Sektion = location-Prefix bis erster Colon, mit Singleton-Only-Fallback auf Flat). Neuer Regression-Test `test_report_human_severity_icons_and_grouping`, 59/59 Smoke-Tests PASS, `--minimal-baseline` 3/3 PASS.
5. ~~**CLAUDE.md Routing-Refactor Tier 1**~~ **DONE 2026-04-24 (alle 3 Sessions geschlossen).** Plan `docs/superpowers/plans/2026-04-24-claude-md-routing-refactor.md` v0.2.1 vollständig ausgeführt (8 Tasks + Section-A-Follow-up). CLAUDE.md 97→71 Zeilen (Option-B-Compression, Spec-Ziel ~70 erreicht), 2 neue SSoT-Files: `00_Core/APPLIED-LEARNING.md` (14/20 Bullets, v2.5) + `00_Core/TOKEN-RULES.md` (Accessibility-Modell). Neue `## Routing-Table` (9 Trigger + 3 Edge-Cases, Edge-Case Tippfehler um Case-Drift + Sprach-Varianten erweitert via CR-Fix) ersetzt On-Demand-Lektüre-Liste (Entscheidung A). `## Pointer (Ausgelagertes)` mit 4 Zeilen inkl. Meilensteine-Archiv (User-Entscheidung gegen Info-Verlust, AC #8 dokumentiert abweichend). Applied-Learning v2.5: +2 Bullets (Plan-Self-Review-Blindspot, Migrations-Invariante-vs-Meta-Logging), Historie als Tabelle strukturiert (CR-Fix #5). 11/11 AC PASS (2 dokumentierte Abweichungen: AC #8, AC #9b Self-Reference). **Session 1:** 16 Commits (`9ae0dcc` Baseline) inkl. Codex-Reconciliation `1e79386` + Option-B-Compression `3bd8632`. **Session 2 (heute):** Vault-Update `f9d65d1` (CLAUDE-md-Konstitution 7-Section-Struktur + Änderungsprotokoll 24.04.) + CodeRabbit-Pass `4cf0ea9` (8 Findings → 3 Fixes / 5 begründete Declines, CR-Command-Bug-Fix in Handover-Block als Zusatz). **Tier 2 (STATE-Split Variante B Hub) + Tier 2b (CORE-MEMORY Restrukturierung) deferred → Session 3 Brainstorm-Kandidat „00_Core Perfect-Organization"** (siehe #12).

### 🟠 Portfolio — Kritische Triggers 10 Tage

- ~~**23.04. TMO Q1 14:30 CEST**~~ **DONE 23.04.2026 Nachmittag.** Beat + Guidance-Raise, Score 64→67, D2→D3, fcf_trend_neg Resolve-Gate CLEAR. Sync-Welle 6 Files Old-Pipeline-Format committed (`620702a`). **Retro-Audit Option B DONE (23.04. spät):** `backtest-ready-forward-verify`-Skill Post-hoc-Validation (P1 parse PASS · P2a freshness INFO · P2b STATE-Tripwire PASS · P3 N/A · P4 Dry-Run PASS gegen synth. Archiv · P4-bis Duplicate-Guard PASS). Kein Re-Append (Informationsverlust-Aversion), erster echter Skill-Forward-Run bleibt V 28.04. **Folge:** ~~XLSX-Tools einmalig aktualisieren~~ **DONE 23.04.** via `5ccfdd1` (Raten 33,53€/16,76€/0€ in Rebalancing_Tool + Satelliten_Monitor) + `a413c32` (Satelliten-Monitor R-Spalte Alter-Formel statt statischer 0).
- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal?).
- **29.04. MSFT Q3 FY26** — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung).

### 🟡 Bereit, wartet auf Gate A (~24.04. frühestens nach v3.0.4-Deploy)

6. **Track 5a SEC EDGAR Skill-Promotion** — Plan `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks). Re-Validation-Check nach 6-Paper-Ingest B21-B24 möglicherweise nötig. **Entscheidung 5a/5b kann Dashboard v2 beeinflussen** (EDGAR-Daten in Faktortabelle-Parser integrierbar, FRED-Macro-Headline als Tavily-Alternative).
7. **Track 5b FRED Macro-Regime-Filter** — Plan `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (15 Tasks). User-Aktion vor Start: FRED-API-Key registrieren. B19 (LLM-Regime-Shift-Bias) stärkt wissenschaftliche Begründung.
7a. **Track 5a/5b Entscheidungspunkt (NEU 23.04.)** — am Konsolidierungstag Fr 24.04. **Block 0 Teil 2 (15 Min)** vor Dashboard v2: ja/nein für 5a, ja/nein für 5b. Grund: Dashboard-Scope (Block 3) hängt von Feed-Entscheidung ab — EDGAR/FRED-Daten im Faktortabelle-Parser wären nachträgliche Re-Integration. User-Pre-Aktion: FRED-API-Key registrieren (falls 5b = ja vorgesehen). Gate: v3.0.4 muss Block 2 PASS haben.
7b. **Dashboard v2** (`dynasty-depot-dashboard` Artifact) — **wartet auf Gate A (v3.0.4 + Tavily-Key-Rotation) + 5a/5b-Entscheidung (Block 0 Teil 2)**. Architektur entschieden 22.04. (Opus+Sonnet Advisory): Faktortabelle-Parser + Shibui-primär + Tavily-scoped + FLAG-Lösungs-Pfade. Scheduled Task `dynasty-dashboard-refresh` läuft bereits (07:09 Mo-Fr). **Ausführung: Konsolidierungstag Fr 24.04., Block 3 (nach v3.0.4 + Key-Rotation + 5a/5b).** **Scope-Entscheidung 22.04. (final):** Rebalancing_Tool / Satelliten_Monitor / Watchlist_Ersatzbank XLSX bleiben externe Arbeitsblätter — kein XLSX-Parsing im Dashboard (zu fehleranfällig). Dashboard-Fokus = aktuelle 11 Satelliten-Positionen.

### 🔵 Deferred / Explizit zurückgestellt

8. **v3.1 Cache-Refactor** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.1-cache-refactor.md`. Trigger: „262s im Alltag stört" ODER „>400s-Alert wiederholt".
9. **Track 4 ETF+Gold-Erweiterung** — Blockiert auf User-Input (ETF-Ticker IWDA.AS/SWDA.L/EUNL.DE? Gold-Ticker SGLD.DE/4GLD.DE/GC=F?). Cron-/Hook-Mechanismus für Auto-Persist kann jetzt auf `portfolio_risk.py --persist daily --as-of $(date -I)` aufsetzen (Backfill-Flag seit 23.04. verfügbar).
10. **KG-Roadmap v0.1 `draft-frozen`** (`07_Obsidian Vault/.../synthesis/Knowledge-Graph-Architektur-Roadmap.md`). Re-Review-Trigger: Cross-Entity-Bedarf ODER Score-Archiv-Interim-Gate 2026-10-17.
11. **Atomic-Write-Hardening `portfolio_risk.py`** (NEU 23.04.2026, aus CodeRabbit-Bug-Hunt) — aktueller Patch nutzt `fsync` + try/truncate-Rollback (deckt Software-Exceptions). CR forderte temp+`os.replace`+dir-fsync für Hard-Crash-Atomarität. **B-Entscheidung (23.04. User):** Solo-Betrieb 1×/Tag, Hard-Crash-Window µs — nicht gehärtet. **Follow-up-Tasks:** (a) Recovery-Script `03_Tools/repair_daily_persist.py` das Split-State `portfolio_returns.jsonl` vs `benchmark-series.jsonl` erkennt + heilt; (b) Atomic-Write-Härtung erst falls Incident oder Track-4-Auto-Hook konkret wird.
12. **00_Core Perfect-Organization — Brainstorm-Kandidat (NEU 24.04.2026, User-Vision):** Ziel = perfekt organisierter + global verknüpfter `00_Core/`-Ordner. Umfang-Kandidaten: (a) **Tier 2b CORE-MEMORY Restrukturierung** — kalendarische Riesen-Liste (~45 §1-Einträge) → Subkategorien (nach Topic / System-Element / Zeit?) + Verknüpfung zu adressierten System-Elementen (Skills/Tools/Files). Single-File vs Split offen. Migrations-Strategie offen. (b) **Tier 2 STATE-Split Variante B Hub** (bereits in #5 Handover-Notiz deferred) — STATE.md ~10-Z-Hub + `00_Core/PORTFOLIO.md`/`PIPELINE.md`/`SYSTEM.md`. (c) **Global-Linking-Strategie** — Back-Refs zwischen 00_Core-Files systematisieren (aktuell nur per Prose-Mention). (d) **Vault-Integration** — sollen Wiki-Concepts strukturell auf neue 00_Core-Struktur Bezug nehmen? (e) **insider-intelligence/SKILL.md §215 Snapshot-First-Block-Review** (aus 24.04. Session 1 Cross-Ref-Pass): prüfen ob einzigartig oder Duplikat von TOKEN-RULES.md Snapshot-First; falls Duplikat → löschen + Cross-Ref; falls einzigartig → in TOKEN-RULES.md Skill-spezifische Ergänzungen mit §-Referenz aufnehmen. **Trigger:** Eigene Brainstorm-Session, nicht in Tier-1-Closeout mitziehen. **Gate:** Session 2 (CodeRabbit + Vault) muss erst schließen. Handover-Notiz `SESSION-HANDOVER.md` verweist hierauf.

### ⏰ Long-Term-Gates (chronologisch)

| Datum | Gate | Owner-Aktion |
|-------|------|--------------|
| ~28.04.2026 | Tavily Dev-Key Rotation | User: Key `tvly-dev-4PYXp...` in Dashboard rotieren (7-Tage-Uhr ab v3.0.4-Prod-Deploy) |
| 2026-07-19 | Track 5a 90-Tage-Audit | EDGAR-Skill Performance-Review (falls promoted) |
| 2026-10-17 | Score-Archiv-Interim-Gate | 6-Monats-Sanity-Check `score_history.jsonl` (Forward-Window + Duplicate-Guard) |
| 2027-10-19 | R5 Interim-Gate | 18-Mo-Dry-Run `risk-metrics-calculation` + Data-Quality `portfolio_returns.jsonl` (inkl. FX-Conversion-Check) |
| 2027-10-19 | `float → Decimal` Migration | `PortfolioReturnRecord` + `Position` + `BenchmarkReturnRecord` auf `Decimal` umstellen — R5-Interim-Gate braucht exakte Arithmetik für Sharpe/Sortino/Beta (Backlog-Punkt 1 aus User-Diskussion 21.04.2026; eigener Migration-Plan ~1 Session, blockt Task 14-19 nicht) |
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
  - ~~**Daily-Persist seit 4 Tagen stale**~~ **→ resolved 23.04.2026 Abend** — `portfolio_risk.py` `--as-of`-Backfill-Flag implementiert (Codex-Audit Option A gehärtet: Gap-Enforcement via yfinance-sessions + strict-chronology-Validator + Atomic-Write mit Size-Rollback), 4 Records 2026-04-20 bis 2026-04-23 chronologisch appendet. Archive 5/5 Records, NAV-Chain mathematisch validiert. CodeRabbit-Bug-Hunt: 1 in-scope Major (Hard-Crash-Atomarität) — als Follow-up Deferred #11 dokumentiert (Solo-Betrieb 1×/Tag → B-Entscheidung). Langfrist: Track 4 Auto-Hook (Cron/Hook nutzt jetzt vorhandenes `--as-of $(date -I)`).
  - ~~**Check-6 False Positive**~~ **→ resolved 23.04.2026 Spät.** `skill_version.py` akzeptiert jetzt bare-name ZIPs (`<skill>.zip`) + Orphan-Detection erweitert auf bare-name ZIPs inkl. `_extern/`-Awareness. Codex-Pre-Commit-Review NO-GO (Spec-Drift + Orphan-False-Negative) beide adressiert: Spec-Drift via Plan-Header-Notice (Memory `feedback_spec_section_drift.md`), Orphan-False-Negative via Code-Fix. 3 neue Smoke-Tests. Audit deckt jetzt 4 echte Orphan-ZIPs auf → neuer Backlog-Item.
  - ~~**06_Skills-Pakete orphan ZIPs (NEU 23.04.)**~~ **→ resolved 23.04.2026 Abend.** Alle 4 Orphan-ZIPs nach `05_Archiv/skills-legacy/` verschoben (Informationsverlust-Aversion statt delete). Triage: `fmp-api` + `qualitative-valuation` legacy per PIPELINE.md-Rejection; `defeatbeta-analyst` + `sec-edgar-skill` Publisher-Prefix-Duplikate zu bereits materialisierten `_extern/`-Skills. README mit Rationale + Recovery-Anleitung in `05_Archiv/skills-legacy/README.md`. Check-6 jetzt ✅ PASS 2/2 (vorher ⚠️ WARN 2/2 mit 4 Orphans).
  - ~~**Check-3 future-date-Bug**~~ **→ resolved 23.04.2026 Spät.** `markdown_header.py` filtert Datums > today vor `max()`-Newest-Event-Berechnung. STATE.md + Faktortabelle.md nicht mehr False-FAIL durch Long-Term-Gates / zukünftige Earnings-Dates. CORE-MEMORY.md-Lag bleibt als legitime WARN (Content-Sync-Todo). Plan-Header-Notice + 1 Smoke-Test mit frozen today.
  - **Check-3 Test time-coupling (NEU 23.04., nicht-blocking):** `test_markdown_header_*_fixture`-Tests rufen `run()` ohne `today`-Override → real `date.today()`. Pre-existing Coupling. Hardening Fr 24.04. mit `today=_dt.date(2026,4,21)`-Freeze.
  - ~~**System-Audit-Tool fehlt**~~ **→ deployed 22.04.2026** — `03_Tools/system_audit.py` v1.0 + `/SystemAudit`-Slash-Command + `--minimal-baseline`-Regression-Guard in INSTRUKTIONEN §27.5. Spec v0.2 + Plan `2026-04-21-system-audit-tool.md` archiviert. Follow-up-Tasks in Task-Backlog: #2 Check-3 future-date-exclude, #4 vault_backlinks Robustness-Pass (Important #4-7), post-Task-17 existence-Cleanup-Welle (~54 CLAUDE.md-Pfadreferenzen).
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
<!-- system-audit:last-audit:start -->
---

## 🔍 Last Audit

**Timestamp (UTC):** 2026-04-24T17:18:34Z
**Result:** 3/3 PASS
**Run:** `python 03_Tools/system_audit.py --minimal-baseline`
**Full-Report:** stdout (kein Archiv-File)

<!-- system-audit:last-audit:end -->

*🦅 STATE.md v1.0 | Dynasty-Depot | Entry-Point statt 1.200-Zeilen-Auto-Read*
