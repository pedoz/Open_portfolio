from bank import value

def test_with_hello():
    assert value("hello") == "$0"

def test_with_h():
    assert value("heya") == "$20"

def test_without_h():
    assert value("caramba") == "$100"
    assert value("123Hola") == "$100"
    assert value("ohio") == "$100"