l = []
cont = 1
pos = 271120

while len(l)< pos:
    c = str(cont)
    c = list(c)
    for i in c:
        l.append(i)

    cont += 1

print(l[pos-1])

    

