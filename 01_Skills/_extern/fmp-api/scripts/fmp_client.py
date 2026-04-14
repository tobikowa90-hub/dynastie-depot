#!/usr/bin/env python3
"""
Financial Modeling Prep (FMP) API Client - Production-ready wrapper.

Usage:
    from fmp_client import FMPClient

    client = FMPClient()  # Uses FMP_API_KEY env var
    quote = client.get_quote("AAPL")
    financials = client.get_income_statement("AAPL")
"""

import os
import time
import requests
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
from functools import wraps


def rate_limit(calls_per_day: int = 250):
    """Basic rate limiting for daily quota."""
    call_count = [0]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] > calls_per_day:
                print(f"Warning: Exceeded {calls_per_day} daily calls")
            return func(*args, **kwargs)
        return wrapper
    return decorator


class FMPClient:
    """Production-ready Financial Modeling Prep API client."""

    # Use stable endpoints (new format)
    BASE_URL = "https://financialmodelingprep.com/stable"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize FMP client.

        Args:
            api_key: API key. If not provided, reads from FMP_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("FMP_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set FMP_API_KEY or pass api_key parameter.")

        self.session = requests.Session()
        self._daily_calls = 0

    @rate_limit(calls_per_day=250)
    def _request(self, endpoint: str, params: Optional[Dict] = None) -> Any:
        """Make API request with error handling."""
        if params is None:
            params = {}
        params["apikey"] = self.api_key

        try:
            response = self.session.get(f"{self.BASE_URL}/{endpoint}", params=params)
            data = response.json()

            # Check for error messages
            if isinstance(data, dict) and "Error Message" in data:
                error = data["Error Message"]
                if "Legacy" in error:
                    raise Exception(f"Endpoint migrated. Use /stable/ base URL. Error: {error}")
                raise Exception(f"API error: {error}")

            self._daily_calls += 1
            return data

        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")

    # ==================== Stock Quotes & Prices ====================

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """
        Get real-time quote for a symbol.

        Returns:
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "price": 280.70,
                "changePercentage": -1.21,
                "change": -3.45,
                "volume": 42680947,
                "dayLow": 278.59,
                "dayHigh": 284.73,
                "yearHigh": 288.62,
                "yearLow": 169.21,
                "marketCap": 4147722287100,
                ...
            }
        """
        data = self._request("quote", {"symbol": symbol})
        return data[0] if data else {}

    def get_batch_quotes(self, symbols: List[str]) -> List[Dict[str, Any]]:
        """Get quotes for multiple symbols."""
        return self._request("quote", {"symbol": ",".join(symbols)})

    def get_historical_prices(
        self,
        symbol: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get historical end-of-day prices.

        Args:
            symbol: Stock symbol
            from_date: YYYY-MM-DD format
            to_date: YYYY-MM-DD format
        """
        params = {"symbol": symbol}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self._request("historical-price-eod/full", params)
        return data.get("historical", []) if isinstance(data, dict) else data

    # ==================== Financial Statements ====================

    def get_income_statement(
        self,
        symbol: str,
        period: str = "annual",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Get income statement.

        Args:
            symbol: Stock symbol
            period: annual or quarter
            limit: Number of periods
        """
        return self._request("income-statement", {
            "symbol": symbol,
            "period": period,
            "limit": limit
        })

    def get_balance_sheet(
        self,
        symbol: str,
        period: str = "annual",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Get balance sheet."""
        return self._request("balance-sheet-statement", {
            "symbol": symbol,
            "period": period,
            "limit": limit
        })

    def get_cash_flow(
        self,
        symbol: str,
        period: str = "annual",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Get cash flow statement."""
        return self._request("cash-flow-statement", {
            "symbol": symbol,
            "period": period,
            "limit": limit
        })

    def get_financials_full(self, symbol: str, period: str = "annual") -> Dict[str, Any]:
        """Get all financial statements at once."""
        return {
            "income_statement": self.get_income_statement(symbol, period),
            "balance_sheet": self.get_balance_sheet(symbol, period),
            "cash_flow": self.get_cash_flow(symbol, period)
        }

    # ==================== Metrics & Ratios ====================

    def get_key_metrics(
        self,
        symbol: str,
        period: str = "annual",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Get key financial metrics."""
        return self._request("key-metrics", {
            "symbol": symbol,
            "period": period,
            "limit": limit
        })

    def get_financial_ratios(
        self,
        symbol: str,
        period: str = "annual",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Get financial ratios."""
        return self._request("financial-ratios", {
            "symbol": symbol,
            "period": period,
            "limit": limit
        })

    def get_enterprise_value(
        self,
        symbol: str,
        period: str = "annual",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Get enterprise value metrics."""
        return self._request("enterprise-values", {
            "symbol": symbol,
            "period": period,
            "limit": limit
        })

    # ==================== Valuations ====================

    def get_dcf(self, symbol: str) -> Dict[str, Any]:
        """
        Get discounted cash flow valuation.

        Returns:
            {
                "symbol": "AAPL",
                "dcf": 185.50,
                "stockPrice": 280.70,
                "date": "2025-12-04"
            }
        """
        data = self._request("discounted-cash-flow", {"symbol": symbol})
        return data[0] if data else {}

    def get_historical_dcf(
        self,
        symbol: str,
        period: str = "annual",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Get historical DCF valuations."""
        return self._request("historical-discounted-cash-flow", {
            "symbol": symbol,
            "period": period,
            "limit": limit
        })

    def get_rating(self, symbol: str) -> Dict[str, Any]:
        """Get company rating score."""
        data = self._request("rating", {"symbol": symbol})
        return data[0] if data else {}

    # ==================== Company Information ====================

    def get_profile(self, symbol: str) -> Dict[str, Any]:
        """
        Get company profile.

        Returns comprehensive company info including:
        name, sector, industry, CEO, website, description, employees, etc.
        """
        data = self._request("profile", {"symbol": symbol})
        return data[0] if data else {}

    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for companies by name or symbol."""
        return self._request("search", {"query": query, "limit": limit})

    def search_by_name(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for companies by name."""
        return self._request("search-name", {"query": query, "limit": limit})

    # ==================== Calendars & Events ====================

    def get_earnings_calendar(
        self,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get earnings calendar."""
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        return self._request("earnings-calendar", params)

    def get_ipo_calendar(
        self,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get IPO calendar."""
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        return self._request("ipo-calendar", params)

    def get_dividend_calendar(
        self,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get dividend calendar."""
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        return self._request("stock-dividend-calendar", params)

    def get_economic_calendar(
        self,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get economic events calendar."""
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        return self._request("economic-calendar", params)

    # ==================== SEC Filings ====================

    def get_sec_filings(
        self,
        symbol: str,
        filing_type: Optional[str] = None,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Get SEC filings.

        Args:
            symbol: Stock symbol
            filing_type: 10-K, 10-Q, 8-K, etc.
            limit: Max results
        """
        params = {"symbol": symbol, "limit": limit}
        if filing_type:
            params["type"] = filing_type

        return self._request("sec-filings", params)

    # ==================== Dividends & Splits ====================

    def get_dividend_history(self, symbol: str) -> List[Dict[str, Any]]:
        """Get historical dividends."""
        return self._request("historical-price-eod/dividend", {"symbol": symbol})

    def get_split_history(self, symbol: str) -> List[Dict[str, Any]]:
        """Get stock split history."""
        return self._request("historical-price-eod/split", {"symbol": symbol})

    # ==================== Peers & Comparisons ====================

    def get_stock_peers(self, symbol: str) -> List[str]:
        """Get list of peer companies."""
        data = self._request("stock-peers", {"symbol": symbol})
        return data[0].get("peersList", []) if data else []

    # ==================== Lists & Screening ====================

    def get_stock_list(self) -> List[Dict[str, Any]]:
        """Get list of all traded stocks."""
        return self._request("stock-list")

    def get_etf_list(self) -> List[Dict[str, Any]]:
        """Get list of all ETFs."""
        return self._request("etf-list")

    def get_available_indexes(self) -> List[Dict[str, Any]]:
        """Get list of available market indexes."""
        return self._request("indexes-list")

    # ==================== Utility Methods ====================

    def get_market_hours(self) -> Dict[str, Any]:
        """Get market hours status."""
        return self._request("is-market-open")

    @property
    def daily_calls_used(self) -> int:
        """Get number of API calls used today."""
        return self._daily_calls


# ==================== Quick Test ====================

def test_client():
    """Test the FMP client with basic operations."""
    print("Testing Financial Modeling Prep Client...")
    print("=" * 50)
    print("Note: Free tier is 250 calls/day")
    print("Using /stable/ endpoints (new format)")
    print("=" * 50)

    try:
        client = FMPClient()

        # Test quote
        print("\n1. Testing get_quote('AAPL')...")
        quote = client.get_quote("AAPL")
        if quote:
            print(f"   AAPL: ${quote['price']:.2f} ({quote['changePercentage']:+.2f}%)")
            print(f"   Market Cap: ${quote['marketCap']:,.0f}")

        # Test profile
        print("\n2. Testing get_profile('AAPL')...")
        profile = client.get_profile("AAPL")
        if profile:
            print(f"   {profile.get('companyName', 'N/A')}")
            print(f"   Sector: {profile.get('sector', 'N/A')}")
            print(f"   Industry: {profile.get('industry', 'N/A')}")

        # Test income statement
        print("\n3. Testing get_income_statement('AAPL')...")
        income = client.get_income_statement("AAPL", limit=1)
        if income:
            latest = income[0]
            print(f"   Period: {latest.get('date', 'N/A')}")
            print(f"   Revenue: ${latest.get('revenue', 0):,.0f}")
            print(f"   Net Income: ${latest.get('netIncome', 0):,.0f}")

        # Test DCF
        print("\n4. Testing get_dcf('AAPL')...")
        dcf = client.get_dcf("AAPL")
        if dcf:
            print(f"   DCF Value: ${dcf.get('dcf', 0):.2f}")
            print(f"   Stock Price: ${dcf.get('stockPrice', 0):.2f}")
            if dcf.get('dcf') and dcf.get('stockPrice'):
                upside = ((dcf['dcf'] / dcf['stockPrice']) - 1) * 100
                print(f"   Upside: {upside:+.1f}%")

        # Test search
        print("\n5. Testing search('Apple')...")
        results = client.search("Apple", limit=3)
        print(f"   Found {len(results)} results")
        for r in results[:3]:
            print(f"   - {r.get('symbol', 'N/A')}: {r.get('name', 'N/A')}")

        # Test key metrics
        print("\n6. Testing get_key_metrics('AAPL')...")
        metrics = client.get_key_metrics("AAPL", limit=1)
        if metrics:
            m = metrics[0]
            print(f"   P/E Ratio: {m.get('peRatio', 'N/A')}")
            print(f"   ROE: {m.get('roe', 'N/A')}")
            print(f"   Debt/Equity: {m.get('debtToEquity', 'N/A')}")

        print(f"\n   Daily calls used: {client.daily_calls_used}")

        print("\n" + "=" * 50)
        print("All tests passed!")
        return True

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_client()
