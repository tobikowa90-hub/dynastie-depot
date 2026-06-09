---
tags: [satellit, aktiv, defcon-2, flag-aktiv]
ticker: AVGO
name: Broadcom Inc.
sektor: KI / Chips / Asset-Light
ersatz: NVDA
tier: 1
score_aktuell: 56
defcon: 2
flag: "FLAG aktiv (insider_selling_20m, $106,4M diskretionär 90d, aktiviert 27.04.2026; Q2 FY26 04.06. Beat-Raise — FLAG bleibt, Samueli $281M 25.03. als 10b5-1 ausgeschlossen)"
sparrate: "0€ (T1-Basis 40€, FLAG-Override Score-unabhängig → 0€)"
letzteAnalyse: 2026-06-04
score_valid_until: 2026-12-04
scoring_notiz_v37: "30.04.2026 Forward-Vollanalyse: Score **84→53 (Δ-31)**, D4→D2, FLAG aktiv unverändert. Codex R1+R2-Doppel-Pass APPROVE Master-Reading 74% Confidence. Quality-Trap voll aktiv (Wide × Fwd P/E 22,98 max 1; Wide × P/FCF 74,4 hart 0); ROIC GAAP 3,98% < WACC 15,96% → §410 Goodwill-bereinigt 45,7% (M&A-Compounder VMware/CA/Symantec/Brocade GW 57,2%). Insider 3/10 (Live-Pull insider_intel.py 30.04.: 231 Tx, Diskr. 90d $106,4M = 5× Schwelle); Skip-Window-Carryover NICHT angewandt (V-Q2-Asymmetrie). 5 PIPELINE-Methodology-Watches #30-34. Sparrate 0€ unverändert (FLAG-Override, keine Kaskade)."
naechsterTrigger: "Q3 FY26 Earnings 03.09.2026 (earnings_calendar.py-Kanon) — !Analysiere FLAG-Re-Eval (Insider-Diskr 90d <$20M) + DEFCON-Refresh + Methodology-Watches"
related_concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]], [[Quality-Trap]], [[CapEx-FLAG]]"
updated: 2026-06-09
---

# AVGO — Broadcom Inc.

> **DEFCON 🟠 2 | Score 56/100 (v3.7.6, Stand Q2 FY26 04.06.2026) | 🔴 FLAG aktiv** (insider_selling_20m, seit 27.04.2026)
> Sparrate: 0€ (T1-Basis 40€, FLAG-Override → 0€) | ehemals Kalibrierungsanker #1 — Anker-Status revidiert post Forward-Vollanalyse
> *(Q2 FY26 Tag-+1-Vollanalyse 04.06.2026 hob Score 53→56; D2/FLAG/0€ unverändert. Body „Warum 53" unten = 30.04.-Analyse — Body-Refresh deferred an `!Analysiere`.)*

## Aktuelle Lage (Stand: 30.04.2026 — Forward-Vollanalyse v3.7.6)

Score **84→53 (Δ-31, D4→D2)** in erster echter Forward-Vollanalyse seit Skill-Adoption — ersetzt PIPELINE #18 ScoreRecord-Backfill durch Schema-konformen `analyse_typ=vollanalyse`-Pfad. **FLAG aktiv unverändert** (insider_selling_20m, Resolve-Schwelle $20M-Diskr-90d weit überschritten bei $106,4M). **Keine Kaskade** auf Sparraten (FLAG-Override Score-unabhängig).

**Codex R1+R2-Doppel-Sparring:** R1 5 HIGH (1=APPROVE §410, 2=REJECT Fwd P/E StockAnalysis→Yahoo/Finviz 22,98 +1, 3=CHALLENGE Insider-Skip-Window, 4=APPROVE ATH, 5=REJECT DCF-Malus heuristic +1) + 4 MED + 3 LOW. R2 zu HIGH-3 disambiguiert: APPROVE Master-Reading 53/D2 (3 Punkte A/B/C, 74% Confidence, kein Mittelweg).

## Warum 53 und nicht höher

- **Quality-Trap voll aktiv (B6 Drawdown-Modulator NICHT aktiviert):** Wide × Fwd P/E 22,98 → max 1 Pkt; Wide × P/FCF 74,4x >35 → hart 0 (§472-§478)
- **ROIC<WACC trotz §410-Bereinigung:** GAAP 3,98% / WACC defeatbeta 15,96% → Goodwill-bereinigt 45,7% (NOPAT $22,2B / IC-GW $48,6B; M&A-Compounder VMware $61B + CA $19B + Symantec $10B + Brocade $5,5B; GW/Assets 57,2%) → 7/8 (konservativ statt 8/8 wegen StockAnalysis-Methodology-Drift)
- **Insider-Block-Kollaps 8→3:** Live-Form-4-Pull 30.04. via insider_intel.py: 231 Tx, 36 Form-4, 7 Diskr.-Verkäufer (CEO Tan / CFO Spears / ISG Velaga / SSG Kawwas / CLO Brazeal); Net 6M -$640M; Diskr. 90d $106,4M = 5× Schwelle. Skip-Window-Carryover NICHT angewandt (V-Q2-Asymmetrie: explizite neue primary-source-Datenerhebung erlaubt Down-Scoring)
- **Sentiment 2/10:** SB 87% Crowd-Malus +1, Sell 0% +1, PT-Upside +4,8% +1, PT-Dispersion 81% -1
- **CapEx/OCF 2,26% Fabless-Referenz** bleibt Top (9/9 max), aber durch Quality-Trap-Cap nicht voll wirksam

## Schlüsselmetriken (30.04.2026 Live)

- CapEx/OCF: **2,26%** — Fabless-Referenz ✅ (9/9 max)
- ROIC GAAP: 3,98% / WACC defeatbeta: 15,96% / §410 GW-bereinigt: 45,7%
- Fwd P/E: 22,98 (StockAnalysis 19,06 vs Yahoo 22,98 vs Finviz — Methodology-Watch #31)
- P/FCF: 74,4x (>35 Quality-Trap-Hart-Cap)
- Insider Diskr. 90d: **$106,4M** (5× Schwelle); Net 6M: -$640M
- Tariff-Exposure: MY/TH ~35% — Risk-Map-Notiz, kein FLAG (Grenzwert)

## Insider-FLAG-Status (UPDATED 30.04.2026)

**FLAG aktiviert 27.04.2026** nach OpenInsider-Cross-Check: 9 Transaktionen 90d, alle „S - Sale" ohne 10b5-1-Suffix, kein Cashless-Pattern. Skript-Lesart $106M (5× Schwelle), OpenInsider-Lesart $280M+ (14× inkl. Samueli $250M Dir 25.03.). Watchlist-These „Post-Vesting" widerlegt — Diskretionäre Sales bestätigt.

**30.04.2026 Live-Pull-Verify** via `insider_intel.py`: 231 Transaktionen über 6 Monate, 36 Form-4-Filings, 7 Diskretionär-Verkäufer (Tan/Spears/Velaga/Kawwas/Brazeal/+2). Insider-Ownership 1,13% = 3/3 (positiv).

**FLAG-Resolution-Pfad:** Diskretionär 90d <$20M-Schwelle nachhaltig 2 Quartale. Re-Eval Q3 FY26.

## Verlinkungen

- [[DEFCON-System]]
- [[NVDA]] — Ersatz-Kandidat
- [[CapEx-FLAG]] — Warum Fabless-Modelle top-scoren

## Analyse-Historie

| Datum | Score | DEFCON | Ereignis |
|-------|-------|--------|---------|
| 25.03.2026 | 86 | 🟢 4 | v3.5-Vollanalyse — Kalibrierungsanker gesetzt |
| 06.04.2026 | 86 | 🟢 4 | Insider-Check — kein FLAG nach manuellem Review |
| 17.04.2026 | 84 | 🟢 4 | v3.7-Algebra (Fundamentals-Cap 50 Fix, -1 Pt.) — Sub-Audit pending Q3 FY26 |
| 27.04.2026 | 84 | 🟢 4 | **FLAG aktiviert** (insider_selling_20m, $106M+ diskretionär 90d) — OpenInsider-Cross-Check widerlegt Watchlist-These „Post-Vesting" |
| 30.04.2026 | **53** | **🟠 2** | **Forward-Vollanalyse v3.7.6** — Δ-31 (Quality-Trap voll + ROIC<WACC + Insider-Live-Verify); FLAG aktiv unverändert; Codex R1+R2 74% Confidence APPROVE; Sparrate 0€ (keine Kaskade) |
| 2026-06-04 | **56** | 🟠 2 | **Q2 FY26 Tag-+1-Vollanalyse** — 53→56 (+3 Beat-Raise); D2/FLAG/Sparrate 0€ unverändert. Samueli $281M 25.03. korrekt als 10b5-1 ausgeschlossen (User-Challenge empirisch bestätigt). ScoreRecord `2026-06-04_AVGO_vollanalyse`, Commit `6f91aad`. |
| 2026-06-09 | **56** | 🟠 2 | **Vault-Sync (Umstrukturierung-2027):** Frontmatter/Header-Score-Mirror 53→56 aus `00_Core/Faktortabelle.md` + Tier-Migration (T1-Basis 40€, FLAG → 0€) + Trigger-Datum 03.09. Tool-Kanon. **KEIN Re-Score** — Spiegelung des bereits committeten 04.06.-Stands. |

## Wissenschaftliche Basis
- [[5J-Fundamental-Fenster]] — 5J-Perspektive als Pflichtrahmen für alle Fundamentaldaten
- [[FCF-Primacy]] — FCF-Yield und forward P/E als primäre Bewertungsanker; trailing P/E: nur Kontext
- [[Moat-Taxonomie-Morningstar]] — Moat-Prüfung nach 8-Quellen-Schema (Wide/Narrow/None)
- [[Wissenschaftliche-Fundierung-DEFCON]] — 7-Befunde-Matrix: wissenschaftliche Validierung des DEFCON-Systems

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E hoch, bewertet als AI-Play; P/FCF oberhalb 5J-Median
- **Quality:** stark — ROIC stark > WACC, Moat wide (Networking + Software-Post-VMware), Customer-Stickiness
- **Momentum:** stark — Kurs-Rally 2025-26 anhaltend, Q3 FY26 Trigger steht aus
- **Defensive:** schwach — Insider $123M/90d trotz wahrscheinlichem Post-Vesting, Kunden-Konzentration
- **Investment:** moderat — VMware-Integration-CapEx elevated, aber operativ kontrolliert

Quellen: [[Aghassi-2023-Fact-Fiction]]
