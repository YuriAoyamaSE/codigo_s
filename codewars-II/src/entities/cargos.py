from .entity import Entity

class Cargos(Entity):

    def __init__(self, id: int, descricao: str, salario_base: float, comissao: float):
        super().__init__(id)
        self.__descricao = descricao
        self.__salario_base = salario_base
        self.__comissao = comissao

    @property
    def descricao(self):
        return self.__descricao

    @property
    def salario_base(self):
        return self.__salario_base
    
    @property
    def comissao(self):
        return self.__comissao
        
    