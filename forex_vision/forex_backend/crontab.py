from forex_backend.constants import (ONE_MONTH, ONE_WEEK, ONE_YEAR, SIX_MONTH,
                                     THREE_MONTH)
from forex_backend.utils import sync_database


def sync_exchange_rate_weekly():
    sync_database(ONE_WEEK)


def sync_exchange_rate_monthly():
    sync_database(ONE_MONTH)


def sync_exchange_rate_quarterly():
    sync_database(THREE_MONTH)


def sync_exchange_rate_half_yearly():
    sync_database(SIX_MONTH)


def sync_exchange_rate_yearly():
    sync_database(ONE_YEAR)
