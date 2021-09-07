from apps.mms.external_repositories import get_candles
from apps.mms.utils.data_import import mms_average
from apps.mms.models import MMS
import logging
from django.db.utils import IntegrityError


logger = logging.getLogger('MMS')


class ImportMMS():

    def __call__(self, pair: str, ts_from: int, ts_to: int):
        try:
            candles = get_candles(pair, ts_from, ts_to)

            if candles:
                mms = MMS(
                    pair=pair,
                    timestamp=candles[200]['timestamp'],
                    mms_200=mms_average(candles, slice(0 - 200, 200), 200),
                    mms_50=mms_average(candles, slice(150 - 200, 200), 50),
                    mms_20=mms_average(candles, slice(180 - 200, 200), 20)
                )

                mms.save()

                logger.info(f'MMS importada com sucesso {mms.date}')
                return mms
        except IntegrityError as error:
            logger.warning(f'Tentativa de duplicar mms {pair}:{ts_from}:{ts_to}')