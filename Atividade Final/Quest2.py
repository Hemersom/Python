lista = []

for i in range (10):
    vet = input(f'Digite o {i+1}º elemento: ')
    
    lista.append(vet)

print("Lista original: ", lista)

lista.reverse()

print("Lista inversa: ", lista)