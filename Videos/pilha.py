from collections import deque
historico = deque()

historico.append("Página Inicial")
historico.append("Sobre nós")
historico.append("Contato")

print("Página Atual: ",historico[-1])
print("Voltando: ",historico.pop())
print("Página Atual: ",historico[-1])
print("Voltando: ",historico.pop())
print("Página Atual: ",historico[-1])
# print("Voltando: ",historico.pop())
if(len(historico) == 0):
    print("Vazio!")
else:
    print("Ainda tem uma página aberta!")

