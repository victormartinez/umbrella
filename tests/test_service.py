import pytest
from datetime import datetime

from umbrella.service import UmbrellaService


@pytest.fixture
def forecasts():
    return [
        {"dt": datetime(2020, 5, 18), "humidity": 70},
        {"dt": datetime(2020, 5, 19), "humidity": 50},
        {"dt": datetime(2020, 5, 20), "humidity": 71},
        {"dt": datetime(2020, 5, 21), "humidity": 80},
        {"dt": datetime(2020, 5, 22), "humidity": 85},
        {"dt": datetime(2020, 5, 23), "humidity": 30},
        {"dt": datetime(2020, 5, 24), "humidity": 40},
    ]


def test_empty_report():
    output = UmbrellaService([]).report()
    assert output == []


def test_humidity_threshold(forecasts):
    expected = [
        {"dt": datetime(2020, 5, 18), "humidity": 70, "umbrella": False},
        {"dt": datetime(2020, 5, 19), "humidity": 50, "umbrella": False},
        {"dt": datetime(2020, 5, 20), "humidity": 71, "umbrella": True},
        {"dt": datetime(2020, 5, 21), "humidity": 80, "umbrella": True},
        {"dt": datetime(2020, 5, 22), "humidity": 85, "umbrella": True},
        {"dt": datetime(2020, 5, 23), "humidity": 30, "umbrella": False},
        {"dt": datetime(2020, 5, 24), "humidity": 40, "umbrella": False},
    ]
    output = UmbrellaService(forecasts).report()
    assert output == expected
