from typing import List
from src.entities.entity import Entity
from .cadastro_abstract import CadastroAbtract


class CadastroCliente(CadastroAbtract):

    def inserir(self, entitie: Entity):
        print(f'{entitie.id} inserido.')

    def consultar(self, id) -> Entity:
        pass

    def remover_por_id(self, id) -> Entity:
        pass

    def remover_por_entidade(self, entitie) -> Entity:
        pass

    def listar_todos() -> List[Entity]:
        pass
