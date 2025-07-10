lista = []
for i in range(6):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))


print(f'Ordem normal: {lista}')
print(f'Ordem inversa: {lista[::-1]}')