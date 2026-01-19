# Re-requesting a Vanity Plate
from p3_plates import is_valid


def test_length_is_valid():
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("A") == False


def test_start_is_valid():
    assert is_valid("AB123") == True
    assert is_valid("A1234") == False


def test_zero_is_valid():
    assert is_valid("AA1234") == True
    assert is_valid("AA0123") == False


def test_number_is_valid():
    assert is_valid("AB123A") == False
    assert is_valid("AB1A23") == False


def test_alnum_is_valid():
    assert is_valid("AA12##") == False
