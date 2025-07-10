def soma(*arg):
    return sum(arg)

lista = []
for i in range(3):
    lista.append(float(input("Insira um número: ")))


print(f'Soma: {soma(lista[0],lista[1],lista[2])}')