"""
Bootcamp código[s]
Data: 10/03/2022
aula 06
tema: Funções

Observações: tipagem como boa prática. Por exemplo: def calcula_media(lst: list) -> float:
    Apesar de não ser necessário, ajuda no entendimento do código. Fica fácil para qualquer pessoa que esta função requer uma entrada do tipo list e irá retornar uma variável do tipo float.

Obs2: Doc string
    Utiliza-se para descrever melhor uma função, caso não esteja suficientemente esclarecido. Trata-se de boa prática e não se confunde com comentários (que usa hastag)

Obs3: def soma (a: int, b: int = 10)
    b se tornou um argumento opcional. A função deve recerber ao menos um argumento, para a. Quando houver parâmentros opcionais, eles devem ser colocados por último.
    No momento de chamar a função, pode usar por posição e por keyword (a=2, b=3). Pode misturar, mas nunca poderá o argumento poscional vir depois de argumentos por ketwords.

"""

def calcula_media(lst: list) -> float:
    return sum(lst) / len(lst)

def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float:
    """ Calcula média ponderada quando as notas possuem pesos distintos"""
    if not pesos:
        pesos = (1,)*len(valores)
    
    numerador = 0
    divisor = sum(pesos)
    for valor, peso in zip(valores, pesos):
        numerador += valor*peso
    return numerador / divisor

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
    media = calcula_media_ponderada(notas)
    print(f"A média do aluno(a) {aluno} é {media}")
