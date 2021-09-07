from datetime import date, timedelta
import datetime
import pytz


def timestamp_to_datetime(ts):
    return datetime.datetime.fromtimestamp(ts)


def datetime_to_timestamp(date):
    return int(datetime.datetime.timestamp(date))

def today():
    return datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))


def today_ts():
    return datetime_to_timestamp(today())


def yesterday():
    today = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
    return today - timedelta(days=1)

def yesterday_ts():
    return datetime_to_timestamp(yesterday())


def subtract_days(date, days):
    return date - datetime.timedelta(days=days)


def date_to_datetime(date, max_datetime: bool):
    if max_datetime:
        return datetime.datetime.combine(date.today(), datetime.datetime.max.time())

    return datetime.datetime.combine(date.today(), datetime.datetime.min.time())


def get_missing_dates(list_dates, start_date, end_date):
    date_set = set(list_dates[0] + timedelta(x) for x in range((list_dates[-1] - list_dates[0]).days))
    missing_dates = sorted(date_set - set(list_dates))

    return missing_dates
