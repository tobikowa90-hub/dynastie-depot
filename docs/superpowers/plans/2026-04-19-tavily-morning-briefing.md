# Tavily Morning Briefing Integration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a triggered News-Signal section to the 10:00 Morning Briefing via `mcp__tavily__tavily_search`, with fail-open behavior, materiality filter, and slot-reserved priority.

**Architecture:** Remote Trigger (`trig_01PyAVAxFpjbPkvXq7UrS2uG`) gets prompt v3.0 + `mcp__tavily__tavily_search` in `allowed_tools`. Tavily connector already attached via Claude.ai web-UI (UUID `4a633350-7128-4729-b8be-85373854fa4d`). SCHRITT 4.5 calls Tavily (1 cohort + 0-5 per-ticker queries); all errors fail-open; test battery runs on probe trigger before prod.

**Tech Stack:** Claude Code RemoteTrigger API tool, Claude Desktop App (for manual runs — `run` API is noop for cron triggers), git, GitHub (tobikowa90-hub/dynastie-depot).

**Spec reference:** `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` (hash `6bd32f4`)

**Relevant artifacts:**
- Prod trigger: `trig_01PyAVAxFpjbPkvXq7UrS2uG` (currently v2.2, cron `0 8 * * *` = 10:00 MESZ)
- Probe trigger: `trig_01XYuQ5mugsvZGZD4K52rjXh` (disabled, manual-run only)
- Environment: `env_01Ek3HiKjymFoWzrQoyvMTEk`
- Shibui connector UUID: `3ecc8248-4bff-4b40-bab2-9bff78a30413`
- Tavily connector UUID: `4a633350-7128-4729-b8be-85373854fa4d`
- Tavily URL (with Dev-Key): pull current value via `RemoteTrigger get` on prod trigger — look in `mcp_connections[1].url`

---

## File Structure

**Create:**
- `03_Tools/morning-briefing-prompt-v3.md` — SoT for v3.0 prompt (metadata + embedded full prompt content)
- `03_Tools/tests/tavily-probe-prompts/T1-happy-path.md` — T1 probe prompt content (mock-light, uses real STATE)
- `03_Tools/tests/tavily-probe-prompts/T3-adversarial-trap.md` — T3 forces SU.PA/RMS.PA queries
- `03_Tools/tests/tavily-probe-prompts/T4-fail-open.md` — T4 provokes 422 (reuses Phase-0-R1-C pattern)
- `03_Tools/tests/tavily-probe-prompts/README.md` — how to run these against probe trigger

**Modify:**
- `03_Tools/morning-briefing-prompt-v2.md` — back-fill with exact v2.2 prompt content (currently only metadata; rollback-integrity fix discovered during spec self-review)
- `memory/morning-briefing-config.md` — post-deploy: update to v3.0 scope
- `00_Core/CORE-MEMORY.md` — append deployment entry per §4 protocol
- `00_Core/STATE.md` — update if v3.0-specific state fields change
- `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` — append entry

**Remote Trigger API side-effects:**
- `trig_01XYuQ5mugsvZGZD4K52rjXh` (probe): `events[0].data.message.content` gets swapped per test; `session_context.allowed_tools` gains `mcp__tavily__tavily_search`; `mcp_connections` gains Tavily entry
- `trig_01PyAVAxFpjbPkvXq7UrS2uG` (prod): `events[0].data.message.content` replaced with v3.0; `session_context.allowed_tools` gains `mcp__tavily__tavily_search`; `mcp_connections` unchanged (Tavily already attached)

---

## Task 0: Back-fill v2.md with current prod prompt content

**Context:** Spec §11 Rollback-Runbook names `03_Tools/morning-briefing-prompt-v2.md` as the v2.2 content source. Current file contains only metadata/changelog — NOT the prompt text. Rollback would fail.

**Files:**
- Modify: `03_Tools/morning-briefing-prompt-v2.md`

- [ ] **Step 0.1: Fetch current prod prompt content**

Use the RemoteTrigger tool:
```
RemoteTrigger action=get trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
```
Extract `trigger.job_config.ccr.events[0].data.message.content` — save as raw text, preserving all whitespace and special chars.

- [ ] **Step 0.2: Append embedded prompt to v2.md**

At the end of `03_Tools/morning-briefing-prompt-v2.md`, add a new section:

```markdown
## Embedded Prompt Content (v2.2, pulled from live trigger 2026-04-19)

```
<paste full content from Step 0.1 here, unmodified>
```

**Purpose:** Rollback runbook (spec §11) reads exact v2.2 content from this file. DO NOT EDIT this block unless deploying a new version AND simultaneously bumping file name to v3.md (etc.).
```

- [ ] **Step 0.3: Verify the embedded content is identical to live**

Run:
```
RemoteTrigger action=get trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
```
Diff `events[0].data.message.content` against the embedded block in v2.md. Expected: byte-identical.

- [ ] **Step 0.4: Commit**

```bash
git add 03_Tools/morning-briefing-prompt-v2.md
git commit -m "docs(briefing): back-fill v2.md with embedded v2.2 prompt content for rollback integrity"
```

---

## Task 1: Write v3.0 prompt file

**Files:**
- Create: `03_Tools/morning-briefing-prompt-v3.md`

- [ ] **Step 1.1: Create file header + changelog**

Create `03_Tools/morning-briefing-prompt-v3.md` with this header:

```markdown
# Morning Briefing Remote Trigger — Prompt v3.0
**Trigger-ID:** `trig_01PyAVAxFpjbPkvXq7UrS2uG`
**Deployed:** <YYYY-MM-DD> (fill after deploy)
**Version:** v3.0 — Tavily News-Signal Integration

## Changelog

### v3.0 (2026-04-19) — Tavily News-Signal
- NEU: SCHRITT 4.5 — News-Signal via `mcp__tavily__tavily_search`
  - 1 Cohort-Query (alle 13 US-Ticker in einem Call)
  - max 5 Per-Ticker-Queries (nur bei Earnings <=3d, FLAG, Score-Alter >90d)
  - Slot-Struktur: 2 Slots reserviert fuer imminent earnings (earnings_in_days <= 1)
  - Tight Allowlist (12 Tier-1-Domains)
  - Materialitaets-Filter (7 positive, 4 negative Kriterien)
  - 6-Klassen-Fehler-Taxonomie, fail-open fuer Klassen 2-5
- NEU: Output-Sektion `--- NEWS-SIGNAL (letzte 24h) ---` zwischen KURS-CHECK und NAECHSTE TRIGGER
- ENTFERNT: Zeile "Keine News-Suche" aus WICHTIG-Liste (kollidiert mit neuer Funktionalitaet)
- Alle v2.2-Bestandteile unveraendert: FLAGS, AKTIVE WATCHES, KURS-CHECK, NAECHSTE TRIGGER, VERALTETE SCORES, AKTIONEN, GROSSES EVENT, WOCHENEND-MODUS

### v2.2 (17.04.2026) — siehe 03_Tools/morning-briefing-prompt-v2.md
### v2.1, v2, v1 — siehe v2.md

## Known Limitations v3.0

1. **Yahoo 403** (unveraendert) — BRK.B/RMS/SU-Kurse nicht verfuegbar aus Cloud-Umgebung.
2. **Push-Notifications** (unveraendert) — wartet auf Anthropic iOS Routines-Support.
3. **`RemoteTrigger run` API** (unveraendert) — noop fuer Cron-Trigger, manuell nur via Desktop App.
4. **Kein Delta fuer Yahoo-Symbole** (unveraendert).
5. **NEU: MCP Connector-Fail** — wenn `mcp.tavily.com` offline, kann Run bei Connector-Init abbrechen (prompt-unabfangbar). Mitigation: Monitoring erfasst fehlende News-Sektion, v3.1-Backlog fuer Healthcheck.
6. **NEU: Tavily Free-Tier** — 1000 Queries/Monat, geschaetzt 132/Monat worst-case (13.2%).
7. **NEU: Dev-Key-URL-Exposure** — Key in MCP-Connector-URL, Rotation monatlich empfohlen.

## API-Update-Regel (unveraendert, siehe v2.md)

## V3.1-Backlog
- [ ] Dedup gegen gestriges Briefing
- [ ] Allowlist-Dynamik (DEFCON-gewichtet)
- [ ] Automatische Materialitaets-Scoring-Auswertung
- [ ] Connector-Healthcheck-Fallback
- [ ] Key-Rotation-Automation
- [ ] EU-spezifische News-Quellen (falls RMS.PA/SU.PA-Quality unzureichend)
- [ ] Cloud-API fuer BRK.B/RMS/SU (Yahoo-Ersatz)

## Embedded Prompt Content (v3.0, active)

```
<v3.0 prompt content from Step 1.2>
```
```

- [ ] **Step 1.2: Write the v3.0 prompt content**

Append this exact content inside the embedded-block code fence:

```
Du bist der Dynasty-Depot Morning Briefing Agent. Sprache: Deutsch.

AUFTRAG: Erstelle ein kompaktes taegliches Depot-Briefing.

SCHRITT 1 — Wochentag pruefen:
- Lies das heutige Datum. Wenn Samstag oder Sonntag: springe zu WOCHENEND-MODUS.
- Wenn Montag bis Freitag: fahre mit Schritt 2 fort.

SCHRITT 2 — Kontext laden:

2a) Lies 00_Core/STATE.md:
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

SCHRITT 4 — Briefing generieren (erstmal nur Grundstruktur, News kommt in 4.5 dazwischen):

SCHRITT 4.5 — NEWS-SIGNAL (nur Werktag):

Wenn Wochenende: diesen Schritt ueberspringen.

(A) COHORT-QUERY — ein einziger MCP-Tool-Call:
Rufe mcp__tavily__tavily_search mit diesen Parametern auf:
  query: "ASML AVGO MSFT TMO VEEV V APH COST MKL SNPS SPGI RACE ZTS earnings guidance news"
  search_depth: "basic"
  time_range: "day"
  max_results: 10
  include_domains: ["reuters.com", "ft.com", "bloomberg.com", "wsj.com", "businesswire.com", "prnewswire.com", "globenewswire.com", "sec.gov", "marketbeat.com", "zacks.com", "finance.yahoo.com", "spglobal.com"]

Lies title + url + content aus jedem results[] Element. Wende Materialitaets-Filter an (siehe D).

(B) TRIGGER-LISTE BERECHNEN:
Aus STATE.md + Faktortabelle (bereits gelesen in Schritt 2):
  Fuer jeden Ticker im Portfolio pruefen:
    - earnings_in_days <= 3 ODER
    - FLAG aktiv ODER
    - score_age_days > 90
  Alle matchenden Ticker sammeln als trigger_candidates.

  SORTIERUNG mit Slot-Struktur (5 Slots gesamt):
    Slot 1-2 (reserviert fuer "imminent earnings" = earnings_in_days <= 1):
      Ticker mit earnings_in_days <= 1 zuerst einordnen, alphabetisch Tiebreaker.
      Wenn weniger als 2 solche Ticker: verbleibende Slots an Slot 3-5 freigeben.
    Slot 3-5 (allgemeine Prioritaet, composite key):
      priority_score = (FLAG_aktiv ? 100 : 0) + (score_age_days > 90 ? 50 : 0) + max(0, 30 - earnings_in_days)
      Sortiere nach priority_score absteigend.
      Tiebreaker 1: earnings_in_days aufsteigend.
      Tiebreaker 2: alphabetisch.

  triggered = finale Liste, max 5 Ticker.
  Wenn triggered leer ist: zeige "Keine getriggerten Ticker" in der Per-Ticker-Sektion. Dann skippe (C) komplett.

(C) PER-TICKER-QUERIES — max 5 MCP-Tool-Calls:
COMPANY_NAME-Map (diese Map IST Teil des Prompts — NICHT dynamisch aus Faktortabelle lesen, sie dient auch als Suncor/Hermes-Trap-Guard):
    ASML    -> "ASML Holding"
    AVGO    -> "Broadcom"
    MSFT    -> "Microsoft"
    TMO     -> "Thermo Fisher Scientific"
    VEEV    -> "Veeva Systems"
    V       -> "Visa Inc"
    APH     -> "Amphenol"
    COST    -> "Costco"
    MKL     -> "Markel Group"
    SNPS    -> "Synopsys"
    SPGI    -> "S&P Global"
    RACE    -> "Ferrari"
    ZTS     -> "Zoetis"
    BRK-B   -> "Berkshire Hathaway"
    RMS.PA  -> "Hermes International"    # NICHT Rockwell Medical, NICHT Rockwell Automation
    SU.PA   -> "Schneider Electric"      # NICHT Suncor Energy

Fuer jeden Ticker t in triggered:
  Bilde query-String: "<COMPANY_NAME> <TICKER> news"
  WICHTIG: Der query-String MUSS BEIDE enthalten — COMPANY_NAME UND TICKER. Nur COMPANY_NAME reicht nicht; nur TICKER reicht nicht.
  Beispiele korrekt:
    - "Thermo Fisher Scientific TMO news"
    - "Hermes International RMS.PA news"    (NICHT "Hermes RMS.PA news")
    - "Schneider Electric SU.PA news"       (NICHT "Schneider SU.PA news")

  Rufe mcp__tavily__tavily_search mit diesen Parametern auf:
    query: "<COMPANY_NAME> <TICKER> news"
    search_depth: "advanced"
    time_range: "day"
    max_results: 3
    include_domains: ["reuters.com", "ft.com", "bloomberg.com", "wsj.com", "businesswire.com", "prnewswire.com", "globenewswire.com", "sec.gov", "marketbeat.com", "zacks.com", "finance.yahoo.com", "spglobal.com"]

  Lies title + url + content aus jedem results[] Element. Wende Materialitaets-Filter an (siehe D).

(D) MATERIALITAETS-FILTER:
Fuer jede zurueckgegebene Headline pruefen: erfuellt sie mindestens eines dieser Kriterien?
  - Earnings-Announcement / Guidance-Update (mit Zahlen oder Richtung, nicht blosse Datumsankuendigung)
  - M&A / Partnership / Akquisition
  - Analyst-Rating-Action (Upgrade / Downgrade / konkrete Target-Aenderung mit Begruendung)
  - Regulatorisches Event (FDA, EMA, SEC Enforcement, 8-K Filing)
  - Management-Wechsel (CEO, CFO, Chief-Role)
  - Produkt-Launch / Recall / Material Lawsuit
  - Dividenden-Aenderung / Buyback-Announcement

AUSSCHLUSS (als Noise verwerfen):
  - "<TICKER> to report earnings on [Datum]" (reine Datumsankuendigung ohne Zahlen)
  - Weekly/Monthly Market-Roundups ohne Ticker-Fokus
  - "Top N Stocks"-Listen, Rankings, ETF-Hype-Pieces
  - Pure Opinion-Pieces, reine Price-Target-Predictions ohne neue Information

Pro Ticker zeige maximal 1 Headline (die hoechstgerangte, die den Filter passiert).
Wenn keine Headline material: behandle als "keine material News" fuer den Ticker.
Fuer Cohort: zeige bis zu 3 material Headlines.

(E) FEHLER-HANDLING:
Wenn mcp__tavily__tavily_search einen Fehler oder Error-Status zurueckgibt:

  HTTP 401/403 (Auth-Fehler):
    - Ausgabe im News-Signal-Header: "NEWS-SIGNAL: Auth-Fehler — Key rotieren"
    - Alle weiteren News-Queries SKIPPEN (weder weitere Per-Ticker noch Cohort)
    - Rest des Briefings NORMAL zu Ende fuehren

  HTTP 429 (Rate-Limit):
    - Ausgabe: "NEWS-SIGNAL: Rate-Limit erreicht (Budget ausgeschoepft)"
    - Alle weiteren News-Queries SKIPPEN
    - Rest des Briefings NORMAL zu Ende fuehren

  HTTP 400/422 (Bad Params):
    - Fuer Cohort: "Cohort: n.v. (bad request)"
    - Fuer Per-Ticker: "<TICKER> — n.v. (bad request)"
    - WEITER mit naechster Query / naechstem Schritt

  HTTP 5xx (Tavily down):
    - Fuer Cohort: "Cohort: n.v. (Tavily <code>)"
    - Fuer Per-Ticker: "<TICKER> — n.v. (Tavily <code>)"
    - WEITER

  Generischer MCP-Tool-Error (kein HTTP-Code, z.B. Protocol/Serialisation/Unknown):
    - Fuer Cohort: "Cohort: n.v. (tool-error)"
    - Fuer Per-Ticker: "<TICKER> — n.v. (tool-error)"
    - WEITER

  Response-Schema malformed (results[] fehlt oder unerwartetes Format):
    - Fuer Cohort: "Cohort: n.v. (parse-error)"
    - Fuer Per-Ticker: "<TICKER> — n.v. (parse-error)"
    - WEITER

  Valides Result aber results[] leer (KEIN Fehler):
    - Fuer Cohort: "Cohort: Keine material News"
    - Fuer Per-Ticker: "<TICKER> — keine News"

  Valides Result, results[] nicht-leer, aber Materialitaets-Filter verwirft alles (KEIN Fehler):
    - Fuer Cohort: "Cohort: Keine material News"
    - Fuer Per-Ticker: "<TICKER> — keine material News"

NIEMALS den Run komplett abbrechen. Fehler in Schritt 4.5 duerfen nur die News-Sektion degradieren.

Budget-Fallback: Wenn nach Cohort + 3 Per-Ticker-Queries bereits >60s Gesamt-Laufzeit vergangen sind (sichtbar am Agent-Timing), skippe die restlichen Per-Ticker-Queries und logge "NEWS-SIGNAL: Runtime-Budget gekappt, <n> Ticker nicht abgefragt".

SCHRITT 4 — Briefing generieren:
Formatiere exakt so:

---
MORNING BRIEFING — [Datum] [Wochentag] 10:00

--- FLAGS ---
Aktiv: [Alle aktiven FLAGs mit Grund aus Faktortabelle]
Review: [Alle unter Review]
(Oder: Keine aktiven FLAGs)

--- AKTIVE WATCHES ---
  [Bullets aus STATE.md Watches-Block — unveraendert uebernehmen]
  (Oder: Keine aktiven Watches)

--- KURS-CHECK (vs. Score-Datum) ---
Satelliten:
  [TICKER]  [Kurs]  [+/-X%]  Score [X] ([Datum])  Rate: [€]  [FLAG falls aktiv]  [Shibui|Yahoo]
  (Score-Datum == heute: zeige 'Score heute' statt Delta)
  (Yahoo-Titel: nur Kurs, kein Delta)
  (Rate aus STATE.md: volle Rate / halbe Rate / 0€ FLAG)

Ersatzbank:
  [TICKER]  [Kurs]  Score [X]  [Shibui]
  (Nur Titel mit dokumentiertem Score)

--- NEWS-SIGNAL (letzte 24h) ---
Cohort:
  [Headline kurz] ([Quelle-Domain])
  (Oder: Keine material Cohort-News)
  (Bei Fehler: analog §4.5(E) Klasse)

Per Ticker (nur getriggert, max 5):
  [TICKER] — [Headline] ([Quelle])
  (Oder: Keine getriggerten Ticker)
  (Oder pro Ticker: [TICKER] — keine News / keine material News / n.v. (<grund>))

--- NAECHSTE TRIGGER & EARNINGS (30 Tage) ---
  [Datum] [Ticker] [Klasse] — [Aktion/Kontext]
  (Kombiniert: STATE.md Trigger-Tabelle + Faktortabelle Earnings-Kalender, nach Datum sortiert)
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
- Lies STATE.md + Faktortabelle (KEIN Shibui-Call, KEIN Yahoo curl, KEIN Tavily-Call)
- Zeige: FLAGS, AKTIVE WATCHES, Earnings + Trigger naechste Woche, veraltete Scores, Empfehlung fuer Montag
- Kurzformat, kein Kurs-Check, kein News-Signal

WICHTIG:
- Keine Dateien aendern (read-only)
- Keine Score-Neuberechnung
- Output kompakt halten
- Keine Symbol-Varianten ausprobieren wenn eine Query fehlschlaegt
```

- [ ] **Step 1.3: Verify file is well-formed**

Run:
```bash
wc -l "03_Tools/morning-briefing-prompt-v3.md"
grep -c "SCHRITT 4.5" "03_Tools/morning-briefing-prompt-v3.md"
grep -c "Keine News-Suche" "03_Tools/morning-briefing-prompt-v3.md"
```
Expected:
- Line count: ~200+
- SCHRITT 4.5 occurrences: ≥2 (header in changelog + prompt body)
- "Keine News-Suche": 0 (removed — was in v2.2 WICHTIG list)

- [ ] **Step 1.4: Commit**

```bash
git add 03_Tools/morning-briefing-prompt-v3.md
git commit -m "feat(briefing): add v3.0 prompt with Tavily News-Signal integration"
```

---

## Task 2: Create test prompt fixtures

**Files:**
- Create: `03_Tools/tests/tavily-probe-prompts/README.md`
- Create: `03_Tools/tests/tavily-probe-prompts/T1-happy-path.md`
- Create: `03_Tools/tests/tavily-probe-prompts/T3-adversarial-trap.md`
- Create: `03_Tools/tests/tavily-probe-prompts/T4-fail-open.md`

- [ ] **Step 2.1: Create test README**

Create `03_Tools/tests/tavily-probe-prompts/README.md`:

```markdown
# Tavily Probe Prompts — Test Battery

Test prompts for the Morning-Briefing-v3.0 probe trigger `trig_01XYuQ5mugsvZGZD4K52rjXh`.
Each file contains a self-contained prompt for a specific test case.

## Running a test

1. Update probe trigger with the test prompt:
   - Use `RemoteTrigger action=update trigger_id=trig_01XYuQ5mugsvZGZD4K52rjXh body={...}`
   - Body must include full `ccr` (env_id, session_context with Bash+Read+Glob+Grep+mcp__tavily__tavily_search, events with the test content, mcp_connections with Shibui + Tavily UUIDs)
2. Open Claude Desktop App → Routines → tavily-probe → "Jetzt ausführen"
3. Wait for completion, copy output, compare against Expected-Output in the test file.

## Tests

- **T1** happy-path: full v3.0 prompt against real STATE.md, verify News-Sektion renders + slot-struktur + allowlist.
- **T2** (not a separate file): covered by T1 under different STATE (not mocked; real state suffices given current portfolio has mix of FLAGs/earnings).
- **T3** adversarial-trap: force SU.PA + RMS.PA queries, verify query-string content + no Suncor/Rockwell in results.
- **T4** fail-open: reuse Phase-0-R1-C bad-params pattern, verify 422 caught and run completes.
- **T5** (not a separate file): post-update content-verify, done in Task 9.
```

- [ ] **Step 2.2: Create T1 prompt**

Create `03_Tools/tests/tavily-probe-prompts/T1-happy-path.md` with this content:

```markdown
# T1 Happy-Path Test

**Setup:** Full v3.0 prompt (see 03_Tools/morning-briefing-prompt-v3.md "Embedded Prompt Content" block). Reads real STATE.md and Faktortabelle from main branch.

**Probe allowed_tools:** `["Bash", "Read", "Glob", "Grep", "mcp__tavily__tavily_search"]`

**Probe mcp_connections:** Shibui + Tavily (both UUIDs, see spec).

**Content:** Use the exact v3.0 prompt body (from v3.md Step 1.2). No modifications.

## Expected Output

- `--- FLAGS ---` section present (v2.2 behavior unchanged)
- `--- AKTIVE WATCHES ---` section present
- `--- KURS-CHECK ---` section present with all 16 symbols
- `--- NEWS-SIGNAL (letzte 24h) ---` section present with:
  - `Cohort:` sub-header with at least 1 headline from allowlist domain, OR "Keine material Cohort-News"
  - `Per Ticker (nur getriggert, max 5):` sub-header. At least some entries present given current portfolio state (TMO earnings 2026-04-23, ASML DEFCON-variant) — exact count depends on trigger computation on run-day.
- `--- NAECHSTE TRIGGER & EARNINGS ---` section present
- `--- VERALTETE SCORES ---` section present
- `--- AKTIONEN EMPFOHLEN ---` section present
- `--- NAECHSTES GROSSES EVENT ---` section present

## Pass Criteria

1. All sections render (kein Abbruch)
2. News-Signal-URLs nur von Allowlist-Domains (reuters/ft/bloomberg/wsj/businesswire/prnewswire/globenewswire/sec.gov/marketbeat/zacks/finance.yahoo/spglobal)
3. Keine Suncor-/Rockwell-Headlines auch wenn RMS.PA oder SU.PA in triggered-Liste
4. Laufzeit < 90s (vom "Jetzt ausführen"-Klick bis Output)
```

- [ ] **Step 2.3: Create T3 prompt**

Create `03_Tools/tests/tavily-probe-prompts/T3-adversarial-trap.md`:

```markdown
# T3 Adversarial Symbol-Trap Test

**Setup:** Modified v3.0 prompt that FORCES SU.PA and RMS.PA into the triggered-list for News-Query, bypassing the normal trigger-computation. Keeps everything else identical.

**Modification to v3.0 prompt:** Between SCHRITT 4.5 (B) and (C), insert this override:
```
OVERRIDE (T3 Test only): Ignoriere die regulaere Trigger-Liste. Setze triggered = ["SU.PA", "RMS.PA"] fix.
```

**Content to send to probe:** Full v3.0 prompt with the OVERRIDE inserted. Everything else unchanged.

## Expected Output

The News-Signal section must show:
- Cohort: normal behavior
- Per Ticker:
  - `SU.PA — <Headline>` with headline from Schneider Electric (NOT Suncor Energy)
  - `RMS.PA — <Headline>` with headline from Hermès International (NOT Rockwell Medical / Rockwell Automation / any unrelated "Hermes" hit)

## Pass Criteria (stricter than T1)

1. **Query-String Assertion (Codex Fix #1):** Inspect the ACTUAL tool invocation that the agent logs. Look for the `query` param passed to `mcp__tavily__tavily_search`. For each of SU.PA/RMS.PA query, the query-string MUST contain BOTH:
   - COMPANY_NAME ("Schneider Electric" / "Hermes International")
   - TICKER ("SU.PA" / "RMS.PA")
2. **Content Assertion:** Each returned headline must reference the CORRECT company. Manually read each headline and verify:
   - SU.PA results mention Schneider Electric, not Suncor (energy/oil sector news is a red flag)
   - RMS.PA results mention Hermès International (luxury goods), not Rockwell (automation/medical device sector news is a red flag)
3. **Adversarial injection:** If on the test day Suncor has high news volume (e.g., oil price shock), verify the allowlist + query-content combination still filters it out. This is the key protection Codex flagged.
```

- [ ] **Step 2.4: Create T4 prompt**

Create `03_Tools/tests/tavily-probe-prompts/T4-fail-open.md`:

```markdown
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
```

- [ ] **Step 2.5: Commit test fixtures**

```bash
git add 03_Tools/tests/tavily-probe-prompts/
git commit -m "test(briefing): add T1/T3/T4 probe prompt fixtures"
```

---

## Task 3: Configure probe trigger MCP + allowed_tools

**Context:** Probe currently has `allowed_tools: ["Bash","Read","Glob","Grep"]` (post-CLI-test) and Tavily in `mcp_connections`. Need to add `mcp__tavily__tavily_search` to allowed_tools. Shibui UUID needs adding too (for T1, which needs Shibui for Kurs-Check).

**Files:**
- None (API-only change)

- [ ] **Step 3.1: Build update body**

Pull current probe config first:
```
RemoteTrigger action=get trigger_id=trig_01XYuQ5mugsvZGZD4K52rjXh
```
Save `ccr.environment_id`, current `mcp_connections`, and `ccr.events[0].data.message.uuid`.

- [ ] **Step 3.2: Build and send update**

Call:
```
RemoteTrigger action=update
  trigger_id=trig_01XYuQ5mugsvZGZD4K52rjXh
  body={
    "job_config": {
      "ccr": {
        "environment_id": "env_01Ek3HiKjymFoWzrQoyvMTEk",
        "session_context": {
          "allowed_tools": ["Bash", "Read", "Glob", "Grep", "mcp__tavily__tavily_search"],
          "model": "claude-sonnet-4-6",
          "sources": [{"git_repository": {"url": "https://github.com/tobikowa90-hub/stie-depot"}}]
        },
        "events": [{
          "data": {
            "message": {
              "content": "<placeholder — gets overwritten per test in Task 4/5/6>",
              "role": "user"
            },
            "parent_tool_use_id": null,
            "session_id": "",
            "type": "user",
            "uuid": "<current event UUID from Step 3.1>"
          }
        }]
      }
    },
    "mcp_connections": [
      {"connector_uuid": "3ecc8248-4bff-4b40-bab2-9bff78a30413", "name": "Shibui-Finance", "permitted_tools": [], "url": "https://mcp.shibui.finance/mcp"},
      {"connector_uuid": "4a633350-7128-4729-b8be-85373854fa4d", "name": "Tavily", "permitted_tools": [], "url": "<current Tavily URL from Step 3.1>"}
    ]
  }
```

Note: `sources.git_repository.url` above has a typo. CORRECT value is `https://github.com/tobikowa90-hub/dynastie-depot`. Always copy from current config (Step 3.1) to avoid typos.

- [ ] **Step 3.3: Verify**

Call:
```
RemoteTrigger action=get trigger_id=trig_01XYuQ5mugsvZGZD4K52rjXh
```
Assert:
- `ccr.session_context.allowed_tools` contains `"mcp__tavily__tavily_search"`
- `mcp_connections` has 2 entries: Shibui (UUID `3ecc8248-…`) + Tavily (UUID `4a633350-…`)

---

## Task 4: Execute T1 (Happy-Path) on probe

**Files:** None (API + user-action)

- [ ] **Step 4.1: Push v3.0 prompt file to GitHub**

The probe trigger reads from main branch. For Step 4.2 we'll inline the prompt in the API payload (not via git). But push now for clean state:

```bash
git push origin main
```
Expected: Push succeeds. (If rejected due to upstream changes, pull --rebase first.)

- [ ] **Step 4.2: Set probe prompt to T1 content**

Copy the full v3.0 prompt body (from `03_Tools/morning-briefing-prompt-v3.md` Embedded Prompt Content block — line between the code fences in the "Embedded Prompt Content" section) into the probe's `events[0].data.message.content`.

Call `RemoteTrigger action=update` with:
- Same `ccr.session_context` and `mcp_connections` as Task 3 Step 3.2
- `events[0].data.message.content` = full v3.0 prompt body, character-for-character
- Fresh `events[0].data.message.uuid` (generate new or reuse — both acceptable)

- [ ] **Step 4.3: Verify probe has T1 content**

Call `RemoteTrigger action=get trigger_id=trig_01XYuQ5mugsvZGZD4K52rjXh`.

Grep-style checks on `events[0].data.message.content`:
- Contains "SCHRITT 4.5" — PASS
- Contains "mcp__tavily__tavily_search" — PASS
- Does NOT contain "Keine News-Suche" — PASS
- Contains allowlist domain "reuters.com" — PASS

- [ ] **Step 4.4: USER ACTION — Manual run in Desktop App**

Open Claude Desktop App → Routines → `tavily-probe` → click "Jetzt ausführen".

Wait for the run to complete (up to ~90s). Copy the full output (from `--- FLAGS ---` or `MORNING BRIEFING —` header through the final `---`).

- [ ] **Step 4.5: Validate T1 output against pass criteria**

Apply the 4 pass criteria from `T1-happy-path.md`:
1. All sections render — yes/no?
2. News-Signal-URLs nur von Allowlist-Domains — verify each URL domain is in allowlist
3. Keine Suncor-/Rockwell-Headlines — if RMS.PA/SU.PA in triggered, verify their headlines
4. Laufzeit <90s — check timestamp on Desktop App

If ALL 4 pass → T1 PASSED. Proceed to Task 5.
If ANY fail → STOP. Fix the v3.0 prompt and retry from Step 4.2 before moving on.

- [ ] **Step 4.6: Record T1 result**

Create a new file `03_Tools/tests/tavily-probe-prompts/results/T1-YYYY-MM-DD.md` (replace YYYY-MM-DD with today's date) with:
- Verdict: PASS / FAIL
- Run timestamp
- Output excerpt (News-Signal section only)
- Any anomalies observed

Commit:
```bash
git add 03_Tools/tests/tavily-probe-prompts/results/
git commit -m "test(briefing): T1 result <PASS|FAIL> <date>"
```

---

## Task 5: Execute T3 (Adversarial Symbol-Trap) on probe

**Files:**
- Create: `03_Tools/tests/tavily-probe-prompts/results/T3-YYYY-MM-DD.md`

- [ ] **Step 5.1: Build T3 prompt variant**

Take the full v3.0 prompt body. Insert between "triggered = finale Liste, max 5 Ticker." and "(C) PER-TICKER-QUERIES":

```
OVERRIDE (T3 Test only): Ignoriere die regulaere Trigger-Liste. Setze triggered = ["SU.PA", "RMS.PA"] fix.
```

- [ ] **Step 5.2: Update probe with T3 content**

Call `RemoteTrigger action=update` with:
- Same `ccr.session_context` and `mcp_connections` as Task 3 Step 3.2
- `events[0].data.message.content` = T3 variant from Step 5.1
- Fresh UUID

- [ ] **Step 5.3: USER ACTION — Manual run**

Desktop App → `tavily-probe` → "Jetzt ausführen". Wait. Copy output.

- [ ] **Step 5.4: Validate T3 pass criteria**

From `T3-adversarial-trap.md`:
1. **Query-String Assertion:** Check the agent's tool-call log (visible in Desktop App run trace). For each SU.PA/RMS.PA query, assert the `query` param contains:
   - SU.PA query: both "Schneider Electric" AND "SU.PA"
   - RMS.PA query: both "Hermes International" AND "RMS.PA"
2. **Content Assertion:** Read each returned headline:
   - SU.PA results must reference Schneider Electric — NOT Suncor Energy
   - RMS.PA results must reference Hermès International — NOT Rockwell Medical/Automation
3. Filter + allowlist combination held even if Suncor has active news on test day

If all 3 hold → T3 PASSED.

- [ ] **Step 5.5: Record T3 result**

Create `03_Tools/tests/tavily-probe-prompts/results/T3-YYYY-MM-DD.md` per Task 4 Step 4.6 pattern.

Commit.

---

## Task 6: Execute T4 (Fail-Open) on probe

**Files:**
- Create: `03_Tools/tests/tavily-probe-prompts/results/T4-YYYY-MM-DD.md`

- [ ] **Step 6.1: Update probe with T4 content**

Call `RemoteTrigger action=update` with:
- `ccr.session_context.allowed_tools` = `["mcp__tavily__tavily_search"]` (minimal)
- `mcp_connections` can keep both (Shibui + Tavily); harmless
- `events[0].data.message.content` = the T4 prompt content from `T4-fail-open.md` Step 2.4 (just the test prompt, not full v3.0)
- Fresh UUID

- [ ] **Step 6.2: USER ACTION — Manual run**

Desktop App → `tavily-probe` → "Jetzt ausführen". Wait. Copy output.

- [ ] **Step 6.3: Validate T4 pass criteria**

From `T4-fail-open.md`:
1. TEST A section has ≥1 real result (title + url)
2. TEST B section contains "FAIL-OPEN OK:" followed by error msg
3. Output reaches `---FERTIG---` marker

If all 3 → T4 PASSED.

- [ ] **Step 6.4: Record T4 result**

Create result file. Commit.

---

## Task 7: Gate review — all tests PASS?

- [ ] **Step 7.1: Verify**

Confirm:
- T1 PASSED (Task 4 Step 4.5)
- T3 PASSED (Task 5 Step 5.4)
- T4 PASSED (Task 6 Step 6.3)

If ANY failed → STOP here. Do not proceed to prod. Diagnose, fix v3.0 prompt, re-test from relevant task.

If ALL PASSED → proceed to Task 8 (production deploy).

---

## Task 8: Deploy v3.0 to production trigger

**Context:** All probe tests green. Now push to prod.

**Files:** None (API + user-action)

- [ ] **Step 8.1: Pull current prod config**

Call:
```
RemoteTrigger action=get trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
```

Save:
- `ccr.environment_id` (should be `env_01Ek3HiKjymFoWzrQoyvMTEk`)
- Current `mcp_connections` (Shibui + Tavily, both UUIDs + URLs)
- `ccr.events[0].data.message.uuid` (reuse this to keep continuity)

- [ ] **Step 8.2: Build prod update body**

```
body = {
  "job_config": {
    "ccr": {
      "environment_id": "env_01Ek3HiKjymFoWzrQoyvMTEk",
      "session_context": {
        "allowed_tools": ["Bash", "Read", "Glob", "Grep", "mcp__tavily__tavily_search"],
        "model": "claude-sonnet-4-6",
        "sources": [{"git_repository": {"url": "https://github.com/tobikowa90-hub/dynastie-depot"}}]
      },
      "events": [{
        "data": {
          "message": {
            "content": "<exact v3.0 prompt body from 03_Tools/morning-briefing-prompt-v3.md Embedded Prompt Content block>",
            "role": "user"
          },
          "parent_tool_use_id": null,
          "session_id": "",
          "type": "user",
          "uuid": "<existing UUID from Step 8.1>"
        }
      }]
    }
  },
  "mcp_connections": [
    {"connector_uuid": "3ecc8248-4bff-4b40-bab2-9bff78a30413", "name": "Shibui-Finance", "permitted_tools": [], "url": "https://mcp.shibui.finance/mcp"},
    {"connector_uuid": "4a633350-7128-4729-b8be-85373854fa4d", "name": "Tavily", "permitted_tools": [], "url": "<exact Tavily URL from Step 8.1>"}
  ]
}
```

- [ ] **Step 8.3: Send update**

Call:
```
RemoteTrigger action=update
  trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
  body=<from Step 8.2>
```
Expected: HTTP 200.

If HTTP != 200: STOP. Analyze error. Do NOT proceed.

---

## Task 9: Post-update content-verify (Codex Fix #7)

**Files:** None (API-only verification)

- [ ] **Step 9.1: Fetch prod trigger back**

```
RemoteTrigger action=get trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
```

- [ ] **Step 9.2: Run grep-style assertions**

Extract `trigger.job_config.ccr.events[0].data.message.content` (call it `content`).

Assert:
- `content.contains("SCHRITT 4.5")` → TRUE (new section landed)
- `content.contains("mcp__tavily__tavily_search")` → TRUE (new tool reference)
- `content.contains("Keine News-Suche")` → FALSE (old restriction removed)
- `trigger.job_config.ccr.session_context.allowed_tools` contains `"mcp__tavily__tavily_search"` → TRUE

If ALL 4 hold → proceed to Task 10.
If ANY fail → DO NOT run prod manually. Re-update from Task 8 Step 8.3.

---

## Task 10: Production manual-run verification

**Files:** None (user-action)

- [ ] **Step 10.1: USER ACTION — Manual run prod trigger**

Open Claude Desktop App → Routines → `morning-briefing` → click "Jetzt ausführen".

**Important:** This is the first real prod run with v3.0. Watch it finish (up to 90s).

- [ ] **Step 10.2: Copy and validate output**

Copy full output. Validate:

1. All v2.2 sections still render (FLAGS, WATCHES, KURS-CHECK, NAECHSTE TRIGGER, VERALTETE SCORES, AKTIONEN, GROSSES EVENT)
2. `--- NEWS-SIGNAL (letzte 24h) ---` section present between KURS-CHECK and NAECHSTE TRIGGER
3. Cohort-News or "Keine material Cohort-News"
4. Per-Ticker-News sinnvoll für aktuell getriggerte Tickers (z.B. TMO vor Earnings 23.04.)
5. Keine Suncor-/Rockwell-Treffer bei RMS.PA/SU.PA (falls in triggered-Liste)
6. Alle News-URLs von Allowlist-Domains
7. Laufzeit <90s

- [ ] **Step 10.3: Record prod run**

Create `03_Tools/tests/tavily-probe-prompts/results/prod-first-run-YYYY-MM-DD.md` with output excerpt + verdict.

Commit.

- [ ] **Step 10.4: Deploy decision**

If all 7 checks pass → deploy succeeded. Proceed to Task 11 (post-deploy housekeeping).

If any fail → ROLLBACK per Task 12.

---

## Task 11: Post-deploy housekeeping

**Files:**
- Modify: `memory/morning-briefing-config.md`
- Modify: `00_Core/CORE-MEMORY.md`
- Modify: `00_Core/STATE.md` (only if relevant)
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md`

- [ ] **Step 11.1: Update memory/morning-briefing-config.md**

Edit `memory/morning-briefing-config.md`:
- Bump version line to `v3.0 (deployed YYYY-MM-DD MESZ)`
- Update `Prompt source of truth:` to `03_Tools/morning-briefing-prompt-v3.md`
- Append to "Known limitations": `NEU: MCP Connector-Fail-Risk (v3.1-Backlog)` + `NEU: Tavily 1000/mo budget, ~132/mo worst-case`
- Append section "v3.0 Tavily Integration" with: Connector UUID, allowlist, trigger criteria

- [ ] **Step 11.2: Update 00_Core/CORE-MEMORY.md**

Per CLAUDE.md §4 protocol, append to §10 Audit-Log:
- Date
- Event: "Morning Briefing v3.0 deployed — Tavily News-Signal integration"
- Key numbers: 1 Cohort-Query + 0-5 Per-Ticker-Queries daily; budget 132/1000 free-tier
- Reference: spec `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md`, plan `docs/superpowers/plans/2026-04-19-tavily-morning-briefing.md`

- [ ] **Step 11.3: Update log.md in Obsidian Vault**

Append to `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md`:
- Date
- 1-line entry: "Morning Briefing v3.0 go-live (Tavily News-Signal integration, Codex-reviewed, slot-reserved trigger-list, fail-open-errors)"

- [ ] **Step 11.4: Commit housekeeping**

```bash
git add memory/morning-briefing-config.md 00_Core/CORE-MEMORY.md "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md"
git commit -m "docs(briefing): post-deploy housekeeping for v3.0 go-live"
git push origin main
```

---

## Task 12: Rollback procedure (only if Task 10 failed)

**Context:** If any production validation failed in Task 10. Execute the exact runbook from spec §11.

**Files:** None (API)

- [ ] **Step 12.1: Read v2.2 content from v2.md**

Open `03_Tools/morning-briefing-prompt-v2.md`. Copy the EXACT content from the "Embedded Prompt Content" block between the code fences.

- [ ] **Step 12.2: Pull current prod baseline**

```
RemoteTrigger action=get trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
```
Save `mcp_connections` verbatim (Shibui + Tavily entries).

- [ ] **Step 12.3: Assemble rollback body**

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
            "content": "<EXACT v2.2 content from Step 12.1>",
            "role": "user"
          },
          "parent_tool_use_id": null,
          "session_id": "",
          "type": "user",
          "uuid": "<existing UUID from Step 12.2 or generate new>"
        }
      }]
    }
  }
}
```
Note: mcp_connections OMITTED from rollback body — Anthropic keeps existing connections if not specified. Tavily-UUID stays attached but tool is inert without allowed_tools.

- [ ] **Step 12.4: Send rollback update**

```
RemoteTrigger action=update
  trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
  body=<from Step 12.3>
```

- [ ] **Step 12.5: Verify rollback**

```
RemoteTrigger action=get trigger_id=trig_01PyAVAxFpjbPkvXq7UrS2uG
```
Assert:
- `content.contains("Keine News-Suche")` → TRUE (v2.2 restored)
- `content.contains("SCHRITT 4.5")` → FALSE (v3.0 removed)
- `allowed_tools` does NOT contain `mcp__tavily__tavily_search`

- [ ] **Step 12.6: USER ACTION — Manual run to confirm rollback**

Desktop App → `morning-briefing` → "Jetzt ausführen". Verify output matches v2.2 format (no News-Signal section).

- [ ] **Step 12.7: Commit rollback decision**

Create `03_Tools/tests/tavily-probe-prompts/results/rollback-YYYY-MM-DD.md` describing what failed, what was rolled back, what to investigate next.

Commit + push.

---

## Task 13: Day 1-3 monitoring

**Context:** Per spec §12, 3-day post-deploy monitoring window.

**Files:**
- Create: `03_Tools/tests/tavily-probe-prompts/results/monitoring-YYYY-MM-DD.md` (3 entries, one per day)

- [ ] **Step 13.1: Day 1 review (same day as deploy)**

After the first cron run at 10:00 MESZ next morning (or after manual go-live run):

Create `03_Tools/tests/tavily-probe-prompts/results/monitoring-day1-YYYY-MM-DD.md`:
- Run timestamp
- News-Signal-Sektion: Cohort + Per-Ticker headlines (listed)
- Pro Headline: `material=yes/no` + Kriterium (Earnings / M&A / Rating / Regulatory / Management / Product / Dividend / "NOISE - Reason")
- Threshold-Check: ≥70% material?

- [ ] **Step 13.2: Day 2 review**

Next trading day 10:00. Same format as Step 13.1. File `monitoring-day2-YYYY-MM-DD.md`.

Check additionally:
- Runtime trend (compared to Day 1)
- Any Fehlerpfade ausgelöst?

- [ ] **Step 13.3: Day 3 review + Tavily Dashboard**

Next trading day. File `monitoring-day3-YYYY-MM-DD.md`.

Plus:
- Open https://app.tavily.com → Dashboard
- Note: total queries consumed in last 3 days
- Threshold: sollte <18 sein (3 Tage × 6/Tag worst-case)

- [ ] **Step 13.4: Threshold-Action**

Per spec §12 "Action auf Threshold-Unterschreitung":
- **≥70% material:** OK. Monitoring beendet. Deployment declared stabil.
- **70-60%:** Allowlist um 1-2 Domains kürzen, Zurück zu Task 8 mit angepasstem Prompt
- **<60%:** Query-Formulierung anpassen, Task 8
- **<40%:** ROLLBACK (Task 12), Design-Review nötig

- [ ] **Step 13.5: Final monitoring commit**

```bash
git add 03_Tools/tests/tavily-probe-prompts/results/monitoring-day*.md
git commit -m "docs(briefing): day 1-3 monitoring results, v3.0 deployment declared <stable|requires adjustment>"
git push origin main
```

---

## Appendix: Key-Rotation Reminder

Per spec Risk #4 (Key-URL-Exposure, HIGH severity):
- After successful go-live, rotate the Tavily Dev-Key within 7 days.
- Workflow: Tavily Dashboard → API Keys → delete old key → new key → `claude mcp` commands to update LOCAL registration AND `RemoteTrigger update` to update prod/probe `mcp_connections.url`.
- This is NOT blocking for go-live — it's a scheduled-ops item.
