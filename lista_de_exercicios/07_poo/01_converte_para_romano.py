"""
Exercício 1: 
Escreva uma classe que converta números inteiros para números romanos. 
"""

class InteiroParaRomano:
    dicionario = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L": 50, "XL":40, "X": 10, "IX":9, "V": 5, "IV":4, "I": 1}

    def __init__(self, numero:int) -> None:
        self.numero = numero
    
    def __str__(self) -> str:
        romano = []
        numero = self.numero
        for k,v in InteiroParaRomano.dicionario.items():
            romano.append((numero // v)*k)
            numero %= v
        return "".join(romano)


numero_romano = InteiroParaRomano(2562)
print(numero_romano)