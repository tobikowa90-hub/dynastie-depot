---
title: "Forest through the Trees: Building Cross-Sections of Stock Returns"
date: 2023
type: source
subtype: academic-paper
medium: paper
tags: [defcon, asset-pricing-trees, test-asset-construction, design-rejected, defcon-orthogonal, phase-d-3-reject]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3493458
venue: "SSRN Working Paper 3493458, August 2023 Version (orig. 2019); JoF (2025-pending)"
authors: "Svetlana Bryzgalova (LBS), Markus Pelger (Stanford MS&E), Jason Zhu (Stanford MS&E)"
status: design-rejected
triage_class: rejected-DEFCON-orthogonal
raw_path: "raw/papers/Bryzgalova, Pelger, Zhu (2020).pdf"
defcon_relevanz: "REJECT-Page (Phase-D-3 Vault-Inventarisierung 2026-05-10). AP-Trees sind Test-Asset-Konstruktion für Asset-Pricing-Modellvergleiche, NICHT Stock-Selection-Methodologie. Methode löst „welche Portfolios spannen den conditional SDF projiziert auf Stock-Returns?" — orthogonal zu DEFCON-Long-Only-Single-Stock-Picking. AP-Trees sind Long-Only-Managed-Portfolios (Median-Splits + SDF-Spanning-Pruning + Robust-MVE-Optimierung), nicht Long-Only-Single-Stock-Picker. OoS-Sharpe-Resultate (2-3x über Standard-Sorts) gelten für Long-Short-Portfolio-Konstruktionen. Latent-Wert: Methodologie-Argument „kombiniere Signal-Extraktion + Portfolio-Konstruktion in einem Schritt" + Test-Asset-Span-Argument für 2028-Review-Gate Backtest-Methodology-Roadmap. Wiedervorlage-Trigger: (a) DEFCON-ML-Migration, (b) 2028-Review-Gate Test-Asset-Span-Frage, (c) Long-Short-Erweiterung Trading-Universum."
sources: []
related:
  - "[[Chen-Pelger-Zhu-2019-Deep-Learning-Asset-Pricing]]"
  - "[[Barillas-Shanken-2015-Which-Alpha]]"
  - "[[Hou-Xue-Zhang-2015-q-Factor]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
  - "[[DEFCON-System]]"
  - "[[svetlana-bryzgalova]]"
  - "[[markus-pelger]]"
  - "[[jason-zhu]]"
created: 2026-05-10
updated: 2026-06-09
aliases:
  - "Bryzgalova Pelger Zhu 2020"
  - "Bryzgalova Pelger Zhu 2023"
  - "BPZ 2020"
  - "BPZ 2023"
  - "Forest through the Trees"
  - "AP-Trees"
---

# Bryzgalova, Pelger & Zhu (2023) — Forest through the Trees

> 🚫 **DESIGN-REJECTED (DEFCON-orthogonal):** Diese Page ist als Vault-Inventarisierung angelegt, KEIN aktiver DEFCON-Anker. Voll-PDF in `raw/papers/Bryzgalova, Pelger, Zhu (2020).pdf` vorhanden. Die Methode (AP-Trees: Asset-Pricing-Trees) ist methodisch beeindruckend, adressiert aber ein anderes Problem als DEFCON: Test-Asset-Konstruktion für Modellvergleiche, nicht Single-Stock-Picking.

## Abstract (eigene Worte, sekundär-zitiert)

Bryzgalova, Pelger und Zhu konstruieren **Asset-Pricing-Trees (AP-Trees)** — eine Decision-Tree-basierte Methode, die rekursive Median-Splits über Stock-Charakteristiken vornimmt, dann jeden Endknoten als Long-Only-Managed-Portfolio behandelt. Diese Portfolios werden via SDF-Spanning-Pruning reduziert und in eine Robust-MVE-Optimierung gegeben. Resultierende Test-Assets erlauben SDF-Approximation mit deutlich höherem OoS-Sharpe (2-3x über klassische Decile-Sortierungen) bei gleicher Anzahl Test-Assets.

## Warum REJECT für DEFCON

### Method-Problem-Mismatch

| Aspekt | DEFCON | AP-Trees |
|---|---|---|
| **Ziel** | Single-Stock-Long-Only-Selection mit Score | SDF-Approximation via Test-Asset-Konstruktion |
| **Output** | DEFCON-Score 0-100 pro Ticker | Mean-Variance-Efficient-Portfolio-Gewichte über Tree-Endknoten |
| **Universum** | 13 Satelliten-Stocks (manuelle Selektion + Watchlist) | gesamtes US-CRSP-Universum (~3.000+ Stocks) |
| **Konstruktions-Logik** | additiv-multiplikative Block-Aggregation (50/20/10/10/10) | binäre Median-Splits + Pruning |
| **Long-Only-Single-Stock vs Long-Only-Portfolio** | Single-Stock | Managed-Portfolio (Aggregation über Endknoten) |
| **OoS-Sharpe-Anwendbarkeit** | nicht direkt (Long-Only-Single-Stock-Sharpe ≠ Long-Short-MVE-Sharpe) | direkt im Long-Short-MVE-Frame |

→ **Verdikt:** AP-Trees lösen ein methodisch sauberes Problem (Test-Asset-Konstruktion), das DEFCON nicht hat. DEFCON ist nicht im Test-Asset-Konstruktions-Geschäft; DEFCON ist im Stock-Picking-Geschäft.

### Latente Werte für 2028-Review-Gate

- **Methodologie-Argument:** „Kombiniere Signal-Extraktion + Portfolio-Konstruktion in einem Schritt" — wenn DEFCON jemals von Score-System auf Portfolio-Optimierung migriert (außerhalb Single-User-Scope), wäre AP-Trees als methodischer Anker relevant.
- **Test-Asset-Span-Argument:** Bei DEFCON-Block-Re-Gewichtung-Diskussion (Barillas/Shanken-Logik aktiviert) könnten AP-Trees-konstruierte Test-Assets methodisch saubere Span-Tests liefern.

## Wiedervorlage-Trigger

1. **DEFCON-ML-Migration** (eigene Migration-Session, nicht Phase-D)
2. **2028-Review-Gate Test-Asset-Span-Frage** (komplementär zu Barillas/Shanken-Aktivierung)
3. **Long-Short-Erweiterung Trading-Universum** (außerhalb DEFCON-v3.7-Scope)

Bei jedem dieser Trigger: REJECT-Status auf `deferred-stub` oder `design-context` revidieren + Voll-Read durchführen + Migration-Session-Plan.

## Beziehung zu anderen DEFCON-Layern

| Bezug | Anknüpfung |
|---|---|
| **CPZ-2019/2023** | gleicher Author-Cluster (Pelger, Zhu); CPZ ist DL-SDF-Approximation, BPZ ist Tree-basierte Test-Asset-Konstruktion — komplementär aber beide DEFCON-orthogonal |
| **B-S 2015 (`Which Alpha?`)** | Barillas/Shanken-Logik adressiert: Test-Asset-Wahl ist konventionell, nicht methodisch; BPZ widerspricht implizit (Tree-konstruierte Test-Assets sind systematisch besser als Decile-Sortierungen) — methodische Spannung in der Literatur |
| **Hou-Xue-Zhang 2015 q-Factor** | linearer Standard-Vergleichsbenchmark für BPZ-OoS-Sharpe |

## Limitationen (für künftige Re-Aktivierung)

- **Tree-Pruning ist hyperparametersensitiv:** Robustness der OoS-Sharpe-Resultate über alternative Pruning-Schwellen offen.
- **MVE-Optimierung sample-fitting-anfällig:** Robust-MVE adressiert das partiell, aber Single-User-Replikation schwierig.
- **Long-Only-Managed-Portfolio-Gewichte können extrem werden:** in Praxis tail-Risiko-Behandlung erforderlich.

## Backlinks

- [[Chen-Pelger-Zhu-2019-Deep-Learning-Asset-Pricing]] — Author-Cluster-Folge-/Schwester-Paper
- [[Barillas-Shanken-2015-Which-Alpha]] — methodische Spannung in der Literatur
- [[Hou-Xue-Zhang-2015-q-Factor]] — linearer Standard-Vergleichsbenchmark
- [[Wissenschaftliche-Fundierung-DEFCON]] — Phase-D Reject-Inventarisiert
- [[DEFCON-System]] — Method-Problem-Mismatch-Begründung
- [[svetlana-bryzgalova]], [[markus-pelger]], [[jason-zhu]] — Author-Entities
