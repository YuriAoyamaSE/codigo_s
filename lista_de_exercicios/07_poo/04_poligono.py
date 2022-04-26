"""
Exercício 4:
Implemente uma classe chamada Poligono que servirá de base para outras classes 
(classe mãe). Esta classe deve ter métodos para calcular área e perímetro. A 
partir desta classe, crie subclasses para cada polígono específico: Triangulo, 
Quadrado, Pentagono. Cada um deles deve sobrescrever o método da classe mãe 
para implementar a sua própria fórmula de cálculo de área e perímetro. 
"""
from math import sqrt

class Poligono:
    def __init__(self, tam_lados,qt_lados) -> None:
        self.qt_lados = qt_lados
        self.tam_lados = tam_lados
    
    def perimetro(self):
        return self.qt_lados * self.tam_lados

    def area(self):
        pass


class Triangulo(Poligono):
    def __init__(self, tam_lados) -> None:
        super().__init__(tam_lados, 3)

    def area(self):
        return self.tam_lados**2 * sqrt(3) / 4
        

class Quadrado(Poligono):
    def __init__(self, tam_lados) -> None:
        super().__init__(tam_lados, 4)

    def area(self):
        return self.tam_lados**2

class Pentagono(Poligono):
    def __init__(self, tam_lados) -> None:
        super().__init__(tam_lados, 5)

    def area(self):
        return 6 * self.tam_lados**2 * sqrt(3) / 4

t = Triangulo(4)
print(t.area())