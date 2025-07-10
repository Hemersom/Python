perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

cont = 0
situacao =''
for i in range(5):
    print(perguntas[i])
    escolha = int(input('1 - Sim;\n0 - Não;\n>>> '))
    if(escolha != 1 and escolha != 0):
        print(f'Inválido')
        exit()
    elif(escolha == 1):
        cont += 1
    
if(cont == 0):
    situacao = "Inocente"
elif(cont == 2):
    situacao = "Suspeito"
elif(cont < 5):
    situacao = "Cúmplice"
else:
    situacao = "Assassino"

print(f'Vc é {situacao}')