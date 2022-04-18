class Ave:

    def __init__(self, numero_de_patas, cor, tamanho) -> None:
        self.numero_de_patas = numero_de_patas
        self.cor = cor
        self.tamanho = tamanho
    
    def voar(self):
        print("Ave voando!")


class Corvo(Ave):
    def __init__(self) -> None:
        #Super() se refere à classe mãe
        super().__init__(2, "preto", "pequeno porte")


class Tucano(Ave):
    def __init__(self) -> None:
        #Super() se refere à classe mãe
        super().__init__(2, "colorido", "médio porte")
        self.tem_mancha_no_olho = True
        self.tem_bico_serrado = True

    #polimorfismo: método igual com funções diferentes. A subclasse subscreveu para gerar um comportamento diferente.
    def voar(self):
        print("Voando como um tucano!")



t = Tucano()
t.voar()
