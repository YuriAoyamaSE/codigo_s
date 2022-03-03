"""
Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
"""

divida_inicial = float(input("Informe o valor da dívida (R$): "))
tx_juros = float(input("Informe a taxa de juros mensal (%): "))
parcela_minima = divida_inicial*tx_juros/100
pagamento_mensal = float(input(f"Parcela mínima deve ser superior a R$ {parcela_minima:.2f}. \nInforme o valor mensal a ser quitado (R$): "))
montante_divida = divida_inicial
meses = 0
juros_totais = 0

if pagamento_mensal > parcela_minima:
    while montante_divida > 0:
        juros_totais += montante_divida * (tx_juros/100)
        montante_divida *= 1+(tx_juros/100)

        if montante_divida >= pagamento_mensal:
            montante_divida -= pagamento_mensal
        else:
            ultima_parcela = montante_divida
            montante_divida = 0

        meses += 1
    
    print(f"A dívida será quitada em {meses} meses, totalizando um pagamento de R$ {(meses*pagamento_mensal+ultima_parcela):.2f}, sendo R$ {juros_totais:.2f} de juros. A última parcela será no valor de R$ {ultima_parcela:.2f}")

else:
    print("O valor do pagamento mensal é incapaz de quitar a dívida.")
