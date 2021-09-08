import pytest
from apps.mms.utils.data_import import mms_average


@pytest.fixture
def candles():
    return [
        {"timestamp":1577836800,"open":529.9598,"close":526.16056,"high":534.99999,"low":525,"volume":68.01555633},
        {"timestamp":1577923200,"open":526.50275,"close":525.35584,"high":540,"low":512,"volume":231.48234248},
        {"timestamp":1578009600,"open":524.5384,"close":547.71894,"high":549.13578,"low":518.40001,"volume":317.83165753}
    ]
    


def test_mms_average(candles):
    mms_3 = mms_average(candles, slice(0, len(candles)), 3)

    assert mms_3 == 533.0784466666667