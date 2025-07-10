import collections as col

Fila_de_espera = col.deque() #criando fila

#adicionando pessoas na fila
Fila_de_espera.append("Pessoa 1")
Fila_de_espera.append("Pessoa 2")
Fila_de_espera.append("Pessoa 3")

Fila_de_espera.popleft() # removendo a primeira pessoa da fila

print(Fila_de_espera) #imprimindo a fila