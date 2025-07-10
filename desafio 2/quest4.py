lista = []
for i in range(8):
    lista.append(float(input(f'Digite o {i+1}º valor: ')))

x = int(input('Digite x: '))
y = int(input('Digite y: '))
if(( x < 0 or x >= 8) or(y < 0 or y >= 8)):
    print('Erro')
    exit()
else:
    soma = lista[x]+lista[y]
    print(f'{lista[x]}+{lista[y]} = {soma}')