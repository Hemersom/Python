l = float(input("Insira um lado do quadrado: "))
if(l <= 0):
    print("Valor inválido!")
    exit()
    
area = l**2
print(f'Area do quadrado: {round(area,2)}')
print(f'Dobro da area do quadrado: {round(area*2,2)}')