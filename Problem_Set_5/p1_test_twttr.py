# Testing my twttr
from p1_twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("aeioucs") == "cs"
    assert shorten("shor123ten???") == "shr123tn???"
