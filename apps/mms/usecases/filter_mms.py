from django.db.models import F
from rest_framework import serializers
from django.conf import settings
from apps.mms.utils.date import today, subtract_days, datetime_to_timestamp
from apps.mms.exceptions import RangeOutOfLimit


MMS_RANGE = {
    20: 'mms_20',
    50: 'mms_50',
    200: 'mms_200'
}

MIN_DAYS_QUERY = settings.MIN_DAYS_QUERY


class FilterMMS:

    def __init__(self, repository):
        self._repository = repository

    def _valid_min_date_query(self, ts_from):
        dt_today = today()
        min_dt = subtract_days(dt_today, MIN_DAYS_QUERY)

        if ts_from < datetime_to_timestamp(min_dt):
            raise RangeOutOfLimit()

    def _filter_mms(self, pair, mms_range, ts_from, ts_to):
        return self._repository.annotate(mms=F(MMS_RANGE[mms_range])) \
               .values('mms', 'timestamp') \
               .filter(pair=pair) \
               .filter(timestamp__gte=ts_from, timestamp__lte=ts_to) \
               .all()

    def __call__(self, pair, mms_range, ts_from, ts_to):
        self._valid_min_date_query(ts_from)
        return self._filter_mms(pair, mms_range, ts_from, ts_to)
