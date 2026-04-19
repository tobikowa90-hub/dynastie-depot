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
