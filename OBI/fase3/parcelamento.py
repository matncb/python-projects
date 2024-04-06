V = int(input())
P = int(input())

p = []

for i in range(P):
    p.append(V//P)

cont = V%P

while cont>0:
    for i in range(len(p)):
        p[i] += 1
        cont -= 1
        if cont == 0:
            break

for i in range(len(p)):
    print(p[i])
