import pytest  # importa o pytest para usar o raises()

# Função que vamos testar
def raiz_quadrada(n):
    if n < 0:
        raise ValueError("Número negativo não possui raiz real")
    return n ** 0.5

# Teste para número positivo (funciona normalmente)
def test_raiz_positiva():
    assert raiz_quadrada(4) == 2.0

# Teste para número negativo (espera um erro)
def test_raiz_negativa():
    with pytest.raises(ValueError) as erro:
        raiz_quadrada(-1)
    assert str(erro.value) == "Número negativo não possui raiz real"
