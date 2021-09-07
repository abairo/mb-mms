import pytest
import datetime
from apps.mms.utils.date import yesterday


def test_yesterday():
    date = yesterday()

    assert isinstance(date, datetime.date)
