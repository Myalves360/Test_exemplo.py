# Função a ser testada
def soma(a, b):
    return a + b


# Classe com os testes organizados
class TestSoma:
    def setup_method(self):
        self.a = 2
        self.b = 3
        self.negativo = -1
        self.zero = 0

    def test_soma_positiva(self):
        assert soma(self.a, self.b) == 5

    def test_soma_negativa(self):
        assert soma(self.negativo, self.b) == 2

    def test_soma_zero(self):
        assert soma(self.zero, self.zero) == 0


