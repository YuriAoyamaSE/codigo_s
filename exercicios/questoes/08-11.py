"""
Escreva uma função para validar uma variável string. Essa função
recebe como parâmetro a string, o número mínimo e máximo de caracteres.
Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e
mínimo, e falso, caso contrário.

Resposta:
"""

def valida_string(string: str, char_min:int, char_max:int) -> bool:
    return len(string) > char_min and len(string) < char_max


print(valida_string("casa",2,5))
print(valida_string("casa",4,5))
print(valida_string("casa",2,4))