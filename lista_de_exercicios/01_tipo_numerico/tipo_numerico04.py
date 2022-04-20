
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (metros): "))

imc = peso/(altura ** 2)

print(f"Seu IMC é {imc:.2f}")
