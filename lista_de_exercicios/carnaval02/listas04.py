
meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
temperaturas = []

for mes in meses:
    temperatura_do_mes = float(input(f"Informe a temperatura média do mês de {mes} (°C): "))
    temperaturas.append(temperatura_do_mes)

media_anual = round(sum(temperaturas)/len(temperaturas),1)

print(f"Meses com temperatura acima da média anual de {media_anual}°:")

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]} - {temperaturas[i]}°C")
