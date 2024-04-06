H = list(input())
V = list(input())


def p():
    for i in range(len(H)-1, -1, -1):
        for j in range(len(V)-1, -1, -1):
            if H[i] == V[j]:
                print(i + 1, end = " ")
                print(j + 1)
                return True
    return False

if p() == False:
    print(-1, end = " ")
    print(-1)



