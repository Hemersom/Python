lista_notas = []
for i in range(15):
    nota = float(input('Insira a nota: '))
    if(nota < 0 or nota > 10):
        print('erro')
        exit()
    else:
        lista_notas.append(nota)

media = round(sum(lista_notas)/len(lista_notas),2)
print(f'Média geral: {media}')