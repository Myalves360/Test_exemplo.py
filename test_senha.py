import re

def senha_valida(senha):
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Z]', senha):  # letra maiúscula
        return False
    if not re.search(r'[a-z]', senha):  # letra minúscula
        return False
    if not re.search(r'\d', senha):     # número
        return False
    if not re.search(r'[!@#$%^&*()\-_=+]', senha):  # caractere especial
        return False
    return True
class TestSenhaValida:
    def setup_method(self):
        self.fraca_1 = "abc123"              # curta e sem maiúscula/especial
        self.fraca_2 = "Abcdefgh"            # sem número e especial
        self.fraca_3 = "Abc12345"            # sem caractere especial
        self.forte = "Abc123$#"              # válida

    def test_senha_curta(self):
        assert senha_valida(self.fraca_1) is False

    def test_senha_sem_numero(self):
        assert senha_valida(self.fraca_2) is False

    def test_senha_sem_especial(self):
        assert senha_valida(self.fraca_3) is False

    def test_senha_valida(self):
        assert senha_valida(self.forte) is True
