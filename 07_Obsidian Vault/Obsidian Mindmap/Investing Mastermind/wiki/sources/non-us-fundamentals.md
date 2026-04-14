---
tags: [skill, tool, non-us, yfinance, ifrs, fundamentals, asml, rms, su]
status: aktiv
version: "1.1"
stand: 2026-04-06
---

# Non-US Fundamentals Module — yfinance für ASML / RMS / SU

> Automatisierte DEFCON-Fundamentaldaten für die 3 europäischen Satelliten via Yahoo Finance (yfinance). Schließt die Shibui/defeatbeta-Lücke für Non-US-Ticker. Kein API-Key nötig. EUR-Kurse, IFRS-Daten, vollständiger DEFCON-Block.

## Non-US Satelliten

| Ticker | yfinance Symbol | Börse | Berichtsfrequenz | Ersatz |
|--------|----------------|-------|-----------------|--------|
| [[ASML]] | ASML.AS | Amsterdam (Euronext) | Quarterly (IFRS) | SNPS |
| [[RMS]] | RMS.PA | Paris (Euronext) | Semi-annual H1/H2 | RACE |
| [[SU]] | SU.PA | Paris (Euronext) | Semi-annual H1/H2 | DE |

## API-Routing-Regel (Gesamtsystem)

```
IF Non-US (ASML / RMS / SU)
    → eodhd_intel.py (yfinance — dieses Modul)
    → Insider: AFM / AMF — manuell (kein Form-4)

IF US-Ticker (NYSE / NASDAQ)
    → Shibui SQL + defeatbeta MCP (dieses Modul NICHT verwenden)
    → insider_intel.py (Form 4 / SEC EDGAR)
```

## Befehle

```bash
python eodhd_intel.py scan          # Alle 3 Non-US-Satelliten
python eodhd_intel.py scan ASML     # Einzelner Ticker
python eodhd_intel.py detail RMS    # Vollständiger DEFCON-Block
python eodhd_intel.py prices        # Kurscheck aller 3 + 200MA-Status
```

## Gelieferte DEFCON-Metriken

| Kategorie | Metriken |
|-----------|----------|
| CapEx/OCF | 4-Jahres-Historie, FLAG-Status |
| Bilanz | Net Debt/EBITDA, Goodwill/Assets, Current Ratio |
| Valuation | Fwd P/E, P/FCF, EV/EBITDA, FCF Yield |
| Margen | Gross Margin, FCF-Marge, Net Margin, SBC/Revenue |
| GM-Trend | 3 Jahre — Moat-Drift-Check |
| ROIC-Proxy | EBIT×0.75 / (Assets - Current Liabilities) |
| Technicals | 200MA-Lage, 52W-Distanz, Beta |
| Analysten | Konsensus-Rating, Ø Kursziel, Upside |
| Ownership | Insider %, Institutionen % |

## Bekannte Datenlimitierungen

| Ticker | Problem | Workaround |
|--------|---------|------------|
| RMS | yfinance: FCF = OCF (IFRS-Datenfehler) | TTM-Backrechnung aus `info.freeCashflow` |
| RMS, SU | Semi-annual → stärkerer Daten-Lag | IR-Website für neuesten Bericht prüfen |
| Alle | ROIC nicht direkt verfügbar | Proxy-Formel + GuruFocus Verifikation |

## Strukturelle OCF-Abweichungen (kein Fehler!)

| Ticker | Erwartete Abweichung | Ursache |
|--------|---------------------|---------|
| ASML | ~10–12% (IFRS vs. US GAAP) | IFRS 16: Leasingzahlungen → Finanzierungs-CF |
| RMS | Gering | Nur IFRS, einheitlich |
| SU | Gering | Nur IFRS, einheitlich |

Toleranz: ±1.5% für CapEx, bis ~15% für OCF (IFRS 16-Effekt).

## EODHD-Hinweis

EODHD Free-Tier hat **keinen** Zugriff auf Fundamentals-Endpunkt (403 Forbidden).
→ yfinance ist die kostenlose Alternative mit vollständiger EUR-Ticker-Coverage.

## Verlinkungen

- [[Non-US-Scoring]] — IFRS-Addendum, Scoring-Anpassungen, Datenlücken
- [[DEFCON-System]] — Integration in Analyse-Workflow
- [[ASML]] — Kalibrierungsanker Non-US (12.5% CapEx/OCF, kein FLAG)
- [[RMS]] — Bekannte yfinance-Datenlücke CapEx
- [[SU]] — Bekannte yfinance-Datenlücke CapEx
- [[defeatbeta]] — US-Counterpart für US-Fundamentals
- [[Shibui-SQL]] — US-Counterpart für Technicals
- [[insider-intelligence]] — US-Insider-Modul (Non-US bleibt manuell)
