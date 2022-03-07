"""
Implemente um jogo em que o usuário tenha que adivinhar o somatório de dois dados.
1.	O jogo deve sortear um número para cada dado. Estes números devem variar entre 1 e 6, inclusive. Deve-se calcular a soma dos dois valores.
2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 2 ou superior a 12. Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
3.	O número do usuário deve ser analisado e o resultado da jogada deve ser apresentado na tela:
a.	Caso o usuário informe um número superior ou inferior à soma dos dados, o jogo deve apresentar a mensagem “Você errou. A soma dos dados é x. O valor do primeiro dado é d1 e o do segundo é d2. ”, sendo x o valor da soma, d1 o valor do primeiro dado e d2 o valor do segundo dado.
b.	Caso o usuário informe um número igual ao valor da soma, o jogo deve apresentar a mensagem “Parabéns! Você acertou a soma dos dados! O valor do primeiro dado é d1 e o do segundo é d2. ”, sendo d1 o valor do primeiro dado e d2 o valor do segundo dado
4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.
"""