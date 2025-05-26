def e_par(numero):
    return numero % 2 == 0

def test_par():
    assert e_par(4) is True

def test_impar():
    assert e_par(3) is False

def test_zero():
    assert e_par(0) is True
