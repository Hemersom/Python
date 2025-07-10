A = [1, 0, 5, -2, -5, 7]

soma = int(A[0] + A[1]+ A[5])

print(f'Soma dos valores nas posições A[0], A[1] e A[5]: {soma}')

A[3] = 100


for i in A:
    print(f'|{i}|')