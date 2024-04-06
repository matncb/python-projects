T, L, O, D = [int(i) for i in input().split()]

l = []

for i in range(L):
    a = [int(i) for i in input().split()]
    a.pop(0)
    l.append(a)

def adj(t):
    adjacentes = set()
    for i in l:
        if t in i:
            j = set(i)
            adjacentes = adjacentes.union(set(i))
    
    return list(adjacentes)

queue = []
visitados = []

def bfs(base, fim):
    queue.append([base])
    visitados.append(base)

    while queue:
        path = list(queue[0])
        #print(path)
        queue.pop(0)

        adjacentes = adj(path[-1])
        #print(adjacentes)

        for i in adjacentes:
            if i not in visitados:
                new_path = list(path)
                new_path.append(i)
                
                if new_path[-1] == fim:
                    return new_path
                else:
                    queue.append(new_path)
                    visitados.append(i)

print(len(bfs(O, D))-1)




