a = []
b = []
c = []
for i in range(10):
    number = int(input("Insira um valor para o vetor A: "))
    a.append(number)
    number = int(input("Insira um valor para o vetor B: "))
    b.append(number)
  
for i in range(3):
      c.append(a[i])
      c.append(b[i])
      
      
print(f'Vetor C: {c}')