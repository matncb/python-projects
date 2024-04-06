N = int(input())
m = []

for i in range(N):
    n = [int(i) for i in input().split()]
    m.append(n)

for i in range(N):
    for j in range(N):
        if i!= 0 and j!=0:
            if m[i-1][j-1] + m[i-1][j] + m[i][j-1] >=2:
                m[i][j] = 0
            else:
                m[i][j] = 1

print(m[N-1][N-1])

        
