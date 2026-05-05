# 🎯 STATE.md — Dynasty-Depot Hub

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — Offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Infrastruktur / Briefing / Backtest-Ready
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13)
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Banner-Chronik

## ⚠️ Critical-Alerts (≤ 10 Tage — handgepflegt)
- **05.05. (Di) Ruflo+Superpowers Coexistence Spec v1.0-Draft DONE — `docs/superpowers/specs/2026-05-05-ruflo-superpowers-coexistence-design.md`** (lokal, gitignore-konform per `docs/superpowers/`-Convention). 7 Sektionen, **Variante D — Capability-Layered Hybrid With Explicit Adoption Gates**. Superpowers = Default-Workflow-Layer; Ruflo = Substrat-Layer; Workflow-Layer-Erweiterungen Ruflos per Default BLOCKED, Promotion nur via fail-closed Adoption-Gate. Codex-Sparring R1-R7 (~75k Tokens, ≥95% Confidence). **User-Review-Gate offen für 06.05. morgens** vor Übergang zu `superpowers:writing-plans` für Plan-v1.2. Welle-3-Empfehlung: 1.8 Doctor-Periodic push, 1.9 Trajectory → audit-trace-lite (semi-manueller Pilot, `05_Archiv/audit_trace_lite.jsonl`). PIPELINE #42 trackt Plan-v1.2 + Spec-Review-Gate.
- **04.05. (Mo) BRK.B Q1 FY26 Tag-+1 Vollanalyse DONE — Codex-R1-REJECT-Korrektur Score 75→71** (Δ-4, post-R1-Sparring 04.05. nachmittags). **Sub-Score-Karte korrigiert: F=35** (Forbes-Cash-Reconciliation ist Secondary, 10-Q p.2-3 ist Primary mit gleichem Inhalt → kein +1-Lift, Pre-Brief §7 NEUTRAL-mit-Caveat-Empfehlung gilt) **/ M=19** (carryover unverändert) **/ T=1** (SKILL.md Z.603 strict: „Kurs unter 200MA → 0/3" — keine Bandbreite; ATH-Buffer-1 1/4, RelStr 0/3, 200MA 0/3) **/ I=10** (carryover Sub-Block + FRESH insider_intel.py-Pull legitimer Verify) **/ S=6** (Annual-Meeting-Color +2 ist Methodology-Drift ohne Skill-Exception-Klausel, V-Q2-Lehre direkt; Standard-Sentiment 6 carryover). **Total 35+19+1+10+6 = 71.** **D3 unverändert** (65-79-Band, 6pt-Puffer zu D2), **FLAG ✅ Clean (Insurance Exception) unverändert**, **Sparrate 38€ unverändert**, **keine Kaskade**. R2-Sparring HIGH-1 via SKILL-Literal-Read = strict-konsistent (kein SendMessage nötig). 15/15 Codex-HIGH-Antis pre-empted (Pre-Brief §9 12 + User-Inputs §4 #13-15; #11 Insider-Form-4-Pull DONE LIVE; #15 Cash-Reconciliation RESOLVED via 10-Q-Primary). 6 PIPELINE-Methodology-Watches Q2-Carryover #36-#41 unverändert. **Schritt 7 backtest-ready ScoreRecord-Append DEFER auf Tag-+1-Abend** (close-of-04.05. erst nach US-Marktschluss 22:00 MEZ; Provenance-Gate Check #3 kurs.referenz="close_of_score_datum" sonst FAIL); Score 71 + korrigierte Sub-Karte werden im ScoreRecord-Draft persistiert.
- **02.05. (Sa) BRK.B Q1 FY26 — Tag-0 DONE** earnings-recap + 10-Q-Quick-Read + Tag-+1-Vorbereitungs-Brief + Annual-Meeting-Q&A-File 02.05. (CNBC Live-Feed via Sonnet) + §19.1 BRK-Ausnahme-Klausel in INSTRUKTIONEN.
- **30.04.** AVGO Forward-Vollanalyse **DONE** — Score **84→53 (Δ-31), D4→D2**, FLAG aktiv unverändert (`AVGO_insider_selling_20m_2026-04-27`), Sparrate 0€ unverändert (FLAG-Override Score-unabhängig, **keine Kaskade**). Erste echte Forward-Vollanalyse seit Skill-Adoption — ersetzt PIPELINE #18 Backfill durch Schema-konformen Vollanalyse-Pivot. Codex R1+R2-Pass APPROVE Master-Reading 74% Confidence (R2 schwächster Hebel B Backfill-Inkonsistenz). Quality-Trap voll aktiv (Wide × Fwd P/E 22,98 max 1; Wide × P/FCF 74,4 hart 0); ROIC GAAP 3,98% < WACC 15,96% → §410-Goodwill-bereinigt 45,7% (M&A-Compounder VMware/CA/Symantec/Brocade GW 57,2%). Insider-Live-Pull (insider_intel.py 30.04.: Diskr. 90d $106,4M = 5× Schwelle), Skip-Window-Carryover NICHT angewandt (V-Q2-Asymmetrie + Backfill-Inkonsistenz). 5 neue PIPELINE-Methodology-Watches #30-34. ScoreRecord `2026-04-30_AVGO_vollanalyse` (record 33). Sync §18.1 v2.3 vollständig.
- **30.04.** PIPELINE #24 Stufe 1 **DONE** — `03_Tools/earnings_calendar.py` v1.0 deployed. yfinance-Pull 11/11 PASS, BRK.B-Smoke ✅, 1 Drift detektiert (BRK.B 02.05. konkretisiert in PORTFOLIO/STATE/PIPELINE-10d). SYSTEM.md neue §Earnings-Calendar-Status, INSTRUKTIONEN §27.6 neu.
- **30.04.** PIPELINE #20 Ruflo-Integration **Phase 1.2-1.7 §18-Sync-Welle DONE** — Google-Drive-Mirror für `Claude Stuff` entfernt (root_id=3 aus DriveFS-Roots, kein File-Lock mehr auf memory.db); WSL `ruflo memory init --force` + 19/20 path-scoped Dynastie-Memory-Import in `patterns`-Namespace (Mock-Embeddings, `import-all` strikt ausgeschlossen); Top-K=3 persistiert via `ruflo config set`; `.claude/settings.json` env-Tool-Mode + ruflo-Config-Block; `.gitignore` erweitert um `.swarm/` + `.claude/memory.db*`; CLAUDE.md Codex-Nits-Nachfix (Hard-Conflict-#5 Hintertür-Klausel verschärft + Compatible-Block `allProjects=false`); SYSTEM.md neu §Ruflo-Status. Welle 3 (1.8/1.9) bleibt 05.-12.05. post-BRK.B-Tag-+1.
- **30.04.** PIPELINE #28 Quality-Trap-Methodology-Review **DONE** — Skill-Paket v3.7.5→v3.7.6 mit B6 Drawdown-Modulator (Option 2 chirurgisch). Codex-R1→R4 96% Confidence (4 HIGH + 4 MEDIUM closed inkl. B1 Nenner-Sign-Gate). Mechanik: `max 1`-Caps deaktiviert per-Subscore wenn Drawdown ≥-20% vs 52W-High UND Multiple unter 5J-Median (np.median 20 Stichtage, mind. 12 belastbar, strikt positive Nenner). Hard-Caps unverändert. Forward-only (keine MSFT-Q3-Backfill); Non-US-Freeze (ASML/SU INAKTIV); Screener-Exceptions (BRK.B/COST/RMS/TMO) ausgenommen.
- **30.04.** MSFT Q3 FY26 Tag-+1 Vollanalyse — **DONE** (Score 59→**50** Δ-9, D2/FLAG aktiv unverändert; Bull-Case Trigger A ✅ / B ❌ FAIL CY26 $190B vs Konsens $154,6B Surprise +23% / C ✅✅; Codex-R1+R2-Doppel-Review V-Q2-Mittelweg via Insider-Skip-Carryover; 4 PIPELINE-Items #25-28 aktiv; Sparrate 0€ unverändert; Methodology-Watch defeatbeta-WACC 13,64% vs FRED-Baseline 9,7% Q4-Verify)
- **30.04.** APH Q1 FY26 Tag-+1 Vollanalyse — DONE (Score 63→61, D2/FLAG aktiv unverändert, Codex-Review-Pass). Methodology-Watch Q2: China-Tax-ETR 27% strukturell + CommScope-Net-Lev 1,6x → <1,5x bis Q4 + ROIC-GW-Bereinigung Full-Year-Confirm
- **14.05.** MSFT Insider-Block-Re-Score post-14d-Skip-Window via insider_intel.py (PIPELINE #26)

## Navigation (on-demand)
| Wenn du brauchst… | Lies… |
|---|---|
| Scores / FLAGs / Watches / Sparraten / 30-Tage-Trigger | **PORTFOLIO.md** (default-load) |
| Offene Pläne, Gates, Primary-Track | PIPELINE.md |
| System-Versionen, Briefing-Status, Infra | SYSTEM.md |
| Lektionen / Per-Ticker-Chronik / Lifecycle | CORE-MEMORY.md (§5 / §12 / §13) |
| Workflows / Sparraten-Formel / Sync-Pflicht | INSTRUKTIONEN.md |
| Strategie / Allokation | KONTEXT.md (on-demand) |
| Score-Detail pro Ticker | Faktortabelle.md |

**Sync-Pflicht (§18 v2.3):** bei Score/FLAG/Sparraten-Change → PORTFOLIO.md + CORE-MEMORY + Faktortabelle + log.md + score_history.jsonl + `01_Skills/dynastie-depot/config.yaml` + `03_Tools/Rebalancing_Tool_v3.4.xlsx` + `03_Tools/Satelliten_Monitor_v2.0.xlsx` (+ flag_events.jsonl). Details in INSTRUKTIONEN §18 (inkl. Multi-Event-Union-Regel + xlsx-Tools-Pflicht seit v2.3 28.04. spätabends).

<!-- system-audit:last-audit:start -->
---

## 🔍 Last Audit

**Timestamp (UTC):** 2026-04-30T15:08:02Z
**Result:** 3/3 PASS
**Run:** `python 03_Tools/system_audit.py --minimal-baseline`
**Full-Report:** stdout (kein Archiv-File)

<!-- system-audit:last-audit:end -->

*🦅 STATE.md Hub v2.0 | Dynasty-Depot | Navigation + Critical-Alert + Last-Audit | Stand: 30.04.2026 (AVGO Forward-Vollanalyse 84→53 D4→D2 FLAG aktiv unverändert)*
