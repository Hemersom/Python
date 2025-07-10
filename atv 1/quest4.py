lista = []
for i in range(0,4):
    lista.append(float(input(f'Digite a {i+1}° nota: ')))
    if(lista[i] > 10 or lista[i] < 0):
        print("Nota inválida!")
        exit()
    
print(f'Média das notas: {sum(lista)/len(lista)}')