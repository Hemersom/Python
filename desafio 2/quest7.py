lista = []
for i in range(10):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))


print(f'Maior: {max(lista)}')
print(f'Posição: {lista.index(max(lista))+1}')