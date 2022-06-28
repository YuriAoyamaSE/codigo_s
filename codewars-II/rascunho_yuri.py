# inss
# usar POO para inss e irrf?

remuneracao = int()
i = 0
recolhimento = 0

faixa_remuneracao = (
    1212.00, 
    2427.35,
    3641.03,
    7087.22)

aliquota = (
    0.075,
    0.09,
    0.12,
    0.14
)

for _ in faixa_remuneracao:
    if faixa_remuneracao[i] < remuneracao:
        remuneracao -= faixa_remuneracao[i]
        recolhimento += faixa_remuneracao[i] * aliquota[i]
    else:
        recolhimento += remuneracao * aliquota[i]
    i += 1

###################### rascunho 2 ##############
remuneracao = int()
recolhimento = 0

faixa_aliquota = {
    1212.00 : 0.075, 
    2427.35 : 0.09,
    3641.03 : 0.12,
    7087.22 : 0.14
}

for faixa, aliquota in faixa_aliquota:
    if faixa < remuneracao:
        remuneracao -= faixa
        recolhimento += faixa * aliquota
    else:
        recolhimento += remuneracao * aliquota
        break #return recolhimento
#return recolhimento

