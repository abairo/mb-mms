from apps.mms.models import MMS
from .date import datetime_to_timestamp, yesterday_ts, subtract_days, timestamp_to_datetime
from functools import reduce
from apps.mms.external_repositories import get_candles


add_candle = lambda x, y: x + y['close']


def mms_average(candles, arr_slice, quantity):
    return reduce(add_candle, candles[arr_slice], 0) / quantity


def initial_import(pair: str):
    end_date = yesterday_ts()
    start_date = datetime_to_timestamp(subtract_days(timestamp_to_datetime(end_date), 565)) # 365 dias mais mms_200 para o primeiro dia
    candles = get_candles(pair, start_date, end_date)

    mms_list = []

    for index in range(200, len(candles)):
        timestamp = int(candles[index]['timestamp'])
        mms_list.append(
            MMS(pair=pair,
                timestamp=timestamp,
                mms_200=mms_average(candles, slice(index - 200, index), 200),
                mms_50=mms_average(candles, slice(index - 50, index), 50),
                mms_20=mms_average(candles, slice(index - 20, index), 20),
                date=timestamp_to_datetime(timestamp)
            )
        )

    objs = MMS.objects.bulk_create(mms_list)
    return len(objs)
