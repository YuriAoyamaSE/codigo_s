"""
Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50
"""

valor = float(input("Digite o valor a pagar:"))
cedulas = 0
cedula_atual = 100
moedas = 0
moeda_atual = 0.5
apagar = valor

while True:
    if cedula_atual <= apagar:
        apagar -= cedula_atual
        cedulas += 1
    elif apagar >= 1 or cedulas !=0:
        print(f"{cedulas} cédula(s) de R${cedula_atual}")
        if apagar == 0:
            break
        elif cedula_atual == 100:
            cedula_atual = 50
        elif cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 5
        elif cedula_atual == 5:
            cedula_atual = 1
        cedulas = 0
    elif moeda_atual <= round(apagar,2):
        apagar -= moeda_atual
        moedas += 1
    else:
        print(f"{moedas} moeda(s) de R${moeda_atual:.2f}")
        if round(apagar,2) == 0:
            break
        elif moeda_atual == 0.5:
            moeda_atual = 0.1
        elif moeda_atual == 0.1:
            moeda_atual = 0.05
        elif moeda_atual == 0.05:
            moeda_atual = 0.02
        elif moeda_atual == 0.02:
            moeda_atual = 0.01        
        moedas = 0
