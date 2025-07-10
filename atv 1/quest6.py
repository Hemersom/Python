pi = 3.14
r = float(input("Insira o raio: "))
if(r <= 0):
    print("Valor inválido!")
    exit()
    
print(f'Tamanho da area: {round(pi*r**2,2)}')