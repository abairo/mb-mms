
from django.db.models import F


MMS_RANGE = {
    20: 'mms_20',
    50: 'mms_50',
    200: 'mms_200'
}


class FilterMMS:

    def __init__(self, repository):
        self._repository = repository

    def _get_queryset(self, pair, mms_range, ts_from, ts_to):
        return self._repository.annotate(mms=F(MMS_RANGE[mms_range])) \
               .values('mms', 'timestamp') \
               .filter(pair=pair) \
               .filter(timestamp__gte=ts_from, timestamp__lte=ts_to) \
               .all()

    def __call__(self, pair, mms_range, ts_from, ts_to):
        return self._get_queryset(pair, mms_range, ts_from, ts_to)
