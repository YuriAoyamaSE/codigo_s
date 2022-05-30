from impostos import *

class Venda:
    def __init__(self, valor_bruto: float, imposto: Imposto):
        self.valor_bruto = valor_bruto
        self.imposto: Imposto = imposto
    
    def calcula_valor_liquido(self):
        return self.imposto.calcula(self.valor_bruto)

    def __str__(self) -> str:
        return "print de venda"


venda1 = Venda(10_000, ICMS()) #Se colocar apenas "ICMS" estará passando a classe. "ICMS()" vai instanciar a classe, ou seja, um objeto.
print(venda1.calcula_valor_liquido())

venda2 = Venda(3_235, ISS())
print(venda2.calcula_valor_liquido())

print(venda1)
print(venda1.imposto)
