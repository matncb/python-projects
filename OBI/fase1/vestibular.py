N = int(input())
r = list(input())
g = list(input())
s = 0

for i in range(N):
    if r[i] == g[i]:
        s += 1

print(s)
