A = int(input())
S = int(input())
D = int(input())

h = 0
d = 0

while h<A:
    h+=S
    d += 1
    if h<A:
        h-=D


print(d)
