from .service import UmbrellaService
from .ui import print_report
from .openweather.client import DailyForecast
from .openweather.serializers import ForecastSchema


def execute(coords):
    success, data = DailyForecast(coords).run()
    if not success:
        print("error")

    forecasts = ForecastSchema(many=True).load(data["daily"])
    report = UmbrellaService(forecasts).report()
    print_report(report)


if __name__ == "__main__":
    execute((1, 2))
