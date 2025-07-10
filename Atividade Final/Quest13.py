meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp = []
for i in meses:
    temp.append(int(input(f'Digite a temperatura média de {i}: ')))
    
    
media = round(sum(temp)/len(temp),0)
print(f'Média: {media}ºC')
print("Meses acima da média:")
for i in range(12):
    if(temp[i] > media):
        print(f'{meses[i]}: {temp[i]}ºC')
        