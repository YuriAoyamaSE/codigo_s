"""
Bootcamp código[s]
Data: 22/03/2022
aula 09
tema: Bibliotecas built-in
"""

from statistics import mean
import calculo

fechamento = dict()

numero_de_alunos = 1 #int( input("Quantos alunos pretende cadastrar? "))
numero_de_notas = 2 #int( input("Quantas notas de cada alunos pretende cadastrar? "))

for _ in range(numero_de_alunos):
    nome = input("Informe o nome do aluno: ")
    fechamento[nome] = []

    for i in range(numero_de_notas):
        nota = int(input(f"Informe a {i +1}ª nota de {nome}: "))
        fechamento[nome].append(nota)

for aluno, notas in fechamento.items():
    media_ponderada = round(calculo.calcula_media_ponderada(notas,(1,2)),2)
    media_aritmetica = mean(notas)
    print(f"A média ponderada do aluno(a) {aluno} é {media_ponderada}")
    print(f"A média aritmética do aluno(a) {aluno} é {media_aritmetica}")
