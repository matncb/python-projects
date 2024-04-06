L1 = int(input())
L2 = int(input())

C1 = int(input())
C2 = int(input())

def pontos(x, y):
    s = x+y
    if x == y:
        s = s*2
    elif x+1 == y or x-1 == y:
        s = s*3

    return s

l = pontos(L1, L2)
c = pontos(C1, C2)

if l>c:
    print("Lia")
elif c>l:
    print("Carolina")
else:
    print("empate")
