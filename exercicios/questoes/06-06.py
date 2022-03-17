"""
Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.
"""

fila1 = list(range(1, 11))
fila2 = list(range(1, 11))

def atendimento(fila: list) -> None:
    if len(fila) > 0:
        atendido = fila.pop(0)
        print(f"Cliente {atendido} atendido")
    else:
        print("Fila vazia! Ninguém para atender.")

def novo_cliente(fila: list) -> None:
    if len(fila) > 0:
        ultimo = fila[-1]+1
    else:
        ultimo = 1
    fila.append(ultimo)

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} na fila 2.")
    print("Fila 1 atual:", fila1)
    print("Fila 2 autal:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila1, G para a fila2.")
    print("Digite A para realizar o atendimento na fila1 ou B na fila2. S para sair.")
    operação = input("Operação (F/G, A/B ou S):").upper()
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            atendimento(fila1)            
        elif operação[x] == "F":
            novo_cliente(fila1)
        if operação[x] == "B":
            atendimento(fila2)            
        elif operação[x] == "G":
            novo_cliente(fila2)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!")
        x = x + 1
    if sair:
        break
