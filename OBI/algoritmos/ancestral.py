grafo = [1,2,3,4,5,6,7,8,9,10,11,12,13]
arestas = [[1,2], [1,3], [1,4], [3,5], [3,6], [3,7], [6,8], [6,9], [7,10], [7,11], [10,12], [10,13]]

adjacencia = [set() for i in range(14)]

for i in range(1, 14):
    for j in arestas:
        if i in j:
            adjacencia[i] = adjacencia[i].union(j)

visitados = []
A = 5
B = 2
pathA = []
pathB = []

def DFS(base, p):
    visitados.append(base)
    path = list(p)
    path.append(base)

    for i in adjacencia[base]:
        if i not in visitados:
            if i == A:
                pathA.append(path)
            if i == B:
                pathB.append(path)
            DFS(i, path)

DFS(1,[1])

pathA[0].pop(0)
pathB[0].pop(0)

pathA = set(pathA[0])
pathB = set(pathB[0])

ancestral = pathA.intersection(pathB)
ancestral = list(ancestral)
print(ancestral[-1])


