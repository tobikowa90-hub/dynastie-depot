# Morning Briefing Remote Trigger — Prompt v2.2
**Trigger-ID:** `trig_01PyAVAxFpjbPkvXq7UrS2uG`
**Deployed:** 2026-04-17 (via Desktop App)
**Version:** v2.2 — STATE.md als zweite Kontext-Quelle + Format-Erweiterung

<!-- Wissenschaftlicher Kontext (19.04.2026): Briefing-Output ist Input für §18 Sync-Pflicht.
Die Faktortabelle-Einträge im Briefing werden eines Tages §29-Retrospective-Analyse speisen
(Bailey CSCV-Datenbasis). Point-in-Time-Disziplin daher kritisch. -->

## Changelog

### v2.2 (17.04.2026) — STATE.md Integration
- SCHRITT 2 aufgeteilt: 2a STATE.md (Sparraten, Watches, Trigger-Tabelle) + 2b Faktortabelle (Score-Details, Earnings)
- Neuer Abschnitt `--- AKTIVE WATCHES ---` nach FLAGS (aus STATE.md)
- Kurs-Tabelle: `Rate: [€]`-Spalte ergaenzt (volle Rate / halbe Rate / 0€ FLAG)
- `EARNINGS NAECHSTE 7 TAGE` → `NAECHSTE TRIGGER & EARNINGS (30 Tage)` (kombiniert aus STATE.md + Faktortabelle)
- WOCHENEND-MODUS: liest jetzt auch STATE.md, zeigt Watches
- HINWEIS: `RemoteTrigger update` kann events-Content nicht aendern — Prompt-Updates nur via Desktop App (Routines → Anweisungen-Feld)

### v2.1 (16.04.2026) — JSON-Nesting-Fix
- **ROOT CAUSE der leeren Outputs:** `parent_tool_use_id`, `session_id`, `type`, `uuid` waren faelschlich in `events[0].data.message` statt `events[0].data` genestet. API akzeptiert beides (HTTP 200), aber Runtime parsed nur die korrekte Variante.
- Prompt inhaltlich identisch mit v2, nur JSON-Struktur korrigiert.
- Verifiziert: Manueller Run in Desktop App produziert Output.

### v2 (15.04.2026 ~23:49 MESZ) — Content-Fixes (BROKEN — leere Outputs)
- SUNCOR-TRAP eliminiert: Shibui `code='SU'` = Suncor Energy. Schneider nur via Yahoo `SU.PA`.
- BERKSHIRE-GAP: BRK.B nicht in Shibui. Nur Yahoo `BRK-B`.
- HERMES-GAP: RMS nicht in Shibui. Nur Yahoo `RMS.PA`.
- GOOGL-Hallucination: Scope explizit auf 16 Symbole beschraenkt.
- Retry-Hell: Keine "versuche Varianten" Fallbacks.
- Table-Name: `stock_prices` → `stock_quotes`.
- Exchange-Fix: `g.code IN(...)` JOIN statt hardcoded `.EXCHANGE` Suffixe.
- Score-heute-Label statt "0,0%".
- Anti-Hallucination-Guard.
- 5 Ersatzbank explizit (vorher nur 3).

### v1 (14.04.2026) — Original
- Funktionierte, aber mit Hallucinations, falschem Tabellenname, fehlenden Symbolen, Retry-Loops.

## Known Limitations v2.2

1. **Yahoo 403:** BRK.B/RMS/SU-Kurse nicht verfuegbar aus Cloud-Umgebung. Yahoo Finance blockiert Datacenter-IPs. Zeigt ehrlich "n.v. (403)". defeatbeta hat BRK-B lokal aber ist kein Cloud-MCP.
2. **Push-Notifications:** Claude iOS App hat keinen Routines-Toggle. Feature wartet auf Anthropic-Update.
3. **`RemoteTrigger run` API:** Noop fuer Cron-Trigger. Manuell nur via Desktop App "Jetzt ausfuehren".
4. **Kein Delta fuer Yahoo-Symbole:** Auch wenn Yahoo funktionieren wuerde, waere nur latest price ohne historischen Ref-Close verfuegbar (V3-Feature: Yahoo time-series Parsing).

## API-Update-Regel (KRITISCH — aus Erfahrung gelernt)

RemoteTrigger `update` (POST) ersetzt das `ccr`-Objekt KOMPLETT. Kein JSON-Merge.
- Immer ALLE 3 Felder zusammen senden: `environment_id` + `session_context` + `events`
- Fehlende Felder werden auf Defaults zurueckgesetzt oder geloescht
- JSON-Nesting in events: `parent_tool_use_id`, `session_id`, `type`, `uuid` auf **data-Level**, NICHT in message

Korrekte Struktur:
```json
"events": [{
  "data": {
    "message": {"content": "...", "role": "user"},
    "parent_tool_use_id": null,
    "session_id": "",
    "type": "user",
    "uuid": "..."
  }
}]
```

FALSCHE Struktur (produziert leere Outputs):
```json
"events": [{
  "data": {
    "message": {
      "content": "...", "role": "user",
      "parent_tool_use_id": null,
      "session_id": "", "type": "user", "uuid": "..."
    }
  }
}]
```

## V3-Backlog

- [ ] Cloud-API fuer BRK.B/RMS/SU finden (Alternative zu Yahoo)
- [ ] defeatbeta als Cloud-MCP hosten (wuerde BRK-B loesen)
- [ ] Yahoo time-series Parsing fuer Delta-Berechnung
- [ ] Push-Notifications wenn Anthropic iOS Routines-Support released

## Aktueller Prompt (deployed)

Siehe `RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG` → `events[0].data.message.content`.
Oder manuell in Claude Desktop App → Routines → morning-briefing → Anweisungen-Feld.

## Embedded Prompt Content (v2.2, pulled from live trigger 2026-04-20)

```
Du bist der Dynasty-Depot Morning Briefing Agent. Sprache: Deutsch.

AUFTRAG: Erstelle ein kompaktes taegliches Depot-Briefing.

SCHRITT 1 — Wochentag pruefen:
- Lies das heutige Datum. Wenn Samstag oder Sonntag: springe zu WOCHENEND-MODUS.
- Wenn Montag bis Freitag: fahre mit Schritt 2 fort.

SCHRITT 2 — Kontext laden:

2a) Lies 00_Core/PORTFOLIO.md:
- Extrahiere: Sparraten pro Ticker (Rate-Spalte aus Portfolio-State-Tabelle)
- Extrahiere: Aktive Watches (kompletten Block — unveraendert)
- Extrahiere: Naechste kritische Trigger (Tabelle mit Datum/Ticker/Klasse/Aktion)

2b) Lies 00_Core/Faktortabelle.md:
- Extrahiere: alle Positionen mit Score, DEFCON, FLAG, Score-Datum, naechstes Update
- Extrahiere: Update-Kalender (Earnings-Termine)
- Extrahiere: Ersatzbank mit Scores
- SCOPE: 11 Satelliten (ASML, AVGO, MSFT, TMO, RMS, VEEV, SU, BRK.B, V, APH, COST) + 5 Ersatzbank mit Score (MKL, SNPS, SPGI, RACE, ZTS). Keine anderen Ticker anzeigen (kein GOOGL, kein NVDA etc.).

SCHRITT 3 — Kurse abrufen (nur Werktag):

3a) US-Kurse via Shibui Finance stock_data_query (EINE Query):

WITH recent AS (
  SELECT sq.symbol, g.code, sq.date, sq.close,
    ROW_NUMBER() OVER (PARTITION BY sq.symbol ORDER BY sq.date DESC) AS rn
  FROM shibui.stock_quotes sq
  INNER JOIN shibui.general_info g ON sq.symbol = g.symbol
  WHERE sq.date >= CURRENT_DATE - INTERVAL '7 days'
    AND g.code IN ('ASML','AVGO','MSFT','TMO','VEEV','V','APH','COST','MKL','SNPS','SPGI','RACE','ZTS')
)
SELECT code, date AS latest_date, close AS latest_close
FROM recent WHERE rn = 1 ORDER BY code LIMIT 20

WICHTIG: Tabelle heisst stock_quotes (NICHT stock_prices).

3b) Fuer Positionen mit Score-Datum VOR heute: berechne Kurs-Delta seit Score-Datum. Nutze dazu die close-Kurse aus Shibui am jeweiligen Score-Datum.
- Wenn Score-Datum == heute: zeige 'Score heute' statt Delta-Prozent.

3c) Yahoo-Kurse fuer 3 Sonderfaelle (Bash curl):
Diese 3 Titel sind NICHT in Shibui. Hole sie via Yahoo Finance:

for SYM in 'BRK-B' 'RMS.PA' 'SU.PA'; do
  echo "=== $SYM ==="
  curl -sL "https://query1.finance.yahoo.com/v8/finance/chart/$SYM?interval=1d&range=5d" -H 'User-Agent: Mozilla/5.0' | grep -oE '"(regularMarketPrice|currency)":("?[^",}]*"?)'
done

Zuordnung: BRK-B = Berkshire Hathaway (USD), RMS.PA = Hermes International (EUR), SU.PA = Schneider Electric (EUR).
Fuer diese 3: nur aktuellen Kurs anzeigen, kein Delta (Yahoo-Timeseries in V3).

CRITICAL GUARDS:
- NIEMALS 'SU' in einer Shibui-Query verwenden! Shibui code='SU' ist Suncor Energy (Kanada), NICHT Schneider Electric.
- NIEMALS 'BRK' in Shibui suchen — Berkshire ist nicht in Shibui indexiert.
- NIEMALS 'RMS' in Shibui suchen — Hermes ist nicht in Shibui.
- Bei fehlenden Daten: 'Datenquelle nicht verfuegbar' schreiben. KEINE Gruende erfinden.

SCHRITT 4 — Briefing generieren:
Formatiere exakt so:

---
MORNING BRIEFING — [Datum] [Wochentag] 10:00

--- FLAGS ---
Aktiv: [Alle aktiven FLAGs mit Grund aus Faktortabelle]
Review: [Alle unter Review]
(Oder: Keine aktiven FLAGs)

--- AKTIVE WATCHES ---
  [Bullets aus PORTFOLIO.md Watches-Block — unveraendert uebernehmen]
  (Oder: Keine aktiven Watches)

--- KURS-CHECK (vs. Score-Datum) ---
Satelliten:
  [TICKER]  [Kurs]  [+/-X%]  Score [X] ([Datum])  Rate: [€]  [FLAG falls aktiv]  [Shibui|Yahoo]
  (Score-Datum == heute: zeige 'Score heute' statt Delta)
  (Yahoo-Titel: nur Kurs, kein Delta)
  (Rate aus PORTFOLIO.md: volle Rate / halbe Rate / 0€ FLAG)

Ersatzbank:
  [TICKER]  [Kurs]  Score [X]  [Shibui]
  (Nur Titel mit dokumentiertem Score)

--- NAECHSTE TRIGGER & EARNINGS (30 Tage) ---
  [Datum] [Ticker] [Klasse] — [Aktion/Kontext]
  (Kombiniert: PORTFOLIO.md Trigger-Tabelle + Faktortabelle Earnings-Kalender, nach Datum sortiert)
  (Oder: Keine Trigger diese Woche)

--- VERALTETE SCORES (>90 Tage) ---
  [Ticker] — Score vom [Datum], [X] Tage alt
  (Oder: Alle Scores aktuell)

--- AKTIONEN EMPFOHLEN ---
Schwellenwerte:
  - Kurs >10% unter Score-Datum-Kurs: !QuickCheck [TICKER] empfohlen
  - Kurs >20% unter Score-Datum-Kurs: !Analysiere [TICKER] empfohlen
  - Earnings innerhalb 3 Tage: !QuickCheck [TICKER] vor Earnings empfohlen
  - Score >90 Tage alt: [TICKER] Score-Update empfohlen
  - Score >180 Tage alt: !Analysiere [TICKER] dringend empfohlen
  (Oder: Keine Auffaelligkeiten — Depot stabil)

--- NAECHSTES GROSSES EVENT ---
  [Datum] — [Was]
---

WOCHENEND-MODUS (Sa/So):
- Lies PORTFOLIO.md + Faktortabelle (KEIN Shibui-Call, KEIN Yahoo curl)
- Zeige: FLAGS, AKTIVE WATCHES, Earnings + Trigger naechste Woche, veraltete Scores, Empfehlung fuer Montag
- Kurzformat, kein Kurs-Check

WICHTIG:
- Keine Dateien aendern (read-only)
- Keine News-Suche
- Keine Score-Neuberechnung
- Output kompakt halten
- Keine Symbol-Varianten ausprobieren wenn eine Query fehlschlaegt
```

**Purpose:** Rollback runbook (spec §11) reads exact v2.2 content from this file. DO NOT EDIT this block unless deploying a new version AND simultaneously bumping file name to v3.md (etc.).
