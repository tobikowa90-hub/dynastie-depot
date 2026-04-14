# Financial Modeling Prep API - Complete Endpoint Reference

## Base URL (New Format)
```
https://financialmodelingprep.com/stable
```

**IMPORTANT:** Legacy `/api/v3/` endpoints no longer work for new accounts. Use `/stable/` base URL.

## Authentication
```bash
# Query parameter only
?apikey=your_api_key
```

## Stock Quotes & Prices

### GET /quote
Real-time quote.
```
Params: symbol (required), can be comma-separated
Returns: [{symbol, name, price, changePercentage, change, volume, dayLow, dayHigh, yearHigh, yearLow, marketCap, priceAvg50, priceAvg200, exchange, open, previousClose, timestamp}]
Free: ✅
```

### GET /quote-short
Quick price only.
```
Params: symbol
Returns: [{symbol, price, volume}]
Free: ✅
```

### GET /historical-price-eod/full
Historical end-of-day prices.
```
Params: symbol, from (YYYY-MM-DD), to (YYYY-MM-DD)
Returns: {symbol, historical: [{date, open, high, low, close, adjClose, volume, unadjustedVolume, change, changePercent, vwap, label, changeOverTime}]}
Free: ✅
```

### GET /historical-price-intraday
Intraday prices.
```
Params: symbol, interval (1min|5min|15min|30min|1hour|4hour)
Free: 💎 Paid only
```

### GET /pre-post-market-quote
Extended hours quotes.
```
Free: 💎 Paid only
```

## Financial Statements

### GET /income-statement
Income statement.
```
Params: symbol, period (annual|quarter), limit
Returns: [{date, symbol, reportedCurrency, cik, filingDate, acceptedDate, fiscalYear, period, revenue, costOfRevenue, grossProfit, grossProfitRatio, researchAndDevelopmentExpenses, generalAndAdministrativeExpenses, sellingAndMarketingExpenses, sellingGeneralAndAdministrativeExpenses, otherExpenses, operatingExpenses, costAndExpenses, interestIncome, interestExpense, depreciationAndAmortization, ebitda, ebitdaratio, operatingIncome, operatingIncomeRatio, totalOtherIncomeExpensesNet, incomeBeforeTax, incomeBeforeTaxRatio, incomeTaxExpense, netIncome, netIncomeRatio, eps, epsdiluted, weightedAverageShsOut, weightedAverageShsOutDil, link, finalLink}]
Free: ✅
```

### GET /balance-sheet-statement
Balance sheet.
```
Params: symbol, period, limit
Returns: [{date, symbol, reportedCurrency, cik, filingDate, acceptedDate, fiscalYear, period, cashAndCashEquivalents, shortTermInvestments, cashAndShortTermInvestments, netReceivables, inventory, otherCurrentAssets, totalCurrentAssets, propertyPlantEquipmentNet, goodwill, intangibleAssets, goodwillAndIntangibleAssets, longTermInvestments, taxAssets, otherNonCurrentAssets, totalNonCurrentAssets, otherAssets, totalAssets, accountPayables, shortTermDebt, taxPayables, deferredRevenue, otherCurrentLiabilities, totalCurrentLiabilities, longTermDebt, deferredRevenueNonCurrent, deferredTaxLiabilitiesNonCurrent, otherNonCurrentLiabilities, totalNonCurrentLiabilities, otherLiabilities, capitalLeaseObligations, totalLiabilities, preferredStock, commonStock, retainedEarnings, accumulatedOtherComprehensiveIncomeLoss, othertotalStockholdersEquity, totalStockholdersEquity, totalEquity, totalLiabilitiesAndStockholdersEquity, minorityInterest, totalLiabilitiesAndTotalEquity, totalInvestments, totalDebt, netDebt, link, finalLink}]
Free: ✅
```

### GET /cash-flow-statement
Cash flow statement.
```
Params: symbol, period, limit
Returns: [{date, symbol, reportedCurrency, cik, filingDate, acceptedDate, fiscalYear, period, netIncome, depreciationAndAmortization, deferredIncomeTax, stockBasedCompensation, changeInWorkingCapital, accountsReceivables, inventory, accountsPayables, otherWorkingCapital, otherNonCashItems, netCashProvidedByOperatingActivities, investmentsInPropertyPlantAndEquipment, acquisitionsNet, purchasesOfInvestments, salesMaturitiesOfInvestments, otherInvestingActivites, netCashUsedForInvestingActivites, debtRepayment, commonStockIssued, commonStockRepurchased, dividendsPaid, otherFinancingActivites, netCashUsedProvidedByFinancingActivities, effectOfForexChangesOnCash, netChangeInCash, cashAtEndOfPeriod, cashAtBeginningOfPeriod, operatingCashFlow, capitalExpenditure, freeCashFlow, link, finalLink}]
Free: ✅
```

### GET /income-statement-growth
Income statement growth rates.
```
Params: symbol, period, limit
Free: ✅
```

## Metrics & Ratios

### GET /key-metrics
Key financial metrics.
```
Params: symbol, period, limit
Returns: [{symbol, date, period, revenuePerShare, netIncomePerShare, operatingCashFlowPerShare, freeCashFlowPerShare, cashPerShare, bookValuePerShare, tangibleBookValuePerShare, shareholdersEquityPerShare, interestDebtPerShare, marketCap, enterpriseValue, peRatio, priceToSalesRatio, pocfratio, pfcfRatio, pbRatio, ptbRatio, evToSales, enterpriseValueOverEBITDA, evToOperatingCashFlow, evToFreeCashFlow, earningsYield, freeCashFlowYield, debtToEquity, debtToAssets, netDebtToEBITDA, currentRatio, interestCoverage, incomeQuality, dividendYield, payoutRatio, salesGeneralAndAdministrativeToRevenue, researchAndDevelopmentToRevenue, intangiblesToTotalAssets, capexToOperatingCashFlow, capexToRevenue, capexToDepreciation, stockBasedCompensationToRevenue, grahamNumber, roic, returnOnTangibleAssets, grahamNetNet, workingCapital, tangibleAssetValue, netCurrentAssetValue, investedCapital, averageReceivables, averagePayables, averageInventory, daysSalesOutstanding, daysPayablesOutstanding, daysOfInventoryOnHand, receivablesTurnover, payablesTurnover, inventoryTurnover, roe, capexPerShare}]
Free: ✅
```

### GET /financial-ratios
Financial ratios.
```
Params: symbol, period, limit
Returns: [{symbol, date, period, currentRatio, quickRatio, cashRatio, daysOfSalesOutstanding, daysOfInventoryOutstanding, operatingCycle, daysOfPayablesOutstanding, cashConversionCycle, grossProfitMargin, operatingProfitMargin, pretaxProfitMargin, netProfitMargin, effectiveTaxRate, returnOnAssets, returnOnEquity, returnOnCapitalEmployed, netIncomePerEBT, ebtPerEbit, ebitPerRevenue, debtRatio, debtEquityRatio, longTermDebtToCapitalization, totalDebtToCapitalization, interestCoverage, cashFlowToDebtRatio, companyEquityMultiplier, receivablesTurnover, payablesTurnover, inventoryTurnover, fixedAssetTurnover, assetTurnover, operatingCashFlowPerShare, freeCashFlowPerShare, cashPerShare, payoutRatio, operatingCashFlowSalesRatio, freeCashFlowOperatingCashFlowRatio, cashFlowCoverageRatios, shortTermCoverageRatios, capitalExpenditureCoverageRatio, dividendPaidAndCapexCoverageRatio, dividendPayoutRatio, priceBookValueRatio, priceToBookRatio, priceToSalesRatio, priceEarningsRatio, priceToFreeCashFlowsRatio, priceToOperatingCashFlowsRatio, priceCashFlowRatio, priceEarningsToGrowthRatio, priceSalesRatio, dividendYield, enterpriseValueMultiple, priceFairValue}]
Free: ✅
```

### GET /enterprise-values
Enterprise value.
```
Params: symbol, period, limit
Free: ✅
```

## Valuations

### GET /discounted-cash-flow
DCF valuation.
```
Params: symbol
Returns: [{symbol, date, dcf, stockPrice}]
Free: ✅
```

### GET /historical-discounted-cash-flow
Historical DCF.
```
Params: symbol, period, limit
Free: ✅
```

### GET /rating
Company rating.
```
Params: symbol
Returns: [{symbol, date, rating, ratingScore, ratingRecommendation, ratingDetailsDCFScore, ratingDetailsDCFRecommendation, ratingDetailsROEScore, ratingDetailsROERecommendation, ratingDetailsROAScore, ratingDetailsROARecommendation, ratingDetailsDEScore, ratingDetailsDERecommendation, ratingDetailsPEScore, ratingDetailsPERecommendation, ratingDetailsPBScore, ratingDetailsPBRecommendation}]
Free: ✅
```

### GET /historical-rating
Rating history.
```
Params: symbol, limit
Free: ✅
```

## Company Information

### GET /profile
Company profile.
```
Params: symbol
Returns: [{symbol, price, beta, volAvg, mktCap, lastDiv, range, changes, companyName, currency, cik, isin, cusip, exchange, exchangeShortName, industry, website, description, ceo, sector, country, fullTimeEmployees, phone, address, city, state, zip, dcfDiff, dcf, image, ipoDate, defaultImage, isEtf, isActivelyTrading, isAdr, isFund}]
Free: ✅
```

### GET /search
Search companies.
```
Params: query, limit
Returns: [{symbol, name, currency, stockExchange, exchangeShortName}]
Free: ⚠️ Limited results on free tier
```

### GET /search-name
Search by company name.
```
Params: query, limit
Free: ⚠️ Limited results on free tier
```

### GET /stock-peers
Peer companies.
```
Params: symbol
Returns: [{symbol, peersList: []}]
Free: ✅
```

## Calendars & Events

### GET /earnings-calendar
Earnings calendar.
```
Params: from, to
Returns: [{date, symbol, eps, epsEstimated, time, revenue, revenueEstimated, updatedFromDate, fiscalDateEnding}]
Free: ✅
```

### GET /ipo-calendar
IPO calendar.
```
Params: from, to
Free: ✅
```

### GET /stock-dividend-calendar
Dividend calendar.
```
Params: from, to
Free: ✅
```

### GET /stock-split-calendar
Split calendar.
```
Params: from, to
Free: ✅
```

### GET /economic-calendar
Economic events.
```
Params: from, to
Free: ✅
```

## SEC Filings

### GET /sec-filings
SEC filings list.
```
Params: symbol, type (10-K|10-Q|8-K|etc.), limit
Returns: [{symbol, cik, type, link, finalLink, acceptedDate, fillingDate}]
Free: ✅
```

### GET /rss-feed-sec-filings
SEC RSS feed.
```
Params: type, limit
Free: ✅
```

## Dividends & Splits

### GET /historical-price-eod/dividend
Dividend history.
```
Params: symbol
Free: ✅
```

### GET /historical-price-eod/split
Split history.
```
Params: symbol
Free: ✅
```

## Lists & Reference

### GET /stock-list
All tradeable stocks.
```
Free: ✅
```

### GET /etf-list
All ETFs.
```
Free: ✅
```

### GET /indexes-list
Market indexes.
```
Free: ✅
```

### GET /is-market-open
Market status.
```
Free: ✅
```

## Premium Endpoints (Paid Only)

### Institutional & Insider Data
```
GET /institutional-holder - Institutional holders
GET /mutual-fund-holder - Mutual fund holders
GET /insider-trading - Insider transactions
GET /form-13f - 13F filings (💎 Premium+)
GET /senate-trading - Senate trades (💎 Ultimate)
GET /house-trading - House trades (💎 Ultimate)
```

### Advanced Data
```
GET /stock-screener - Stock screening (💎 Starter+)
GET /analyst-estimates - Analyst estimates (💎 Premium+)
GET /earnings-surprises - Earnings surprises
GET /earnings-transcript - Earnings transcripts (💎 Ultimate)
```

### Real-Time Data
```
GET /historical-price-intraday - Intraday data (💎 Starter+)
GET /pre-post-market-quote - Extended hours (💎 Premium+)
```

## WebSocket (Premium+)

### URL
```
wss://websockets.financialmodelingprep.com
```

### Message Format
```json
{
  "event": "subscribe",
  "payload": {
    "symbols": ["AAPL", "MSFT"]
  }
}
```

## Rate Limits

| Tier | Calls/Day | Calls/Min | Symbols |
|------|-----------|-----------|---------|
| Free | 250 | N/A | ~100 sample |
| Starter | Unlimited | 300 | US only |
| Premium | Unlimited | 750 | US/UK/Canada |
| Ultimate | Unlimited | 3,000 | Global |

## Free Tier Symbol Limitations

Free tier is limited to approximately 100 sample symbols including:
AAPL, TSLA, AMZN, GOOGL, MSFT, META, NVDA, and ~90 others.

## Error Responses

```json
{
  "Error Message": "Error description..."
}
```

Common errors:
- "Legacy Endpoint" - Use /stable/ base URL
- "Invalid API KEY" - Check API key
- "Limit Reach" - Daily limit exceeded
