from django.test import TestCase
import pytest
from apps.mms.models import MMS


class TestSignalCreateDate(TestCase):

    @pytest.mark.django_db
    def test_missing_dates_two_count(self):
        mms = MMS(
            pair='BRLBTC',
            timestamp=1599361199,
            mms_200=54334.33,
            mms_50=534.12,
            mms_20=3457.43
        )
        mms.save()

        self.assertIsNotNone(mms.date)
        self.assertIsNotNone(mms.id)