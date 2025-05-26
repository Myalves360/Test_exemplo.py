import pytest

def e_par(numero):
    return numero % 2 == 0

@pytest.mark.parametrize("entrada, esperado", [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (10, True),
])
def test_e_par_parametrizado(entrada, esperado):  # <- agora com os dois parâmetros
    assert e_par(entrada) is esperado
