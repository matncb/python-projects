

N = int(input())
l =[int(i) for i in input().split()]
t = sum(l)

def ap(a, b):
    direita = 0
    esquerda = 0
    d = -1
    for i in range(N):
        if l[i] == a or l[i] == b:
            d = d*-1
        if d == -1:
            esquerda +=1
        else:
            direita +=1 

    return direita, esquerda

foi = False           
for i in range(N):
    for j in range(N):
        if l[i] != l[j]:
            dist1, dist2  = ap(l[i], l[j])
            if dist1 > dist2:
                d_max = dist1
                d_min = dist2
            else:
                d_max = dist2
                d_min = dist1

            d = (t - 2*d_max)/2
            p = i
            if i < j:
                p = i
            else:
                p = j

            sub = 0

            while sub < d:
                sub += l[p]
                p-=1

            if sub == d:
                foi = True

if foi:
    print("S")
else:
    print("N")
            





