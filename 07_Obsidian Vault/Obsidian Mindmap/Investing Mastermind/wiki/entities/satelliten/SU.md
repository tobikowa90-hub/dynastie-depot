---
tags: [satellit, aktiv, defcon-3, non-us, ifrs]
ticker: SU
name: Schneider Electric S.E.
sektor: Energie-Infrastruktur / Automatisierung
ersatz: DE
tier: 3
score_aktuell: 69
defcon: 3
flag: "keins"
sparrate: "18€ (T3-Basis, D3 ×1,0 — Tier-Modell seit 06/2026)"
letzteAnalyse: 2026-04-17
score_valid_until: 2026-10-14
scoring_notiz_v37: "v3.7: Score 71→69 (Fix 3 Sell-Ratio-Kalibrierung leichter Malus). Label D4→D3 seit 18.04.2026 nach Schema-SKILL-Threshold-Alignment (Score 69 in 65-79-Range, Sparrate bei D3/D4 identisch)."
naechsterTrigger: "H1 2026 Earnings 30.07.2026 (earnings_calendar.py-Kanon, half_year_h1 + Earnings-Call → Tag-+1)"
waehrung: EUR
ifrs: true
related_concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]]"
updated: 2026-06-09
---

# SU — Schneider Electric

> **DEFCON 🟡 3 | Score 69/100 (v3.7) | Kein FLAG**
> Sparrate: 18€ (T3-Basis, D3 ×1,0 — Tier-Modell seit 06/2026) | Non-US / IFRS
> *(Label D4→D3 seit 18.04.2026 nach Schema-SKILL-Threshold-Alignment — Score unverändert, Sparrate bei D3/D4 identisch, Volle-Rate-Wert 33,53€→35,63€ weil Nenner 8.5→8.0 nach V-Downgrade)*

## DEFCON v3.4 Analyse (15.04.2026)

| Block | Score | Details |
|-------|-------|---------|
| Fundamentals | 31/50 | ROIC 10.48% > WACC 8.96%. CapEx/OCF 25.2% (stabil). FCF +41% 3J (€4.59B). P/FCF 37.7x (teuer), FCF Yield 2.65%. Goodwill 40.2% (AVEVA, –Malus). Net Debt/EBITDA 2.51x |
| Moat | 16/20 | Narrow/Wide (Morningstar Narrow). EcoStruxure IoT Switching Costs, Intangible Assets (#1 Energiemanagement), Efficient Scale (DC-Boom) |
| Technicals | 8/10 | +12.6% über 200D-MA (einziger Satellit über 200MA ✅). -4.5% vom 52W-Hoch. PT Ø €294.45 (+10.1%) |
| Insider | 7/10 | 3.39% Ownership (>1%-Schwelle). AMF manuell unverified |
| Sentiment | 9/10 | 22 Analysten Strong Buy, 0% Sell |

**Nächste Aktion:** H1 2026 Earnings 30.07.2026 (`earnings_calendar.py`-Kanon)

**Vault-Sync 2026-06-09 (Umstrukturierung-2027):** Tier-Migration Sparrate 35,63€ → **18€** (T3-Basis × D3 1,0) + Frontmatter-Score-Mirror aus `00_Core/Faktortabelle.md` (69/🟡3/Clean unverändert) + Trigger-Datum 30.07. Tool-Kanon. **KEIN Re-Score** — reine State-Spiegelung.

## Stärken

- Energie-Infrastruktur: Profiteur der Elektrifizierungs- und KI-Datacenter-Trends
- EUR-denominiert: Natürlicher USD-Hedge
- CapEx/OCF: 25.2% (4J stabil 23–25%)
- Einziger Satellit über 200D-MA (Stand 15.04.2026)

## IFRS-Besonderheiten

- Halbjährliche Berichte (H1/H2)
- Insider: AMF-Meldungen (amf-france.org)
- Datenquelle: yfinance (SU.PA)

## Verlinkungen

- [[DEFCON-System]]
- [[Faktortabelle-Architektur]]
- [[Analyse-Pipeline]]
- [[Non-US-Scoring]]

## Wissenschaftliche Basis
- [[5J-Fundamental-Fenster]] — 5J-Perspektive als Pflichtrahmen für alle Fundamentaldaten
- [[FCF-Primacy]] — FCF-Yield und forward P/E als primäre Bewertungsanker; trailing P/E: nur Kontext
- [[Moat-Taxonomie-Morningstar]] — Moat-Prüfung nach 8-Quellen-Schema (Wide/Narrow/None)
- [[Wissenschaftliche-Fundierung-DEFCON]] — 7-Befunde-Matrix: wissenschaftliche Validierung des DEFCON-Systems

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** stark — Fwd P/E niedrig, P/FCF klar unter 5J-Median; klassischer Value-Faktor
- **Quality:** moderat — ROIC ölpreisabhängig, Moat narrow (Oil-Sands-Kostenposition)
- **Momentum:** moderat — Commodity-getrieben
- **Defensive:** schwach — hohe Ölpreis-Sensitivität, Beta >1
- **Investment:** moderat — CapEx in Oil-Sands strukturell hoch, aber Integration FCF-positiv

Quellen: [[Aghassi-2023-Fact-Fiction]]
