qtd = int(input('Digite a quantidade de valores da lista: '))
lista = []
if( qtd <= 0):
    exit()
else:
    num = int(input("Digite um número especifico: "))

    for i in range(qtd):
        lista.append(int(input(f'Digite o {i+1} valor: ')))

qtdv = 0
for j in lista:
    if( j == num):
        qtdv += 1

print(f'Quantidade de vezes repetidas: {qtdv}')