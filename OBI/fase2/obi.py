N, P = [int(i) for i in input().split()]
s = 0

for i in range(N):
    X, Y = [int(i) for i in input().split()]
    if X + Y >= P:
        s += 1

print(s)
