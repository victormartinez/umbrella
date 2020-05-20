from mock import Mock
from requests import Response

import settings
from umbrella.openweather.client import DailyForecastCall


def test_success_call(monkeypatch):
    def mock_response(self):
        r = Mock(spec=Response)
        r.json.return_value = {
            "daily": [
                {"dt": 1589796000, "humidity": 10},
                {"dt": 1589882400, "humidity": 20},
            ]
        }
        r.status_code = 200
        return r

    monkeypatch.setattr(settings, "OPEN_WEATHER_API_KEY", "abcdefghi")
    monkeypatch.setattr(DailyForecastCall, "make_call", mock_response)

    client = DailyForecastCall((-10.3042, -20.1212))

    assert client.build_url() == (
        "https://api.openweathermap.org/"
        "data/2.5/onecall?lat=-10.3042&lon=-20.1212&"
        "exclude=minutely,hourly&appid=abcdefghi"
    )
    assert client.coords == (-10.3042, -20.1212)

    output_success, output_data = client.run()
    expected = {
        "daily": [
            {"dt": 1589796000, "humidity": 10},
            {"dt": 1589882400, "humidity": 20},
        ]
    }
    assert output_success is True
    assert output_data == expected


def test_failure_call__status_code(monkeypatch):
    def mock_response(self):
        r = Mock(spec=Response)
        r.json.return_value = {}
        r.status_code = 400
        return r

    monkeypatch.setattr(settings, "OPEN_WEATHER_API_KEY", "abcdefghi")
    monkeypatch.setattr(DailyForecastCall, "make_call", mock_response)

    client = DailyForecastCall((-10.3042, -20.1212))

    assert client.build_url() == (
        "https://api.openweathermap.org/"
        "data/2.5/onecall?lat=-10.3042&lon=-20.1212"
        "&exclude=minutely,hourly&appid=abcdefghi"
    )
    assert client.coords == (-10.3042, -20.1212)

    output_success, output_data = client.run()
    assert output_success is False
    assert output_data == {}
