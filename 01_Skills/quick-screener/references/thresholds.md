Quick-Screener Schwellenwerte (v1.1 – 03.04.2026)
Dieses Dokument definiert alle Schwellenwerte zentral. Änderungen hier wirken
sich auf alle Screening-Durchläufe aus.

Standard-Filter
1. P/FCF (Price-to-Free-Cash-Flow)

Ampel
Schwelle
Interpretation
GRUEN
<= 35
Faire bis günstige Bewertung relativ zum Cashflow
GELB
35.1 – 45
Teuer, aber bei starkem Wachstum noch vertretbar
ROT
> 45 oder negativ/n.a.
Zu teuer oder kein positiver FCF


Hinweis: Trailing P/FCF bevorzugt. Forward P/FCF nur wenn TTM nicht 
verfügbar, dann explizit kennzeichnen als "(fwd)".
⚠️ Ausnahme Kurs Crash-Korrektur (neu, v1.1):
Wenn Kurs >30% unter ATH: TTM-P/FCF ist systematisch verzerrt (künstlich 
billig). In diesem Fall Forward P/FCF als primäre Scoring-Basis.
TTM-Wert nur als Kontext Referenz dokumentieren.
Konsistenz mit sources.md v2.4 Regel: "TTM-Verzerrung bei Kurscrash".
2. ROIC (Return on Invested Capital)

Ampel
Schwelle
Interpretation
GRUEN
\>= 15%
Starke Kapitalrendite, deutlich ueber Kapitalkosten
GELB
12% – 14.9%
Akzeptabel, aber nicht ueberzeugend
ROT
\< 12%
Kapitalallokation fragwuerdig

Hinweis: Letzte 12 Monate (TTM) bevorzugt. Bei zyklischen Unternehmen den 3-Jahres-Durchschnitt verwenden und kennzeichnen.

3. Moat-Proxy
**Standard-Variante** (wenn kein Morningstar-Rating verfügbar):

Ampel
Gross Margin
Revenue CAGR 5Y
Bedingung
GRUEN
> 40%
> 8%
Beide erfuellt
GELB
35–40% ODER
5–8%
Genau ein Kriterium knapp verfehlt
ROT
< 35%
< 5%
Mindestens eines deutlich verfehlt


**Morningstar-Variante** (ersetzt den Proxy komplett wenn verfügbar):

Ampel
Morningstar Moat
GRUEN
Wide Moat
GELB
Narrow Moat
ROT
No Moat / None


---

Gesamtampel-Logik

Die Einzel Ampeln werden wie folgt zur Gesamt Ampel aggregiert:

Kombination
Gesamt
3x Gruen
 GRUEN
2x Gruen + 1x Gelb
 GRUEN
1x Gruen + 2x Gelb
 GELB
3x Gelb
 GELB
Mindestens 1x Rot
 ROT



Keine Ausnahme: Ein einzelnes Rot führt immer zur Gesamt Ampel Rot.

Begründung: Der Screener ist ein harter Vorfilter. Wenn ein Ticker bei einem

der drei Kernkriterien versagt, sollte er die DEFCON-Analyse nicht erreichen.
---
Screener-Exceptions

Für bestimmte Geschäftsmodelle passen die Standard-Filter nicht. Diese Ticker

verwenden angepasste Metriken:

Versicherungen / Holdings / Float-basierte Modelle

Betrifft: BRK, BRK.B, MKL, FFH, FFH.TO (konfigurierbar in config.yaml unter
`screener_exceptions`)

Discount-Retail / Membership-Modelle

Betrifft: COST (konfigurierbar in config.md unter `screener_exceptions`)

Kennzahl
Schwellenwert
Begründung/Anmerkung
P/FCF
≤ 55 🟢 / 55–65 🟡 / > 65 🔴
COST reinvestiert aggressiv in Expansion; P/FCF strukturell höher als bei Software-Moats
ROIC
Unverändert (≥ 15% 🟢)
ROIC ~25%+ bestätigt Kapitaleffizienz trotz Niedrigmargen
Moat-Proxy
GM-Filter deaktiviert; nur CAGR > 8% zählt
Gross Margin ~13% ist Geschäftsmodell-bedingt (Selbstkostenpreis + Membership-Fee). Moat entsteht über Membership-Loyalität und Skaleneffekte, nicht über Rohmargen



Begründung: Costcos Wert liegt im Membership-Flywheel (~93% Renewal Rate) und der
Preismacht gegenüber Lieferanten – nicht in der Bruttomarge. Ein strikter GM-Filter
würde das Modell systematisch missverstehen. ROIC und CAGR bleiben als valide Filter.


Filter
Ersatz-Metrik
Grün 🟢
Gelb 🟡
Rot 🔴
P/FCF
Price/Book
<= 1.3
1.3 – 1.5
> 1.5
ROIC
Combined Ratio ODER Float Growth
CR < 95% oder FG > 8%
CR 95-100% oder FG 5-8%
CR > 100% und FG < 5%
Moat-Proxy
Unveraendert
Standard
Standard
Standard



Begründung: Versicherungen generieren Wert ueber Float-Wachstum und
Underwriting-Profit. Ihr P/FCF ist strukturell hoch weil Reserve Änderungen
den FCF verzerren. Price/Book ist der branchenübliche Bewertungsmaßstab.
---

 Kalibrierungsanker

Zum Abgleich — so sollten bekannte Ticker abschneiden:

Ticker
P/FCF
ROIC
Moat-Proxy
Erwartete Ampel
AVGO
~30
 ~30%+
GM>70%, CAGR>15%
 GRUEN
COST
~55
 ~25%+
GM Exception (Membership-Modell)
 GRUEN (mit Exception-Regeln)
MSFT
~35
 ~30%+
Wide Moat
 GRUEN
GOOGL
~25
 ~25%+
Wide Moat, aber FLAG
 GRUEN (FLAG separat)



Hinweis: COST läuft über die aktiven Exception-Regeln (P/FCF ≤55 🟢, GM-Filter
deaktiviert, nur CAGR >8% zählt) und wird damit korrekt als GRUEN gewertet.
Die Standard-Schwellen (P/FCF ≤35, GM >40%) gelten für COST NICHT.
Im Batch-Screener (screen.py) muss COST manuell als Exception behandelt werden —
das Script kennt derzeit nur Versicherungs-/Holding-Ausnahmen (BRK.B, MKL, FFH.TO).
Beim Einzel-Screening per Web-Search die COST-Sonderregeln aus diesem Abschnitt anwenden.

