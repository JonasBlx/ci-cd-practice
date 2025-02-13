from src.main import add


def test_add_function():
    assert add(1, 1) == 2
    assert add(1, -1) == 0
    assert add(0, 0) == 0
