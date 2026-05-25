# Session-Handover xlsx-smoke-test-runner (Skill v0.1 — operational)

**Status**: ✅ Stage-2 KOMPLETT 2026-05-25 — Skill produktiv, alle SPEC §8 Akzeptanz-Kriterien erfüllt.

## Aktueller Stand

- **Skill operational** seit Commit `84a1aa9` (2026-05-25)
- **3 Module**: `safe_insert.py` (169 LOC) · `verify_wrapper.py` (130 LOC) · Hook-§G in `03_Tools/precommit/xlsx_smoke_test.py`
- **54/54 pytest GREEN** · Hook rc=0 gegen 3 Live-xlsx · §G Σ=285 MATCH gegen Live config.yaml

## Commit-Lineage

| Commit | Phase | Inhalt |
|--------|-------|--------|
| `ecf3b12` | Substrate | SPEC v0.1 + drift-doc + Klasse-D §D-Block-Rewrite |
| `53efb7b` | Schritt 5 | safe_insert + verify_wrapper + 24 Tests (Codex 7/7 adressiert) |
| `49750cc` | Schritt 6 | Hook-§G + P13 sheets-Expand + 15 Tests (Codex 3/3 adressiert) |
| `84a1aa9` | Schritte 7+8 | 15 Fixtures Generator + 16 Integration-Tests + Regex-Fix |

## v0.2-Deferred (NICHT v0.1-Blocker)

- **Codex-R3 MED-1**: `_resolve_profil` startswith → regex full-match (`^<Profil>_v\d+\.\d+\.xlsx$`). NOTE-Kommentar in xlsx_smoke_test.py Z83. Trigger: Backup-Filename-Kollision.
- **C4 Cross-Sheet-Refs systematisch** (drift-doc §1.4): aktuell nur Stichprobe (B4, B16). Trigger: Real-Incident.
- **C5 4-Felder-Annotation-Schema** (drift-doc §5): formal Verification-Metadata-Schema. Trigger: ≥2 Real-Runs.
- **Promotion-Schwelle**: 2 echte Real-Runs vor v0.2-Iteration (Memory `feedback_redefer_over_prespec_dynastie`).

## Cross-Reference

- SPEC: `SPEC.md` (635 LOC, GO-Ready post 2× Sparring)
- Drift-Doc: `drift-live-vs-doc.md` (16 Patches, Substrate verbraucht)
- Hook: `03_Tools/precommit/xlsx_smoke_test.py` (P13 sheets + §G integriert)
- Fixtures: `_fixtures/_generate_fixtures.py` (Generator gitignored = deterministisch regenerable)
- Tests: `tests/test_{safe_insert,verify_wrapper,hook_g,fixtures_integration}.py` (54 total)

## Re-Open-Trigger (für künftige Sessions)

Nur bei: (a) Real-Incident gegen v0.2-Deferred, (b) Hook-Latency >100ms in Production, (c) neuer Drift-Befund gegen Live-xlsx. Sonst Skill ist done.
