from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from collections import OrderedDict
from rest_framework.utils.serializer_helpers import ReturnList



class TestMMSView(TestCase):

    fixtures = [
        'fixtures/mms.json'
    ]

    @pytest.mark.django_db
    def test_filtra_mms_api(self):
        client = APIClient()
        pair = 'BRLBTC'
        mms_range = 200
        ts_from = 1614999599
        ts_to = 1630897199

        response = client.get(f'/{pair}/mms?range={mms_range}&from={ts_from}&to={ts_to}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, ReturnList)
        self.assertIsInstance(response.data[0], OrderedDict)
