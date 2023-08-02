from plates import is_valid


def test_not_valid():
    assert is_valid("ab1c23") == False
    assert is_valid("tryp09") == False
    assert is_valid("ab1") == False
    assert is_valid("76ab12") == False
    assert is_valid("s1ab43") == False
    assert is_valid("hk0765") == False

def test_valid():
    assert is_valid("cs50") == True
    assert is_valid("abc500") == True
    assert is_valid("bp41") == True
    assert is_valid("hk7065") == True