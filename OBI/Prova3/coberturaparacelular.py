import sys

sys.setrecursionlimit(10**5)


N = int(input())

p = []
ligs = {}

for i in range(N):
    x, y = [int(i) for i in input().split()]
    p.append((x,y))
    ligs[(x,y)] = []

A = int(input())

def d(a,b, dm):
    Xa, Ya = a
    Xb, Yb = b
    dis = (((Xb - Xa)**2) + ((Yb-Ya)**2))**0.5

    if dis>dm:
        return False
    else:
        return True


def lig():
    for i in p:
        for j in p:
            if i != j:
                if d(i,j,A):
                    ligs[i].append(j)

lig()

verificados = []

def mapear(i, m):
    verificados.append(i)
    
    if m == N:
        responder("S")
        return True
    
    ops = ligs[i]

    for i in ops:
        if not i in verificados:
            mapear(i, m+1)

def responder(resposta):
        print(resposta)
        global respondido
        respondido = True
         
mapear(p[0], 1)

try:
    x = respondido
except:
    print("N")





    

    





