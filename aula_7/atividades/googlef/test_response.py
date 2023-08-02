import pytest
from response import email

def test_mail():

    assert email("malan@harvard.edu") == "Valid"
    assert email("luiz@hotmail.com") == "Valid"
    assert email("malan@@@harvard.edu") == "Invalid"
    assert email("luiz@hotmail.com.") == "Invalid"
