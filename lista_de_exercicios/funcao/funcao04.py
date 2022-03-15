from random import sample

def embaralha_palavra(palavra):    
    embaralhado = sample(palavra, k=len(palavra))
    return ''.join(embaralhado).lower()

print(embaralha_palavra("Python"))
