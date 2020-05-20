import pytest
from datetime import datetime

from umbrella.openweather.serializers import ForecastSchema


@pytest.fixture
def single_data():
    return {"dt": 1589796000, "humidity": 10, "a": 1}


@pytest.fixture
def daily_data():
    return [
        {"dt": 1589796000, "humidity": 10, "a": 1},
        {"dt": 1589882400, "humidity": 20, "x": "xyz"},
        {"dt": 1589968800, "humidity": 30, 12: 345},
        {"dt": 1590055200, "humidity": 40, "city": "city"},
        {"dt": 1590141600, "humidity": 50, "a": "b", "c": 12},
    ]


def test_many_forecast_schema(daily_data):
    expected = [
        {"dt": datetime(2020, 5, 18, 7), "humidity": 10},
        {"dt": datetime(2020, 5, 19, 7), "humidity": 20},
        {"dt": datetime(2020, 5, 20, 7), "humidity": 30},
        {"dt": datetime(2020, 5, 21, 7), "humidity": 40},
        {"dt": datetime(2020, 5, 22, 7), "humidity": 50},
    ]
    output = ForecastSchema(many=True).load(daily_data)
    assert output == expected
