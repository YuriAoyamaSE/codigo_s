"""
Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:

Código Preço
1      0,50
2      1,00 
3      4,00
5      7,00
9      8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
"""

lista_de_produtos = {1:0.5, 2:1, 3:4, 5:7, 9:8}
total_da_compra = 0

while True:
    cod_produto = int(input("Informe o código do produto: "))
    if (cod_produto != 0) and (cod_produto not in lista_de_produtos):
        print("Código inválido")      
    elif cod_produto in lista_de_produtos:
        qt_comprada = int(input("Informe a quantidade comprada: "))
        total_da_compra += lista_de_produtos[cod_produto] * qt_comprada    
    else:
        print(f"Total das compras: R$ {total_da_compra:.2f}")
        break
    