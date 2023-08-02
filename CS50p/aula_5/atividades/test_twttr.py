from twttr import shorten

def test_without_num():
    assert shorten("ola como vc vai?") == "l cm vc v?"
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_with_num():
    assert shorten("Hello you 1, you 2 gay") == "Hll y 1, y 2 gy"
    assert shorten("a12b3c4d5e6f7g8h9i0j") == "12b3c4d56f7g8h90j"

def test_random():
    assert shorten("W,akka232") == "W,kk232"