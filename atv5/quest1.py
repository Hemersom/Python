lista = []
for i in range(5):
    num = int(input(f'Digite o {i+1}º valor: '))
    lista.append(num)


soma = sum(lista)
print(f'Soma dos valores: {soma}')