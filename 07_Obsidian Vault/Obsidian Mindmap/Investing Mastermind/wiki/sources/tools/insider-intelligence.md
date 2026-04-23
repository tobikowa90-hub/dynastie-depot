---
tags: [skill, tool, insider, form-4, sec, flag, edgar]
status: aktiv
version: "1.0"
stand: 2026-04-06
aliases:
  - "insider-intelligence-skill"

---

# Insider Intelligence Module — Form-4-Automatisierung

> Automatisiertes SEC EDGAR Form-4-Scanning der 8 US-Satelliten. Berechnet DEFCON-Insider-Block (10 Punkte) und erkennt FLAGs automatisch. Kein API-Key nötig.

## Architektur

```
SEC EDGAR API (kostenlos, nur User-Agent nötig)
    → Form 4 XML abrufen + parsen
    → Transaktions-Klassifikation
    → DEFCON Insider-Score (7/10 automatisch)
    → FLAG-Detection (>$20M diskretionär in 90d)
    → Output: DEFCON-ready Markdown-Block
```

## 8 US-Satelliten (CIK-Tabelle)

| Ticker | CIK | Börse |
|--------|-----|-------|
| [[AVGO]] | 0001730168 | NASDAQ |
| [[MSFT]] | 0000789019 | NASDAQ |
| [[V]] | 0001403161 | NYSE |
| [[BRKB\|BRK.B]] | 0001067983 | NYSE |
| [[TMO]] | 0000097745 | NYSE |
| [[VEEV]] | 0001393052 | NYSE |
| [[APH]] | 0000820313 | NYSE |
| [[COST]] | 0000909832 | NASDAQ |

## Transaktions-Klassifikation

| Code | Typ | FLAG-relevant? |
|------|-----|----------------|
| P | Open-Market-Kauf | Nein (positiv) |
| S + 10b5-1 | Plan-Verkauf | Nein |
| S ohne 10b5-1 | **Diskretionärer Verkauf** | **Ja (>$20M = FLAG)** |
| M+S gleicher Tag | Cashless Exercise | Nein |
| M (Preis $0) | RSU-Vesting | Nein |
| A | Grant / Award | Nein |

## Insider-Scoring (10 Punkte)

| Komponente | Max | Automatisiert? | Quelle |
|-----------|-----|---------------|--------|
| Net Buy (6 Monate) | 4 | Ja | SEC EDGAR Form 4 |
| Management Ownership >1% | 3 | Nein | Shibui / GuruFocus |
| Kein diskr. Selling >$20M (90d) | 3 | Ja | SEC EDGAR Form 4 |

## Befehle

```bash
python insider_intel.py scan          # Alle 8 US-Satelliten (~30-45s)
python insider_intel.py scan AVGO     # Einzelner Ticker
python insider_intel.py flag-check    # Nur FLAG-Status aller Satelliten (schnell)
python insider_intel.py detail AVGO   # 12-Monats-Report mit allen Transaktionen
```

## Non-US Insider (bleibt manuell!)

| Ticker | Behörde | URL |
|--------|---------|-----|
| [[ASML]] | AFM (NL) | afm.nl/registers |
| [[RMS]] | AMF (FR) | amf-france.org |
| [[SU]] | AMF (FR) | amf-france.org |

Non-US-Satelliten unterliegen nicht der SEC Form-4-Pflicht.

## Verhältnis zu OpenInsider

- **Dieses Modul:** Automatisierter Scoring-Block (Form 4 direkt von SEC EDGAR)
- **[[OpenInsider]]:** Manueller Pflicht-Gegencheck bei Grenzfällen (Spalte "X"/"M")

## Verlinkungen

- [[CapEx-FLAG]] — FLAG-Logik und Sparraten-Überschreibung
- [[DEFCON-System]] — Insider-Block = 10 Punkte im Score
- [[OpenInsider]] — Pflicht-Gegencheck bei Grenzfällen
- [[Non-US-Scoring]] — Warum Non-US manuell bleibt
- [[Analyse-Pipeline]] — Integration in !Analysiere Workflow
- [[AVGO]] — Kalibrierungsbeispiel: $123M formal FLAG → nach manuellem Check kein FLAG
