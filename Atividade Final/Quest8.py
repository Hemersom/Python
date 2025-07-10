idade = []
altura = []
for i in range(5):
    idd = int(input('Insira a idade: '))
    
    if(idd <= 0):
        print('Idade invalida')
        exit()
        
        
    idade.append(idd)
    
    alt = float(input('Insira a altura: '))
    
    if(alt <= 0):
        print('Altura invalida')
        exit()
        
    altura.append(alt)

print("Idades: ")
for i in idade[::-1]:
    print(f' |{i}| ',end='')
  
  
print()  
print("Alturas: ")
for i in altura[::-1]:
    print(f' |{i}| ',end='')