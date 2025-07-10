lista = []
lista_quadrado = []
for i in range(10):
    lista.append(float(input(f'Digite o {i+1}º valor: ')))
    lista_quadrado.append((lista[i]**2))

for i in range(10):
    print(f'{lista[i]}^2 = {lista_quadrado[i]}')
