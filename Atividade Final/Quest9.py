a = []
soma = 0
for i in range(10):
    number = int(input("Insira um valor: "))
    a.append(number)
    
for i in a:
    soma += i**2
    
print(f'Resultado: {soma}')