lista = []
pares = 0
for i in range(10):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))
    if(lista[i] % 2 == 0):
        pares += 1
    
print(f'Possui {pares} valores pares!')