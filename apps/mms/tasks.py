from mercadobitcoin.celery import app
from time import sleep
from celery import shared_task
from django.conf import settings
import logging
from .usecases import CheckMissingDates, ImportMMS
from .utils.date import yesterday, datetime_to_timestamp, subtract_days, date_to_datetime


logger = logging.getLogger('MMS')


@shared_task(bind=False)
def check_missing_dates():
    usecase = CheckMissingDates()
    for pair in settings.PAIRS:
        usecase(pair)


@shared_task(bind=False)
def create_mms_from_date(pair: str, ts_from: int, ts_to: int):
    use_case = ImportMMS()
    use_case(pair, ts_from, ts_to)


@shared_task(bind=False)
def import_yesterday():
    dt_yesterday = yesterday().date()

    dt_min = date_to_datetime(dt_yesterday, max_datetime=False)
    dt_max = date_to_datetime(dt_yesterday, max_datetime=True)

    ts_from = datetime_to_timestamp(subtract_days(dt_min, 200))
    ts_to = datetime_to_timestamp(dt_max)
    for pair in settings.PAIRS:
        create_mms_from_date.delay(pair, ts_from, ts_to)
