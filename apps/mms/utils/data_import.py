from apps.mms.models import MMS
from django.conf import settings
from .date import date_to_timestamp, yesterday_ts, subtract_days, timestamp_to_date
import httpx
from functools import reduce


def get_candles(pair: str, start_date: int, end_date: int):
    start_date = start_date
    end_date = end_date
    URL = settings.CANDLE_MB_URL.format(pair=pair,
                                        ts_from=start_date,
                                        ts_to=end_date)

    response = httpx.get(URL).json()

    return response['candles']


add_candle = lambda x, y: x + y['close']


def mms_average(candles, arr_slice, quantity):
    return reduce(add_candle, candles[arr_slice], 0) / quantity


def initial_import(pair: str):
    end_date = yesterday_ts()
    start_date = date_to_timestamp(subtract_days(timestamp_to_date(end_date), 565)) # 365 dias mais mms_200 para o primeiro dia
    candles = get_candles(pair, start_date, end_date)

    mms_list = []

    for index in range(200, len(candles)):
        mms_list.append(
            MMS(pair=pair,
                timestamp=int(candles[index]['timestamp']),
                mms_200=mms_average(candles, slice(index - 200, index), 200),
                mms_50=mms_average(candles, slice(index - 50, index), 50),
                mms_20=mms_average(candles, slice(index - 20, index), 20)
            )
        )

    objs = MMS.objects.bulk_create(mms_list)
    return len(objs)
