import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def test_divisao_valida():
    assert dividir(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError) as erro:
        dividir(10, 0)
    assert str(erro.value) == "Não é possível dividir por zero"
