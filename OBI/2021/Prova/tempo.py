N = int(input())

m = []
d = {}

anterior = False

'''
for i in range(N):
    evento, x = input().split()
    x = int(x)
    if evento == "R":
        if x not in m:
            m.append(x)
            d[x] = [1, False]
            anterior = x

    elif evento == "T":
        for j in range(len(d)):
            a = d[m[j]]
            if a[1] == False:
                if m[j] != anterior:
                    a[0] += x
                    d[m[j]] = a
                else:
                    a[0] += x-1
                    d[m[j]] = a

    else:
        anterior = None

        b = d[x]
        b[1] = True
        d[x] = b

        for k in range(len(d)):
            n = d[m[k]]
            if n[1] == False:
                n[0] += 1
            d[m[k]] = n


m = sorted(m)

for i in m:
    c = d[i]
    print(i, end =' ')
    if c[1] == True:
        print(c[0])
    else:
        print(-1)
    
'''
for i in range(N):
    evento, x = input().split()
    x = int(x)

    if evento == "R":
        
        if anterior == False:
            for l in range(len(d)):
                o = d[m[l]]
                if o[1] == False:
                    o[0] += 1
                    d[m[l]] = o

        if x not in m:
            m.append(x)
            d[x] = [0, False]
        else:
            p = d[x]
            p[1] = False
            d[x] = p
        
        anterior = False

    elif evento == "T":
        for j in range(len(d)):
            a = d[m[j]]
            if a[1] == False:
                a[0] += x
                d[m[j]] = a

        anterior = True

    else:

        if anterior == False:
            for k in range(len(d)):
                n = d[m[k]]
                if n[1] == False:
                    n[0] += 1
                    d[m[k]] = n

        b = d[x]
        b[1] = True
        d[x] = b


        anterior = False

        

m = sorted(m)

for i in m:
    c = d[i]
    print(i, end =' ')
    if c[1] == True:
        print(c[0])
    else:
        print(-1)