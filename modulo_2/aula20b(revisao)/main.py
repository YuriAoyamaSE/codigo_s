from src.passaro_africano import PassaroAfricano
from src.passaro_europeu import PassaroEuropeu

africano1 = PassaroAfricano()
europeu1 = PassaroEuropeu()

print(africano1.calcula_velocidade())
africano1.incrementa_tempo()
print(africano1.calcula_velocidade())
africano1.incrementa_distancia()
print(africano1.calcula_velocidade())

print(europeu1.calcula_velocidade())