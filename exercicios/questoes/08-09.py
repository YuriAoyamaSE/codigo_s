"""Rastreie o Programa 8.6 e compare o seu resultado com o apresentado

sem acesso. Gabarito:
"""

# Comparando o programa da listagem 8.12 com o resultado
# da listagem 8.13.
#
# O programa calcula o fatorial de 4
# Pelas mensagens impressas na listagem 8.13 e pelo rastreamento do programa,
# podemos concluir que o fatorial de 4 é calculado com chamadas recursivas
# na linha: fat = n * fatorial(n-1)
#
# Como a chamada do fatorial precede a impressão da linha Fatorial de,
# podemos visualisar a sequencia em forma de pilha, onde o cálculo é feito de fora
# para dentro: Calculo do fatorial de 4, 3 , 2 e 1
# para então processiguir na linha seguinte, que faz a impressão dos resultados:
# fatorial de 1,2,3,4