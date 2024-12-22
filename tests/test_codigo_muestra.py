from application.codigo_muestra import add_numbers, greet


def test_add_numbers():
    assert add_numbers(3, 4) == 7
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_greet():
    assert greet("Charly") == "Hello, Charly"
    assert greet("Rosa") == "Hello, Rosa"

