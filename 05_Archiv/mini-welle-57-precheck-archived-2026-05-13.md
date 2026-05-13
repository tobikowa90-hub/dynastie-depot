# Mini-Welle #57 — Pre-Welle-Precheck (vorbereitet 2026-05-12 spätabends)

**Zweck:** In neuer Session direkt nach Session-Restart `cat .swarm/mini-welle-57-precheck.md` lesen, dann blind-Ausführung von Step 4.1.5 + folgenden Schritten von #57 ohne Discovery-Loop.

**Persistiert:** `.swarm/` (gitignored, an MCP-Server-State-Ort, konsistent mit `.swarm/rollback-stage.txt`-Pattern).

**SSoT-Pointer:**
- Plan: `docs/superpowers/plans/2026-05-12-ruflo-bridge-upgrade-alpha21.md` (gitignored, 854 LOC)
- PIPELINE: `00_Core/PIPELINE.md` #57
- Resume-Checkliste: `00_Core/SYSTEM.md §Ruflo-Status`

---

## Step 4.1.5 — Tool-Schema-Discovery-Snippet (FIRST-GATE)

**Ausführen sofort nach Session-Restart, bevor irgendwas anderes:**

```text
# In Claude Code Session via Bash:
echo "=== Step 4.1.5 — Tool-Schema-Introspection ==="

# (a) MCP-Server-Tools verfügbar?
# In Claude Code prüfen: ist mcp__ruflo__memory_import_claude im Tool-Index?
# Falls Tool-Index nicht direkt einsehbar, einen No-Op-Call versuchen
# (z.B. mit absichtlich invalidem Parameter um Schema-Error zu erzwingen)
```

**Was zu prüfen ist (in fresh Claude-Code-Session via Tool-Aufruf):**

1. **Tool `mcp__ruflo__memory_import_claude` verfügbar?**
   - ToolSearch query: `"select:mcp__ruflo__memory_import_claude"`
   - Erwarteter Output: JSONSchema mit Parameter-Liste
   
2. **Hat das Schema einen `projectPath`-Parameter (oder ähnliches: `path`, `projectDir`, `cwd`)?**
   - **PASS-Fall:** Parameter exposed → Weiter mit Step 4.2 unter Verwendung des expliziten Parameters
   - **STOP-GATE-Fall:** Parameter NICHT exposed (Plan-Annahme aus PR #1886-Body Drift gegen Reality)

**STOP-GATE-4.1.5 Decision-Tree (User-Approval erforderlich):**

| Beobachtung | Decision-Option |
|---|---|
| Schema hat `projectPath` o.ä. | ✅ PROCEED mit explizitem Parameter |
| Schema hat NUR `allProjects: bool` | ⚠️ User-Approval-A: `allProjects=false` über native cwd-Detection (Bug-A-Fix-Pfad ohne Hint) — Risiko: cwd-Drift wenn WSL/Win32-cwd asymmetrisch |
| Schema komplett anders (Major-Refactor in alpha.27) | ⛔ Plan-Pause + Codex-Sparring auf neue API |

**Default-Empfehlung wenn STOP-GATE:** Option-A (`allProjects=false` + native cwd) probieren — wenn `imported >= 39` zurückkommt, ist Bug-A faktisch gefixt auch ohne projectPath-Hint. Wenn `imported: 0` wie 12.05.: alpha.21-Behavior **unverändert** zu v3.6.11 → Bug-A-Fix nicht greifbar in unserem Setup → Rollback-Plan oder Plan-Pause.

---

## Step 4.2-4.5 — Bridge-Smoke-Test (post 4.1.5 PASS)

**Plan-Steps direkt aus** `docs/superpowers/plans/2026-05-12-ruflo-bridge-upgrade-alpha21.md` Z.298-440:

- Step 4.2: path-scoped Re-Import via `memory_import_claude({allProjects:false, projectPath:"..."})` ODER native cwd-Detection
- Step 4.3: Post-Import Verify (Erwartung: `imported >= 39` Dynastie-MD-Files)
- Step 4.4: Cross-Project-Pollution-Check (Post-Import-Count `claude:C--Users-tobia-Code:*` darf NICHT größer sein als Pre-Import-Count)
- Step 4.5: Bug-B-Verify 5-Step-Sequence mit voller `DANGEROUS_KEY_CHARS`-Klasse (Write/Read/Search/Delete/Post-Delete)
- Step 6.4: Behavioral-Verify `memory_search "BRK.B Earnings Call"` mit similarity ≥ 0.7

**Backup vor Step 4.2 verpflichtend:** `cp .swarm/memory.db .swarm/memory.db.pre-import-2026-05-13` (oder aktuelles Datum).

---

## Step (c) — MD-File-Migration Code-Pfad → OneDrive-Pfad (DISCOVERY KOMPLETT)

**Discovery-Output 2026-05-12 spätabends:**

- Code-Pfad MDs: **22** in `C:\Users\tobia\.claude\projects\C--Users-tobia-Code\memory\`
- OneDrive-Pfad MDs: **46** in `C:\Users\tobia\.claude\projects\C--Users-tobia-OneDrive-Desktop-Claude-Stuff\memory\`
- In beiden: **16** (Konflikt-Analyse unten)
- Unique-in-Code: **6** (Migration-Pflicht, sonst Data-Loss bei Sweep)
- Unique-in-OneDrive: **30** (kein Migration-Bedarf, sind die "modernen" Dynastie-Memories post-30.04.)

### Migration-Action-Tabelle

#### Bucket A — Unique-in-Code (6 Files, MUST-COPY)

Diese existieren NUR im Code-Pfad. Bei Sweep ohne Migration = echter Data-Loss.

| File | mtime | Size | Action |
|------|-------|------|--------|
| `feedback_core_folder_lean_discipline.md` | 2026-05-05 12:23 | 1653 B | Copy → OneDrive |
| `feedback_cr_convergence_and_project_compat.md` | 2026-05-08 15:15 | 3818 B | Copy → OneDrive |
| `feedback_cr_pass_after_bulk_refactor.md` | 2026-05-07 05:10 | 3159 B | Copy → OneDrive |
| `feedback_multi_commit_wip_resume.md` | 2026-05-05 16:17 | 2238 B | Copy → OneDrive |
| `reference_coderabbit_via_wsl.md` | 2026-04-26 21:04 | 2547 B | ⚠️ STALE post-12.05.-Migration + Topic-Duplikat — siehe Bucket-C-Edge unten |
| `reference_dynastie_log_location.md` | 2026-05-09 21:08 | 1551 B | Copy → OneDrive |

#### Bucket B — In-beiden, IDENTISCH (11 Files, no-op-Migration)

SHA256 identisch in beiden Pfaden. Code-Version kann gelöscht werden ohne Verlust, OneDrive-Version bleibt unverändert.

```
feedback_anchor_promotion_sync_gap.md
feedback_brk_no_earnings_call.md
feedback_codex_sparring_heuristic.md
feedback_earnings_call_wait_discipline.md
feedback_no_visualization_skills_dynastie.md
feedback_onedrive_edit_collision.md
feedback_pre_commit_diff_inspection.md
feedback_review_via_codex_not_advisor.md
feedback_skill_methodology_drift_v_q2.md
feedback_windows_python_crlf_text_mode.md
reference_defeatbeta_mcp_setup.md
reference_video_analysis_path.md
```

Action: nichts zu mergen, Code-Versionen können direkt mit Sweep (Step d) entsorgt werden.

#### Bucket C — In-beiden, OD-NEWER (4 Files, OneDrive gewinnt)

OneDrive-Version ist content-newer; Code-Version ist stale. Action: Code-Version verwerfen (Default: newer-mtime-wins).

| File | Code mtime | OD mtime | Action |
|------|-----------|----------|--------|
| `feedback_ruflo_memory_bridge_onedrive_pitfall.md` | 2026-04-30 15:21 | 2026-05-12 21:13 | OD-Version behalten (heute spätabends verengt auf Cloud-Sync-Risiken) |
| `feedback_tavily_connector_uuid_rotation.md` | 2026-04-27 21:40 | 2026-05-07 20:02 | OD-Version behalten |
| `MEMORY.md` | 2026-05-11 23:02 | 2026-05-12 21:14 | OD-Version behalten (Index ist live im OneDrive-Pfad, Code-Index stale) |
| (1 weiterer falls Drift entsteht zwischen Pre-Welle-Doc und Mini-Welle-Execution) | — | — | — |

#### Bucket D — In-beiden, CODE-NEWER (1 File, ⚠️ Code gewinnt!)

| File | Code mtime | OD mtime | Diff |
|------|-----------|----------|------|
| `feedback_xlsx_tools_in_sync_set.md` | 2026-05-11 23:02 | 2026-05-02 22:30 | Code-Version hat 11.05.-§18.7-Smoke-Test-Punkt-6 (zusätzliche Zeilen 40-41). OD-Version ist 9 Tage älter. |

**Action:** Code-Version **muss OneDrive-Version überschreiben** (sonst geht §18.7-Update verloren). Das ist der einzige File wo der Default "OneDrive-wins" NICHT gilt.

**Root-Cause-Hypothese (informational):** Edit am 11.05. 23:02 lief vermutlich aus einer Code-cwd-Session, nicht aus Dynastie-cwd → Auto-Memory-Hook hat den Patch in den Code-Pfad-Hash geschrieben statt OneDrive-Hash. Erinnert an Bug-A. Konsistent mit Pre-alpha.21-cwd-Resolution-Bug.

#### Bucket C-Edge — Rename-Verdacht `reference_coderabbit_via_wsl.md` ↔ `coderabbit_cli_via_wsl.md`

Beide Files behandeln gleiches Topic (CodeRabbit-CLI über WSL). Code-Version (`reference_coderabbit_via_wsl.md`, 2547 B, 26.04.) ist alte Stub. OneDrive-Version (`coderabbit_cli_via_wsl.md`, 5700 B, 02.05.) ist neuere richtere Doku. **Beide sind post-12.05.-Migration STALE** (CodeRabbit lebt jetzt in Ubuntu-24.04, user `tobia` — beide Files sprechen von alter Distro `Ubuntu` user `tobiatobia`).

**Action:**
1. Code-Version `reference_coderabbit_via_wsl.md` als Bucket-B-äquivalent behandeln (nicht migrieren, sweep mit Code-Pfad)
2. OneDrive-Version `coderabbit_cli_via_wsl.md` post-Welle separat updaten (ist im `bewusst NICHT angefasst`-Block von Commit f800250 als "separate Mini-Commit deferred" markiert).

### Konflikt-Resolution-Policy (Plan-Addendum für #57 Step c)

**Default:** newer-mtime-wins, ABER:

1. **Bucket A (unique-in-Code):** copy → OneDrive, kein Konflikt möglich
2. **Bucket B (identisch):** no-op, Code-Version kann silent gelöscht werden
3. **Bucket C (OD-newer):** OneDrive behält, Code-Version silent gelöscht
4. **Bucket D (Code-newer):** Code-Version überschreibt OneDrive (NICHT default-OneDrive-wins!)
5. **Bucket C-Edge (Rename-Verdacht):** Code-Version löschen, OneDrive-Version post-#57 separat updaten
6. **Frische Drifts zwischen heute (12.05.) und #57-Execution:** Re-Run dieser Discovery-Sequenz vor Step (c), Buckets neu zuordnen, dann Policy anwenden

**Pre-Step-(c)-Backup verpflichtend:** vor jedem `cp` oder `mv` Snapshot des OneDrive-memory-Dirs nach `~/.claude/projects/C--Users-tobia-OneDrive-Desktop-Claude-Stuff/memory.backup-pre-mini-welle-57/` (rekursiv, mtime-preserve).

---

## Step (d) — Stranded-Keys-SQL-Sweep (post Step c PASS)

Nach Migration sollten die 26 + 25 = 51 `claude:C--Users-tobia-Code:*`-Keys in der DB jetzt entweder:
- Identisch zu OneDrive-Pendants (sweep-safe) — gilt für Bucket-B + Bucket-C
- Bereits unter neuem Pfad-Hash via Re-Import (sweep-safe) — gilt für Bucket-A nach erfolgreicher Step-4.2-Re-Import inkl. migrierter Source-Files
- Bucket-D-xlsx: spezielle Behandlung — vor Sweep der Code-Pfad-Hash-DB-Eintrag muss content den NEUEN Code-Version-Content haben (nicht den alten OD-Stand). Wenn Re-Import den Code-Source-File (jetzt mit Punkt-6-Smoke-Test) gelesen hat, gibt's einen Konflikt: zwei DB-Einträge mit verschiedenen Pfad-Hash-Präfixen aber unterschiedlichem Content. Auflösung: nach Migration die Code-Source-File löschen, dann Re-Import erneut → ein konsistenter DB-Eintrag mit OneDrive-Pfad-Hash.

**SQL-Sweep (aus Plan Z.520-585):**

```bash
# Pre-Sweep Backup verpflichtend
cp .swarm/memory.db .swarm/memory.db.pre-sweep-2026-05-13   # aktuelles Datum

# 1. Count Pre-Sweep
sqlite3 .swarm/memory.db "SELECT namespace, COUNT(*) FROM memory_entries WHERE key LIKE 'claude:C--Users-tobia-Code:%' GROUP BY namespace;"

# 2. Sweep
sqlite3 .swarm/memory.db "DELETE FROM memory_entries WHERE key LIKE 'claude:C--Users-tobia-Code:%';"

# 3. Count Post-Sweep (Erwartung: 0)
sqlite3 .swarm/memory.db "SELECT COUNT(*) FROM memory_entries WHERE key LIKE 'claude:C--Users-tobia-Code:%';"
```

**Acceptance:** AC4 (Post-Import-Count Code-Präfix ≤ Pre-Import-Count) + AC6 (Stranded-Keys-Count post-Sweep = 0).

---

## Exit-Criteria-Checkliste (für Verdict-Stempel)

- [ ] **AC3:** `imported >= 39` Dynastie-MD-Files nach Step 4.2 Re-Import
- [ ] **AC4:** Kein NEUER Cross-Project-Pollution post-Import (Post-Count ≤ Pre-Count für `claude:C--Users-tobia-Code:*`)
- [ ] **AC5:** Bug-B 5-Step-Sequence Write/Read/Search/Delete/Post-Delete alle PASS mit voller `DANGEROUS_KEY_CHARS`-Klasse
- [ ] **AC6:** Stranded-Keys-Count post-Sweep = 0 für `claude:C--Users-tobia-Code:*`
- [ ] **AC7:** `memory_search "BRK.B Earnings Call"` mit similarity ≥ 0.7
- [ ] Bucket-A-Migration: 5 Files copy-to-OneDrive (6 minus 1 Stale-Rename `reference_coderabbit_via_wsl.md`)
- [ ] Bucket-D-xlsx: Code-Version überschreibt OneDrive-Version, dann Code-Source gelöscht, dann Re-Import konsistent
- [ ] Backup pre-import-2026-05-13 + pre-sweep-2026-05-13 erstellt

**Bei vollem PASS:** PIPELINE #57 ⚠️ PENDING → ✅ DONE, dann §18-System-Event-Sync-Welle (SYSTEM + PIPELINE + STATE + CORE-MEMORY §13 + log.md). PIPELINE #50 bleibt ⚠️ PARTIAL (Plan-AC-Block historisch zementiert in commit f800250).

**Bei AC3 PASS aber AC5/AC7 FAIL:** Mini-Welle wird Sub-PARTIAL — neue Mini-Mini-Welle für isolierten Bug-B-Re-Verify.

**Bei AC3 FAIL (`imported: 0` wie 12.05.):** alpha.21-Behavior unverändert in unserem Setup → Bug-A nicht fixed → ⛔ STOP + Codex-Sparring auf neue Hypothese (Setup-spezifisches Issue jenseits PR #1886-Scope).

---

## Open Questions (User-Entscheidung in neuer Session)

1. **Step 4.1.5 Schema-Drift Decision:** Falls `projectPath` nicht exposed, automatisch Option-A (`allProjects=false` + native cwd) oder erst Codex-Sparring?
2. **Bucket-D-xlsx Spezial-Behandlung:** Code-Version überschreibt OneDrive sofort, oder erst manueller Content-Diff-Review (User-Bestätigung dass Punkt-6-Add gewollt war)?
3. **Bucket-C-Edge Rename:** `reference_coderabbit_via_wsl.md` jetzt sweep-safe löschen (Dupe-Topic), oder behalten bis post-Mini-Welle CodeRabbit-Doku-Update?
4. **Memory-Pitfall-Doc-Split (separate Mini-Mini-Welle):** dem #57-Run beifügen oder nach #57 als Side-Track?

**Empfehlung:**
- Q1: automatisch Option-A — wenn das fehlschlägt (AC3 FAIL), sowieso Codex
- Q2: Code-Version überschreibt OneDrive sofort (Punkt-6-Add ist real, am 11.05. committed im Repo-Spec §18.7 — die Code-Pfad-Memory ist konsistent zum Repo, die OneDrive-Memory war stale)
- Q3: Sweep-safe löschen, separater CodeRabbit-Doku-Update wie geplant
- Q4: Memory-Doc-Split ist bereits in dieser Session (12.05. spätabends) erfolgt — die OneDrive-Version `feedback_ruflo_memory_bridge_onedrive_pitfall.md` ist heute neu (OD-NEWER, Bucket C), `feedback_ruflo_memory_bridge_path_hash_pitfall.md` ist NEU (Unique-in-OneDrive, kein Code-Pendant). Beide bleiben in #57-Migration unangetastet.

---

*Pre-Welle-Precheck v1.0 | Erstellt 2026-05-12 spätabends post-Codex-R2-Sparring | Verbraucht in neuer Session 1× Read, dann blind-Ausführung möglich*
