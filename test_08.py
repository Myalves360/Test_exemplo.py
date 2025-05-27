def formatar_nome(nome):
    nome = nome.strip()  # remove espaços do começo/fim
    return nome.title()  # primeira letra maiúscula, resto minúsculo

class TestFormatarNome:
    def setup_method(self):
        self.nome1 = "matheus"
        self.nome2 = "  maria alice "
        self.nome3 = "MARIA HELENA"
        self.nome4 = ""
        
    def test_nome_simples(self):
        assert formatar_nome(self.nome1) == "Matheus"

    def test_nome_com_espacos(self):
        assert formatar_nome(self.nome2) == "Maria Alice"

    def test_nome_maiusculo(self):
        assert formatar_nome(self.nome3) == "Maria Helena"

    def test_nome_simples(self):
        assert formatar_nome(self.nome4) == ""