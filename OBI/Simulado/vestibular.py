N = int(input())
g = list(input())
c = list(input())
s = 0

for i in range(N):
    if c[i] == g[i]:
        s += 1

print(s)
