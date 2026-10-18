# Abgleichliste Alt-Regelquellen — Radikalkur Phase 1

> Erzeugt 2026-10-18 per `02_Analysen/2026-10-17_inventar.py` (Neuerzeugung: `python 02_Analysen/2026-10-17_inventar.py .` im Repo-Root; Codex-Scope-Review 18.10. eingearbeitet). Schritt 1 = Inventar; Spalten **Verdikt / E-Bezug / Skill wörtlich?** füllt Schritt 2 (Verfahren E18).
> Verdikt-Werte: `übernehmen` · `streichen` · `Zustand→Broker` · `Urteil→Ledger` · `Methode→Skill` · `offen → Owner`.
> **Treffer** = regelartige Zeilen im eigenen Abschnittstext (Muster: ≥ ≤ < > · % pp Pt. Punkte Tage Mio · Schwelle Malus Bonus · DEFCON 1–4). Abschnitte mit vielen Treffern werden in Schritt 2 in Einzelregeln zerlegt — „Fehlende = 0“ gilt auf Abschnittsebene, nicht auf Regelebene.

## Suchraum

| Quelle | Einheit | Anzahl |
|---|---|---|
| `00_Core/INSTRUKTIONEN.md` | INSTRUKTIONEN.md — Überschriften H2–H4 | 83 |
| `00_Core/KONTEXT.md` | KONTEXT.md — Überschriften H2–H4 | 24 |
| `00_Core/CORE-MEMORY.md` | CORE-MEMORY.md (→ Archiv E14) — Überschriften H2–H4 | 52 |
| `00_Core/Faktortabelle.md` | Faktortabelle.md (→ Archiv E14) — Überschriften H2–H4 | 5 |
| `00_Core/PORTFOLIO.md` | PORTFOLIO.md (→ Archiv E14) — Überschriften H2–H4 | 4 |
| `01_Skills/dynastie-depot/SKILL.md` | dynastie-depot SKILL.md — Überschriften H2–H4 | 57 |
| `01_Skills/dynastie-depot/Beispiele.md` | dynastie-depot Beispiele.md (Kalibrierungsanker) — Überschriften H2–H4 | 29 |
| `01_Skills/dynastie-depot/sources.md` | dynastie-depot sources.md — Überschriften H2–H4 | 28 |
| `01_Skills/dynastie-depot/manifest.md` | dynastie-depot manifest.md — Überschriften H2–H4 | 8 |
| `01_Skills/quick-screener/SKILL.md` | quick-screener SKILL.md — Überschriften H2–H4 | 18 |
| `01_Skills/quick-screener/references/thresholds.md` | quick-screener references/thresholds.md — Überschriften H2–H4 | 36 |
| `01_Skills/insider-intelligence/SKILL.md` | insider-intelligence SKILL.md — Überschriften H2–H4 | 21 |
| `01_Skills/non-us-fundamentals/SKILL.md` | non-us-fundamentals SKILL.md — Überschriften H2–H4 | 16 |
| `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` | Vault Wissenschaftliche-Fundierung-DEFCON.md (Überschriften) — Überschriften H2–H4 | 19 |
| `03_Tools/depot-architecture-spec.md` | depot-architecture-spec.md (→ Archiv E14) — Überschriften H2–H4 | 50 |
| `01_Skills/dynastie-depot/config.yaml` | config.yaml — Blätter (Listen als `[*]` zusammengefasst) | 118 |
| `01_Skills/dynastie-depot/config.yaml` | config.yaml — Kommentarblöcke | 19 |
| `03_Tools/Rebalancing_Tool_v4.0.xlsx, 03_Tools/Satelliten_Monitor_v4.0.xlsx, 03_Tools/Watchlist_Ersatzbank_Monitor_v1.2.xlsx` | xlsx — Parameterblatt / bedingte Formate / Vergleichsformeln | 138 |
| `07_Obsidian Vault/**/*.md` | Vault — `operative_regel`-Frontmatter | 23 |
| `03_Tools/depot-architecture-spec.md` | depot-architecture-spec.md — Code-/YAML-Blöcke | 6 |
| `03_Tools/earnings_schedule_overrides.yaml` | earnings_schedule_overrides.yaml — Blätter (ohne Regex-Filter) | 12 |
| `03_Tools/earnings_schedule_overrides.yaml` | earnings_schedule_overrides.yaml — Kommentarblöcke (ohne Regex-Filter) | 8 |
| `32 .py-Dateien` | Code — Modul-Konstanten (GROSSBUCHSTABEN, Literalwert) aktiver Skills + 03_Tools | 91 |
| **Σ** | | **865** |

**Bewusst nicht im Suchraum (Owner 18.10.):** H1-Dateititel · `CLAUDE.md`, `APPLIED-LEARNING.md`, `STATE.md` (Ablaufregeln → E15/E16) · Memories (E16) · xlsx-Datenvalidierungen (Dropdowns) und US-Exposure-Blatt (reine Verweise) · Vault-Fließtext außer `operative_regel` + Wiss-Fundierung-Überschriften. Vollständige Gegenliste → letzter Abschnitt.

## INSTRUKTIONEN.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| I-001 | Z. 6–16 | ## Verweise | 0 | | | |
| I-002 | Z. 17–31 | ## §0. Code-Verhaltens-Regeln (Präambel) — Stub | 1 | | | |
| I-003 | Z. 32–48 | ## 1. Befehls-Übersicht | 0 | | | |
| I-004 | Z. 49–72 | ## 2. Analyse-Pipeline (Stufe 0 → Entscheidung) | 2 | | | |
| I-005 | Z. 73–89 | ## 3. STUFE 0 — Quick-Screener | 0 | | | |
| I-006 | Z. 75–89 | ### Drei harte Filter: | 3 | | | |
| I-007 | Z. 90–121 | ## 4. STUFE 2 — DEFCON-Scoring (100-Punkte-Matrix) | 0 | | | |
| I-008 | Z. 92–113 | ### Befunde-Router (Pflicht vor jedem Scoring-Start) | 0 | | | |
| I-009 | Z. 114–121 | ### Scoring-Skalen, DEFCON-Schwellen, FLAGs | 2 | | | |
| I-010 | Z. 122–135 | ## 5. Sentiment-Scoring (v3.7-Kalibrierung) | 3 | | | |
| I-011 | Z. 136–147 | ## 6. Insider-Scoring — Pflichtregeln | 2 | | | |
| I-012 | Z. 148–161 | ## 7. Kalibrierungsanker (vor jeder Analyse pflichtlesen!) | 4 | | | |
| I-013 | Z. 162–169 | ## 8. Datenquellen-Logik | 0 | | | |
| I-014 | Z. 170–190 | ## 9. !Rebalancing — Workflow | 2 | | | |
| I-015 | Z. 191–219 | ## 10. !QuickCheck — Workflow | 7 | | | |
| I-016 | Z. 220–232 | ## 11. CapEx-FCF-Analyse — 6 Excel-Sheets | 1 | | | |
| I-017 | Z. 233–242 | ## 12. config-Pflege-Pflicht | 0 | | | |
| I-018 | Z. 243–250 | ## 13. Verhaltensregeln | 1 | | | |
| I-019 | Z. 251–260 | ## 14. Non-US Scoring Addendum (ASML / RMS / SU / KYCCF) | 0 | | | |
| I-020 | Z. 261–268 | ## 15. Tariff Exposure | 1 | | | |
| I-021 | Z. 269–276 | ## 16. Non-US API Sanity Check | 1 | | | |
| I-022 | Z. 277–329 | ## 17. Skill-Hierarchie & Aktivierungslogik (v2.1 — 25.04.2026) | 0 | | | |
| I-023 | Z. 283–299 | ### Wann wird welcher Skill eigenständig aktiviert? | 0 | | | |
| I-024 | Z. 300–311 | ### Warum kein manuelles Skill-Chaining innerhalb !Analysiere? | 0 | | | |
| I-025 | Z. 312–329 | ### 17.1 Memory-Guard-Rail — Routing- und Live-State-Vorrang (PF-1 Option C) | 0 | | | |
| I-026 | Z. 330–447 | ## 18. Sync-Pflicht — Trigger-basiertes File-Set-Mapping (v2.4, 2026-05-11) | 0 | | | |
| I-027 | Z. 334–365 | ### §18.0 Auto-Invoke-Disziplin `paragraph-18-sync` (NEU 2026-05-23 spätabends, v2.5 → v2.5.1 2026-05-2… | 0 | | | |
| I-028 | Z. 366–382 | ### 18.1 Event-Typ-Mapping | 1 | | | |
| I-029 | Z. 383–392 | ### 18.2 Multi-Event-Union-Regel (bindender §18-Vertrags-Teil) | 0 | | | |
| I-030 | Z. 393–398 | ### 18.3 Commit-Granularität | 0 | | | |
| I-031 | Z. 399–402 | ### 18.4 Stand-Footer-Konvention (seit 2026-04-26) | 0 | | | |
| I-032 | Z. 403–406 | ### 18.5 Provenance-Gate für Score-Appends (seit 2026-04-28, v3.7.4) | 0 | | | |
| I-033 | Z. 407–419 | ### 18.6 Log-Rollover-Convention (seit 2026-05-10) | 2 | | | |
| I-034 | Z. 420–447 | ### 18.7 xlsx Post-Write Smoke-Test Stufe 1 (seit 2026-05-11, v2.4) | 2 | | | |
| I-035 | Z. 448–503 | ## 19. Daten-Update-Klassen (wissenschaftlich fundiert) | 4 | | | |
| I-036 | Z. 459–503 | ### 19.1 Earnings-Call-Wait-Discipline (NEU 2026-04-28 spätabends, post V Q2 Reinfall) | 6 | | | |
| I-037 | Z. 504–514 | ## 20. Ersatzbank-Aktivierungsprotokoll | 3 | | | |
| I-038 | Z. 515–532 | ## 21. Non-US Scoring Kurzreferenz | 2 | | | |
| I-039 | Z. 533–560 | ## 22. Sparplan-Formel (3-Tier, aktuell 2026-06-07 — Umstrukturierung Phase A) | 0 | | | |
| I-040 | Z. 561–568 | ## 23. Tariff Exposure Scoring | 2 | | | |
| I-041 | Z. 569–584 | ## 25. Session-Closure | 0 | | | |
| I-042 | Z. 573–584 | ### 25.5 Session-Closure-Workflow (21.05.2026, session-closure v0.2.0) | 0 | | | |
| I-043 | Z. 585–611 | ## 26. Archiv-Sync (Backtest-Ready-Pipeline) | 0 | | | |
| I-044 | Z. 591–597 | ### Workflow (4 Schritte) | 2 | | | |
| I-045 | Z. 598–605 | ### Fehler-Klassen | 2 | | | |
| I-046 | Z. 606–611 | ### Nicht archiviert | 0 | | | |
| I-047 | Z. 612–763 | ## 27. Scoring-Hygiene & Daten-Integrität | 0 | | | |
| I-048 | Z. 616–628 | ### 27.1 Double-Counting-Vermeidung bei Scoring-Erweiterungen | 2 | | | |
| I-049 | Z. 629–641 | ### 27.2 Bonus-Cap-Check bei neuen Bonus-Regeln | 5 | | | |
| I-050 | Z. 642–666 | ### 27.3 Primärquellen vs. Navigations-/Projektions-Layer | 0 | | | |
| I-051 | Z. 667–689 | ### 27.4 Multi-Source-Drift-Check vor "fertig"-Meldung | 2 | | | |
| I-052 | Z. 690–714 | ### 27.5 Migration-Regression-Guard (22.04.2026, system-audit v1.0) | 0 | | | |
| I-053 | Z. 715–733 | ### 27.6 Earnings-Calendar-Drift-Check (Stufe 2 — earnings_calendar.py v2.0, 06.05.2026) | 0 | | | |
| I-054 | Z. 734–745 | ### 27.7 Carryover-Discipline-Asymmetrie (NEU 09.05.2026, PIPELINE #23 Closure) | 1 | | | |
| I-055 | Z. 746–763 | ### 27.8 DCF-Malus Bull-Source-Pflicht (NEU 09.05.2026, PIPELINE #34 Closure) | 3 | | | |
| I-056 | Z. 764–840 | ## 28. Scoring-Version-Migration-Workflow | 1 | | | |
| I-057 | Z. 770–806 | ### 28.1 Pflicht-Checklist | 3 | | | |
| I-058 | Z. 807–825 | ### 28.2 Algebra-≠-Forward-Diskrepanz (gestuft) | 3 | | | |
| I-059 | Z. 826–840 | ### 28.3 Nicht-Migration-Trigger | 0 | | | |
| I-060 | Z. 841–881 | ## 29. Retrospective-Analyse-Gate | 0 | | | |
| I-061 | Z. 849–851 | ### 29.1 Methoden-Gate — Overfitting (Bailey et al. 2015) | 1 | | | |
| I-062 | Z. 852–854 | ### 29.2 External-Benchmark-Gate (Aghassi et al. 2023) | 0 | | | |
| I-063 | Z. 855–857 | ### 29.3 Temporal-Konsistenz (Flint & Vermaak 2021) | 0 | | | |
| I-064 | Z. 858–860 | ### 29.4 Neue-Parameter-Gate — Harvey/Liu/Zhu-Hurdle | 1 | | | |
| I-065 | Z. 861–863 | ### 29.5 Seven-Sins-Pre-Flight-Gate (Palomar 2025 Ch 8.2) | 0 | | | |
| I-066 | Z. 864–866 | ### 29.6 Portfolio-Return-Metrik-Layer (Palomar 2025 Ch 6) | 1 | | | |
| I-067 | Z. 867–869 | ### 29.7 M&P-Discount-Gate — Post-Publication-Decay (McLean & Pontiff 2016, B25) | 0 | | | |
| I-068 | Z. 870–872 | ### 29.8 Aktivierungs-Reihenfolge bei Review 2028 | 0 | | | |
| I-069 | Z. 873–881 | ### 29.9 Rückverweise | 0 | | | |
| I-070 | Z. 882–925 | ## 30. Live-Monitoring & Cadence | 0 | | | |
| I-071 | Z. 888–895 | ### 30.1 Trigger-Definition | 0 | | | |
| I-072 | Z. 896–902 | ### 30.2 Aktuelle Scope (Stand 19.04.2026) | 1 | | | |
| I-073 | Z. 903–910 | ### 30.3 Monthly-Refresh-Workflow | 0 | | | |
| I-074 | Z. 911–917 | ### 30.4 Constraints (Applied-Learning-Wächter) | 0 | | | |
| I-075 | Z. 918–925 | ### 30.5 Wissenschaftliche Fundierung | 0 | | | |
| I-076 | Z. 926–1000 | ## 33. Skill-Self-Audit-Gate (Anti-Creep für KG/RAG/Agentic-Architekturen) | 0 | | | |
| I-077 | Z. 946–953 | ### 33.1 Gate 1 — Sinnhaftigkeits-Check | 0 | | | |
| I-078 | Z. 954–959 | ### 33.2 Gate 2 — Operationalisierungs-Check | 0 | | | |
| I-079 | Z. 960–965 | ### 33.3 Gate 3 — Anti-Over-Engineering-Check | 0 | | | |
| I-080 | Z. 966–973 | ### 33.4 Decision-Output | 0 | | | |
| I-081 | Z. 974–979 | ### 33.5 Dokumentation | 0 | | | |
| I-082 | Z. 980–989 | ### 33.6 Beispiel-Anwendung (Phase-1b 2026-04-20) | 0 | | | |
| I-083 | Z. 990–1000 | ### 33.7 Rückverweise | 0 | | | |

## KONTEXT.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| K-001 | Z. 6–13 | ## Verweise | 0 | | | |
| K-002 | Z. 14–27 | ## 1. Identität & Philosophie | 0 | | | |
| K-003 | Z. 28–37 | ## 2. Die drei Triebwerke | 1 | | | |
| K-004 | Z. 38–53 | ## 3. Allokation & Struktur | 5 | | | |
| K-005 | Z. 54–68 | ## 4. ETF-Core (60% — ING + Scalable) | 2 | | | |
| K-006 | Z. 69–94 | ## 4b. Phase B ab 2027 — Altersvorsorgedepot (AVD) & Broker-Konsolidierung | 7 | | | |
| K-007 | Z. 95–124 | ## 5. Satelliten — Die Startelf (Scalable Capital) | 1 | | | |
| K-008 | Z. 125–149 | ## 6. Ersatzbank & Watchlist | 5 | | | |
| K-009 | Z. 150–166 | ## 7. Steuer-Architektur | 1 | | | |
| K-010 | Z. 167–176 | ## 8. Psychologie & Krisenprotokoll | 0 | | | |
| K-011 | Z. 177–185 | ## 9. Dynastie-Protokoll (Bus-Faktor) | 0 | | | |
| K-012 | Z. 186–201 | ## 10. Anstehende Termine (Juni–Sept 2026) | 2 | | | |
| K-013 | Z. 202–259 | ## 11. Datenhaltung — 4-Layer-Architektur (ab 2026-04-17) | 0 | | | |
| K-014 | Z. 206–210 | ### State-Layer — Aktueller Zustand (überschrieben) | 0 | | | |
| K-015 | Z. 211–216 | ### Narrative-Layer — Menschenlesbare Historie (evolvierend) | 0 | | | |
| K-016 | Z. 217–222 | ### History-Layer — Maschinenlesbare Historie (append-only, unveränderlich) | 0 | | | |
| K-017 | Z. 223–231 | ### Projection-Layer — Session-Entry-Snapshot (abgeleitet) | 1 | | | |
| K-018 | Z. 232–244 | ### Schreib-Disziplin (§18 Sync-Pflicht) | 0 | | | |
| K-019 | Z. 245–259 | ### Wann welcher Layer gelesen wird | 1 | | | |
| K-020 | Z. 260–300 | ## 12. Watchlist-Eintritts-Disziplin (ab 2026-05-14) | 0 | | | |
| K-021 | Z. 264–274 | ### Rule (a) — Schätz-Score-Verbot | 0 | | | |
| K-022 | Z. 275–285 | ### Rule (b) — Eintrittsschwelle | 5 | | | |
| K-023 | Z. 286–291 | ### Anti-Patterns dokumentiert | 0 | | | |
| K-024 | Z. 292–300 | ### Cross-References | 0 | | | |

## CORE-MEMORY.md (→ Archiv E14) — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| CM-001 | Z. 4–18 | ## Verweise | 0 | | | |
| CM-002 | Z. 19–55 | ## 2. Strategische Entscheidungen (dauerhaft bindend) | 0 | | | |
| CM-003 | Z. 21–28 | ### Umstrukturierung-2027 Phase A — Owner-Override (05.06.2026, ERSETZT die drei nachstehenden „bindend… | 0 | | | |
| CM-004 | Z. 29–33 | ### Allokations-Entscheidung (März 2026) — ⚠️ ÜBERSCHRIEBEN 05.06.2026 (siehe oben) | 0 | | | |
| CM-005 | Z. 34–38 | ### Gewichtungs-Entscheidung Satelliten — ⚠️ ÜBERSCHRIEBEN 05.06.2026 (siehe Umstrukturierung-Override … | 2 | | | |
| CM-006 | Z. 39–43 | ### Slot-Anzahl — ⚠️ ÜBERSCHRIEBEN 05.06.2026 (siehe Umstrukturierung-Override oben) | 0 | | | |
| CM-007 | Z. 44–48 | ### CRWD und PLTR Entfernung | 0 | | | |
| CM-008 | Z. 49–55 | ### GOOGL struktureller Ausschluss | 1 | | | |
| CM-009 | Z. 56–61 | ## 3. Aktive Positions-Entscheidungen (archiviert 2026-05-23) | 0 | | | |
| CM-010 | Z. 62–73 | ## 4. Score-Register | 0 | | | |
| CM-011 | Z. 74–223 | ## 5. Scoring-Lektionen (gelernte Regeln) | 0 | | | |
| CM-012 | Z. 76–81 | ### Goodwill-Malus | 2 | | | |
| CM-013 | Z. 82–86 | ### ROIC < WACC = harter Malus | 1 | | | |
| CM-014 | Z. 87–91 | ### FLAG ist absolut | 2 | | | |
| CM-015 | Z. 92–96 | ### Cashless Exercise ≠ Insider-Selling | 1 | | | |
| CM-016 | Z. 97–101 | ### Datenlücken → konservativ scoren | 0 | | | |
| CM-017 | Z. 102–106 | ### TTM-Verzerrung bei Kurscrash | 2 | | | |
| CM-018 | Z. 107–113 | ### Pre-Processing Layer (v3.3 — 06.04.2026) | 2 | | | |
| CM-019 | Z. 114–119 | ### API-Sanity-Check-Lücke IFRS (v3.3 — 06.04.2026) | 2 | | | |
| CM-020 | Z. 120–130 | ### SEC EDGAR 10b5-1 Footnote-Luecke (v1.0 Insider-Modul) | 0 | | | |
| CM-021 | Z. 131–139 | ### Non-US Kalibrierungsanker: ASML (06.04.2026) | 0 | | | |
| CM-022 | Z. 140–144 | ### Tariff Exposure als Scoring-Malus (v3.1) | 1 | | | |
| CM-023 | Z. 145–151 | ### V-Rescoring (18.04.2026) — Sub-Score-Strenge bei Validity-Mismatches | 3 | | | |
| CM-024 | Z. 152–157 | ### Schema-Trigger ≠ SKILL-Regel-Semantik (18.04.2026, TMO-Präzedenz) | 1 | | | |
| CM-025 | Z. 158–168 | ### 4-Paper-Triage für §29 Retrospective-Gate (v3.7 — 19.04.2026) | 1 | | | |
| CM-026 | Z. 169–181 | ### R5 Portfolio-Return-Persistenz aktiviert (v3.7.2 — 19.04.2026) | 0 | | | |
| CM-027 | Z. 182–194 | ### R1 §30 Live-Monitoring aktiviert (v3.7.2 — 19.04.2026) | 1 | | | |
| CM-028 | Z. 195–223 | ### Phase-2-System-Konsequenzen der wissenschaftlichen Fundierung (20.04.2026) | 0 | | | |
| CM-029 | Z. 224–234 | ## 6. System-Upgrades & Versionsverlauf | 0 | | | |
| CM-030 | Z. 235–244 | ## 7. Steuer-Erinnerungen | 0 | | | |
| CM-031 | Z. 245–255 | ## 8. Nächste offene Entscheidungen | 2 | | | |
| CM-032 | Z. 256–278 | ## 10. API-Audit-Log (Quarterly Sanity Check) | 2 | | | |
| CM-033 | Z. 270–278 | ### IFRS 16 vs. ASC 842 — Strukturelle OCF-Differenz (Non-US Pflicht-Wissen) | 2 | | | |
| CM-034 | Z. 279–297 | ## 11. Backtest-Ready Infrastructure (aktiviert 2026-04-17) | 1 | | | |
| CM-035 | Z. 298–405 | ## 12. Per-Ticker-Chronik | 0 | | | |
| CM-036 | Z. 302–310 | ### 12.1 AVGO | 5 | | | |
| CM-037 | Z. 311–316 | ### 12.2 APH | 3 | | | |
| CM-038 | Z. 317–322 | ### 12.3 ASML | 3 | | | |
| CM-039 | Z. 323–333 | ### 12.4 BRK.B | 6 | | | |
| CM-040 | Z. 334–338 | ### 12.5 COST | 2 | | | |
| CM-041 | Z. 339–346 | ### 12.6 MSFT | 5 | | | |
| CM-042 | Z. 347–351 | ### 12.7 RMS | 2 | | | |
| CM-043 | Z. 352–355 | ### 12.8 SU | 1 | | | |
| CM-044 | Z. 356–361 | ### 12.9 TMO | 3 | | | |
| CM-045 | Z. 362–369 | ### 12.10 V | 5 | | | |
| CM-046 | Z. 370–375 | ### 12.11 VEEV | 1 | | | |
| CM-047 | Z. 376–389 | ### 12.12 AMZN | 5 | | | |
| CM-048 | Z. 390–392 | ### 12.13 NOW | 0 | | | |
| CM-049 | Z. 393–396 | ### 12.14 KYCCF | 1 | | | |
| CM-050 | Z. 397–399 | ### 12.15 ZETA | 0 | | | |
| CM-051 | Z. 400–405 | ### 12.16 GOOGL | 0 | | | |
| CM-052 | Z. 406–468 | ## 13. System-Lifecycle-History | 17 | | | |

## Faktortabelle.md (→ Archiv E14) — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| F-001 | Z. 14–22 | ## Verweise | 0 | | | |
| F-002 | Z. 23–70 | ## Haupttabelle | 17 | | | |
| F-003 | Z. 71–86 | ## Update-Kalender | 1 | | | |
| F-004 | Z. 87–92 | ## Ersatzbank | 0 | | | |
| F-005 | Z. 93–101 | ## Vault-Verknüpfungen | 0 | | | |

## PORTFOLIO.md (→ Archiv E14) — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| P-001 | Z. 7–15 | ## Verweise | 0 | | | |
| P-002 | Z. 16–43 | ## Portfolio-State (13 Satelliten — 3-Tier Conviction) | 5 | | | |
| P-003 | Z. 44–58 | ## Aktive Watches | 9 | | | |
| P-004 | Z. 59–79 | ## Nächste kritische Trigger (30 Tage) | 3 | | | |

## dynastie-depot SKILL.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| S-001 | Z. 19–32 | ## Übersicht | 0 | | | |
| S-002 | Z. 33–45 | ## Dateien in diesem Skill | 0 | | | |
| S-003 | Z. 46–330 | ## WORKFLOW 1: \!Analysiere \[TICKER\] | 0 | | | |
| S-004 | Z. 50–73 | ### Schritt 0: Snapshot-First + Earnings-Call-Wait-Check (v3.7.5, eingeführt 28.04.2026 spätabends post… | 4 | | | |
| S-005 | Z. 74–164 | ### Schritt 1: Daten sammeln | 7 | | | |
| S-006 | Z. 165–173 | ### Schritt 2: Qualitätscheck ausgeben | 0 | | | |
| S-007 | Z. 174–195 | ### Schritt 2.5: Befunde-Check (Phase-2 2026-04-20, erweitert 2026-04-26 um B25-B28) | 1 | | | |
| S-008 | Z. 196–265 | ### Schritt 3: 100-Punkte-Matrix scoren | 2 | | | |
| S-009 | Z. 266–281 | ### Schritt 6b: FLAG-Resolution-Check (Post-Output, vor Archiv) | 3 | | | |
| S-010 | Z. 282–296 | ### Schritt 6c: Score-Konsistenz-Pre-Flight (v3.7.4, eingeführt 28.04.2026) | 2 | | | |
| S-011 | Z. 297–330 | ### Schritt 7: Archiv-Write (via `backtest-ready-forward-verify`-Skill) | 2 | | | |
| S-012 | Z. 331–712 | ## SCORING-SKALEN (100-Punkte-Matrix) | 0 | | | |
| S-013 | Z. 335–545 | ### Fundamentals (50 Punkte) | 65 | | | |
| S-014 | Z. 518–545 | #### Screener-Exceptions (v3.7) | 10 | | | |
| S-015 | Z. 546–578 | ### Moat (20 Punkte) | 0 | | | |
| S-016 | Z. 557–569 | #### GM-Trend 3 Jahre (Moat-Qualitäts-Check) | 4 | | | |
| S-017 | Z. 570–578 | #### Pricing Power Confirmation (Bonus, optional) | 1 | | | |
| S-018 | Z. 579–648 | ### Technicals (10 Punkte) | 1 | | | |
| S-019 | Z. 587–648 | #### Technicals-Präzisierungen | 17 | | | |
| S-020 | Z. 649–660 | ### Insider (10 Punkte) | 4 | | | |
| S-021 | Z. 661–712 | ### Sentiment (10 Punkte) — v3.7-Kalibrierung (B11) | 14 | | | |
| S-022 | Z. 687–712 | #### Sentiment-Präzisierungen | 5 | | | |
| S-023 | Z. 713–734 | ## DEFCON-SCHWELLENWERTE | 0 | | | |
| S-024 | Z. 715–723 | ### Neueinstieg (neue Position / Slot-Besetzung) | 2 | | | |
| S-025 | Z. 724–734 | ### Bestandsüberwachung (Depot-Positionen) | 3 | | | |
| S-026 | Z. 735–776 | ## FLAG-REGELN (score-unabhängig) | 3 | | | |
| S-027 | Z. 754–776 | #### FLAG Typ 4: Tariff Exposure 🔴 (eingeführt v3.2 — 03.04.2026) | 4 | | | |
| S-028 | Z. 777–787 | ## VALUE LEGENDS (Abschnitt 5 der Analyse) | 2 | | | |
| S-029 | Z. 788–800 | ## WORKFLOW 2: \!CAPEX-FCF-ANALYSIS \[TICKER\] \[NAME\] | 1 | | | |
| S-030 | Z. 801–870 | ## WORKFLOW 4: \!QuickCheck \[TICKER \| ALL\] | 0 | | | |
| S-031 | Z. 807–812 | ### Trigger-Logik | 0 | | | |
| S-032 | Z. 813–818 | ### Risiko-Reihenfolge bei \!QuickCheck ALL | 0 | | | |
| S-033 | Z. 819–830 | ### 7 Checkpunkte (fest, immer gleich) | 3 | | | |
| S-034 | Z. 831–852 | ### Output-Format | 0 | | | |
| S-035 | Z. 853–861 | ### Deep-Dive-Trigger (automatisch → \!Analysiere) | 1 | | | |
| S-036 | Z. 862–870 | ### Rhythmus | 1 | | | |
| S-037 | Z. 871–891 | ## WORKFLOW 3: \!Rebalancing | 6 | | | |
| S-038 | Z. 892–906 | ## PORTFOLIO-KONTEXT (Kurzreferenz) | 2 | | | |
| S-039 | Z. 907–980 | ## 🧹 PRE-PROCESSING & DATA CLEANING (API-Filter) | 0 | | | |
| S-040 | Z. 911–922 | ### Regel 1 — SBC-Check (Stock-Based Compensation) | 3 | | | |
| S-041 | Z. 923–935 | ### Regel 2 — Hyperscaler CapEx-Korrektur (Finance Leases) | 1 | | | |
| S-042 | Z. 936–945 | ### Regel 3 — CapEx-Qualität (Growth vs. Maintenance) | 1 | | | |
| S-043 | Z. 946–958 | ### Regel 4 — M&A Amortization Add-back (ROIC-Proxy) | 3 | | | |
| S-044 | Z. 959–980 | ### Regel 5 — Roh→Metrik-Triage (Tool-Output-Disziplin) | 2 | | | |
| S-045 | Z. 981–1041 | ## 🔍 QUARTERLY API SANITY CHECK | 0 | | | |
| S-046 | Z. 987–995 | ### Rotationsplan (fix, nicht zufällig) | 4 | | | |
| S-047 | Z. 996–1005 | ### Methodik — US-Titel (Toleranz ±0,5%) | 0 | | | |
| S-048 | Z. 1006–1031 | ### Methodik — Non-US-Titel (Toleranz ±1,5%, IFRS) | 1 | | | |
| S-049 | Z. 1032–1041 | ### FLAG-Protokoll bei Drift | 0 | | | |
| S-050 | Z. 1042–1098 | ## 🌐 API-ROUTING-REGEL | 0 | | | |
| S-051 | Z. 1044–1057 | ### Routing-Logik | 0 | | | |
| S-052 | Z. 1058–1068 | ### Feldnamen yfinance (US + Non-US identisch) | 0 | | | |
| S-053 | Z. 1069–1098 | ### SEC EDGAR API — Insider-Scoring (US) | 1 | | | |
| S-054 | Z. 1099–1110 | ## VERHALTENSREGELN | 1 | | | |
| S-055 | Z. 1111–1142 | ## Methodology-Switch-Disziplin (M1 — Spec 2026-05-11-codebase-defect-patterns §3) | 1 | | | |
| S-056 | Z. 1116–1131 | ### Decision-Tree | 1 | | | |
| S-057 | Z. 1132–1142 | ### Präzedenz-Fälle (Anti-Patterns) | 0 | | | |

## dynastie-depot Beispiele.md (Kalibrierungsanker) — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| B-001 | Z. 29–44 | ## 📌 Verwendung dieser Datei | 1 | | | |
| B-002 | Z. 45–63 | ## 🧭 Mechanismen-Index | 0 | | | |
| B-003 | Z. 64–133 | ## 🥇 AVGO – Broadcom Inc. \| Score: 84/100 \| 🟢 DEFCON 4 | 0 | | | |
| B-004 | Z. 71–81 | ### Scoring-Status (v3.7) | 1 | | | |
| B-005 | Z. 82–89 | ### v3.7-Mechanismen an AVGO (qualitativ) | 4 | | | |
| B-006 | Z. 90–96 | ### FLAG-Status (17.04.2026) | 4 | | | |
| B-007 | Z. 97–102 | ### 🚨 Risk Map | 1 | | | |
| B-008 | Z. 103–108 | ### 🐂 Bull / 🐻 Bear | 1 | | | |
| B-009 | Z. 109–114 | ### 🎯 Value Legends (qualitativ, nicht punktscored) | 0 | | | |
| B-010 | Z. 115–120 | ### Depot-Einordnung | 0 | | | |
| B-011 | Z. 121–133 | ### 📚 Scoring-Lektion (Anker-Rolle) | 3 | | | |
| B-012 | Z. 134–211 | ## 🔬 ASML – ASML Holding N.V. \| Score: 68/100 \| 🟡 DEFCON 3 | 0 | | | |
| B-013 | Z. 139–147 | ### Scoring-Status (v3.7) | 2 | | | |
| B-014 | Z. 148–157 | ### Subscores (v3.7) | 4 | | | |
| B-015 | Z. 158–166 | ### v3.7-Mechanismen an ASML (qualitativ) | 6 | | | |
| B-016 | Z. 167–173 | ### FLAG-Status (17.04.2026) | 3 | | | |
| B-017 | Z. 174–179 | ### 🚨 Risk Map | 2 | | | |
| B-018 | Z. 180–185 | ### 🐂 Bull / 🐻 Bear | 2 | | | |
| B-019 | Z. 186–191 | ### 🎯 Value Legends (qualitativ, nicht punktscored) | 1 | | | |
| B-020 | Z. 192–197 | ### Depot-Einordnung | 1 | | | |
| B-021 | Z. 198–211 | ### 📚 Scoring-Lektion (Anker-Rolle) | 5 | | | |
| B-022 | Z. 212–231 | ## 🥈 MKL – Markel Group Inc. \| Score: 82/100 \| 🟢 DEFCON 4 | 5 | | | |
| B-023 | Z. 232–251 | ## 🥉 SNPS – Synopsys Inc. \| Score: 76/100 \| 🟡 DEFCON 3 | 5 | | | |
| B-024 | Z. 252–271 | ## 🔵 SPGI – S&P Global Inc. \| Score: 74/100 \| 🟡 DEFCON 3 | 6 | | | |
| B-025 | Z. 272–291 | ## 🔬 TMO – Thermo Fisher Scientific \| Score: 62/100 \| 🟠 DEFCON 2 | 9 | | | |
| B-026 | Z. 292–315 | ## 🌍 EXPN – Experian PLC \| Score: 61/100 \| 🟡 DEFCON 3 | 5 | | | |
| B-027 | Z. 316–343 | ## 💱 FICO - Fair Isaac Corp. \| Score 67/100 \| 🟡 DEFCON 3 | 9 | | | |
| B-028 | Z. 344–365 | ## 📊 Score-Kalibrierung auf einen Blick | 3 | | | |
| B-029 | Z. 366–384 | ## 🔄 v3.7-Voll-Anker-Status | 0 | | | |

## dynastie-depot sources.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| SR-001 | Z. 11–20 | ## ⚠️ Architektur-Änderungen v3.0 (gegenüber v2.7) | 0 | | | |
| SR-002 | Z. 21–29 | ## ⚠️ FinnHub — Read-Only Real-Time-Layer (KEINE Scoring-Quelle) | 0 | | | |
| SR-003 | Z. 30–53 | ## 🎯 Primärquellen (MCP / SQL / Scripts — Top-Tier) | 0 | | | |
| SR-004 | Z. 32–39 | ### US-Ticker (NYSE/NASDAQ) | 0 | | | |
| SR-005 | Z. 40–53 | ### Non-US-Ticker (ASML, RMS, SU; KYCCF JP) | 0 | | | |
| SR-006 | Z. 54–68 | ## 🔬 Web-Sekundärquellen (Fallback/Verifikation) | 0 | | | |
| SR-007 | Z. 69–90 | ## 🚀 GuruFocus Pflicht-Batch (bei `!Analysiere` Start) | 0 | | | |
| SR-008 | Z. 91–144 | ## 🦅 Insider & Institutional | 1 | | | |
| SR-009 | Z. 102–112 | ### 🚨 10b5-1 FLAG-Prüflogik | 1 | | | |
| SR-010 | Z. 113–127 | ### 🔍 Form 4 Transaktions-Code Cheatsheet (SEC EDGAR) | 1 | | | |
| SR-011 | Z. 128–144 | ### 🔍 OpenInsider Spalten-Cheatsheet (Triage-Fallback) | 2 | | | |
| SR-012 | Z. 145–154 | ## 🏰 Moat & Qualität | 0 | | | |
| SR-013 | Z. 155–166 | ## 📋 Primärquellen (Pflicht für CapEx-FCF) | 0 | | | |
| SR-014 | Z. 167–196 | ## ⚡ Quick-Lookup nach Analyse-Schritt | 0 | | | |
| SR-015 | Z. 197–257 | ## ⚠️ Scoring-Protokoll: Kritische Datenanpassungen | 0 | | | |
| SR-016 | Z. 199–205 | #### 1. TTM-Verzerrung bei Kurscrash (>30% vom ATH) | 1 | | | |
| SR-017 | Z. 206–212 | #### 2. GAAP vs. Non-GAAP Protokoll | 0 | | | |
| SR-018 | Z. 213–227 | #### 3. Non-US Ticker Quellenregel | 1 | | | |
| SR-019 | Z. 228–238 | #### 4. Insider Ownership Bewertungsskala | 4 | | | |
| SR-020 | Z. 239–246 | #### 5. Fwd PE Quellen-Hierarchie bei Widerspruch | 1 | | | |
| SR-021 | Z. 247–257 | #### 6. Quarterly vs. Annual Daten | 0 | | | |
| SR-022 | Z. 258–286 | ## 🚫 §7 Methodology-Drift Hard-Ausschluss-Register | 0 | | | |
| SR-023 | Z. 262–267 | ### Aktuelles Register | 1 | | | |
| SR-024 | Z. 268–271 | ### Hintergrund | 1 | | | |
| SR-025 | Z. 272–278 | ### Operative Regel | 1 | | | |
| SR-026 | Z. 279–286 | ### Anti-Pattern (was NICHT passieren darf) | 0 | | | |
| SR-027 | Z. 287–294 | ## 🔑 Goldene Regel (gilt immer, überall) | 0 | | | |
| SR-028 | Z. 295–340 | ## 🔍 URL-Muster für Ticker-spezifische Abfragen | 0 | | | |

## dynastie-depot manifest.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| M-001 | Z. 13–29 | ## Kapitel 1: Der Maschinenraum (Setup & Cashflow) | 1 | | | |
| M-002 | Z. 30–49 | ## Kapitel 2: Das Fundament – ETF-Core (60% / ~616€) + Gold (5% / ~51€) | 3 | | | |
| M-003 | Z. 50–72 | ## Kapitel 3: Die Startelf – Satelliten (35% / ~364€ SOLL, 13 Positionen) | 0 | | | |
| M-004 | Z. 73–98 | ## Kapitel 4: Ersatzbank & 1:1-Auswechsel-Matrix | 2 | | | |
| M-005 | Z. 99–108 | ## Kapitel 5: Steuer-Architektur (Freistellungsauftrag) | 0 | | | |
| M-006 | Z. 109–137 | ## Kapitel 6: End-Game-Mechanik (Steuern & Entnahme) | 2 | | | |
| M-007 | Z. 138–146 | ## Kapitel 7: Psychologie & Geopolitik | 0 | | | |
| M-008 | Z. 147–154 | ## Kapitel 8: Dynastie-Protokoll (Notfall & Vermächtnis) | 0 | | | |

## quick-screener SKILL.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| QS-001 | Z. 29–45 | ## Pipeline-Einordnung | 2 | | | |
| QS-002 | Z. 46–55 | ## Dateien in diesem Skill | 1 | | | |
| QS-003 | Z. 56–192 | ## WORKFLOW 1: Einzel-Screening | 0 | | | |
| QS-004 | Z. 61–81 | ### Schritt 1: Daten beschaffen | 0 | | | |
| QS-005 | Z. 82–131 | ### Schritt 2: Datenverifikation | 6 | | | |
| QS-006 | Z. 132–136 | ### Schritt 3: Schwellenwerte anwenden | 1 | | | |
| QS-007 | Z. 137–148 | ### Schritt 4: Gesamtampel bestimmen | 1 | | | |
| QS-008 | Z. 149–177 | ### Schritt 5: Ergebnis ausgeben | 5 | | | |
| QS-009 | Z. 178–192 | ### Schritt 6: Config aktualisieren | 0 | | | |
| QS-010 | Z. 193–283 | ## WORKFLOW 2: Batch-Screening (Watchlist-Durchlauf) | 0 | | | |
| QS-011 | Z. 199–237 | ### Modus A: CSV-Import (bevorzugt fuer Batch) | 1 | | | |
| QS-012 | Z. 238–252 | ### Modus B: Web-Search (fuer Einzel-Screenings oder wenn keine CSV vorhanden) | 1 | | | |
| QS-013 | Z. 253–283 | ### Batch-Ergebnis-Format | 3 | | | |
| QS-014 | Z. 284–311 | ## Sonderregeln | 0 | | | |
| QS-015 | Z. 286–292 | ### Morningstar-Rating verfuegbar | 0 | | | |
| QS-016 | Z. 293–304 | ### Screener-Exceptions (Float-basierte Modelle) | 2 | | | |
| QS-017 | Z. 305–311 | ### FLAG-Ticker | 0 | | | |
| QS-018 | Z. 312–325 | ## Verhaltensregeln | 1 | | | |

## quick-screener references/thresholds.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| QT-001 | Z. 1 (Klartext) | Quick-Screener Schwellenwerte (v1.1 – 03.04.2026) | 1 | | | |
| QT-002 | Z. 2 (Klartext) | Dieses Dokument definiert alle Schwellenwerte zentral. Änderungen hier wirken | 1 | | | |
| QT-003 | Z. 9 (Klartext) | Schwelle | 1 | | | |
| QT-004 | Z. 12 (Klartext) | <= 35 | 1 | | | |
| QT-005 | Z. 18 (Klartext) | > 45 oder negativ/n.a. | 1 | | | |
| QT-006 | Z. 25 (Klartext) | Wenn Kurs >30% unter ATH: TTM-P/FCF ist systematisch verzerrt (künstlich | 1 | | | |
| QT-007 | Z. 32 (Klartext) | Schwelle | 1 | | | |
| QT-008 | Z. 35 (Klartext) | \>= 15% | 1 | | | |
| QT-009 | Z. 38 (Klartext) | 12% – 14.9% | 1 | | | |
| QT-010 | Z. 41 (Klartext) | \< 12% | 1 | | | |
| QT-011 | Z. 54 (Klartext) | > 40% | 1 | | | |
| QT-012 | Z. 55 (Klartext) | > 8% | 1 | | | |
| QT-013 | Z. 58 (Klartext) | 35–40% ODER | 1 | | | |
| QT-014 | Z. 59 (Klartext) | 5–8% | 1 | | | |
| QT-015 | Z. 62 (Klartext) | < 35% | 1 | | | |
| QT-016 | Z. 63 (Klartext) | < 5% | 1 | | | |
| QT-017 | Z. 122 (Klartext) | Schwellenwert | 1 | | | |
| QT-018 | Z. 125 (Klartext) | ≤ 55 🟢 / 55–65 🟡 / > 65 🔴 | 1 | | | |
| QT-019 | Z. 128 (Klartext) | Unverändert (≥ 15% 🟢) | 1 | | | |
| QT-020 | Z. 129 (Klartext) | ROIC ~25%+ bestätigt Kapitaleffizienz trotz Niedrigmargen | 1 | | | |
| QT-021 | Z. 131 (Klartext) | GM-Filter deaktiviert; nur CAGR > 8% zählt | 1 | | | |
| QT-022 | Z. 132 (Klartext) | Gross Margin ~13% ist Geschäftsmodell-bedingt (Selbstkostenpreis + Membership-Fee). Moat entsteht über Membership-Loyal… | 1 | | | |
| QT-023 | Z. 136 (Klartext) | Begründung: Costcos Wert liegt im Membership-Flywheel (~93% Renewal Rate) und der | 1 | | | |
| QT-024 | Z. 148 (Klartext) | <= 1.3 | 1 | | | |
| QT-025 | Z. 150 (Klartext) | > 1.5 | 1 | | | |
| QT-026 | Z. 153 (Klartext) | CR < 95% oder FG > 8% | 1 | | | |
| QT-027 | Z. 154 (Klartext) | CR 95-100% oder FG 5-8% | 1 | | | |
| QT-028 | Z. 155 (Klartext) | CR > 100% und FG < 5% | 1 | | | |
| QT-029 | Z. 180 (Klartext) | ~30%+ | 1 | | | |
| QT-030 | Z. 181 (Klartext) | GM>70%, CAGR>15% | 1 | | | |
| QT-031 | Z. 185 (Klartext) | ~25%+ | 1 | | | |
| QT-032 | Z. 190 (Klartext) | ~30%+ | 1 | | | |
| QT-033 | Z. 195 (Klartext) | ~25%+ | 1 | | | |
| QT-034 | Z. 201 (Klartext) | Hinweis: COST läuft über die aktiven Exception-Regeln (P/FCF ≤55 🟢, GM-Filter | 1 | | | |
| QT-035 | Z. 202 (Klartext) | deaktiviert, nur CAGR >8% zählt) und wird damit korrekt als GRUEN gewertet. | 1 | | | |
| QT-036 | Z. 203 (Klartext) | Die Standard-Schwellen (P/FCF ≤35, GM >40%) gelten für COST NICHT. | 1 | | | |

## insider-intelligence SKILL.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| II-001 | Z. 19–48 | ## Architektur | 2 | | | |
| II-002 | Z. 49–69 | ## CIK-Tabelle (9 US-Satelliten — Stand 2026-06-09, Umstrukturierung-2027) | 0 | | | |
| II-003 | Z. 70–118 | ## Befehle | 0 | | | |
| II-004 | Z. 72–94 | ### !InsiderScan [TICKER \| ALL] | 1 | | | |
| II-005 | Z. 95–105 | ### !FlagCheck | 0 | | | |
| II-006 | Z. 106–118 | ### !InsiderDetail [TICKER] | 0 | | | |
| II-007 | Z. 119–149 | ## Transaktions-Klassifikation (DEFCON-Logik) | 0 | | | |
| II-008 | Z. 137–142 | ### 10b5-1 Erkennung (drei Ebenen) | 0 | | | |
| II-009 | Z. 143–149 | ### Cashless Exercise Erkennung | 0 | | | |
| II-010 | Z. 150–191 | ## DEFCON Insider-Scoring (10 Punkte) | 2 | | | |
| II-011 | Z. 160–169 | ### Net Buy Score (max 4) | 0 | | | |
| II-012 | Z. 170–178 | ### No-FLAG Score (max 3) | 0 | | | |
| II-013 | Z. 179–191 | ### Ownership Score (max 3, extern) | 4 | | | |
| II-014 | Z. 192–204 | ## FLAG-Regeln (aus INSTRUKTIONEN.md — unveraendert) | 3 | | | |
| II-015 | Z. 205–262 | ## Integration in !Analysiere Workflow | 0 | | | |
| II-016 | Z. 220–240 | ### Snapshot-First Workflow (Chat + Cowork + Code) | 2 | | | |
| II-017 | Z. 241–247 | ### Vault-Integration | 0 | | | |
| II-018 | Z. 248–262 | ### BRK.B Sonderregel (Entity-Level-Exception) | 2 | | | |
| II-019 | Z. 263–278 | ## Verhaeltnis zum generischen sec-edgar-skill | 0 | | | |
| II-020 | Z. 279–298 | ## Setup (einmalig) | 0 | | | |
| II-021 | Z. 299–313 | ## Wartung | 0 | | | |

## non-us-fundamentals SKILL.md — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| NU-001 | Z. 21–54 | ## Architektur | 1 | | | |
| NU-002 | Z. 55–71 | ## Non-US Satelliten | 2 | | | |
| NU-003 | Z. 72–124 | ## Befehle | 0 | | | |
| NU-004 | Z. 74–101 | ### !NonUSScan [TICKER \| ALL] | 0 | | | |
| NU-005 | Z. 102–112 | ### !NonUSDetail [TICKER] | 0 | | | |
| NU-006 | Z. 113–124 | ### !NonUSPrices | 0 | | | |
| NU-007 | Z. 125–140 | ## DEFCON-Metriken (was das Modul liefert) | 2 | | | |
| NU-008 | Z. 141–155 | ## FLAG-Regeln (Non-US) | 2 | | | |
| NU-009 | Z. 156–185 | ## Bekannte Daten-Limitierungen | 0 | | | |
| NU-010 | Z. 158–170 | ### RMS (Hermes) — IFRS CapEx-Luecke | 1 | | | |
| NU-011 | Z. 171–177 | ### ROIC — kein direkter Wert | 0 | | | |
| NU-012 | Z. 178–185 | ### Semi-Annual Reporting (RMS, SU) | 0 | | | |
| NU-013 | Z. 186–200 | ## Integration in !Analysiere Workflow | 0 | | | |
| NU-014 | Z. 201–226 | ## Setup (einmalig) | 0 | | | |
| NU-015 | Z. 227–238 | ## EODHD-Hinweis (warum nicht EODHD) | 0 | | | |
| NU-016 | Z. 239–256 | ## Wartung | 0 | | | |

## Vault Wissenschaftliche-Fundierung-DEFCON.md (Überschriften) — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| W-001 | Z. 109–124 | ## v3.7-Änderungsprotokoll (17.04.2026) | 5 | | | |
| W-002 | Z. 125–161 | ## 30-Befunde Entscheidungsmatrix (Stand: 10.05.2026, post Phase-D-1-Confidence-Upgrade-Pass) | 20 | | | |
| W-003 | Z. 162–224 | ## Status-Matrix (operative Aktivierungs-Klassifikation) | 0 | | | |
| W-004 | Z. 166–174 | ### Legende | 0 | | | |
| W-005 | Z. 175–209 | ### Matrix | 7 | | | |
| W-006 | Z. 210–218 | ### Aktivierungs-Regeln (bindend) | 2 | | | |
| W-007 | Z. 219–224 | ### Regel für neue Befunde (B25+) | 0 | | | |
| W-008 | Z. 225–236 | ## PFLICHT-Regeln (wörtlich, session-übergreifend) | 0 | | | |
| W-009 | Z. 227–230 | ### Aus Gu/Kelly/Xiu (2020): | 0 | | | |
| W-010 | Z. 231–236 | ### Aus Buffetts Alpha (AQR 2018): | 0 | | | |
| W-011 | Z. 237–285 | ## Quellen-Übersicht (42 Quellen inventarisiert: 36 active + 5 deferred-Stub + 1 reject-inventarisiert… | 16 | | | |
| W-012 | Z. 286–307 | ## Betroffene Entitäten | 0 | | | |
| W-013 | Z. 288–307 | ### Aktive Satelliten (v3.5-Zeitstand: 16.04.2026 — dient B1-B11 Mapping) | 8 | | | |
| W-014 | Z. 308–321 | ## Implikationen für SKILL.md | 0 | | | |
| W-015 | Z. 322–348 | ## Konzept-Karte (aktualisiert) | 1 | | | |
| W-016 | Z. 349–367 | ## Scoring-System-Audit v3.4 → v3.5 (16.04.2026) | 3 | | | |
| W-017 | Z. 368–383 | ## Änderungsprotokoll | 3 | | | |
| W-018 | Z. 384–401 | ## Validierung der Befunde (Backtest-Ready-Infrastructure, seit 2026-04-17) | 0 | | | |
| W-019 | Z. 402–421 | ## 4-Dimensionen-Validation-Gate (§29, seit 2026-04-19, erweitert 2026-04-20 + 2026-04-26) | 2 | | | |

## depot-architecture-spec.md (→ Archiv E14) — Überschriften H2–H4

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| DS-001 | Z. 16–118 | ## 1 · Zweck und Abnahmekriterium | 0 | | | |
| DS-002 | Z. 22–78 | ### 1.1 Befund | 1 | | | |
| DS-003 | Z. 79–118 | ### 1.2 Abnahmekriterium | 1 | | | |
| DS-004 | Z. 119–290 | ## 2 · Datenmodell | 1 | | | |
| DS-005 | Z. 134–156 | ### 2.1 Zuordnung aller heutigen `config.yaml`-Blöcke | 0 | | | |
| DS-006 | Z. 157–168 | ### 2.2 `satelliten`-Block feldweise (24 Felder, alle 13 Einträge) | 0 | | | |
| DS-007 | Z. 169–191 | ### 2.3 Zweite Regelwerk-Quelle: `Rebalancing_Tool` Blatt `Parameter & Regeln` | 2 | | | |
| DS-008 | Z. 192–224 | ### 2.4 Dritte Regelwerk-Quelle: `KONTEXT.md` | 0 | | | |
| DS-009 | Z. 225–248 | ### 2.4b Vierte Quelle — `00_Core/STATE.md`, die Datei mit null Treffern | 0 | | | |
| DS-010 | Z. 249–278 | ### 2.5 Der Entnahme-Topf „Hochzeit" ist kein Dynastie-Kapital | 10 | | | |
| DS-011 | Z. 279–290 | ### 2.6 Steuer-Lage — Korrektur der Doku | 0 | | | |
| DS-012 | Z. 291–507 | ## 3 · REGELWERK.yaml | 5 | | | |
| DS-013 | Z. 454–468 | ### 3.1 Beim Befüllen zu entscheiden (Daten, nicht Spec) | 1 | | | |
| DS-014 | Z. 469–476 | ### 3.2 Ersatzbank ist Synthesearbeit, kein Verschieben | 0 | | | |
| DS-015 | Z. 477–507 | ### 3.3 Overrides — Escape-Hatch für bewusste Regelabweichungen | 3 | | | |
| DS-016 | Z. 508–604 | ## 4 · Urteil-Layer | 0 | | | |
| DS-017 | Z. 512–530 | ### 4.1 Aktueller Score — Dateireihenfolge, nicht Datum | 0 | | | |
| DS-018 | Z. 531–553 | ### 4.2 FLAG-Status — zwei Objektklassen, die v1.5 vermischt hat | 4 | | | |
| DS-019 | Z. 554–559 | ### 4.3 Nicht-Roster-Ticker | 0 | | | |
| DS-020 | Z. 560–604 | ### 4.4 Zwei Gates im Score-Schreibpfad müssen neu gefasst werden | 0 | | | |
| DS-021 | Z. 585–604 | #### Gate 2 — die Tripwire P2b, härter und in derselben Datei | 1 | | | |
| DS-022 | Z. 605–625 | ## 5 · Live-Layer | 1 | | | |
| DS-023 | Z. 626–663 | ## 6 · Analyse-Pflicht | 0 | | | |
| DS-024 | Z. 632–647 | ### 6.1 Kadenz | 2 | | | |
| DS-025 | Z. 648–663 | ### 6.2 Zwei Stufen | 1 | | | |
| DS-026 | Z. 664–793 | ## 7 · `depot check` | 0 | | | |
| DS-027 | Z. 670–698 | ### 7.1 Checks | 3 | | | |
| DS-028 | Z. 699–725 | ### 7.2 Verteilungsrechnung | 2 | | | |
| DS-029 | Z. 726–742 | ### 7.3 Vorgefundener Widerspruch (Befund 2026-08-26) | 0 | | | |
| DS-030 | Z. 743–770 | ### 7.4 Entscheidung: additiv mit gestaffeltem Ziel (Owner-Freigabe 2026-08-26) | 6 | | | |
| DS-031 | Z. 771–793 | ### 7.5 Konzentrations-Kappung — der zweite zulässige Verkaufspfad | 2 | | | |
| DS-032 | Z. 794–809 | ## 8 · Generierte Artefakte | 0 | | | |
| DS-033 | Z. 810–933 | ## 9 · Migration | 0 | | | |
| DS-034 | Z. 812–836 | ### 9.1 Blast-Radius (korrigiert nach Codex-R1-H1) | 0 | | | |
| DS-035 | Z. 837–856 | ### 9.2 Zwingende Anpassungen | 0 | | | |
| DS-036 | Z. 857–911 | ### 9.3 Stufe 0 — Datenreparatur, Voraussetzung für alles Weitere | 0 | | | |
| DS-037 | Z. 866–911 | #### 9.3.1 Warum Schritt 1 entfiel — und was der Ausführungsversuch über Prüfrunden verrät | 4 | | | |
| DS-038 | Z. 912–921 | ### 9.4 Stufe 1 — begrenzter Blast-Radius | 0 | | | |
| DS-039 | Z. 922–927 | ### 9.5 Stufe 2 — eigene Session, eigener Plan | 0 | | | |
| DS-040 | Z. 928–933 | ### 9.6 Die §18-Schuld vom 26.08. löst sich auf | 0 | | | |
| DS-041 | Z. 934–950 | ## 10 · §18 neu | 0 | | | |
| DS-042 | Z. 951–983 | ## 11 · Offen | 5 | | | |
| DS-043 | Z. 984–992 | ## 12 · Prüfung dieser Spec | 0 | | | |
| DS-044 | Z. 993–1150 | ## 13 · Review-Spur | 0 | | | |
| DS-045 | Z. 1026–1044 | ### Codex-Sparring R2 auf v1.1 — 5 HIGH, 4 MEDIUM, 1 LOW | 0 | | | |
| DS-046 | Z. 1045–1050 | ### v1.3 — Owner-Entscheidung Rebalancing-Modell (2026-08-26) | 1 | | | |
| DS-047 | Z. 1051–1067 | ### Codex-Sparring R3 auf v1.2 — 2 HIGH, 1 MEDIUM, 1 Präzisierung | 0 | | | |
| DS-048 | Z. 1068–1090 | ### R4 — Eigenrunde mit Live-Verifikation und Codex-Gegenprüfung (2026-08-26) | 1 | | | |
| DS-049 | Z. 1091–1150 | ### R5 — Live-Verifikation und sechs Owner-Entscheidungen (2026-09-04) | 2 | | | |
| DS-050 | Z. 1129–1150 | #### Codex-Gegenprüfung R5 auf v1.6 (`e88f0d7`) — 2 HIGH, 2 MEDIUM, 2 LOW | 1 | | | |

## config.yaml — Blätter (Listen als `[*]` zusammengefasst)

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| C-001 | `portfolio.sparrate_eur` | 1031 | – | | | |
| C-002 | `portfolio.aktuelle_slots` | 20 | – | | | |
| C-003 | `portfolio.max_aktien_slots` | 13 | – | | | |
| C-004 | `portfolio.belegte_aktien_slots` | 13 | – | | | |
| C-005 | `portfolio.freie_aktien_slots` | 0 | – | | | |
| C-006 | `portfolio.us_hard_cap_pct` | 63 | – | | | |
| C-007 | `portfolio.us_current_pct` | 46.41 | – | | | |
| C-008 | `portfolio.zieljahr` | 2058 | – | | | |
| C-009 | `brokers.ing.zweck` | ETF-Core + Freistellungsauftrag | – | | | |
| C-010 | `brokers.ing.sparanteil_pct` | 60 | – | | | |
| C-011 | `brokers.ing.sparrate_eur` | 616.0 | – | | | |
| C-012 | `brokers.ing.freistellung_eur` | 1500 | – | | | |
| C-013 | `brokers.scalable.zweck` | Satelliten + Alpha | – | | | |
| C-014 | `brokers.scalable.sparanteil_pct` | 35 | – | | | |
| C-015 | `brokers.scalable.sparrate_eur` | 364.0 | – | | | |
| C-016 | `brokers.scalable.freistellung_eur` | 500 | – | | | |
| C-017 | `brokers.euwax.zweck` | Gold | – | | | |
| C-018 | `brokers.euwax.sparanteil_pct` | 5 | – | | | |
| C-019 | `brokers.euwax.sparrate_eur` | 51.0 | – | | | |
| C-020 | `allokation.etf_core_pct` | 60 | – | | | |
| C-021 | `allokation.satelliten_pct` | 35 | – | | | |
| C-022 | `allokation.gold_pct` | 5 | – | | | |
| C-023 | `satelliten_tier_raten.1` | 40 | – | | | |
| C-024 | `satelliten_tier_raten.2` | 32 | – | | | |
| C-025 | `satelliten_tier_raten.3` | 18 | – | | | |
| C-026 | `system_regeln._system_version` | v3.7 — 17.04.2026 (System-Gap-Release) | – | | | |
| C-027 | `system_regeln.score_verfallsregel.beschreibung` | Score gilt 180 Tage ab score_datum. Danach: QuickCheck erzwingt Re-Analyse. | – | | | |
| C-028 | `system_regeln.score_verfallsregel.formel` | score_valid_until = score_datum + 180 Tage | – | | | |
| C-029 | `system_regeln.score_verfallsregel.trigger` | Score-Alter > 180 Tage → automatischer Deep-Dive-Trigger im QuickCheck (Checkpunkt 7 Rot) | – | | | |
| C-030 | `system_regeln.substitute_activation_global.beschreibung` | Ersatz-Aktivierungsregel für alle Satelliten. Einheitlich und bindend. | – | | | |
| C-031 | `system_regeln.substitute_activation_global.vorbereitung_bei` | DEFCON 2 (Score 50–64) — Ersatz identifizieren + analysieren | – | | | |
| C-032 | `system_regeln.substitute_activation_global.ausfuehrung_bei` | DEFCON 1 (Score <50) ODER explizites Veto durch User | – | | | |
| C-033 | `system_regeln.substitute_activation_global.ersatz_voraussetzung` | Ersatz-Ticker muss zum Tauschzeitpunkt Score ≥80 + kein aktives FLAG haben | – | | | |
| C-034 | `system_regeln.substitute_activation_global.steuer_regel` | Niemals durch Verkauf tauschen — Sparplan auf Ersatz umleiten. Bei unvermeidbarem Verkauf… | – | | | |
| C-035 | `system_regeln.moat_drift_trigger.beschreibung` | Drei objektive Auslöser für automatischen !Analysiere-Trigger, unabhängig vom Score-Alter | – | | | |
| C-036 | `system_regeln.moat_drift_trigger.trigger_1` | Morningstar Moat-Downgrade Wide → Narrow (sofort, score-unabhängig) | – | | | |
| C-037 | `system_regeln.moat_drift_trigger.trigger_2` | Marktanteilsverlust >10% im Kernsegment — dokumentiert in Earnings Call / Pressebericht | – | | | |
| C-038 | `system_regeln.moat_drift_trigger.trigger_3` | Gross Margin Rückgang >5 Prozentpunkte über 4 aufeinanderfolgende Quartale (Shibui cash_f… | – | | | |
| C-039 | `system_regeln.moat_drift_trigger.aktion` | Sofortiger !Analysiere — kein Warten auf Score-Verfall | – | | | |
| C-040 | `system_regeln.sparplan_verteilung.beschreibung` | Formelle Berechnungsregel für !Rebalancing. Verbindlich. Tier-Modell-Stand (Umstrukturier… | – | | | |
| C-041 | `system_regeln.sparplan_verteilung.modell` | 3-Tier Conviction-Weighting + DEFCON-Modulation + FLAG-Heiligkeit | – | | | |
| C-042 | `system_regeln.sparplan_verteilung.tier_basis` | siehe satelliten_tier_raten (Top-Level): Tier 1 = 40€, Tier 2 = 32€, Tier 3 = 18€ (Optima… | – | | | |
| C-043 | `system_regeln.sparplan_verteilung.modulation` | DEFCON 3/4 → volle Tier-Rate (×1.0) \| DEFCON 2 → halbe Tier-Rate (×0.5, 'Sockelbetrag') … | – | | | |
| C-044 | `system_regeln.sparplan_verteilung.formel` | effektive Rate = satelliten_tier_raten[satellit.tier] × Modulation(defcon, flag) | – | | | |
| C-045 | `system_regeln.sparplan_verteilung.budget_logik` | SOLL-Σ (alle 13 × Tier-Basis) = 364€ = brokers.scalable.sparrate_eur. Funded-Σ (Summe mod… | – | | | |
| C-046 | `system_regeln.sparplan_verteilung.beispiel` | Aktueller Stand (2026-06-07, post-Umstrukturierung 13-Roster): SOLL-Σ = Tier1 4×40 (AMZN/… | – | | | |
| C-047 | `system_regeln.tariff_exposure_quelle.beschreibung` | Primärquelle für Tariff-Exposure-Scoring (Pflicht bei jedem !Analysiere) | – | | | |
| C-048 | `system_regeln.tariff_exposure_quelle.quelle_1` | SEC EDGAR 10-K / 20-F → Abschnitt 'Geographic Revenue' (primär, maschinenlesbar) | – | | | |
| C-049 | `system_regeln.tariff_exposure_quelle.quelle_2` | Earnings Call Transcript (defeatbeta get_stock_earning_call_transcript) → Management-Komm… | – | | | |
| C-050 | `system_regeln.tariff_exposure_quelle.quelle_3` | Simply Wall St 'Company Analysis' → Schätzung (Fallback wenn keine exakten Daten) | – | | | |
| C-051 | `system_regeln.tariff_exposure_quelle.schwelle_check` | CN + TW + MY + TH + VN Anteil an Revenue + Supply-Chain-Anteil > 35% → FLAG | – | | | |
| C-052 | `etfs[*].ticker` | 7× · 7 Werte: IWDA / EIMI / EXUS / AVGC / … | – | | | |
| C-053 | `etfs[*].name` | 7× · 7 Werte: iShares Core MSCI World / iShares Core MSCI EM IMI / Xtrackers MSCI World ex USA / Avantis Global Small Cap Value / … | – | | | |
| C-054 | `etfs[*].isin` | 6× · 6 Werte: IE00B4L5Y983 / IE00BKM4GZ66 / IE0006WW1TQ4 / IE0003R87OG3 / … | – | | | |
| C-055 | `etfs[*].broker` | 7× · 2 Werte: ING / Scalable | – | | | |
| C-056 | `etfs[*].typ` | 7× · 7 Werte: Developed World / Emerging Markets / Geo-Hedge / World ex USA (US-… / Factor / Small Cap Value / … | – | | | |
| C-057 | `etfs[*].rate_eur` | 7× · 5 Werte: 206 / 123 / 82 / 72 / … | – | | | |
| C-058 | `satelliten[*].ticker` | 13× · 13 Werte: ASML / AVGO / MSFT / RMS / … | – | | | |
| C-059 | `satelliten[*].name` | 13× · 13 Werte: ASML Holding / Broadcom / Microsoft / Hermès International / … | – | | | |
| C-060 | `satelliten[*].typ` | 13× · 13 Werte: Asset-Light / Halbleiter-Equi… / Asset-Light / Semiconductors / Asset-Light / Cloud / Substanz / Luxury / … | – | | | |
| C-061 | `satelliten[*].tier` | 13× · 3 Werte: 2 / 1 / 3 | – | | | |
| C-062 | `satelliten[*].defcon` | 13× · 3 Werte: 3 / 2 / 1 | – | | | |
| C-063 | `satelliten[*].score` | 13× · 10 Werte: 68 / 59 / 50 / 69 / … | – | | | |
| C-064 | `satelliten[*].score_datum` | 13× · 9 Werte: 2026-04-17 / 2026-09-03 / 2026-04-30 / 2026-05-04 / … | – | | | |
| C-065 | `satelliten[*].score_valid_until` | 11× · 8 Werte: 2026-10-14 / 2027-03-02 / 2026-10-27 / 2026-10-31 / … | – | | | |
| C-066 | `satelliten[*].flag` | 13× · 2 Werte: False / True | – | | | |
| C-067 | `satelliten[*].flag_hinweis` | 2× · 2 Werte: China-Revenue ~24% FY2024 (Ex… / fcf_trend_neg Resolve-Gate CL… | – | | | |
| C-068 | `satelliten[*].sparrate_hinweis` | 10× · 7 Werte: DEFCON 3, kein 🔴 FLAG → Gewic… / DEFCON 3, kein FLAG → Gewicht… / DEFCON 2, kein 🔴 FLAG → Gewic… / 🔴 FLAG aktiv → Gewicht 0.0 (e… / … | – | | | |
| C-069 | `satelliten[*].naechste_pruefung` | 13× · 13 Werte: Q2 2026 Earnings 15.07. (bmo,… / Q4 FY26 Earnings 09.12.2026 (… / Q4 FY26 Earnings 29.07. — Cap… / H1 2026 Report 29.07.2026 (8:… / … | – | | | |
| C-070 | `satelliten[*].scoring_notiz` | 13× · 12 Werte: Score 68 (v3.7 Live-Verify po… / 30.04.2026 Forward-Vollanalys… / 30.04.2026 Tag-+1 Vollanalyse… / Score 68 (v3.7 Live-Verify, 7… / … | – | | | |
| C-071 | `satelliten[*].ersatz` | 13× · 9 Werte: SNPS / NVDA / MRVL / GOOGL / RACE / … | – | | | |
| C-072 | `satelliten[*].substitute_activation_rule` | 13× · 5 Werte: siehe system_regeln.substitut… / GOOGL ist Ersatz aber selbst … / Vorbereitung PAUSIERT seit 23… / Kein definierter Ersatz — bei… / … | – | | | |
| C-073 | `satelliten[*].region` | 13× · 3 Werte: Europa / USA / Asien | – | | | |
| C-074 | `satelliten[*].us_exposure` | 13× · 2 Werte: False / True | – | | | |
| C-075 | `satelliten[*].flag_grund` | 4× · 4 Werte: Insider-Selling FLAG (insider… / CapEx/OCF FLAG aktiv — Q3 FY2… / Score-basiert — Score 61 (v3.… / CapEx/OCF FLAG aktiv (Neuaufn… | – | | | |
| C-076 | `satelliten[*].flag_seit` | 4× · 4 Werte: 2026-04-27 / 2026-Q1 / 2026-04-09 / 2026-05-15 | – | | | |
| C-077 | `satelliten[*].flag_wirkung` | 4× · 1 Werte: Sparrate komplett gestoppt (0… | – | | | |
| C-078 | `satelliten[*].flag_aufloesung` | 3× · 3 Werte: Diskretionäre Insider-Verkäuf… / Q4 FY26 Earnings 29.07.2026 —… / CapEx/OCF <60% (rolling). Rea… | – | | | |
| C-079 | `satelliten[*].roic_notiz` | 3× · 3 Werte: ROIC GAAP 5,54% (Q1'26) vs WA… / ROIC 6Q-Ø 7,68% vs. WACC defe… / ROIC 6Q-Ø ~5,4% GAAP vs WACC … | – | | | |
| C-080 | `satelliten[*].worst_case` | Score <50 → DEFCON 1 → Ersatz-Analyse eskalieren (GOOGL FLAG noch aktiv → alternativ ZTS) | – | | | |
| C-081 | `satelliten[*].screener_exception` | True | – | | | |
| C-082 | `satelliten[*].earnings_trigger` | DEFCON 4 bei: Q2 Organic ≥3% + Clario-Integration on-track + Sustained-FCF-Recovery. DEFC… | – | | | |
| C-083 | `flags_aktiv[*].ticker` | 4× · 4 Werte: MSFT / APH / AVGO / AMZN | – | | | |
| C-084 | `flags_aktiv[*].grund` | 4× · 4 Werte: CapEx/OCF FLAG aktiv (30.04.2… / Score-basiert — Score 61 (v3.… / Insider-Selling 90d $106,4M (… / CapEx/OCF TTM 99,2% netto (Vo… | – | | | |
| C-085 | `flags_aktiv[*].seit` | 4× · 4 Werte: 2026-Q1 / 2026-04-09 / 2026-04-27 / 2026-05-15 | – | | | |
| C-086 | `flags_aktiv[*].wirkung` | 4× · 1 Werte: Sparrate komplett gestoppt (0… | – | | | |
| C-087 | `flags_aktiv[*].naechste_pruefung` | 4× · 4 Werte: Q4 FY26 Earnings 29.07. — Q4-… / Q2 2026 Earnings 29.07. — Chi… / Q4 FY26 Earnings 09.12.2026 (… / Q2 FY26 Earnings — CapEx/OCF-… | – | | | |
| C-088 | `flags_review` | [] | – | | | |
| C-089 | `flags_watchlist` | [] | – | | | |
| C-090 | `screener_exceptions` | ['BRK.B', 'BRK', 'MKL', 'FFH.TO', 'COST'] | – | | | |
| C-091 | `watchlist[*].ticker` | 7× · 7 Werte: MKL / SNPS / SPGI / GOOGL / … | – | | | |
| C-092 | `watchlist[*].name` | 7× · 7 Werte: Markel Group / Synopsys / S&P Global / Alphabet / … | – | | | |
| C-093 | `watchlist[*].score` | 6× · 6 Werte: 82 / 79 / 77 / 72 / … | – | | | |
| C-094 | `watchlist[*].score_datum` | 6× · 5 Werte: 2026-03-25 / 2026-03-26 / 2026-03-31 / 2026-03-28 / … | – | | | |
| C-095 | `watchlist[*].score_valid_until` | 6× · 5 Werte: 2026-09-21 / 2026-09-22 / 2026-09-27 / 2026-09-24 / … | – | | | |
| C-096 | `watchlist[*].defcon` | 6× · 2 Werte: 4 / 3 | – | | | |
| C-097 | `watchlist[*].status` | 7× · 7 Werte: Ersatzbank BRK.B – Screen bes… / Ersatzbank ASML – 1 Punkt unt… / 3 Punkte unter Einstiegsschwe… / FLAG aktiv – kein Einstieg / … | – | | | |
| C-098 | `watchlist[*].naechste_aktion` | 7× · 7 Werte: DEFCON-Analyse bei Kurskorrek… / Re-Analyse Q2 2026 nach Q1 Ea… / Re-Analyse nach Q1 2026 Earni… / FLAG-Review nach Q2 2026 Earn… / … | – | | | |
| C-099 | `watchlist[*].screener_exception` | True | – | | | |
| C-100 | `watchlist[*].flag` | False | – | | | |
| C-101 | `watchlist[*].region` | 3× · 1 Werte: USA | – | | | |
| C-102 | `watchlist[*].us_exposure` | 3× · 1 Werte: True | – | | | |
| C-103 | `watchlist[*].quick_screener.datum` | 2026-04-25 | – | | | |
| C-104 | `watchlist[*].quick_screener.ergebnis` | GRÜN | – | | | |
| C-105 | `watchlist[*].quick_screener.p_fcf` | 30.2 | – | | | |
| C-106 | `watchlist[*].quick_screener.p_fcf_quelle` | GuruFocus (10J-Median 37.3) | – | | | |
| C-107 | `watchlist[*].quick_screener.roic_ttm` | 43.0 | – | | | |
| C-108 | `watchlist[*].quick_screener.roic_quelle` | GuruFocus | – | | | |
| C-109 | `watchlist[*].quick_screener.moat` | Wide | – | | | |
| C-110 | `watchlist[*].quick_screener.moat_quelle` | Morningstar moat-score | – | | | |
| C-111 | `watchlist[*].related` | ['V'] | – | | | |
| C-112 | `keine_zuteilung[*].ticker` | 4× · 4 Werte: CLPBY / CPRT / MSCI / PEGA | – | | | |
| C-113 | `keine_zuteilung[*].grund` | 4× · 2 Werte: Bewertung prüfen / Earnings Mai 2026 abwarten | – | | | |
| C-114 | `termine[*].datum` | 10× · 10 Werte: 2026-07-15 / 2026-07-22 / 2026-07-28 / 2026-07-29 / … | – | | | |
| C-115 | `termine[*].event` | 10× · 10 Werte: ASML Q2 2026 (bmo, confirmed)… / NOW Q2 (yf/UW; TipRanks 29.07… / V Q3 FY26 (amc) → Cross-Borde… / MSFT Q4 FY26 (amc) CapEx-Plat… / … | – | | | |
| C-116 | `api_audit_log.eintraege` | ['2026-04-07 \| ASML \| OCF: ~10% Δ (IFRS 16 vs ASC 842, strukturell) \| CapEx: ≤3.5% Δ \… | – | | | |
| C-117 | `api_audit_log.naechster_check` | 2026-08-01 | – | | | |
| C-118 | `api_audit_log.check_ticker_q2` | ['V', 'BRK.B', 'TMO'] | – | | | |

## config.yaml — Kommentarblöcke

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| CK-001 | Z. 1–3 | Dynastie-Depot – Portfolio State Regeln: SKILL.md \| Strategie: manifest.md \| Pipeline: PIPELINE.md Stand: 2026-09-04 (AVGO Q3 FY26 Vollanalyse Paragraph 19.1… | 1 | | | |
| CK-002 | Z. 6–6 | PORTFOLIO-RAHMEN | 0 | | | |
| CK-003 | Z. 40–46 | SATELLITEN-TIER-RATEN (Single-Source, Umstrukturierung 2026-06-07) SOLL-Basisrate je Conviction-Tier (Optimal-Fall = DEFCON 3/4 clean, kein FLAG). Rate-Modell … | 2 | | | |
| CK-004 | Z. 54–54 | SYSTEMREGELN (v3.7 — 17.04.2026) | 0 | | | |
| CK-005 | Z. 106–106 | ETF-CORE (60% — Bucket über ING + Scalable verteilt; broker-Tag = physische Lage) | 1 | | | |
| CK-006 | Z. 108–109 | Umstrukturierung 2026-06-07: exUSA gestoppt 04.06.; JEDI + WQTM neu (zwei Themen-Wetten); Gold EUWAX→EWG2. ISIN/Rate aus UMSTRUKTURIERUNG-2027 §2. exUSA-Re-Add… | 1 | | | |
| CK-007 | Z. 154–157 | SATELLITEN (Scalable) – 13/13 Slots belegt (Umstrukturierung 2026-06-07: VEEV+COST raus, NOW/KYCCF/ZETA rein) 3-Tier Conviction-Modell (siehe satelliten_tier_r… | 1 | | | |
| CK-008 | Z. 400–400 | AKTIVE FLAGS | 0 | | | |
| CK-009 | Z. 429–430 | flags_watchlist haelt HANDELSREGELN (kein Einstieg / kein Nachkauf), nicht Urteilsstaende. Damit gehoert der Block ins REGELWERK, nicht in den Urteil-Layer (Sp… | 0 | | | |
| CK-010 | Z. 432–437 | AUFGEHOBEN 2026-09-04 (Stufe 0 Schritt 3, Owner-Entscheidung) — vorheriger Eintrag zur Nachvollziehbarkeit: - ticker: GOOGL grund: "CapEx FY26: 74-79% OCF — st… | 1 | | | |
| CK-011 | Z. 439–442 | Begruendung der Aufhebung: Der Owner baut GOOGL seit 26.08.2026 bewusst als Core-Position auf (Sparplan 50 EUR/Mt, Position seit 01.09.2026). Eine Handelsregel… | 0 | | | |
| CK-012 | Z. 444–448 | WICHTIG: Der CapEx/OCF-FLAG bleibt AKTIV (Trigger GOOGL_capex_ocf_2026-03-15 ohne Resolve). Ausschluss = Handelsregel (Owner hebt auf). FLAG = Urteilsstand (nu… | 0 | | | |
| CK-013 | Z. 452–453 | SCREENER-EXCEPTIONS (Float-/Holding-Modelle) Verwendet angepasste Schwellenwerte: P/B statt P/FCF | 1 | | | |
| CK-014 | Z. 463–463 | WATCHLIST / ERSATZBANK | 0 | | | |
| CK-015 | Z. 544–544 | KEINE ZUTEILUNG (Beobachtung, keine Analyse-Prio) | 0 | | | |
| CK-016 | Z. 557–557 | TERMINE & TRIGGER (Stand 25.04.2026) | 0 | | | |
| CK-017 | Z. 560–561 | Stand 2026-06-09: tool-kanonische Earnings-Termine (earnings_calendar.py, yfinance+Override SSoT). 30-Tage-Fenster (→09.07.) leer; nächstes Roster-Event ASML 1… | 0 | | | |
| CK-018 | Z. 578–578 | Sonstige offene (non-earnings): | 0 | | | |
| CK-019 | Z. 585–585 | API-AUDIT-LOG (Quarterly Sanity Check) | 0 | | | |

## xlsx — Parameterblatt / bedingte Formate / Vergleichsformeln

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| X-001 | `Rebalancing_Tool_v4.0!Parameter & Regeln!1` | ⚙️ REBALANCING PARAMETER | – | | | |
| X-002 | `Rebalancing_Tool_v4.0!Parameter & Regeln!3` | Parameter · Wert · Einheit | – | | | |
| X-003 | `Rebalancing_Tool_v4.0!Parameter & Regeln!4` | Sparrate monatlich · 1031 · € | – | | | |
| X-004 | `Rebalancing_Tool_v4.0!Parameter & Regeln!5` | ETF-Core Zielanteil · 0.597 · % | – | | | |
| X-005 | `Rebalancing_Tool_v4.0!Parameter & Regeln!6` | Satelliten Zielanteil · 0.353 · % | – | | | |
| X-006 | `Rebalancing_Tool_v4.0!Parameter & Regeln!7` | Gold Zielanteil · 0.05 · % | – | | | |
| X-007 | `Rebalancing_Tool_v4.0!Parameter & Regeln!8` | Drift-Toleranz ETF/Gold · 0.015 · % | – | | | |
| X-008 | `Rebalancing_Tool_v4.0!Parameter & Regeln!9` | Drift-Toleranz Aktien · 0.04 · % | – | | | |
| X-009 | `Rebalancing_Tool_v4.0!Parameter & Regeln!10` | Single-Stock-Cap · 0.1 · % | – | | | |
| X-010 | `Rebalancing_Tool_v4.0!Parameter & Regeln!11` | US-Hard-Cap · 0.63 · % | – | | | |
| X-011 | `Rebalancing_Tool_v4.0!Parameter & Regeln!12` | Max Aktien Slots · 13 | – | | | |
| X-012 | `Rebalancing_Tool_v4.0!Parameter & Regeln!13` | Aktien-Slots belegt · =COUNTIF('Portfolio & Rebalancing'!C5:C24,"Aktie") | – | | | |
| X-013 | `Rebalancing_Tool_v4.0!Parameter & Regeln!14` | Gesamt Positionen belegt · =COUNTIFS('Portfolio & Rebalancing'!A5:A24,"<>",'Portfolio … | – | | | |
| X-014 | `Rebalancing_Tool_v4.0!Parameter & Regeln!15` | Drift-Warnschwelle (Faktor × Toleranz → K rot) · 3 · × | – | | | |
| X-015 | `Rebalancing_Tool_v4.0!Parameter & Regeln!16` | Allokations-Check (Summe ETF+Sat+Gold) · =B5+B6+B7 · % | – | | | |
| X-016 | `Rebalancing_Tool_v4.0!Parameter & Regeln!17` | 📋 REBALANCING-REGELN | – | | | |
| X-017 | `Rebalancing_Tool_v4.0!Parameter & Regeln!19` | Situation · Bedeutung · Aktion | – | | | |
| X-018 | `Rebalancing_Tool_v4.0!Parameter & Regeln!20` | Abweichung negativ (rot) · Untergewicht · 📈 Sparrate erhöhen/starten | – | | | |
| X-019 | `Rebalancing_Tool_v4.0!Parameter & Regeln!21` | Abweichung positiv (gelb) · Übergewicht · 📉 Sparrate stoppen/drosseln | – | | | |
| X-020 | `Rebalancing_Tool_v4.0!Parameter & Regeln!22` | Innerhalb Toleranz (grün) · Gleichgewicht · ⚖️ Sparrate weiterführen | – | | | |
| X-021 | `Rebalancing_Tool_v4.0!Parameter & Regeln!23` | NIEMALS durch Verkauf rebalancen · Steuer-Bremse · Nur Sparplan umleiten | – | | | |
| X-022 | `Rebalancing_Tool_v4.0!Parameter & Regeln!25` | Satelliten-Budget / Monat · =B4*B6 · € | – | | | |
| X-023 | `Rebalancing_Tool_v4.0!Parameter & Regeln!26` | Aktive Aktien (DEFCON 3+, kein 🔴 FLAG) · =COUNTIFS('Portfolio & Rebalancing'!C5:C24,"Aktie",'Portfol… | – | | | |
| X-024 | `Rebalancing_Tool_v4.0!Parameter & Regeln!27` | DEFCON-2-Sockelbetrag (% der vollen Rate) · 0.5 · % | – | | | |
| X-025 | `Rebalancing_Tool_v4.0!Parameter & Regeln!28` | 📋 DEFCON-SPARRATEN-LOGIK | – | | | |
| X-026 | `Rebalancing_Tool_v4.0!Parameter & Regeln!29` | DEFCON 4 oder 3 (kein 🔴 FLAG) · Volle Sparrate (Gewicht 1.0) · Budget ÷ Σ Gewichte × 1.0 | – | | | |
| X-027 | `Rebalancing_Tool_v4.0!Parameter & Regeln!30` | DEFCON 2 (kein 🔴 FLAG) · 50% Sockelbetrag (Gewicht 0.5) · Budget ÷ Σ Gewichte × 0.5 — Position halten | – | | | |
| X-028 | `Rebalancing_Tool_v4.0!Parameter & Regeln!31` | DEFCON 1 (egal welcher FLAG) · 0 € – eingefroren · Exit-Kandidat — Auswechslung prüfen | – | | | |
| X-029 | `Rebalancing_Tool_v4.0!Parameter & Regeln!32` | 🔴 FLAG (egal welcher DEFCON) · 0 € – eingefroren · 🔴 FLAG überschreibt jeden Score | – | | | |
| X-030 | `Rebalancing_Tool_v4.0!Parameter & Regeln!34` | 🎯 TIER-SYSTEM (Satelliten-Gewichtung) | – | | | |
| X-031 | `Rebalancing_Tool_v4.0!Parameter & Regeln!35` | Tier 1 – Gewicht/SOLL-Rate · 40 · AMZN · MSFT · NOW · AVGO | – | | | |
| X-032 | `Rebalancing_Tool_v4.0!Parameter & Regeln!36` | Tier 2 – Gewicht/SOLL-Rate · 32 · V · KYCCF · ASML | – | | | |
| X-033 | `Rebalancing_Tool_v4.0!Parameter & Regeln!37` | Tier 3 – Gewicht/SOLL-Rate · 18 · RMS · BRK.B · TMO · APH · SU · ZETA | – | | | |
| X-034 | `Rebalancing_Tool_v4.0!Parameter & Regeln!39` | 🎯 TIER-ZUORDNUNG (Ticker → Tier-Faktor) | – | | | |
| X-035 | `Rebalancing_Tool_v4.0!Parameter & Regeln!40` | Ticker · Tier · Faktor | – | | | |
| X-036 | `Rebalancing_Tool_v4.0!Parameter & Regeln!41` | AMZN · 1 · =$B$35 | – | | | |
| X-037 | `Rebalancing_Tool_v4.0!Parameter & Regeln!42` | MSFT · 1 · =$B$35 | – | | | |
| X-038 | `Rebalancing_Tool_v4.0!Parameter & Regeln!43` | NOW · 1 · =$B$35 | – | | | |
| X-039 | `Rebalancing_Tool_v4.0!Parameter & Regeln!44` | AVGO · 1 · =$B$35 | – | | | |
| X-040 | `Rebalancing_Tool_v4.0!Parameter & Regeln!45` | V · 2 · =$B$36 | – | | | |
| X-041 | `Rebalancing_Tool_v4.0!Parameter & Regeln!46` | KYCCF · 2 · =$B$36 | – | | | |
| X-042 | `Rebalancing_Tool_v4.0!Parameter & Regeln!47` | ASML · 2 · =$B$36 | – | | | |
| X-043 | `Rebalancing_Tool_v4.0!Parameter & Regeln!48` | RMS · 3 · =$B$37 | – | | | |
| X-044 | `Rebalancing_Tool_v4.0!Parameter & Regeln!49` | BRK.B · 3 · =$B$37 | – | | | |
| X-045 | `Rebalancing_Tool_v4.0!Parameter & Regeln!50` | TMO · 3 · =$B$37 | – | | | |
| X-046 | `Rebalancing_Tool_v4.0!Parameter & Regeln!51` | APH · 3 · =$B$37 | – | | | |
| X-047 | `Rebalancing_Tool_v4.0!Parameter & Regeln!52` | SU · 3 · =$B$37 | – | | | |
| X-048 | `Rebalancing_Tool_v4.0!Parameter & Regeln!53` | ZETA · 3 · =$B$37 | – | | | |
| X-049 | `Rebalancing_Tool_v4.0!Parameter & Regeln!55` | 💶 FESTE SPARRATEN ETF/GOLD (€/Monat) | – | | | |
| X-050 | `Rebalancing_Tool_v4.0!Parameter & Regeln!56` | EWG2 · 51 | – | | | |
| X-051 | `Rebalancing_Tool_v4.0!Parameter & Regeln!57` | IWDA · 206 | – | | | |
| X-052 | `Rebalancing_Tool_v4.0!Parameter & Regeln!58` | EIMI · 123 | – | | | |
| X-053 | `Rebalancing_Tool_v4.0!Parameter & Regeln!59` | EXUS · 82 | – | | | |
| X-054 | `Rebalancing_Tool_v4.0!Parameter & Regeln!60` | AVGC · 82 | – | | | |
| X-055 | `Rebalancing_Tool_v4.0!Parameter & Regeln!61` | JEDI · 72 | – | | | |
| X-056 | `Rebalancing_Tool_v4.0!Parameter & Regeln!62` | WQTM · 51 | – | | | |
| X-057 | `Rebalancing_Tool_v4.0!Parameter & Regeln!64` | 📌 REBALANCING-SIGNAL (manuell) | – | | | |
| X-058 | `Rebalancing_Tool_v4.0!Parameter & Regeln!65` | Schwelle Fehlbetrag für Nachkauf-Signal (€) · 300 | – | | | |
| XF-001 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!H25` | expression/-: ABS($H$25-1)>0.0001 | – | | | |
| XF-002 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!K5:K24` | dataBar/-: dataBar | – | | | |
| XF-003 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!L5:L24` | expression/-: NOT(ISERROR(SEARCH("Reduzieren",L5))) | – | | | |
| XF-004 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!L5:L24` | expression/-: NOT(ISERROR(SEARCH("Aufstocken",L5))) | – | | | |
| XF-005 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!L5:L24` | expression/-: NOT(ISERROR(SEARCH("Halten",L5))) | – | | | |
| XF-006 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!M5:M24` | expression/-: NOT(ISERROR(SEARCH("ÜBER CAP",M5))) | – | | | |
| XF-007 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!M5:M24` | expression/-: NOT(ISERROR(SEARCH("OK",M5))) | – | | | |
| XF-008 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!N12:N24` | containsText/containsText: NOT(ISERROR(SEARCH("DEFCON 1",N12))) | – | | | |
| XF-009 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!N12:N24` | containsText/containsText: NOT(ISERROR(SEARCH("DEFCON 2",N12))) | – | | | |
| XF-010 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!N12:N24` | containsText/containsText: NOT(ISERROR(SEARCH("DEFCON 3",N12))) | – | | | |
| XF-011 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!O12:O24` | containsText/containsText: NOT(ISERROR(SEARCH("🔴",O12))) | – | | | |
| XF-012 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!O12:O24` | containsText/containsText: NOT(ISERROR(SEARCH("🟠",O12))) | – | | | |
| XF-013 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!O12:O24` | containsText/containsText: NOT(ISERROR(SEARCH("🟡",O12))) | – | | | |
| XF-014 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!O12:O24` | containsText/containsText: NOT(ISERROR(SEARCH("✅",O12))) | – | | | |
| XF-015 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!P5:P24` | expression/-: P5="" | – | | | |
| XF-016 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!R5:R24` | containsText/containsText: NOT(ISERROR(SEARCH("Nachkaufen",R5))) | – | | | |
| XF-017 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!R5:R24` | containsText/containsText: NOT(ISERROR(SEARCH("Über Ziel",R5))) | – | | | |
| XF-018 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!R5:R24` | containsText/containsText: NOT(ISERROR(SEARCH("FLAG",R5))) | – | | | |
| XF-019 | `Rebalancing_Tool_v4.0!Parameter & Regeln!B16` | expression/-: ABS($B$16-1)>0.0001 | – | | | |
| XF-020 | `Satelliten_Monitor_v4.0!Satelliten Monitor!L7:L19` | expression/-: ISNUMBER(SEARCH("DEFCON 4",L7)) | – | | | |
| XF-021 | `Satelliten_Monitor_v4.0!Satelliten Monitor!L7:L19` | expression/-: ISNUMBER(SEARCH("DEFCON 3",L7)) | – | | | |
| XF-022 | `Satelliten_Monitor_v4.0!Satelliten Monitor!L7:L19` | expression/-: ISNUMBER(SEARCH("DEFCON 2",L7)) | – | | | |
| XF-023 | `Satelliten_Monitor_v4.0!Satelliten Monitor!L7:L19` | expression/-: ISNUMBER(SEARCH("DEFCON 1",L7)) | – | | | |
| XF-024 | `Satelliten_Monitor_v4.0!Satelliten Monitor!M7:M19` | cellIs/lessThan: 0 | – | | | |
| XF-025 | `Satelliten_Monitor_v4.0!Satelliten Monitor!M7:M19` | cellIs/greaterThan: 0 | – | | | |
| XF-026 | `Satelliten_Monitor_v4.0!Satelliten Monitor!M7:M19` | cellIs/equal: 0 | – | | | |
| XF-027 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: LEFT(N7,1)="🔴" | – | | | |
| XF-028 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: ISNUMBER(SEARCH("FLAG",N7)) | – | | | |
| XF-029 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: LEFT(N7,1)="🟠" | – | | | |
| XF-030 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: LEFT(N7,1)="🟡" | – | | | |
| XF-031 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: ISNUMBER(SEARCH("DEFCON 3",N7)) | – | | | |
| XF-032 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: LEFT(N7,1)="🟢" | – | | | |
| XF-033 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: ISNUMBER(SEARCH("Halten",N7)) | – | | | |
| XF-034 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: ISNUMBER(SEARCH("DEFCON 2",N7)) | – | | | |
| XF-035 | `Satelliten_Monitor_v4.0!Satelliten Monitor!N7:N19` | expression/-: OR(ISNUMBER(SEARCH("NEU",N7)),ISNUMBER(SEARCH("ausstehend",N7))) | – | | | |
| XF-036 | `Satelliten_Monitor_v4.0!Satelliten Monitor!O7:O19` | cellIs/equal: 0 | – | | | |
| XF-037 | `Satelliten_Monitor_v4.0!Satelliten Monitor!O7:O19` | cellIs/greaterThan: 0 | – | | | |
| XF-038 | `Satelliten_Monitor_v4.0!Satelliten Monitor!R7:R19` | cellIs/lessThanOrEqual: 30 | – | | | |
| XF-039 | `Satelliten_Monitor_v4.0!Satelliten Monitor!R7:R19` | cellIs/between: 31 ; 90 | – | | | |
| XF-040 | `Satelliten_Monitor_v4.0!Satelliten Monitor!R7:R19` | cellIs/greaterThan: 90 | – | | | |
| XF-041 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!D6:D18` | expression/-: $J6=-1 | – | | | |
| XF-042 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!D6:D18` | expression/-: AND($J6>=0,$J6<=35) | – | | | |
| XF-043 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!D6:D18` | expression/-: AND($J6>35,$J6<=45) | – | | | |
| XF-044 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!D6:D18` | expression/-: $J6>45 | – | | | |
| XF-045 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!D6:G18` | containsText/containsText: NOT(ISERROR(SEARCH("ausstehend",D6))) | – | | | |
| XF-046 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!E6:E18` | expression/-: $K6=-1 | – | | | |
| XF-047 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!E6:E18` | expression/-: $K6>=15 | – | | | |
| XF-048 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!E6:E18` | expression/-: AND($K6>=12,$K6<15) | – | | | |
| XF-049 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!E6:E18` | expression/-: AND($K6>=0,$K6<12) | – | | | |
| XF-050 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!F6:F18` | containsText/containsText: NOT(ISERROR(SEARCH("Wide",F6))) | – | | | |
| XF-051 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!F6:F18` | containsText/containsText: NOT(ISERROR(SEARCH("Narrow",F6))) | – | | | |
| XF-052 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!F6:F18` | containsText/containsText: NOT(ISERROR(SEARCH("None",F6))) | – | | | |
| XF-053 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!G6:G18` | containsText/containsText: NOT(ISERROR(SEARCH("FLAG",G6))) | – | | | |
| XF-054 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!G6:G18` | containsText/containsText: NOT(ISERROR(SEARCH("D2",G6))) | – | | | |
| XF-055 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!G6:G18` | containsText/containsText: NOT(ISERROR(SEARCH("Sockel",G6))) | – | | | |
| XF-056 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!H6:H18` | containsText/containsText: NOT(ISERROR(SEARCH("NEU",H6))) | – | | | |
| XF-057 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!H6:H18` | containsText/containsText: NOT(ISERROR(SEARCH("EINGEFROREN",H6))) | – | | | |
| XF-058 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!H6:H18` | containsText/containsText: NOT(ISERROR(SEARCH("Sockelbetrag",H6))) | – | | | |
| XF-059 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!H6:H18` | containsText/containsText: NOT(ISERROR(SEARCH("VOLLRATE",H6))) | – | | | |
| XF-060 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!H6:H18` | containsText/containsText: NOT(ISERROR(SEARCH("HALTEN",H6))) | – | | | |
| XL-001 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!G5` (+19) | =IF(F$#=0,0,F#/F$#) | – | | | |
| XL-002 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!L5` (+19) | =IF(C#="Aktie",IF(K#>'Parameter & Regeln'!B$#,"📉 Reduzieren",IF(K#<-'Parameter & Regeln'!B$#,"📈 Aufstocken","⚖️ Halten")),IF(K#>'Parameter … | – | | | |
| XL-003 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!M5` (+19) | =IF(C#="Aktie",IF(G#>'Parameter & Regeln'!B$#,"🚨 ÜBER CAP","✅ OK"),"") | – | | | |
| XL-004 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!P5` (+19) | =IF(C#="Aktie",'Parameter & Regeln'!$B$#*'Parameter & Regeln'!$B$#*Q#/SUMIFS($Q$#:$Q$#,$C$#:$C$#,"Aktie"),IFERROR(VLOOKUP(B#,'Parameter & R… | – | | | |
| XL-005 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!Q5` (+19) | =IF(OR(C#="ETF",C#="Gold"),H#,IF(C#<>"Aktie",0,IF(OR(LEFT(O#,1)="🔴",LEFT(N#,8)="DEFCON 1"),0,IF(LEFT(N#,8)="DEFCON 2",IFERROR(VLOOKUP(B#,'P… | – | | | |
| XL-006 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!R5` (+19) | =IF(AND(C#="Aktie",OR(LEFT(O#,1)="🔴",LEFT(N#,8)="DEFCON 1")),IF(J#>'Parameter & Regeln'!$B$#,"🚩 FLAG (gesperrt)",""),IF(J#>'Parameter & Reg… | – | | | |
| XL-007 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!M25` (+1) | =COUNTIF(M#:M#,"🚨 ÜBER CAP") | – | | | |
| XL-008 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!N25` | =COUNTIF(N#:N#,"DEFCON 1*")+COUNTIF(N#:N#,"DEFCON 2*")+COUNTIF(N#:N#,"DEFCON 3*") | – | | | |
| XL-009 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!O25` | =COUNTIF(O#:O#,"🚩*")+COUNTIF(O#:O#,"🔴*") | – | | | |
| XL-010 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!P25` | =SUMIF(C#:C#,"Aktie",P#:P#)+SUMIF(C#:C#,"<>Aktie",P#:P#) | – | | | |
| XL-011 | `Rebalancing_Tool_v4.0!Portfolio & Rebalancing!F31` | =IF((F#-F#)<=0,0,F#/(F#-F#)) | – | | | |
| XL-012 | `Rebalancing_Tool_v4.0!US-Exposure!B26` | =IF('Portfolio & Rebalancing'!F#=0,0,E#/'Portfolio & Rebalancing'!F#) | – | | | |
| XL-013 | `Rebalancing_Tool_v4.0!US-Exposure!B29` | =IF(B#>B#,"⛔ ÜBER CAP","✅ OK") | – | | | |
| XL-014 | `Rebalancing_Tool_v4.0!US-Exposure!B30` | =IF(B#>B#,"⛔ ZIEL ÜBER CAP","✅ Ziel OK") | – | | | |
| XL-015 | `Rebalancing_Tool_v4.0!Parameter & Regeln!B13` | =COUNTIF('Portfolio & Rebalancing'!C#:C#,"Aktie") | – | | | |
| XL-016 | `Rebalancing_Tool_v4.0!Parameter & Regeln!B14` | =COUNTIFS('Portfolio & Rebalancing'!A#:A#,"<>",'Portfolio & Rebalancing'!F#:F#,">0") | – | | | |
| XL-017 | `Rebalancing_Tool_v4.0!Parameter & Regeln!B26` | =COUNTIFS('Portfolio & Rebalancing'!C#:C#,"Aktie",'Portfolio & Rebalancing'!N#:N#,"DEFCON 4*",'Portfolio & Rebalancing'!O#:O#,"<>🔴*")+COUNT… | – | | | |
| XL-018 | `Satelliten_Monitor_v4.0!Satelliten Monitor!R7` (+12) | =IF(Q#="","",TODAY()-Q#) | – | | | |
| XL-019 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!J6` (+12) | =IFERROR(IF(ISNUMBER(SEARCH("ausstehend",D#)),"",IF(ISNUMBER(SEARCH("Exception",D#)),-1,VALUE(SUBSTITUTE(_xlfn.TEXTBEFORE(_xlfn.TEXTAFTER(D… | – | | | |
| XL-020 | `Satelliten_Monitor_v4.0!QuickScreen Ampel!K6` (+12) | =IFERROR(IF(ISNUMBER(SEARCH("ausstehend",E#)),"",IF(ISNUMBER(SEARCH("Exception",E#)),-1,VALUE(SUBSTITUTE(_xlfn.TEXTBEFORE(_xlfn.TEXTAFTER(E… | – | | | |

## Vault — `operative_regel`-Frontmatter

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| V-001 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/5J-Fundamental-Fenster.md` | 5-Jahres-Durchschnitt als Pflichtperspektive — Spot-Werte allein sind unzureichende Prädiktoren. Jede DEFCON-Analyse prüft 5J-Trend neben aktuellem Wert. | – | | | |
| V-002 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Accruals-Anomalie-Sloan.md` | Accrual Ratio < 5% kein Effekt \| 5–10% -1 Pt. \| >10% -2 Pt. Malus. v3.6-Erweiterung: <3% → +2 Pt. Bonus (Piotroski-Parallelität). | – | | | |
| V-003 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Behavioural-Factors-DHS-Model.md` | (1) Buyback-Aktivität ist KEIN Sentiment-Bonus — gehört konzeptuell zu FIN-Long-Horizon-Behavioural-Faktor (deferred). (2) Earnings-Day-Reaktionen (Tag 0) sind… | – | | | |
| V-004 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Buffett-Faktorlogik.md` | PFLICHT: Float-Leverage (~1,6x) nicht replizierbar. Übertragbar: nur cheap + safe + high-quality als operativer Dreiklang. | – | | | |
| V-005 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/CLAUDE-md-Konstitution.md` | CLAUDE.md ist die einzige Wahrheitsquelle für Session-Verhalten — jede strukturelle Änderung sofort dort dokumentieren. Seit 17.04.2026: Session-Init liest nur… | – | | | |
| V-006 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Competitive-Advantage-Period.md` | CAP-Estimation in Bull/Bear-DCF-Szenarien (capex-fcf-template.md Sheet 2) als theoretische Begründung für Terminal-Value-Annahme; Briefing-Argument für Buy-and… | – | | | |
| V-007 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Context-Hygiene-Code.md` | Tool Search (v2.1.7+) reduziert Token-Last um ~95% — nur mit Sonnet 4 / Opus 4 verfügbar. | – | | | |
| V-008 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Context-Hygiene.md` | Nur Pflicht-Lektüren im Session-Init laden — alles weitere strikt on-demand. | – | | | |
| V-009 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Earnings-Foreknowledge-Window.md` | insider-intelligence v1 verwendet 6-Monats-Lookback (~2 Quartale) und verfehlt damit strukturell die echte Pre-Break-Sell-Zone (Q-9 bis Q-3). v2-Roadmap: 24-Mo… | – | | | |
| V-010 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/F-Score-Quality-Signal.md` | F-Score ≥7 → +2 Pt. Fundamentals-Bonus. F-Score 4–6 neutral. F-Score ≤3 → -1 Pt. Malus (niedrige Fundamentalqualität). | – | | | |
| V-011 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Faktortabelle-Architektur.md` | Faktortabelle vor API-Abfragen lesen — spart ~60-70% Token-Kosten pro Session. | – | | | |
| V-012 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/FCF-Primacy.md` | PFLICHT: Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide. FCF-Yield und P/FCF sind primäre Bewertungsanker. | – | | | |
| V-013 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Gross-Profitability-Premium.md` | Konzept dokumentarisch beschrieben, nicht in DEFCON v3.7 aktiv. Hypothetisches Scoring-Schema unten ist Diskussions-Artefakt, kein Workflow. | – | | | |
| V-014 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Insider-Trading-Primary-Signal.md` | Form-4-X/M-Filter via OpenInsider HEILIG; Buy-Side höher gewichtet als Sell-Side; diskretionäres Selling >$20M/90 Tage = automatisches FLAG. | – | | | |
| V-015 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Intangible-Adjusted-Value.md` | Bei Goodwill > 40% Assets dominiert §410 IC-Bereinigung über Regel-4 Cash-ROIC-Add-Back; bei moderaten Goodwill-Anteilen (30-40%) bleibt Regel-4 Default. §410 … | – | | | |
| V-016 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Media-Pessimism-Sentiment.md` | Score-Stabilität-Anker: Score-Updates an strukturelle Trigger gebunden (Earnings, FLAG-Events, Watch-Resolves), NICHT an kurzfristige Sentiment-Schwankungen — … | – | | | |
| V-017 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Moat-Taxonomie-Morningstar.md` | 8 Moat-Quellen prüfen; Wide Moat ≠ automatisch Excess Return — erst in Kombination mit Fundamentals und attraktiver Bewertung. CAP-Mapping (Mauboussin/Callahan… | – | | | |
| V-018 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Noise-Trader-Model.md` | Mean-Reversion ist erwartetes Equilibrium-Verhalten in Märkten mit Noise-Traders; kurzfristige Sentiment-Drifts triggern KEINEN Score-Update. | – | | | |
| V-019 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Post-Publication-Decay.md` | Externe in-sample-Performance-Claims werden vor Adoption mit Faktor 0,42 (= 1 − 0,58) diskontiert. Eigenes Score-Archiv (post-publication-Sample) benötigt kein… | – | | | |
| V-020 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/QMJ-Faktor.md` | QMJ + BAB + Value erklärt Buffetts Alpha vollständig — cheap+safe+quality ist wissenschaftlich fundiert und operativ replizierbar. | – | | | |
| V-021 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Session-Start-Protokoll.md` | Session-Start liest STATE.md (Hub, ~40 Z) + PORTFOLIO.md (Live-State). Andere 00_Core-Dateien on-demand via Routing-Table. Spart ~80% Auto-Read-Token gegenüber… | – | | | |
| V-022 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Token-Mechanik.md` | Token-Kosten durch strukturiertes Laden minimieren — kein redundantes Vollladen großer Dateien. | – | | | |
| V-023 | `Obsidian Mindmap/Investing Mastermind/wiki/concepts/Update-Klassen-DEFCON.md` | Klasse C (Event-getriggert) hat Vorrang — Insider >$20M oder Moat-Downgrade löst Sofortupdate aus, Score-Alter irrelevant. | – | | | |

## depot-architecture-spec.md — Code-/YAML-Blöcke

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| DSY-001 | Z. 295–440 | ```yaml meta: {version: "1.0", gueltig_ab: 2026-09-05} · budget: · monatlich_eur: 1068 # Owner-Entscheidung 04.09.2026: Broker-Ist uebernommen · # (vorher 1031… | 5 | | | |
| DSY-002 | Z. 566–568 | ```python REQUIRED_TOUCH_FILES = ("PORTFOLIO.md", "Faktortabelle.md", "log.md") | 0 | | | |
| DSY-003 | Z. 578–581 | ```python REQUIRED_TOUCH_FILES = ("log.md",) # Chronik, weiterhin handgeschrieben · # zusätzlich: REGELWERK.yaml, wenn die Analyse eine Regel geändert hat | 0 | | | |
| DSY-004 | Z. 591–593 | ``` Ticker +1=Score +2=DEFCON +3=Rate +4=FLAG | 0 | | | |
| DSY-005 | Z. 711–716 | ``` Gewicht Q_i = 0 falls FLAG aktiv oder DEFCON 1 · tier_basis(i) × 0,5 falls DEFCON 2 · tier_basis(i) sonst · Rate P_i = Sparrate × Aktienanteil × Q_i / Σ Q … | 2 | | | |
| DSY-006 | Z. 870–872 | ```python flag_typ: Literal["capex_ocf", "fcf_trend_neg", "insider_selling_20m", "tariff_exposure"] | 0 | | | |

## earnings_schedule_overrides.yaml — Blätter (ohne Regex-Filter)

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| EO-001 | `schema_version` | 1.0 | – | | | |
| EO-002 | `schedules.SU.ir_calendar_url` | https://www.se.com/ww/en/about-us/investor-relations/financial-results/ | – | | | |
| EO-003 | `schedules.SU.events[*].date` | 2× · 2 Werte: 2026-07-30 / 2026-10-29 | – | | | |
| EO-004 | `schedules.SU.events[*].type` | 2× · 2 Werte: half_year_h1 / trading_update_q3 | – | | | |
| EO-005 | `schedules.RMS.ir_calendar_url` | https://finance.hermes.com/en/calendar | – | | | |
| EO-006 | `schedules.RMS.events[*].date` | 2× · 2 Werte: 2026-07-29 / 2026-10-22 | – | | | |
| EO-007 | `schedules.RMS.events[*].type` | 2× · 2 Werte: half_year_h1 / trading_update_q3 | – | | | |
| EO-008 | `schedules.RMS.events[*].note` | 2× · 1 Werte: 08:00 CEST | – | | | |
| EO-009 | `schedules.ASML.ir_calendar_url` | https://www.asml.com/investors/financial-calendar | – | | | |
| EO-010 | `schedules.ASML.events[*].date` | 2026-07-15 | – | | | |
| EO-011 | `schedules.ASML.events[*].type` | half_year_h1 | – | | | |
| EO-012 | `schedules.ASML.events[*].note` | Q2 H1-cumulative; auch in yfinance, Override als Backup | – | | | |

## earnings_schedule_overrides.yaml — Kommentarblöcke (ohne Regex-Filter)

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| EOK-001 | Z. 1–2 | earnings_schedule_overrides.yaml — SSoT für IR-Termine, die yfinance nicht zuverlässig liefert (Schneider/Hermes Q1+Q3 Trading-Updates, ASML H1-Backup). | 0 | | | |
| EOK-002 | Z. 4–6 | Pflege 1x/Jahr nach IR-Calendar-Release der Non-US-Issuer (typisch November/Dezember für Folgejahr). Past-Filter im Tool eliminiert obsolete Events automatisch. | 0 | | | |
| EOK-003 | Z. 8–10 | Ticker-Konvention: Dynastie-internal symbols (siehe 01_Skills/dynastie-depot/config.yaml satelliten[]). Yahoo-Suffix-Mapping happens in earnings_calendar.py YA… | 0 | | | |
| EOK-004 | Z. 12–14 | Confusion-Guard: SU = Schneider Electric (Yahoo: SU.PA, Euronext Paris), NICHT Suncor Energy (Yahoo: SU bare, NYSE/TSX). YAHOO_MAP regelt das, aber dieser Comm… | 0 | | | |
| EOK-005 | Z. 18–22 | Event-Type-Werte (relevant fuer Paragraph 19.1 Tag-0/Tag-+1-Decision; Sub-Workflow out-of-scope fuer Stufe 2): trading_update_q1, trading_update_q3 -> revenue-… | 0 | | | |
| EOK-006 | Z. 30–30 | 2027-Annual: noch nicht von SE IR angekuendigt; Pflege-Workflow Nov/Dez 2026 nachziehen. | 0 | | | |
| EOK-007 | Z. 36–36 | 2027-Annual: noch nicht von Hermes IR angekuendigt; Pflege-Workflow Nov/Dez 2026 nachziehen. | 0 | | | |
| EOK-008 | Z. 41–43 | ASML hat Q3 als richtige Earnings-Call (yfinance covered) - kein Override noetig. Capital Markets Day 2026 nicht angekuendigt; ASML hatte 2024 Investor Day. 20… | 0 | | | |

## Code — Modul-Konstanten (GROSSBUCHSTABEN, Literalwert) aktiver Skills + 03_Tools

| ID | Fundstelle | Inhalt | Treffer | Verdikt | E-Bezug | Skill wörtlich? |
|---|---|---|---|---|---|---|
| PY-001 | `01_Skills/insider-intelligence/insider_intel.py:41` | `DATA_URL` = 'https://data.sec.gov' | – | | | |
| PY-002 | `01_Skills/insider-intelligence/insider_intel.py:42` | `SEC_WWW` = 'https://www.sec.gov' | – | | | |
| PY-003 | `01_Skills/insider-intelligence/insider_intel.py:45` | `USER_AGENT` = 'Tobias tobikowa90@gmail.com' | – | | | |
| PY-004 | `01_Skills/insider-intelligence/insider_intel.py:51` | `SATELLITES_CIK` = {'AVGO': '0001730168', 'MSFT': '0000789019', 'V': '0001403161', 'BRK.B': '0001067983', 'TMO': '0000097745', 'APH': '000… | – | | | |
| PY-005 | `01_Skills/insider-intelligence/insider_intel.py:73` | `BRK_ENTITY_NAMES` = {'BERKSHIRE HATHAWAY INC.', 'BERKSHIRE HATHAWAY INC', 'BERKSHIRE HATHAWAY'} | – | | | |
| PY-006 | `01_Skills/insider-intelligence/insider_intel.py:80` | `FLAG_THRESHOLD_USD` = 20000000 | – | | | |
| PY-007 | `01_Skills/insider-intelligence/insider_intel.py:81` | `FLAG_WINDOW_DAYS` = 90 | – | | | |
| PY-008 | `01_Skills/insider-intelligence/insider_intel.py:82` | `SCORING_WINDOW_DAYS` = 180 | – | | | |
| PY-009 | `01_Skills/insider-intelligence/insider_intel.py:85` | `TX_CODES` = {'P': 'Purchase (Open Market)', 'S': 'Sale (Open Market)', 'M': 'Exercise/Conversion', 'A': 'Grant/Award', 'D': 'Dispos… | – | | | |
| PY-010 | `01_Skills/non-us-fundamentals/eodhd_intel.py:41` | `NON_US_SATELLITES` = {'ASML': {'yf_symbol': 'ASML.AS', 'name': 'ASML Holding N.V.', 'currency': 'EUR', 'exchange': 'Amsterdam', 'reporting':… | – | | | |
| PY-011 | `01_Skills/non-us-fundamentals/eodhd_intel.py:85` | `FLAG_CAPEX_THRESHOLD` = 60.0 | – | | | |
| PY-012 | `01_Skills/non-us-fundamentals/eodhd_intel.py:86` | `FLAG_SBC_THRESHOLD` = 15.0 | – | | | |
| PY-013 | `01_Skills/quick-screener/scripts/screen.py:26` | `THRESHOLDS` = {'p_fcf': {'green': 35, 'yellow': 45}, 'roic': {'green': 15, 'yellow': 12}, 'gross_margin': {'green': 40, 'yellow': 35}… | – | | | |
| PY-014 | `01_Skills/quick-screener/scripts/screen.py:40` | `EXCEPTION_THRESHOLDS` = {'price_book': {'green': 1.3, 'yellow': 1.5}, 'combined_ratio': {'green': 95, 'yellow': 100}, 'float_growth': {'green':… | – | | | |
| PY-015 | `01_Skills/quick-screener/scripts/screen.py:392` | `AMPEL_EMOJI` = {'GRUEN': '🟢', 'GELB': '🟡', 'ROT': '🔴'} | – | | | |
| PY-016 | `03_Tools/_numeric_utils.py:12` | `DEFAULT_ABS_TOL` = 1e-09 | – | | | |
| PY-017 | `03_Tools/_numeric_utils.py:13` | `DEFAULT_REL_TOL` = 1e-06 | – | | | |
| PY-018 | `03_Tools/backtest-ready/_forward_verify_helpers.py:26` | `REQUIRED_TOUCH_FILES` = ('PORTFOLIO.md', 'Faktortabelle.md', 'log.md') | – | | | |
| PY-019 | `03_Tools/backtest-ready/archive_flag.py:35` | `FLAG_METRIK_NAME` = {'capex_ocf': 'capex_ocf_pct', 'fcf_trend_neg': 'fcf_yoy_delta_pct', 'insider_selling_20m': 'insider_selling_20m_usd', … | – | | | |
| PY-020 | `03_Tools/backtest-ready/archive_score.py:49` | `FORWARD_WINDOW_DAYS` = 3 | – | | | |
| PY-021 | `03_Tools/backtest-ready/backfill_scores.py:82` | `MONTHS_DE` = {'Januar': 1, 'Februar': 2, 'März': 3, 'April': 4, 'Mai': 5, 'Juni': 6, 'Juli': 7, 'August': 8, 'September': 9, 'Oktobe… | – | | | |
| PY-022 | `03_Tools/backtest-ready/backfill_scores.py:100` | `BACKFILL_STAMP` = '2026-04-17' | – | | | |
| PY-023 | `03_Tools/backtest-ready/flag_event_study.py:48` | `HORIZONS` = [30, 90, 180, 360] | – | | | |
| PY-024 | `03_Tools/backtest-ready/flag_event_study.py:49` | `BENCHMARK_TICKER` = '^GSPC' | – | | | |
| PY-025 | `03_Tools/backtest-ready/migrate_tmo_28_block_coverage.py:59` | `TARGET_RECORD_ID` = '2026-04-23_TMO_vollanalyse' | – | | | |
| PY-026 | `03_Tools/backtest-ready/migrate_tmo_28_block_coverage.py:61` | `BACKFILL_VALUES` = {'gm_trend_3j_pct_p_a': 0.5, 'rel_strength_sp500_6m_pct': -16, 'rel_staerke_sp500_6m_pct': -16, 'kurs_vs_200ma_pct': -2… | – | | | |
| PY-027 | `03_Tools/backtest-ready/provenance_gate.py:73` | `CARRYOVER_SOURCE_PREFIXES` = ('ir_',) | – | | | |
| PY-028 | `03_Tools/backtest-ready/provenance_gate.py:86` | `QUELLEN_PFLICHT_FELDER` = ('fundamentals', 'technicals', 'insider', 'moat', 'sentiment') | – | | | |
| PY-029 | `03_Tools/backtest-ready/schemas.py:40` | `FUNDAMENTALS_CAP` = 50 | – | | | |
| PY-030 | `03_Tools/backtest-ready/schemas.py:41` | `FUNDAMENTALS_FLOOR` = 0 | – | | | |
| PY-031 | `03_Tools/backtest-ready/schemas.py:44` | `QT_FWD_PE_HARD` = 30.0 | – | | | |
| PY-032 | `03_Tools/backtest-ready/schemas.py:45` | `QT_FWD_PE_MAX1_LOW` = 22.0 | – | | | |
| PY-033 | `03_Tools/backtest-ready/schemas.py:46` | `QT_P_FCF_HARD` = 35.0 | – | | | |
| PY-034 | `03_Tools/backtest-ready/schemas.py:47` | `QT_P_FCF_MAX1_LOW` = 22.0 | – | | | |
| PY-035 | `03_Tools/backtest-ready/schemas.py:88` | `FLAG_RULES` = {'capex_ocf': (60.0, '>'), 'fcf_trend_neg': (0.0, '<'), 'insider_selling_20m': (20000000.0, '>'), 'tariff_exposure': (3… | – | | | |
| PY-036 | `03_Tools/backtest-ready/versions.py:10` | `DEFCON_ACTIVE_VERSION` = 'v3.7' | – | | | |
| PY-037 | `03_Tools/defeatbeta_subprocess.py:20` | `WSL_PYTHON` = '/home/tobia/.defeatbeta-env/bin/python' | – | | | |
| PY-038 | `03_Tools/defeatbeta_subprocess.py:21` | `WSL_DISTRO` = 'Ubuntu-24.04' | – | | | |
| PY-039 | `03_Tools/defeatbeta_subprocess.py:22` | `SUBPROCESS_TIMEOUT_SEC` = 30 | – | | | |
| PY-040 | `03_Tools/earnings_calendar.py:40` | `YAHOO_MAP` = {'BRK.B': 'BRK-B', 'ASML': 'ASML.AS', 'RMS': 'RMS.PA', 'SU': 'SU.PA', 'KYCCF': '6861.T'} | – | | | |
| PY-041 | `03_Tools/earnings_calendar.py:49` | `SMOKE_TICKER` = 'BRK.B' | – | | | |
| PY-042 | `03_Tools/earnings_calendar.py:299` | `TOOL_VERSION` = '2.0' | – | | | |
| PY-043 | `03_Tools/finnhub_a12_identity_check.py:24` | `DEFAULT_SYMBOLS` = ['MSFT', 'V', 'TMO'] | – | | | |
| PY-044 | `03_Tools/finnhub_crosswalk_trigger.py:40` | `METRIC_TOLERANCES` = {'peTTM': '5%', 'roe': '2pp', 'roic': '2pp', 'grossMargin5Y': '2pp', 'debtToEquity': '10%', 'epsGrowth5Y': '3pp', 'cape… | – | | | |
| PY-045 | `03_Tools/finnhub_crosswalk_trigger.py:98` | `FINNHUB_KEY_MAP` = {'peTTM': 'peTTM', 'roe': 'roeTTM', 'roic': 'roiTTM', 'grossMargin5Y': 'grossMargin5Y', 'debtToEquity': 'totalDebt/tota… | – | | | |
| PY-046 | `03_Tools/finnhub_smoke_test.py:28` | `SATELLITES` = ['MSFT', 'V', 'MA', 'TMO', 'COST', 'VEEV', 'APH', 'AMZN', 'AVGO', 'ASML'] | – | | | |
| PY-047 | `03_Tools/para18_sync/validator.py:40` | `EXIT_PASS` = 0 | – | | | |
| PY-048 | `03_Tools/para18_sync/validator.py:41` | `EXIT_FAIL_P1` = 1 | – | | | |
| PY-049 | `03_Tools/para18_sync/validator.py:42` | `EXIT_FAIL_P2` = 2 | – | | | |
| PY-050 | `03_Tools/para18_sync/validator.py:43` | `EXIT_FAIL_P3` = 3 | – | | | |
| PY-051 | `03_Tools/para18_sync/validator.py:44` | `EXIT_FAIL_P4` = 4 | – | | | |
| PY-052 | `03_Tools/para18_sync/validator.py:45` | `EXIT_FAIL_P5` = 5 | – | | | |
| PY-053 | `03_Tools/para18_sync/validator.py:46` | `EXIT_FAIL_P6` = 6 | – | | | |
| PY-054 | `03_Tools/para18_sync/validator.py:52` | `VALID_EVENT_TYPES` = {'system-zustand', 'critical-alert', 'score-flag-sparraten', 'pipeline-item'} | – | | | |
| PY-055 | `03_Tools/para18_sync/validator.py:404` | `ACTIVE_XLSX_BLOCK_HEADING` = '## Active xlsx-Filenames' | – | | | |
| PY-056 | `03_Tools/portfolio_risk.py:33` | `SATELLITES` = {'V': 'V', 'AVGO': 'AVGO', 'BRK.B': 'BRK-B', 'VEEV': 'VEEV', 'COST': 'COST', 'TMO': 'TMO', 'APH': 'APH', 'MSFT': 'MSFT'… | – | | | |
| PY-057 | `03_Tools/portfolio_risk.py:47` | `STRESS_SCENARIOS` = {'2020_covid_crash': ('2020-02-19', '2020-03-23'), '2022_rate_hikes': ('2022-01-01', '2022-10-31')} | – | | | |
| PY-058 | `03_Tools/portfolio_risk.py:52` | `HISTORY_START` = '2019-01-01' | – | | | |
| PY-059 | `03_Tools/portfolio_risk.py:53` | `ANN_FACTOR` = 252 | – | | | |
| PY-060 | `03_Tools/spec_inventory_diff.py:34` | `SPEC_DEFAULT` = '03_Tools/depot-architecture-spec.md' | – | | | |
| PY-061 | `03_Tools/spec_inventory_diff.py:38` | `AGENT_READ_SOURCES` = ('CLAUDE.md', '.pre-commit-config.yaml', '03_Tools/precommit/para18_sync_reminder.py') | – | | | |
| PY-062 | `03_Tools/spec_inventory_diff.py:45` | `EXTS` = ('.md', '.yaml', '.yml', '.json', '.jsonl', '.xlsx', '.py', '.toml', '.ps1', '.txt') | – | | | |
| PY-063 | `03_Tools/spec_inventory_diff.py:50` | `EXCLUDED_PREFIXES` = (('04_Templates/', 'Vorlagen, kein Live-State'), ('05_Archiv/', 'historisch -- Ausnahme: *.jsonl (Live-Append-Ziele)'),… | – | | | |
| PY-064 | `03_Tools/spec_inventory_diff.py:56` | `VAULT_KEEP` = ('WIKI-SCHEMA.md', 'log.md') | – | | | |
| PY-065 | `03_Tools/spec_inventory_diff.py:64` | `VAULT_RULE_KEYS` = ('score_aktuell', 'score_valid_until', 'flag', 'defcon', 'defcon_block', 'operative_regel', 'naechsterTrigger', 'ersatz… | – | | | |
| PY-066 | `03_Tools/spec_inventory_diff.py:75` | `NOISE_MARKERS` = ('__pycache__/', '/tests/', '/test_fixtures/', '/_fixtures/', 'node_modules/', '.venv/') | – | | | |
| PY-067 | `03_Tools/system_audit/checks/__init__.py:15` | `CORE` = {'jsonl_schema': 'system_audit.checks.jsonl_schema:run', 'store_freshness': 'system_audit.checks.store_freshness:run', … | – | | | |
| PY-068 | `03_Tools/system_audit/checks/__init__.py:32` | `OPTIONAL` = {'vault_backlinks': 'system_audit.checks.vault_backlinks:run', 'status_matrix': 'system_audit.checks.status_matrix:run'} | – | | | |
| PY-069 | `03_Tools/system_audit/checks/existence.py:32` | `WHITELIST_PREFIXES` = ('_drafts/', 'node_modules/', '.git/', 'venv/', '__pycache__/', 'http://', 'https://', '~/') | – | | | |
| PY-070 | `03_Tools/system_audit/checks/existence.py:49` | `ALIAS_RESOLUTIONS` = {'00_Core/log.md': '07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md'} | – | | | |
| PY-071 | `03_Tools/system_audit/checks/existence.py:57` | `PLAN_PATH_PREFIX` = 'docs/superpowers/plans/' | – | | | |
| PY-072 | `03_Tools/system_audit/checks/governance_parity.py:23` | `EXPECTED_FLAGS` = (('--core',), ('--full',), ('--vault',), ('--minimal-baseline',), ('--no-write',), ('--json',), ('-v', '--verbose'), ('… | – | | | |
| PY-073 | `03_Tools/system_audit/checks/header_freshness.py:21` | `DEFAULT_TARGETS` = (('03_Tools/morning-briefing-prompt-v3.md', 'Deployed'), ('03_Tools/morning-briefing-prompt-v2.md', 'Deployed'), ('01_S… | – | | | |
| PY-074 | `03_Tools/system_audit/checks/header_freshness.py:30` | `PLACEHOLDER_PATTERNS` = ('<YYYY-MM-DD>', '<DATE>', 'TBD', '<TBD>', 'TODO') | – | | | |
| PY-075 | `03_Tools/system_audit/checks/header_freshness.py:31` | `STALE_THRESHOLD_DAYS` = 30 | – | | | |
| PY-076 | `03_Tools/system_audit/checks/header_freshness.py:35` | `HEADER_SCAN_LIMIT_LINES` = 12 | – | | | |
| PY-077 | `03_Tools/system_audit/checks/score_event_parity.py:25` | `CANONICAL_SCORE_EVENT_BASENAMES` = ('log.md', 'CORE-MEMORY.md', 'Faktortabelle.md', 'PORTFOLIO.md', 'score_history.jsonl', 'config.yaml', 'flag_events.jso… | – | | | |
| PY-078 | `03_Tools/system_audit/checks/score_event_parity.py:34` | `CANONICAL_VERSION` = 'v2.1' | – | | | |
| PY-079 | `03_Tools/system_audit/checks/score_event_parity.py:35` | `WRONG_VERSIONS` = ('v1.7', 'v2.0') | – | | | |
| PY-080 | `03_Tools/system_audit/checks/skill_frontmatter.py:20` | `REQUIRED_FRONTMATTER_FIELDS` = ('name', 'description', 'version') | – | | | |
| PY-081 | `03_Tools/system_audit/checks/store_freshness.py:16` | `LAG_THRESHOLD_BUSINESS_DAYS` = 3 | – | | | |
| PY-082 | `03_Tools/system_audit/checks/sum_consistency.py:42` | `BLOCK_NUMERIC_FIELDS` = {'fundamentals': ('fwd_pe', 'p_fcf', 'bilanz', 'capex_ocf', 'roic', 'fcf_yield', 'operating_margin', 'sbc_malus', 'accr… | – | | | |
| PY-083 | `03_Tools/system_audit/checks/sum_consistency.py:67` | `ABS_TOL` = 0.01 | – | | | |
| PY-084 | `03_Tools/system_audit/report.py:12` | `STATUS_ICON` = {'PASS': '✅', 'FAIL': '❌', 'WARN': '⚠️', 'SKIP': '⏭️'} | – | | | |
| PY-085 | `03_Tools/system_audit/report.py:13` | `SEVERITY_ICON` = {'error': '🔴', 'warning': '⚠️', 'info': 'ℹ️'} | – | | | |
| PY-086 | `03_Tools/system_audit/report.py:15` | `GROUP_THRESHOLD` = 3 | – | | | |
| PY-087 | `03_Tools/system_audit/report.py:16` | `PER_SECTION_PREVIEW` = 2 | – | | | |
| PY-088 | `03_Tools/system_audit/state_writer.py:13` | `START_MARKER` = '<!-- system-audit:last-audit:start -->' | – | | | |
| PY-089 | `03_Tools/system_audit/state_writer.py:14` | `END_MARKER` = '<!-- system-audit:last-audit:end -->' | – | | | |
| PY-090 | `03_Tools/system_audit/state_writer.py:15` | `FOOTER_SENTINEL` = '🦅 STATE.md v' | – | | | |
| PY-091 | `03_Tools/system_audit.py:65` | `MINIMAL_BASELINE_KEYS` = ('jsonl_schema', 'pipeline_ssot', 'log_lag') | – | | | |

## Suchraum-Komplement (Dateibestand 00_Core · 01_Skills ohne `_extern` · 03_Tools · 04_Templates · .claude · CLAUDE.md)

> Mechanisch erzeugt: **jede** .md/.yaml/.yml/.py/.json/.toml-Datei, auch mit 0 Treffern (Regex = Priorisierung, kein Vollständigkeitsnachweis — Textregeln wie „KEIN“/„Tag +1“ trifft er nicht). `✓` = oben inventarisiert. Nicht inventarisierte Dateien sind in Schritt 2 zu begründen (Archiv, Ablaufregel, Infrastruktur).

| Datei | Zeilen | Treffer | im Suchraum |
|---|---|---|---|
| `01_Skills/dynastie-depot/SKILL.md` | 1142 | 198 | ✓ |
| `00_Core/CORE-MEMORY.md` | 468 | 91 | ✓ |
| `01_Skills/dynastie-depot/Beispiele.md` | 384 | 91 | ✓ |
| `00_Core/INSTRUKTIONEN.md` | 1000 | 83 | ✓ |
| `01_Skills/dynastie-depot/config.yaml` | 591 | 72 | ✓ |
| `03_Tools/depot-architecture-spec.md` | 1150 | 60 | ✓ |
| `03_Tools/backtest-ready/schemas.py` | 1189 | 57 | ✓ |
| `01_Skills/non-us-fundamentals/eodhd_intel.py` | 869 | 49 | ✓ |
| `01_Skills/quick-screener/references/thresholds.md` | 207 | 36 | ✓ |
| `00_Core/KONTEXT.md` | 300 | 32 | ✓ |
| `01_Skills/dynastie-depot/PIPELINE.md` | 295 | 26 |  |
| `01_Skills/quick-screener/SKILL.md` | 325 | 25 | ✓ |
| `01_Skills/insider-intelligence/insider_intel.py` | 1193 | 24 | ✓ |
| `01_Skills/dynastie-depot/capex-fcf-template.md` | 164 | 23 |  |
| `00_Core/Faktortabelle.md` | 101 | 21 | ✓ |
| `00_Core/PORTFOLIO.md` | 79 | 20 | ✓ |
| `01_Skills/core-slim-refactor/tests/fixtures/v0_2_0_t2_section_13_pre.md` | 74 | 19 |  |
| `00_Core/PIPELINE.md` | 96 | 18 |  |
| `01_Skills/insider-intelligence/SKILL.md` | 313 | 18 | ✓ |
| `01_Skills/dynastie-depot/sources.md` | 340 | 16 | ✓ |
| `01_Skills/quick-screener/scripts/screen.py` | 542 | 15 | ✓ |
| `03_Tools/portfolio_risk.py` | 487 | 14 | ✓ |
| `00_Core/SESSION-HANDOVER.md` | 156 | 13 |  |
| `00_Core/RETROSPECTIVE-GATE.md` | 169 | 12 |  |
| `01_Skills/sec-edgar-skill/SKILL.md` | 324 | 12 |  |
| `01_Skills/xlsx-smoke-test-runner/safe_insert.py` | 169 | 12 |  |
| `03_Tools/backtest-ready/migrate_tmo_28_block_coverage.py` | 203 | 12 | ✓ |
| `03_Tools/system_audit/_smoke_test.py` | 2574 | 12 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/v0_2_0_t2_section_13_v0_1_1_baseline_post.md` | 49 | 11 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/v0_2_0_t2_section_13_v0_2_0_expected_post.md` | 49 | 11 |  |
| `03_Tools/para18_sync/validator.py` | 1161 | 11 | ✓ |
| `03_Tools/system_audit/checks/markdown_header.py` | 235 | 11 |  |
| `.claude/settings.local.json` | 490 | 10 |  |
| `01_Skills/dynastie-depot/manifest.md` | 154 | 10 | ✓ |
| `03_Tools/finnhub_crosswalk_trigger.py` | 195 | 10 | ✓ |
| `00_Core/SYSTEM.md` | 96 | 9 |  |
| `03_Tools/backtest-ready/provenance_gate.py` | 501 | 9 | ✓ |
| `03_Tools/tests/test_finnhub_crosswalk_trigger.py` | 179 | 9 |  |
| `03_Tools/video_ingest_lib.py` | 110 | 9 |  |
| `01_Skills/cross-source-verify/GATE0-COVERAGE.md` | 77 | 8 |  |
| `01_Skills/non-us-fundamentals/SKILL.md` | 256 | 8 | ✓ |
| `01_Skills/sec-edgar-skill/_smoke_test.py` | 232 | 8 |  |
| `03_Tools/backtest-ready/flag_event_study.py` | 656 | 8 | ✓ |
| `03_Tools/earnings_calendar.py` | 475 | 8 | ✓ |
| `03_Tools/tests/test_finnhub_client.py` | 269 | 8 |  |
| `03_Tools/xlsx-smoke-test.md` | 176 | 8 |  |
| `03_Tools/backtest-ready/_forward_verify_helpers.py` | 342 | 7 | ✓ |
| `03_Tools/finnhub_smoke_test.py` | 198 | 7 | ✓ |
| `00_Core/APPLIED-LEARNING.md` | 66 | 6 |  |
| `03_Tools/backtest-ready/README.md` | 142 | 6 |  |
| `03_Tools/backtest-ready/backfill_scores.py` | 504 | 6 | ✓ |
| `01_Skills/core-slim-refactor/scripts/patterns.py` | 478 | 5 |  |
| `01_Skills/cross-source-verify/SKILL.md` | 115 | 5 |  |
| `03_Tools/backtest-ready/migrate_defcon_drift.py` | 98 | 5 |  |
| `03_Tools/system_audit/checks/log_lag.py` | 150 | 5 |  |
| `03_Tools/system_audit/checks/store_freshness.py` | 120 | 5 | ✓ |
| `CLAUDE.md` | 120 | 5 |  |
| `00_Core/CODE_GUIDELINES.md` | 82 | 4 |  |
| `03_Tools/backtest-ready/_drafts/ASML_20261015-1900.json` | 112 | 4 |  |
| `03_Tools/backtest-ready/backfill_flags.py` | 331 | 4 |  |
| `03_Tools/tests/test_schema_le_bounds.py` | 89 | 4 |  |
| `03_Tools/tests/test_sum_consistency.py` | 219 | 4 |  |
| `01_Skills/backtest-ready-forward-verify/_smoke_test.py` | 704 | 3 |  |
| `01_Skills/core-slim-refactor/tests/test_patterns.py` | 197 | 3 |  |
| `01_Skills/paragraph-18-sync/references/failure-recovery.md` | 49 | 3 |  |
| `03_Tools/backtest-ready/archive_score.py` | 502 | 3 | ✓ |
| `03_Tools/finnhub_client.py` | 359 | 3 |  |
| `03_Tools/hook-latency-probe.py` | 101 | 3 |  |
| `03_Tools/para18_sync/_smoke_test.py` | 1324 | 3 |  |
| `03_Tools/system_audit/fixtures/cross_source/faktortabelle.md` | 15 | 3 |  |
| `03_Tools/system_audit/state_writer.py` | 85 | 3 | ✓ |
| `03_Tools/tests/test_video_ingest_lib.py` | 234 | 3 |  |
| `00_Core/STATE.md` | 50 | 2 |  |
| `00_Core/TOKEN-RULES.md` | 48 | 2 |  |
| `01_Skills/backtest-ready-forward-verify/SKILL.md` | 291 | 2 |  |
| `01_Skills/core-slim-refactor/references/configs/core-memory-s13-lifecycle-pre-may-10-bucket.yaml` | 77 | 2 |  |
| `01_Skills/core-slim-refactor/references/failure_modes.md` | 400 | 2 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/v0_2_0_t2_section_13_cut_config.yaml` | 77 | 2 |  |
| `01_Skills/core-slim-refactor/tests/test_pipeline.py` | 190 | 2 |  |
| `01_Skills/paragraph-18-sync/SKILL.md` | 121 | 2 |  |
| `03_Tools/_numeric_utils.py` | 52 | 2 | ✓ |
| `03_Tools/backtest-ready/_drafts/ADBE_20261014.json` | 111 | 2 |  |
| `03_Tools/backtest-ready/_drafts/KYCCF_20260613-1104.json` | 112 | 2 |  |
| `03_Tools/backtest-ready/_drafts/KYCCF_bare.json` | 110 | 2 |  |
| `03_Tools/backtest-ready/_smoke_test_event_study.py` | 179 | 2 |  |
| `03_Tools/backtest-ready/archive_flag.py` | 664 | 2 | ✓ |
| `03_Tools/finnhub_a12_identity_check.py` | 55 | 2 | ✓ |
| `03_Tools/precommit/xlsx_smoke_test.py` | 314 | 2 |  |
| `03_Tools/schema_drift_phase2.py` | 108 | 2 |  |
| `03_Tools/spec_inventory_diff.py` | 353 | 2 | ✓ |
| `03_Tools/system_audit.py` | 342 | 2 | ✓ |
| `03_Tools/system_audit/checks/status_matrix.py` | 121 | 2 |  |
| `03_Tools/system_audit/checks/sum_consistency.py` | 185 | 2 | ✓ |
| `03_Tools/system_audit/report.py` | 154 | 2 | ✓ |
| `01_Skills/core-slim-refactor/references/configs/core-memory-s6-versionsverlauf-bucket.yaml` | 68 | 1 |  |
| `01_Skills/core-slim-refactor/references/pattern_specs.md` | 64 | 1 |  |
| `01_Skills/core-slim-refactor/references/yaml_schema.md` | 122 | 1 |  |
| `01_Skills/core-slim-refactor/scripts/config.py` | 267 | 1 |  |
| `01_Skills/core-slim-refactor/scripts/core_slim_refactor.py` | 745 | 1 |  |
| `01_Skills/core-slim-refactor/tests/test_backlink.py` | 42 | 1 |  |
| `01_Skills/paragraph-18-sync/references/build-time-review-log.md` | 70 | 1 |  |
| `01_Skills/paragraph-18-sync/references/event_typ_mapping.yaml` | 63 | 1 |  |
| `01_Skills/session-closure/SKILL.md` | 217 | 1 |  |
| `01_Skills/session-closure/references/commit-banners.md` | 107 | 1 |  |
| `01_Skills/session-closure/references/push-safety.md` | 108 | 1 |  |
| `01_Skills/xlsx-smoke-test-runner/SKILL.md` | 139 | 1 |  |
| `01_Skills/xlsx-smoke-test-runner/tests/test_safe_insert.py` | 193 | 1 |  |
| `03_Tools/_atomic_io.py` | 88 | 1 |  |
| `03_Tools/backtest-ready/_drafts/2026-04-30_APH_vollanalyse.json` | 1 | 1 |  |
| `03_Tools/backtest-ready/_drafts/AMZN_20260518-0140.json` | 105 | 1 |  |
| `03_Tools/backtest-ready/_drafts/AVGO_20260430-2115.json` | 115 | 1 |  |
| `03_Tools/backtest-ready/_drafts/AVGO_20260430-2115_bare.json` | 113 | 1 |  |
| `03_Tools/backtest-ready/_drafts/AVGO_20260904-0300.json` | 112 | 1 |  |
| `03_Tools/backtest-ready/_drafts/BRK.B_20260504-2240.json` | 112 | 1 |  |
| `03_Tools/backtest-ready/_drafts/BRK.B_20260504-2240_bare.json` | 109 | 1 |  |
| `03_Tools/backtest-ready/_drafts/GOOGL_20260920-0200.json` | 110 | 1 |  |
| `03_Tools/backtest-ready/_drafts/MSFT_20260430-0132.json` | 111 | 1 |  |
| `03_Tools/backtest-ready/_drafts/MSFT_20260430-0132_bare.json` | 113 | 1 |  |
| `03_Tools/backtest-ready/_drafts/_AMZN_bare.json` | 116 | 1 |  |
| `03_Tools/backtest-ready/_forward_verify_helpers_test.py` | 271 | 1 |  |
| `03_Tools/defeatbeta_subprocess.py` | 114 | 1 | ✓ |
| `03_Tools/system_audit/_smoke_temp_repo.py` | 151 | 1 |  |
| `03_Tools/system_audit/checks/cross_source.py` | 400 | 1 |  |
| `03_Tools/system_audit/checks/governance_parity.py` | 188 | 1 | ✓ |
| `03_Tools/system_audit/checks/header_freshness.py` | 178 | 1 | ✓ |
| `03_Tools/system_audit/checks/vault_backlinks.py` | 140 | 1 |  |
| `03_Tools/system_audit/fixtures/cross_source/state.md` | 7 | 1 |  |
| `03_Tools/system_audit/fixtures/markdown_header/pipeline_ok.md` | 23 | 1 |  |
| `03_Tools/system_audit/fixtures/markdown_header/portfolio_ok.md` | 17 | 1 |  |
| `03_Tools/system_audit/fixtures/markdown_header/state_hub_ok.md` | 20 | 1 |  |
| `03_Tools/video_ingest.py` | 349 | 1 |  |
| `04_Templates/CAPEX-FCF-ANALYSE.md` | 8 | 1 |  |
| `.claude/commands/SystemAudit.md` | 17 | 0 |  |
| `.claude/settings.json` | 4 | 0 |  |
| `01_Skills/.claude/settings.local.json` | 13 | 0 |  |
| `01_Skills/core-slim-refactor/SKILL.md` | 95 | 0 |  |
| `01_Skills/core-slim-refactor/references/configs/defcon-fat-rows-slim.yaml` | 67 | 0 |  |
| `01_Skills/core-slim-refactor/references/configs/ruflo-sunset-bucket.yaml` | 67 | 0 |  |
| `01_Skills/core-slim-refactor/references/configs/session-handover-banner-list-cut.yaml` | 74 | 0 |  |
| `01_Skills/core-slim-refactor/references/configs/session-handover-date-cut.yaml` | 69 | 0 |  |
| `01_Skills/core-slim-refactor/scripts/__init__.py` | 0 | 0 |  |
| `01_Skills/core-slim-refactor/scripts/backlink.py` | 80 | 0 |  |
| `01_Skills/core-slim-refactor/tests/__init__.py` | 0 | 0 |  |
| `01_Skills/core-slim-refactor/tests/_helpers.py` | 121 | 0 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/append_only_immutable.md` | 5 | 0 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/backlink_clean.md` | 7 | 0 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/backlink_positive.md` | 8 | 0 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/bucket_archive_sample.md` | 12 | 0 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/date_cut_sample.md` | 16 | 0 |  |
| `01_Skills/core-slim-refactor/tests/fixtures/slim_convention_sample.md` | 10 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_config.py` | 203 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_p18_gate_parser.py` | 56 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_reference_archive_match.py` | 146 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_session_handover_worked_example.py` | 263 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_v0_1_1_bugfixes.py` | 307 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_v0_1_2_bugfixes.py` | 115 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_v0_2_0_compat_matrix.py` | 91 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_v0_2_0_executed_auto_populate.py` | 266 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_v0_2_0_header_count_precheck.py` | 98 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_v0_2_0_pattern_c_bullet.py` | 151 | 0 |  |
| `01_Skills/core-slim-refactor/tests/test_v0_2_0_section_splice.py` | 281 | 0 |  |
| `01_Skills/non-us-fundamentals/config.json` | 6 | 0 |  |
| `01_Skills/paragraph-18-sync/references/sub-tool-coupling.md` | 36 | 0 |  |
| `01_Skills/quick-screener/references/config_extension.yaml` | 35 | 0 |  |
| `01_Skills/session-closure/references/file-classification.md` | 109 | 0 |  |
| `01_Skills/session-closure/references/sync-coupling.md` | 98 | 0 |  |
| `01_Skills/session-closure/references/test-scenarios.md` | 145 | 0 |  |
| `01_Skills/xlsx-smoke-test-runner/_fixtures/Satelliten_Monitor_g_sparrate_mapping_drift_config.yaml` | 60 | 0 |  |
| `01_Skills/xlsx-smoke-test-runner/_fixtures/_generate_fixtures.py` | 251 | 0 |  |
| `01_Skills/xlsx-smoke-test-runner/tests/conftest.py` | 10 | 0 |  |
| `01_Skills/xlsx-smoke-test-runner/tests/test_fixtures_integration.py` | 199 | 0 |  |
| `01_Skills/xlsx-smoke-test-runner/tests/test_hook_g.py` | 257 | 0 |  |
| `01_Skills/xlsx-smoke-test-runner/tests/test_verify_wrapper.py` | 111 | 0 |  |
| `01_Skills/xlsx-smoke-test-runner/verify_wrapper.py` | 130 | 0 |  |
| `03_Tools/Output/PORTFOLIO-RISK-2026-04-17.md` | 46 | 0 |  |
| `03_Tools/_arg_utils.py` | 26 | 0 |  |
| `03_Tools/_test_earnings_calendar.py` | 575 | 0 |  |
| `03_Tools/backtest-ready/versions.py` | 12 | 0 | ✓ |
| `03_Tools/earnings_schedule_overrides.yaml` | 43 | 0 | ✓ |
| `03_Tools/finnhub_health.json` | 54 | 0 |  |
| `03_Tools/para18_sync/__init__.py` | 0 | 0 |  |
| `03_Tools/precommit/_fixtures/_generate_fixtures.py` | 195 | 0 |  |
| `03_Tools/precommit/_smoke_test.py` | 90 | 0 |  |
| `03_Tools/precommit/crlf_guard.py` | 49 | 0 |  |
| `03_Tools/precommit/para18_sync_reminder.py` | 120 | 0 |  |
| `03_Tools/precommit/validate_flag_events.py` | 106 | 0 |  |
| `03_Tools/precommit/validate_score_history.py` | 155 | 0 |  |
| `03_Tools/system_audit/__init__.py` | 7 | 0 |  |
| `03_Tools/system_audit/audit_types.py` | 44 | 0 |  |
| `03_Tools/system_audit/checks/__init__.py` | 35 | 0 | ✓ |
| `03_Tools/system_audit/checks/cross_source_reverse.py` | 206 | 0 |  |
| `03_Tools/system_audit/checks/existence.py` | 182 | 0 | ✓ |
| `03_Tools/system_audit/checks/jsonl_schema.py` | 142 | 0 |  |
| `03_Tools/system_audit/checks/pipeline_ssot.py` | 104 | 0 |  |
| `03_Tools/system_audit/checks/pointer_completeness.py` | 145 | 0 |  |
| `03_Tools/system_audit/checks/score_event_parity.py` | 293 | 0 | ✓ |
| `03_Tools/system_audit/checks/skill_frontmatter.py` | 121 | 0 | ✓ |
| `03_Tools/system_audit/checks/skill_version.py` | 188 | 0 |  |
| `03_Tools/system_audit/fixtures/cross_source/config.yaml` | 13 | 0 |  |
| `03_Tools/system_audit/fixtures/markdown_header/core_memory_ok.md` | 9 | 0 |  |
| `03_Tools/system_audit/fixtures/markdown_header/faktortabelle_ok.md` | 7 | 0 |  |
| `03_Tools/system_audit/fixtures/markdown_header/state_ok.md` | 4 | 0 |  |
| `03_Tools/system_audit/fixtures/markdown_header/state_stale.md` | 4 | 0 |  |
| `03_Tools/system_audit/fixtures/markdown_header/state_warn.md` | 4 | 0 |  |
| `03_Tools/system_audit/fixtures/markdown_header/system_ok.md` | 11 | 0 |  |
| `03_Tools/system_audit/fixtures/pipeline_ssot/state_broken.md` | 5 | 0 |  |
| `03_Tools/system_audit/fixtures/pipeline_ssot/state_empty.md` | 7 | 0 |  |
| `03_Tools/system_audit/fixtures/pipeline_ssot/state_full.md` | 25 | 0 |  |
| `03_Tools/tests/__init__.py` | 0 | 0 |  |
| `03_Tools/tests/conftest.py` | 40 | 0 |  |
| `03_Tools/tests/fixtures/sample_transcript_normal.md` | 50 | 0 |  |
| `03_Tools/tests/fixtures/sample_transcript_short.md` | 2 | 0 |  |
| `03_Tools/tests/test_atomic_io.py` | 69 | 0 |  |
| `03_Tools/tests/test_defeatbeta_subprocess.py` | 57 | 0 |  |
| `03_Tools/tests/test_finnhub_metrics_guardrail.py` | 106 | 0 |  |
| `03_Tools/tests/test_finnhub_persistence_assertion.py` | 40 | 0 |  |
| `03_Tools/tests/test_numeric_utils.py` | 67 | 0 |  |

