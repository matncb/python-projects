N = int(input())
m = []

for i in range(N):
    m.append([])
    for j in range(N):
        if i%2 == 0:
            if j%2 == 0:
                m[i].append("X")
            else:
                m[i].append("O")
        else:
            if j%2 == 0:
                m[i].append("O")
            else:
                m[i].append("X")

for i in range(N):
    print(m[i])

