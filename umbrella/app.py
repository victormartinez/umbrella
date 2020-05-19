from .service import UmbrellaService
from .ui import ReportPrinter
from .openweather.client import DailyForecastCall
from .openweather.serializers import ForecastSchema


def execute(coords):
    success, data = DailyForecastCall(coords).run()
    if not success:
        print(data["message"])
        return

    forecasts = ForecastSchema(many=True).load(data["daily"][1:])
    report = UmbrellaService(forecasts).report()
    ReportPrinter(report).print_inline()


if __name__ == "__main__":
    execute((1, 2))
