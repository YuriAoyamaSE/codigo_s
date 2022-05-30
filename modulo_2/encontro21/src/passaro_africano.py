from .passaro import Passaro


class PassaroAfricano(Passaro):
    pass

    def __init__(self) -> None:
        self.distancia = 200
        self.tempo = Passaro.calcula_tempo() 
