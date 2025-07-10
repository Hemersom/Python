def inverso(num):
    txt = str(num)
    return int(txt[::-1])

num = int(input('Insira um número: '))
print(f'Inverso de {num}: {inverso(num)}')