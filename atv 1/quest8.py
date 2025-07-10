ganho_por_hora = float(input("Digite quanto vc ganha por hora: "))
if(ganho_por_hora <= 0):
    print("Valor inválido!")
    exit()
    
horas_trabalhadas = int(input("Insira as horas trabalhadas: "))
if(horas_trabalhadas <= 0):
    print("Valor inválido!")
    exit()
    
print(f'Salário: R${round(ganho_por_hora*horas_trabalhadas,2)}')