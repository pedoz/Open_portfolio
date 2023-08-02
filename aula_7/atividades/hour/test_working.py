import pytest
from working import convert, convert_pm, check_zero

def test_values():
    assert convert("12:24 PM to 2:34 AM") == "24:24 to 02:34"
    assert convert("1 AM to 9 PM") == "01:00 to 21:00"
    assert convert("12 PM to 12 AM") == "24:00 to 12:00"
    with pytest.raises(ValueError):
        convert("asa")