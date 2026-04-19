# Design Spec — Tavily Integration in Morning Briefing

**Date:** 2026-04-19
**Author:** Tobias Kowalski (via Claude + 2× Codex review rounds)
**Status:** Awaiting approval → writing-plans
**Target:** Morning Briefing Remote Trigger `trig_01PyAVAxFpjbPkvXq7UrS2uG`, prompt v2.2 → v3.0
**Architecture:** **CLI via Bash/curl** (pivoted 2026-04-19 from MCP after discussion of autonomous-run robustness; MCP remains for interactive Claude Code)
**Spec location:** `03_Tools/specs/` (co-located with prompt files, not `docs/superpowers/specs/` — project has no `docs/` root)

---

## 1. Problem & Goals

### Problem
Current Morning Briefing (v2.2) delivers Kurse, FLAGs, Watches und Trigger um 10:00 MESZ — aber ist zwischen Quartalsberichten blind für Events (FDA, M&A, Rating-Changes, Guidance-Updates, Management-Wechsel). Wichtige Entwicklungen zeigen sich erst im Kurs-Drop oder Earnings-Shock.

### Goal
News-Signal-Sektion ergänzt das Briefing mit:
- **Cohort-Level:** Sektor-/Macro-Events, die mehrere Portfolio-Titel treffen
- **Per-Ticker-Level:** Company-spezifische News **nur** für Ticker mit Earnings ≤3d, aktivem FLAG oder Score-Alter >90d

### Success Criteria
- News-Sektion erscheint in allen Werktags-Briefings ab Go-Live
- Pro Werktag: ≥1 material Cohort-News ODER ≥1 material Per-Ticker-News
- Zero Regressions: v2.2-Funktionalität (Kurse, FLAGs, Trigger, Watches) bleibt unverändert
- Monatliches Tavily-Budget bleibt unter 15% des Free-Tiers (<150/1000)
- Ticker-Traps (SU.PA ≠ Suncor, RMS.PA ≠ Rockwell) werden zuverlässig vermieden

---

## 2. Non-Goals (YAGNI Boundaries)

Folgendes ist **nicht** Teil von v3.0 — explizit weggelassen:

- Dedup gegen gestriges Briefing (erfordert persistenten State)
- News-Sentiment-Analyse oder LLM-Scoring der Headlines
- Allowlist-Gewichtung nach DEFCON-Level
- Automatic-Retry-Logic bei HTTP 5xx (einfach fail-open, manuelle Investigation)
- Push-Notifications (wartet auf Anthropic iOS Routines-Support)
- EU-spezifische News-Quellen jenseits der Tier-1-Aggregatoren
- Automatische Key-Rotation
- Budget-Counter im Prompt (Tavily liefert kein Remaining-Header ohne API-Call)

Diese Features kommen nach Go-Live in v3.1 wenn gebraucht.

---

## 3. Background

### Existing System (v2.2)
- **Trigger:** `trig_01PyAVAxFpjbPkvXq7UrS2uG`, Cron `0 8 * * *` (10:00 MESZ), enabled
- **Environment:** `env_01Ek3HiKjymFoWzrQoyvMTEk`
- **Prompt SoT:** `03_Tools/morning-briefing-prompt-v2.md` (v2.2)
- **Scope:** 16 Portfolio-Symbole (13 Shibui, 3 Yahoo)
- **Connectors:** Shibui-Finance (UUID `3ecc8248-4bff-4b40-bab2-9bff78a30413`)
- **Tools:** `["Bash","Read","Glob","Grep"]`

### Constraints
- **Remote Trigger API:** Full-replace on update (siehe `remote-trigger-api` memory). Alle 3 Felder (`environment_id`, `session_context`, `events`) zusammen senden.
- **JSON-Nesting:** `parent_tool_use_id`, `session_id`, `type`, `uuid` auf data-Level, nicht in message.
- **`run` endpoint:** Noop für Cron-Trigger. Manual runs nur via Desktop App.
- **Tavily Free Tier:** 1000 Queries/Monat.
- **Prompt-Size:** Kein dokumentiertes Limit bekannt; 32 MB Anthropic-Request-Cap. v2.2 ~5000 Zeichen, v3.0 ~6500 Zeichen — unkritisch.

### New Dependency
- **Tavily REST API:** `https://api.tavily.com/search` (POST, `Authorization: Bearer <KEY>`)
- **No MCP connector required** — Bash/curl in Remote Trigger Runtime
- **Existing Yahoo-curl-Pattern wird erweitert** — kein neuer Architektur-Stil
- **Claude-Agent parst JSON-Response in-prompt** — kein jq-Runtime-Dependency
- **Historical note:** Tavily MCP war in Phase 0 verifiziert (UUID `4a633350-7128-4729-b8be-85373854fa4d`). CLI-Pivot in derselben Session nach Trade-off-Analyse — MCP-Connector bleibt in Claude.ai registriert (harmlos), kann manuell entfernt werden.

---

## 4. Design Decisions (from brainstorming)

| # | Frage | Entscheidung | Rationale |
|---|---|---|---|
| 1 | Scope | Getriggert (Earnings≤3d OR FLAG OR Score>90d) | Matcht bestehendes Trigger-Modell; max 5 Per-Ticker + 1 Cohort; <150/mo |
| 2 | Execution | Remote Trigger (Cloud) | News direkt im 10:00-Briefing; keine zweistufige lokale Anreicherung |
| 3 | Deployment | In-place + strict Manual-Test-Gate | Matcht v2.2-Rollout-Muster; simpler als Shadow-Trigger |
| 4 | Fallback | Fail-open | Konsistent mit Yahoo-403-Pattern ("n.v."); Rest des Briefings bleibt intakt |
| 5 | Noise-Filter | Tight Allowlist (12 domains) | Signal >> Breite; EU-Coverage via Reuters/FT ausreichend |

---

## 5. Architecture

### Topology
```
Cron 0 8 * * *  (08:00 UTC = 10:00 MESZ)
    │
    ▼
Remote Trigger  trig_01PyAVAxFpjbPkvXq7UrS2uG
    ├─ mcp_connections:         (UNVERAENDERT)
    │   └─ Shibui-Finance
    ├─ session_context.allowed_tools:  (UNVERAENDERT)
    │   └─ Bash, Read, Glob, Grep
    └─ events[0].data.message.content =
        Prompt v3.0
            ├─ Schritt 1-3: unveraendert (v2.2-Logik)
            ├─ SCHRITT 4.5: NEUE News-Sektion
            │   └─ Bash curl → https://api.tavily.com/search
            │       (Authorization: Bearer tvly-...)
            └─ Schritt 4+: unveraendert, neue News-Section im Output
```

### Change Summary (exactly 1)
**`ccr.events[0].data.message.content`:** Replace with v3.0 prompt (v2.2 + neue SCHRITT 4.5 Bash-curl-News + neue Output-Sektion + "Keine News-Suche"-Zeile entfernt). **Keine Änderung** an `mcp_connections` oder `allowed_tools`.

### CLI Design Rationale (vs. MCP)
1. **Weniger Kaskaden-Failures:** Keine MCP-Connector-Init-Pfad → Connector-Offline-Risk (Codex Residual #5) eliminiert
2. **Konsistenz:** Exakt das Pattern, das Yahoo-Kurs-Fetch in v2.2 schon nutzt
3. **Auth in Header statt URL-Query:** Bearer-Token statt URL-Parameter (weniger Log/Snapshot-Exposure)
4. **Keine Web-UI-Registrierung nötig:** Ein Konfig-Ort (Prompt-Text) statt zwei (Connector + Trigger)

### Isolation
News-Sektion ist zwischen KURS-CHECK und NAECHSTE TRIGGER eingeschoben. Alle anderen Sektionen (FLAGS, WATCHES, VERALTETE SCORES, AKTIONEN, GROSSES EVENT, WOCHENEND-MODUS) unverändert. Shibui-MCP und Yahoo-curl bleiben wie in v2.2.

---

## 6. Components & Prompt Logic

### New Section in Prompt v3.0: SCHRITT 4.5 — NEWS-SIGNAL (via curl)

```
SCHRITT 4.5 — NEWS-SIGNAL (nur Werktag):

(A) COHORT-QUERY — 1 curl-Call:
  curl -sL -X POST "https://api.tavily.com/search" \
    -H "Authorization: Bearer $TAVILY_KEY" \
    -H "Content-Type: application/json" \
    --max-time 20 \
    -d '{
      "query": "ASML AVGO MSFT TMO VEEV V APH COST MKL SNPS SPGI RACE ZTS earnings guidance news",
      "search_depth": "basic",
      "time_range": "day",
      "max_results": 10,
      "include_domains": [<ALLOWLIST>]
    }'

  Response-Parsing: Claude-Agent liest JSON-Response direkt, extrahiert
  title + url + source aus results[]. Keine jq-Dependency.

(B) TRIGGER-LISTE berechnen:
  triggered = [Ticker fuer Ticker in Portfolio if:
    earnings_in_days(Ticker) <= 3
    OR flag_active(Ticker)
    OR score_age_days(Ticker) > 90]

  SORTIERUNG mit Slot-Reservierung (Codex Fix #3):
    SLOT-STRUKTUR (5 gesamt):
      - Slot 1-2: RESERVIERT für "imminent earnings" (earnings_in_days <= 1).
        Wenn <2 solche Ticker existieren: Slots fallen an allgemeine Priorität.
      - Slot 3-5: allgemeine Priorität mit composite key:
          priority_score = (flag_active ? 100 : 0)
                         + (stale_score ? 50 : 0)
                         + max(0, 30 - earnings_in_days)

    Sortierung (innerhalb jeder Gruppe):
      1. priority_score absteigend
      2. earnings_in_days aufsteigend (Tiebreaker 1)
      3. alphabetisch (Tiebreaker 2)

    RATIONALE (Codex Fix #3): Verhindert "stale FLAG outranks earnings-tomorrow"-
    Pathology. Imminent-Earnings haben garantierte Slots auch bei aktiven FLAGs
    in anderen Tickern.

(C) PER-TICKER-QUERIES — max 5 curl-Calls:
  FOR t in triggered:
    QUERY_STRING muss MINDESTENS enthalten:
      - COMPANY_NAME(t) (aus Map unten) UND
      - TICKER(t) symbol

    Format: "<COMPANY_NAME(t)> <TICKER(t)> news"

    curl -sL -X POST "https://api.tavily.com/search" \
      -H "Authorization: Bearer $TAVILY_KEY" \
      -H "Content-Type: application/json" \
      --max-time 20 \
      -d '{
        "query": "<COMPANY_NAME> <TICKER> news",
        "search_depth": "advanced",
        "time_range": "day",
        "max_results": 3,
        "include_domains": [<ALLOWLIST>]
      }'

(D) MATERIALITÄTS-FILTER (Codex Fix #2):
  PRO Headline im Response prüfen ob sie mindestens eines dieser Kriterien erfüllt:
    - Earnings-Announcement / Guidance-Update
    - M&A / Partnership / Akquisition
    - Analyst-Rating-Action (Upgrade/Downgrade)
    - Regulatorisches Event (FDA, EMA, SEC Enforcement, 8-K)
    - Management-Wechsel (CEO, CFO, Chief-Role)
    - Produkt-Launch / Recall / Material Lawsuit
    - Dividenden-Änderung / Buyback-Announcement

  AUSSCHLUSS (als Noise verwerfen):
    - "<TICKER> to report earnings on [Datum]" (nur Datums-Ankündigung)
    - Weekly/Monthly Market-Roundups ohne Ticker-Fokus
    - "Top N Stocks"-Listen, Rankings
    - Pure Opinion-Pieces, Price-Target-Predictions

  Wenn KEINE material Headline zurückkommt: Ticker als "keine material News" behandeln.
  Zeige max 1 material Headline pro Ticker (die höchstgerangt ist).

(E) FEHLER-HANDLING (erweitert für CLI, Codex Fix #4):

  KLASSE 1 — curl exit code != 0 (Network/DNS/Timeout):
    - Log "<TICKER> — n.v. (curl exit <code>)"
    - Weiter mit nächstem Ticker

  KLASSE 2 — HTTP-Status != 200 (4xx/5xx):
    - 401/403: "NEWS-SIGNAL: Auth-Fehler — Key rotieren" in Sektions-Header; alle weiteren Queries skippen
    - 429: "NEWS-SIGNAL: Rate-Limit erreicht (Budget ausgeschöpft)"; alle weiteren Queries skippen
    - 500+: "<TICKER> — n.v. (HTTP <code>)"; weiter
    - 400/422: "<TICKER> — n.v. (bad request)"; weiter

  KLASSE 3 — Response-Body kein valides JSON / malformed:
    - Log "<TICKER> — n.v. (parse-error)"
    - Weiter mit nächstem Ticker

  KLASSE 4 — Valides JSON aber results[] leer:
    - "<TICKER> — keine News" (kein Fehler, sondern normaler Zero-Match)

  KLASSE 5 — Valides JSON, results[] nicht-leer, aber nach Materialitäts-Filter alles Noise:
    - "<TICKER> — keine material News"

  KLASSE 6 — Claude-Runtime-Timeout vor Schritt 4.5-Abschluss (>90s gesamt):
    - Ist KEIN fail-open-Pfad. Runtime-Fehler = Rollback-Trigger (siehe §11).
    - Mitigation: Hard-Cap 6 curl-Calls, `--max-time 20` pro curl = max 120s theoretisch,
      praktisch meist <30s. Wenn trotzdem Timeout: Spec-Revision in v3.1.

  Budget-Fallback (Codex Fix #4, partial):
    Wenn nach Cohort + 3 Per-Ticker-Queries die verbrauchte Zeit >60s:
      - Skippe die restlichen Per-Ticker-Queries
      - Log "NEWS-SIGNAL: Runtime-Budget gekappt, <n> Ticker nicht abgefragt"
      - Weiter mit Schritt 4

  NIEMALS Run abbrechen (ausser Klasse 6 Runtime-Timeout, der ist außerhalb unserer Kontrolle).
```

### Implizite Prompt-Änderung zu v2.2
In der `WICHTIG`-Liste am Ende des v2.2-Prompts steht aktuell: `Keine News-Suche`. Diese Zeile MUSS in v3.0 entfernt werden, sonst kollidieren die Anweisungen.

### Query-Content-Assertion (Codex Fix #1, adressiert T3-Gap)
In den PER-TICKER-Queries MUSS der `query`-String BEIDE enthalten: COMPANY_NAME UND TICKER. Nur COMPANY_NAME allein reicht nicht (bei Schneider "Schneider news" könnte Schneider-Electric vs. -Trucking disambiguiert werden, aber sicherer ist "Schneider Electric SU.PA news"). Test T3 verifiziert diese Assertion durch String-Content-Check am emittierten curl-Body.

### Allowlist (hardcoded im Prompt)
```
[
  "reuters.com", "ft.com", "bloomberg.com", "wsj.com",
  "businesswire.com", "prnewswire.com", "globenewswire.com",
  "sec.gov",
  "marketbeat.com", "zacks.com",
  "finance.yahoo.com",
  "spglobal.com"
]
```
Gründe:
- **Tier-1-News** (Reuters, FT, Bloomberg, WSJ) decken global inkl. EU
- **Wire-Services** (Businesswire, PRNewswire, Globenewswire) = direkte PR-Quellen, Globenewswire hat hohe EU-Coverage
- **sec.gov** für 8-K/Filings
- **Marketbeat/Zacks** für Consensus-Daten (Earnings-Vorfeld-Signal)
- **finance.yahoo.com** als breiter Aggregator
- **spglobal.com** für Rating-Actions
- **IR-URLs bewusst weggelassen:** Tavily-Indexierung mit 4-48h Latenz; für `time_range=day` wertlos

### Company-Name-Map (hardcoded im Prompt)
```
ASML    → "ASML Holding"
AVGO    → "Broadcom"
MSFT    → "Microsoft"
TMO     → "Thermo Fisher Scientific"
VEEV    → "Veeva Systems"
V       → "Visa Inc"
APH     → "Amphenol"
COST    → "Costco"
MKL     → "Markel Group"
SNPS    → "Synopsys"
SPGI    → "S&P Global"
RACE    → "Ferrari"
ZTS     → "Zoetis"
BRK-B   → "Berkshire Hathaway"
RMS.PA  → "Hermes International"    # NICHT Rockwell Medical
SU.PA   → "Schneider Electric"      # NICHT Suncor Energy
```

Gründe für hardcoded:
- Stable Data (Namen ändern sich praktisch nie)
- Git-Diff-Sichtbarkeit bei Änderungen
- Guard-Selbstdokumentation (Suncor/Hermès-Trap mit Kommentaren im Prompt)

### New Output Section

Eingeschoben zwischen `--- KURS-CHECK ---` und `--- NAECHSTE TRIGGER & EARNINGS ---`:

```
--- NEWS-SIGNAL (letzte 24h) ---
Cohort:
  [Headline kurz] ([Quelle-Domain])
  (Oder: Keine material Cohort-News)

Per Ticker (nur getriggert):
  [TICKER] — [Headline] ([Quelle])
  (Oder: Keine getriggerten Ticker, oder: [TICKER] — n.v. bei Fehler)
```

---

## 7. Data Flow

```
1. Git Repo (tobikowa90-hub/dynastie-depot)
   ├─ 00_Core/STATE.md         → Sparraten, Watches, Trigger-Tabelle
   └─ 00_Core/Faktortabelle.md → Scores, DEFCON, FLAGs, Earnings, Score-Alter

2. Shibui MCP → 13 US-Ticker Close-Prices    (UNVERAENDERT)

3. Bash curl (Yahoo) → BRK-B, RMS.PA, SU.PA Close-Prices   (UNVERAENDERT)

4. Trigger-Liste berechnen (in-prompt, rein aus Schritt-1-Daten)

5. Bash curl (Tavily REST API)       ← NEU (via curl, nicht MCP)
   ├─ Cohort-Query (1 Call, search_depth=basic)
   ├─ Per-Ticker-Queries (0..min(5, len(triggered)), search_depth=advanced)
   └─ Claude-Agent parst JSON-Response in-prompt, applies Materialitäts-Filter

6. Briefing-Assembly (in-prompt, keine weiteren Tool-Calls)
```

**Reihenfolge-Invariante:** Schritt 5 MUSS nach Schritt 4. Cohort hängt nicht von Triggern ab, Per-Ticker schon.

**Output-Kanal:** `trigger.run.output` in Anthropic Routines-History, via Desktop App sichtbar.

**Idempotenz:** Stateless per Run. Re-Run innerhalb 1h zählt 2× gegen Budget.

**Determinismus:** Gleiche Trigger-Bedingungen → gleiche Query-Liste → ~identischer Output (Tavily-Ranking minimal volatil, aber Allowlist + `time_range=day` dämpft Drift).

---

## 8. Error Handling

Siehe Section 6(E) für die vollständige Klassen-Taxonomie. Zusammenfassung:

| Klasse | Beispiel | Verhalten | Output |
|---|---|---|---|
| 1. curl exit ≠ 0 | DNS/Network/Timeout | Catch, weiter | `[TICKER] — n.v. (curl exit <code>)` |
| 2a. HTTP 401/403 | Auth-Fehler | Loud flag, alle weiteren Queries skippen | `NEWS-SIGNAL: Auth-Fehler — Key rotieren` |
| 2b. HTTP 429 | Rate-Limit | Loud flag, alle weiteren Queries skippen | `NEWS-SIGNAL: Rate-Limit erreicht` |
| 2c. HTTP 400/422 | Bad params | Catch, weiter | `[TICKER] — n.v. (bad request)` |
| 2d. HTTP 500+ | Tavily down | Catch, weiter | `[TICKER] — n.v. (HTTP <code>)` |
| 3. JSON malformed | Partial response | Catch, weiter | `[TICKER] — n.v. (parse-error)` |
| 4. Empty results[] | Keine Treffer | Kein Fehler | `[TICKER] — keine News` |
| 5. Materialitäts-Filter verwirft alles | Noise-only | Kein Fehler | `[TICKER] — keine material News` |
| 6. Claude-Runtime-Timeout | >90s gesamt | Rollback-Trigger, NICHT fail-open | — (Run wird vom Runtime abgebrochen) |

### Eliminated Failure Mode (vs. MCP-Architektur)
**MCP Connector-Fail** (Codex' prior Residual-Risk #5) existiert in CLI-Architektur **nicht**. Kein extra Runtime-Dienst, der erreichbar sein muss — curl ist Bash-intrinsic.

### Post-Deployment Verification Step (Codex Fix #7)
Nach jedem `RemoteTrigger update` auf Prod-Trigger:
1. `RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG` aufrufen
2. Verifizieren: `ccr.events[0].data.message.content` enthält `SCHRITT 4.5` String
3. Verifizieren: `ccr.events[0].data.message.content` enthält **nicht** `Keine News-Suche`
4. Erst danach Manual-Run via Desktop App auslösen

Dieser Gate verhindert Cache-Interference-Fälle, bei denen ein Update API-Level akzeptiert wird, aber alter Content weiter ausgeliefert würde.

### Rate-Limit Budget-Tracking
Keine in-Prompt-Zählung (Tavily liefert keine Remaining-Header ohne Extra-API-Call). Monitoring:
- Monatlich Tavily-Dashboard prüfen
- Hard-Cap pro Run: 6 Queries (1 Cohort + max 5 Per-Ticker)
- Hard-Cap pro Monat: 22 Werktage × 6 = 132/Monat worst-case (13.2% des Free-Tiers)
- Zusätzlich Budget-Fallback (siehe 6E): wenn Runtime >60s, restliche Queries skippen

---

## 9. Testing Plan

### Pre-Deployment Tests auf Probe-Trigger

Probe-Trigger `trig_01XYuQ5mugsvZGZD4K52rjXh` wiederverwenden. Prompt je Test via `RemoteTrigger update` austauschen, manueller Run via Desktop App.

| # | Test | Setup | Pass-Kriterium |
|---|---|---|---|
| T1 | Happy-Path | Voller v3.0-Prompt mit mock-STATE (1-2 Ticker mit FLAG/Earnings), echter Key | Cohort-curl + ≥1 Per-Ticker-curl, Allowlist-Domains only, material-Filter angewandt, kein Abbruch |
| T2 | Empty-Trigger-List | mock-STATE ohne FLAGs/Earnings/stale Scores | News-Sektion zeigt nur Cohort, "Keine getriggerten Ticker" |
| T3 | Symbol-Trap (adversarial, Codex Fix #1) | Per-Ticker-Query für SU.PA und RMS.PA erzwingen; **zusätzlich**: prüfe query-string in curl-Body (muss COMPANY_NAME UND TICKER enthalten); **und**: manueller Noise-Injection — Tester liest Output und verifiziert dass keine Suncor/Rockwell-Headlines durchgerutscht sind auch bei hoher Tavily-Rangliste für Homonyme | Results enthalten nur Schneider/Hermès-Headlines; curl-Body enthält beide Terme; manuelle Content-Prüfung findet keinen Trap-Durchschlag |
| T4 | Fehler-Klassen | Prompt provoziert jede der Klassen 1-5 nacheinander (z.B. bad key → Klasse 2a; Rate-Limit-Sim schwierig, aber malformed JSON via Proxy geht) | Jede Klasse korrekt gecatched, Run läuft bis `---FERTIG---` durch (außer Klasse 6 — nicht testbar) |
| T5 | Post-Update Content-Verify (Codex Fix #7) | Nach `RemoteTrigger update`: `RemoteTrigger get` aufrufen, content grep auf `SCHRITT 4.5` + Negativ-Grep auf `Keine News-Suche` | Beide Checks PASS bevor Manual-Run getriggert wird |

Alle 5 Tests müssen **PASS** bevor Prod-Update.

### Phase 0 — Round 1 (MCP-Architektur, retrospektiv)

Historischer Record. Getestet, dann verworfen durch CLI-Pivot:

| # | Test | Ergebnis |
|---|---|---|
| A | API akzeptiert UUID-basierte MCP-Anbindung | ✅ HTTP 200 |
| B | Tool-Name `mcp__tavily__tavily_search` + Connectivity | ✅ 2 Results, 0.88s |
| C | Fail-Open bei MCP-Tool-Fehler | ✅ HTTP 422 gecatched |

### Phase 0 — Round 2 (CLI-Architektur, vor Spec-Finalisierung erforderlich)

| # | Test | Verifiziert |
|---|---|---|
| A2 | curl verfügbar in Remote-Trigger-Runtime | (Yahoo-curl in v2.2 funktioniert bereits → implizit bestätigt) |
| B2 | curl gegen `api.tavily.com/search` mit Bearer-Token liefert JSON | Minimal-Prompt auf Probe-Trigger |
| C2 | Claude-Agent parst JSON-Response ohne jq | Prompt fordert title+url aus results[], Agent extrahiert korrekt |
| D2 | Bad-Key-Pfad: HTTP 401/403 wird gecatched | Prompt mit `Bearer invalid-key`, prüfe "Auth-Fehler" Output |

---

## 10. Deployment Plan

### Gate-Sequenz (alle Schritte müssen PASS)

```
1. Phase 0 Round 2 (A2-D2) auf Probe-Trigger PASS
2. T1-T5 auf Probe-Trigger PASS
3. Prompt v3.0 committed nach 03_Tools/morning-briefing-prompt-v3.md
4. Push zu GitHub (VOR 10:00 UTC — sonst liest Cron morgen alte Daten)
5. RemoteTrigger update auf Prod-Trigger:
   - ccr.events[0].data.message.content = v3.0 prompt
   - ccr.session_context.allowed_tools: UNVERÄNDERT (Bash,Read,Glob,Grep)
   - ccr.mcp_connections: UNVERÄNDERT (Shibui only; Tavily-UUID harmlos falls noch drin)
6. POST-UPDATE VERIFY (Codex Fix #7):
   - RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG
   - Assert content.contains("SCHRITT 4.5")
   - Assert NOT content.contains("Keine News-Suche")
   - Bei Assertion-Fail: RE-UPDATE nötig, KEIN Manual-Run
7. Manueller "Jetzt ausführen" in Desktop App
8. Output-Validierung:
   - News-Sektion present?
   - Allowlist-Domains only?
   - Trigger-List respektiert (Slot-Struktur korrekt)?
   - Materialitäts-Filter greift (keine "TMO to report earnings"-Noise)?
   - curl-Fehler-Pfad falls provoziert: catched?
9. PASS → DONE. FAIL → Rollback (siehe §11).
```

### Timing
- Phase 0 Round 2: ~10 Min
- Pre-deploy Tests T1-T5: ~20 Min
- Prod-Update + Post-Update-Verify + Manual-Run: ~5 Min
- Total: ~35 Min, keine Downtime
- Deployment-Fenster: bis 08:00 UTC am Deployment-Tag (damit 10:00-Cron die neue Version nimmt — obwohl wir das heute manuell triggern, nicht Cron)

---

## 11. Rollback Plan — Exact Runbook (Codex Fix #5)

### Trigger-Bedingungen
- T1-T5 fail
- Post-Update-Verify (Gate-Schritt 6) fail
- Prod-Manual-Run fail (Gate-Schritt 8)
- Tag 1-3 Post-Deploy Monitoring findet Regression
- Claude-Runtime-Timeout (Fehlerklasse 6) tritt auf

### Rollback-Runbook (EXAKT, in dieser Reihenfolge)

Ausführbar in <2 Min durch Implementer, auch unter Zeitdruck (09:55 UTC-Szenario).

```bash
# SCHRITT 1: v2.2-Prompt-Inhalt laden (lokal, nicht aus Memory)
cat "03_Tools/morning-briefing-prompt-v2.md"
# DANN: manuell Zeile "Keine News-Suche" wiederherstellen falls im aktuellen v2.md
# entfernt wurde (Safety: v2.md bleibt unverändert im Repo bis Rollback-Ende)
```

**SCHRITT 2: Aktuelle Prod-Trigger-Konfig holen (für Full-Replace-Payload)**
```
Claude Code oder API-Caller:
  RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG
  → Response enthält vollständiges ccr-Objekt, speichere als baseline
```

**SCHRITT 3: Payload zusammensetzen — Full-Replace, ALLE Felder**
```
body = {
  "job_config": {
    "ccr": {
      "environment_id": "env_01Ek3HiKjymFoWzrQoyvMTEk",
      "session_context": {
        "allowed_tools": ["Bash", "Read", "Glob", "Grep"],
        "model": "claude-sonnet-4-6",
        "sources": [{"git_repository": {"url": "https://github.com/tobikowa90-hub/dynastie-depot"}}]
      },
      "events": [{
        "data": {
          "message": {
            "content": "<EXAKTER INHALT aus 03_Tools/morning-briefing-prompt-v2.md>",
            "role": "user"
          },
          "parent_tool_use_id": null,
          "session_id": "",
          "type": "user",
          "uuid": "<neue UUID generieren oder alte aus Baseline wiederverwenden>"
        }
      }]
    }
  }
}
```

**SCHRITT 4: Update posten**
```
RemoteTrigger update trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG body=<payload>
```

**SCHRITT 5: Verify (wie Post-Update-Verify in §10)**
```
RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG
Assert content.contains("Keine News-Suche")     ← zurück in v2.2
Assert NOT content.contains("SCHRITT 4.5")      ← kein v3.0-Reste
```

**SCHRITT 6: Kurz-Manual-Run via Desktop App** — bestätigen dass Briefing v2.2-Format liefert.

### Key-Prinzipien
- **Quelle der v2.2-Content ist die Datei** `03_Tools/morning-briefing-prompt-v2.md`, nicht Gedächtnis. Datei DARF bis Rollback-Ende NICHT geändert werden.
- **Full-Replace-Pflicht:** Alle 3 ccr-Felder (`environment_id`, `session_context`, `events`) zusammen senden. Partial-Update existiert nicht (siehe `remote-trigger-api` memory).
- **JSON-Nesting:** `parent_tool_use_id`/`session_id`/`type`/`uuid` auf data-Ebene, NICHT innerhalb `message`.

### Rollback-SLA: <2 Min bei eingeübtem Runbook, <5 Min beim ersten Mal

---

## 12. Post-Deployment Monitoring

| Tag | Check | Zeitpunkt | Rollback-Trigger |
|---|---|---|---|
| Tag 1 (Go-Live) | Full Output Review | Manueller Run direkt nach Deploy | Cohort+Triggered leer trotz passender Bedingung / Ticker-Trap trifft |
| Tag 2 (Cron) | Output Review | Nach 10:00 MESZ | Runtime >60s / News-Sektion fehlt / Fehler nicht gecatched |
| Tag 3 (Cron) | Output Review + Tavily-Dashboard Quota | Nach 10:00 MESZ | >15 Queries/Tag / Low-Quality-Domains durchgerutscht |

### Quality-Kriterien (Codex Fix #6 — messbar statt subjektiv)

**Materialitäts-Definition:** siehe Section 6(D). Identische Liste wird im Prompt UND im Monitoring verwendet → ein Truth-Wert.

**Measurement-Protokoll (Tag 1-3 Post-Deploy):**

1. **Sampling-Window:** Rollend über 3 aufeinanderfolgende Werktags-Briefings (alle Per-Ticker + Cohort-Headlines)
2. **Denominator:** Anzahl emittierter Headlines (nicht Queries, nicht Tavily-Results — nur was im Briefing landet)
3. **Numerator:** Headlines die mindestens ein Material-Kriterium aus 6(D) erfüllen
4. **Logging-Format** — während Tag 1-3 Review manuell pro Headline:
   ```
   Datum  Ticker  Headline (kurz)                           material  Kriterium
   04-20  TMO     "Q1 EPS beat by $0.08, raised guidance"   yes       Earnings/Guidance
   04-20  ASML    "New CEO appointed effective May 1"       yes       Management
   04-20  AVGO    "Top 10 Chip Stocks for 2026"             no        Rankings/Noise
   ```
5. **Threshold:** ≥70% material über 3-Tage-Window
6. **Action auf Threshold-Unterschreitung:**
   - 70-60%: Allowlist um 1-2 Tier-2-Domains kürzen, neu messen
   - <60%: Query-Formulierung überarbeiten (z.B. "news" entfernen, "earnings OR guidance OR filing" hinzufügen)
   - <40%: Rollback-Kandidat; Design-Review nötig

**Cohort-Quality:** ≥1 material Treffer/Tag an Werktagen mit S&P500-Movement >1%. Messung wie oben, separater Denominator.

**Keine automatische Auswertung in v3.0 geplant** — manueller Review ist explizit akzeptiert. v3.1-Kandidat falls Belastung zu hoch wird.

---

## 13. Risks & Mitigations

Konsolidiert aus Codex-Review Round 1 (`a6353fc19fe65e09a`) + Round 2 (pending) + Phase 0 Round 1 (MCP) + Round 2 (CLI, pending).

| # | Risk | Severity | Status | Mitigation |
|---|---|---|---|---|
| 1 | MCP `connector_uuid` Requirement | CRITICAL | ✅ Moot (CLI-Pivot) | Architektur-Wechsel entfernt Risk |
| 2 | MCP Tool-Name Korrektheit | HIGH | ✅ Moot (CLI-Pivot) | Architektur-Wechsel entfernt Risk |
| 3 | Prompt-Fail-Open bei Tool-Fehler | HIGH | ✅ Resolved (Phase 0 R1 Test C, Pattern übernehmen in CLI) | curl-exit-Handling analog |
| 4 | API-Key im Prompt-Text — Exposure | HIGH | ⚠️ Acknowledged, posture-only | Rotation nach Go-Live + monatlich; Dev-Key nur, separat vom Billing-Account |
| 5 | MCP Connector-Level-Fail (MCP offline) | MEDIUM | ✅ Moot (CLI-Pivot) | curl nicht betroffen |
| 6 | Tavily-Behavior-Drift (third-party) | MEDIUM | ⚠️ Accepted | Monitoring erfasst Degradation |
| 7 | Budget-Exhaust bei Retries | LOW | ⚠️ Accepted | Hard-Cap 6/Run + 60s-Runtime-Budget-Fallback |
| **8** | **curl/Bash-Runtime in Remote Trigger** | MEDIUM | ✅ Resolved (Yahoo-curl in v2.2 funktioniert → implizit bestätigt) | — |
| **9** | **JSON-Response-Parsing ohne jq** | MEDIUM | ⏳ Phase 0 Round 2 | Claude-Agent-Fähigkeit empirisch testen; Fallback: Regex-Extraction wie Yahoo |
| **10** | **Claude-Runtime-Timeout (>90s)** | MEDIUM | ⚠️ Accepted, Rollback-Trigger | Budget-Fallback (60s-Gate) + --max-time 20 pro curl |
| **11** | **Post-Update Cache-Interference** | LOW | ✅ Mitigated (Codex Fix #7) | Post-Update-Verify Gate vor Manual-Run |

### Codex-Findings-Trace (Round 1, alle integriert)

| Codex # | Finding | Integration |
|---|---|---|
| #1 | T3 Symbol-Trap nicht adversarial genug | Section 9 T3 erweitert: query-content-check + manuelle Noise-Injection |
| #2 | Materialitäts-Filter nur im Monitoring | Section 6(D) eingebaut in Prompt-Logik |
| #3 | Sort-Priority starvation | Section 6(B) Slot-Reservierung + composite priority |
| #4 | Runtime/Tooling-Error-Taxonomie | Section 6(E) + 8 — 6 Klassen explizit |
| #5 | Rollback nicht reproduzierbar | Section 11 Exact Runbook |
| #6 | 70%-Threshold nicht messbar | Section 12 Logging-Format + konkrete Actions |
| #7 | Post-Deploy-Cache-Interference | Section 8 + 10 Post-Update-Verify-Gate |

---

## 14. Open Questions / v3.1-Backlog

Verschoben aus v3.0-Scope, Kandidaten wenn Go-Live stabil:

- [ ] Dedup gegen gestriges Briefing (erfordert persistente History)
- [ ] Allowlist-Dynamik (DEFCON-gewichtet)
- [ ] Automatische Materialitäts-Scoring-Auswertung (eliminiert manuelle Tag-1-3-Zählarbeit)
- [ ] Retry-Logic bei HTTP 5xx (mit Exponential Backoff)
- [ ] Key-Rotation-Automation (monatlich via CI)
- [ ] Budget-Counter im Prompt (Tavily-Usage-API call vor Queries)
- [ ] EU-spezifische News-Quellen (handelsblatt, lesechos) falls Per-Ticker-Quality für RMS.PA/SU.PA unzureichend
- [ ] Environment-Variable für API-Key (falls Remote Trigger Secrets-Feature verfügbar wird)

---

## 15. Appendix

### A. Prompt v3.0 Skeleton (full text in `03_Tools/morning-briefing-prompt-v3.md` after writing-plans phase)

Strukturell: v2.2 + neuer SCHRITT 4.5 + neue Output-Sektion. Alle anderen Teile (CRITICAL GUARDS, WOCHENEND-MODUS, WICHTIG-Liste) unverändert ausser:
- `Keine News-Suche` (WICHTIG-Liste) → entfernen

### B. Codex Review Summary

**Round 1 (Architecture-Review, pre-Phase 0):**
- Agent-ID: `a6353fc19fe65e09a`
- 4 CRITICAL/HIGH-Flags — alle adressiert (3 empirisch via Phase 0 Round 1, 1 Posture-akzeptiert)

**Round 1 bis (Spec-Review nach initial-Write):**
- Agent-ID: `aede6311232389387`
- 7 Findings (3 HIGH, 3 MEDIUM, 1 LOW) — alle in Round-2-Spec-Revision integriert (siehe Trace in Section 13)

**Round 2 (Final-Review, nach CLI-Pivot):**
- Status: PENDING nach Spec-Commit
- Fokus: CLI-spezifische Risks, Integrität der Codex-1-Fixes, neue Gaps

### C. Phase 0 Test Results

**Round 1 (MCP-Architektur, retrospektiv nach CLI-Pivot):**
- Test A: UUID-MCP-Anbindung OK (HTTP 200 auf `RemoteTrigger create`)
- Test B: Tool-Name + Connectivity OK (2 Results für TMO earnings, 0.88s)
- Test C: Fail-Open OK (HTTP 422 bei `query=""`+`max_results=-1` → "FAIL-OPEN OK" in Output)

**Round 2 (CLI-Architektur, pending vor finaler Approval):**
- Test A2: curl-Verfügbarkeit (implizit durch Yahoo-curl in v2.2 bestätigt)
- Test B2: curl gegen `api.tavily.com/search` mit Bearer-Token liefert JSON
- Test C2: Claude-Agent parst JSON ohne jq
- Test D2: HTTP 401/403 wird gecatched und löst "Auth-Fehler"-Flag aus

### D. Architecture Decision Log

| Datum | Entscheidung | Kontext | Begründung |
|---|---|---|---|
| 2026-04-19 morning | MCP-basierte Tavily-Integration | Initial-Brainstorming | Typed schema, strukturiertes Protokoll |
| 2026-04-19 (Phase 0 Round 1) | MCP-Architektur empirisch verifiziert | Nach Codex Round 1 | `connector_uuid`, `mcp__tavily__tavily_search`, 422-fail-open |
| 2026-04-19 (Codex Round 1 bis) | 7 Gaps im MCP-Spec identifiziert | Nach Self-Review | Adversarial-T3, Materialitäts-Filter, Sort-Priority, Error-Taxonomy, Rollback-Runbook, Messbarkeit, Cache-Verify |
| 2026-04-19 (User-Prompt) | Pivot MCP → CLI | Fragestellung "CLI vs. MCP" | Eliminiert Connector-Fail-Risk, matcht Yahoo-Pattern, Bearer-Header statt URL-Query |
| 2026-04-19 (Revision) | Spec v2 mit CLI + 7 Codex-Fixes | Aktueller Stand | Siehe Sections 5-13 |

### D. Referenzen

- `03_Tools/morning-briefing-prompt-v2.md` — SoT der v2.2-Prompt
- `memory/morning-briefing-config.md` — v2.1-Scope + Known Issues
- `memory/remote-trigger-api.md` — Full-Replace-Regel, JSON-Nesting-Gotcha
- `CLAUDE.md §25` — `!SyncBriefing` / `!BriefingCheck`-Workflow
- Codex Feedback Memory (`feedback_codex_over_advisor.md`) — Second-Opinion-Pattern

---

**Next step:** Self-Review → Codex-Review → User-Review → writing-plans skill.
