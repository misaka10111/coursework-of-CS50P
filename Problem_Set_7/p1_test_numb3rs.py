# NUMB3RS Test
from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("256.1.1.1") == False
    assert validate("1.2222.1.1") == False
