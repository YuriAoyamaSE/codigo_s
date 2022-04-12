"""
Bootcamp código[s]
Data: 17/02/2022
aula 02 
"""
continuar = "s"

while continuar == "s":

    aluno = input("Digite o nome do aluno(a): ")
    quantidade_de_notas = int( input("Quantas notas você gostaria de cadastrar? "))
    nota = []

    for contador in range(0, quantidade_de_notas):
        nota.append(float(input(f"Digite a {contador+1}ª nota: ")))

    media = sum(nota)/quantidade_de_notas

    print(f"A média das notas de {aluno} é {round(media,2)}")

    continuar = input("Gostaria de repetir? (s/n) ")
