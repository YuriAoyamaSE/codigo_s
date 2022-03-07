"""
Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida.
"""

while True:
    operacao = int(input("Escolha uma operação: \n 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - multiplicação \n 5 - Sair \n"))
    if operacao == 5:
        break
    elif operacao in range(1,5):
        for i in range(1,11):
            for j in range(1,11):
                if operacao == 1:
                    print(f"{i} + {j} = {i+j}")
                if operacao == 2:
                    print(f"{i} - {j} = {i-j}")
                if operacao == 3:
                    print(f"{i} / {j} = {i/j:2f}")
                if operacao == 4:
                    print(f"{i} x {j} = {i*j}")        
    else:
        print("Opção inválida")
