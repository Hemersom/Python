import os

medias = []
aprovados = 0
soma = 0

for i in range(10):
    soma = 0
    for i in range(4):
        nota = float(input(f'Insira a {i+1}° nota: '))
        if(nota > 10 or nota < 0):
            print(f'{nota} é invalido!')
            exit()
        else:
            soma = soma + nota

    medias.append(soma/4)
    
    
for i in medias:
    if i >= 7:
        aprovados+=1

print(medias)
print(f'{aprovados} tiveram nota acima da média')