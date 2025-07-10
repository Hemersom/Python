qtd = int(input('Digite a quantidade de valores da lista: '))
lista1 = []
lista2 = []
if( qtd <= 0):
    exit()
else:
    for i in range(qtd):
        lista1.append(int(input(f'Digite o {i+1} valor da lista 1: ')))
        lista2.append(int(input(f'Digite o {i+1} valor da lista 2: ')))

n_lista =[]
for i in lista1:
    for j in lista2:
        if(i == j):
            n_lista.append(i)

print(f'Elementos de ambas: {n_lista}')