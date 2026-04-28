# Ruflo-Integration-Plan — Dynastie-Depot

**Status:** Draft v1.0 — pending Phase-1-Start
**Erstellt:** 2026-04-28
**Basis-Quelle:** Ruflo USERGUIDE.md v3.5 (7557 Zeilen, vollständig durchgegangen)
**Kontext:** User will Ruflo statt Superpowers nutzen, optimal in Dynastie-Depot einbinden
**Vorgehensweise:** Inkrementell in 4 Phasen, jede mit Stop-Criterion + Rollback

---

## Executive Summary

Ruflo ist ein generalistisches Multi-Agent-Orchestrierungs-Framework mit Code-Domain-Bias. Für Dynastie-Depot (Markdown-Vault, Skill-deterministisch, Single-User) sind ~25% der Features echter Hebel, ~50% irrelevant, ~25% schädlich wenn als Default aktiviert.

**Größter Hebel:** Self-Learning Memory (ADR-048 + ADR-049 + ADR-050) — wandelt statisches APPLIED-LEARNING in PageRank-ranked Auto-Pattern-Recall.

**Größtes Risiko:** Globale Ruflo-CLAUDE.md-Defaults (`/src/tests/docs`, "1 message = all ops", Swarm-Pflicht) kollidieren frontal mit Dynastie-Architektur.

---

## Voranalyse-Ergebnisse (für Resumption-Kontext)

### Diff zwischen Ruflo-CLAUDE.md und Dynastie-CLAUDE.md

**9 Hard-Conflicts** (müssen explizit überschrieben werden):

| # | Ruflo-Regel | Dynastie-Reality |
|---|-------------|------------------|
| 1 | `File Org: /src /tests /docs /config /scripts /examples` | `00_Core/ 01_Skills/ 02_Analysen/ 03_Tools/ 04_Templates/ 05_Archiv/ 06_Skills-Pakete/ 07_Obsidian Vault/` |
| 2 | `NEVER save working files, text/mds, or tests to root folder` | CLAUDE.md liegt selbst im Root |
| 3 | `NEVER proactively create *.md` | DEFCON-Analysen + log + ScoreRecords sind Kern-Output |
| 4 | `1 MESSAGE = ALL RELATED OPERATIONS` | §18 Sync erfordert Reihenfolge |
| 5 | `MUST initialize swarm... MUST spawn concurrent agents... ALWAYS run_in_background` | Skill-deterministisch, sequenziell |
| 6 | `npm run build / test / lint` | Kein npm, nur Python in 03_Tools/ |
| 7 | `ALWAYS verify build succeeds before committing` | Kein Build-Step |
| 8 | `Use event sourcing for state changes` | State = Markdown + JSONL-Append |
| 9 | `Project Config: hierarchical-mesh, 15 Agents, HNSW, Neural` | Skill-basiert, kein Multi-Agent-Modell |

**4 Soft-Conflicts** (Kontext-abhängig):
10. DDD with bounded contexts — nur in 03_Tools/ relevant
11. TDD London School — optional für Python-Tools
12. Typed interfaces for all public APIs — nur 03_Tools/
13. Files unter 500 Zeilen — INSTRUKTIONEN.md sprengt das bewusst

**7 Compatible Features** (ohne Konflikt nutzbar):
A. `aidefence_scan` / `aidefence_is_safe` — Pre-Edit-Hook + Tavily-Filter
B. `memory_import_claude` + `memory_search_unified` — Cross-Session-Pattern-Recall
C. `memory_store` mit Namespace `patterns`
D. AIDefence vor Tavily-Web-Fetches
E. `NEVER commit secrets, .env files`
F. `ALWAYS read a file before editing`
G. `Run tests after code changes` für 03_Tools/ Python

### Filter-Tabelle (komplette Bewertung)

✅ **Aktiv nutzen** (HEBEL: groß)
1. ADR-048 Auto Memory Bridge
2. ADR-049 LearningBridge + MemoryGraph + AgentMemoryScope
3. ADR-050 Intelligence Loop (Top-K Pattern-Recall, Top-K=3)
4. ADR-051 Context Autopilot
5. AgentDB v3 Controllers: HierarchicalMemory + CausalRecall + ExplainableRecall + AttestationLog
6. Statusline (ohne DDD-Bar)
7. Custom Tool Mode `dynastie`: `memory,monitor`
8. 6 Hooks: session-start/end, pre/post-task, pattern-store/search
9. Worker Manager: `patterns`, `adr`, `consolidate`, `predict`, `learning`
10. Codex Dual-Mode für Algebra-Gate-Verify + Multi-Ticker-Batch
11. Stream-Chain für Skill-Pipeline-Formalisierung
12. Doctor periodisch
13. AIDefence pre-agent-input für Tavily-Outputs
14. Trajectory-Recording für DEFCON-Score-Begründung-Audit

🔥 **Spannend, lohnen Eval** (HEBEL: groß, RISIKO: medium)
15. Hyperbolic Embeddings für Sektor-Taxonomie (Healthcare→MedDev→TMO)
16. Granger Causality (GraphTransformerService) auf score_history.jsonl
17. plugin-prime-radiant für Hallucination-Prevention via Consensus
18. plugin-cognitive-kernel für Miller's Law (7±2)-Check der 28-Faktor-Bewertung
19. plugin-hyperbolic-reasoning für taxonomische Inferenz
20. Drift-Detection zwischen aufeinanderfolgenden DEFCON-Analysen
21. MCP Multi-Client: Ruflo via HTTP für ChatGPT-Mobile-Workflow

⚠️ **Selektiv** (HEBEL: situativ)
22. Hive-Mind nur für `!BatchScan`-Trigger
23. Claims-System für Codex-Sparring-Stuck-Detection
24. AIDefence Multi-Agent-Consensus für Score-Disagreement
25. Browser-Automation perspektivisch zur Ablösung der `annual-*`-Skills

❌ **NICHT integrieren** (klar abgegrenzt)
- WASM Agent Booster (kein Code)
- Tier 1 Routing (irrelevant)
- SPARC-Methodology als Default
- DDD Bounded Contexts
- 21 von 27 Hooks
- IPFS-Marketplace (Privat-Vault)
- Pre-trained Pattern-Packs (alle Code-Domain)
- `plugin-financial-risk` (PCI-DSS, nicht Investment)
- `plugin-healthcare`, `legal`, `code/test/perf-intelligence`, `qe`, `gastown`, `neural-coordination`, `quantum`
- RuVector PostgreSQL (Single-User → AgentDB+SQLite reicht)
- Flow Nexus Cloud (Single-User)
- Pair Programming
- Mesh/Ring/Star-Topologies
- Agentic-Jujutsu
- Performance-Benchmarking Code-fokussiert
- Testing-Framework (kein TS)
- Migration V2→V3 (frisch installiert)
- Auto-Update wenn aggressiv
- 9 von 12 Hook-Workers (nur consolidate, predict, ggf. ultralearn)
- Dev-Tools/Helper-Scripts (du hast eigene `03_Tools/`)
- Pattern-Marketplace
- Stream-Chain-Templates für Code (feature/security/refactor)
- Provider-Failover (Single-Provider)

---

# Phase 1 — Sofort & risikolos (Woche 1-2)

**Ziel:** Größter Hebel mit minimalem Eingriff. Memory-Layer + Override-Schutz + Token-Save.

## Schritte

### 1.1 Override-Block in `Claude Stuff\CLAUDE.md`
Append-only, am Ende der Datei. Liste die 9 Hard-Conflicts aus Tabelle oben explizit als "in diesem Projekt überschrieben". Dynastie-Architektur (00_Core/01_Skills/...) bleibt SSoT.

### 1.2 ADR-048 Auto Memory Bridge aktivieren
```bash
npx ruflo@latest memory init --force
node .claude/helpers/auto-memory-hook.mjs import-all
```
Auto-Memory (`~/.claude/projects/.../memory/*.md`) wird in AgentDB importiert mit ONNX-Embeddings (384-dim).
**Read-only auf Markdown** — keine Auto-Generierung in APPLIED-LEARNING.md, nur in `pending-insights.jsonl`.

### 1.3 ADR-050 Intelligence Loop (Top-K=3)
```bash
npx ruflo@latest hooks intelligence --status
node .claude/helpers/hook-handler.cjs stats   # Baseline
```
Top-K=3 statt Default 5 wegen kleiner Memory-Basis (~10 Entries). Bei jedem UserPrompt werden Top-3 PageRank-gerankte Patterns ins Context injected.

### 1.4 ADR-051 Context Autopilot
Default-Schwellen (warn 70%, prune 85%). Verhindert dass DEFCON-Sessions tool-output verlieren bei Compaction.

### 1.5 Custom Tool Mode `dynastie`
```bash
export CLAUDE_FLOW_TOOL_GROUPS=memory,monitor
```
In `.claude/settings.json` persistent setzen. Reduziert ~313 Tools auf ~30-50. Tool-Schemas im System-Prompt schrumpfen massiv → Token-Save.

### 1.6 Statusline aktivieren, DDD-Bar disabled
Auto via `npx ruflo init`. In `.claude/settings.json` DDD-Component manuell rausnehmen oder leer lassen (Dynastie-irrelevant). `🛡️ ctx% | tokens | 🧠 intel%` reicht.

### 1.7 6 Hooks (von 27) aktivieren
In `.claude/settings.json`:
```json
{
  "hooks": {
    "session-start": { "enabled": true },
    "session-end": { "enabled": true },
    "pre-task": { "enabled": true },
    "post-task": { "enabled": true },
    "pattern-store": { "enabled": true },
    "pattern-search": { "enabled": true }
  }
}
```
Andere 21 explizit `"enabled": false`.

### 1.8 Doctor-Baseline ziehen
```bash
npx ruflo@latest doctor --verbose > /tmp/ruflo-baseline-$(date +%F).txt
```
Snapshot vor jeder Phase-Änderung.

### 1.9 Trajectory-Recording auf `dynastie-depot`-Skill verdrahten
Im Skill am Anfang `trajectory-start --task "$ticker"`, am Ende `trajectory-end --success $verdict`. Liefert RL-Training-Daten + Audit-Replay für jede DEFCON-Analyse.

## Risiko: NIEDRIG
- Memory-Bridge ist additiv (read-only auf MD, write nur in AgentDB)
- Tool Mode reversibel via env-Reset
- Hook-Subset isoliert
- Worst Case: Alle Phase-1-Features deaktivieren via Settings-Flip

## Erfolgskriterium
- Nach 5 Sessions: `intelligence stats` zeigt **Trend: IMPROVING** mit confidence-drift > 0
- Token-Usage pro Session ~20% niedriger (durch Tool-Mode)
- Statusline zeigt live Daten ohne Crash
- Mind. 3 Trajectories aufgezeichnet

## Rollback
```bash
unset CLAUDE_FLOW_TOOL_GROUPS
# .claude/settings.json hooks alle auf false
# Override-Block in CLAUDE.md rauslöschen
```

---

# Phase 2 — Eval-Phase (Woche 3-6)

**Ziel:** Validierung der 5 vielversprechenden, aber unsicheren Hebel. Jeder einzeln, mit Pilot-Use-Case.

## Schritte

### 2.1 AgentDB v3 Controllers schrittweise

Reihenfolge nach Risiko:
1. **HierarchicalMemory** (Working/Episodic/Semantic + Ebbinghaus-Forgetting): mit MEMORY.md anfangen — jeder Entry kommt initial in Episodic, nach 3+ Accesses → Semantic. Ergibt natürliche Pattern-Promotion.
2. **AttestationLog** aktivieren: jede Memory-Operation gibt cryptographic-Audit-Trail. Ergänzt `00_Core/log.md` um Memory-Layer-History.
3. **ExplainableRecall**: bei Top-3-Pattern-Injection liefert Zertifikat "warum gerade diese". Nutzbar in §28-Score-Begründung.
4. **CausalRecall** (riskanter): Causal Re-Ranking statt Pure-Similarity. Pilot mit FLAG-Pattern (z.B. "Sparraten-Drift TMO 23.04. → Anker-Promotion-Lücke 25.04." als kausale Edge).

**Stop-Criterion**: Falls CausalRecall die Pattern-Empfehlungen schlechter macht (mehr Noise) → zurück auf Pure-Similarity.

### 2.2 Worker Manager 7 — die 5 relevanten aktivieren
```bash
.claude/helpers/worker-manager.sh start 60
# In settings.json: nur patterns, adr, consolidate, predict, learning enabled
```
- `patterns` (15min): Dedup APPLIED-LEARNING + Auto-Memory
- `adr` (15min): Compliance-Check auf INSTRUKTIONEN.md §§ — bei Edits gegen §-Referenz prüfen
- `consolidate` (30min): Memory-Konsolidierung (Episodic→Semantic)
- `predict` (Hook-Worker): bei `!Analysiere`-Trigger Pre-Load
- `learning` (30min): SONA-Optimization

Nach 1 Woche: Worker-Stats prüfen. Wenn `adr` False-Positives wirft (legitime §-Erweiterungen blockt) → auf warn-only stellen.

### 2.3 Codex Dual-Mode für §28.2 Algebra-Gate (Pilot)
1. Codex-Companion sicherstellen: `/codex:setup` skill
2. INSTRUKTIONEN.md §28.2 ergänzen (3-5 Zeilen):
   > "Bei Algebra-Δ-Gate **optional**: parallel zu Claude-Berechnung Codex-Background-Worker spawnen für Independent-Verify. Verdict-Match = ✅, Mismatch = Hard-Stop + Hand-Verify."
3. Pilot bei nächster Score-Update-Aktion testen
4. Erfolgsmessung: Match-Rate über 5 Algebra-Gates. Bei <80% Match → Worker zurückziehen, Workflow zu schwach formalisiert

### 2.4 AIDefence pre-agent-input für Tavily
```json
{
  "hooks": {
    "pre-agent-input": {
      "command": "node -e \"const { isSafe } = require('@claude-flow/aidefence'); if (!isSafe(process.env.AGENT_INPUT)) { process.exit(1); }\"",
      "timeout": 5000
    }
  }
}
```
Schützt vor injizierten Inhalten in Tavily-Crawl-Outputs (z.B. wenn ein gescraped'es Earnings-Call-Transcript prompt-injection enthält). 0.04ms Overhead — vernachlässigbar.

### 2.5 Stream-Chain Pipeline-Definition für `dynastie-depot` Skill

YAML-File `01_Skills/dynastie-depot/pipeline.yaml`:
```yaml
name: dynastie-defcon-analysis
stages:
  - research-data       # defeatbeta + non-us-fundamentals
  - apply-§28-scoring   # 28-Faktor-Bewertung
  - algebra-gate-verify # §28.2
  - score-record-draft  # ScoreRecord-JSON
  - persist-via-skill   # backtest-ready-forward-verify Schritt 7
  - sync-§18            # log + CORE-MEMORY + Faktortabelle + PORTFOLIO + score_history + config.yaml
```
Formalisiert was der Skill heute implizit macht. Vorteil: klare Stage-Trennung erlaubt Stream-Pipeline-Hooks (z.B. Stage-Quality-Score, retry-on-fail).

### 2.6 Hyperbolic Embeddings für Sektor-Taxonomie (Pilot)
```bash
npx ruflo embeddings init --hyperbolic
```
Sektoren-Taxonomie aufbauen: Healthcare → MedDev → TMO. Distanz Healthcare-TMO vs Industrial-TMO sollte semantisch korrekter sein. Pilot: peer-Vergleich für 2 Ticker (z.B. TMO vs Hermès) — ist hyperbolische Distanz informativer als Euclidean?

### 2.7 Drift-Detection Baseline
Bei `!Analysiere TMO Q2`: Snapshot als Baseline setzen. Bei `!Analysiere TMO Q3`: Drift-Score zur Q2-Baseline. Drift > 0.15 = automatisch flag "signifikante Strategie-Änderung".

## Risiko: MITTEL
- AgentDB v3 Controllers könnten Pattern-Empfehlungs-Qualität verschlechtern
- `adr`-Worker kann False-Positives generieren
- Codex-Worker-Pattern muss erst etabliert werden
- Stream-Chain-Migration ist Skill-Refactor mit Breakage-Risk

## Erfolgskriterium (Woche 6 Review)
- Codex Algebra-Gate-Match-Rate ≥80% über 5 Runs
- Tavily-AIDefence: keine False-Positives in 4 Wochen
- HierarchicalMemory: ≥3 Patterns spontan zu Semantic promoted
- Worker `patterns`: APPLIED-LEARNING-Duplicate-Count rückläufig
- Stream-Chain-Pipeline läuft stable für 1 Voll-Analyse
- Hyperbolic Sektor-Distanzen plausibel (manueller Sanity-Check)

## Rollback
Jeder einzelne Schritt isoliert deaktivierbar. `adr`-Worker zuerst zurückziehen wenn nervig. Stream-Chain-Pipeline zurück zum monolithischen Skill ist 1-Commit-Revert.

---

# Phase 3 — Selektive Erweiterung (Monat 2-3, situativ)

**Ziel:** Use-Case-getriebene Aktivierung. Nur wenn Phase 1+2 stabil seit 4 Wochen.

## Schritte

### 3.1 Hive-Mind für `!BatchScan`-Trigger
- Neuer Trigger in CLAUDE.md Routing-Table: `!BatchScan satellites` oder `!BatchScan watches`
- Hierarchical Topology, Strategic Queen, max 8 Worker (≤Anzahl Satelliten)
- Worker spawnen `dynastie-depot`-Skill je Ticker parallel
- Byzantine Consensus optional bei FLAG-Disagreement (Pilot: Skip Byzantine, später nachrüsten)
- Hard-Cap: Max $5 pro BatchScan-Run, sonst Abort

### 3.2 Claims-System für Codex-Sparring
- Bei langlaufenden Codex-Reviews (>5min): Codex registriert Claim
- Stuck-Detection: 30min ohne Progress → STEALABLE → Claude übernimmt
- Visual-Board: `npx ruflo issues board` für laufende Sparring-Sessions

### 3.3 Multi-Agent Security Consensus für Score-Disagreement
- Bei FLAG-Trigger-Edge-Case: 3 unabhängige "Agents" (Claude-Strat, Claude-Skeptic, Codex) bewerten
- `calculateSecurityConsensus`-API auf Score-Verdict übertragen
- Konsens nötig für FLAG-Promotion zu STATE.md

### 3.4 Browser-Automation für `annual-*`-Skills (Migration-Eval)
- 1 Skill als Pilot: `annual-revenue` migrieren auf `@claude-flow/browser`
- Vorteil: Trajectory-Learning lernt Yahoo-Element-Selektoren, Drift-Detection bei Yahoo-Änderungen
- Aufwand: ca. 2-3 Stunden Refactor pro Skill
- Wenn Pilot erfolgreich: Plan für 6 weitere annual-*-Skills

### 3.5 MCP Multi-Client für Mobile-Workflow
- Ruflo MCP via HTTP-Transport: `npx ruflo mcp start --transport http --port 3000`
- ChatGPT-Pro/Plus Developer-Mode → Connector zu localhost:3000 (oder via Tunnel/ngrok wenn Mobile-extern)
- Ergänzt Memory `feedback_tavily_connector_uuid_rotation.md` um Ruflo-Layer
- Erlaubt Score-Lookups via ChatGPT-Mobile ohne Claude Code

## Risiko: MITTEL-HOCH
- Hive-Mind: Score-Konsistenz-Risk wenn Worker isoliert scoren
- Claims-System: nur sinnvoll bei realen langen Codex-Sessions
- Browser-Migration: Skill-Breakage-Risk während Refactor
- MCP-HTTP: Sicherheits-Implikation bei externem Tunnel

## Erfolgskriterium (Monat 3 Review)
- BatchScan: 11 Satelliten-Scan in <50% der seriellen Zeit, FLAG-Konsistenz vs serieller Run validiert
- Claims-Board zeigt aktive Codex-Sessions sinnvoll
- Mind. 1 annual-*-Skill auf Browser migriert + stable
- Multi-Client-MCP: 1 erfolgreicher Mobile-Lookup

## Rollback
- BatchScan-Trigger entfernen → Routing-Table-Default greift wieder
- Claims-System ausschalten → Codex-Sparring bleibt ad-hoc
- Browser-Migration einzelner Skill via Git-Revert

---

# Phase 4 — Optional & langfristig (Monat 3+)

**Ziel:** Experimentelle Hebel. Nur evaluieren wenn 1-3 stable. Hier ist's "nice to have", nicht "needed".

## Schritte

### 4.1 plugin-prime-radiant — Hallucination Prevention via Consensus
- 6 mathematische Engines, davon 2 relevant: **Causal Inference** + **Consensus Verification**
- Use-Case: bei DEFCON-Score-Berechnung mathematische Plausibilitäts-Check gegen Wiss-Fundierung
- Tools: `pr_coherence_check`, `pr_causal_infer`, `pr_consensus_verify`
- Risiko: Alpha + Mathematik-Komplexität — könnte Score-Workflow überlasten

### 4.2 plugin-cognitive-kernel — Miller's Law (7±2)
- 28-Faktor-Bewertung sprengt Working-Memory-Limit
- Plugin könnte erkennen wenn Reasoning Working-Memory überlastet → Empfehlung: Faktoren-Cluster vor Score-Synthese
- Use-Case: Meta-Audit der Faktortabelle-Anwendung

### 4.3 plugin-hyperbolic-reasoning — Taxonomic Inference
- Erweitert Phase-2-Hyperbolic-Embeddings um aktive Inferenz
- "Wenn TMO in MedDev-Cluster und MedDev-Sektor hat FLAG X, gilt FLAG X auch für TMO?" — taxonomische Vererbung von Sektor-Patterns

### 4.4 Granger Causality auf score_history.jsonl
- GraphTransformerService extrahiert kausale Beziehungen zwischen Score-Faktoren
- Beantwortet: "Welche Faktor-Bewegungen sind predictive für FLAG-Trigger?"
- Erfordert: ≥30 Score-Records minimum für statistische Signifikanz
- Output: Faktortabelle-Refactor-Vorschläge ("Faktor 17 redundant zu Faktor 9")

### 4.5 Guidance Library — Hard Gates (post-Alpha)
- Sobald `@claude-flow/guidance` aus Alpha raus
- Compile INSTRUKTIONEN.md §18 + §28.2 zu PolicyBundle
- Hard-Gate für §18 Sync (alle Sync-Targets in einem Commit erforderlich)
- Hard-Gate für §28.2 Algebra (Codex-Independent-Verify mandatory bei kritischen Scores)
- Risiko: False-Positives blocken legitime Edits → vorher 2-Wochen warn-only-Phase

### 4.6 Pattern-Export als Backup
- Memory + APPLIED-LEARNING als RVF-File exportieren
- **Privat** (nicht in IPFS-Marketplace): lokales Backup
- Cron: monatlich in `05_Archiv/`

### 4.7 Helper-Scripts evaluieren vs. eigene `03_Tools/`
- Ruflo bringt 30+ Helper-Scripts mit (`.claude/helpers/`)
- Du hast eigene `03_Tools/` (system_audit, etc.)
- Eval pro Helper: ist Ruflo-Version überlegen? Falls ja: Migration. Falls nicht: Dynastie-eigenes nutzen.
- Beispiel: `pattern-consolidator.sh` könnte APPLIED-LEARNING-Pflege ersetzen

## Risiko: HOCH (alle alpha/experimentell)

## Erfolgskriterium
- Jeder 4.x-Punkt hat eigenen Eval-Zyklus
- Stop-Criterion bei jedem: "Bringt es nachweislich Mehrwert über Phase 1-3 hinaus, oder fügt es nur Komplexität hinzu?"
- Default-Tendenz: SKIP wenn unklar

## Rollback
Jeder Punkt komplett isoliert. Plugin uninstall via npm. Guidance via env-flag.

---

# Übergreifende Prinzipien

## Sync-Pflicht
Jede Phase-Änderung gemäß §18:
- Routing-Table-Updates → CLAUDE.md
- §-Erweiterungen (z.B. §28.2 Codex-Verify) → INSTRUKTIONEN.md
- Skill-Refactor (z.B. Stream-Chain-Pipeline) → log.md + Skill-Versionierung
- System-Zustand-Change → SYSTEM.md + STATE.md Last-Audit-Block

## Audit-Cadence
- Phase 1: Wochen-Check (intelligence stats trend)
- Phase 2: 2-Wochen-Check (Codex-Match-Rate, Worker-False-Positives)
- Phase 3: Monats-Check (BatchScan-Konsistenz, Browser-Stability)
- Phase 4: Quarterly mit explizitem GO/NOGO

## Wenn etwas schiefgeht
- Doctor periodisch: `npx ruflo doctor --verbose`
- AttestationLog gibt cryptographische Memory-Op-History
- Trajectory-Replay erlaubt Reverse-Engineering von Score-Decisions
- Git ist immer noch die Audit-SSoT

## Was diese Roadmap NICHT macht
- Keine Migration zu Codex als Primary-Platform (Claude Code bleibt)
- Keine Cloud-Skalierung (Single-User stays)
- Keine Wiki/Vault-Auto-Generation aus AgentDB
- Keine Auto-Pflege von INSTRUKTIONEN.md §§ (Tier-3-Regeln bleiben manuell)
- Keine Aktivierung von Patterns/Plugins die Code-Domain sind

---

# Resumption-Hinweise für neue Session

## Session-Start-Checkliste
1. `Session starten` lesen → STATE.md + PORTFOLIO.md
2. Diese Datei (`00_Core/RUFLO-INTEGRATION-PLAN.md`) als Kontext laden
3. **Erster Schritt:** 1.1 — Override-Block für `Claude Stuff\CLAUDE.md` schreiben, Review, Commit
4. Danach 1.2 → 1.9 sequenziell

## Voraussetzungen prüfen
- `claude mcp list` zeigt `claude-flow` connected
- `npx ruflo@latest doctor --verbose` ohne kritische Fehler
- Git working-tree clean (kein Phase-Start mit dirty state)

## Wenn neue Session resumed
Pipeline-Item ergänzen in `00_Core/PIPELINE.md` mit Eintrag:
> "Ruflo-Integration Phase 1 (1.1-1.9) — Plan-Ref: `00_Core/RUFLO-INTEGRATION-PLAN.md`"

§18-Sync bei Phase-Start:
- log.md: "Ruflo-Integration Phase 1 gestartet, Plan-Ref ..."
- SYSTEM.md §Ruflo-Status (neuer Abschnitt): Aktivierte Features tracken
- STATE.md Last-Audit-Block aktualisieren

## Quellen
- USERGUIDE.md v3.5 lokal: `/c/Users/tobia/Downloads/USERGUIDE.md`
- Cache: `/tmp/ruflo-userguide.md`
- Repo: https://github.com/ruvnet/ruflo
- Diese Datei: einzige SSoT für Ruflo-Integration. Bei Plan-Änderungen hier updaten + Versions-Stempel oben.

---

**Plan-Status:** Draft v1.0 — pending User-OK für Phase-1-Start
**Nächster Schritt:** Override-Block in `Claude Stuff\CLAUDE.md` schreiben (1.1)
