"""
Usando a função mdc definida no exercício anterior, defina uma função
para calcular o menor múltiplo comum (M.M.C.) entre dois números.
mmc(a, b) = |a × b| / mdc(a, b)
Em que |a × b| pode ser escrito em Python como: abs(a * b).

Resposta:
"""

def mdc(a,b):
    c = b
    while c > 0:
        if a % c == 0 and b % c == 0:
            return c
        c-=1

def mmc(a,b):
    return abs(a * b)/mdc(a,b)

print(mmc(20,16))
print(mmc(45,15))