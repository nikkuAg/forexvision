from datetime import datetime

from forex_backend.constants import CURRENCIES_QUOTE, PERIODS, PERIODS_DELTAS


def convert_string_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def convert_to_date(string):
    try:
        return datetime.strptime(string, "%b %d, %Y")
    except ValueError:
        raise ValueError("Incorrect data format, should be MMM DD, YYYY")


def validate_date_range(start_date, end_date):
    try:
        start_date = convert_string_to_date(start_date)
        end_date = convert_string_to_date(end_date)
    except Exception as e:
        raise Exception(e)
    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date")

    return start_date, end_date


def validate_period(period):
    if period not in PERIODS:
        raise ValueError("Invalid Period")


def convert_period_to_date_range(period):
    try:
        validate_period(period)
        now = datetime.now()
        start_date = now - PERIODS_DELTAS[period]
        return start_date, now
    except Exception as e:
        raise Exception(e)


def validate_quote(quote):
    if quote not in CURRENCIES_QUOTE:
        raise ValueError("Invalid Quote")

    return quote
