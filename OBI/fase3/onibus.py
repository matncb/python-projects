import sys

sys.setrecursionlimit(10**5)

'''
N, A, B = [int(i) for i in input().split()]

m = [[False]* (N+1)] * (N+1)

for i in range(N-1):
    x, y = [int(i) for i in input().split()]
    m[x][y] = True

def op(x):
    ops = []
    for i in range(N):
        if m[x][i]:
            ops.append(i)
    return ops


def ma(x):
    for i in x:
        if i == B:
            print(i)
            return i
        else:
            ma(op(i))
        
ma(op(A))
'''
'''
N, A, B = [int(i) for i in input().split()]

cidades = {}

for i in range(N-1):
    X, Y = [int(i) for i in input().split()]

    if not X in cidades:
        cidades[X] = [Y]
    elif Y not in cidades[X]:
        cidades[X].append(Y)

    if not Y in cidades:
        cidades[Y] = [X]
    elif X not in cidades[Y]:
        cidades[Y].append(X)
        
    
comumA = []
comumB = []
lA = []
lB = []

comumA.extend(cidades[A])
lA.append(cidades[A])

comumB.extend(cidades[B])
lB.append(cidades[B])


s = 2

while True:
    stop = False
    for i in comumA:
        for j in comumB:
            if i==j:
                stop = True
                break

    if stop:
        break

    for i in range(len(comumA)):
        comumA.extend(cidades[comumA[i]])

    s += 1

print(s)
'''

N, A, B = [int(i) for i in input().split()]

cidades = {}
for i in range(1, N+1, 1):
    cidades[i] = []

for i in range(N-1):
    X, Y = [int(i) for i in input().split()]
    
    #if Y not in cidades[X]:
    cidades[X].append(Y)

    #if X not in cidades[Y]:
    cidades[Y].append(X)


verificados = []

def mapear(x, cont):
    if not x in verificados:
        if x == B:
            print(cont)
            return True
    
        verificados.append(x)
        for i in cidades[x]:
            mapear(i, cont+1)


mapear(A,0)
    


    
    
    
    
