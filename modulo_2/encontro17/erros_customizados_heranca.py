"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Henrique Junqueira Branco
Enunciado: POO - parte 3

uso do try para validação
os tipos de erros são classes e, por isso, podem ser criadas e personalizadas
Para tal, pode usar herança da classe Exception
"""


a = 1
b = 0
c = {"1":"2"}

try:

    print("123")
    print(c["3"])
    print(a / b)
    print(d)
# o try para no primeiro erro
# se der qualquer tipo de erro no bloco try, executa o except e vai verificar com o tipo de erro
# Pode deixar em branco o except ou colocar Exception e aí vai capturar qualquer erro (genérico)
# se o tipo de error conincidir, executa o except. Pode ter vários erros em um except
# pode ter vários excepts
except (ZeroDivisionError, KeyError):
    print("O código continua normalmente!!!")
except NameError:
    raise NameError("Variável não inicializada")
# o raise vai parar o código e por uma mensagem. É um comando que independe do try


# Má prática except: pass


class SalaryNotInRangeError(Exception):
    """Exceção gerada quando o salário não está dentro da faixa especificada.
    Attributes:
        salary (int): salário que gerou o erro
        message (str): mensagem ao usuário
    """

    def __init__(self, salary, message="Salário não está na faixa especificada (5000, 15000)"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.salary} -> {self.message}"


salary = int(input("Digite um salário: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)