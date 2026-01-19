# Refueling
import pytest
from p4_fuel import convert
from p4_fuel import gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("0/10") == 0


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

def test_error():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
