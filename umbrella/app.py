from .service import UmbrellaService
from .ui import ReportPrinter
from .openweather.client import DailyForecast
from .openweather.serializers import ForecastSchema


def execute(coords):
    success, data = DailyForecast(coords).run()
    if not success:
        print(data["message"])
        return

    forecasts = ForecastSchema(many=True).load(data["daily"])
    report = UmbrellaService(forecasts).report()
    ReportPrinter(report).print_inline()


if __name__ == "__main__":
    execute((1, 2))
