---
name: quick-screener
description: >
  Schnell-Screener (Stufe 0) fuer das Dynastie-Depot. Filtert Ticker mit drei
  harten Kriterien (P/FCF, ROIC, Moat-Proxy) und gibt ein Ampel-Ergebnis
  (Gruen/Gelb/Rot) zurueck — bevor eine aufwaendige DEFCON-Analyse gestartet wird.
  Verwende diesen Skill IMMER wenn der User einen neuen Ticker pruefen will
  ("Screen mal X", "Lohnt sich Y?", "Ist Z was fuer uns?"), die Watchlist
  durchfiltern moechte, oder nach einem schnellen Qualitaetscheck fragt.
  Trigger-Woerter: Screen, Screener, Vorfilter, Quick-Check, Ampel, Watchlist
  durchlaufen, Ticker pruefen, "passt X ins Depot?", "lohnt sich", Erstcheck,
  Stufe 0, Batch-Screen. Auch bei Ersatzbank-Kandidaten oder "keine Zuteilung"-
  Tickern diesen Skill zuerst verwenden. Bei Unsicherheit: lieber aktivieren.
---

# Quick-Screener — Stufe 0 des Dynastie-Depot Analyse-Frameworks

**Zweck:** Schnelle Vorqualifikation von Tickern, bevor Zeit und Tokens in eine
vollstaendige DEFCON-Analyse investiert werden. Der Screener beantwortet genau
eine Frage: *Rechtfertigt dieser Ticker eine tiefere Analyse?*

**Sprache:** Deutsch bevorzugt. Englische Fachbegriffe (P/FCF, ROIC, Wide Moat)
bleiben auf Englisch — das sind Standardbegriffe im Finanzkontext.

---

## Pipeline-Einordnung

```
Stufe 0: QUICK-SCREENER (dieser Skill) → Gruen / Gelb / Rot
  ↓ nur Gruen
Stufe 1: ~~generate-stock-reports~~ (entfernt 08.04.2026 — Qualitative
         Vorab-Recherche erfolgt jetzt direkt via WebSearch in Stufe 2)
Stufe 2: !Analysiere → DEFCON 100-Punkte-Scoring
  ↓ nur Score >= 80 + kein FLAG
Stufe 3: !CAPEX-FCF-ANALYSIS → Excel-Dokument
```

Der Screener ist bewusst simpel gehalten — drei Filter, klares Ergebnis, keine
Grauzone. Komplexitaet gehoert in Stufe 2 (DEFCON), nicht hier.

---

## Dateien in diesem Skill

| Datei | Wann lesen |
|-------|------------|
| `SKILL.md` (diese Datei) | Immer — Logik, Workflows, Regeln |
| `references/thresholds.md` | Bei jeder Screening-Ausfuehrung — Schwellenwerte, Ausnahmen |
| `scripts/screen.py` | Bei CSV-Import oder Template-Erstellung — ausfuehren, nicht lesen |

---

## WORKFLOW 1: Einzel-Screening

Wenn der User einen einzelnen Ticker screenen will (z.B. "Screen mal FICO",
"Passt RACE ins Depot?", "Quick-Check SPGI"):

### Schritt 1: Daten beschaffen

Suche per Web Search nach diesen drei Metriken fuer den Ticker. Verwende
**mindestens zwei unabhaengige Quellen** pro Metrik, um Datenqualitaet
sicherzustellen.

1. **P/FCF** (Price-to-Free-Cash-Flow, Trailing oder Forward)
   - Primaer: StockAnalysis.com, AlphaSpread, GuruFocus
   - Fallback: Yahoo Finance (Operating Cash Flow - CapEx, dann Marktkapitalisierung / FCF)

2. **ROIC** (Return on Invested Capital)
   - Primaer: GuruFocus, AlphaSpread
   - Fallback: berechnen aus NOPAT / Invested Capital

3. **Moat-Proxy** (nur wenn kein Morningstar Wide-Moat-Rating verfuegbar):
   - **Gross Margin** (Bruttomarge): StockAnalysis, SimplyWallSt
   - **Revenue CAGR 5Y**: StockAnalysis, Macrotrends

Falls ein **Morningstar Wide-Moat-Rating** verfuegbar ist, ersetzt dieses den
Moat-Proxy komplett (Wide = Gruen, Narrow = Gelb, None = Rot).

### Schritt 2: Datenverifikation

Bevor die Schwellenwerte angewendet werden, pruefe die gesammelten Daten auf
Plausibilitaet. Web-Daten koennen veraltet, fehlerhaft oder inkonsistent sein —
der Screener muss das erkennen und transparent machen.

**Plausibilitaetschecks:**

- **Quellen-Divergenz:** Wenn zwei Quellen fuer dieselbe Metrik um mehr als 20%
  voneinander abweichen, ist das ein Warnsignal. Beispiel: GuruFocus zeigt
  P/FCF = 30, AlphaSpread zeigt P/FCF = 42 → Divergenz melden.

- **Fehlende Daten:** Wenn eine Metrik bei keiner Quelle gefunden wird, nicht
  raten oder schaetzen. Stattdessen als "n.v." markieren und den User informieren.

- **Veraltete Daten:** Wenn die gefundenen Zahlen aelter als 6 Monate sind
  (z.B. basierend auf einem Geschaeftsjahr das > 2 Quartale zurueckliegt),
  als "veraltet" kennzeichnen.

- **Negative/unplausible Werte:** Negativer FCF, ROIC > 100%, Gross Margin > 95%
  bei Nicht-Software-Unternehmen — solche Ausreisser explizit flaggen.

**Wenn ein Verifikationsproblem auftritt:**

Zeige dem User einen Warnblock im Output:

```
### ⚠ Datenverifikation
| Metrik | Quelle A | Quelle B | Abweichung | Status |
|--------|----------|----------|------------|--------|
| P/FCF | 30.2 (GuruFocus) | 42.1 (AlphaSpread) | 39% | ⚠ DIVERGENZ |
| ROIC | 28.5% (GuruFocus) | 27.1% (AlphaSpread) | 5% | ✓ OK |

**Empfehlung:** P/FCF-Wert manuell pruefen. Moegliche Ursachen: unterschiedliche
Berechnungszeitraeume (TTM vs. Forward), Sondereffekte im FCF.
→ Welchen Wert soll ich verwenden? [30.2 / 42.1 / eigener Wert]
```

Wenn kein Verifikationsproblem auftritt, diesen Block weglassen — er soll nur
bei tatsaechlichen Diskrepanzen erscheinen, nicht als Pflichtfeld.

Der User kann daraufhin:
- Einen der gefundenen Werte bestaetigen
- Einen eigenen Wert angeben (z.B. aus eigenem Screener-Export)
- Oder den Screener mit dem konservativeren Wert fortfahren lassen (Default)

**Default bei Divergenz ohne User-Input:** Verwende den konservativeren Wert
(den, der naeher an einer Abstufung liegt — also den hoeheren P/FCF oder den
niedrigeren ROIC). Das ist konsistent mit der Regel "im Zweifel strenger".

### Schritt 3: Schwellenwerte anwenden

Lies `references/thresholds.md` fuer die aktuellen Schwellenwerte und Ausnahmen.
Pruefe den Ticker gegen alle drei Filter und bestimme die Einzelampel pro Filter.

### Schritt 4: Gesamtampel bestimmen

Die Gesamtampel folgt dieser Logik:

- **GRUEN** = Alle drei Filter gruen ODER maximal einer gelb (Rest gruen)
- **GELB** = Zwei Filter gelb (kein Rot) ODER genau ein Filter gelb mit Grenzwert
- **ROT** = Mindestens ein Filter rot

Ausnahmeregel: Ticker auf der `screener_exceptions`-Liste in config.yaml
(z.B. Versicherungen/Holdings) verwenden angepasste Schwellenwerte —
siehe thresholds.md.

### Schritt 5: Ergebnis ausgeben

Verwende exakt dieses Format:

```
## Quick-Screen: [TICKER] — [FIRMENNAME]
**Datum:** [TT.MM.JJJJ] | **Kurs:** $[XXX] [web:Quelle]

| Filter | Wert | Schwelle | Ampel |
|--------|------|----------|-------|
| P/FCF | [XX.X] | ≤ 35 🟢 / ≤ 45 🟡 | 🟢 / 🟡 / 🔴 |
| ROIC | [XX.X%] | ≥ 15% 🟢 / ≥ 12% 🟡 | 🟢 / 🟡 / 🔴 |
| Moat-Proxy | GM [XX%], CAGR [XX%] | GM>40% + CAGR>8% | 🟢 / 🟡 / 🔴 |

### Ergebnis: [AMPEL-EMOJI] [GRUEN/GELB/ROT]
[1-2 Saetze Begruendung — warum diese Ampel, was ist der ausschlaggebende Faktor]

### Naechster Schritt
[Empfehlung basierend auf Ampel — siehe unten]

Quellen: [Links zu allen verwendeten Datenquellen]
```

**Empfehlungen nach Ampel:**

- 🟢 GRUEN: *"→ `!Analysiere [TICKER]` fuer vollstaendige DEFCON-Bewertung empfohlen"*
- 🟡 GELB: *"→ Watchlist. Re-Screen bei: [konkreter Katalysator, z.B. 'Earnings Q2', 'P/FCF < 35']"*
- 🔴 ROT: *"→ Aussortiert. Grund: [konkreter Mangel]. Re-Screen bei: [was sich aendern muesste]"*

### Schritt 6: Config aktualisieren

Nach dem Screening:

- **GRUEN:** Wenn der Ticker noch nicht in der Watchlist der `config.yaml` steht,
  schlage vor ihn mit Status "Screen bestanden — DEFCON pending" einzutragen.
- **GELB:** Schlage Watchlist-Eintrag vor mit Status "Beobachtung" und dem
  konkreten Re-Screen-Trigger.
- **ROT:** Kein Config-Update. Nur im Gespraech dokumentieren.

Fuehre Config-Updates nie automatisch aus — schlage sie vor und warte auf
Bestaetigung des Users.

---

## WORKFLOW 2: Batch-Screening (Watchlist-Durchlauf)

Wenn der User die gesamte Watchlist, Ersatzbank oder "keine Zuteilung"-Liste
screenen will (z.B. "Screen die Watchlist", "Batch-Check Ersatzbank",
"Lauf mal alle durch"):

### Modus A: CSV-Import (bevorzugt fuer Batch)

CSV ist der bevorzugte Modus fuer Batch-Screenings — er ist schneller,
reproduzierbar und erlaubt dem User die volle Kontrolle ueber die Datenqualitaet.

**CSV-Template erstellen:**
Wenn der User noch keine CSV hat, erstelle ein vorausgefuelltes Template:

```bash
python scripts/screen.py --yaml [pfad/config.yaml] --generate-template [output.csv]
```

Das generiert eine CSV mit allen Tickern aus der config.yaml und leeren
Spalten fuer die Metriken. Der User fuellt die Werte aus seinen bevorzugten
Quellen (SimplyWallSt, TraderFox, etc.) ein und gibt die CSV zurueck.

**CSV verarbeiten:**

```bash
python scripts/screen.py --csv [input.csv] --exceptions BRK.B,MKL,FFH.TO
```

Erwartete Spalten (flexibel — Script sucht nach passenden Headern):
- Ticker / Symbol
- P/FCF (oder Price-to-Free-Cash-Flow)
- ROIC (oder Return on Invested Capital)
- Gross Margin (oder Bruttomarge)
- Revenue CAGR 5Y (oder Umsatzwachstum)
- Optional: Morningstar Moat, Price/Book, Combined Ratio, Float Growth

Wenn Spalten fehlen, meldet das Script sie explizit. Biete dem User an,
die fehlenden Werte per Web-Search nachzuschlagen.

**Ablauf bei CSV-Import:**
1. CSV einlesen und validieren (fehlende Spalten? leere Werte?)
2. Schwellenwerte anwenden (via screen.py)
3. Zusammenfassungstabelle ausgeben
4. Config-Updates fuer gruene/gelbe Ticker vorschlagen

### Modus B: Web-Search (fuer Einzel-Screenings oder wenn keine CSV vorhanden)

1. Lies `config.yaml` und extrahiere alle relevanten Ticker:
   - `watchlist[]` (immer)
   - `keine_zuteilung[]` (wenn User das anfragt)
   - Ersatzbank-Ticker aus `satelliten[].ersatz` (wenn User das anfragt)

2. Fuehre fuer jeden Ticker Workflow 1 (Schritt 1-5) aus.
   Hinweis: Bei >5 Tickern den User fragen ob er lieber eine CSV vorbereiten will —
   Web-Search fuer viele Ticker dauert lang und verbraucht Tokens.

3. Erstelle eine Zusammenfassungstabelle am Ende (siehe Format unten).

4. Schlage Config-Updates fuer alle gruenen und gelben Ticker gesammelt vor.

### Batch-Ergebnis-Format

Sortiere nach Ampel (Gruen oben, Rot unten):

```
## Batch-Screen — [Datum] | [Anzahl] Ticker

### 🟢 DEFCON-Analyse empfohlen
| Ticker | Name | P/FCF | ROIC | Moat | Naechster Schritt |
|--------|------|-------|------|------|-------------------|
| MSCI | MSCI Inc | 28.6 | 27.8% | Wide | → !Analysiere MSCI |

### 🟡 Watchlist / Beobachtung
| Ticker | Name | P/FCF | ROIC | Moat | Re-Screen-Trigger |
|--------|------|-------|------|------|-------------------|
| SNPS | Synopsys | 40.2 | 22.0% | GM 82% / CAGR 15% | P/FCF < 35 |

### 🔴 Aussortiert
| Ticker | Name | P/FCF | ROIC | Moat | Grund |
|--------|------|-------|------|------|-------|
| PEGA | Pegasystems | 35.0 | 7.9% | GM 72% / CAGR 10% | ROIC < 12% |

### Zusammenfassung
🟢 [X] Ticker → DEFCON | 🟡 [X] Ticker → Watchlist | 🔴 [X] Ticker → Aussortiert

### ⚠ Datenhinweise (falls vorhanden)
[Ticker mit Verifikationsproblemen, fehlenden Daten, veralteten Werten]
```

---

## Sonderregeln

### Morningstar-Rating verfuegbar
Wenn ein Morningstar Wide/Narrow/None-Rating per Web-Search gefunden wird, ersetzt
es den Moat-Proxy (Gross Margin + Revenue CAGR) komplett:
- Wide Moat → GRUEN
- Narrow Moat → GELB
- No Moat → ROT

### Screener-Exceptions (Float-basierte Modelle)
Ticker auf der `screener_exceptions`-Liste in config.yaml (z.B. BRK, MKL, FFH)
haben strukturell andere Cashflow-Profile. Fuer diese gilt:
- P/FCF-Filter wird durch **Price/Book < 1.5** ersetzt
- ROIC-Filter wird durch **Combined Ratio < 100%** oder **Float Growth > 5%** ersetzt
- Moat-Proxy bleibt unveraendert

Begruendung: Versicherungen/Holdings generieren Wert ueber Float-Wachstum und
Underwriting-Profit, nicht ueber klassischen FCF. Ein strikter P/FCF-Filter wuerde
sie systematisch benachteiligen — das widerspricht dem bestehenden DEFCON-System,
das diese Sonderregel bereits anerkennt.

### FLAG-Ticker
Ticker mit aktivem FLAG in config.yaml werden beim Screening mit einem Warnhinweis
versehen: *"⚠ FLAG aktiv: [Grund]. Screen-Ergebnis unabhaengig vom FLAG."*
Der Screener hebt kein FLAG auf und setzt keins — das ist Aufgabe des DEFCON-Systems.

---

## Verhaltensregeln

1. **Quellenpflicht:** Jede Metrik mit Web-Quelle belegen. Kein Raten, kein Schaetzen.
2. **Datenverifikation:** Bei Quellen-Divergenz >20% den User informieren und
   nachsteuern lassen. Transparenz ueber Datenqualitaet ist wichtiger als Speed.
3. **Speed over Depth:** Der Screener soll schnell sein — drei Metriken, klare Antwort.
   Keine ausfuehrliche Analyse, keine Value-Legends, kein Bull/Bear-Case.
4. **Konservativ bei Grenzfaellen:** Im Zweifel eine Stufe strenger (Gelb statt Gruen,
   Rot statt Gelb). Bei Divergenz den konservativeren Wert verwenden.
5. **Keine Anlageberatung:** Der Screener filtert — die Entscheidung trifft der User.
6. **Config-Vorschlaege, keine Auto-Edits:** Aenderungen an config.yaml immer erst
   vorschlagen und auf Bestaetigung warten.
7. **Deutsch bevorzugt:** Output auf Deutsch, Fachbegriffe auf Englisch.
   Englisch ist akzeptabel wenn der User auf Englisch fragt.
