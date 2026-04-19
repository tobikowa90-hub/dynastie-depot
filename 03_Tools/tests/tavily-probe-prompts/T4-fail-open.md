# T4 Fail-Open Test

**Setup:** Minimal prompt that provokes Tavily HTTP 422 error (same as Phase-0-R1 Test C pattern), verifies fail-open behavior.

**Probe allowed_tools:** `["mcp__tavily__tavily_search"]` (minimal)

**Probe mcp_connections:** Tavily UUID only (Shibui nicht erforderlich)

**Content to send to probe:**
```
TEST-PROMPT fuer Fail-Open-Verhalten (MCP-Architektur, post-CLI-Revert).

Aufgabe 1: Eine valide tavily_search mit query='TMO news', max_results=2, time_range='day'. Gib title+url der Results aus. Bei Fehler: 'TEST A FEHLER: <msg>'.

Aufgabe 2: Eine ZWEITE tavily_search mit absichtlich ungueltiger Konfiguration:
  query: '' (leer)
  max_results: -1 (negativ)
Diese soll fehlschlagen. Fange den Fehler ab und gib 'TEST B FAIL-OPEN OK: <fehlermeldung>' aus. Brich NICHT ab — setze normal fort.

Output-Format exakt:
---TEST A---
<OK mit URLs oder FEHLER>
---TEST B---
<FAIL-OPEN OK oder FAIL-CLOSED>
---FERTIG---
```

## Expected Output

```
---TEST A---
OK — <N> Results:
<title> (<url>)
...
---TEST B---
FAIL-OPEN OK: HTTP 422 — {"type":"missing","loc":["body","query"],...}
---FERTIG---
```

## Pass Criteria

1. TEST A liefert mindestens 1 echtes Result (beweist Konnektivitaet)
2. TEST B zeigt "FAIL-OPEN OK:" gefolgt von Fehlermeldung
3. "---FERTIG---" wird erreicht (Run laeuft durch, kein Abbruch)

## Precedent

Phase-0-R1 Test C hat dieses Pattern bereits mit Erfolg verifiziert (HTTP 422 sauber gecatched, Run bis Ende). T4 ist im Wesentlichen Regression-Check nach Spec-Aenderungen.
