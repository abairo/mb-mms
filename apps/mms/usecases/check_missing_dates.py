from apps.mms.models import MMS
import logging


logger = logging.getLogger('MMS')


class CheckMissingDates():

    def _check_missing_dates(self, pair: str):
        return MMS.objects.missing_dates(pair)

    def __call__(self, pair: str):
        missing_dates = self._check_missing_dates(pair)

        if missing_dates:
            logger.error(f'{pair}: dias inexistentes: {missing_dates}')
