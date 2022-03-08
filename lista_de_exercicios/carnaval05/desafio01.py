"""
Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

1.	O jogo deve sortear um número entre 1 e 100.
2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 1 ou superior a 100. Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
3.	O número do usuário deve ser analisado:
a.	Caso o usuário informe um número inferior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é maior.”.
b.	Caso o usuário informe um número superior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é menor.”.
c.	Caso o usuário informe um número igual ao número sorteado, o jogo deve apresentar a mensagem “Parabéns! Você acertou o número sorteado” e o jogo deve ser finalizado, sendo apresentado ao usuário a quantidade de tentativas efetuadas até este momento.
4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

Dica!
Pesquise sobre o módulo buit-in do Python chamado random
"""

from random import randrange

print("***** Bem vindos ao jogo de adivinhação do Código[s] *****")

continuar = "s"

while continuar == "s":
    total_de_tentativas = 0
    numero_sorteado = randrange(1,101)
    numero_do_usuario = 0

    while numero_do_usuario != numero_sorteado:
        numero_do_usuario = int(input("Digite um número de 1 a 100: "))
        if numero_do_usuario not in range(1,101):
            print("Você digitou um número inválido.")
            total_de_tentativas -= 1
        elif numero_do_usuario < numero_sorteado:
            print("O número sorteado é maior.")        
        elif numero_do_usuario > numero_sorteado:
            print("O número sorteado é menor.")

        total_de_tentativas += 1
    
    print("Parabéns! Você acertou o número sorteado")
    print(f"Total de tentativas: {total_de_tentativas}")
    print("*********** Fim do jogo ***********")

    continuar = input("\nDeseja jogar novamente? (s/n) ")

print("*********** Jogo encerrado ***********")
