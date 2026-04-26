---
title: "Value and Momentum Everywhere"
date: 2013
type: source
subtype: academic-paper
tags: [value-factor, momentum-factor, global-asset-pricing, liquidity-risk, three-factor-model, source-only]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2174501
venue: "Journal of Finance 68(3), 2013, 929-985. Chicago Booth Working Paper No. 80, NBER Working Paper 18039"
authors: "Clifford S. Asness (AQR Capital Management), Tobias J. Moskowitz (University of Chicago Booth, NBER), Lasse Heje Pedersen (NYU Stern, Copenhagen Business School, AQR, CEPR, NBER)"
status: processed
defcon_relevanz: "SOURCE-ONLY (anchors B7 Block-Gewichtung 50/20/10/10/10). Value + Momentum-Faktoren existieren kohärent über 8 globale Asset-Klassen (Aktien US/UK/Europa/Japan, Country-Equity-Indices, Government Bonds, Currencies, Commodities). Kern: Value und Momentum sind **global, persistent, und negativ korreliert intra/inter-asset-class**. Funding-Liquidity-Risk erklärt einen Teil der Returns. Operative Konsequenz: bestätigt **Block-Gewichtung 50/20/10/10/10** — Value/Trailing-Bewertung muss Faktor sein (über Fwd-P/E + P/FCF im Fundamentals-Block), Momentum/Technicals als sekundärer 10-Pt-Block ist methodisch ankerfest. Liquidity-Risk-Befund ankert APH-FLAG-Logik (Score-basierter Stopp-Trigger bei Funding-Stress). Kein active-scoring — DEFCON ist Long-Only, keine Faktor-Portfolio-Konstruktion."
related: "[[QMJ-Faktor]], [[Asness-Frazzini-Pedersen-2013-QMJ]], [[Buffetts-Alpha]], [[Factor-Investing-Framework]], [[Aghassi-2023-Fact-Fiction]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/Asness, Moskowitz, Pedersen (2013).pdf"
aliases:
  - "Asness Moskowitz Pedersen 2013"
  - "Value and Momentum Everywhere"
  - "VME"
---

# Asness, Moskowitz & Pedersen (2013) — Value and Momentum Everywhere

## Abstract (eigene Worte)

AMP studieren Value- und Momentum-Strategien gemeinsam über 8 Asset-Klassen (Individual Stocks US/UK/Europa/Japan, Country Equity Indices, Government Bonds, Currencies, Commodity Futures) über 1972-2011. Kern-Befunde:

1. **Value-Premium und Momentum-Premium existieren konsistent in jeder Asset-Klasse** — auch in Currencies, Bonds, Commodities (zu der Zeit neuartig)
2. **Strong common factor structure** — Value-Strategien sind global positiv-korreliert über sonst unverbundene Märkte; Momentum analog
3. **Value und Momentum sind negativ-korreliert** intra- und inter-Asset-Class — eine Combination ist deutlich näher an der Efficient Frontier als jede Strategie isoliert
4. **3-Faktor-Modell** (Global Market + Global Value + Global Momentum) erklärt Returns über Asset-Klassen hinweg + FF-US-Stock-Portfolios + Hedge-Fund-Indizes
5. **Funding-Liquidity-Risk** ist negativ korreliert mit Value, positiv mit Momentum — partial Erklärung für Existenz beider Premia
6. **Kombi-Premium ist immune gegen Funding-Liquidity-Risk** — Momentum-Liquidity-Long und Value-Liquidity-Short heben sich auf

Theoretische Implikation: behavioral und rational-asset-pricing-Modelle, die nur US-Equities erklären, sind ungenügend. Die globale Korrelations-Struktur deutet auf **common global risk factors** hin, von denen Funding-Liquidity einer ist.

## Drei Befunde mit DEFCON-Relevanz

### 1. Block-Gewichtung 50/20/10/10/10 (B7 Anker)

AMP zeigen: Value (Trailing-Bewertung) und Momentum (Technicals) sind **echte, persistente, kausal-erklärbare** Faktoren — nicht Anomalien. Block-Gewichtung 50% Fundamentals + 10% Technicals ist konsistent mit der relativen Faktor-Importance, die AMP empirisch zeigen. **Würde Momentum 0 Pt. bekommen, wäre das gegen AMP-Evidenz.** Würde es 30 Pt. bekommen, wäre das ohne AMP-Justification.

### 2. Value+Momentum-Komplementarität

DEFCON nutzt **beides**: Fundamentals-Block hat Value-Komponente (Fwd-P/E, P/FCF, FCF-Yield, ROIC-WACC-Spread); Technicals-Block hat Momentum-Komponente (200-MA-Distance, RelStärke vs. SPY). Die Block-Trennung ist AMP-konform — beide Faktoren werden separat erfasst, nicht in einer Composite-Note vermischt.

### 3. Funding-Liquidity-Risk ankert APH-FLAG-Logik

AMP zeigen: in Funding-Stress-Phasen (1998 LTCM, 2008 GFC) brechen Value-Long-Momentum-Short-Strategien zusammen. Das ist ein generelles Liquidity-Crowding-Phänomen. **APH-Score-basierter-FLAG (0€-Sparrate) bei Score <65 + DEFCON 2** = analoges Pattern: Wenn Quality-Position Stress sieht, ist das ein Funding-/Liquidity-Risk-Signal, nicht nur firma-spezifisches Problem. AMP gibt der defensiven Sparrate-Logik makro-Validation.

## Komplementarität zu QMJ + Buffetts Alpha

| Quelle | Faktor-Stack | Mapping zu DEFCON |
|---|---|---|
| **AMP 2013** (VME) | Mkt + Value + Momentum | 50/20/10/10/10 Block-Architektur |
| **AFP 2013** (QMJ) | Quality (4 Pillars) | Fundamentals + Moat dekomponiert |
| **FKP 2018** (Buffetts Alpha) | QMJ + BAB Float-Leverage + Value | Methodologie-Kombi, B5-Anker |

→ **Konvergente Methodik-Schichten**: Value/Momentum/Quality decken empirisch unabhängige Risk-Premium-Dimensionen ab, alle drei in DEFCON repräsentiert.

## DEFCON-Konsequenzen (kein Scoring-Change)

- **B7 Block-Gewichtung (50/20/10/10/10)** ist methodisch ankerfest dank AMP-Evidenz
- **Trailing-P/E De-Priorisierung** (B2) ist nicht im Konflikt mit Value-Faktor-Existenz — DEFCON nutzt **Forward Value** (Fwd-P/E) als robusteren Proxy, was empirisch bei Gu/Kelly/Xiu (2020, B2) bestätigt wird
- **Momentum-Block 10 Pt.** ist ankerfest, nicht overweighted
- **Funding-Liquidity-Awareness:** In Stress-Phasen sollte FLAG-Bereitschaft erhöht sein (APH-Pattern)

## Backlinks

- [[QMJ-Faktor]] — komplementäre Methodik (Quality-Faktor)
- [[Asness-Frazzini-Pedersen-2013-QMJ]] — paralleles AQR-Paper, gleiches Jahr
- [[Buffetts-Alpha]] — Buffetts dekomponiertes Alpha als V+M+Q+BAB-Beispiel
- [[Factor-Investing-Framework]] — 4-Faktor-Kanon (B16 Anker)
- [[Aghassi-2023-Fact-Fiction]] — neuere AQR-Praxis-Anwendung
- [[DEFCON-System]] — Block-Gewichtung 50/20/10/10/10
- [[Wissenschaftliche-Fundierung-DEFCON]] — Source-only-Quelle (anchors B7)
- [[Clifford S. Asness]], [[Tobias Moskowitz]], [[Lasse Heje Pedersen]] — Author-Entities
