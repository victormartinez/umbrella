import argparse

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
    parser = argparse.ArgumentParser(description="Should you take a umbrella?")
    parser.add_argument(
        "--lat", metavar="lat", type=float, nargs=1, required=True, help="Latitude"
    )
    parser.add_argument(
        "--lon", metavar="lon", type=float, nargs=1, required=True, help="Longitude"
    )

    args = parser.parse_args()
    lat, lon = args.lat[0], args.lon[0]

    print(f"Latitude: {lat} Longitude: {lon}")
    execute((lat, lon))
