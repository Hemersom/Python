import os
def add(lista_compras):
    item = input('Digite um produto para a lista: ')
    if item in Lista_compras:
        print('Produto repetido!')
    else:
        Lista_compras.append(item)
        print('Produto adcionado com sucesso!')
    return Lista_compras

def procurar(lista_compras):
    if((input('Digite o produto: ')) in Lista_compras):
        print('Produto encontrado!')
    else:
        print('Produto ñ encontrado!')

def Mostrar(lista_compras):
    for i in Lista_compras:
        print(f'|{i}|-',end='')
    print('FIM')

def remover(lista_compras):
    try:
        Lista_compras.remove(input('Digite o produto que deseja remover: '))
        print('Produto removido com sucesso!')
    except:
        print('Produto não encontrado!')
    finally:
        return Lista_compras
    
Lista_compras = []

while(True):
    os.system("pause")
    os.system("cls")
    print("""+---------Menu---------+
    1 - Adcionar item;
    2 - Verificar item;
    3 - Mostrar lista;
    4 - Excluir item;
    0 - Sair;""")
    try:
        esc = int(input('>>>'))
    except:
        print('NaN')
        exit()

    if (esc == 1):
        Lista_compras = add(Lista_compras)
    elif(esc == 2):
        procurar(Lista_compras)
    elif(esc == 3):
        Mostrar(Lista_compras)
    elif(esc == 4):
        Lista_compras = remover(Lista_compras)
    else:
        exit()
