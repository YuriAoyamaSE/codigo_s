"""
Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.

Resposta:
"""

def fibonacci(n):
    output = [1,1]
    for i in range(2,n+1):
        output.append(output[i-1]+output[i-2])
    return output

print(fibonacci(10))