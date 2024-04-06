N, T = [int(i) for i in input().split()]

cima = [int(i) for i in input().split()]
baixo = [int(i) for i in input().split()]


'''
trocas = []

for i in range(T):
    i, j = [int(i) for i in input().split()]
    i -= 1
    j -= 1
    trocas.append((i,j))


for k in trocas:
    i, j = k
    while i<=j:
        cima[i], baixo[i] = baixo[i], cima[i]
        i += 1
        
for i in cima:
    print(i, end = " ")
'''

'''
trocas = [False] * N

for i in range(T):
    i, j = [int(i) for i in input().split()]
    trocas[i-1:j] = [not(i) for i in trocas[i-1:j]]

for i in range(N):
    if trocas[i]:
        print(baixo[i], end=' ')
    else:
        print(cima[i], end=' ')
'''

pre = [0] * (N + 1)
op = [0] * (N + 1)


for i in range(T):
    i, j = [int(i) for i in input().split()]
    i -= 1
    j -= 1

    op[i] += 1
    op[j+1] -= 1

for i in range(N):
    pre[i] = pre[i-1] + op[i]

for i in range(N):
    if pre[i]%2 == 0:
        print(cima[i], end = ' ')
    else:
        print(baixo[i], end = ' ')
    
    
