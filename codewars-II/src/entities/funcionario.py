from .entity import Entity

class Funcionario(Entity):

    def __init__(self, id: int, nome: str, cpf: str, data_de_admissao: str, cargo: str, comissao: int):
        super().__init__(id)
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_de_admissao: str = data_de_admissao
        self.__cargo: str = cargo
        self.__comissao: str = comissao

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_de_admissao(self) -> str:
        return self.__data_de_admissao

    @property
    def cargo(self) -> str:
        return self.__cargo

    @property
    def comissao(self) -> str:
        return self.__comissao