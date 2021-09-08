from django.test import TestCase
import pytest
from apps.mms.models import MMS


class TestManagerMissingDates(TestCase):

    fixtures = [
        'fixtures/mms.json'
    ]

    @pytest.mark.django_db
    def test_missing_dates_two_count(self):
        mms_list = MMS.objects.filter(pair='BRLBTC').all()[5:7]

        for mms in mms_list:
            mms.delete()

        missing_dates = MMS.objects.missing_dates('BRLBTC')

        self.assertEqual(len(missing_dates), 2)
    
    @pytest.mark.django_db
    def test_missing_dates_none(self):
        
        missing_dates = MMS.objects.missing_dates('BRLBTC')

        self.assertEqual(len(missing_dates), 0)