---
title: "Buffett-Faktorlogik (AQR)"
type: concept
tags: [defcon, buffett, faktor, qualitaet, cheap-safe-quality, qmj, bab]
source: "[[Buffetts-Alpha]]"
related: "[[QMJ-Faktor]], [[Moat-Taxonomie-Morningstar]], [[DEFCON-System]], [[BRKB]], [[Wissenschaftliche-Fundierung-DEFCON]]"
defcon_block: "Fundamentals + Moat (kombiniert)"
operative_regel: "PFLICHT: Float-Leverage (~1,6x) nicht replizierbar. Übertragbar: nur cheap + safe + high-quality als operativer Dreiklang."
---

# Buffett-Faktorlogik (AQR)

## Definition
Frazzini, Kabiller und Pedersen (AQR 2018) dekonstruieren Buffetts Alpha in drei replizierbare Faktoren: QMJ (Quality Minus Junk), BAB (Betting Against Beta) und Value. Ein vierter Faktor — Float-Leverage aus Versicherungsprämien (~1,6x) — ist für Privatanleger nicht replizierbar. Die übertragbare Essenz ist der Dreiklang: **cheap + safe + high-quality**.

## Wissenschaftliche Basis
Quelle: [[Buffetts-Alpha]] — Frazzini, Kabiller, Pedersen (AQR 2018)

Faktor-Zerlegung von Berkshires Outperformance:
| Faktor | Beschreibung | Replizierbar? |
|--------|-------------|---------------|
| QMJ | Quality Minus Junk — profitabel, wachsend, sicher, gut geführt | ✅ Ja |
| BAB | Betting Against Beta — niedrig-Beta-Aktien mit Leverage | ⚠️ Teilweise |
| Value | Günstige Bewertung (cheap) | ✅ Ja |
| Float-Leverage | ~1,6x Hebel aus Versicherungs-Float | ❌ Nicht replizierbar |

## PFLICHT-Regel (wörtlich, in jeder Datei dokumentiert)

> **"Float-Leverage (~1,6x) nicht replizierbar. Übertragbar: nur cheap + safe + high-quality."**
>
> — Frazzini, Kabiller, Pedersen (AQR 2018)

Diese Regel gilt bei:
- Jeder BRK.B-Analyse (Float-Modell dokumentieren, nicht als Vorlage nutzen)
- Diskussionen über Leverage-Strategien (Float ≠ Margin-Leverage)
- Qualitätsfaktor-Auswahl für Depot-Satelliten

## Operativer Dreiklang für DEFCON

| Komponente | DEFCON-Umsetzung |
|-----------|-----------------|
| **Cheap** | P/FCF ≤ 35, Fwd P/E ≤ 25, FCF Yield > 2% |
| **Safe** | Debt/EBITDA < 3, CapEx/OCF < 60%, stabile FCF |
| **High-Quality** | Wide Moat (Morningstar), ROIC > WACC, GM > 40% |

→ Alle drei Komponenten zusammen = DEFCON-4-Kandidat

## Verbindung zu BRK.B

[[BRKB]] ist die einzige direkte Entity-Instanz der Buffett-Faktorlogik im Depot:
- Screening-Exception: P/B statt P/FCF (Float-Modell)
- Float-Leverage dokumentieren, nicht auf andere Positionen übertragen
- cheap+safe+quality-Dreiklang dennoch anwendbar

## Backlinks
- [[Buffetts-Alpha]] — Primärquelle
- [[QMJ-Faktor]] — Quality-Komponente operationalisiert
- [[Moat-Taxonomie-Morningstar]] — quality = Wide Moat
- [[DEFCON-System]] — Dreiklang als Scoring-Fundament
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B5

## Moderne Faktor-Decomposition (Aghassi 2023)

Buffett-Alpha wird in akademischer Faktor-Sprache dekomponiert in:
- **QMJ (Quality)** — Buffett's "wonderful companies at fair price"
- **BAB (Betting against Beta)** — Low-Beta-Präferenz bei Leverage-Amplifikation
- **Defensive** — Versicherungs-Float als low-cost leverage

Aghassi 2023 validiert diese Faktoren als persistent. → [[Aghassi-2023-Fact-Fiction]], [[QMJ-Faktor]], [[Buffetts-Alpha]]
