---
title: "Quality Minus Junk"
date: 2013
type: source
subtype: academic-paper
tags: [quality-factor, qmj, defcon, profitability, growth, safety, payout, source-only, factor-model]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2312432
venue: "AQR Working Paper, October 2013 Draft. Final: Review of Accounting Studies 24, 2019, 34-112"
authors: "Clifford S. Asness (AQR Capital Management), Andrea Frazzini (AQR Capital Management), Lasse Heje Pedersen (NYU Stern, Copenhagen Business School, AQR, CEPR, NBER)"
status: processed
defcon_relevanz: "SOURCE-ONLY. QMJ ist die kanonische Definition des Quality-Faktors (4 Pillars: Profitability, Growth, Safety, Payout) und die Primärquelle für die Quality-Komponente in Buffetts Alpha (B5). Kein direkter Score-Pfad — DEFCON nutzt Quality bereits dekomponiert (ROIC/FCF/OpM/Bilanz). Wert dieser Quelle: (1) Sprachregel für Briefings/Analysen — wenn 'Quality' diskutiert wird, dann mit 4-Pillars-Framing. (2) Buffett-Faktorlogik (B5) ankert hier methodologisch. (3) Komplementäre Lesart zu Piotroski F-Score (B12, dekomponiert) und Wolff-Echterling 2023 (B8/B9, ROIC+FCF+OpM-Top-Prädiktoren)."
sources: []
related:
  - "[[QMJ-Faktor]]"
  - "[[Buffett-Faktorlogik]]"
  - "[[Buffetts-Alpha]]"
  - "[[Piotroski-2000]]"
  - "[[Novy-Marx-2013]]"
  - "[[Wolff-Echterling-2023]]"
  - "[[F-Score-Quality-Signal]]"
  - "[[DEFCON-System]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/asness-frazzini-pedersen.pdf"
aliases:
  - "QMJ Asness Frazzini Pedersen"
  - "Quality Minus Junk"
  - "AQR Quality Paper"
---

# Asness, Frazzini & Pedersen (2013) — Quality Minus Junk

## Abstract (eigene Worte)

Asness, Frazzini und Pedersen definieren Quality als Eigenschaften, für die ein rationaler Investor *ceteris paribus* einen höheren Preis zahlen sollte. Sie operationalisieren Quality über vier Pillars — **Profitability, Growth, Safety, Payout** — und konstruieren einen Quality-Minus-Junk (QMJ) Long-Short-Faktor. Befunde über 24 Developed Markets (1956-2012):

1. **Quality ist gepreist, aber unvollständig** — höhere Quality korreliert mit höheren P/B, aber R² nur 12% (long sample) bzw. 6% (broad sample) → Quality-Premium-Puzzle
2. **QMJ erzielt signifikante risk-adjusted Returns** in 23 von 24 Ländern; positive Alpha gegen 4-Faktor-Modell
3. **Quality ist persistent** — Profitability/Growth/Safety/Payout-Charakteristika bleiben über 5-10 Jahre stabil (notwendige Bedingung für rationale Pricing)
4. **Quality-Resurrection des Size-Effekts** — kontrolliert für Quality wird SMB hoch signifikant (kleine Firmen sind im Schnitt junkig); QMJ erklärt einen Großteil der Buffett-Alpha-Konstruktion
5. **Quality-at-Reasonable-Price (QARP)** — QMJ × Value-Combination outperformt isoliertes HML; ankert Graham-Dodd-Logik empirisch

## Vier Quality-Pillars

| Pillar | Operationalisierung (im Paper) | DEFCON-Mapping |
|---|---|---|
| **Profitability** | Gross profits, margins, earnings, accruals, cash flows — gerankt und kombiniert | ROIC, OpM, FCF-Yield (Fundamentals-Block) |
| **Growth** | Prior 5-J Growth in Profitability-Metriken | 5J-Fundamental-Fenster |
| **Safety** | Market beta, Vola, Leverage, Profit-Vola, Credit Risk | Bilanz-Block (Net Debt/EBITDA, Current Ratio) + ASML-Cycle-Awareness |
| **Payout** | Net Payout Ratio (Dividende + Buybacks − Issuance) | Cash-Deployment-Quality (manuell, kein Score-Pfad) |

→ DEFCON nutzt **alle 4 Pillars dekomponiert**, nicht als Composite — bewusst, weil 4-Min-Score-Routine pro Sub-Dimension Transparenz braucht.

## DEFCON-Konsequenzen (ohne Scoring-Change)

- **B5 (Buffetts Alpha) Methoden-Anker:** QMJ ist die zentrale Quality-Komponente in Buffetts dekomponiertem Alpha. B5 nennt QMJ als ein Drittel des Buffett-Faktor-Stacks (zusammen mit Value/HML und BAB Float-Leverage).
- **Sprachregel:** Wenn "Quality" in Briefing/Analyse diskutiert wird, immer 4-Pillars-Framing benutzen — verhindert reduktive Quality≈Profitability-Verkürzung.
- **QARP-Konzept:** Cross-Reference zu unserer Praxis "Wide Moat × günstige Bewertung = Compounder-Sweet-Spot" — Mauboussin Moat (CAP-Konzept) + QARP sind dieselbe Idee aus unterschiedlichen Methodik-Schulen.
- **Persistence-Befund:** Quality-Charakteristika sind sticky → 5J-Trendbetrachtung (Pflicht in DEFCON) hat empirische Begründung.

## Backlinks

- [[QMJ-Faktor]] — bestehende Concept-Page, B5-Anker (4-Pillars-Framing)
- [[Buffett-Faktorlogik]] — bestehende Concept-Page
- [[Buffetts-Alpha]] — komplementäre Primärquelle (B5)
- [[Piotroski-2000]] — diskrete F-Score-Implementierung
- [[Novy-Marx-2013]] — Profitability-Pillar-Detail
- [[Wolff-Echterling-2023]] — STOXX-600-Validation Quality+ROIC+FCF
- [[F-Score-Quality-Signal]] — operative Konzept-Page
- [[Wissenschaftliche-Fundierung-DEFCON]] — Source-only-Quelle (anchors B5)
- [[Clifford S. Asness]], [[andrea-frazzini|Andrea Frazzini]], [[Lasse Heje Pedersen]] — Author-Entities
