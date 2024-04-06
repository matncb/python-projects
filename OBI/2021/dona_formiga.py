S, T, P = [int(i) for i in input().split()]
sh = [int(i) for i in input().split()]
sl = [[] for i in range(T)]

for i in range(T):
    s1, s2 = [int(i) for i in input().split()]
    s1 -= 1
    s2 -= 1

    if sh[s1] > sh[s2]:
        sl[s1].append(s2)
    else:
        sl[s2].append(s1)

visitados= []

C = [0]

def bfs(base, c):
    visitados.append(base)
    adjacentes = sl[base]

    for i in adjacentes:
        C.append(c+1)
        bfs(i, c+1)
            
        
bfs(P-1, 0)

print(max(C))

