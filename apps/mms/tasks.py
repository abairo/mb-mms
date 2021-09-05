from mercadobitcoin.celery import app
from time import sleep
from celery import shared_task


@shared_task(bind=False)
def check_missing_days():
    pass


@shared_task(bind=False)
def create_mms(date):
    pass


@shared_task(bind=False)
def import_yesterday():
    pass
