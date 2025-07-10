lista = []
pares = 0
while(True):
    num = int(input('Digite um valor: '))
    if(num % 2 == 0):
        pares += 1
        lista.append(num)
    if(pares == 6):
        break


print(f'Valores: {lista}')