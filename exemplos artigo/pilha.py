from collections import deque as pilha

pia_suja = pilha() # criando a pilha

#adicionando valores na pilha
pia_suja.append("Prato sujo 1")
pia_suja.append("Prato sujo 2")
pia_suja.append("copo")

pia_suja.pop() #removendo o elemento do topo

print(pia_suja) #imprimindo a pilha