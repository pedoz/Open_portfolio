import pytest
from fuel import convert, gauge

def test_gauge_c():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_gauge_w():
    assert gauge (-1) == "erro"


def test_convert_c():
    assert convert("3/5") == 60
    assert convert("5/5") == 100


def test_convert_w():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("cat")