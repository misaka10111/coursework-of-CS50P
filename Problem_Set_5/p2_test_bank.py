# Back to the Bank
from p2_bank import value


def test_value():
    assert value("hello") == 0
    assert value("Hey") == 20
    assert value("oh") == 100
