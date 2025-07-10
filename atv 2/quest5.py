x = float(input("Insira o 1° Valor: "))
y = float(input("Insira o 2° Valor: "))
soma = x+y
sub = x-y
mult = x*y
print(f'Soma: {soma} | tipo: {type(soma)} ')
print(f'Subtração: {sub} | tipo: {type(sub)}')
print(f'Multiplicação: {mult} | tipo: {type(mult)}')
if( y == 0):
    print(f'Divisão impossivel')
    exit()

div = x/y
print(f'Divisão: {round(x/y,3)} | tipo: {type(div)}')