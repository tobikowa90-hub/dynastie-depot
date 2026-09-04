# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner (Sliding-Window — letzte 2 Sessions; volle Historie → `05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md` + git log + Vault `log.md`):**
- **Datum:** 2026-09-04 (Fr, Nacht-Session) — **🟢 R5 Live-Verifikation + 6 Owner-Entscheidungen — Spec v1.6 SCHREIBREIF (PIPELINE #83, scoring-neutral, kein §18-Score-Event). Spec absichtlich NICHT geschrieben** (Kontext >300 k) — vollständige Übergabe in **`02_Analysen/2026-09-04_Depot-Live-Verifikation.md`**, die nächste Session muss nichts neu abfragen. **Entscheidungen:** Allokation **wertbasiert** (Rate = Instrument, nicht Ziel) · `budget.monatlich_eur: 1068` als **Erhaltungs-Invariante** der §7.4-Staffel statt Eingangsfaktor · GOOGL-Ausschluss **förmlich aufheben** (drei Stellen) · **`entnahme_2027`**-Block: 9.000 € Einzahlung 11.08., investiert 13.08. in 5 Tranchen (IWDA 3150 · NOW 2000 · EIMI 1750 · AVGC 1190 · EXUS 910), heute 9.246,62 €, Ziel 10–11 k bis **07.08.2027**, raus aus **allen** Quoten inkl. US-Cap · kein Tranchen-/Klassen-Konstrukt. **Folge:** maßgebliche Dynastie-Basis **22.881 €** → 47,9/48,3/3,8 gegen 60/35/5 (ETF **und** Aktien ROT, Gold OK); NOW **12,33 %** statt 15,88 %, nach Entnahme 7,90 % → der Termin löst den Cap-Verstoß, nicht Verwässerung. Drift ist **Bestand, nicht Flow** (Ratenüberschuss 51 €/Mt → 59 Monate Aufbauzeit). **Befunde: H14 (HIGH)** `Rebalancing_Tool_v4.0.xlsx` Blatt `Parameter & Regeln` ist nicht inventarisierte Regelwerk-Quelle — **`Single-Stock-Cap` B10 existiert nur dort**, und **Stufe 1 Schritt 7 archiviert genau diese Datei** · **H15 (HIGH)** `KONTEXT.md` fehlt komplett als Sync-Ziel, 7 Stellen Drift (u. a. **IWDA am 17.08. mit übertragen statt 2027 verkauft** → §4b-Steuerplanung offen) · **H10 (HIGH)** drei FLAG-Blöcke in `config.yaml`, GOOGL steht in `flags_watchlist` → Widerspruch ist dreifach · H11/H1/M5/M6. **Bewusst offen in §11:** `allokation_drift`-Severity · Cap-Parameter (Höhe/Hysterese/Steuerjahr) · Ernte-Auslöser (Owner-Vorschlag: **Konzentrations-Kappung als Ernte-Trigger**, abgegrenzt vom verbotenen Block-Rebalancing). **⚠️ AVGO Q3 FY26 Tag +1 überfällig** (Call 03.09. amc, letzte Analyse 13.06. = 83 Tage). **Selbstkritik:** 6 Fehlaussagen in einer Session, eine Wurzel — „Teilausschnitt → Ganzes" (Korrektur-Log im Analyse-Doc §5).
- **Datum:** 2026-08-26/27 (Di/Mi, Nacht-Session) — **✅ Architektur-Spec v1.5 — 95%-GATE PASSIERT (PIPELINE #83, scoring-neutral, kein §18-Score-Event).** Vierte Prüfrunde, erstmals **gegen die Scalable-API** statt nur gegen das Repo, plus zwei Codex-Runden (eine enge Verifikation, eine offene Suche — Überschneidung praktisch null). **13 Befunde, 5 HIGH:** `geschrieben_am` scheitert an `ConfigDict(extra="forbid")` in `schemas.py:364` → Schema-Bump 1.0→1.1 nötig, `schemas.py` fehlte im Blast-Radius · **Roster-ISINs existieren nirgends im Repo** (config.yaml führt 6, alle ETFs; xlsx keine) → Quelle ist der Broker → **Stufe 1 ist nicht offline durchführbar** · Vault-Frontmatter trägt Scores nur für 3 Ersatzbank-Seiten, `cross_source.py` überspringt die leere Quelle **still und absichtlich** (Z. 184/332-334) · **GOOGL:** Vault führt „struktureller Ausschluss seit 01.04." gegen die neue Core-Klassenregel mit 50 €/Mt → Stufe-0-Entscheidung nötig · `INSTRUKTIONEN §22` ist eine achte Score-Kopie (Z. 542-556) und fehlte in allen Sync-Zielen. **Codex zusätzlich:** `CLAUDE.md` trägt den alten 8-9-Datei-Sync als Fließtext (Z. 27/29/57/59/77/78) und gehört in denselben Commit wie der xlsx-Move · `provenance_gate.py:176-181` blockiert Gate 1 **hart** in P3.5 bei `vollanalyse` (35/37 Records) — §4.4 nannte es nur „bedeutungslos". **Live-Verifikation:** 4 Spec-Zahlen bestätigt (NOW 14,6 % · Gold 2,7 % · Sparplan-Ist 1068 vs. SOLL 1031 · Depotwert 30.124 €), eine falsifiziert (META hat **keine** Position, nur Sparplan ab 01.09. — wie GOOGL). §11 Punkte 4/5/6/7 geschlossen, 11/12/13 neu. **Stand: Stufe 0 + 1 umsetzungsreif (1 nicht offline), Stufe 2 gated auf §4.4 + §4.1 + `provenance_gate` Check #2. Offen nur noch Owner-Entscheidungen, keine Wissenslücken.**
- **Datum:** 2026-08-26 (Di) — **📐 Depot-Architektur-Spec v1.4 SPEC-READY (PIPELINE #83 NEU, scoring-neutral, kein §18-Score-Event).** Konsequenz aus der Scalable-Anbindung: Positionen/Raten/Cash/Kurse sind **Zustand aus der API**, Urteil bleibt append-only in den beiden jsonl, Politik zieht in ein neues `00_Core/REGELWERK.yaml`; `PORTFOLIO.md` + `Faktortabelle.md` + `config.yaml` + Vault-Frontmatter werden **generiert**. Der aktuelle Score bekommt keinen Ort mehr — er ist der letzte Record je Ticker. Bilanz: −3 xlsx, −2 Skills, −900 Z. Prüfcode, §18 von 8-9 auf **4 Quellen mit je einem Schreiber**. 3 Codex-Runden, 14 HIGH alle nachgeprüft + bestätigt; Codex-Urteil **Stufe 0+1 umsetzungsreif, Stufe 2 gated**. **Fund mit Portfolio-Relevanz: GOOGL trägt seit 15.03. einen CapEx/OCF-Trigger ohne Resolve** und wird seit 26.08. mit 50 €/Mt als Core-4-Titel bespart — sichtbar nur in `flag_events.jsonl`. Entschieden: Rebalancing-Modell **additiv** mit gestaffeltem Ziel (Ersatz → Block-Untergewicht → ETF-Core).
- **Datum:** 2026-06-16 (Mo) ~00:00–01:10 Europe/Berlin — **🔬 Quellen-Audit Free-Stack (scoring-neutral; NUR Doc/Memory durable, KEINE Workflow-Edits — die folgen frische Session).** Empirisch geklärt (Sandbox-Probes + Shibui-Schema + yfinance 1.3.0): **defeatbeta + Shibui + yfinance decken ALLE Fundamentals-Daten aller 11 Satelliten ab, gratis → kein EODHD ($60)/FMP ($99)-Kauf nötig.** Lineage-Schlüssel: **Shibui = EODHD/Tiingo** (US-only), **defeatbeta + yfinance = Yahoo**. **Unabhängiges Struktur-Dual nur US + ASML**; **RMS/SU/KYCCF nur Yahoo-Backend → CORROBORATED** + **KEINE non-US-Transcripts**. Durable in `01_Skills/cross-source-verify/GATE0-COVERAGE.md`.

## 🎯 Resume-Anweisung für nächste Session

**Cold-Start:** Keine fixed Track-Empfehlung. Live-Forward-Tracks sind ausschließlich `00_Core/PIPELINE.md` offene Items (numbered list, Status-Felder normativ) und die unten stehende `📅 Nächste reguläre Termine`-Tabelle. Falls Resume mit konkretem `!`-Trigger oder Klasse-B-Earnings-Slot: Routing-Table in `CLAUDE.md` ist verbindlich.

**Wichtig — Re-Investigation-Recall-Check (Memory `feedback_pre_investigation_recall_check`):** Vor mehrschrittiger Diagnose immer EIN `mem-search`/PIPELINE-Live-Grep-Pass; veraltete Handover-Banner waren am 2026-05-26 nachweislich Quelle eines #73a-Misroutings, deswegen ist Live-State immer Ground-Truth, nie Handover-Snapshot allein.

### 🔼 PRIORITÄT nächste Session — Owner-Entscheidungen, dann Stufe 0

> **🔓 GATE PASSIERT (27.08.).** Die User-Direktive vom 26.08. („Unter 95 % Confidence will ich nicht in die Planung gehen") ist erfüllt: Spec v1.5, vier Prüfrunden, R4 erstmals **gegen die Live-API**. Was jetzt offen ist, sind **Owner-Entscheidungen — keine Wissenslücken.** Die schließt keine weitere Review-Runde.

**Ausgangslage:** `03_Tools/depot-architecture-spec.md` **v1.5** (744 Z.), PIPELINE #83. Urteil beider R4-Runden: Stufe 0 + Stufe 1 umsetzungsreif, **Stufe 1 aber nicht offline** (Roster-ISINs kommen nur vom Broker). Stufe 2 gated auf Gate-Neufassung §4.4 **plus** Schema-Bump §4.1 **plus** `provenance_gate.py` Check #2.

**Zu entscheiden (Daten/Politik, nicht Recherche):**
1. **Klassen-Zuordnung** (§3.1) — Core-4 gesetzt; offen: NOW `satellit T1` oder `core`? Adobe/Veeva Tier? ZETA bestätigen? Costco Roster oder Abgang (dann auch `screener_exceptions`-Eintrag mit entfernen)?
2. **Ersatzbank-Synthese** (§3.2) — verstreut als Inline-`ersatz:`, `substitute_activation_global` und `watchlist`-Freitext. **Empirisch bestätigt 27.08.:** die Broker-Watchlist kann das nicht ersetzen — sie enthält 3 von 10 Kandidaten und ist eine andere Liste (Beobachtung statt Zuordnung). Bleibt Handarbeit.
3. **GOOGL-Ausschluss** (§9.3, NEU) — der Vault führt „struktureller Ausschluss seit 01.04.2026 — kein Einstieg", während 50 €/Mt laufen. Förmlich aufheben (Chronik-Eintrag) **oder** Override nach §3.3 mit `grund`/`seit`/`review_am`. Unkommentiert stehen lassen ist nicht zulässig.
4. **JEDI** (§11.11, NEU) — Position 2,25 Stk. ≈ 158 € **ohne Sparplan**. Halten, aufstocken, abgehen?
5. **ETF-SOLL-Raten** (§11.13, NEU) — Ist weicht bei allen sechs ab (Σ config.yaml 616 gegen Broker 563; JEDI 72 → 0, Gold 51 → 80).

**Danach Stufe 0** (Datenreparatur, ~30 min): APH-FLAG-Trigger in `flag_events.jsonl` nachtragen · AMZN-Divergenz in `flags_aktiv` klären · GOOGL-Entscheidung aus Punkt 3 umsetzen. Danach ist die jsonl die maßgebliche Quelle — deckungsgleich sind die Listen bewusst **nicht** (GOOGL bleibt divergent bis zur Analyse).

**Vor Stufe 1 beachten:** Regelwerk-Befüllen braucht den **laufenden Live-Layer** (ISINs aus `holdings ∪ savings_plans`) · `CLAUDE.md` gehört in denselben Commit wie den xlsx-Move (Z. 27/29/57/59/77/78 tragen den alten 8-9-Datei-Sync als Prosa) · `para18_sync/validator.py` in Stufe 1 stilllegen (bricht nicht, warnt aber dauerhaft).

**⚠️ Live-State-Warnung:** `PORTFOLIO.md`, `Faktortabelle.md`, `config.yaml`, PIPELINE.md und die drei xlsx beschreiben den **Juni-Stand** und sind seit dem Broker-Übertrag 17.08. + der Sparplan-Umstellung 26.08. bewusst veraltet. Live-Wahrheit ist die **Scalable-API**; dokumentierter Ist-Stand → `02_Analysen/2026-08-26_Depot-Reconciliation.md` Abschnitt F. Nicht punktuell nachpflegen — das ist Teil von #83.

**Offener Portfolio-Punkt, unabhängig von der Spec:** **GOOGL** trägt seit 2026-03-15 einen CapEx/OCF-Trigger ohne Resolve und wird seit 26.08. mit 50 €/Mt bespart. Klasse `core` → Analysepflicht, kein Ratenstopp. Dazu: AVGO Q3 FY26 am **03.09.** (FLAG-Resolve-Gate) und der unbearbeitete Juli-Earnings-Cluster (ASML/TMO/V/MSFT/APH/RMS/SU/AMZN/BRK.B).

**Ebenfalls beschlossen, noch nicht terminiert:** systemweiter Rückbau. Empirie 26.08.: 719 Commits seit 15.04., davon 42 (5,8 %) mit Portfolio-/Analyse-Bezug. Reihenfolge vom User bestätigt — (1) Spec fertig, (2) Rückbau-Inventar, (3) Zielbild Ordnerstruktur + CLAUDE.md + Routing. Anti-Creep-Regel steht in Spec §1.2.

---

### 🔽 NACHRANGIG (USER-Direktive 2026-06-16, weiterhin offen) — Free-3-Source-Stack vollumfänglich in Analyseworkflows einbinden

**Wichtiger als die cross-source-verify-Skill-Entscheidung** ist das Updaten der BESTEHENDEN Struktur. **Standing-Konvention ab sofort:** !Analysiere-Datensammlung = **defeatbeta + Shibui (US + ASML) + yfinance (Non-US-Primär)**. Empirie-SSoT (durable): `01_Skills/cross-source-verify/GATE0-COVERAGE.md` §Source-Routing CONFIRMED 2026-06-16.

**To-Do (eigene Session, §18-Sync-pflichtig — pipeline-item/system-zustand):**
1. **PIPELINE.md** — neues Work-Item (#83+) für diese Integration anlegen + Footer-Bump (jetzt bewusst NICHT angelegt, um §18-Welle nicht mitten in Capture zu zünden).
2. **dynastie-depot** — `01_Skills/dynastie-depot/references/sources.md` (o.ä.) + SKILL.md Datensammelschritt: Shibui als 2. strukturierter US-Layer + yfinance-Non-US-Routing + **Lineage-bewusste Verdikt-Tiers** (VERIFIED US+ASML / CORROBORATED RMS/SU/KYCCF) + **Basis-Norm-Pflicht** (Shibui-ROIC NOPAT/IC-TTM vs defeatbeta quartalsdekomponiert).
3. **Relevante 01_Skills prüfen/anpassen:** `non-us-fundamentals` (yfinance-Primär + Self-Consistency-Gate bestätigen), `insider-intelligence` (Form-4 EDGAR-Pfad), `quick-screener` (falls Quellen referenziert), `backtest-ready-forward-verify` (ScoreRecord-Quellen-Provenance/`notizen`).
4. **Caveats hart kodieren:** non-US-**Transcripts fehlen** (defeatbeta nur US/ASML → §19.1 für RMS/SU/KYCCF via IR-Webcast/Primär); Shibui **US-only + EODHD/Tiingo-Lineage** (NICHT unabhängig von EODHD — relevant falls je EODHD gekauft); `6861.T` `.info`-ROE/FCF=None → aus Statements rechnen; RMS CapEx/FCF historisch IFRS-flaky → Self-Consistency-Gate.
5. **cross-source-verify-Skill = NACHRANGIG** (Gate-0 ✅; GATE0-COVERAGE.md hält Befund). Erst NACH Struktur-Update entscheiden, ob eigener Skill nötig oder Konvention in bestehenden Skills reicht.

**§18-Impact dieser Capture-Session:** Keiner — SESSION-HANDOVER + Memory + GATE0-Doc = working-tree-doc, scoring-neutral, kein §18-Sync-Set-Touch (kein Score/FLAG/Sparraten/Pipeline-Item-Edit jetzt).

### 📅 Nächste reguläre Termine (chronologisch)

> ⚠️ **Stand 09.06.2026 — die Juli-Termine sind sämtlich verstrichen und unbearbeitet.** Der Cluster ASML 15.07. · TMO/NOW 22.07. · V 28.07. · MSFT/APH/RMS/KYCCF 29.07. · SU/AMZN 30.07. · BRK.B 01.08. · ZETA 04.08. liegt als Earnings-Nachzug offen; §19.1 Tag-0/Tag-+1-Split greift nicht mehr, alle Transcripts sind verfügbar. Nächster **zukünftiger** Termin ist AVGO Q3 FY26 am **03.09.** KYCCF ist nicht mehr im Depot. Vor Verwendung `03_Tools/earnings_calendar.py --check` neu laufen lassen.

| Datum | Item | Aktion |
|-------|------|--------|
| **15.07.** (bmo) | ASML Q2 | Nächstes Roster-Event (Q1 17.04. ✅; 30-Tage-Fenster →09.07. sonst leer) |
| **22.07.** | NOW Q2 / TMO Q2 | NOW O3-Vollanalyse (US `!Analysiere`; yf/UW, TipRanks 29.07 — IR-confirm pending) · TMO Organic+Clario |
| **28.07.** (amc) | V Q3 FY26 | Cross-Border-Velocity + ROIC-Methodology-Verify (#21) |
| **29.07.** | MSFT Q4 / APH Q2 / RMS H1 / KYCCF Q1 | MSFT CapEx+WACC (#25/#27) · APH China-Tax+CommScope (Score 61<65 FLAG) · RMS H1 · KYCCF Q1 (yf, JP-Termin verifizieren) |
| **30.07.** (amc) | SU H1 / AMZN Q2 | SU H1 · AMZN CapEx/OCF-FLAG-Re-Eval (Resolve-Gate <60%) + Vollanalyse |
| **01.08.** (Sa, 10-Q) | BRK.B Q2 FY26 | KHC-OTTI / GEICO-Decel / Form-13F Apple-Trim (#36) |
| **04.08.** | ZETA Q2 | O3-Vollanalyse (US, war QuickScreener-Rot) |
| **03.09.** (amc) | AVGO Q3 FY26 | FLAG-Resolve-Gate (Q2 04.06. 53→56, FLAG bleibt) — §19.1 Tag+1 |

### 📋 Pending offene Slots (kein fester Termin)

- **PIPELINE #52** Quick-Screener-Refresh deferred bis Use-Case-Trigger
- **PIPELINE #53** ✅ Decision-C USER-APPROVED 10.05. — Weiter beobachten + Re-Audit ~09.07.2026 mit Use-Case-Count-Tracking (Memory `project_trigger_landscape_audit_2026-05`)

### 🔬 Phase-D-Restbestand (deferred per Cluster-Trigger)

- **Phase-D-2 active-deferred-D2 Cluster:** EP-2013 + EKP-2020 → V Q3 FY26 ROIC-Methodology-Verify ~Ende Juli (PIPELINE #21)
- **Phase-D-2 meta-gate-deferred-D2:** BS-2015 → 2028-Review-Gate ODER nächste DEFCON-Block-Re-Gewichtung
- **Phase-D-3 source-only-deferred-D3:** CPZ-2019 → 2028-Review-Gate Backtest-Validation-Wave
- **Phase-D Reject-Inventarisiert:** BPZ-2023 → Latent für 2028-Review-Gate Backtest-Methodology-Roadmap

## 📌 Mini-Task: xlsx-smoke-test-runner Description-Optimization-Loop — RE-DEFERRED 2026-05-26

**Status:** Re-Deferred (User-Entscheidung 2026-05-26 ~13:50 GMT+2). Pain-grounded Trigger statt Polish-Tier-Spec.

**Was passiert ist (2026-05-26 13:40-13:50 GMT+2):**
1. 20 Trigger-Eval-Queries gedraftet (10/10 Split), HTML-Review via `assets/eval_review.html` durchlaufen, User hat 3 Tweaks bestätigt (#9 schärfen, #16 → Cell-Existence-§C/D-Boundary, #20 → Cell-Number-Format-§Out-of-Scope-Boundary).
2. `eval_set.json` exportiert + ins Workspace kopiert (`01_Skills/xlsx-smoke-test-runner-workspace/desc-opt-iteration-1/eval_set.json`, 20 Queries, 10 positive).
3. `python -m scripts.run_loop` gestartet → **sofortiger Crash** mit `WinError 10038` (alle 8 Parallel-Worker-Subprocess-Calls failen) + `UnicodeEncodeError cp1252 ✗`.

**Blocker (durable diagnostiziert):**
- **Root-Cause:** `skill-creator/scripts/run_eval.py:108` benutzt `select.select([process.stdout], ...)` — auf Windows funktioniert `select.select` ausschließlich mit Socket-Handles, nicht mit Pipe-Handles. Fundamentale Plattform-Inkompatibilität (Python-Doku: "On Windows, the underlying select() function is provided by the WinSock library, and does not handle file descriptors that don't originate from WinSock").
- **Sekundär:** `run_loop.py:151/278/317/321` schreibt HTML via `.write_text(generate_html(...))` ohne `encoding='utf-8'` → cp1252-Crash bei UTF-8-Symbolen (✗/✓). Klassische Memory-Anker `feedback_windows_console_ascii_safe_inline_python`.
- **Konsequenz:** Description-Optimization-Loop ist auf Windows-Nativ-Python NICHT lauffähig. Brauchbar nur via WSL2-Ubuntu (~60-90min Setup: Plugin-Cache + OneDrive-Workspace WSL-side mounten) ODER lokalem Plugin-Patch (~30-45min, Risiko: Upstream-Drift bei Plugin-Update).

**Begründung Re-Defer (statt WSL/Patch):**
- Description ist frisch empirie-validiert (Commit `aab66f4` post-Codex 2026-05-26 ~00:47): 0 HIGH/MEDIUM/LOW Findings open; literal-Scope §A/§B/§E/§G in / §C/§D/Cell-Format out korrekt abgebildet.
- Zero Real-World-Empirie bisher (Skill <24h alt, 0 Live-Trigger-Events) — kein konkretes Drift-Signal das WSL/Patch-Aufwand rechtfertigt.
- Polish-Tier per ursprünglicher Pickup-Spec, kein Blocker für offene PIPELINE-Items oder reguläre Termine.
- Memory-Anker `feedback_redefer_over_prespec_dynastie` (24.05.2026): bei <2 Real-Runs + Infrastruktur-Pain → Re-Defer mit pain-grounded Trigger ist nominaler Pfad.

**Re-Trigger-Schwellen (klar verifizierbar):**
1. **Untrigger-Drift:** ≥1 dokumentierter Real-World-Case wo User ein `openpyxl`-Live-Tool-Mutation macht UND Skill silent bleibt (Detection via Pre-Commit-Hook-Block oder downstream-Audit-Fail) → konkretes Pain-Signal.
2. **Overtrigger-Drift:** ≥1 Case wo Skill triggert bei klarem Non-Smoke-Kontext (z.B. Markdown-Edit, `!`-Routing-Trigger) und User-Override braucht.
3. **Description-Mutation-Anlass:** SKILL.md description wird aus anderem Grund substantiell editiert (Scope-Expansion §C/§D inkl., neues 4. Live-Tool, etc.) → Optimization-Loop wird auf neuer Description-Baseline sinnvoll.
4. **Tooling-Fix:** skill-creator-Plugin patched select-Issue upstream ODER WSL2-Dynastie-Bridge wird für anderen Use-Case aufgesetzt (sunk-cost-Argument).

**Durables Substrate (für nächsten Pickup, falls Re-Trigger hits):**
- Eval-Set: `01_Skills/xlsx-smoke-test-runner-workspace/desc-opt-iteration-1/eval_set.json` (20 Queries, 10/10 Split, User-validiert + bewusst editiert; SKILL-Description-Contract-aligned — §C/D/Cell-Format Out-of-Scope-Boundaries explizit covered).
- Draft-JSON: gleiches Verzeichnis `trigger-eval-draft.json` (Vorstufe vor User-Review).
- Workspace-Verzeichnis bleibt erhalten unter `01_Skills/xlsx-smoke-test-runner-workspace/` (gitignored per `.gitignore` Pattern `01_Skills/*-workspace/`, lokal-only — Skill-Creator-Convention, kein §18-Substrate).

**Memory-Anker (neu + reused):**
- NEU: `reference_skill_creator_windows_pipe_incompat` (run_eval.py select.select Pipe-Trap, Line 108, mit Fix-Pfaden).
- Reused: `feedback_skill_name_is_scope_contract` · `feedback_brainstorming_terminal_override_dynastie` · `feedback_codex_default_english_in_dynastie` · `feedback_redefer_over_prespec_dynastie` · `feedback_windows_console_ascii_safe_inline_python` · `feedback_pre_investigation_recall_check`.

**§18-Sync-Impact:** Keiner. SESSION-HANDOVER.md ist working-tree-only, außerhalb §18-Trigger-Set. Reiner doc-Commit ohne Sync-Wave.

**Out-of-Scope (war + bleibt):** Kein Code-Change am Skill, kein Hook-Behavior-Change, kein Version-Bump.

---

## 🔖 Vorgänger-Historie

Vollständige Banner-Historie + Phase-0a/0b-Detail + Phase-D-1-Final-Closure 09.05. + Konsolidierungstag-Wave-1/2/3/4 + Cluster-A-#31/#32/#33/#34 + Wiki-Modus-#54 + AVGO/MSFT/V/BRK.B/APH-Vollanalysen → **`05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md` + git log + STATE.md Critical-Alerts (≤10-Tage-Window) + CORE-MEMORY.md §13 (System-Lifecycle) + Vault `log.md` + `archive/log/` (vollständige History; quartalsweise Roll-over per INSTRUKTIONEN §18.6, Initial-Cut 10.05.2026)**.

**Skill-Versions-Stempel:** dynastie-depot v3.7.6 (SKILL §410 + §27.7-Anti-Buyback-Cross-Reference + Bull-DCF-Source-Pflicht + ATH-Distance-Boundaries; keine Versions-Bump bei Confidence-Upgrade-Pass — nur Begründungs-Härtung). User-Manual-Step bei Skill-Edits: `06_Skills-Pakete/dynastie-depot_v3.7.6.zip` neu deployen + Desktop-App-Install.
