---
tags: [quelle, sql, technicals, screening]
status: aktiv
---

# Shibui Finance SQL — Primärquelle Technicals

## Was es liefert

- 56+ Technicals (RSI, MACD, Bollinger, Moving Averages etc.)
- Historische Fundamentaldaten (breite Zeitreihen)
- FCF-Konsistenz-Screening über mehrere Jahre
- CapEx-FLAG-Historik (z.B. MSFT Dez-Quartale: 83.6% / 70.9%)

## Coverage-Lücken

- ASML, RMS, SU (Euronext) haben keine primäre Shibui-Coverage
- Non-US → yfinance (via eodhd_intel.py)

## Primäre Use-Cases im DEFCON-System

1. Technicals-Block jeder !Analysiere-Analyse
2. FLAG-Historie quantifizieren (historische CapEx/OCF-Reihen)
3. Screening-Vorfilter (Stufe 0)
4. GM-Trend über 4 Quartale (Moat-Drift-Check)

## Verlinkungen

- [[defeatbeta]] — komplementäre Fundamentals-Quelle
- [[DEFCON-System]]
