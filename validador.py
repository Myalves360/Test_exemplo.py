import re

def email_valido(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao, email) is not None
