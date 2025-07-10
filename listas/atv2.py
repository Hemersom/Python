dic  = {'nome': str(input('Digite seu nome: '))}
lista = []
for i in range(3):
    lista.append(float(input(f'Insira a {i+1}° nota: ')))
    if(lista[i] < 0 or lista[i] > 10):
        print('Nota invalida')
        exit()
    
    dic['Notas'] = lista
soma = 0
for i in dic['Notas']:
    soma += i

print(f'o aluno {dic["nome"]} obteve a média: {round(soma/3,2)}')
    
