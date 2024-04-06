grafo = [0 ,1, 2, 3, 4]

adjacencia = [[2, 1], [], [3, 4], [4], []]
visitados = []

def DFS(base):
    visitados.append(base)

    for i in adjacencia[base]:
        if i not in visitados:
            print(i)
            DFS(i)

print("DFS:")
DFS(0)
print()

queue = []
visitados = []

def BFS(base):
    queue.append(base)
    visitados.append(base)

    while queue:
        s = queue[0]
        queue.pop(0)

        for i in adjacencia[s]:
            if i not in visitados:
                print(i)
                queue.append(i)
                visitados.append(i)

print("BFS")  
BFS(0)
print()

queue = []
visitados = []

def BFS_short(inicio, fim):
    queue.append([inicio])
    visitados.append(inicio)

    while queue:
        path = queue.pop(0)
        node = path[-1]

        for i in adjacencia[node]:
            if i not in visitados:
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)
                visitados.append(i)
                if i == fim:
                    print(new_path)
                    return

    print(-1)

BFS_short(0, 4)
print()

queue = []
visitados = []
paths = []

def BFS_max(inicio, fim):
    queue.append([inicio])
    visitados.append(inicio)

    while queue:
        path = queue.pop(0)
        node = path[-1]

        for i in adjacencia[node]:
            if i not in visitados:
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)
                if i == fim:
                    paths.append(new_path)
                    
    paths.sort()

    print(paths[0])


BFS_max(0,4)



        
    