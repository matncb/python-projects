'''N = int(input())
matrizE = []
matriz = []
soma = 101
it = 0
jt = 0
repete = N
acres = 0
somat = 0
for i in range(N):
    matriz.append(input().split())
    matrizE.append(matriz[i])
    for j in range(N):
        matriz[i][j] = int(matriz[i][j])
        matrizE[i][j] = 1
        
for k in range(N):
    if(j!=N and j>=acres):
        for j in range(N):
            for i in range(N):
                somat += matriz[i][j]
                if (somat<soma and matrizE[i][j]==1):
                    soma = somat
                    jt = j
        for i in range (N):
            matrizE[i][jt] = 0
        repete += -1
        acres += 1
        soma = 101
for j in range(N):
    matrizE[N-1][j] = 0

soma = 0

for i in range(N):
    for j in range(N):
        if(matrizE[i][j] ==0):
            soma += matriz[i][j]

print(soma)
'''
'''
N = int(input())
matriz = []
soma = 101
soma1 = 0
total = 0
pos = []
jt = 0
jd = 0
iantes = 0

for i in range (N):
    matriz.append(input().split())
    for j in range(N):
        matriz[i][j] = int(matriz[i][j])

for y in range(N):        
    for i in range(N):
        for j in range(N):
            for w in range(len(pos)):
                if (pos[w][1] == j):
                    j += 1
            jafoi = False
            soma1 += matriz[j][i]
            for k in range(len(pos)):
                if (j == pos[k][0]):
                    jafoi = True
            if (jafoi == False):
                jt = j
                iantes = i
        if (soma1 < soma):
            soma = soma1
            jd = jt
            diantes = iantes
        soma1 = 0
        jt = 0
        iantes
    total += soma
    pos.append([jd,diantes])

    print(soma)
    print(pos)
print(total)
'''
N = int(input())
matriz = []
dic = {}

for i in range (N):
    matriz.append(input().split())
    for j in range(N):
        matriz[i][j] = int(matriz[i][j])

print(matriz)



for i in range(N):
    if(i!=0 and i!=N-1)
        dic[i] = matriz[i] + matriz[i+1][i]
    
