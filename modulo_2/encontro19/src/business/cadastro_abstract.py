from typing import List
from abc import ABC, abstractmethod
from src.entities.entity import Entity


class CadastroAbtract(ABC):

    @abstractmethod
    def inserir(self, entitie: Entity):
        pass

    @abstractmethod
    def consultar(self, id) -> Entity:
        pass

    @abstractmethod
    def remover_por_id(self, id) -> Entity:
        pass

    @abstractmethod
    def remover_por_entidade(self, entitie) -> Entity:
        pass

    @abstractmethod
    def listar_todos() -> List[Entity]:
        pass
