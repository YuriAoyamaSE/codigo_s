from unicodedata import normalize

class Funcionario:
    #variáveis da classe:
    aumento_percentual: float = 0.1


    def __init__(self, nome: str, sobrenome: str, salario_inicial: int = 1_200) -> None:
        #variáveis de instância da classe
        self.nome = nome
        self.sobrenome = sobrenome
        self.__salario_inicial = salario_inicial
        self._salario_atual = self.__salario_inicial
        self.email = gerar_email(self.nome, self.sobrenome)


    def dar_aumento(self) -> None:        
        self._salario_atual *= (1 + Funcionario.aumento_percentual)


def gerar_email(nome,sobrenome) -> str:
    email = list(nome+sobrenome)
    while email.count(" ") != 0:
        email.remove(" ")
    email = "".join(email)    
    email = normalize('NFD', email)        
    email = email.encode("ascii", "ignore")
    email = email.decode("utf-8")
    email = email.lower()+"@empresa.com.br"    
    return email
