# Lista de exercícios
## Tema: tipos numéricos
## Diversão do carnaval \o/


### Exercício 1: [Resposta](https://github.com/YuriAoyamaSE/codigo_s/blob/main/lista_de_exercicios/carnaval01/tipo_numerico01.py)

Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
	A soma de A e B;
	A diferença quando se subtrai B de A;
	O produto (multiplicação) entre A e B;
	O quociente (parte inteira da divisão) quando se divide A por B;
	O resto da divisão entre A e B;
	O resultado de log10 de A;
	O resultado de A elevado a B;

Dica!
Para calcular o log10, utilize a função log10 do módulo math conforme exemplo abaixo
>>> from math import log10
>>> log10(100)
2.0


### Exercício 2: [Resposta](https://github.com/YuriAoyamaSE/codigo_s/blob/main/lista_de_exercicios/carnaval01/tipo_numerico02.py)

Faça um programa que receba a base e altura de um triângulo e imprima a área dele.

Dica!
A área de um triângulo é dada pela seguinte fórmula abaixo
area=(base x altura)/2


### Exercício 3: [Resposta](https://github.com/YuriAoyamaSE/codigo_s/blob/main/lista_de_exercicios/carnaval01/tipo_numerico03.py)

No exercício acima você calculou a área de um triângulo a partir da sua base e altura. Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.


Dica!
A área de um triângulo também é dada pela seguintes fórmulas abaixo
s=(s1+s2+s3)/2
area=√(s.(s-s1).(s-s2).(s-s3)  )


### Exercício 4: [Resposta](https://github.com/YuriAoyamaSE/codigo_s/blob/main/lista_de_exercicios/carnaval01/tipo_numerico04.py)

Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.

Dica!
O IMC é calculado de acordo com a fórmula abaixo
IMC=peso/〖altura〗^2 


### Exercício 5: [Resposta](https://github.com/YuriAoyamaSE/codigo_s/blob/main/lista_de_exercicios/carnaval01/tipo_numerico05.py)

Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.

