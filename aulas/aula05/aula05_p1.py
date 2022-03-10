"""
Bootcamp código[s]
Data: 08/03/2022
aula 05

tema: Estrutura de repetição
"""

fechamento = dict()

numero_de_alunos = int( input("Quantos alunos pretende cadastrar? "))
numero_de_notas = int( input("Quantas notas de cada alunos pretende cadastrar? "))

for _ in range(numero_de_alunos):
    nome = input("Informe o nome do aluno: ")
    fechamento[nome] = []

    for i in range(numero_de_notas):
        nota = int(input(f"Informe a {i +1}ª nota de {nome}: "))
        fechamento[nome].append(nota)


for aluno, notas in fechamento.items():
    media = round(sum(notas)/len(notas),1)
    print(f"A média do aluno(a) {aluno} é {media}")
