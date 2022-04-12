from statistics import mean
import bingo


todos_sorteios = []
cartelas_geradas = []
jogos_simulados = 0
parar_se_ganhar = False
max_sorteios = 75

for _ in range(100000):
    bingo.iniciar()
    bolas_sorteadas = []    
    sorteios_ocorridos = 0
    cartela_1 = bingo.gerar_cart()

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

print(f"\nQuantidade de jogos simulados: {jogos_simulados}")
print(f"Número mínimo de bolas sorteadas para uma vitória: {min(todos_sorteios)}")
print(f"Número médio de bolas sorteadas para uma vitória: {mean(todos_sorteios)}")
print(f"Número máximo de bolas sorteadas para uma vitória: {max(todos_sorteios)}\n")


