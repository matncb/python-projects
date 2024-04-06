
N, M = [int(i) for i in input().split()]

m = []

'''
manchas = []

class mancha:
    def __init__(self, i, j):
        self.pix = [(i, j)]
        
    def ver(self, value):
        if value in self.pix:
            return True

def varrer_mancha(x):
    for i in range(len(manchas)):
        if manchas[i].ver(x):
            return i

def pos_con(x, y):
    i1, j1 = x
    i2, j2 = y

    if i1 == i2 and j1 + 1 == j2:
        return True

    if i1 == i2 and j1 - 1 == j2:
        return True

    if j1 == j2 and i1 + 1 == i2:
        return True

    if j1 == j2 and i1 - 1 == i2:
        return True

    return False
    
    
def mapear(i, j):
    m[i][j] = -1

    if j<M-1:  
        if m[i][j+1] == -1:
            manchas[varrer_mancha((i, j+1))].pix.append((i, j))
            return True
  
    if j>0:
        if m[i][j-1] == -1:
            manchas[varrer_mancha((i, j-1))].pix.append((i, j))
            return True

    if i<N-1:
        if m[i+1][j] == -1:
            manchas[varrer_mancha((i+1, j))].pix.append((i, j))
            return True
   
    if i>0:
        if m[i-1][j] == -1:
            manchas[varrer_mancha((i-1, j))].pix.append((i, j))
            return True

    return False

for i in range(N):
    m.append([int(i) for i in input().split()])

s = 0

for i in range(N):
    for j in range(M):
        if m[i][j] == 1:
            if mapear(i, j) == False:
                s += 1
                manchas.append(mancha(i, j))
                
v = 0

for i in manchas:
    for j in i.pix:
        for k in manchas:
            if k != i:
                for y in k.pix:
                    if pos_con(j,y):
                        v += 1
                    
v = v/2
s -= v

print(int(s))

'''

class mancha:
    def __init__(self, l):
        self.pix = []
        self.pix.extend(l)
        
manchas = []

for i in range(N):
    lista = [int(i) for i in input().split()]

    x = 0
    y = False
    a = 0
    
    for x in range(M):   
        if lista[x] == 1:
            if y == False:
                manchas.append(mancha([(i, x)]))
                a = len(manchas) - 1
                y = True
            else:
                manchas[a].pix.append((i, x))
        else:
            y = False
            
        
    m.append(lista)


def pos_con(x, y):
    i1, j1 = x
    i2, j2 = y

    if i1 == i2 and j1 + 1 == j2:
        return True

    if i1 == i2 and j1 - 1 == j2:
        return True

    if j1 == j2 and i1 + 1 == i2:
        return True

    if j1 == j2 and i1 - 1 == i2:
        return True

    return False


new_manchas = []

for i in manchas:
    for j in i.pix:
        for k in manchas:
            if k != i:
                for y in k.pix:
                    if pos_con(j,y):
                        l = i.pix + k.pix
                        new_manchas.append(mancha(l))






            

 
