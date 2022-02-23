"""
Escreva um programa que leia a quantidade de dias, horas, minutos e 
segundos do usuário. Calcule o total em segundos.
"""

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_de_segundos = segundos + minutos*60 + horas*60+60 + dias*24*60*60

print(f"Em {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos há: {total_de_segundos} segundos.")
