from seasons import Date
from datetime import date, timedelta
import pytest


def test_calculate_minutes():
    one_year = date.today() - timedelta(days=365)
    day = Date(one_year)
    assert day.calculate_minutes() == 525600
    assert day.convert_minutes(10) == "Ten minutes"

