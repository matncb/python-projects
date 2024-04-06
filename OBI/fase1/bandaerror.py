N, M = [int(i) for i in input().split()]
matriz = []
p = []
for i in range(M):
    matriz.append(input().split())

print(matriz)

pont = []

for i in range(N):
    pont.append(i+1)
    p.append(0)
for i in range(M):
    for j in range(2):
        for z in range(len(pont)):
            if matriz[i][j] == pont[z]:
                x = int(matriz[i][2])
                p[z] += x

print(p)
print(pont)
