import pytest

def soma(a, b):
    return a + b

@pytest.mark.parametrize("a,b,esperado", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_soma_parametrizada(a, b, esperado):
    assert soma(a, b) == esperado

