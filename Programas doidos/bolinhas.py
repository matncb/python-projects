import random
l = []

caixas = [16, 8, 4, 2, 1]
caixas2 = [0, 0, 0, 0, 0]

m6 = 6
M6 = 6 * caixas[0]

while True:
    nt = True
    caixas2 = [0, 0, 0, 0, 0]
    
    for i in range(6):
        x = random.randrange(5)
        caixas2[x] += 1
        
    n = (caixas[0] * caixas2[0]) + (caixas[1] * caixas2[1]) + (caixas[2] * caixas2[2]) + (caixas[3] * caixas2[3]) + (caixas[4] * caixas2[4])
    

    if n> m6 and n<M6:
        for i in l:
            if i == n:
                nt = False
    else:
        nt = False

    if nt:
        l.append(n)
        print(sorted(l))


    
