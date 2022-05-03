from abc import ABC, abstractmethod

class Poligono(ABC):
    
    @abstractmethod
    def numero_lados(self):
        pass

    @abstractmethod
    def calcula_area(self):
        pass

    @abstractmethod
    def calcula_perimetro(self):
        pass

class Triangulo(Poligono):
    def __init__(self, *args:tuple) -> None:
        self.lados = args

    def numero_lados(self):
        print("tenho 3 lados")

    def calcula_area(self):
        sp = self.calcula_perimetro() / 2
        return (sp*(sp-self.lados[0])*(sp-self.lados[1])*(sp-self.lados[2]))**(1/2)

    def calcula_perimetro(self):
        return sum(self.lados)


class Quadrado(Poligono):   
    def __init__(self, lados: float) -> None:
        self.lados = lados

    def numero_lados(self):
        print("tenho 4 lados")

    def calcula_area(self):
        return self.lados**2

    def calcula_perimetro(self):
        return 4*self.lados


class Pentagono(Poligono):   
    def numero_lados(self):
        print("tenho 5 lados")

    def calcula_area(self):
        pass

    def calcula_perimetro(self):
        pass

class Hexagono(Poligono):   
    def numero_lados(self):
        print("tenho 6 lados")

    def calcula_area(self):
        pass

    def calcula_perimetro(self):
        pass