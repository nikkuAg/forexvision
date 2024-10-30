from datetime import timedelta

YAHOO_FINANACE_QUOTE_URL = "https://finance.yahoo.com/quote/"

CURRENCIES_QUOTE = [
    "EURUSD",
    "GBPUSD",
    "INRUSD",
    "GBPINR",
    "AEDINR",
]

CURRENCIES_QUOTE_CHOICES = (
    ("EURUSD", "Euro to US Dollar"),
    ("GBPUSD", "British Pound to US Dollar"),
    ("INRUSD", "Indian Rupee to US Dollar"),
    ("GBPINR", "British Pound to Indian Rupee"),
    ("AEDINR", "UAE Dirham to Indian Rupee"),
)

ONE_WEEK = "1W"
ONE_MONTH = "1M"
THREE_MONTH = "3M"
SIX_MONTH = "6M"
ONE_YEAR = "1Y"

PERIODS = [ONE_WEEK, ONE_MONTH, THREE_MONTH, SIX_MONTH, ONE_YEAR]

PERIODS_DELTAS = {
    ONE_WEEK: timedelta(days=7),
    ONE_MONTH: timedelta(days=30),
    THREE_MONTH: timedelta(days=90),
    SIX_MONTH: timedelta(days=180),
    ONE_YEAR: timedelta(days=365),
}
