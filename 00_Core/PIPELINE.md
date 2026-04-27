# PIPELINE.md — Pipeline-SSoT + Long-Term-Gates

## Verweise
- [INSTRUKTIONEN.md §18](INSTRUKTIONEN.md#18-sync-pflicht-logmd--core-memorymd--faktortabellemd--statemd--score_historyjsonl--flag_eventsjsonl) — Pipeline-Item-Sync-Pflicht (Event-Typ "Pipeline-Item")
- [PORTFOLIO.md](PORTFOLIO.md) — Portfolio-nahe Gates synchron
- [SYSTEM.md](SYSTEM.md) — Infra/Audit-nahe Pipeline-Items
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Abschluss-Pflicht bei Pipeline-Status-Transition
- [CORE-MEMORY.md §13](CORE-MEMORY.md#13-system-lifecycle-history) — Lifecycle-Einträge bei Done/Deferred (kanonische Archivquelle für entfernte DONE-Items; Numbering-Gaps in Aktiv-Liste sind Pointer dorthin + git log)

---

## 🗺 Aktive Pipeline (SSoT)

> **Zweck:** Single-Source-of-Truth für alle offenen Pläne, Gates und Termine. Ersetzt die bisherige Fragmentierung über STATE.md + SESSION-HANDOVER.md + Plan-Files + Memory (jedes Mal aus 4 Quellen rekonstruiert — exakter Anti-Pattern der 21.04.-Drift-Lesson).
> **Pflege-Pflicht:** Update bei (a) jedem neuen Plan-Commit in `docs/superpowers/plans/`, (b) jedem Gate-Passage, (c) jeder Status-Transition (ready→in-progress→done, deferred→active). Parallel zur §18-Sync-Welle (aber eigener Trigger — Plan-Commit ist nicht automatisch Score-Change).
> **Numbering-Convention:** Items werden bei DONE-Entfernung **nicht renumbered**. Gaps signalisieren entfernte Archive-Kandidaten (siehe CORE-MEMORY §13 + git log). Stable-Numbering hält Commit-Message-Referenzen wie „PIPELINE #13" historisch lesbar.

### 🔴 Unmittelbar / Primär-Track

2. **Morning Briefing v3.0.6 — Phase 4-6 Re-Test + Prod-Deploy (NEU 27.04.2026)** — Phase 3.5 Probe-E2E-Verify PASS (B1-B9 9/9, 6 hart) am 27.04. ~20:50 MESZ via Manual-Run #2 nach Tavily-Connector-UI-Reattach (UUID `0da14a12-...`). v3.0.6-Body deployed 17:38:50Z (Commit `1a3cf51`). **Phase 4-6 freigegeben, blockiert durch Earnings:** T6 voll-Test (Calendar-Mismatch §6F-4) + T1/T3/T4-Retest gegen v3.0.6 + Prod-Deploy v3.0.6 auf `trig_01PyAVAxFpjbPkvXq7UrS2uG`. **Reihenfolge:** nach V Q2 FY26 (28.04. ~22:00 MESZ) + MSFT Q3 FY26 (29.04. ~22:30 MESZ) Earnings, voraussichtlich Mi 30.04. oder Konsolidierungstag. Plan-Files: `docs/superpowers/plans/2026-04-27-briefing-v3.0.5-implementation.md` (8 Phasen, Phase 4-6 queued) + `docs/superpowers/plans/2026-04-27-briefing-v3.0.6-hotfix.md` (Tasks 17-18 covered, Plan-File nicht committed). Prod-Trigger läuft weiter v2.1 bis Deploy. Gate A bleibt ausgesetzt bis Prod-Deploy v3.0.6. **Historische Phasen:** v3.0.3 Halluzinations-Incident 20.04. → Rollback v2.1 → v3.0.4 Anti-Fallback-Guards (commit `7514ba7` Foundation A1-A14) → v3.0.5 Provenance-Architecture → v3.0.6 Hotfix (Anti-Fabrikations-Cracks geschlossen: Tools-Verbot, Domain-Subset-Retry-Verbot, Score-Datum-Substituts-Verbot, §6F-4 Calendar-Mismatch, Tool-Provenance-Check). **Gate für Dashboard v2 Tavily-Integration + Track 5a/5b.**
3. **Score-Append Provenance-Gate** — Plan v2 `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (7 Tasks, 40 Steps) + Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`. **Pfad-2-Entscheidung 22.04. Spät-Nacht:** TMO Q1 23.04. läuft mit **Old-Pipeline** (Weekly-Limit 93%, Reset Do 22:00 CEST — kein Raum für 7-Tasks/40-Steps-Execution im Minimal-Modus). TMO-Record im Old-Pipeline-Format archiviert, **Retro-Migration post-Reset** (Do Abend 22:00+ ODER Fr 24.04. Konsolidierungstag). „Critical vor TMO Q1"-Formulierung war Self-Imposed-Gate, kein echter Blocker — Provenance-Gate-Nutzen ist in zukünftigen Appends, nicht retrospektiv.

### 🟠 Portfolio — Kritische Triggers 10 Tage

- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal?).
- **29.04. MSFT Q3 FY26** — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung).

### 🟡 Bereit, wartet auf Earnings-Window-Schluss (post-29.04.)

6. **Track 5a SEC EDGAR Skill-Promotion** — Plan `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks, ~2-3h). **Decision A1-Final 27.04.2026** (Decision-Spec `docs/superpowers/specs/2026-04-27-track5a-5b-decision.md` nach Codex-Sparring): freigegeben für Execution post-V/MSFT-Earnings (30.04.+). Skill-Move `_extern/sec-edgar-skill/` → `01_Skills/sec-edgar-skill/`, EdgarTools-Install + `set_identity()`. Eskalations-Fallback (NICHT auto in `!Analysiere`).
7b. **Dashboard v2** (`dynasty-depot-dashboard` Artifact) — **entkoppelt von 5a/5b** (Decision-Spec 27.04.). Architektur (Opus+Sonnet Advisory 22.04.): Faktortabelle-Parser + Shibui-primär + Tavily-scoped + FLAG-Lösungs-Pfade. Scheduled Task `dynasty-dashboard-refresh` läuft bereits (07:09 Mo-Fr). XLSX-Tools bleiben externe Arbeitsblätter (kein XLSX-Parsing im Dashboard). Dashboard-Fokus = aktuelle 11 Satelliten-Positionen. Sequenzierung: nach 5a-Skill-Promotion.

### 🔵 Deferred / Explizit zurückgestellt

8. **v3.1 Cache-Refactor** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.1-cache-refactor.md`. Trigger: „262s im Alltag stört" ODER „>400s-Alert wiederholt".
9. **Track 4 ETF+Gold-Erweiterung** — Blockiert auf User-Input (ETF-Ticker IWDA.AS/SWDA.L/EUNL.DE? Gold-Ticker SGLD.DE/4GLD.DE/GC=F?). Cron-/Hook-Mechanismus für Auto-Persist kann jetzt auf `portfolio_risk.py --persist daily --as-of $(date -I)` aufsetzen (Backfill-Flag seit 23.04. verfügbar).
10. **KG-Roadmap v0.1 `draft-frozen`** (`07_Obsidian Vault/.../synthesis/Knowledge-Graph-Architektur-Roadmap.md`). Re-Review-Trigger: Cross-Entity-Bedarf ODER Score-Archiv-Interim-Gate 2026-10-17.
11. ❄️ **Atomic-Write-Hardening `03_Tools/portfolio_risk.py`** (Frozen — 23.04.2026 B-Entscheidung) — aktueller Patch (`fsync` + try/truncate-Rollback) deckt Software-Exceptions. CR-Vorschlag temp+`os.replace`+dir-fsync nicht umgesetzt: Solo-Betrieb 1×/Tag, Hard-Crash-Window µs. **Re-Activation-Trigger:** Incident ODER Track-4-Auto-Hook konkret. Bei Re-Activation: (a) Recovery-Script repair_daily_persist.py für Split-State + (b) Hardening.
7. ❄️ **Track 5b FRED Macro-Regime-Filter** (Deferred — 27.04.2026 A1-Final-Entscheidung) — Plan `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (15 Tasks) bleibt unverändert archiviert. Decision-Spec `docs/superpowers/specs/2026-04-27-track5a-5b-decision.md` dokumentiert Codex-Sparring-Befund: bei aktuellem Sparraten-Volumen 285€/Monat realistisch <20bps/Jahr Alpha → Effort/Reward-Verhältnis nicht gegeben. **Re-Activation-Trigger (mind. einer):** (a) Sparrate >1.000€/Monat ODER (b) Depotwert >50.000€ ODER (c) konkret aufgetretener Regime-Aware-Schmerz (Drawdown-Ex-post-Reduktion oder Bull-Phase-Ex-post-Erhöhung sichtbar besser). Bei Re-Activation: Plan-Update mit (i) Hysterese-Smoothing-Layer (Codex-Stress #3 Caveat — ISM-Volatilität würde Composite instabilisieren) + (ii) Empfohlener-vs-Eingetragener-Detector (Codex-Stress #4 Caveat — User-vergisst-Zelle ist primärer Failure-Mode).
14. 👁 **Vault-Discoverability für INSTRUKTIONEN.md §§** (monitor-only, 2026-04-26) — Tier-3-Verortung außerhalb Vault intentional + voll integriert (5 Pointer 00_Core + 3 Wikilinks Vault). §§ vom Wiki-Modus aus nicht per Wikilink springbar — reine Bequemlichkeits-Lücke. **Mögliche Optionen** falls relevant: (a) Vault INSTRUKTIONEN-§§-Index.md Concept-Page (geplant); (b) Reverse-Backlinks-Footer in INSTRUKTIONEN.md. **Re-Activation-Trigger:** konkret aufgetretener Discoverability-Schmerz.

## ⏰ Long-Term-Gates (chronologisch)

| Datum | Gate | Owner-Aktion |
|-------|------|--------------|
| ~04.05.2026 | Tavily Dev-Key Rotation #2 | **Rotation 27.04.2026 KOMPLETT verified** — alter Key `tvly-dev-4PYXp...` ersetzt + post-Restart Smoke-Test PASS (V-Headline-Query lieferte konsistente Daten zu Pre-Earnings-Brief) + alter Key auf tavily.com revoked. Neue Connector-UUID `0da14a12-17bb-4609-bcba-ba2b21152c9b` (alte `4a633350-...` disconnected). Connector-Name weiter `tavily`, friendly-name-Resolution `mcp__tavily__` greift unverändert — Repo-Prompts (`03_Tools/morning-briefing-prompt-v3.md`) unangetastet richtig. Spec-Doc `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` enthält weiter alte UUID als historische Referenz (Doku, nicht operativ — kein Edit nötig). 7-Tage-Uhr läuft formal ab v3.0.4-Prod-Deploy, pragmatisch ~04.05. (7d-rolling ab 27.04.). |
| 2026-07-19 | Track 5a 90-Tage-Audit | EDGAR-Skill Performance-Review (falls promoted) |
| 2026-10-17 | Score-Archiv-Interim-Gate | 6-Monats-Sanity-Check `05_Archiv/score_history.jsonl` (Forward-Window + Duplicate-Guard) |
| 2027-10-19 | R5 Interim-Gate | 18-Mo-Dry-Run `risk-metrics-calculation` + Data-Quality `05_Archiv/portfolio_returns.jsonl` (inkl. FX-Conversion-Check) |
| 2027-10-19 | `float → Decimal` Migration | `PortfolioReturnRecord` + `Position` + `BenchmarkReturnRecord` auf `Decimal` umstellen — R5-Interim-Gate braucht exakte Arithmetik für Sharpe/Sortino/Beta (Backlog-Punkt 1 aus User-Diskussion 21.04.2026; eigener Migration-Plan ~1 Session, blockt Task 14-19 nicht) |
| 2028-04-01 | Review-Gate §29.6 | Aktivierung formales 2J-System-Review |

---

*🦅 PIPELINE.md v1.2 | Dynasty-Depot | Pipeline-SSoT — on-demand via Routing-Table | Stand: 27.04.2026 (Track-5a/5b-Decision A1-Final + AVGO Insider-FLAG-Aktivierung — Long-Term-Gate „AVGO OpenInsider Manual-Check" DONE)*
