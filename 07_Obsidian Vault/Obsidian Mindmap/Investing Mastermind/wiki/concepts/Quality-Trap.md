---
tags: [concept, defcon, scoring, valuation]
typ: concept
related_skills: "[[dynastie-depot-skill]], [[backtest-ready-forward-verify]]"
related_concepts: "[[DEFCON-System]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]], [[CapEx-FLAG]]"
updated: 2026-05-06
---

# Quality-Trap (DEFCON v3.7 §472-§478)

> Wide-Moat × High-Multiple-Cap-Mechanik im DEFCON-Scoring-System. Verhindert, dass strukturell teure Wide-Moat-Kompounder allein durch Moat-Bonus auf hohe Scores klettern, wenn das Multiple bewertungsseitig fundamental gegen den Investor läuft.

## Kern-Mechanik

Wide-Moat-Tickers triggern bei bestimmten Bewertungsschwellen Cap-Regeln, die einzelne Sub-Score-Punkte unabhängig von anderen Faktoren auf Maximalwerte deckeln:

- **Wide × Fwd P/E**: bei Fwd P/E ∈ [22; 30] → max 1 Pkt im Fwd-P/E-Sub-Block (statt regulär 5-7 Pkt)
- **Wide × P/FCF >35**: harter 0-Cap im P/FCF-Sub-Block (§472-§478, kein Pkt-Anrechnung mehr)

Diese Caps wirken vor allem bei strukturell expensive Compounders mit anhaltend gutem operativem Beat — das operative Wachstum wird zwar im Moat-Block belohnt, aber im Bewertungs-Block durch die Caps geblockt. Ergebnis: Wide-Moat-Premium-Aktien zeigen oft Score-Plafonds um 50-70 trotz weiterhin starker Operations.

## §410 Goodwill-Bereinigte ROIC (Eskalations-Pfad)

Bei M&A-Compoundern (GW/Assets ≥30%) ist die GAAP-ROIC-Lesart strukturell verzerrt. Das DEFCON-System erlaubt §410-Goodwill-Bereinigung als ROIC-Alternativrechnung mit den Bedingungen:
- GW/Assets ≥30% (Threshold-Gating, nicht graduell)
- M&A-Compounder-Profil belegt (mehrere Akquisitionen, klare Akquisitions-Strategie)
- Invested Capital bereinigt = Total Assets − Goodwill (näherungsweise)

§410-Bereinigung kann Quality-Trap teilweise neutralisieren, weil bereinigte ROIC>WACC-Spreads im Quality-Sub-Block deutlich höhere Punkte liefern. Aber: Die Wide × P/FCF >35-Hartcap bleibt bestehen, weil sie multiplebasiert ist, nicht renditebasiert.

## B6 Drawdown-Modulator (v3.7.6 chirurgisch)

Skill-Paket v3.7.6 (30.04.2026, post Quality-Trap-Methodology-Review PIPELINE #28) ergänzt: **Drawdown ≥-20% vs. 52W-High UND Multiple unter 5J-Median (np.median 20 Stichtage, mind. 12 belastbar, strikt positive Nenner) → `max 1`-Caps deaktiviert per-Subscore.** Hard-Caps unverändert. Codex-R1→R4 96% Confidence (4 HIGH + 4 MEDIUM closed inkl. B1 Nenner-Sign-Gate).

Anwendungsbereich: Forward-only (keine MSFT-Q3-Backfill); Non-US-Freeze (ASML/SU INAKTIV); Screener-Exceptions (BRK.B/COST/RMS/TMO) ausgenommen.

## Beispiele aus Live-Runs

- **AVGO 30.04.2026:** Wide × Fwd P/E 22,98 → max 1; Wide × P/FCF 74,4x → hart 0; ROIC GAAP 3,98% < WACC 15,96% → §410 GW-bereinigt 45,7% (NOPAT $22,2B / IC-GW $48,6B; M&A-Compounder VMware/CA/Symantec/Brocade GW 57,2%). Score 84→53 (D4→D2).
- **MSFT 30.04.2026:** Wide × Fwd P/E 22,44 → max 1; Wide × P/FCF 39,7x → hart 0; ROIC 7,68% < WACC defeatbeta 13,64% = 1/8. Score 59→50 (D2 unverändert, FLAG aktiv).
- **APH 30.04.2026:** Multiple-Expansion P/E 25→33,7 deckelt 16 Pkt. weg trotz operativem Beat; CommScope Net-Lev 1,6x verschärft Bilanz-Gewichtung. Score 63→61 (D2 unverändert).

## Verlinkungen

- [[DEFCON-System]] — Übergeordnetes Scoring-System
- [[FCF-Primacy]] — FCF-Yield + Forward P/E als primäre Bewertungsanker
- [[Moat-Taxonomie-Morningstar]] — Wide/Narrow/None-Klassifikation
- [[CapEx-FLAG]] — Verwandte FLAG-Mechanik (CapEx/OCF-basiert)
- [[AVGO]], [[MSFT]], [[APH]] — Aktive Quality-Trap-Anwendungsfälle
- [[Wissenschaftliche-Fundierung-DEFCON]] — Wissenschaftliche Validierung der Moat-Bewertungs-Wechselwirkung
