qtd = int(input('Digite a quantidade de valores da lista: '))
lista = []
if( qtd <= 0):
    exit()
else:
    num = int(input("Digite um valor: "))

    for i in range(qtd):
        lista.append(int(input(f'Digite o {i+1} valor: ')))

for i in lista:
    if(num == i):
        lista.remove(i)

print(f'Lista sem o valor: {lista}')