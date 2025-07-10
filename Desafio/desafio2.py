import os
var = 0
lista = []

while(var != -1 ):
    var = float(input('Digite um valor(-1 para parar): '))
    if(var != -1):
        lista.append(var)
    else:
        print('tchau')

    
print("Quantidade de elementos: ",len(lista))
print('Valores: ',end='')
for i in lista:
    print(f'|{i}|',end='')

print()
print('Valores ordem invertida: ')
for i in lista[::-1]:
    print(f'|{i}|')

print(f'Somatorio: {sum(lista)}')
media = round((sum(lista)/len(lista)),2)
print(f'Média: {media}')

print("Valores acima da média: ")
for i in lista:
    if(i > media):
        print(f'| {i}| ',end='')

print() 
print("Valores abaixo da média: ")
for i in lista:
    if(i < media):
        print(f'| {i}| ',end='')

print()
input("Fim do programa!")
os.system("cls")