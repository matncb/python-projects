N = int(input())
l = [int(i) for i in input().split()]

while len(l) != 1:
    m = []
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            m.append(1)
        else:
            m.append(-1)
    l = m

if l[0] == 1:
    print("preta")
else:
    print("branca")
