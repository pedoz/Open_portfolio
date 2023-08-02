from numb3rs import validate
import re

def test_valid_ip():
    assert validate('255.0.0.1') == "Valid IP"
    assert validate("11.56.255.1") == "Valid IP"

def test_invalid_ip():
    assert validate("256.3.6.1") == "Invalid IP"
    assert validate("0.0.0.") == "Valid IP"   