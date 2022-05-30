"""
How Bootcamps - Stone - /código[s]
Data: 26/04/2022
Autor: Henrique Junqueira Branco
Tema: POO - aula 4/5

CLASSES ABSTRATAS (São chamadas de Interface)
São classes que NUNCA são instanciadas e possuem AO MENOS um método abstrato.
Não é boa prática e nem faz sentido ter métodos que não sejam abstratos, já que ela não deveria ser instanciada.
Servem apenas de modelo obrigatório para classes filhas, que vão ser as CLASSES CONCRETAS (obriga elas terem métodos obrigatórios).

Módulo ABC = Abstract Base Class -> para gerar a classe abstrata
decorador abstractmethod -> define método abstrato (não fazem nada)

"""

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def alimentar(self):
        pass

class Leao(Animal):
    def alimentar(self):
        print("leão alimentado")


class Cobra(Animal):
    def x():
        pass
    """
    def alimentar(self):
        print("cobra alimentada")
    """


class Tigre(Animal):
    def alimentar(self):
        print("Tigre alimentado")

t = Tigre()
t.alimentar()
c= Cobra()