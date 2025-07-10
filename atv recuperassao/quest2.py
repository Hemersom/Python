lista1 = []
lista2 = []
def comparar(l1,l2):
    iguais = 1
    for i in l1:
        for j in l2:
            if j not in l1:
                iguais = 0
                break

    if(iguais == 1):
        print("Iguais")
    else:
        print("Diferentes")  
try:
    qtd = int(input('Quantos itens terão em cada lista: '))
    if (qtd <= 0):
        print('Quantidade inválida!')
    else:
        for i in range(qtd):
            lista1.append(input('Digite o item da lista1: '))
            lista2.append(input('Digite o item da lista2: '))
        comparar(lista1,lista2)
except:
    print('Inválido')