N = int(input())
M = int(input())

c = []

for i in range(M):
    U, V = [int(i) for i in input().split()]
    c.append([U,V])

pares = []
for i in range(1,N+1):
    for j in range(1, N+1):
        par = [i,j, i+j]
        if [j,i, i+j] not in pares:
            pares.append(par)

def soma(a):
    return a[2]

pares.sort(key=soma)


