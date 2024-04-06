
n = int(input())

m = []
a = [n] * n

for  i in range(n):
    m.append(a)

def print_bonito(m):
    for i in range(n):
        for j in range(n):
            if (i, j) not in verdes:
                print(m[i][j], end = " ")
            else:
                print("|", end="")
                print(m[i][j], end = "| ")

        print()

def comp(i, j, ver):
    a = -1
    b = -1
    c =-1
    d = -1
    menor = 0
    if i>0:
        a = m[i+1][j]
        if menor == 0:
            menor = a
        if a < menor:
            menor = a
    if j <= n-1:
        b = m[i][j+1]
        if menor == 0:
            menor = b
        if b < menor:
            menor = b
    if i <= n -1:
        c = m[i-1][j]
        if menor == 0:
            menor = c
        if c < menor:
            menor = c
    if j>0:
        d = m[i][j-1]
        if menor == 0:
            menor = d
        if d < menor:
            menor = d

    if menor == a:
        p = (i+1, j)
    if menor == b:
        p= (i, j+1)
    if menor == c:
        p =(i-1, j)
    if menor == d:
        p = (i, j-1)
    
    if p not in ver:
        ver.append(p)
        a, b = p
        comp(a,b, ver)
    else:
        if len(ver) == n:
            return True
        else:
            return False

verdes = []

for i in range(n):
    for j in  range(n):
        ver  = []
        if comp(i, j, ver):
            verdes.append((i,j))






