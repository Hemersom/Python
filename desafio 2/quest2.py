lista_int = [] 
lista_reais = []
lista_q =[]
for i in range(6):
    lista_int.append(int(input(f'Digite o {i+1}º valor')))

print(f'Valores lidos: {lista_int}')
for i in range(10):
    lista_reais.append(float(input(f'Digite o {i+1}º valor')))
    lista_q.append(lista_reais[i]**2)

print(f'Quadrado dos valores: {lista_q}')