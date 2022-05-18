"""
Aula 23
Data: 17/05/2022
Assunto: testes unitários


testes funcionais: unitários; integração, sistema; aceitação.

Unitário: objetivo de testar a menor partetestável do sistema (geralmente um método).


"""

def somar (a,b):
    return a+b

def dividir(a,b):
    return a/b

def multiplicar(a,b):
    return a*b

def subtrair(a,b):
    return a-b


#Uma forma simples está abaixo, mas há problema de ter que ficar apagando ou comentando, já que não pode fazer parte do código ao final: 
valor_a = 1
valor_b = 2
resultado = somar(valor_a,valor_b)
print(resultado)
