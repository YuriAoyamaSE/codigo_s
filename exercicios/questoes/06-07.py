"""
Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.

Exemplo:

(()) OK
()()(()()) OK
()) Erro
Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar, verifique se o topo da pilha é um abre parênteses. Se a expressão estiver correta, sua pilha estará vazia no final.
"""

entrada = "(()(())())"
abre = 0
fecha = 0
ok = True

for item in entrada:
    if item == "(":
        abre += 1
    elif item == ")":
        fecha += 1
    if (abre - fecha) < 0:
        ok = False
        break

if ok and abre == fecha:
    print("Ok")
else:
    print("Erro")
