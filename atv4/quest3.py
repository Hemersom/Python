def calculoImposto(taxa,custo):
    Nvalor = (taxa*custo) + custo
    return round(Nvalor , 2)

taxa = int(input("Insira a porcentagem de imposto: "))
taxa = taxa/100
if(taxa <= 0 or taxa >100): 
    print("Invalido")
    exit()

custo = float(input("Insira o custo do produto: "))
if(custo <= 0): 
    print("Invalido")
    exit()

custo = calculoImposto(taxa,custo)
print(f'O novo valor é: R${custo}')