lista = []
lista.append(str(input("Digite seu nome: ")))
lista.append(int(input("Digite sua idade: ")))
if(lista[1] <= 0):
    print("Idade inválida")
    exit()
    
lista.append(float(input("Digite sua altura: ")))
if(lista[2] <= 0):
    print("Altura inválida")
    exit()
    
print(f'Nome: {lista[0]} | Idade: {lista[1]} | Altura: {lista[2]}')