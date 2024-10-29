import requests
from bs4 import BeautifulSoup
from forex_backend.constants import YAHOO_FINANACE_QUOTE_URL


def fetch_exchange_data(quote: str, start_timestamp: int, end_timestamp: int) -> list:
    """Fetch exchange data from Yahoo Finance"""
    try:
        url = f"{YAHOO_FINANACE_QUOTE_URL}{quote}/history/?period1={start_timestamp}&period2={end_timestamp}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3",
            "Accept": "text/html",
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Error fetching exchange data {quote}: {response.status_code}"
            )
        soup = BeautifulSoup(response.text, "html.parser")

        data = []
        for row in soup.select("table tbody tr"):
            columns = row.find_all("td")
            if len(columns) >= 5:
                date = columns[0].text.strip()
                open_price = columns[1].text.strip()
                high_price = columns[2].text.strip()
                low_price = columns[3].text.strip()
                close_price = columns[4].text.strip()
                data.append(
                    {
                        "date": date,
                        "open": open_price,
                        "high": high_price,
                        "low": low_price,
                        "close": close_price,
                    }
                )

        return data
    except Exception as e:
        print(f"Error fetching exchange data {quote}: {e}")
        return []
