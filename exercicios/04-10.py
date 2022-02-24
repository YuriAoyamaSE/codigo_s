"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+
"""

consumo = float(input(f"Informe o consumo mensal (kWh): "))
instalacao = input(f"Informe o tipo de instalação: \nResidência (R) \nIndústria (I) \nComércio (C)").lower()

def calcula_tarifa(consumo, instalacao):
    if instalacao == "r":
        if consumo <= 500:
            return 0.40
        else:
            return 0.65
    elif instalacao == "c":
        if consumo <= 1000:
            return 0.55
        else:
            return 0.60
    elif instalacao == "i":
        if consumo <= 5000:
            return 0.55
        else:
            return 0.60

tarifa = calcula_tarifa(consumo,instalacao)
conta = consumo * tarifa

print(f"Total a ser pago: R$ {conta:.2f}")
