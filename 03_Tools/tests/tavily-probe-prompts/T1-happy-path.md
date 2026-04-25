# T1 Happy-Path Test

**Setup:** Full v3.0 prompt (see 03_Tools/morning-briefing-prompt-v3.md "Embedded Prompt Content" block). Reads real PORTFOLIO.md and Faktortabelle from main branch.

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
