"""
A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Barulho	Nível sonoro (dB)
Britadeira	130
Cortador de grama	106
Despertador	70
Cômodo em silêncio	40


Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 
"""

nivel_sonoro = float(input("Informe o nível sonoro (db): "))

if nivel_sonoro > 130:
    barulho = "Barulho acima do ruído máximo."
elif nivel_sonoro == 130:
    barulho  = "Barulho equivalente a uma britadeira."
elif nivel_sonoro > 106:
    barulho = "Barulho entre uma britadeira e um cortador de grama."
elif nivel_sonoro == 106:
    barulho  = "Barulho equivalente a um cortador de grama."
elif nivel_sonoro > 70:
    barulho = "Barulho entre um cortador de grama e um despertador."
elif nivel_sonoro == 70:
    barulho  = "Barulho equivalente a um despertador."
elif nivel_sonoro > 40:
    barulho = "Barulho entre um despertador e um cômodo em silêncio."
elif nivel_sonoro == 40:
    barulho  = "Barulho equivalente a um cômodo em silêncio."
else:
    barulho = "Barulho abaixo do ruído mínimo."

print(barulho)
