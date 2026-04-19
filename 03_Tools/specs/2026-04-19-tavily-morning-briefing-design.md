# Design Spec — Tavily Integration in Morning Briefing

**Date:** 2026-04-19
**Author:** Tobias Kowalski (via Claude + Codex review)
**Status:** Awaiting approval → writing-plans
**Target:** Morning Briefing Remote Trigger `trig_01PyAVAxFpjbPkvXq7UrS2uG`, prompt v2.2 → v3.0
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
- Connector-Level-Healthcheck-Fallback (MCP down → kein Briefing möglich)
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
- **Tavily MCP:** hosted HTTP MCP bei `https://mcp.tavily.com/mcp/?tavilyApiKey=<KEY>`
- **Connector-UUID:** `4a633350-7128-4729-b8be-85373854fa4d` (registriert via Claude.ai Web-UI, 2026-04-19)
- **Tool exposé:** `mcp__tavily__tavily_search` (empirisch verifiziert, Phase 0 Test B)

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
    ├─ mcp_connections:
    │   ├─ Shibui-Finance  (UUID 3ecc8248-…)
    │   └─ Tavily          (UUID 4a633350-…)  ← NEU
    ├─ session_context.allowed_tools:
    │   ├─ Bash, Read, Glob, Grep
    │   └─ mcp__tavily__tavily_search         ← NEU
    └─ events[0].data.message.content =
        Prompt v3.0 (v2.2 + SCHRITT 4.5 NEWS-SIGNAL)
```

### Change Summary (exactly 3)
1. **`ccr.mcp_connections`:** Append Tavily entry (connector_uuid + url)
2. **`ccr.session_context.allowed_tools`:** Append `"mcp__tavily__tavily_search"`
3. **`ccr.events[0].data.message.content`:** Replace with v3.0 prompt (new Schritt 4.5 + output section between Kurs-Check and Naechste-Trigger)

### Isolation
News-Sektion ist zwischen KURS-CHECK und NAECHSTE TRIGGER eingeschoben. Alle anderen Sektionen (FLAGS, WATCHES, VERALTETE SCORES, AKTIONEN, GROSSES EVENT, WOCHENEND-MODUS) unverändert.

---

## 6. Components & Prompt Logic

### New Section in Prompt v3.0: SCHRITT 4.5 — NEWS-SIGNAL

```
SCHRITT 4.5 — NEWS-SIGNAL (nur Werktag):

(A) COHORT-QUERY — 1 Call:
  query: "ASML AVGO MSFT TMO VEEV V APH COST MKL SNPS SPGI RACE ZTS earnings guidance news"
  search_depth: "basic"
  time_range: "day"
  max_results: 10
  include_domains: <ALLOWLIST>

(B) TRIGGER-LISTE berechnen:
  triggered = [Ticker fuer Ticker in Portfolio if:
    earnings_in_days(Ticker) <= 3
    OR flag_active(Ticker)
    OR score_age_days(Ticker) > 90]

  SORTIERUNG (Priorität absteigend, wenn >5 Ticker matchen):
    1. flag_active == True  (FLAGs = dringlichstes Signal)
    2. earnings_in_days aufsteigend (je näher, desto wichtiger)
    3. score_age_days absteigend (je älter, desto dringender)
    4. alphabetisch (Tiebreaker)

  triggered = triggered[:5]  # Hard-Cap nach Sortierung

(C) PER-TICKER-QUERIES — max 5 Calls:
  FOR t in triggered:
    query: "<COMPANY_NAME(t)> <TICKER(t)> news"
    search_depth: "advanced"
    time_range: "day"
    max_results: 3
    include_domains: <ALLOWLIST>

(D) FEHLER-HANDLING:
  Cohort-Query fails:
    - Log "Cohort: n.v. (<fehlermeldung-kurz>)"
    - Weiter mit Per-Ticker-Queries
  Per-Ticker-Query fails (einzelner Ticker):
    - Log "<TICKER> — n.v. (<fehlermeldung-kurz>)"
    - Weiter mit nächstem Ticker
  Alle Per-Ticker fail:
    - Sektion zeigt alle als "n.v."
    - Rest des Briefings läuft durch
  NIEMALS Run abbrechen.
  Bei leerem Result (keine Fehler, nur 0 Treffer):
    - "Cohort: Keine material News" bzw. "<TICKER> — keine News"
```

### Implizite Prompt-Änderung zu v2.2
In der `WICHTIG`-Liste am Ende des v2.2-Prompts steht aktuell: `Keine News-Suche`. Diese Zeile MUSS in v3.0 entfernt werden, sonst kollidieren die Anweisungen.

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

2. Shibui MCP → 13 US-Ticker Close-Prices

3. Bash curl (Yahoo) → BRK-B, RMS.PA, SU.PA Close-Prices

4. Trigger-Liste berechnen (in-prompt, rein aus Schritt-1-Daten)

5. Tavily MCP
   ├─ Cohort-Query (1 Call)
   └─ Per-Ticker-Queries (0..min(5, len(triggered)))

6. Briefing-Assembly (in-prompt, keine Tool-Calls)
```

**Reihenfolge-Invariante:** Schritt 5 MUSS nach Schritt 4. Cohort hängt nicht von Triggern ab, Per-Ticker schon.

**Output-Kanal:** `trigger.run.output` in Anthropic Routines-History, via Desktop App sichtbar.

**Idempotenz:** Stateless per Run. Re-Run innerhalb 1h zählt 2× gegen Budget.

**Determinismus:** Gleiche Trigger-Bedingungen → gleiche Query-Liste → ~identischer Output (Tavily-Ranking minimal volatil, aber Allowlist + `time_range=day` dämpft Drift).

---

## 8. Error Handling

| Fehlerklasse | Beispiel | Verhalten | Output |
|---|---|---|---|
| Tavily API-Fehler (400/422/500) | Bad params, empty query | Catch, weiter | `[TICKER] — n.v. (API-Fehler)` |
| Tavily Auth-Fehler (401/403) | Key expired | Catch, loud flag | `NEWS-SIGNAL: Auth-Fehler — Key rotieren` + Sektion leer |
| Tavily Rate-Limit (429) | >1000/mo | Catch, weiter | `NEWS-SIGNAL: Rate-Limit erreicht` |
| Tavily Timeout (>30s) | Netzlag | Catch, weiter | `[TICKER] — n.v. (timeout)` |
| Empty Results | Keine Treffer | Kein Fehler | `Cohort: Keine material News` / `[TICKER] — keine News` |
| Allowlist-Filter leer | Results existieren, keine Tier-1 | Kein Fehler | Analog empty |
| MCP Connector-Fail | `mcp.tavily.com` down | Runtime-Level, prompt-unabfangbar ⚠️ | Potenziell Run-Abbruch |

### Prompt-Level Guard-Pattern (in v3.0 eingebaut)
```
Wenn tavily_search einen Fehler zurueckgibt:
  - NIEMALS den Run abbrechen
  - Schreibe in News-Section: "n.v. (<Fehlermeldung-kurz>)"
  - Fahre mit naechstem Ticker / naechstem Schritt fort
Wenn KEIN Result zurueckgegeben wird:
  - Schreibe: "Keine material News"
```

### Known Residual Risk
**MCP Connector-Fail** wird in v3.0 nicht gemitigated (YAGNI). Falls `mcp.tavily.com` total offline ist, kann der Run bei Connector-Init fehlschlagen. Mitigation post-Go-Live wenn beobachtet.

### Rate-Limit Budget-Tracking
Keine in-Prompt-Zählung (Tavily liefert keine Remaining-Header leicht parsebar). Manuelles Monitoring via Tavily-Dashboard 1× monatlich. Hard-Cap 6 Queries/Run × 22 Werktage = 132/Monat worst-case.

---

## 9. Testing Plan

### Pre-Deployment Tests auf Probe-Trigger

Probe-Trigger `trig_01XYuQ5mugsvZGZD4K52rjXh` (aus Phase 0) wiederverwenden. Prompt je Test via `RemoteTrigger update` austauschen, manueller Run via Desktop App.

| # | Test | Setup | Pass-Kriterium |
|---|---|---|---|
| T1 | Happy-Path | Voller v3.0-Prompt mit mock-STATE (1-2 Ticker mit FLAG/Earnings) | Cohort + ≥1 Per-Ticker News, Allowlist-Domains, kein Abbruch |
| T2 | Empty-Trigger-List | mock-STATE ohne FLAGs/Earnings/stale Scores | News-Sektion zeigt nur Cohort, "Keine getriggerten Ticker" |
| T3 | Symbol-Trap | Force Per-Ticker-Query für SU.PA und RMS.PA | Results nur von Schneider/Hermès, NICHT Suncor/Rockwell |
| T4 | Tavily-Fehler-Pfad | Prompt provoziert malformed query | Fail-Open, Briefing komplett bis FERTIG |

Alle 4 Tests müssen **PASS** bevor Prod-Update.

### Phase 0 (bereits bestanden)

| # | Test | Ergebnis |
|---|---|---|
| A | API akzeptiert UUID-basierte MCP-Anbindung | ✅ HTTP 200 bei `RemoteTrigger create` |
| B | Tool-Name `mcp__tavily__tavily_search` + Connectivity | ✅ 2 Results, 0.88s Response-Time |
| C | Fail-Open bei Tool-Level-Fehler | ✅ HTTP 422 sauber abgefangen, Run bis Ende |

---

## 10. Deployment Plan

### Gate-Sequenz (alle Schritte müssen PASS)

```
1. T1-T4 auf Probe-Trigger alle PASS
2. Prompt v3.0 committed nach 03_Tools/morning-briefing-prompt-v3.md
3. Push zu GitHub (VOR 10:00 UTC — sonst liest Cron morgen alte Daten)
4. RemoteTrigger update auf Prod-Trigger:
   - ccr.events[0].data.message.content = v3.0 prompt
   - ccr.session_context.allowed_tools += "mcp__tavily__tavily_search"
   - ccr.mcp_connections already contains Tavily (via UI, 2026-04-19)
5. Manueller "Jetzt ausführen" in Desktop App
6. Output-Validierung:
   - News-Sektion present?
   - Allowlist-Domains only?
   - Trigger-List respektiert?
   - Fail-Open-Pfad im Bedarfsfall?
7. PASS → DONE. FAIL → Rollback.
```

### Timing
- Pre-deploy Tests: ~15 Min
- Prod-Update + Manual-Run: ~5 Min
- Total: ~20 Min, keine Downtime
- Deployment-Fenster: bis 10:00 UTC am Deployment-Tag

---

## 11. Rollback Plan

### Trigger
- T1-T4 fail
- Prod-Manual-Run fail
- Tag 1-3 Post-Deploy Monitoring findet Regression

### Prozedur
1. v2.2-Prompt erhalten in `03_Tools/morning-briefing-prompt-v2.md` (NICHT löschen nach v3.0-Commit)
2. `RemoteTrigger update` mit:
   - `ccr.events[0].data.message.content` = v2.2 content
   - `ccr.session_context.allowed_tools` = `["Bash","Read","Glob","Grep"]` (remove Tavily)
   - `ccr.mcp_connections` = unchanged (Tavily entry darf bleiben — ohne allowed_tools inaktiv)
3. Optional: `RemoteTrigger update` mit ohne-Tavily-mcp_connections (sauberer, aber nicht nötig)

### Rollback-SLA: <2 Min

---

## 12. Post-Deployment Monitoring

| Tag | Check | Zeitpunkt | Rollback-Trigger |
|---|---|---|---|
| Tag 1 (Go-Live) | Full Output Review | Manueller Run direkt nach Deploy | Cohort+Triggered leer trotz passender Bedingung / Ticker-Trap trifft |
| Tag 2 (Cron) | Output Review | Nach 10:00 MESZ | Runtime >60s / News-Sektion fehlt / Fehler nicht gecatched |
| Tag 3 (Cron) | Output Review + Tavily-Dashboard Quota | Nach 10:00 MESZ | >15 Queries/Tag / Low-Quality-Domains durchgerutscht |

### Quality-Kriterien

**"Material" definiert als** (mindestens eine Bedingung):
- Earnings-Announcement / Guidance-Update
- M&A / Strategische Partnership / Akquisition
- Analyst-Upgrade/Downgrade / Rating-Action (S&P, Moody's)
- Regulatorisches Event (FDA-Approval, EMA, SEC-Enforcement, 8-K Filing)
- Management-Wechsel (CEO, CFO, Chief Scientist)
- Produkt-Launch / Produktrückruf / Lawsuit mit Material Impact
- Dividenden-Änderung / Buyback-Programm

**Nicht material (= Noise):**
- "TMO to report earnings on [Datum]" ohne zusätzlichen Kontext
- Weekly/Monthly Market-Roundups ohne Ticker-Fokus
- Rankings ("Top 10 Stocks"-Listen)
- Opinion-Pieces ohne Fakten

**Monitoring-Thresholds:**
- **Per-Ticker-News:** ≥70% material nach obiger Definition. Unterschreitung 2 Tage in Folge → Allowlist tightnen oder Query-Formulierung anpassen.
- **Cohort-News:** ≥1 material Treffer/Tag an Werktagen mit S&P500-Movement >1%.

---

## 13. Risks & Mitigations

Übernommen aus Codex-Review (17.690 Tokens, Agent-ID `a6353fc19fe65e09a`) + Phase 0-Tests.

| # | Risk | Severity | Status | Mitigation |
|---|---|---|---|---|
| 1 | `mcp_connections` benötigt `connector_uuid` | CRITICAL | ✅ Resolved via UI-Registrierung | UUID `4a633350-…` reused |
| 2 | Tool-Name korrekt? | HIGH | ✅ Resolved (Phase 0 Test B) | `mcp__tavily__tavily_search` bestätigt |
| 3 | Prompt-Fail-Open unreliable bei Tool-Fehler | HIGH | ✅ Resolved (Phase 0 Test C) | 422 sauber gecatched |
| 4 | API-Key in URL — Exposure | HIGH | ⚠️ Acknowledged, posture-only | Rotation nach Go-Live + monatlich; nur Dev-Key, nicht Billing-Key |
| 5 | Connector-Level-Fail (MCP offline) | MEDIUM | ⚠️ Accepted for v3.0 | Beobachten; v3.1-Backlog |
| 6 | Tavily-Behavior-Drift (third-party) | MEDIUM | ⚠️ Accepted | Monitoring erfasst Degradation |
| 7 | Budget-Exhaust bei Retries | LOW | ⚠️ Accepted | Hard-Cap 6/Run begrenzt worst-case |

---

## 14. Open Questions / v3.1-Backlog

Verschoben aus v3.0-Scope, Kandidaten wenn Go-Live stabil:

- [ ] Dedup gegen gestriges Briefing (erfordert persistente History)
- [ ] Allowlist-Dynamik (DEFCON-gewichtet)
- [ ] Connector-Level-Healthcheck-Fallback
- [ ] Key-Rotation-Automation (monatlich via CI)
- [ ] Budget-Counter im Prompt (Tavily-Usage-API call vor Queries)
- [ ] EU-spezifische News-Quellen (handelsblatt, lesechos) falls Per-Ticker-Quality für RMS.PA/SU.PA unzureichend

---

## 15. Appendix

### A. Prompt v3.0 Skeleton (full text in `03_Tools/morning-briefing-prompt-v3.md` after writing-plans phase)

Strukturell: v2.2 + neuer SCHRITT 4.5 + neue Output-Sektion. Alle anderen Teile (CRITICAL GUARDS, WOCHENEND-MODUS, WICHTIG-Liste) unverändert ausser:
- `Keine News-Suche` (WICHTIG-Liste) → entfernen

### B. Codex Review Summary (2026-04-19)

- **Agent-ID:** `a6353fc19fe65e09a` (SendMessage to continue)
- **CRITICAL/HIGH-Flags:** 4 (alle adressiert — 1-3 empirisch via Phase 0, 4 als Posture-Issue akzeptiert)
- **Recommendation:** "No materially better design within locked constraints" nach Phase-0-Tests

### C. Phase 0 Test Results

- Test A: UUID-MCP-Anbindung OK (HTTP 200 auf `RemoteTrigger create`)
- Test B: Tool-Name + Connectivity OK (2 Results für TMO earnings, 0.88s)
- Test C: Fail-Open OK (HTTP 422 bei `query=""`+`max_results=-1` → "FAIL-OPEN OK" in Output)

### D. Referenzen

- `03_Tools/morning-briefing-prompt-v2.md` — SoT der v2.2-Prompt
- `memory/morning-briefing-config.md` — v2.1-Scope + Known Issues
- `memory/remote-trigger-api.md` — Full-Replace-Regel, JSON-Nesting-Gotcha
- `CLAUDE.md §25` — `!SyncBriefing` / `!BriefingCheck`-Workflow
- Codex Feedback Memory (`feedback_codex_over_advisor.md`) — Second-Opinion-Pattern

---

**Next step:** Self-Review → Codex-Review → User-Review → writing-plans skill.
