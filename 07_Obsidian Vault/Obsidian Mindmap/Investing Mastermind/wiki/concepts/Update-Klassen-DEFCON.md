---
title: "Update-Klassen DEFCON (A/B/C/D)"
type: concept
tags: [defcon, update, prozess, token-effizienz, workflow]
updated: 2026-04-20
related: "[[DEFCON-System]], [[CapEx-FLAG]], [[Context-Hygiene]], [[Analyse-Pipeline]], [[Token-Mechanik]], [[Wissenschaftliche-Fundierung-DEFCON]], [[Regime-Aware-LLM-Failure-Modes]]"
defcon_block: "Update-Prozess"
operative_regel: "Klasse C (Event-getriggert) hat Vorrang — Insider >$20M oder Moat-Downgrade löst Sofortupdate aus, Score-Alter irrelevant."
---

# Update-Klassen DEFCON (A/B/C/D)

## Definition
Die Update-Klassen strukturieren, wann welche DEFCON-Metriken aktualisiert werden müssen. Ziel: Token-effiziente Sessions durch klare Trigger-Logik — kein permanentes Neuladen stabiler Daten, aber sofortige Reaktion auf kritische Events.

## Klassen-Tabelle

| Klasse | Trigger | Frequenz | Felder | Halbwertszeit |
|--------|---------|----------|--------|---------------|
| **A** | Quartalsweise | ~90 Tage | FCF, ROIC, Gross Margin, Debt/EBITDA | 18–33 Monate |
| **B** | Earnings-getriggert | 14 Tage nach Earnings | Alle Fundamentals, Score, Guidance, Fwd P/E | 60% Verfall Monat 1 post-Earnings |
| **C** | Event-getriggert | Sofort | Insider >$20M diskretionär, Moat-Downgrade, Makro-Schock >50 Bps, FLAG-Auslösung | — |
| **D** | Monatlich | 1× pro Monat | Sentiment, Short Interest, Analyst-Drift | — |

## Klasse-C-Priorität (heilig)

Klasse-C-Events überschreiben alle anderen Klassen:
- **Insider >$20M diskretionär:** sofortige FLAG-Auslösung → Sparrate 0€
- **Moat-Downgrade Wide → Narrow:** sofortiger !Analysiere, score-unabhängig
- **Makro-Schock >50 Bps:** Tariff-Exposure-Prüfung aller Satelliten
- **FLAG-Auslösung:** immer sofort, unabhängig vom Score-Alter

## Token-Effizienz-Logik

| Frage | Antwort |
|-------|---------|
| Muss ich alle Metriken neu laden? | Nein — nur die jeweilige Klasse |
| Wann lohnt sich Klasse-A-Update? | Nur bei Quartalsabschluss oder expliziter Anfrage |
| Wann MUSS ich updaten? | Immer bei Klasse-C-Event |
| Was passiert bei überfälligem Klasse-B? | QuickCheck erzwingt !Analysiere (Score-Alter >180 Tage) |

## Backlinks
- [[DEFCON-System]] — Score-Verfallsregel greift auf Klasse B
- [[CapEx-FLAG]] — FLAG-Auslösung = Klasse-C-Event
- [[Analyse-Pipeline]] — Stufe-0/1/2-Logik parallel zu Update-Klassen
- [[Context-Hygiene]] — Klassen-Logik minimiert Token-Verbrauch

## Wissenschaftliche Fundierung: Faktor-Half-Life (Flint-Vermaak 2021)

Update-Klassen-Cadence wird durch Flint-Vermaak 2021 Half-Life-Tabelle gestützt:

| DEFCON-Block | Faktor-Analog | Half-Life | Unsere Cadence | Status |
|---|---|---|---|---|
| Fundamentals | Value | 3-4M | Earnings (~3M) | ✅ aligned |
| Moat/Quality | Quality | 4-5M | Earnings + Jahresanalyse | ✅ konservativ |
| Technicals | Momentum | 3M | Earnings + Monitor | ✅ aligned |
| **CapEx-FLAG** | **Investment** | **~1M** | Earnings (zu träge bei aktiven FLAGs) | ⚠️ §30 Monthly-Refresh |
| Insider | — | Real-time | OpenInsider | ✅ aligned |

→ [[Flint-Vermaak-2021-Decay]], [[Factor-Information-Decay]], INSTRUKTIONEN §30

## Klasse-C-Erweiterungs-Potenzial (Meta-Gate, aktuell nicht aktiv)

Zwei Befunde aus der 6-Paper-Ingest (20.04.2026) stehen als **konditionale Klasse-C-Erweiterungen** in der Status-Matrix, aktivieren aber keine neuen Trigger solange DEFCON v3.7 unverändert bleibt:

- **B17 (Flint-Vermaak 2021) — CapEx-Half-Life ~1M:** motiviert den §30-Monthly-Refresh (schon oben verzeichnet). Bei künftiger Aktivierung eines zweiten Investment-Faktors (z.B. R&D-Intensity-FLAG) würde der §30-Rhythmus auf Klasse C gehoben, nicht auf D.
- **B19 (Li-Kim-Cucuringu-Ma 2026 — Regime-Aware-LLM-Failure-Modes):** potenzieller Klasse-C-Trigger "Regime-Shift-Audit" bei abrupten Makro-Regime-Wechseln (Rate-Cut-Zyklus, Recession-Call, Tariff-Schock). Operationalisierung abhängig von Track 5b (FRED Macro-Regime-Filter) — vor Aktivierung bleibt B19 Meta-Gate-Status `active-audit` in der Status-Matrix.

**Status-Matrix (kanonische SSoT):** [[Wissenschaftliche-Fundierung-DEFCON#Status-Matrix (operative Aktivierungs-Klassifikation)]]
