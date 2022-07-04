

"""
1. Gerar o holerite de um funcionário específico
  - solicitar o mês
  - definir campo chave para busca, apresentar os dados pessoais do funcionário, solicitar a quantidade de faltas, gerar e apresentar o holerite
  - armazenar o holerite do funcionário no banco de dados
  - apresentar mensagem de erro caso a chave de busca não seja encontrada (Exceções)

2. Gerar o holerite de todos os funcionários
  - solicitar o mês
  - gerar holerite apenas dos funcionários que ainda não possuem holerite do mês
  - considerar que estes funcionários não tiveram falta (automaticamente, considerar 22,5 dias trabalhados)
  - apresentar o holerite do mês de todos os funcionários
  - emitir mensagem de erro caso não hajam funcionários cadastrados (Exceções)
"""

from src.entities.funcionario import Funcionario


class Holerites():

    def __init__(self, funcionario: Funcionario) -> None:
        self.funcionario = funcionario
    
    def gerar_holerite(self, mes: str, faltas: int):
        pass
    
    def listar_holerites(mes):
        pass

    