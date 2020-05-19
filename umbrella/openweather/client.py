from urllib.parse import urljoin

import requests

import settings
from ..http import BaseHttpCall


class DailyForecast(BaseHttpCall):

    DAILY_FORECAST_PATH = "/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={}"

    def __init__(self, coords):
        self.coords = coords

    def build_url(self):
        path = self.DAILY_FORECAST_PATH.format(
            self.coords[0], self.coords[1], settings.OPEN_WEATHER_API_KEY
        )
        return urljoin(settings.OPEN_WEATHER_HOST, path)

    def make_call(self):
        url = self.build_url()
        return requests.get(url)
