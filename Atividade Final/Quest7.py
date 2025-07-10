lista = []
soma = 0
mult = 0
for i in range(5):
    lista.append(int(input("Insira um valor: ")))
    soma += lista[i]
    if (mult ==0):
        mult += lista[i]
    else:
        mult *= lista[i]
    

print(f'Valores: {lista}')
print(f'Soma dos valores: {soma}')
print(f'Multiplicação dos valores: {mult}')