def moldura(linha,coluna):
    for i in range(linha):
        if(i == 0 or i == linha-1):
            print('|',end='')
        else:
            print()
        for j in range(coluna):
            
            if(i == 1 or i == coluna-1):
                print('-',end='')


moldura(5,5)
