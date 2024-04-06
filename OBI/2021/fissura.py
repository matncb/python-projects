
N, F = [int(i) for i in input().split()]

m = []

for i in range(N):
    m.append([int(i) for i in list(input())])

queue = []
visitados = []

def bfs(base):
    visitados.append(base)
    queue.append(base)

    while queue:
        s = queue.pop(0)
        x,y = s

        if m[x][y] <= F:

            m[x][y] = "*"
            adjacentes = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            for i in adjacentes:
                a,b = i
                if a<0 or a>N-1 or b<0 or b>N-1 or i in visitados:
                    pass
                else:
                    visitados.append(i)
                    queue.append(i)

bfs((0,0))

for i in m:
    print("".join([str(j) for j in i]))
                    




'''
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s, end=" ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


# Driver Code
bfs(visited, graph, 'A')
'''

'''
verificados = []

def mapear(base):
    x, y = base

    if m[x][y] <= F:
        verificados.append(base)
        m[x][y] = "*"

        adjacentes = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for i in adjacentes:
            a,b = i

            if a<0 or a>N-1 or b<0 or b>N-1 or i in verificados:
                pass   
            else:
                mapear(i)    
    else:
        verificados.append(base)

mapear((0,0))

for i in m:
    print("".join([str(j) for j in i]))
'''
