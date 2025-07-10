vogais = "aeiouAEIOU"
consoantes_lidas = []
contador_consoantes = 0

for i in range(10):
    caractere = input("Digite um caractere: ")

    if caractere not in vogais: 
        consoantes_lidas.append(caractere)
        contador_consoantes += 1

print("Consoantes lidas:", consoantes_lidas)
print("Total de consoantes:", contador_consoantes)