nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
if(idade <= 0):
    print("Idade inválida")
    exit()

cdd = str(input("Digite sua cidade: "))

dic = {'Nome': nome, 'Idade': idade, 'Cidade': cdd}
print(f'Nome: {dic['Nome']}')