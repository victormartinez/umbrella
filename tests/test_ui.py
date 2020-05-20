import pytest
from datetime import datetime

from umbrella.ui import ReportPrinter


@pytest.fixture
def daily_report():
    return [
        {"dt": datetime(2020, 5, 18), "umbrella": True},
        {"dt": datetime(2020, 5, 19), "umbrella": False},
        {"dt": datetime(2020, 5, 20), "umbrella": True},
        {"dt": datetime(2020, 5, 21), "umbrella": False},
        {"dt": datetime(2020, 5, 22), "umbrella": True},
        {"dt": datetime(2020, 5, 23), "umbrella": False},
        {"dt": datetime(2020, 5, 24), "umbrella": True},
    ]


def test_empty_report():
    output = ReportPrinter([]).print_inline()
    assert output == "There is not need of umbrella for the next days."


def test_daily_report(daily_report):
    expected = (
        "You should take an umbrella in these days: Monday, Wednesday, Friday, Sunday"
    )
    output = ReportPrinter(daily_report).print_inline()
    assert output == expected
