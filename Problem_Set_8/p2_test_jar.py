from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12
    jar.withdraw(5)
    assert jar.size == 7
    jar.withdraw(4)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(10)
