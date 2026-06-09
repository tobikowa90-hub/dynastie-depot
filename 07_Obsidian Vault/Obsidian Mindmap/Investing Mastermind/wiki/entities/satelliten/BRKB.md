---
tags: [satellit, aktiv, defcon-3, screener-exception]
ticker: BRK.B
name: Berkshire Hathaway Inc. (Class B)
sektor: Kapitalallokation / Holding
ersatz: MKL
tier: 3
score_aktuell: 71
defcon: 3
flag: "keins"
sparrate: "18€ (T3-Basis, D3 ×1,0 — Tier-Modell seit 06/2026)"
letzteAnalyse: 2026-05-04
score_valid_until: 2026-10-31
naechsterTrigger: "Q2 FY26 10-Q-Filing 01.08.2026 (earnings_calendar.py-Kanon; §19.1 BRK-Ausnahme — kein Q-Call) — KHC-OTTI-Resolve + GEICO-UW-Decel-Trend + Form-13F Apple-Trim-Magnitude + Buyback-Cashflow-Reconciliation + BHE-ETR-Wildfire-Settlement + OxyChem-Goodwill-Allocation-Refinement"
scoring_notiz_v37: "04.05.2026 Q1 FY26 Tag-+1 Vollanalyse + Codex-R1-REJECT-Korrektur (§19.1 BRK-Ausnahme: Filing-Trigger 02.05. Sa, kein Q-Call): Score **75→71 (Δ-4)** post-R1-Sparring; D3 unverändert (65-79-Band 6pt-Puffer), FLAG ✅ Clean Insurance-Exception unverändert, Sparrate 38€ unverändert, keine Kaskade. Sub-Score-Karte F=35/M=19/T=1/I=10/S=6."
related_concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]], [[Buffett-Faktorlogik]], [[QMJ-Faktor]]"
related_sources: "[[Buffetts-Alpha]]"
updated: 2026-06-09
---

# BRK.B — Berkshire Hathaway B

> **DEFCON 🟡 3 | Score 71/100 | ✅ Clean (Insurance Exception)**
> Sparrate: 18€ (T3-Basis, D3 ×1,0 — Tier-Modell seit 06/2026) | Defensivster Satellit
> *(Score 75→71 Δ-4 post Codex-R1-REJECT-Korrektur 04.05.2026 nach Q1 FY26 Tag-+1 Vollanalyse — D3 unverändert, keine Kaskade)*

## DEFCON v3.7 Analyse — Q1 FY26 Tag-+1 (04.05.2026)

§19.1 BRK-Ausnahme aktiv: Filing-Trigger 02.05. Sa (10-Q + Press-Release parallel zur Annual Meeting Omaha), kein Quarterly Earnings Call → Tag-+1 = Mo 04.05. mit 10-Q-Read + Annual-Meeting-Q&A-Substitute (CNBC paywall, Forbes/Bill-Stone + Perplexity-Aggregation) + insider_intel.py Form-4-Pull live.

| Block | Score | Details |
|-------|-------|---------|
| Fundamentals | 35/50 | fwd_pe=1 (QT-Cap Wide × Fwd-P/E 22,82 ∈ [22,30]) / p_fcf=0 (Insurance/Float N/A) / bilanz=9 (Cash-ATH effektiv $380,2B nach Forbes-T-Bill-Settlement-Bereinigung; nominal $397,4B − $17,2B Payable) / capex_ocf=9 (Insurance-Exception N/A) / roic=8 (Float-Modell-Spread, Buffett→Abel-Capital-Allocation-Continuity) / fcf_yield=7 (Holdings-Earnings-Power 4,5%) / operating_margin=1 (~11% TTM Konzern-Aggregate) / sbc/accruals/tariff_malus=0/0/0 |
| Moat | 19/20 | Wide-Konsens 3 Quellen: Morningstar Wide carryover + GuruFocus Moat-Score carryover + Annual-Meeting-2026 Abel-Allocation-Framework-Continuity. Float-Leverage einzigartig, BNSF Efficient Scale, 60J Capital-Allocation-Track-Record. Kein Pricing-Power-Bonus (V-Q2-Lehre: Statement ohne quantifizierte Implementierung) |
| Technicals | 1/10 | Kurs $468,52 vs ATH ~$528 = -11,3% (Buffer-1 1/4) · YTD/6M -9,7pp vs SPY (RelStr 0/3) · Kurs unter 200MA $489,90 strict (200MA-Lage 0/3 per SKILL.md Z.603) · ma200_slope=flat |
| Insider | 10/10 | insider_intel.py 04.05. live-pull: 7 Form-4-Filings, Net Buy 6M $+15.308.372 dominiert von Greg Abel Open-Market = 4/4 · Diskretionäre 90d-Sales $0 = 3/3 · Buffett >30% Class-A Ownership carryover = 3/3 · Annual-Meeting-Anchor: „Abel investierte sein gesamtes Netto-Gehalt $15M persönlich in BRK-Aktien" = doppelt verankert SEC Form-4 + Live-Statement |
| Sentiment | 6/10 | strong_buy_ratio=2 (Coverage-Sparseness 2-3 Analysten FY26/FY27, Zacks-Rank #4 tautologisch zu Coverage) · sell_ratio=2 · pt_upside=2 · eps_revision_delta=0 (0/0 Revisions 7d/30d, Pre-Earnings-Estimate-Stale; Refresh-Window 07.-09.05.) · pt_dispersion_delta=0. **GAAP-vs-Operating-EPS-Outlier-Caveat:** FY26e Operating-EPS ~$20,83 vs GAAP-EPS ~$14,06 (32,5% Diff durch ASC 825-10 Mark-to-Market) |

**Q1 FY26 Operativer Beat:** Operating Earnings $11,346B vs $9,641B Q1-25 (+17,7%); Operating-EPS Class B ~$5,26 vs Estimate $5,05 (+4,2% Beat); Insurance-Underwriting $1,72B (+28,5% Headline, ABER GEICO-Loss-Ratio 73,9% vs 69,0% +4,9pp Decel-Asymmetrie + BHRG/BH-Primary-Recovery-Base-Effekt); BNSF $1,38B (+13,4% Operating-Leverage 2,8×); BHE $1,11B (+1,5% flat); MSR $3,20B (+4,5%); Float $176,9B (+$0,5B QoQ marginal); Buyback Q1 $235M (Run-Rate 0,06% von Cash); OxyChem-Acquisition $9,5B (02.01.2026, erste Major-M&A seit Alleghany 2022).

**Codex-R1-REJECT-Korrektur (3 HIGHs, kein R2-SendMessage nötig — SKILL-Literal-Read):**
- **HIGH-1** T=2 → T=1 (SKILL.md Z.603 strict „Kurs unter 200MA → 0/3" keine Bandbreite)
- **HIGH-2** S=8 → S=6 (+2 Annual-Meeting-Color = Methodology-Drift ohne Skill-Exception-Klausel; V-Q2-Lehre direkt — Annual-Meeting-Color gehört in notizen, nicht in Score)
- **HIGH-3** F=36 → F=35 (Forbes/Bill-Stone Cash-Reconciliation ist Secondary-Confirm; 10-Q p.2-3 ist Primary mit gleichem Inhalt; Pre-Brief §7 „NEUTRAL mit Caveat"-Empfehlung gilt — kein +1-Lift)

**Nächste Aktion:** Q2 FY26 Earnings ~02./03.08.2026 — 6 Methodology-Watches PIPELINE #36-#41: KHC-OTTI-Resolve · GEICO-UW-Decel-Trend · Form-13F Apple-Trim-Magnitude (mid-Mai 14.05. Definitiv) · BHE-ETR-Wildfire-Settlement (PacifiCorp $577M unpaid) · OxyChem-Goodwill-Allocation-Refinement (ASC 805 12-Mo-Window) · Buyback-Cashflow-Discrepancy-Reconciliation ($4,57B 10-Q vs $235M PR Settlement-Timing-Hypothese)

**Vault-Sync 2026-06-09 (Umstrukturierung-2027):** Tier-Migration Sparrate 38,00€ → **18€** (T3-Basis × D3 1,0) + Frontmatter-Score-Mirror aus `00_Core/Faktortabelle.md` (71/🟡3/Clean unverändert); Trigger-Datum auf `earnings_calendar.py`-Kanon 01.08. präzisiert. **KEIN Re-Score** — reine State-Spiegelung.

## Sonderregel

**P/B statt P/FCF** — Float-Modell. Versicherungs-Exception aktiv. Combined Ratio als Primärmetrik statt ROIC.

## Stärken

- Holding mit diversifizierter Wertschöpfung (BNSF, GEICO, Apple-Stake etc.)
- Niedrige Tariff-Direktexposition strukturell
- Warren Buffett Kapitalallokation — Jahrzehnte-Track-Record
- Greg Abel Insider-Käufe $15.3M — starkes Nachfolge-Alignment

## Verlinkungen

- [[DEFCON-System]]
- [[Faktortabelle-Architektur]]
- [[Analyse-Pipeline]]
- [[MKL]] — Ersatz-Kandidat (Ersatzbank)

## Wissenschaftliche Basis
- [[5J-Fundamental-Fenster]] — 5J-Perspektive als Pflichtrahmen für alle Fundamentaldaten
- [[FCF-Primacy]] — FCF-Yield und forward P/E als primäre Bewertungsanker; trailing P/E: nur Kontext
- [[Moat-Taxonomie-Morningstar]] — Moat-Prüfung nach 8-Quellen-Schema (Wide/Narrow/None)
- [[Buffett-Faktorlogik]] — PFLICHT: Float-Leverage (~1,6x) nicht replizierbar; übertragbar: cheap+safe+quality
- [[QMJ-Faktor]] — QMJ+BAB+Value erklärt Buffetts Alpha vollständig
- [[Buffetts-Alpha]] — Primärquelle: Frazzini, Kabiller, Pedersen (AQR 2018)
- [[Wissenschaftliche-Fundierung-DEFCON]] — 7-Befunde-Matrix: wissenschaftliche Validierung des DEFCON-Systems

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** moderat — P/B historisch nah am Median, Fwd P/E nicht dramatisch
- **Quality:** stark — operative Töchter + Versicherungs-Float, Buffett-Faktorlogik (siehe [[Buffett-Faktorlogik]], [[QMJ-Faktor]])
- **Momentum:** moderat — Kurs-Stabilität
- **Defensive:** stark — Insurance-Exception-Profil, Rezessions-resilient, Cash-Reserve
- **Investment:** n.a. — Holding-Struktur, CapEx-Logik via Töchter nicht direkt ableitbar

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Buffetts-Alpha]], [[Buffett-Faktorlogik]]
