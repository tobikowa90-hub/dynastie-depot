# Pattern Specs — core-slim-refactor v0.1

Vollständige Pattern-Definitionen: siehe `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` Sektion 1.3 + 3.1.

Dieser Doc liefert nur User-fokussiertes Quick-Reference + die empirischen Known-Pitfalls aus den 4 manuellen Iterationen.

---

## Pattern A — Bucket-Archive

**Use-Case:** Semantic row-cluster (Ruflo-Sunset, MCP-Setup-History, abgeschlossene Initiativen) wird out-of-band archiviert und durch 1 chronologischen Pointer-Eintrag ersetzt.

**Mechanik:**
1. `classify`: Zeilen die `keywords` enthalten → `archive`. Zeilen die `keep_keywords` enthalten → IMMER `keep` (auch wenn `keywords` matchen, KEEP gewinnt). Alle anderen Tabellenzeilen → `keep`.
2. `mutate`: Aus dem Section-Anchor-Bereich werden alle `archive`-Zeilen entfernt; **1** Pointer-Zeile wird chronologisch eingefügt (per `insert_at` und `pointer_date`).

**Worked-Example:** `references/configs/ruflo-sunset-bucket.yaml`.

---

## Pattern B — Slim-Convention

**Use-Case:** Fat-Rows > `fat_threshold_bytes` (Default 3500b) werden in-place komprimiert zu `**Bold-Title** Outcome (max N chars) — [Archive](...), PIPELINE ..., git ...`. Verbatim-Kopie aller fat-rows landet im Archive.

**Mechanik:**
1. `classify`: Tabellenzeile > threshold UND nicht in `exclude_keywords` UND Datum nicht in `exclude_dates` → `slim_targets` + `archive`. Sonst `keep`.
2. `mutate`: Jede slim-target-Zeile wird durch ihre slim-Version ersetzt (Bold-Title-Extract + Body-Truncate auf `outcome_max_chars` + Pointer-Tail mit PIPELINE-IDs und Short-SHAs).

**Worked-Example:** `references/configs/defcon-fat-rows-slim.yaml`.

---

## Pattern C — Date-Cut

**Use-Case:** Banner/Chronicle wird vor `cut_before` wholesale archiviert. Pointer-Header (mit Archive-Link) ersetzt die archivierten Einträge.

**Mechanik:**
1. `classify`: Markdown-Entries per `date_parser.pattern` separiert. Header-Datum `< cut_before` → `archive`; Header-Datum `>= cut_before` → `keep`. **Strikt less-than:** Datum gleich `cut_before` ist POST-cut.
2. `mutate`: Pre-cut-Entries werden komplett entfernt. 1 Pointer-Header (per `pointer.template`) wird am Section-Top eingefügt.

**HARTE Constraint (Codex-R1 HIGH-2):** `pattern=date-cut` erfordert `target.section: null` (wholesale-archive Semantik). Section-scoped date-cut ist **NICHT** in v0.1 supported — Config schlägt fail-close mit `ConfigError`.

**Worked-Example:** `references/configs/session-handover-date-cut.yaml` (Plan v0.1 nutzte SESSION-HANDOVER.md als target; Build-Stage Wave-6 hat auf `07_Obsidian Vault/.../log.md` umgestellt da SESSION-HANDOVER keine `## YYYY-MM-DD`-Headers hat).

---

## Known-Pitfalls (4-Iter Empirie + Build-Stage)

Erfahrungen aus den 4 manuellen Iterationen (`05_Archiv/refactor-tools/2026-05-23/`) und der v0.1 Build-Stage:

1. **Migrate-before-Strip-Lücke** — Wenn `keywords` einen semantischen Tag treffen der NUR in `archive`-Rows existiert (kein `keep`-Row trägt ihn), geht der Tag implizit verloren. Mitigation: explizit prüfen ob alle wichtigen tags noch in `keep` vorhanden sind. Skill v0.1 hat dafür noch KEIN explicit-check — TODO v0.2.
2. **Pointer-Stub-Vergesslichkeit** — Mutate-Operationen ohne Pointer-Stub hinterlassen "tote" Sections die Reader verwirren. v0.1 erzwingt 1 Pointer pro Pattern.
3. **Backlink-Leak** — §-References in CLAUDE.md/INSTRUKTIONEN/Vault auf den slim-Range zeigen ins Leere. P3 Backlink-Scan ist PFLICHT (fail-close-default).
4. **Fat-Row-Definition-Drift** — Slim-Convention im Project-Code default 3500b. Wenn andere Tools (Linter, Pre-Commit) anders messen (codepoints vs bytes), entsteht Drift. v0.1 misst konsistent in UTF-8-Bytes (`len(row.encode('utf-8'))`).
5. **Empty-Classify-Trap** — Wenn `classify` 0 rows liefert (z.B. cut_before zu früh, keywords zu eng), failed P2 mit `EXIT_CLASSIFY_EMPTY=4`. Das ist beabsichtigt — Skill macht keine no-op-runs.
6. **YAML executed-Field Re-Run-Trap** — Configs mit populated `executed`-Block (retroaktiv-Doku) blocken Re-Run hart. `--force-rerun` ist die einzige Override (für Reference-Archive-Match-Tests).

---

## Cross-Reference

- Spec-Section 1.3 (Phase-DAG-Summary): `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md#13-8-phase-pipeline-summary`
- Spec-Section 3.1 (Phase-DAG-Table mit Failure-Modes): same file §3.1
- Empirie-Substrate: `05_Archiv/refactor-tools/2026-05-23/` (README.md + 3 Python-Scripts)
