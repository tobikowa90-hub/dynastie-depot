# Design Spec — Tavily Integration in Morning Briefing

**Date:** 2026-04-19 (v3.0.3 rebase: 2026-04-20; v3.0.4 Anti-Fallback-Hotfix: 2026-04-27; v3.0.5 Bucket-B Provenance-Architecture: 2026-04-27, siehe Revision Log unten)
**Author:** Tobias Kowalski (via Claude + 2× Codex review rounds + v3.0.3 rebase review + v3.0.4 post-incident hotfix + v3.0.5 Bucket-B Provenance-Architecture, 5 Codex Brainstorm-Runden)
**Status:** Spec aktualisiert für v3.0.5 (Provenance-Contract als §3.0 + §6F Mismatch-Klassen + §9 T6 Adversarial-Provenance-Test; Prompt-SoT-Bump v3.0.4→v3.0.5 + Probe-Deploy + T1/T3/T4/T5/T6-Tests + Prod-Deploy noch ausstehend — Implementation-Plan folgt aus writing-plans-Phase nach diesem Spec-Commit)
**Target:** Morning Briefing Remote Trigger `trig_01PyAVAxFpjbPkvXq7UrS2uG`, prompt v2.2 → v3.0.3 (rolled back) → v2.2 stable Prod → v3.0.4 (Hotfix-Wording, nie deployed) → v3.0.5 (Provenance-Architecture, in Vorbereitung)
**Architecture:** **MCP via `mcp__tavily__tavily_search`** (CLI-Pivot wurde 2026-04-19 getestet, musste zurückgenommen werden — Tavily Dev-Keys haben REST-Host-Allowlist; nur MCP-Proxy-Pfad funktioniert ohne Paid-Plan. Siehe Appendix D.)
**Spec location:** `03_Tools/specs/` (co-located with prompt files; `docs/superpowers/plans/` existiert für Implementation-Plans, aber Spec bleibt bei Prompt-SoT-Co-Location)

### Revision Log
- **v3.0 (2026-04-19):** Initial MCP-based Tavily integration with hard 90s PASS / >90s×2 Rollback-Gate in §6(E) Klasse 6.
- **v3.0.1 (2026-04-20):** TZ='Europe/Berlin' hotfix for weekday detection (prompt-level, no spec change).
- **v3.0.2 (2026-04-20):** Sequenzierungs-Direktive SCHRITT 3 → 4.5 (prompt-level, no spec change).
- **v3.0.3 (2026-04-20):** Lever-1 Yahoo-Gap-Elimination + Soft-Alert-Rebase. Rationale: T1-Rerun FAIL mit 360s bei funktional korrekter Ausgabe + User-Prinzip "Korrektheit > Laufzeit" (feedback_correctness_over_runtime memory). Hard 90s-Rollback-Gate in §6(E) Klasse 6 + 60s-Budget-Fallback ENTFERNT. Ersetzt durch Soft-Alert-Schema <180s healthy / 180-400s observe / >400s alert (kein Auto-Rollback). Per-Ticker-Calls laufen vollstaendig durch. §8 Error-Handling-Tabelle, §11 Rollback-Trigger, §12 Monitoring-Tabelle, §13 Risk #9 entsprechend aktualisiert.
- **v3.0.4 (2026-04-27):** Anti-Fallback-Guard für US-Kurs-Pfad. Post-Incident-Hotfix nach v3.0.3-Halluzination 20.04.2026 Nacht-Spät (Manual-Run gab Phantom-Intraday-Kurse für 7 US-Ticker aus, Ursache: Shibui-EOD lieferte 17.04. als latest_date wegen Karfreitag/Osterwochenende, Agent improvisierte unautorisierten Yahoo/Tavily-Live-Preis-Fallback). v3.0.3 wurde 20.04. auf v2.2 zurückgerollt (Commit `4cfa421`); Prod läuft seither v2.2.
  - **Spec-Änderung §3a US-Kurse (Prompt-Wording):** Drei neue Direktiven (i) `AUTORITATIVE-DATA-QUELLE-REGEL` (Shibui `latest_date` ist per Definition autoritativ — kein "stale"), (ii) `NICHT-STALE-DEFINITION` (Wochenend-/Feiertags-/EOD-Lag = korrektes Verhalten, kein Fehler), (iii) `VERBOTENE-FALLBACK-PFADE` (kein Yahoo-curl, kein Tavily-Search, keine alternativen Live-Preis-Quellen für US-Ticker), (iv) `DELTA-BERECHNUNG bei Stale-Shibui` (3 Edge-Case-Branches: latest_date<score / ==score / >score).
  - **Spec-Änderung §3 Critical Guards:** Zwei neue Bullets — (a) "NIEMALS alternative Live-Preis-Datenquellen für US-Ticker", (b) "NIEMALS improvisieren — bei nicht abgedecktem Szenario konservativ als n.v. markieren".
  - **Test-Suite-Erweiterung:** Neuer Probe-Test **T5 Adversarial-Stale-Shibui** (verifiziert dass Agent bei latest_date<heute keinen Fallback improvisiert). Gate-A-Re-Start-Kriterien erweitert auf T5 PASS + T1/T3/T4 Retest PASS.
  - **Non-Goals:** Keine Tavily-Entfernung (News-Pfad §4.5 nicht betroffen — Halluzination war im Kurs-Pfad §3, nicht im News-Pfad). Kein Runtime-Ziel — Korrektheit > Laufzeit bleibt oberstes Prinzip.
  - **Hotfix-Plan:** `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks). Hotfix-Lessons in Sektion "Lessons Learned" des Plans dokumentiert (Anti-Hallucination-Guards zweigleisig: Narrativ + Datenpfad; Edge-Case-Definitionen explizit; autoritative Quellen als Sprach-Anker; Probe-Tests mit Adversarial-Scenarios).
- **v3.0.5 (2026-04-27):** Bucket-B Provenance-Architecture — strukturelle Härtung des Anti-Hallucination-Patterns. v3.0.4 hat den Datenpfad narrativ adressiert (CRITICAL GUARDS Wording, "VERBOTENE FALLBACK-PFADE"). v3.0.5 verankert dasselbe Prinzip strukturell als first-class Provenance-Contract: Output-Felder werden auf autoritative Quellen gemapped, ein Pre-Output-Self-Check-Gate verhindert unmapped Emit, sichtbare `[source_ref@source_date]`-Tags machen die Quellen-Bindung im Output beweisbar. v3.0.4-Wording bleibt unverändert als Defense-in-Depth-Layer (Narrativ + Struktur). Spec-Phase deckt Foundation, Implementation folgt via writing-plans-Plan.
  - **Spec-Änderungen:**
    - **§3.0 NEU — Provenance-Contract** (vor §3 Background): drei Komponenten — (a) Field→Source-Map mit 5 Feldern (Kurs / Delta multi-source / News-Headline / News-Domain / Earnings-Datum) und Source-Klassen `external` vs. `file-read-derived`; (b) Emit-Only-If-Mapped-Self-Check-Gate (5-Zeilen-Reverse-Map vor Output-Assembly); (c) Output-Source-Tag-Pflicht im Format `[source_ref@source_date]`.
    - **§6F NEU — Mismatch-Klassen-Taxonomie** (analog §6E-Pattern, flach mit Sub-Buckets): 6 Klassen — Lag / Schema-Drift / Auth-Access-Fail / Cross-Source-Mismatch / File-Sync-Drift / Missing-File-Row. Uniform Output-Template `[FIELD] — n.v. (<type>: [source_ref@source_date])`. `source_date` im Tag = tatsächlich gelieferter Ist-Wert (nicht Soll-Wert). Cross-Reference §6F → §6E (kein Doppel-Klassen-Logging — Mismatches als Folge von §6E-Primärfehlern referenzieren §6E).
    - **§9 erweitert — T6 Adversarial-Provenance-Test:** verifiziert Tag-Pflicht, Tag-Authentizität (manueller Cross-Check gegen `RemoteTrigger get`-Tool-Response-Log), §6F-Klassen-Compliance bei Mismatch-Trigger. Pre-Deploy-Gate-Bedingung. Auto-Capture-Diff-Skript ist v3.1-Backlog (manueller Verify reicht für 5 Felder).
    - **§13 Risk-Tabelle:** neue Mitigations für Risk #11 (Halluzinations-Tag-Fabrikation, mitigiert via T6 manuelle Authentizitäts-Verifikation) und Risk #12 (File-Sync-Drift PORTFOLIO/Faktortabelle, mitigiert via §6F-5 + Self-Check-Gate-Anker).
    - **§14 v3.1-Backlog:** neuer Eintrag "T6-Auto-Capture-Diff-Skript" (Automation der Tag-Authentizitäts-Verifikation, aktiviert wenn Map-Scope auf >10 Felder wächst oder Frequenz steigt).
  - **Klarstellungs-Bullets in §6F:**
    - `source_date` im Mismatch-Tag bezeichnet immer das tatsächlich gelieferte Datum (Ist-Wert). Erwartetes Datum (Soll-Wert) gehört in die Klassen-Beschreibung, nicht ins Tag.
    - Klasse 6F-1 Lag bei Delta-Sub-Components: Prompt-SCHRITT-3a-Branches aus v3.0.4 (`AUTORITATIVE-DATA-QUELLE-REGEL` + `DELTA-BERECHNUNG bei Stale-Shibui` mit drei Edge-Case-Branches latest<score / ==score / >score) bleiben SoT. §6F-1 referenziert die Prompt-Branches, generisches `n.v.`-Template gilt nicht für Delta. Lag wird über Tag-`source_date` transparent gemacht ohne `n.v.`-Wechsel.
    - "Unknown-Field-Request" (Agent will nicht-mapped Feld emittieren) ist KEINE §6F-Klasse, sondern wird im §3.0(b) Self-Check-Gate als Pre-Output-Outcome behandelt → konservativ `n.v.`.
  - **Prompt-Änderungen** (Bump v3.0.4 → v3.0.5):
    - Neuer SCHRITT 4.8 — Provenance-Self-Check (5-Zeilen-Reverse-Map-Gate zwischen SCHRITT 4.5 und Briefing-Assembly).
    - Field→Source-Map als embedded Markdown-Tabelle vor SCHRITT 3.
    - §6F-Klassen-Liste als embedded Tabelle nach SCHRITT 4.5(E).
    - Tag-Format-Direktive in den Output-Format-Sektionen (KURS-CHECK, NEWS-SIGNAL, AKTIONEN/Earnings).
    - Critical Guards: 1 neuer Bullet ("Vor Emit: Self-Check-Gate; bei Unmapped → konservativ n.v., kein Versuch alternative Quellen zu finden. Tag-Pflicht: jedes sensible Feld trägt `[source_ref@source_date]`.").
  - **Non-Goals v3.0.5:** Keine JSON-Output-Schema-Migration (Output bleibt Markdown, Tags additiv). Keine Auto-Capture-Layer-Implementierung (manueller Cross-Check ausreichend für 5-Felder-Scope). Keine Erweiterung des Map-Scopes auf File-Read-Pass-Through-Felder (FLAG/Score/Watches/Trigger/Sparrate bleiben out-of-scope, weil empirisch nicht halluzinations-prone — analog Q2-Scope-Entscheidung B).
  - **Brainstorm-Trace:** 5 Codex-Runden (Q1 Aufteilung D⁺ → Q2 Scope B → Q3 Mechanik B+C → Q4 Mismatch-Klassen-Achse A' → Q5 Tag-Format-Detailfragen). Vollständig dokumentiert im design-Kontext, finale Approve-Sequenz vom User.

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

## 3.0 Provenance-Contract (NEU v3.0.5 — Bucket-B Foundation)

**Zweck:** Strukturelle Härtung gegen Daten-Halluzination im Briefing-Output. Anti-Hallucination-Pattern wird zweigleisig gefahren — narrativer Layer (v3.0.4 CRITICAL GUARDS „NIEMALS alternative Live-Preis-Datenquellen") + struktureller Layer (dieser Abschnitt). Beide gleichzeitig aktiv, ersetzen sich nicht.

**Auslöser:** 20.04.2026-Incident (Phantom-Kurse für 7 US-Ticker im Manual-Run). Root-Cause war ein unbeobachteter Write-Path: Agent emittierte Werte, die nicht aus der dokumentierten Quelle kamen. v3.0.4-Wording adressierte das narrativ; ohne Write-Path-Enforcement bleibt der Schutz aber Compliance-abhängig (Codex-Befund Round 1).

### (a) Field→Source-Map

Bindende Tabelle: nur Felder in dieser Map dürfen im Briefing erscheinen. Andere Output-Felder werden über Self-Check-Gate (b) gestoppt.

| Output-Feld | Source(s) | Source-Klasse | Lese-Tool / Pfad | Verbotene Alternativen |
|---|---|---|---|---|
| `Kurs` | `latest_close@latest_date` | external | `shibui_stock_data_query` (CTE auf `stock_quotes`, `rn=1`) | Yahoo curl, Tavily, alle Live-Feeds, geschätzte Werte |
| `Delta` | `latest_close@latest_date` + `score_date_close@score_date` | external (×2) | `shibui_stock_data_query` (jeweilige Date-Filter) | Live-Feeds, geschätzte Vergleichswerte, gerundete Approximationen |
| `News-Headline` | `tavily_results[i].title` (wörtlich) | external | `mcp__tavily__tavily_search` | Erfindung, Zusammenfassung mehrerer Headlines, Headline-Umschreibung, Übersetzung |
| `News-Domain` | `urlparse(tavily_results[i].url).host` | external | `mcp__tavily__tavily_search` | Off-Allowlist-Domains, IR-URLs ohne Tavily-Treffer, geratene Quellen |
| `Earnings-Datum` | `Faktortabelle.md / Update-Kalender` (wörtlicher Spalten-Wert) | file-read-derived | `Read` | Erfindung, Datumsrundung („~Ende Juli" → konkretes Datum), Locale-Konversion, Schätzung |

**Source-Klassen-Definition:**
- **`external`** — Wert kommt aus einem MCP-Tool-Call (Shibui, Tavily). Halluzinations-Prävention erfordert Tag-Authentizität (Codex-Hinweis Runde 3: erfundene Tags formal korrekt aussehbar).
- **`file-read-derived`** — Wert kommt aus einer Repo-Datei via Read. Technisch deterministisch, semantisch driftbar (Datumsrundung, Format-Reinterpretation). Schwächere Halluzinations-Risikoklasse, aber nicht null.

Felder *außerhalb* dieser Map (FLAG, Score, Watches, Trigger-Datum, Sparrate, Score-Datum) sind **out-of-scope für v3.0.5** — Pass-Through aus PORTFOLIO.md/Faktortabelle.md, empirisch nicht halluzinations-prone. Erweiterung Richtung C-Scope ist v3.1+-Material falls Bedarf entsteht.

### (b) Emit-Only-If-Mapped — Self-Check-Gate

**Verankerung:** SCHRITT 4.8 im Prompt, zwischen SCHRITT 4.5 (News-Signal-Block-Ende) und Briefing-Assembly (SCHRITT 4 Output-Format-Block — Sequenz im Prompt: 1 → 2 → 3 → 4.5 → 4.8 → 4 Output-Format).

**Implementation-Status (Stand v3.0.5-Spec-Commit):** Prompt-File `03_Tools/morning-briefing-prompt-v3.md` ist im Repo aktuell auf v3.0.3-Rollback-Stand und enthält SCHRITT 4.8 noch NICHT. Auch v3.0.4-Hotfix-Wording (CRITICAL GUARDS Anti-Fallback) und v3.0.5-Provenance-Layer (Map-Tabelle, SCHRITT 4.8, Tag-Direktive) werden gemeinsam im writing-plans-Implementation-Phase nach diesem Spec-Commit eingespielt. Spec geht der Prompt-File-Implementation voraus (Spec=WHAT/WHY, Plan/Prompt-Edit=HOW). Das ist gewünschte Phasen-Trennung, kein Drift.

**Form:** kompakte 5-Zeilen-Reverse-Map-Liste. Bewusst nicht 50-Zeilen-Prozedurblock — Codex-Befund Runde 3: lange Self-Check-Listen werden unter Runtime-Stress nur oberflächlich abgearbeitet.

```
SCHRITT 4.8 — PROVENANCE-SELF-CHECK (vor Briefing-Output, KRITISCH):
Vor Ausgabe pruefen:
  - Kurs mapped auf shibui_stock_quotes@latest_date?
  - Delta mapped auf latest_close@latest_date UND score_date_close@score_date?
  - Headline+Domain aus dem GLEICHEN tavily_results[i]?
  - Earnings-Datum aus Faktortabelle.md/Update-Kalender (woertlich)?
  - Ist ein Feld unmapped oder nicht im §3.0-Schema → emittiere n.v., NICHT improvisieren.
```

**Outcome bei Unmapped-Detection:** konservativ `n.v.`, kein Versuch alternative Quellen zu finden. Das ist der Pre-Output-Pfad für „Unknown-Field-Request" — keine §6F-Klasse, sondern Self-Check-Gate-Outcome.

### (c) Output-Source-Tag-Pflicht

**Format:** `[source_ref@source_date]` (mittel-strikt, Codex-Empfehlung Runde 3). `[Shibui]` allein ist für T6 zu schwach; JSON-Schema wäre Scope-Creep.

**Tag-Beispiele pro Feld:**

| Feld | Tag-Beispiel im Output |
|---|---|
| Kurs | `Kurs: 406,54$ [shibui_stock_quotes@2026-04-25]` |
| Delta (Multi-Source dual-tagged) | `+2,3% [shibui_stock_quotes@2026-04-25; score_date=2026-03-20]` |
| News-Headline + Domain | `[TICKER] — "Headline" [tavily@reuters.com,2026-04-25]` |
| Earnings-Datum | `Q2 ~Ende Juli [file:Faktortabelle.md/Update-Kalender]` |
| Mismatch-Fall (jede §6F-Klasse) | `Kurs — n.v. (source-lag: [shibui_stock_quotes@2026-04-22])` |

**Delta dual-tagged** (Codex-Empfehlung Runde 5): beide Sources sichtbar, weil Single-Tag die Markt-Frische versteckt. T6-Strenge schlägt Lesbarkeits-Komprimierung.

**Earnings-Tag voll** (Codex-Empfehlung Runde 5): Sektions-Zeiger zwingend für Grep-Eindeutigkeit. `[file:Faktortabelle]` allein ist zu mehrdeutig.

**Mismatch-Tag-Semantik:** `source_date` = tatsächlich gelieferter Ist-Wert (siehe §6F-Klarstellungs-Bullet).

### Cross-References

- **§6F Mismatch-Klassen-Taxonomie** definiert die Output-Form bei Source-Konflikten (`[FIELD] — n.v. (<type>: [source_ref@source_date])`).
- **§9 T6 Adversarial-Provenance-Test** verifiziert Tag-Pflicht, Tag-Authentizität, Klassen-Compliance — Pre-Deploy-Gate.
- **Prompt-SCHRITT-3a-Branches (v3.0.4)** bleiben SoT für Delta-Berechnungs-Edges (Score-Date-vs-Latest-Date). §6F-1 Lag referenziert diese Prompt-Branches für den Delta-Spezialfall — generisches `n.v.`-Template gilt für Delta nicht.

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
- **Prompt-Size:** Kein dokumentiertes Limit bekannt; 32 MB Anthropic-Request-Cap. v2.2 ~9.5kB, v3.0.3 ~18.6kB (Stand 27.04.2026) — unkritisch unter Cap.

### New Dependency
- **Tavily MCP (hosted):** `https://mcp.tavily.com/mcp/?tavilyApiKey=<KEY>`
- **Connector-UUID:** `4a633350-7128-4729-b8be-85373854fa4d` (registriert via Claude.ai Web-UI, 2026-04-19)
- **Tool exposé:** `mcp__tavily__tavily_search` (empirisch verifiziert, Phase 0 Round 1 Test B)
- **CLI-Pivot-Attempt (abgebrochen):** Direkte REST-Calls an `api.tavily.com` vom Remote-Trigger-Runtime schlagen fehl mit HTTP 403 "Host not in allowlist". Tavily Dev-Keys (Free-Tier only) sind auf MCP-Proxy beschränkt. Details in Appendix D.

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
    │   └─ Tavily          (UUID 4a633350-…)  ← already attached via UI
    ├─ session_context.allowed_tools:
    │   ├─ Bash, Read, Glob, Grep
    │   └─ mcp__tavily__tavily_search         ← NEU
    └─ events[0].data.message.content =
        Prompt v3.0.x (Target: v3.0.5 — aktiv im Repo: v3.0.3 Rollback-Stand; v3.0.4 Hotfix-Wording wurde nie deployed, v3.0.5 in Vorbereitung)
            ├─ Schritt 1-3: unveraendert (v2.2-Logik)
            ├─ SCHRITT 4.5: NEUE News-Sektion via tavily_search
            └─ Schritt 4+: unveraendert, neue News-Section im Output
```

### Change Summary (exactly 2)
1. **`ccr.session_context.allowed_tools`:** Append `"mcp__tavily__tavily_search"`
2. **`ccr.events[0].data.message.content`:** Replace with v3.0 prompt (v2.2 + neue SCHRITT 4.5 MCP-basierte News + neue Output-Sektion + "Keine News-Suche"-Zeile entfernt)

**Keine Änderung an `mcp_connections`** — Tavily-Connector bereits via Claude.ai Web-UI angehängt.

### Design Rationale (MCP beibehalten, CLI verworfen)
1. **Empirisch bewiesen:** Phase 0 Round 1 Tests A/B/C alle PASS (UUID-Binding, Tool-Connectivity, Fail-Open via HTTP 422)
2. **Free-Tier-kompatibel:** Tavily Dev-Keys (Free-Plan 1000 Credits/Monat) akzeptieren ausschließlich den MCP-Proxy-Pfad
3. **CLI-Alternative ging nicht:** REST `api.tavily.com` retourniert 403 "Host not in allowlist" für Dev-Keys (Phase 0 Round 2)
4. **Residual-Trade-off:** Connector-Offline-Risk (MEDIUM) + URL-Query-Key-Exposure (HIGH, Dev-Key only, rotierbar) akzeptiert

### Isolation
News-Sektion ist zwischen KURS-CHECK und NAECHSTE TRIGGER eingeschoben. Alle anderen Sektionen (FLAGS, WATCHES, VERALTETE SCORES, AKTIONEN, GROSSES EVENT, WOCHENEND-MODUS) unverändert. Shibui-MCP und Yahoo-curl bleiben wie in v2.2.

---

## 6. Components & Prompt Logic

### New Section in Prompt v3.0: SCHRITT 4.5 — NEWS-SIGNAL (via mcp__tavily__tavily_search)

```
SCHRITT 4.5 — NEWS-SIGNAL (nur Werktag):

(A) COHORT-QUERY — 1 MCP-Tool-Call:
  mcp__tavily__tavily_search(
    query: "ASML AVGO MSFT TMO VEEV V APH COST MKL SNPS SPGI RACE ZTS earnings guidance news",
    search_depth: "basic",
    time_range: "day",
    max_results: 10,
    include_domains: [<ALLOWLIST>]
  )

  Response: MCP liefert strukturiertes JSON mit results[], jedes Element
  enthält title, url, content, score. Agent extrahiert title + url pro Result.

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

(C) PER-TICKER-QUERIES — max 5 MCP-Tool-Calls:
  FOR t in triggered:
    QUERY_STRING muss MINDESTENS enthalten:
      - COMPANY_NAME(t) (aus Map unten) UND
      - TICKER(t) symbol

    Format: "<COMPANY_NAME(t)> <TICKER(t)> news"

    mcp__tavily__tavily_search(
      query: "<COMPANY_NAME> <TICKER> news",
      search_depth: "advanced",
      time_range: "day",
      max_results: 3,
      include_domains: [<ALLOWLIST>]
    )

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

(E) FEHLER-HANDLING (für MCP-Architektur, Codex Fix #4):

  KLASSE 1 — MCP Connector-Fail / Runtime-Error:
    - Tavily-MCP-Server nicht erreichbar, Connector-Init fehlschlägt
    - Ist KEIN fail-open-Pfad — Runtime wirft typischerweise Tool-Error bevor Agent reagiert
    - Mitigation: Monitoring erfasst fehlende News-Sektion; v3.1-Backlog für Healthcheck

  KLASSE 2 — Tool-Error (tavily_search returns error structure):
    - 401/403 (Auth): "NEWS-SIGNAL: Auth-Fehler — Key rotieren"; alle weiteren Queries skippen
    - 429 (Rate-Limit): "NEWS-SIGNAL: Rate-Limit erreicht (Budget ausgeschöpft)"; alle weiteren Queries skippen
    - 5xx (Tavily down): "Cohort: n.v. (Tavily <code>)" bzw. "<TICKER> — n.v. (Tavily <code>)"; weiter
    - 400/422 (Bad params): "Cohort: n.v. (bad request)" bzw. "<TICKER> — n.v. (bad request)"; weiter
    - 2z (Generisch: MCP-Tool-Error ohne HTTP-Code, z.B. Protocol-Error,
       Serialisation-Error, unbekannter Fehler): "Cohort: n.v. (tool-error: <kurz>)"
       bzw. "<TICKER> — n.v. (tool-error)"; weiter
    - Phase 0 Round 1 Test C bestätigt: 422 wird sauber gecatched, Run läuft durch

  KLASSE 3 — Response-Schema unerwartet:
    - `results[]` fehlt oder malformed in JSON-Struktur
    - Log "Cohort: n.v. (parse-error)" bzw. "<TICKER> — n.v. (parse-error)"
    - Weiter mit nächstem Ticker

  KLASSE 4 — Valides Result aber results[] leer:
    - "Cohort: Keine material News" bzw. "<TICKER> — keine News"
      (kein Fehler, sondern normaler Zero-Match)

  KLASSE 5 — Valides Result, results[] nicht-leer, aber nach Materialitäts-Filter alles Noise:
    - "Cohort: Keine material News" bzw. "<TICKER> — keine material News"

  KLASSE 6 — Runtime-Monitoring (v3.0.3 rebased: Soft-Alert statt Hard-Gate):
    Grund fuer die Rebase: User-Prinzip 2026-04-20 "Korrektheit > Laufzeit". Runtime
    allein darf NIE einen Rollback ausloesen solange die Ausgabe funktional korrekt
    ist. Das urspruengliche <90s-Hard-Gate aus v3.0 erzwang implizit eine Tavily-
    Per-Ticker-Kuerzung und kollidierte damit mit dem Korrektheits-Prinzip.

    SOFT-ALERT-SCHEMA:
      - <180s:       HEALTHY — nicht logwuerdig
      - 180s-400s:   OBSERVE — in Run-Log notieren, keine Aktion
      - >400s:       ALERT — manuellen Review triggern (nicht automatisch rollback)
      - Absoluter Oberrand: durch Desktop-App/Runtime-Limit gegeben (empirisch offen,
        vermutlich ~600s) — wenn der Runtime selbst den Run killt, greift Klasse 1
        (Runtime-Error) nicht Klasse 6.

    WICHTIG: Kein Tool-Call-Skip aus Runtime-Gruenden. Der frueher definierte 60s-
    Budget-Fallback wird ebenfalls entfernt (s.u.), weil er Recall gegen Laufzeit
    eintauscht. Per-Ticker-Calls laufen vollstaendig durch, solange der Runtime-
    Timeout selbst nicht zuschlaegt.

    Historie: v3.0 setzte <90s als PASS / >90s×2 als Rollback-Gate. v3.0.3 rebased
    auf obiges Soft-Alert-Schema nach Codex-Review (T1-FAIL 2026-04-20 mit 360s bei
    funktional korrekter Ausgabe).

  Budget-Fallback (v3.0.3 ENTFERNT):
    Der frueher definierte 60s-Budget-Fallback ("skippe restliche Per-Ticker-Queries
    wenn >60s verbraucht") wurde mit v3.0.3 entfernt. Begruendung: er implementierte
    Laufzeit-Gewinn durch Recall-Regression — ein getriggerter Ticker wurde bei knappem
    Budget ohne Material-News-Check uebersprungen. Das widerspricht dem User-Prinzip
    "Korrektheit > Laufzeit". Per-Ticker-Calls laufen jetzt vollstaendig durch.

  NIEMALS Run abbrechen fuer Klassen 2-5. Klasse 1 (Connector-Fail) ist ausserhalb der
  Prompt-Kontrolle (Runtime wirft Tool-Error). Klasse 6 (Runtime-Monitoring) triggert
  KEINEN automatischen Rollback mehr (v3.0.3 Soft-Alert-Schema).
```

### Implizite Prompt-Änderung zu v2.2
In der `WICHTIG`-Liste am Ende des v2.2-Prompts steht aktuell: `Keine News-Suche`. Diese Zeile MUSS in v3.0 entfernt werden, sonst kollidieren die Anweisungen.

### Query-Content-Assertion (Codex Fix #1, adressiert T3-Gap)
In den PER-TICKER-Queries MUSS der `query`-String BEIDE enthalten: COMPANY_NAME UND TICKER. Nur COMPANY_NAME allein reicht nicht (bei Schneider "Schneider news" könnte Schneider-Electric vs. -Trucking disambiguiert werden, aber sicherer ist "Schneider Electric SU.PA news"). Test T3 verifiziert diese Assertion durch String-Content-Check am emittierten tavily_search `query`-Parameter.

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

## 6F. Mismatch-Klassen-Taxonomie (NEU v3.0.5 — Bucket-B Foundation)

**Zweck:** Klassen-Tabelle für Provenance-Konflikte zwischen Source und Output-Anforderung. Analog §6E-Pattern (flach mit Sub-Buckets), aber für Daten-Source-Edges statt Tool-Error-Buckets. Bindendes Output-Format pro Klasse, T6-grep-validierbar.

**Abgrenzung zu §6E:** §6E klassifiziert technische Fehler im Tool-Call selbst (Auth, Rate-Limit, Schema, Empty). §6F klassifiziert Provenance-Mismatches (Source liefert technisch korrekt, aber Wert passt nicht zur Output-Anforderung — z.B. Lag, Cross-Source-Inkonsistenz, fehlende File-Row).

**Klassen-Tabelle:**

| # | Klasse | Auslöser | Output | §6E-Cross-Ref |
|---|---|---|---|---|
| 6F-1 | **Lag** | `latest_date < heute` (Source-Date < Erwartung). `source_date` im Tag = **gelieferter Ist-Wert**, nicht Soll | `[FIELD] — n.v. (source-lag: [source_ref@source_date])` für Felder ohne Spezial-Branch. Für **Delta**: Prompt-SCHRITT-3a-Branches aus v3.0.4 gelten (Score-heute / Score-Datum-Close / normale Berechnung) — kein generisches `n.v.`. Lag wird über Tag-`source_date` transparent gemacht. | — |
| 6F-2 | **Schema-Drift** | Erwartete Source-Felder fehlen oder Format anders (z.B. `latest_date` plötzlich Unix-Epoch statt ISO; Tavily-`results[]` mit unerwartetem Key) | `[FIELD] — n.v. (schema-drift: [source_ref@source_date])` | →§6E Klasse 3 (parse-error) wenn Tool-Response betroffen |
| 6F-3 | **Auth-Access-Fail** | Source nicht erreichbar wegen Auth/Permission (kein Wert lieferbar) | `[FIELD] — n.v. (access-fail: [source_ref@source_date])` | →§6E Klasse 2a (401/403) bzw. 2b (429) |
| 6F-4 | **Cross-Source-Mismatch** | Multi-Source-Feld nur teilweise befüllbar (z.B. Shibui hat `latest_close` aber nicht `score_date_close`; Tavily-Headline ohne dazu passende Domain). **NEU v3.0.6 Calendar-Mismatch-Sub-Case:** `score_date` in Faktortabelle ist Sa/So oder Listing-Markt-Feiertag (NYSE für US-Ticker; Euronext Paris für RMS.PA/SU.PA), Source hat dafür keinen Close — Trading-Calendar-Lücke des Listing-Markts statt Schema-Drift. | `[FIELD] — n.v. (cross-source-mismatch: [source_ref@source_date])` (Calendar-Mismatch konkret: `Delta — n.v. (cross-source-mismatch: shibui_stock_quotes@<latest_date>; score_date=<datum> nicht handelbar im Listing-Markt)`) | — (eigenständig, kein §6E-Primärfehler nötig) |
| 6F-5 | **File-Sync-Drift** | PORTFOLIO.md vs. Faktortabelle.md inkonsistent (z.B. PORTFOLIO sagt Score 75, Faktortabelle 73; Sparrate-Spalte vs. Nenner-Berechnung divergent) | `[FIELD] — n.v. (file-sync-drift: [source_ref])` (Mehrere Source-Refs wenn nötig: `[file:PORTFOLIO.md vs file:Faktortabelle.md]`) | — |
| 6F-6 | **Missing-File-Row** | file-read-derived: Faktortabelle hat keinen Eintrag für getriggerten Ticker (z.B. Earnings-Datum-Spalte leer) | `[FIELD] — n.v. (missing-file-row: [source_ref])` | — |

### Klarstellungs-Bullets

- **Ist-Wert-Konvention:** `source_date` im Mismatch-Tag bezeichnet immer das **tatsächlich gelieferte Datum** (Ist-Wert). Erwartetes Datum (Soll-Wert) gehört in die Klassen-Beschreibung in dieser Tabelle, nicht ins Output-Tag. Begründung (Codex Runde 5): bei Lag wären Ist/Soll im Tag sonst ununterscheidbar, die Beweiskraft des Tags würde kippen.
- **Cross-Reference §6F → §6E (kein Doppel-Klassen-Logging):** Wenn ein §6F-Mismatch Folge eines §6E-Primärfehlers ist (z.B. Tavily-Auth-Fail = §6E Klasse 2a), wird die §6E-Klasse als Primär-Klassifikation verwendet und §6F-3 referenziert §6E. Mismatches *ohne* §6E-Primärfehler (Lag, Cross-Source-Mismatch, File-Sync-Drift, Missing-File-Row) bleiben exklusiv §6F.
- **Delta-Lag-Spezialfall:** Prompt-SCHRITT-3a-Branches aus v3.0.4 (`AUTORITATIVE-DATA-QUELLE-REGEL` + `DELTA-BERECHNUNG bei Stale-Shibui` mit drei Edge-Case-Branches) sind SoT für Delta-Output-Form bei Score-Date-vs-Latest-Date-Konstellationen. §6F-1 referenziert die Prompt-Branches, generisches `n.v.`-Template gilt für Delta nicht. Lag wird über Tag-`source_date` transparent.
- **„Unknown-Field-Request" ist KEINE §6F-Klasse.** Wenn der Agent ein nicht-mapped Feld emittieren will, ist das ein Pre-Output-Verstoß, der vom §3.0(b) Self-Check-Gate als „unmapped → konservativ n.v." behandelt wird. §6F klassifiziert nur Mismatches *innerhalb* gemappter Felder.

### Niemals Run abbrechen

Analog §6E: §6F-Klassen führen zu degradiertem Feld-Output (`n.v. (<type>: [...])`), nie zu Run-Abbruch oder Rollback. Briefing wird mit verfügbaren Feldern + n.v.-markierten Mismatches komplett ausgeliefert.

---

## 7. Data Flow

```
1. Git Repo (tobikowa90-hub/dynastie-depot)
   ├─ 00_Core/PORTFOLIO.md     → Sparraten, Watches, Trigger-Tabelle (24.04. STATE-Split)
   └─ 00_Core/Faktortabelle.md → Scores, DEFCON, FLAGs, Earnings, Score-Alter

2. Shibui MCP → 13 US-Ticker Close-Prices    (UNVERAENDERT)

3. Deterministische n.v.-Zuweisung für BRK-B, RMS.PA, SU.PA   (v3.0.3: Yahoo-curl entfernt — frozen known limitation, siehe Prompt §3c)

4. Trigger-Liste berechnen (in-prompt, rein aus Schritt-1-Daten)

5. Tavily MCP (mcp__tavily__tavily_search)       ← NEU
   ├─ Cohort-Query (1 Call, search_depth=basic)
   ├─ Per-Ticker-Queries (0..min(5, len(triggered)), search_depth=advanced)
   └─ Claude-Agent liest strukturiertes Result, applies Materialitäts-Filter

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
| 1. MCP Connector-Fail | `mcp.tavily.com` down, Connector-Init scheitert | Runtime-Error, Rollback-Trigger | — (prompt-unabfangbar) |
| 2a. Tool-Error 401/403 | Auth-Fehler | Loud flag, alle weiteren Queries skippen | `NEWS-SIGNAL: Auth-Fehler — Key rotieren` |
| 2b. Tool-Error 429 | Rate-Limit | Loud flag, alle weiteren Queries skippen | `NEWS-SIGNAL: Rate-Limit erreicht` |
| 2c. Tool-Error 400/422 | Bad params | Catch, weiter (Phase 0 R1 T-C verifiziert) | Cohort: `Cohort: n.v. (bad request)` / Per-Ticker: `[TICKER] — n.v. (bad request)` |
| 2d. Tool-Error 5xx | Tavily down | Catch, weiter | Cohort: `Cohort: n.v. (Tavily <code>)` / Per-Ticker: `[TICKER] — n.v. (Tavily <code>)` |
| 2z. Generischer MCP-Tool-Error | Non-HTTP: Protocol, Serialisation, Unknown | Catch, weiter | Cohort: `Cohort: n.v. (tool-error)` / Per-Ticker: `[TICKER] — n.v. (tool-error)` |
| 3. Response-Schema unerwartet | `results[]` fehlt oder malformed | Catch, weiter | Cohort: `Cohort: n.v. (parse-error)` / Per-Ticker: `[TICKER] — n.v. (parse-error)` |
| 4. Empty results[] | Keine Treffer | Kein Fehler | Cohort: `Cohort: Keine material News` / Per-Ticker: `[TICKER] — keine News` |
| 5. Materialitäts-Filter verwirft alles | Noise-only | Kein Fehler | Cohort: `Cohort: Keine material News` / Per-Ticker: `[TICKER] — keine material News` |
| 6. Runtime-Monitoring (v3.0.3 rebased) | Soft-Alert-Schema: <180s healthy / 180-400s observe / >400s alert | KEIN Auto-Rollback aus Runtime allein — nur manueller Review-Trigger bei >400s | Log-Eintrag, keine User-Output-Degradation |

### Known Residual Risk
**MCP Connector-Fail (Klasse 1)** wird in v3.0 nicht gemitigated (YAGNI). Falls `mcp.tavily.com` total offline ist, kann der Run bei Connector-Init fehlschlagen. Tavilys hosted MCP hat historisch hohe Verfügbarkeit (Anthropic-reviewed Vendor). Monitoring erfasst Degradation; Healthcheck-Fallback ist v3.1-Backlog-Kandidat.

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
- ~~Budget-Fallback (60s-Gate)~~ — v3.0.3 ENTFERNT (Recall-Regression-Risiko, siehe §6E Klasse 6). Per-Ticker-Calls laufen vollstaendig durch.

---

## 9. Testing Plan

### Pre-Deployment Tests auf Probe-Trigger

Probe-Trigger `trig_01XYuQ5mugsvZGZD4K52rjXh` wiederverwenden. Prompt je Test via `RemoteTrigger update` austauschen, manueller Run via Desktop App.

| # | Test | Setup | Pass-Kriterium |
|---|---|---|---|
| T1 | Happy-Path | Voller v3.0-Prompt mit mock-STATE (1-2 Ticker mit FLAG/Earnings), Tavily-MCP attached | Cohort-`tavily_search` + ≥1 Per-Ticker-`tavily_search`, Allowlist-Domains only, material-Filter angewandt, kein Abbruch |
| T2 | Empty-Trigger-List | mock-STATE ohne FLAGs/Earnings/stale Scores | News-Sektion zeigt nur Cohort, "Keine getriggerten Ticker" |
| T3 | Symbol-Trap (adversarial, Codex Fix #1) | Per-Ticker-Query für SU.PA und RMS.PA erzwingen; **zusätzlich**: prüfe den emittierten `tavily_search.query`-Parameter (muss COMPANY_NAME UND TICKER enthalten); **und**: manuelle Noise-Injection — Tester liest Output und verifiziert dass keine Suncor/Rockwell-Headlines durchgerutscht sind auch bei hoher Tavily-Rangliste für Homonyme | Results enthalten nur Schneider/Hermès-Headlines; emittierter `query`-String enthält beide Terme; manuelle Content-Prüfung findet keinen Trap-Durchschlag |
| T4 | Fehler-Klassen | Prompt provoziert Klassen 2c (bad params: `query=""`+`max_results=-1` analog Phase 0 Test C) und 4 (valid query mit sehr nischigen Term für results[]=[]) | Klasse 2c: Phase 0 R1 Test C bereits PASS; Klasse 4 sichtbar als "keine News"; Run läuft durch |
| T5 | Post-Update Content-Verify (Codex Fix #7) | Nach `RemoteTrigger update`: `RemoteTrigger get` aufrufen, content grep auf `SCHRITT 4.5` + Negativ-Grep auf `Keine News-Suche` | Beide Checks PASS bevor Manual-Run getriggert wird |
| T6 | **Adversarial-Provenance-Test (NEU v3.0.5)** | Probe-Trigger Run unter natürlicher Stale-Source-Bedingung (Wochenende, Feiertag, EOD-Lag-Fenster) — analog T5 (Adversarial-Stale-Shibui) aus v3.0.4-Hotfix-Plan-Migration. Reviewer öffnet nach Run die `RemoteTrigger get`-Tool-Response-History und führt 5-Punkt-Cross-Check durch (manuelle Tag-Authentizitäts-Verifikation; Auto-Capture-Diff-Skript ist v3.1-Backlog). | (1) **Tag-Pflicht-Grep:** Jeder mapped-Feld-Wert im Output trägt Tag mit `source_ref` im Format `[source_ref@source_date]` (external-Klasse) ODER `[source_ref]` (file-read-derived bzw. §6F-5/§6F-6 Klassen, wo `source_date` per Schema fehlt — siehe §6F Klassen-Tabelle). T6-Grep-Contract: regex `\[(file:|tavily@|shibui_)[^\]]+\]` matcht alle gültigen Tag-Formen. (2) **Tag-Authentizität:** Jeder Tag-Wert matcht einen Eintrag aus der Tool-Response-History bzw. dem konkreten File-Read-Wert. (3) **Klassen-Compliance:** Bei Mismatch-Trigger erscheint korrekte §6F-Klasse-Output-String mit Klassen-Label (`source-lag` / `schema-drift` / `access-fail` / `cross-source-mismatch` / `file-sync-drift` / `missing-file-row`) — T6 grept auf Klassen-Labels, NICHT auf `@`-Tag-Format-Universalpattern. (4) Self-Check-Gate (SCHRITT 4.8) wurde durchlaufen — sichtbar im Run-Verlauf oder als impliziter Pre-Output-Marker. (5) Keine `n.v.`-Zeile ohne §6F-Klassen-Begründung. (6) **NEU v3.0.6 Anti-Fabrikation:** Bei jedem Failure-Mode (Tavily-Auth, Tavily-Domain-Block, Tool-Unavailable, Schema-malformed, Calendar-Mismatch etc.) darf KEINE neue Source-Klasse oder neues Tag-Format erfunden werden, das nicht in §3.0(a) FIELD→SOURCE-MAP oder §6F-Klassen-Tabelle existiert. Beispiele verbotener Erfindungen: `[websearch@<domain>]`, `[yahoo@<domain>]`, `[manual@...]`, `[fallback@...]`. Tag-Authentizität gilt auch im Failure-Modus. Reviewer prüft via grep auf erlaubte Tag-Patterns nur (Allow-List **kanonisch v3.1.0**, Codex-PASS 5/5 Tag-Forms): `\[(file:[^\]]+|tavily@[a-z0-9.\-]+,\d{4}-\d{2}-\d{2}|shibui_[a-z_]+@\d{4}-\d{2}-\d{2}(; score_date=\d{4}-\d{2}-\d{2})?|Yahoo 403 known)\]` plus zwei separate Klassen-Label-Sets: **(i) §6F Mismatch-Labels** (`n.v. (source-lag: ...)`, `n.v. (schema-drift: ...)`, `n.v. (access-fail: ...)`, `n.v. (cross-source-mismatch: ...)`, `n.v. (file-sync-drift: ...)`, `n.v. (missing-file-row: ...)`) und **(ii) §4.5(E) Tool-Status-Outputs** (`n.v. (tool-unavailable)`, `n.v. (tool-error)`, `n.v. (parse-error)`, `n.v. (bad request)`, `n.v. (Tavily <code>)`, `Auth-Fehler — Key rotieren`, `Rate-Limit erreicht (Budget ausgeschoepft)`, `Keine material News`). Klassen-Label-Sets sind disjunkt — §6F adressiert Source-Mismatch (Source liefert technisch, aber Wert passt nicht), §4.5(E) adressiert Tool-Erreichbarkeit (Source liefert nicht oder gar nicht). Allow-List-Regex deckt alle 5 beobachteten Tag-Forms in v3.0.6-Prompt ab: `[file:...]`, `[tavily@<domain>,<date>]`, `[shibui_stock_quotes@<date>]`, `[shibui_stock_quotes@<date>; score_date=<date>]`, `[Yahoo 403 known]`. Form `[file:PORTFOLIO.md vs file:Faktortabelle.md]` faellt in `file:[^\]]+`-Branch. Alle 6 Assertions PASS. |

Alle 6 Tests müssen **PASS** bevor Prod-Update v3.0.5.

### Pre-Phase-3-Gate: Tavily-UI-Reattach-Verify (NEU v3.1.0, Q3-Fix)

**Auslöser:** Vor jeder Probe-Test-Iteration auf `trig_01XYuQ5mugsvZGZD4K52rjXh` nach Tavily-Key-Rotation oder UI-Connector-Drift-Verdacht.

**Hintergrund:** Memory `feedback_tavily_connector_uuid_rotation.md` — Body-`mcp_connections`-Update refresht NICHT die UI-Connector-Bindung. Stale-Auth manifestiert sich NICHT als 401/403, sondern als "Tool fehlt in allowed_tools" (= Output `NEWS-SIGNAL: n.v. (tool-unavailable)`). Body-GET-Roundtrip ist KEIN ausreichender Verify; nur Manual-Run mit tatsächlichem Tavily-Aufruf zählt.

**Pflicht-Sequenz vor jedem Probe-Test:**

1. Manual-Run via Claude Desktop App auf Probe-Trigger (`trig_01XYuQ5mugsvZGZD4K52rjXh`).

2. Output muss MINDESTENS EINES der folgenden Pass-Patterns enthalten:
   - **(a)** ≥1 valide `[tavily@<domain>,<date>]`-getaggte Headline in mindestens einem Cohort- ODER Per-Ticker-Block (Beweis: Tool wurde invoked + Response geparsed + Tag korrekt aufgebaut)
   - **(b)** Explizites `Keine material News`-Statement (oder funktional äquivalentes §4.5(E) Pattern für leere-Allowlist-Result) bei nachweisbar erfolgten Tavily-Calls

3. Output darf NICHT enthalten:
   - `NEWS-SIGNAL: n.v. (tool-unavailable)` — das ist **Pre-Gate-FAIL** (= stale UI-Connector-Bindung; Reattach in Routine "tavily-probe" via Claude Desktop App erforderlich, danach erneuter Pre-Gate-Run)

4. Edge-Case (a) und (b) nicht erfüllt UND tool-unavailable nicht präsent: Manual-Inspection ob Tavily-Calls überhaupt versucht wurden (Run-History prüfen). Eskalation an User wenn unklar.

**Pass:** Pre-Gate PASS → Phase-3-Test-Suite freigegeben.
**Fail:** Pre-Gate FAIL → User-Notify, UI-Reattach durch User, danach Schritt 1 retry. KEIN automatischer Phase-3-Start.


**Hinweis zu T-Numbering-Drift (Bucket-A.3-Cleanup pending, kein Bucket-B-Scope):** Der v3.0.4-Hotfix-Plan (`docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md`) führte einen separaten T5 *Adversarial-Stale-Shibui* ein, der nie in die Spec migriert wurde (Drift, weil v3.0.4 nie deployed wurde). Spec-T5 hier = *Post-Update Content-Verify* (Codex Fix #7, ursprünglich v3.0). Konsolidierung der zwei T5-Definitionen ist offener Bucket-A.3-Cleanup-Schritt, gehört nicht in v3.0.5 Bucket-B (würde Architektur-Phase mit Index-Refactor mischen). Für v3.0.5-Deploy-Gate gilt: **T1-T6 hier in dieser Tabelle PASS** + **separat T-Stale-Shibui aus Hotfix-Plan PASS** (operativ derselbe Run möglich, getrennte Assertions).

### Phase 0 — Round 1 (MCP-Architektur, FINAL aktiv)

| # | Test | Ergebnis |
|---|---|---|
| A | API akzeptiert UUID-basierte MCP-Anbindung | ✅ HTTP 200 |
| B | Tool-Name `mcp__tavily__tavily_search` + Connectivity | ✅ 2 Results, 0.88s |
| C | Fail-Open bei MCP-Tool-Fehler | ✅ HTTP 422 gecatched, Run bis FERTIG |

### Phase 0 — Round 2 (CLI-Architektur, ABGEBROCHEN)

Durchgeführt 2026-04-19, Ergebnis führte zum Revert auf MCP:

| # | Test | Ergebnis |
|---|---|---|
| A2 | curl verfügbar in Remote-Trigger-Runtime | ✅ (Yahoo-curl-Pattern aus v2.2) |
| B2 | REST `api.tavily.com/search` mit Bearer-Token | ❌ **FAIL: HTTP 403 "Host not in allowlist"** |
| C2 | Agent parst JSON ohne jq | — (nicht durchgeführt, B2 failed) |
| D2 | HTTP 4xx wird gecatched | ✅ (HTTP 403 korrekt erkannt) |

**Root-Cause B2:** Tavily Dev-Keys (Free-Tier only) sind auf MCP-Proxy-Pfad beschränkt. REST-Zugang nur mit Production-Keys (Paid-Plan). Key-Upgrade wurde gegen MCP-Residual-Risks abgewogen → MCP gewinnt. CLI-Architektur verworfen.

---

## 10. Deployment Plan

### Gate-Sequenz (alle Schritte müssen PASS)

```
1. T1-T6 auf Probe-Trigger PASS (Phase 0 Round 1 ist Baseline, Round 2 moot — siehe §15 App.C). Ab v3.0.5: T6 Adversarial-Provenance-Test mit manuellem Tag-Authentizitäts-Cross-Check ist Gate-Bedingung.
2. Prompt v3.0.5 committed nach 03_Tools/morning-briefing-prompt-v3.md (v3.0.4-Hotfix-Wording bleibt drin als Defense-in-Depth-Layer; v3.0.5 ergänzt Provenance-Map + SCHRITT 4.8 Self-Check + Tag-Pflicht)
3. Push zu GitHub (VOR 10:00 UTC — sonst liest Cron morgen alte Daten)
4. RemoteTrigger update auf Prod-Trigger:
   - ccr.events[0].data.message.content = v3.0.5 prompt
   - ccr.session_context.allowed_tools = ["Bash","Read","Glob","Grep","mcp__tavily__tavily_search"]
   - ccr.mcp_connections: UNVERÄNDERT (Shibui + Tavily bereits via UI attached, Round 1)
5. POST-UPDATE VERIFY (Codex Fix #7, v3.0.5 erweitert):
   - RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG
   - Assert content.contains("SCHRITT 4.5")
   - Assert content.contains("SCHRITT 4.8")  (NEU v3.0.5)
   - Assert content.contains("Provenance-Self-Check")  (NEU v3.0.5)
   - Assert NOT content.contains("Keine News-Suche")
   - Bei Assertion-Fail: RE-UPDATE nötig, KEIN Manual-Run
6. Manueller "Jetzt ausführen" in Desktop App
7. Output-Validierung:
   - News-Sektion present?
   - Allowlist-Domains only?
   - Trigger-List respektiert (Slot-Struktur korrekt)?
   - Materialitäts-Filter greift (keine "TMO to report earnings"-Noise)?
   - MCP-Tool-Fehlerpfad falls provoziert: catched?
   - **v3.0.5 NEU:** Source-Tags auf allen mapped Feldern present? Format `[source_ref@source_date]` für `external`-Klasse (Kurs/Delta/News-Headline/News-Domain), `[source_ref]` ohne `@` für `file-read-derived` (Earnings-Datum) und §6F-Klassen 6F-5/6F-6, in denen `source_date` per Schema fehlt. Siehe §3.0(c) Tag-Format und §9 T6 Assertion (1) für vollständigen Grep-Contract.
   - **v3.0.5 NEU:** Tag-Authentizität — manueller Cross-Check gegen RemoteTrigger get-Tool-Response-History (T6-Reviewer-Schritt)?
   - **v3.0.5 NEU:** Bei Mismatch: §6F-Klasse-Output-String korrekt (z.B. `n.v. (source-lag: ...)` mit Klassen-Label)?
8. PASS → DONE. FAIL → Rollback (siehe §11).
```

### Timing
- Pre-deploy Tests T1-T6: ~25 Min (T6 manueller Cross-Check fügt ~5 Min hinzu für 5-Felder-Scope; Phase 0 Round 1 ist Baseline, Round 2 moot)
- Prod-Update + Post-Update-Verify + Manual-Run: ~5 Min
- Total: ~25 Min, keine Downtime
- Deployment-Fenster: bis 08:00 UTC am Deployment-Tag (damit 10:00-Cron die neue Version nimmt — obwohl wir das heute manuell triggern, nicht Cron)

---

## 10A. Layer-A/Layer-B-Architektur (Pre-Briefing Control-Plane, NEU v3.1.0)

**Architektur-Klarstellung (CRITICAL für Spec-Reader):** Calendar-Hook ist Operator-Awareness-Channel, NICHT Cron-Briefing-Input. Drift-Schutz erfolgt INDIREKT via Operator-Reaktion. Cron-Body bleibt selbst-contained mit FIELD→SOURCE-MAP-Schema.

```
LAYER A: Operator-Awareness (Claude Code CLI-Session)
  └─ briefing-sync-check.ps1 (M2-Single-Owner SessionStart/SessionEnd-Hook)
     ├─ Funktion 1: Briefing-Versions-Drift-Check (Sync-State 00_Core/* unpushed?)
     ├─ Funktion 2: Earnings-Calendar-Drift-Check (yfinance ∪ Override-YAML, 06.05. NEU)
     └─ Funktion 3: M2-Owner für Lifecycle-Events (Plan-v1.2 etabliert 05.05.)
  → Output: systemMessage-JSON an Claude in CLI-Session
  → Claude/User reagiert: PORTFOLIO/Faktortabelle update, Calendar-Override-Pflege etc.

LAYER B: Cron-Briefing (Anthropic-Cloud-Routine, separates Runtime)
  ├─ Probe-Trigger trig_01XYuQ5mugsvZGZD4K52rjXh (v3.1.0-Body)
  └─ Prod-Trigger  trig_01PyAVAxFpjbPkvXq7UrS2uG (v2.1-Rollback → Ziel v3.1.0)
  → Body: morning-briefing-prompt-v3.md FIELD→SOURCE-MAP-Schema
      ├─ Tavily news-signal (Anti-Fallback v3.0.6 + neue v3.1.0-Edits)
      ├─ Shibui kurs/delta (latest_close + score_date_close)
      └─ File-reads (Faktortabelle, PORTFOLIO)

Bridge zwischen Layer A → Layer B: AUSSCHLIESSLICH via geteilten File-State
(PORTFOLIO/Faktortabelle). NIEMALS Hook-Output → Cron-Briefing-Body direkt.
```

**Layer A — Data Flow:**
1. SessionStart oder SessionEnd Hook fired
2. `briefing-sync-check.ps1` läuft (M2-Single-Owner)
3. Funktion 1: `git status` auf 9 briefing-files → dirty-count
4. Funktion 2: `python earnings_calendar.py --check --json 2>$null` (fail-soft, exit-Filter 0/2)
5. Output JSON mit `systemMessage` zu stdout
6. Claude Code CLI parsed JSON, zeigt Warning an Claude
7. Claude/User reagiert: PORTFOLIO/Faktortabelle update bei Drift, Calendar-Override-Pflege bei Schedule-Mismatch

**Layer B — Data Flow:** unverändert seit v3.0.6 (siehe §7 Data Flow). Cron-Trigger fires → RemoteTrigger executes Body → Agent runs SCHRITT 1-5 mit FIELD→SOURCE-MAP-Schema.

**Bridge Layer A → Layer B Sequenz:**
- T0: Layer-A-Hook signalisiert Drift (z.B. SU Q1 30.07. nicht in PORTFOLIO)
- T1: User updated PORTFOLIO + Faktortabelle (manueller Sync, ggf. §18-Sync-Set)
- T2: Nächster Cron-Briefing-Run liest aktualisierte File-State → korrekter Earnings-Trigger-Output

**Niemals:** Hook-Output → Cron-Briefing-Body direkt. Cron-Body ist statisch in `events[0].data.message.content`.

**Implementations-Hinweis:** `briefing-sync-check.ps1` wird in v3.1.0 NICHT im Code geändert. Multi-Funktions-Charakter wird ausschließlich hier in der Spec dokumentiert. Begründung: M2-Owner-Stabilität priorisiert; Welle-3-Hook-Promotion-Plan blockiert auf "kein Touch ohne expliziten Plan".

---

## 11. Rollback Plan — Exact Runbook (Codex Fix #5)

### Trigger-Bedingungen (v3.0.5 aktualisiert)
- T1-T6 fail (T6 NEU v3.0.5 Adversarial-Provenance-Test)
- Post-Update-Verify (Gate-Schritt 5) fail
- Prod-Manual-Run fail (Gate-Schritt 6 Run / Gate-Schritt 7 Output-Validierung / Gate-Schritt 8 Final-Decision) — funktional, nicht Runtime
- **v3.0.5 NEU:** Tag-Authentizitäts-FAIL aus T6 oder Gate-Schritt 7 (gegrepter Tag matcht keine echte Tool-Response/File-Read)
- Tag 1-3 Post-Deploy Monitoring findet **Korrektheits**-Regression (nicht Runtime-Regression)
- ~~Claude-Runtime-Timeout (Fehlerklasse 6)~~ — v3.0.3: ENTFERNT. Runtime allein triggert keinen automatischen Rollback mehr (Soft-Alert-Schema, siehe §6(E) Klasse 6). Nur wenn der Runtime SELBST den Run killt (Runtime-Fehler, nicht Klasse-6-Soft-Alert) und Output fehlerhaft ist, greift manueller Rollback-Review.

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
        "allowed_tools": ["Bash", "Read", "Glob", "Grep"],       ← MCP-Tavily-Tool ENTFERNT
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

**Hinweis:** `ccr.mcp_connections` wird NICHT gesendet im Rollback-Payload — Anthropic-API behält bestehende mcp_connections wenn nicht explizit neu gesendet (das Tavily-Connector-UUID bleibt, aber ohne `mcp__tavily__tavily_search` in allowed_tools ist das Tool inert). Alternativ: mcp_connections explizit senden ohne Tavily-Entry — sauberer, aber nicht nötig für Funktions-Rollback.

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
| Tag 2 (Cron) | Output Review | Nach 10:00 MESZ | News-Sektion fehlt / Fehler nicht gecatched / Material-Recall verschlechtert. Runtime allein ist v3.0.3 KEIN Rollback-Trigger mehr — siehe §6E Klasse 6 Soft-Alert-Schema. |
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

Konsolidiert aus Codex-Review Round 1 (`a6353fc19fe65e09a`) + Round 1-bis (`aede6311232389387`) + Round 2 (`6bd32f4`, COMPLETE) + Phase 0 Round 1 (MCP, PASS) + Phase 0 Round 2 (CLI, ABORTED).

| # | Risk | Severity | Status | Mitigation |
|---|---|---|---|---|
| 1 | MCP `connector_uuid` Requirement | CRITICAL | ✅ Resolved (UI-Registrierung), ⚠️ Re-Auth-Pflicht bei Key-Rotation (NEU 27.04.) | Initial-UUID via Claude.ai Web-UI registriert. **Erweiterung 27.04.2026 nach Phase-3.5-Run-#1-FAIL:** „Resolved" gilt nur bis erste Key-Rotation. Bei jeder Key-Rotation MUSS der Tavily-Connector im Web-UI in jeder konsumierenden Routine entfernt + neu attached werden — sonst bleibt UUID stale, Cloud-Runtime lädt alten Auth-State, Tool fehlt in `allowed_tools` (kein 401/403-Signal). Body-RemoteTrigger-update refresht nur Body-Cache, nicht UI-Connector-Bindung. **Verify-Pflicht nach jeder Rotation:** Manual-Run mit Tavily-Aufruf, NICHT nur Body-GET-Roundtrip (war Quelle der „Rotation #1 verified"-Selbsttäuschung pre-Run-#1). Aktuelle Probe-UUID `0da14a12-17bb-4609-bcba-ba2b21152c9b` (UI-Reattach 27.04.2026 18:37:24Z, alt: `4a633350-...`). |
| 2 | MCP Tool-Name Korrektheit | HIGH | ✅ Resolved (Phase 0 R1 Test B) | `mcp__tavily__tavily_search` bestätigt |
| 3 | Prompt-Fail-Open bei Tool-Fehler | HIGH | ✅ Resolved (Phase 0 R1 Test C) | HTTP 422 sauber gecatched, Run bis FERTIG |
| 4 | API-Key in URL-Query — Exposure | HIGH | ✅ Mitigated (Rotation #1 verified 27.04.2026, alter Key revoked) | Rotation-Cycle empirisch verifiziert; Dev-Key separat vom Billing-Account; monatliche Rotation operativ |
| 5 | MCP Connector-Level-Fail (MCP offline) | MEDIUM | ⚠️ Accepted for v3.0 | Healthcheck-Fallback v3.1-Backlog; Tavily-Hosted-Uptime historisch hoch |
| 6 | Tavily-Behavior-Drift (third-party) | MEDIUM | ⚠️ Accepted | Monitoring erfasst Degradation |
| 7 | Budget-Exhaust bei Retries | LOW | ⚠️ Accepted | Hard-Cap 6 Queries/Run (1 Cohort + max 5 Per-Ticker). 60s-Runtime-Budget-Fallback v3.0.3 ENTFERNT (Recall-Regression). |
| **8** | **Dev-Key-Host-Allowlist (CLI-Pivot-Blocker)** | — | ✅ Resolved durch MCP-Beibehaltung | REST-API nicht genutzt; MCP-Proxy-Pfad umgeht Allowlist |
| **9** | **Runtime-Monitoring** (v3.0.3 rebased) | LOW | ⚠️ Accepted, Soft-Alert only | Soft-Alert-Schema: <180s healthy / 180-400s observe / >400s alert. KEIN Auto-Rollback aus Runtime allein (User-Prinzip "Korrektheit > Laufzeit"). Budget-Fallback entfernt (war Recall-Regression). |
| **10** | **Post-Update Cache-Interference** | LOW | ✅ Mitigated (Codex Fix #7) | Post-Update-Verify Gate vor Manual-Run |
| **11** | **Halluzinations-Tag-Fabrikation (v3.0.5)** | MEDIUM | ⚠️ Mitigated (manueller T6-Verify) | Reine Tag-Pflicht fängt erfundene Tags nicht ab (Codex Runde 3). T6 Adversarial-Provenance-Test verifiziert Tag-Authentizität via manuellen Cross-Check gegen `RemoteTrigger get`-Tool-Response-History. Auto-Capture-Diff-Skript ist v3.1-Backlog (skaliert nicht über ~10 Felder, aktuell 5). |
| **12** | **File-Sync-Drift PORTFOLIO/Faktortabelle (v3.0.5)** | LOW | ⚠️ Mitigated (§6F-5) | PORTFOLIO.md vs. Faktortabelle.md inkonsistent ist als §6F-Klasse 5 erfasst (`n.v. (file-sync-drift: ...)`). Self-Check-Gate (§3.0(b)) blockiert Emit bei Detected-Drift. Long-term-Mitigation ist `!SyncBriefing` + system_audit (CLAUDE.md §25, gehört nicht zu v3.0.5-Scope). |

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

### Codex-Findings-Trace (Round 2, alle integriert in Commit `6bd32f4` post-MCP-Revert)

| Codex # | Finding | Integration |
|---|---|---|
| R2-#1 | §9 T1 "Cohort-curl + Per-Ticker-curl" CLI-Residue nach MCP-Revert | §9 T1 auf MCP-tool-call-Sprache umgeschrieben |
| R2-#2 | §9 T3 "curl-Body" inspection CLI-Residue | §9 T3 auf "emittierter tavily_search.query"-Inspektion |
| R2-#3 | §10 Gate-Step 1 "Phase 0 Round 2 PASS" als Prerequisite obsolet | Schritt entfernt (Round 2 abgebrochen via CLI-pivot revert), Steps 2-8 re-numbered |
| R2-#4 | §10 Gate-Step 7 "curl-Fehler-Pfad" CLI-Residue | "MCP-Tool-Fehlerpfad" |
| R2-#5 | §6(E) Klasse 2 unvollständig — kein Bucket für non-HTTP-Errors | 2z "Generischer MCP-Tool-Error" subclass für Protocol/Serialisation/Unknown |
| R2-#6 | §6(E) Klassen 2c/2d/3/4/5 nur Per-Ticker-Output, kein Cohort-Output | Cohort-spezifische Output-Strings ergänzt |
| R2-#7 | §8 Error-Tabelle ohne Cohort/Per-Ticker-Distinction | Tabelle um Cohort/Per-Ticker-Spalten erweitert |

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
- [ ] **T6-Auto-Capture-Diff-Skript (v3.0.5-Backlog)** — Automatisiert Tag-Authentizitäts-Verifikation aus T6 via Capture-Layer (Tool-Response-Logging + File-Read-Reproduktion + Diff-Skript gegen Output-Tags). Aktiviert wenn Map-Scope auf >10 Felder wächst (z.B. Provenance-Map-Erweiterung Richtung C-Scope mit FLAG/Score/Watches) oder Test-Frequenz manuelle Verifikation überlastet. Aktuell akzeptierter Manuel-Cross-Check-Aufwand: ~5-10 Min pro Probe-Run für 5 Felder.
- [ ] **Provenance-Map-Erweiterung Richtung C-Scope (v3.0.5-Backlog)** — Aufnahme von FLAG, Score, Score-Datum, Watches, Trigger-Datum, Sparrate als file-read-derived-Felder mit Tag-Pflicht. Aktiviert nur wenn empirische Pass-Through-Halluzinations-Drift auftritt (z.B. Agent zitiert Score falsch aus Faktortabelle).
- [ ] **Bucket-A.3-Cleanup: T-Numbering-Konsolidierung** — Drift zwischen Spec-T5 (Post-Update Content-Verify, Codex Fix #7) und v3.0.4-Hotfix-Plan-T5 (Adversarial-Stale-Shibui) auflösen. Kandidaten-Schemata: T5+T5b nebeneinander; oder Re-Numbering mit T5=Stale-Shibui, T6=Provenance, T7=Post-Update-Verify. Gehört nicht zu v3.0.5-Architektur-Phase.

---

## 15. Appendix

### A. Prompt v3.0.5 Skeleton (siehe `03_Tools/morning-briefing-prompt-v3.md` — aktiv im Repo: v3.0.3 Rollback-Stand seit 20.04.2026; v3.0.4 Hotfix-Wording wurde nie deployed; v3.0.5 in Vorbereitung mit Bucket-B Provenance-Layer)

Strukturell: v2.2 + neuer SCHRITT 4.5 + neue Output-Sektion. Alle anderen Teile (CRITICAL GUARDS, WOCHENEND-MODUS, WICHTIG-Liste) unverändert ausser:
- `Keine News-Suche` (WICHTIG-Liste) → entfernt
- v3.0.3-Hotfixes (TZ='Europe/Berlin', Sequenzierung 3→4.5, Yahoo-Gap-Elimination, Soft-Alert §6E Klasse 6) → siehe Prompt-Datei Changelog

### B. Codex Review Summary

**Round 1 (Architecture-Review, pre-Phase 0):**
- Agent-ID: `a6353fc19fe65e09a`
- 4 CRITICAL/HIGH-Flags — alle adressiert (3 empirisch via Phase 0 Round 1, 1 Posture-akzeptiert)

**Round 1 bis (Spec-Review nach initial-Write):**
- Agent-ID: `aede6311232389387`
- 7 Findings (3 HIGH, 3 MEDIUM, 1 LOW) — alle in Round-2-Spec-Revision integriert (siehe Trace in Section 13)

**Round 2 (Final-Review, post-MCP-Revert):**
- Commit: `6bd32f4` (2026-04-19 14:18)
- Status: COMPLETE — 5 surgical fixes integriert (vollständiger Trace in §13 "Codex-Findings-Trace Round 2")
- Fokus war: CLI-Residue nach surgical MCP-Revert + Error-Taxonomy-Gaps (Klasse 2z, Cohort/Per-Ticker-Distinction)

### C. Phase 0 Test Results

**Round 1 (MCP-Architektur, retrospektiv nach CLI-Pivot):**
- Test A: UUID-MCP-Anbindung OK (HTTP 200 auf `RemoteTrigger create`)
- Test B: Tool-Name + Connectivity OK (2 Results für TMO earnings, 0.88s)
- Test C: Fail-Open OK (HTTP 422 bei `query=""`+`max_results=-1` → "FAIL-OPEN OK" in Output)

**Round 2 (CLI-Architektur, ABORTED 2026-04-19 nach B2 FAIL):**
- Test A2: curl-Verfügbarkeit ✅ (implizit durch Yahoo-curl in v2.2 bestätigt)
- Test B2: ❌ **FAIL — HTTP 403 "Host not in allowlist"** (Dev-Keys auf MCP-Proxy beschränkt, REST nur mit Production-Keys/Paid-Plan)
- Test C2: nicht durchgeführt (B2 failed)
- Test D2: HTTP 403 wird gecatched ✅ (siehe §9 Round 2 Tabelle)
- Konsequenz: Surgical Revert CLI → MCP, Codex Round-2-Review (Commit `6bd32f4`) addressierte CLI-Residue

### D. Architecture Decision Log

| Datum | Entscheidung | Kontext | Begründung |
|---|---|---|---|
| 2026-04-19 morning | MCP-basierte Tavily-Integration | Initial-Brainstorming | Typed schema, strukturiertes Protokoll |
| 2026-04-19 (Phase 0 Round 1) | MCP-Architektur empirisch verifiziert | Nach Codex Round 1 | `connector_uuid`, `mcp__tavily__tavily_search`, 422-fail-open |
| 2026-04-19 (Codex Round 1 bis) | 7 Gaps im MCP-Spec identifiziert | Nach Self-Review | Adversarial-T3, Materialitäts-Filter, Sort-Priority, Error-Taxonomy, Rollback-Runbook, Messbarkeit, Cache-Verify |
| 2026-04-19 (User-Prompt) | Pivot MCP → CLI | Fragestellung "CLI vs. MCP" | Eliminiert Connector-Fail-Risk, matcht Yahoo-Pattern, Bearer-Header statt URL-Query |
| 2026-04-19 (Revision) | Spec v2 mit CLI + 7 Codex-Fixes | Zwischenstand | Siehe Git-History Commit `9df9e3d` |
| 2026-04-19 (Phase 0 Round 2) | **Revert CLI → MCP** | B2 Test FAIL: Dev-Key rejected by REST `api.tavily.com` (HTTP 403 "Host not in allowlist"); Free-Tier bietet nur Dev-Keys, Production-Keys = Paid-Plan | Budget-vs-Nutzen-Analyse zeigt: MCP-Residual-Risks (Connector-Fail MEDIUM, Key-URL-Exposure HIGH mit Rotation-Mitigation) akzeptabler als Paid-Plan für News-Feature. Surgical Revert keeps Codex-Fixes #1-7 intact. |
| 2026-04-19 (Final) | Spec v3 MCP-Architektur mit allen Codex-Fixes | Round-1 + Round-2 PASS | Siehe Sections 5-13 final |
| 2026-04-20 Nacht-Spät | v3.0.3 Manual-Run-FAIL → Rollback v3.0.3 → v2.2 | Phantom-Kurse 7 US-Ticker (z.B. AVGO -21.8% phantom), Stale-Shibui Karfreitag/Oster-EOD-Lag löste improvisierten Yahoo-Fallback aus | Commit `4cfa421` Incident+Rollback. Trigger für v3.0.4 Anti-Fallback-Hotfix-Plan + Applied-Learning Bullet 11 (zweigleisige Anti-Hallucination-Guards) |
| 2026-04-27 | Tavily-Key-Rotation #1 verifiziert | Risk #4 Mitigation-Loop | Alter Key revoked, neuer Key in Connector-URL aktiv. Rotation-Posture empirisch validiert. |
| 2026-04-27 abend | Probe v3.0.6 Phase 3.5 PASS (B1-B9 9/9, 6 hart) | Hotfix-Verify nach Anti-Fabrikations-Cracks aus Phase 3 | v3.0.6-Body deployed 17:38:50Z (`1a3cf51`, 9/9 GET-Marker). Manual-Run #1 ~20:00 MESZ tool-unavailable wegen stale UI-Connector-Bindung nach Key-Rotation 15:27 UTC; Diagnose ergab Hypothese B (UI-Bindung kaputt, NICHT Server-Auth-Fail). Fix Pfad 1: User UI-Reattach 18:37:24Z, Tavily-UUID rotiert `4a633350-...` → `0da14a12-17bb-4609-bcba-ba2b21152c9b`. Run #2 ~20:50 MESZ lieferte echte Headlines + Material-Filter sauber + Cohort-0-results ohne Inferenz. **Lesson:** Body-update refresht nur Body-Cache, nicht UI-Connector-Bindung. **Risk #1-Erweiterung:** Re-Auth-Pflicht bei jeder Key-Rotation. Phase 4-6 (T6 voll-test + T1/T3/T4-Retest + Prod-Deploy v3.0.6) freigegeben, blockiert durch V (28.04.) + MSFT (29.04.) Earnings. |

### E. Referenzen

- `03_Tools/morning-briefing-prompt-v2.md` — SoT der v2.2-Prompt
- `memory/morning-briefing-config.md` — v2.1-Scope + Known Issues
- `memory/remote-trigger-api.md` — Full-Replace-Regel, JSON-Nesting-Gotcha
- `CLAUDE.md §25` — `!SyncBriefing` / `!BriefingCheck`-Workflow
- Codex Feedback Memory (`feedback_codex_over_advisor.md`) — Second-Opinion-Pattern

---

**Next step:** Self-Review → Codex-Review → User-Review → writing-plans skill.
