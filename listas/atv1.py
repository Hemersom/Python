lista = []
for i in range(5):
    lista.append(int(input(f'Insira o {i+1}° valor: ')))

soma = 0

for i in lista:
    soma += i

print(f'Somatorio: {soma}')