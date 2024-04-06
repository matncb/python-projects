N = int(input())
M = int(input())

v = [False for i in range(N)]
vi = [0]

for i in range(M):
    vi.append(int(input()))


'''
maximo = [0]
def DFS(c, vagas):
    if (c+1) <= M:
        for i in range(vi[c+1]):
            if vagas[i] == False:
                new_vaga = vagas
                new_vaga[i] = True
                if c > maximo[0]:
                    maximo[0] = c
                DFS(c+1, new_vaga)

DFS(1, v)
print(maximo[0])
'''

queue = []

def BFS(base):
    queue.append([base])
    t = 0

    while queue:
        s = queue[0]
        queue.pop(0)
        if len(s) <= M:
            for i in range(1, vi[len(s)] + 1):
                new_path = list(s)
                new_path.append(i)
                if len(new_path) > t:
                    t = len(new_path)
                queue.append(new_path)
    return t

t = []   
for i in range(1, vi[1] + 1):
    t.append(BFS(i))

print(max(t))
        