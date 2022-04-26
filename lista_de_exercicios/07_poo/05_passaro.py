"""
Exercício 5 (desafio): 
Como você reduziria a quantidade de estruturas if-else no código abaixo 
usando herança e polimorfismo? 

class Passaro: 
    # ... 
    def calcula_velocidade(self): 
 
        if self.tipo == “EUROPEU”: 
            return self.calcula_veloridade_base() 
 
 
        elif self.tipo == “AFRICANO”: 
            return self.calcula_veloridade_base() - self.calcula_fator_carga() * 
self.altura_maxima_de_voo 
 
        elif self.tipo == “NORUEGUES”: 
            return 0 if self.nao_voa else calcula_veloridade_base() 
# ... 
 
"""
class Passaro: 
    # ... 
    def calcula_velocidade(self): 
        pass
    # ... 

class Africano(Passaro):
    def calcula_velocidade(self):
        return self.calcula_velocidade_base() - self.calcula_fator_carga() * self.altura_maxima_de_voo

class Europeu(Passaro):
    def calcula_velocidade(self):
        return self.calcula_velocidade_base() 

class Noruegues(Passaro):
    def calcula_velocidade(self):
        return 0 if self.nao_voa else self.calcula_velocidade_base()
