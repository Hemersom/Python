qtd = int(input('Digite a quantidade de valores da lista: '))
lista = []
if( qtd <= 0):
    exit()
else:
    for i in range(qtd):
        lista.append(int(input(f'Digite o {i+1} valor: ')))

dict = dict.fromkeys(lista)
lista = list(dict)
print(f'Sem valores repetidos: {lista}')
