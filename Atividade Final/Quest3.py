notas = []
media = 0

for i in range (4):
    nota = float(input(f'Digite a {i+1}º nota: '))

    notas.append(nota)
    media += notas[i]

media = media/4

print ('Notas: ', notas)

print ('Media: ', media)