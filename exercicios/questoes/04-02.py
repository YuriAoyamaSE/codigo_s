"""
Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
"""

velocidade = float(input("Digite a velocidade do carro: "))
limite = 80

if velocidade > limite:
    multa = (velocidade-80)*5
    print(f"Velocidade acima do limite permitido. \nMulta a pagar: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite permitido")
