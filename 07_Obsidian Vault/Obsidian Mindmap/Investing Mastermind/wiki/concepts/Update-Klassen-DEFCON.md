---
title: "Update-Klassen DEFCON (A/B/C/D)"
type: concept
tags: [defcon, update, prozess, token-effizienz, workflow]
related: "[[DEFCON-System]], [[CapEx-FLAG]], [[Context-Hygiene]], [[Analyse-Pipeline]], [[Token-Mechanik]]"
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
