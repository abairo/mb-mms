from django.conf import settings
import httpx


def get_candles(pair: str, start_date: int, end_date: int):
    URL = settings.CANDLE_MB_URL.format(pair=pair,
                                        ts_from=start_date,
                                        ts_to=end_date)

    response = httpx.get(URL).json()

    return response['candles']