import os

frutas = ["maçã", "banana", "uva","mirtilo"]
carnes = ["boi", "frango", "porco"]
dicionario = {"frutas": frutas, "carne":carnes}

escolha = 1
while(escolha != 0):
    print("""
      1 - Ver elementos;
      2 - Adicionar elementos;
      3 - Remover elementos;
      4 - Procurar elemento;
      0 - Sair""")
    
    escolha = int(input("Escolha uma opção >>> "))
    
    if(escolha == 1):
        print(f'Elementos do dicionario: {dicionario}')
        input("Aperte enter para continuar...")
        os.system("cls")
        
    elif(escolha == 2):
        chave = str(input("Insira a chave: "))
        valor = str(input("Insira o valor: "))
        
        try:
            dicionario[chave].append(valor)
        except:
            Nlista = [valor]
            dicionario[chave] = Nlista
        finally:
            print("valor adicionado !")
            input("Aperte enter para continuar...")
            os.system("cls")
        
    elif(escolha == 3):
        chave = str(input("Insira a chave: "))
        valor = str(input("Insira o valor: "))
        
        if valor in dicionario[chave]:
            dicionario[chave].remove(valor)
            print("Removido com sucesso!")
        else:
            print(f'{valor} Não pertence ao dicionario!')
        
        input("Aperte enter para continuar...")
        os.system("cls")
            
    elif( escolha == 4):
        valor = str(input("Insira o valor: "))
        chave = str(input("Insira a chave: "))
        try:
            if valor in dicionario[chave]:
                print('Valor encontrado!')
                print(f'{dicionario[chave]}')
        except:
            print('Valor não encontrado!')
        
        finally:
            input("Aperte enter para continuar...")
            os.system("cls")
            
    else:
        print('Adeus!')
        exit()