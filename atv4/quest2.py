def positivoNegativo(arg):
    if(arg > 0):
        return 'P'
    else:
        return 'N'
    

num = float(input("Insira um valor: "))
print(f'{positivoNegativo(num)}')
