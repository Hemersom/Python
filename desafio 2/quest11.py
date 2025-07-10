lista = []
for i in range(10):
    lista.append(float(input(f'Digite o {i+1}º valor: '))) 

soma_positivos = 0
qtd_negativos = 0

for i in lista:
    if(i < 0):
        qtd_negativos += 1
    else:
        soma_positivos += i

print(f'Quantidade de negativos: {qtd_negativos}')
print(f'Soma dos positivos: {soma_positivos}')