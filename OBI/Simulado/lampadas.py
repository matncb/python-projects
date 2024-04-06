N = int(input())
l = [int(i) for i in input().split()]

a = 0
b = 0

for i in range(N):
    if l[i] == 1:
        if a == 1:
            a = 0
        else:
            a = 1
    else:
        if a == 1:
            a = 0
        else:
            a = 1
        if b == 1:
            b = 0
        else:
            b = 1

print(a)
print(b)
