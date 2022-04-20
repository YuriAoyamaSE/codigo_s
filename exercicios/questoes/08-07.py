"""
Defina uma função recursiva que calcule o maior divisor comum (M.D.C.) entre dois números a e b, em que a > b.
[ver representação no livro]

Resposta:
"""

def mdc(a,b):
    c = b
    while c > 0:
        if a % c == 0 and b % c == 0:
            return c
        c-=1

print(mdc(20,16))
print(mdc(45,15))