from datetime import datetime


class ReportPrinter:

    INLINE_NO_DAYS = "There is not need of umbrella for the next days."
    INLINE_TEMPLATE = "You should take an umbrella in these days: {}"

    def __init__(self, report):
        self.report = report

    def print_inline(self):
        umbrella_usage_days = [
            datetime.strftime(row["dt"], "%A") for row in self.report if row["umbrella"]
        ]

        if umbrella_usage_days:
            days_str = ", ".join(umbrella_usage_days)
            return self.INLINE_TEMPLATE.format(days_str)
        else:
            return self.INLINE_NO_DAYS
