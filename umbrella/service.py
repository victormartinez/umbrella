class UmbrellaService:

    HUMIDITY_THRESHOLD = 70

    def __init__(self, forecasts):
        self.forecasts = forecasts

    def report(self):
        return [
            {
                "dt": f["dt"],
                "humidity": f["humidity"],
                "umbrella": f["humidity"] > self.HUMIDITY_THRESHOLD
            }
            for f in self.forecasts
        ]

