"""
Exercício 2:  
Escreva uma classe que converta números romanos para números inteiros. 
"""

class RomanoParaInteiro:
    dicionario = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L": 50, "XL":40, "X": 10, "IX":9, "V": 5, "IV":4, "I": 1}

    def __init__(self, romano:str) -> None:
        self.romano = romano
    
    def __str__(self) -> int:
        output = 0
        romano = self.romano
        for k,v in RomanoParaInteiro.dicionario.items():
            while romano.find(k) == 0:
                output += v
                romano = romano.removeprefix(k)
        return str(output)


numero_romano = RomanoParaInteiro("MMCDXCIII")
print(numero_romano)

