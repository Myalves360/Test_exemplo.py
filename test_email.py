from validador import email_valido

class TestEmailValido: 
    def setup_method(self): 
        self.email_1 = "user@example.com"
        self.email_2 = "usuario@site"
        self.email_3 = "semarroba.com"
        self.email_4 = "a@b.c"
        self.email_5 = "ok@email.com"
        
    def test_email_valido(self): 
        assert email_valido(self.email_1) is True 
        assert email_valido(self.email_5) is True
        
    def test_email_sem_ponto(self): 
        assert email_valido(self.email_2) is False
        
    def test_email_sem_arroba(self):
        assert email_valido(self.email_3) is False
        
    def test_email_curto(self): 
        assert email_valido(self.email_4) is False
        

        

        
        