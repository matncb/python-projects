N, I, F = [int(i) for i in input().split()]

V = [int(i) for i in input().split()]
s = 0

for i in range(N):
    for j in range(N):
        if j>i:
            if V[j] != V[i]:
                if (V[i] + V[j]) >= I and (V[i] + V[j]) <= F:
                    s += 1

print(s)
