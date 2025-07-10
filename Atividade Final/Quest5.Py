numeros = []
pares = []
impares = []

for i in range (20):
    numero = int(input("Digite um numero inteiro: "))
    
    numeros.append(numero)

    if numeros[i] % 2 == 0:
        pares.append(numero)
    else:
       impares.append(numero)

print("Todos os numeros: ", numeros)
print("Numeros pares: ", pares)
print("Numeros impares: ", impares)