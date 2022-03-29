import bingo

while True:
    bingo.iniciar()
    bolas_sorteadas = []
    num_max_bolas = 50
    parar_se_ganhar = True
    cartela_1 = bingo.gerar_cart()

    bingo.imprimir_cart(cartela_1)
    print()

    for i in range(num_max_bolas):
        nova_bola = bingo.sortear_bola()
        bolas_sorteadas.insert(i, nova_bola)
        cartela_1 = bingo.checar_cartela(nova_bola, cartela_1)
        if bingo.ganhou(cartela_1) == True and not parar_se_ganhar:
            break

    print(f"{len(bolas_sorteadas)} números sorteados: {bolas_sorteadas}\n")
    bingo.imprimir_cart(cartela_1)

    if bingo.ganhou(cartela_1):
        print("BINGO!!!\nParabéns, você ganhou!!!")
    else:
        print("Sua cartela não perseverou...")

    if input("Repetir Bingo? (s/n)  ").lower() != "s":
        break


print()
print("|||||||||||||||||||||")
print("||   FIM DE JOGO   ||")
print("|||||||||||||||||||||")
