---
title: "Faktortabelle — Snapshot-First Architektur"
type: concept
tags: [token-effizienz, defcon, datenbasis, snapshot-first]
related: "[[insider-intelligence]], [[Context-Hygiene]], [[Update-Klassen-DEFCON]], [[Context-Hygiene-Code]], [[Token-Mechanik]], [[ASML]], [[AVGO]], [[MSFT]], [[RMS]], [[VEEV]], [[SU]], [[BRKB]], [[V]], [[TMO]], [[APH]], [[COST]]"
defcon_block: "System-Datenbasis"
operative_regel: "Faktortabelle vor API-Abfragen lesen — spart ~60-70% Token-Kosten pro Session."
---

# Faktortabelle — Snapshot-First Architektur

## Zweck

Die Faktortabelle (`00_Core/Faktortabelle.md`) ist ein kompakter Snapshot aller 11 Satelliten-Scores, FLAGs, Fundamentaldaten und Termine. Sie reduziert den Token-Verbrauch pro Session um ~60-70%, weil Claude den aktuellen Depot-State aus einer einzigen Datei laden kann, statt config.yaml + Shibui + defeatbeta einzeln abzufragen.

## Datenhierarchie

```
config.yaml (Primärquelle — hat immer Vorrang)
     ↓
Faktortabelle.md (Snapshot — 4. Pflicht-Lektüre)
     ↓
MCP-APIs (on-demand — nur wenn Tabelle veraltet)
```

**Regel:** Bei Datenkonflikt zwischen Faktortabelle und config.yaml → config.yaml gewinnt immer. Die Faktortabelle ist eine Convenience-Kopie, keine autoritative Quelle.

## Kommentar-Anker-Format

Die Haupttabelle verwendet `<!-- DATA:TICKER -->` Anker vor jeder Zeile:
```
<!-- DATA:AVGO -->
| AVGO | ~30% | >20% | ... | 86 | 🟢 4 | 🔴 CEO-Selling ~$51M | ... |
<!-- END_TABLE -->
```
→ Ermöglicht automatisches Update via `insider_intel.py --update-faktortabelle`

## Update-Klassen (Referenz: [[Update-Klassen-DEFCON]])

| Klasse | Faktortabelle-Aktion |
|--------|---------------------|
| A (Quartalsweise) | FCF, ROIC, GM, Debt/EBITDA aktualisieren |
| B (Earnings) | Alle Spalten nach Earnings-Analyse aktualisieren |
| C (Event/sofort) | FLAG-Spalte sofort via `--update-faktortabelle` |
| D (Monatlich) | Nicht in Faktortabelle (Sentiment = API-only) |

## 90-Tage-Veralterungsregel

- `score_datum` > 90 Tage → 🟡 veraltet markieren
- `score_datum` > 180 Tage → QuickCheck erzwingt Re-Analyse
- Bei Veralterung: Shibui/defeatbeta direkt abfragen, nicht Faktortabelle vertrauen

## Schnittstelle Insider-Intelligence

```bash
# FLAG-Update nach Scan
python insider_intel.py flag-check --update-faktortabelle

# 3-Wege-Vergleich (config.yaml + Faktortabelle + Live)
python insider_intel.py factor-sync
```

**Wichtig:** `--update-faktortabelle` aktualisiert nur die Faktortabelle, **nie** config.yaml. Config.yaml wird immer manuell synchronisiert.

## Drei Arbeitsbereiche

| Modus | Faktortabelle-Nutzung |
|-------|----------------------|
| **Chat** | Snapshot-First: Faktortabelle lesen → Shibui-Abfragen reduzieren |
| **Cowork** | Beim Session-Start laden → sofort Depot-Überblick |
| **Code** | `--update-faktortabelle` nach jedem Insider-Scan |

## Backlinks

### Satelliten
[[ASML]] · [[AVGO]] · [[MSFT]] · [[RMS]] · [[VEEV]] · [[SU]] · [[BRKB]] · [[V]] · [[TMO]] · [[APH]] · [[COST]]

### System-Konzepte
- [[Context-Hygiene]] — On-demand-Loading-Prinzip
- [[Context-Hygiene-Code]] — Claude Code Optimierungen (autoCompact, Tool Search)
- [[Token-Mechanik]] — Token-Kostenstruktur
- [[Update-Klassen-DEFCON]] — A/B/C/D Klassen
- [[insider-intelligence]] — Automatisiertes FLAG-Update
- [[Wissenschaftliche-Fundierung-DEFCON]] — Datenhierarchie (B7)
