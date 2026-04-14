# 🔗 Quellen-Referenz – Dynastie-Depot v3.4

**Stand:** 06.04.2026 | **Version:** 2.7 | **Zweck:** Verbindliche Quellenmatrix für alle DEFCON-Analysen

Lies diese Datei bei jeder `!Analysiere`\- und `!CAPEX-FCF-ANALYSIS`\-Analyse. Die Quellen-Reihenfolge entspricht dem DEFCON v3.1 Workflow.

---

## ⚠️ Kritische Änderung gegenüber v1.0

**GuruFocus `/stock/[TICKER]/summary` ist JS-gerendert und nicht fetchbar.** Ausschliesslich `/term/[METRIK]/[TICKER]` verwenden – diese Seiten liefern vollstaendige, strukturierte Daten ohne Login. Siehe Pflicht-Batch unten.

**Morningstar** ist hinter einer Paywall und wird nicht mehr als Primaerquelle fuer Moat verwendet. GuruFocus `moat-score` ist der neue Standard.

---

## 🔬 Bewertung & Fundamentals

| Quelle | URL | Wofür |
| :---- | :---- | :---- |
| **AlphaSpread** | [https://alphaspread.com](https://alphaspread.com) | DCF Fair Value, Relative Valuation, Fwd PE/FCF |
| **Simply Wall St** | [https://simplywall.st](https://simplywall.st) | Snowflake, DCF, Insider, Debt-Check |
| **GuruFocus** | [https://gurufocus.com](https://gurufocus.com) | ROIC, Moat Score, FCF Yield, Insider (via term-pages) |
| **Macrotrends** | [https://macrotrends.net](https://macrotrends.net) | Historische FCF, CapEx, OCF (10-Jahres) |
| **Stock Analysis** | [https://stockanalysis.com](https://stockanalysis.com) | CapEx/OCF quarterly, Kennzahlen, Earnings |

---

## 🚀 GuruFocus Pflicht-Batch (\!Analysiere Start)

Diese 4 URLs werden bei jeder `!Analysiere`\-Analyse **gleichzeitig** abgerufen. Sie decken \~35 von 50 Fundamentals-Punkten \+ den kompletten Moat-Block ab.

| Metrik | URL-Muster | Liefert |
| :---- | :---- | :---- |
| **Moat Score** | `gurufocus.com/term/moat-score/[TICKER]` | 0–10 Skala \+ Wide/Narrow/None |
| **P/FCF (TTM)** | `gurufocus.com/term/price-to-free-cash-flow/[TICKER]` | Price-to-FCF TTM |
| **ROIC** | `gurufocus.com/term/roic/[TICKER]` | ROIC % TTM |
| **FCF Yield** | `gurufocus.com/term/fcf-yield/[TICKER]` | FCF Yield % |

**Erweiterter GuruFocus-Batch (bei Bedarf):**

| Metrik | URL-Muster | Liefert |
| :---- | :---- | :---- |
| **Gross Margin** | `gurufocus.com/term/gross-margin/[TICKER]` | GM % TTM |
| **Debt/EBITDA** | `gurufocus.com/term/debt-to-ebitda/[TICKER]` | Net Debt/EBITDA |
| **Revenue CAGR 3Y** | `gurufocus.com/term/revenue-growth-3y/[TICKER]` | Umsatzwachstum 3J |
| **Insider** | `gurufocus.com/insiders/[TICKER]` | Buy/Sell Transaktionen 90 Tage |

---

## 📊 Kurse, Technicals & Sentiment

| Quelle | URL | Wofür |
| :---- | :---- | :---- |
| **Yahoo Finance** | [https://finance.yahoo.com](https://finance.yahoo.com) | Live-Kurs, USD/EUR-Rate, Earnings Calendar |
| **TradingView** | [https://tradingview.com](https://tradingview.com) | RSI, MACD, MA-Lage, Chart-Analyse |
| **Finviz** | [https://finviz.com](https://finviz.com) | Screener, PE/FCF-Übersicht, Heatmap |
| **Zacks** | [https://zacks.com](https://zacks.com) | EPS-Revisionen, Analyst-Ratings |
| **Stock3** | [https://stock3.com](https://stock3.com) | Deutschsprachige Analyse, Technicals |

# ---

## 🦅 Insider & Institutional

| Quelle | URL | Wofür | Priorität |
| :---- | :---- | :---- | :---- |
| **Openinsider** | [https://openinsider.com/](https://openinsider.com/)\[TICKER\] | **10b5-1-FLAG-Prüfung** – Spalte „X"/„M" \= Plan vorhanden | ✅ Primär |
| **SEC EDGAR Form 4** | [https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany)\&CIK=\[TICKER\]\&type=4\&dateb=\&owner=include\&count=40 | Rohdaten aller Insider-Transaktionen | ✅ Primär |
| **GuruFocus Insider** | [gurufocus.com/insiders/](https://gurufocus.com/insiders/)\[TICKER | Buy/Sell-Saldo 90 Tage, Ownership % | Sekundär |
| **Fintel** | [https://fintel.io](https://fintel.io) | Institutional Ownership, Insider-Screening | Sekundär |

🚨 10b5-1 FLAG-Prüflogik (OpenInsider)Diese Prüfung ist **Pflicht** bei jedem Verkauf \>$20M in den letzten 90 Tagen.

| Spalte “X” / “M” | Bedeutung | FLAG? |
| :---- | :---- | :---- |
| **M** angezeigt | ✅ 10b5-1-Plan vorhanden – automatischer, vorher festgelegter Verkauf | 🟢 Kein FLAG |
| **Leer** | 🔴 Diskretionärer Verkauf – keine Planabsicherung bestätigt | 🚨 FLAG aktiv |

**Regel:** Verkauf \>$20M \+ kein „M" \+ innerhalb 90-Tage-Fenster \= **FLAG aktiv**, Sparrate einfrieren, unabhängig vom Score.  
\---

### \#\#\# 🔍 Form 4 Transaktions-Code Cheatsheet (SEC EDGAR)

Die 10b5-1-Prüfung gilt \*\*ausschließlich bei echten Verkäufen\*\*.   
Zuerst Code prüfen, dann erst 10b5-1-Box auswerten:

| Code | Bedeutung | 10b5-1 prüfen? | FLAG möglich? |
| ----- | ----- | ----- | ----- |
| **S** | Open-Market-Verkauf | ✅ Ja — Box prüfen | 🚨 Ja |
| **D** | Disposal (sonstige Übertragung) | ✅ Ja — Box prüfen | 🚨 Ja |
| **M** \+ **S** gleicher Tag \+ Option nahe Expiry | Cashless Exercise (erzwungen) | ❌ Nein | 🟢 Kein FLAG |
| **M** \+ Preis $0.00 | RSU-Vesting | ❌ Nein | 🟢 Kein FLAG |
| **A** | Acquisition (Grant, RSU, Zuteilung) | ❌ Nein | 🟢 Kein FLAG |
| **M** allein (Option Exercise, kein S) | Option ausgeübt, Aktien behalten | ❌ Nein | 🟢 Kein FLAG |

\*\*Cashless Exercise erkennen:\*\*  
Code M \+ Code S am gleichen Tag \+ Options-Expiry ≤ 30 Tage \= erzwungener Verkauf, kein Timing-Signal.  
Transaktionsvolumen trotzdem prüfen — bei \>$20M und kein 10b5-1-Plan → FLAG.

\---

### \#\#\# 🔍 OpenInsider Spalten-Cheatsheet

| Spalte | Inhalt | Relevanz |
| ----- | ----- | ----- |
| **X** | 10b5-1-Plan vorhanden | ✅ Kernprüfung — leer \= FLAG-Kandidat |
| **Trade Type** | P \= Purchase, S \= Sale, S-Auto \= 10b5-1-Sale | S ohne X \= 🚨 |
| **Value** | Transaktionswert in USD | \>$20M \= FLAG-Schwelle |
| **\#Shares** | Anzahl gehandelter Aktien | Kontext |
| **Own** | Ownership nach Trade (D/I) | D \= Direct \= stärker gewichtet |

\*\*Automatische Entlastung (kein FLAG trotz leerem X):\*\*  
\- Trade Type \*\*„S-Auto"\*\* \= automatischer 10b5-1-Verkauf → 🟢 Kein FLAG  
\- Trade Type \*\*„Option Ex."\*\* \+ gleicher Tag S \= Cashless Exercise → 🟢 Kein FLAG  
\- Value \*\*\< $20M\*\* \= unter FLAG-Schwelle → ⚠️ Negatives Signal, aber kein FLAG

\*\*Workflow OpenInsider:\*\*  
1\. Filtere auf letzte 90 Tage  
2\. Zeige nur „Sales" (Trade Type S)  
3\. Prüfe Spalte X → leer \+ Value \>$20M \= FLAG aktiv  
4\. Trade Type „S-Auto" → kein FLAG unabhängig von X

---

## 🏰 Moat & Qualität

| Quelle | URL | Wofür | Priorität |
| :---- | :---- | :---- | :---- |
| **GuruFocus Moat** | `gurufocus.com/term/moat-score/[TICKER]` | Moat Score 0–10 \+ Wide/Narrow/None | ✅ Primär |
| **Simply Wall St** | [https://simplywall.st](https://simplywall.st) | Moat-Einschätzung qualitativ | Sekundär |
| **Morningstar** | [https://morningstar.com](https://morningstar.com) | Wide/Narrow/None (Paywall) | Nur bei User-Zugang |
| **CB Insights** | [https://cbinsights.com](https://cbinsights.com) | Wettbewerbsanalyse, Marktstruktur | Kontextuell |

---

## 📋 Primärquellen (Pflicht für CapEx-FCF)

| Quelle | URL | Wofür |
| :---- | :---- | :---- |
| **SEC EDGAR** | [https://sec.gov/cgi-bin/browse-edgar](https://sec.gov/cgi-bin/browse-edgar) | 10-K, 10-Q direkt |
| **Investor Relations** | `[TICKER] investor relations` (Google-Suche) | Press Releases, Earnings PDFs |
| **EZB Wechselkurs** | [https://ecb.europa.eu/stats/policy\_and\_exchange\_rates](https://ecb.europa.eu/stats/policy_and_exchange_rates) | USD/EUR offizieller Referenzkurs |

---

## ⚡ Quick-Lookup nach Analyse-Schritt

Diese Tabelle definiert die verbindliche Quellen-Reihenfolge pro Scoring-Schritt. Primär zuerst abfragen. Sekundär nur bei fehlenden/widersprüchlichen Daten.

| \*\*Schritt\*\* | \*\*Primär\*\* | \*\*Sekundär\*\* |
| :---- | :---- | :---- |
| **\*\*Live-Kurs \+ Marktdaten\*\*** | Yahoo Finance | TradingView |
| **\*\*Fwd PE / DCF\*\*** | AlphaSpread | Simply Wall St |
| **\*\*P/FCF (TTM)\*\*** | GuruFocus term/price-to-free-cash-flow | StockAnalysis statistics |
| **\*\*ROIC\*\*** | GuruFocus term/roic | AlphaSpread |
| **\*\*FCF Yield\*\*** | GuruFocus term/fcf-yield | StockAnalysis |
| **\*\*Bilanz (Debt/EBITDA)\*\*** | GuruFocus term/debt-to-ebitda | Stock Analysis |
| **\*\*Gross Margin\*\*** | GuruFocus term/gross-margin | StockAnalysis |
| **\*\*Moat-Check\*\*** | GuruFocus term/moat-score | Simply Wall St |
| **\*\*Insider-Check (FLAG)\*\*** | OpenInsider (10b5-1-Spalte prüfen\!) | GuruFocus insiders / SEC EDGAR Form 4 |
| **\*\*Analyst-Konsensus \+ PTs\*\*** | Zacks | Yahoo Finance analysis |
| **\*\*CapEx / OCF quarterly\*\*** | StockAnalysis cash-flow-statement | Yahoo Finance cash-flow |
| **\*\*CapEx / OCF 5J-Historie\*\*** | Macrotrends | StockAnalysis |
| **\*\*10-K Primärquelle\*\*** | SEC EDGAR | IR-Website direkt |
| **\*\*USD/EUR Umrechnung\*\*** | Yahoo Finance (Echtzeit) | EZB (offiziell) |
| **\*\*SBC/Revenue\*\*** | GuruFocus term/sbc-to-revenue | StockAnalysis statistics |
| **\*\*Accruals Ratio\*\*** | StockAnalysis cash-flow-statement \+ balance-sheet (berechnet: NI-OCF/Assets) | — |
| **\*\*GM-Trend 3J\*\*** | Macrotrends gross-profit-margin | GuruFocus term/gross-margin |
| **\*\*Pricing Power\*\*** | Quartr TICKER (Transcript: "pricing", "price increase") | IR-Website Earnings Call |
| **\*\*Rel. Stärke 6M\*\*** | Finviz quote.ashx?t=TICKER → Performance-Tabelle 6M | — |
| **\*\*EPS Revisionen\*\*** | Zacks TICKER → Consensus EPS Revisions | Yahoo Finance analysis |
| **\*\*Tariff Exposure\*\*** | SEC EDGAR 10-K → "Geographic Revenue" | Quartr (Management Commentary Zölle) |

—

## ⚠️ Scoring-Protokoll: Kritische Datenanpassungen

#### 1\. TTM-Verzerrung bei Kurscrash (\>30% vom ATH)

* **Problem:** Wenn der Kurs \>30% unter dem All-Time High (ATH) liegt, sind TTM-Multiples (PFCF, FCF Yield, PE) künstlich billig und verzerren den Score nach oben.  
* **Regel:** **Forward-Metriken** (Fwd PE, Fwd P/FCF) sind die primäre Scoring-Basis.  
* **TTM-Werte:** Nur als Kontextreferenz dokumentieren, nicht zur Score-Berechnung verwenden.  
* **Quelle Forward-PFCF:** AlphaSpread (P/FCFE Forward) → GuruFocus (Fwd-Sektion).

#### 2\. GAAP vs. Non-GAAP Protokoll

* **Standard:** **GAAP-Metriken** für alle Score-Berechnungen (konservativ).  
* **Non-GAAP:** Nur als Kontextinformation in Klammern dokumentieren.  
* **Ausnahme:** Wenn die Non-GAAP-Differenz *ausschließlich* aus Amortisierung von Akquisitions-Goodwill besteht (z.B. AVGO nach VMware), kann Non-GAAP als Hauptmetrik mit explizitem Vermerk verwendet werden.  
* **Begründung:** Stock-Based Compensation (SBC) ist ein realer Kostenfaktor und darf *niemals* herausgerechnet werden. Amortisierung ist buchhalterisch, kein Cash-Abfluss.

#### 3\. Non-US Ticker Quellenregel

* **US-Ticker (NYSE/NASDAQ):**
  * **Primär:** Shibui Finance SQL (Technicals) + defeatbeta MCP (Fundamentals)
  * **Insider:** insider\_intel.py (SEC EDGAR Form 4 — automatisiert)
  * **Fallback:** GuruFocus/Macrotrends
* **Non-US-Ticker (ASML, RMS, SU):**
  * **Primär:** `eodhd_intel.py` (yfinance, EUR-Ticker) — vollstaendiger DEFCON-Block automatisiert
  * **Befehl:** `python eodhd_intel.py detail [TICKER]`
  * **Insider:** AFM (ASML) / AMF (RMS, SU) — manuell, keine Form-4-Pflicht
  * **Verifikation Valuation:** AlphaSpread `/par/[TICKER]` (Paris) oder `/ams/[TICKER]` (Amsterdam)
  * **Verifikation ROIC:** GuruFocus `term/roic/[TICKER]` (yfinance liefert nur Proxy)
* **Hinweis AlphaSpread:** Börsen-Prefix beachten: `/par` (Paris), `/ams` (Amsterdam), `/xet` (Xetra), `/nasdaq`, `/nyse`.

#### 4\. Insider Ownership Bewertungsskala

| Direct Ownership | Punkte | Bewertung |
| ----- | ----- | ----- |
| **\>5%** | 3/3 | CEO/Gründer-Alignment |
| **1% – 5%** | 2/3 | Signifikant |
| **0.1% – 1%** | 1/3 | Minimal |
| **\<0.1%** | 0/3 | Faktisch kein Skin in the Game |

* **Zählweise:** Nur **Direct (D)** Ownership zählt. Indirect (I) gibt max. 1/3 Punkt.

#### 5\. Fwd PE Quellen-Hierarchie bei Widerspruch

1. **AlphaSpread** (Relative Valuation Tab) — **Primär**  
2. **Yahoo Finance** (/analysis: Consensus EPS × aktueller Kurs) — **Sekundär**  
3. **Finviz** (Forward PE Zeile) — **Tertiär**  
* **Abweichung:** Bei \>15% Abweichung den konservativsten Wert verwenden \+ Abweichung dokumentieren.

#### 6\. Quarterly vs. Annual Daten

| Metrik / Zweck | Frequenz / Zeitraum | Quelle |
| ----- | ----- | ----- |
| **CapEx/OCF** für CapEx-FLAG-Prüfung | Quarterly (letzte 4Q annualisiert) | StockAnalysis |
| **CapEx/OCF** für historischen Trend | Annual (5–10 Jahre) | Macrotrends |
| **FCF** für DEFCON-Score | TTM Annual | GuruFocus |
| **FCF** für Forward-Bewertung | Nächstes volles Fiskaljahr | AlphaSpread/Consensus |

\-----

## \#\#\# 🔑 Goldene Regel (gilt immer, überall)

Bei widersprüchlichen Daten zwischen Quellen: konservativsten Wert   
verwenden und Abweichung explizit in der Analyse dokumentieren.  
SEC EDGAR \> GuruFocus \> Drittanbieter bei US-Tickern.

---

## 🔍 URL-Muster für Ticker-spezifische Abfragen

Ersetze `[TICKER]` durch das jeweilige Kürzel (z.B. COST, AVGO, MSFT).

**GuruFocus Term-Seiten (fetchbar, kein Login)**

| Bezeichnung | Link-Vorlage |
| :---: | :---: |
| Moat | `[https://www.gurufocus.com/term/moat-score/](https://www.gurufocus.com/term/moat-score/)[TICKER]` |
| P/FCF | `[https://www.gurufocus.com/term/price-to-free-cash-flow/](https://www.gurufocus.com/term/price-to-free-cash-flow/)[TICKER]` |
| ROIC | `[https://www.gurufocus.com/term/roic/](https://www.gurufocus.com/term/roic/)[TICKER]` |
| FCF Yield | `[https://www.gurufocus.com/term/fcf-yield/](https://www.gurufocus.com/term/fcf-yield/)[TICKER]` |
| Gross Margin (GM) | `[https://www.gurufocus.com/term/gross-margin/](https://www.gurufocus.com/term/gross-margin/)[TICKER]` |
| Debt to EBITDA | `[https://www.gurufocus.com/term/debt-to-ebitda/](https://www.gurufocus.com/term/debt-to-ebitda/)[TICKER]` |
| Revenue Growth 3Y (CAGR) | `[https://www.gurufocus.com/term/revenue-growth-3y/](https://www.gurufocus.com/term/revenue-growth-3y/)[TICKER]` |
| Insider Trades | `[https://www.gurufocus.com/insiders/](https://www.gurufocus.com/insiders/)[TICKER]` |

**❌ NICHT verwenden (JS-gerendert, nicht fetchbar)** `https://www.gurufocus.com/stock/](https://www.gurufocus.com/stock/)[TICKER]/summary`

**AlphaSpread (Börsen-Prefix beachten)**

| Bezeichnung | Link-Vorlage |
| ----- | :---: |
| US NASDAQ | `[https://alphaspread.com/security/nasdaq/](https://alphaspread.com/security/nasdaq/)[TICKER]` |
| US NYSE | `[https://alphaspread.com/security/nyse/](https://alphaspread.com/security/nyse/)[TICKER]` |
| EU Paris (z.B. SU, RMS) | `[https://alphaspread.com/security/par/](https://alphaspread.com/security/par/)[TICKER]` |
| EU Xetra | `[https://alphaspread.com/security/xet/](https://alphaspread.com/security/xet/)[TICKER]` |

**Weitere Quellen**

| Bezeichnung | Link-Vorlage |
| ----- | ----- |
| StockAnalysis (Cash Flow Statement, Quarterly) | `[https://stockanalysis.com/stocks/](https://stockanalysis.com/stocks/)[ticker]/financials/cash-flow-statement/?p=quarterly` |
| StockAnalysis (Statistics) | `[https://stockanalysis.com/stocks/](https://stockanalysis.com/stocks/)[ticker]/statistics/` |
| Macrotrends (Charts) | `[https://macrotrends.net/stocks/charts/](https://macrotrends.net/stocks/charts/)[TICKER]/` |
| Yahoo Finance (Quote) | `[https://finance.yahoo.com/quote/](https://finance.yahoo.com/quote/)[TICKER]/` |
| Yahoo Analysis | `[https://finance.yahoo.com/quote/](https://finance.yahoo.com/quote/)[TICKER]/analysis` |
| Finviz | `[https://finviz.com/quote.ashx?t=](https://finviz.com/quote.ashx?t=)[TICKER]` |
| Fintel | `[https://fintel.io/n/](https://fintel.io/n/)[TICKER]` |
| SEC EDGAR (10-K) | `[https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=)[TICKER]&type=10-K` |

---

*🦅 Bei widersprüchlichen Daten zwischen Quellen: konservativsten Wert verwenden und Abweichung in der Analyse dokumentieren.* *Version 2.7 – 06.04.2026 | Non-US Primärquelle → yfinance (eodhd_intel.py). OpenInsider → schneller Triage-Check (Spalte X + Trade Type + Value). SEC EDGAR Form 4 → forensische Verifikation bei Unklarheiten.*  
