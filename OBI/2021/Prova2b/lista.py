import math
N = int(input())
l = [int(i) for i in input().split()]

def p(l):
    menor = -1
    pos = -1
    t = len(l)-1

    for i in range(math.floor((t+1)/2)):
        if l[i] != l[t-i]:
            if menor == -1:
                menor = l[i]
                pos = i
                
            if l[i] < menor:
                menor = l[i]
                pos = i
            if l[t-i] < menor:
                menor = l[t-i]
                pos = t-i
    ant = -1

    if pos < math.floor((t+1)/2):
        if pos>0:
            if l[pos-1] != l[t-pos+1]:
                ant = pos-1
        if l[pos+1] != l[t-pos-1]:
            ant= pos+1
    else:
        if pos <t-1:
            if l[pos+1] != l[t-pos-1]:
                ant = pos+1
        if l[pos-1] !=l[t-pos+1]:
            ant = pos-1


        


    return [menor, pos,ant]
            
def comb(p1, p2, l):
    s = l[p1] + l[p2]
    l[p1] = s
    l.pop(p2)

    return l

cont = 0
while True:
    menor, pos, ant = p(l)

    if menor == -1:
        print(cont)
        break

    cont += 1
    meio = len(l)/2

    if pos < math.floor(len(l)/2):
        p2 = pos+1
    else:
        p2 = pos-1

    if ant != -1:
        p2 = ant

    l = comb(pos, p2, l)
         


