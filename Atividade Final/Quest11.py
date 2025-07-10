a = []
b = []
c = []
d = []
for i in range(10):
    number = int(input("Insira um valor para o vetor A: "))
    a.append(number)
    number = int(input("Insira um valor para o vetor B: "))
    b.append(number)
    number = int(input("Insira um valor para o vetor C: "))
    c.append(number)
  
for i in range(3):
      d.append(a[i])
      d.append(b[i])
      d.append(c[i])
      
      
print(f'Vetor D: {d}')