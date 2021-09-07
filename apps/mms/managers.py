from django.db import models
from .utils.date import get_missing_dates


class MMSManager(models.Manager):

    def missing_dates(self, pair):
        dates = [x[0] for x in self.all().values_list('date').filter(pair=pair).order_by('date')]
        return get_missing_dates(dates, 0, 0)
