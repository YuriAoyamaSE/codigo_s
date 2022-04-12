"""
Bootcamp código[s]
Data: 15/03/2022
aula 07
tema: Módulos, pacotes e ambientes virtuais
"""

import calculo

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
    media = calculo.calcula_media_ponderada(notas)
    print(f"A média do aluno(a) {aluno} é {media}")
