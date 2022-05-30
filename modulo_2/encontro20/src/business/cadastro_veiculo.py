from typing import List
from src.business.cadastro_abstract import CadastroAbtract
from src.entities.veiculo import Veiculo


class CadastroVeiculo(CadastroAbtract):
    
    def __init__(self) -> None:
        super().__init__()
        self.__veiculos: List[Veiculo] = []

    def inserir(self, veiculo: Veiculo) -> None:
        self.__veiculos.append(veiculo)

    def consultar(self, id) -> Veiculo:
        veiculo = list(
            filter(lambda veiculo: veiculo.id == id, self.__veiculos))
        return veiculo[0]

    def remover_por_id(self, id: str) -> None:
        veiculo = self.consultar(id)
        self.__veiculos.remove(veiculo)

    def remover_por_entidade(self, veiculo: Veiculo) -> None:
        self.__veiculos.remove(veiculo)

    def listar_todos(self) -> List[Veiculo]:
        return self.__veiculos
