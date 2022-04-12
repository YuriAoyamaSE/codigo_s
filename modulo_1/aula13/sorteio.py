"""
How Bootcamps - Stone - /código[s]
Data: 04/04/2022
Autor: Henrique Junqueira Branco
Enunciado: Sistema de sorteio e arquivo CSV

sorteio:
2 equipes ganham premios da stones
1 equipe ganha da how
3 pessoas ganham da stones, independente da equipe
"""

from collections import defaultdict
import csv
from random import choice

brindes = {"how": 5, "stone": 13}
equipes = defaultdict(list)

with open(r'aulas\aula13\Sorteio.csv', 'r') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=',', quotechar='|')
    for linha in arquivo:
        if linha[0] == "Nome do Aluno":
            continue
        nome_aluno = linha[0].strip().replace("  ", " ")
        numero_equipe = linha[1]
        equipes[numero_equipe].append(nome_aluno)


for _ in range(2):
    print("\nSorteio da Stone!")
    equipe_sorteada = choice(list(equipes.keys()))
    pessoas_sorteadas = equipes[equipe_sorteada]
    print(f"\nEquipe sorteada foi a nº {equipe_sorteada}")
    for pessoa in pessoas_sorteadas:
        print(f"Parabéns {pessoa}, você ganhou um brinde da Stone!")

    equipes.pop(equipe_sorteada)
    print("*" * 60)
    print("*" * 60)

    