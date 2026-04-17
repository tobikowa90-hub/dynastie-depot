# Morning Briefing Remote Trigger — Prompt v2.2
**Trigger-ID:** `trig_01PyAVAxFpjbPkvXq7UrS2uG`
**Deployed:** 2026-04-17 (via Desktop App)
**Version:** v2.2 — STATE.md als zweite Kontext-Quelle + Format-Erweiterung

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
