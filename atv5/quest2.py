lista = []
for i in range(5):
    num = int(input(f'Digite o {i+1}º valor: '))
    lista.append(num)


soma = sum(lista)
media = soma/ len(lista)
print(f'Soma dos valores: {soma}')
print(f'Média: {round(media,2)}')
lista_maior = []
lista_menor = []
for i in lista:
    if(i < media):
        lista_menor.append(i)
    else:
        lista_maior.append(i)

print("Valores acima da média: ",lista_maior)
print("Valores abaixo da média: ",lista_menor)