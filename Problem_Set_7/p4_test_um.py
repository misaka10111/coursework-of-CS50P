# Regular, um, Expressions Test
from um import count

def test_count():
    assert count("um") == 1
    assert count("Um, um, um,") == 3
    assert count("yum") == 0
    assert count("um, hello um,") == 2
