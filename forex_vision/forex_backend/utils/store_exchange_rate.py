from forex_backend.constants import CURRENCIES_QUOTE
from forex_backend.models import ExchangeRate
from forex_backend.scrapper import fetch_exchange_data
from forex_backend.utils import convert_period_to_date_range


def store_exchange_rate(quote: str, start_timestamp: int, end_timestamp: int):
    try:
        data = fetch_exchange_data(quote, start_timestamp, end_timestamp)
        for d in data:
            ExchangeRate.objects.update_or_create(
                date=d["date"],
                quote=d["quote"],
                defaults={
                    "open": d["open"],
                    "high": d["high"],
                    "low": d["low"],
                    "close": d["close"],
                },
            )
    except Exception as e:
        raise Exception(e)


def sync_database(period):
    try:
        start_date, end_date = convert_period_to_date_range(period)
        for quote in CURRENCIES_QUOTE:
            print(
                f"Syncing data for {quote} for period {period} from {start_date} to {end_date}"
            )
            store_exchange_rate(quote, start_date, end_date)
    except Exception as e:
        raise Exception(e)
