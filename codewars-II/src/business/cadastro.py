from src.entities.entity import Entity
from typing import List

class Cadastro():

    def __init__(self):
        self.__lista = []
        
    def inserir(self, entidade: Entity) -> None:
        self.__lista.append(entidade)
    
    def consultar(self, id: str) -> Entity:
        entidade = list(filter(lambda x: x.id == id, self.__lista))


    def remover_por_id(self, id: str) -> None:
        entidade = self.consultar(id)
        self.__lista.remove(entidade)

    def listar_todos(self) -> List[Entity]:
        return self.__lista
