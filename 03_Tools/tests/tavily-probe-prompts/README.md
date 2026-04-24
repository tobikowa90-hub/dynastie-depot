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

- **T1** happy-path: full v3.0 prompt against real PORTFOLIO.md, verify News-Sektion renders + slot-struktur + allowlist.
- **T2** (not a separate file): covered by T1 under different PORTFOLIO state (not mocked; real state suffices given current portfolio has mix of FLAGs/earnings).
- **T3** adversarial-trap: force SU.PA + RMS.PA queries, verify query-string content + no Suncor/Rockwell in results.
- **T4** fail-open: reuse Phase-0-R1-C bad-params pattern, verify 422 caught and run completes.
- **T5** (not a separate file): post-update content-verify, done in Task 9.
