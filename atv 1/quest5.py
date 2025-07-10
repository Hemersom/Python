m = float(input("insira um valor(em m): "))
if(m <= 0):
    print("Valor inválido!")
    exit()
    

print(f'{m} metros Convertido em cm: {round(m,3)}')