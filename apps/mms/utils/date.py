import datetime
import pytz


def timestamp_to_date(ts):
    return datetime.datetime.fromtimestamp(ts)


def date_to_timestamp(date):
    return int(datetime.datetime.timestamp(date))

def today():
    return datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))


def today_ts():
    return date_to_timestamp(today())


def yesterday():
    today = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
    return today - datetime.timedelta(days=1)

def yesterday_ts():
    return date_to_timestamp(yesterday())


def subtract_days(date, days):
    return date - datetime.timedelta(days=days)
