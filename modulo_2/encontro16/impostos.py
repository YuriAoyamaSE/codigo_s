class Imposto:
    def calcula(self):
        pass


class ICMS(Imposto):
    def calcula(self, valor_bruto: float) -> float:
        return valor_bruto * (1 - 0.05)
    
    # sobrescreve o print da classe
    def __str__(self) -> str:
        return "str: Imposto ICMS"
        

    # sobrescreve a representação da classe
    def __repr__(self) -> str:
        return "repr: Impostro ICMS"
        
        


class IPI(Imposto):
    def calcula(self, valor_bruto: float) -> float:
        return valor_bruto * (1 - 0.15)


class ISS(Imposto):
    def calcula(self, valor_bruto: float) -> float:
        return valor_bruto * (1 - 0.10)

