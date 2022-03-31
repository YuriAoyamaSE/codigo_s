from statistics import mean
import bingo

#while True:
todos_sorteios = []
#cartelas_geradas = []
jogos_simulados = 0
jogos_a_simular = 10**3

for _ in range(jogos_a_simular):
    bingo.iniciar()
    bolas_sorteadas = []
    max_sorteios = 75
    sorteios_ocorridos = 0
    parar_se_ganhar = False
    cartela_1 = bingo.gerar_cart()

    #bingo.imprimir_cart(cartela_1)
    
#    if cartela_1 not in cartelas_geradas:
#        cartelas_geradas.append(cartela_1)
#    else:
#        break


    for i in range(max_sorteios):
        nova_bola = bingo.sortear_bola()
        bolas_sorteadas.insert(i, nova_bola)
        cartela_1 = bingo.checar_cartela(nova_bola, cartela_1)
        if bingo.ganhou(cartela_1) == True and sorteios_ocorridos == 0:
            sorteios_ocorridos = len(bolas_sorteadas)
            if parar_se_ganhar:
                break
    
    jogos_simulados += 1
    todos_sorteios.append(sorteios_ocorridos)

print(f"\nQuantidade de jogos simulados: {jogos_simulados}")
print(f"Número mínimo de bolas sorteadas para uma vitória: {min(todos_sorteios)}")
print(f"Número médio de bolas sorteadas para uma vitória: {mean(todos_sorteios)}")
print(f"Número máximo de bolas sorteadas para uma vitória: {max(todos_sorteios)}\n")

"""
    print(f"{len(bolas_sorteadas)} números sorteados: {bolas_sorteadas}\n")
    bingo.imprimir_cart(cartela_1)

    if bingo.ganhou(cartela_1):
        print(f"BINGO!!!\nParabéns, você ganhou na {sorteios_ocorridos}ª bola sorteada!!!")
    else:
        print("Sua cartela não perseverou...")

    if input("Repetir Bingo? (s/n)  ").lower() != "s":
       break

bingo.fim()

"""


