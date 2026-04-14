---
title: "Chain-of-Thought Prompting"
type: concept
tags: [prompting, llm, reasoning, ki-methodik]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [llm-stock-rating, gpt-4, news-sentiment-analysis, ai-in-investment-analysis, defcon-system, analyse-pipeline, dynastie-depot-skill]
---

# Chain-of-Thought Prompting

Eine Prompting-Technik für LLMs, bei der das Modell aufgefordert wird, seinen Denkprozess **Schritt für Schritt explizit darzustellen**, bevor es eine finale Antwort oder Entscheidung ausgibt. Dies verbessert die Qualität und Nachvollziehbarkeit der Ausgaben erheblich — besonders bei komplexen Analyse-Aufgaben.

## Grundprinzip

Statt direkt "Bewerte diese Aktie" zu fragen, wird das LLM angewiesen:
1. Analysiere die vorliegenden Daten Schritt für Schritt
2. Begründe deine Einschätzung
3. Nenne Preis-Targets
4. Gib erst danach das Rating aus

## Varianten

### Standard CoT
LLM denkt laut nach und gibt dann die Antwort.

### Few-Shot CoT
Dem LLM wird ein vollständiges Beispiel (Input + Reasoning + Output) im Kontext gezeigt. Besonders effektiv bei strukturierten Aufgaben wie Aktienrating.

### Chain of Verification (CoVE)
Erweiterung: LLM prüft nach der Antwort spezifische Fakten. In [[LLMs for Equity Stock Ratings]] als Datumsprüfung implementiert — stellt sicher, dass das Modell die richtigen Zeithorizonte berechnet hat (Halluzinations-Check).

## Einsatz in Finanz-Analyse

Aus [[LLMs for Equity Stock Ratings]] (J.P. Morgan):
- LLM erklärt zuerst sein Reasoning zur Datenlage
- Nennt Preis-Targets für jeden Zeithorizont
- Gibt dann das 5-stufige Rating aus
- CoVE prüft, ob die Zieldaten korrekt berechnet wurden

**Vorteil:** Erhöhte Interpretierbarkeit. Man kann nachvollziehen, **warum** das Modell ein bestimmtes Rating vergibt — wichtig für eigene Investment-Entscheidungen.

## Warum CoT für Investmentanalyse wichtig ist

- **Fehler-Erkennung:** Fehlerhaftes Reasoning ist sichtbar und korrigierbar
- **Vertrauen:** Begründete Empfehlungen sind überzeugender als Blackbox-Outputs
- **Lernen:** Man versteht, welche Faktoren das Modell für wichtig hält
- **Prompt-Optimierung:** Reasoning zeigt, welche Daten das Modell tatsächlich nutzt

## Best Practices

1. Instruktion: "Denke Schritt für Schritt" oder "Analysiere zuerst, dann entscheide"
2. Few-Shot Beispiel mit vollständigem Reasoning im Kontext bereitstellen
3. Spezifische Ausgabestruktur vorgeben (z.B. "Begründung → Preis-Target → Rating")
4. CoVE für überprüfbare Fakten (Daten, Zahlen) einbauen

## Umsetzung im Dynastie-Depot

CoT ist das strukturelle Rückgrat des `!Analysiere`-Befehls im [[DEFCON-System]]:

| CoT-Schritt | DEFCON-Äquivalent |
|---|---|
| Daten lesen + kommentieren | Block-by-Block-Scoring (Fundamentals → Moat → Technicals → Insider → Sentiment) |
| Begründung vor Zahl | Jeder Punkt wird mit Datenbasis erklärt, nicht nur ausgegeben |
| CoVE / Verifikation | CapEx-FLAG-Prüfung als harte Override-Regel nach dem Score |
| Finales Rating | DEFCON-Stufe (4/3/2/1) + Sparrate |

Die [[Analyse-Pipeline]] (Stufe 0 → 2 → Entscheidung) folgt demselben Prinzip: erst filtern, dann begründen, dann entscheiden — kein Blackbox-Output.

## Verbundene Seiten

- [[LLMs for Equity Stock Ratings]] · [[LLM-Based Stock Rating]] · [[GPT-4]] · [[AI in Investment Analysis]]
- [[DEFCON-System]] · [[Analyse-Pipeline]] · [[dynastie-depot-skill]]
