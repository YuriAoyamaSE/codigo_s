
class Passaro():
    
    def __init__(self) -> None:
        self.distancia = 0
        self.tempo = Passaro.calcula_tempo() 

    @staticmethod
    def calcula_tempo() -> int:
        return 20
    #método estático chama direto pela classe, pois é estático,independente, não usa o self  
          
    def calcula_velocidade(self) -> float:
        return self.distancia / self.tempo

    def incrementa_tempo(self):
        self.tempo += 20        
        
    def incrementa_distancia(self):
        self.distancia *= 1.5
