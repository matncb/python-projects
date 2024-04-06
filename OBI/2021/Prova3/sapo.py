
N, M = [int(i) for i in input().split()]
P = int(input())

p = []
for i in range(P):
    a, b = [int(i) for i in input().split()]
    p.append((a,b))

S1, S2 = [int(i) for i in input().split()]
S = (S1, S2)

R1, R2 = [int(i) for i in input().split()]
R = (R1, R2)

def mod(x):
    if x<0:
        return x*(-1)
    else:
        return x

def adj(base):
    a, b = base
    adjacentes = []
    for i in p:
        x,y = i
        if x == a:
            d = mod(y-b)
            if d<=3:
                adjacentes.append(i)
        elif y == b:
            d = mod(x-a)
            if d<=3:
                adjacentes.append(i)
    return adjacentes

queue = []
visitados = []

def BFS(inicio, fim):
    queue.append(inicio)
    visitados.append(inicio)

    while queue:
        s = queue[0]
        queue.pop(0)

        for i in adj(s):
            if i not in visitados:
                if i == fim:
                    return "S"
                else:
                    queue.append(i)
                    visitados.append(i)

    return "N"

print(BFS(S, R))



