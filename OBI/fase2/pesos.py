'''
N = int(input())
l = [int(i) for i in input().split()]
b = l
c = []
nao = False

for i in range(len(l)):
    if l[i]<=8:
        c.append(l[i])
        b[i] = 0
k = c

def v():
    s = 0
    for i in c:
        for j in l:
            if i==j:
                s += 1
    if s == len(l):
        return True
    else:
        return False
    



while len(c) != len(l):
        for i in range(len(b)):
            for j in range(len(c)):
                if len(c) != len(l):
                    if b[i]!=0:
                        if b[i]<= 8:
                            c.append(b[i])
                            b[i] = 0
                        elif b[i] - c[j] <= 8 or b[i] - c[j] <= -8:
                            b[i], c[j] = c[j], b[i]
                else:
                    break
        if k==c and b == l and len(c) != len(l):
            nao = True
            print("N")
            break
            


'''
'''
while True:
    x = v()
    if x == False:
        for i in range(len(b)):
            for j in range(len(c)):
                x = v()
                if x == False:
                    if b[i]!=0:
                        if b[i]<= 8:
                            c.append(b[i])
                            b[i] = 0
                        elif b[i] - c[j] <= 8 or b[i] - c[j] <= -8:
                            b[i], c[j] = c[j], b[i]
                else:
                    break
        x = v()
        #if k==c and b == l and x == False:
            #nao = True
            #print("N")
            #break
    else:
        break

'''

'''

if nao == False:
    print("S")
                        

'''
'''
N = int(input())
l = [int(i) for i in input().split()]
b = l
c = []
nao = False

for i in range(len(l)):
    if l[i]<=8:
        c.append(l[i])
        b[i] = 0
k = c

while len(c) != len(l):
        for i in range(len(b)):
            for j in range(len(c)):
                if len(c) != len(l):
                    if b[i]!=0:
                        if b[i]<= 8:
                            c.append(b[i])
                            b[i] = 0
                        elif b[i] - c[j] <= 8 or b[i] - c[j] <= -8:
                            b[i], c[j] = c[j], b[i]
                else:
                    break
        if k==c and b == l:
            nao = True
            print("N")
            break


if nao == False:
    print("S")
'''

N = int(input())
l = [int(i) for i in input().split()]
b = l
c = []

for i in range(len(l)):
    if l[i]<=8:
        c.append(l[i])
        b[i] = 0

cont = 0
nao = False

while len(c) != len(l):
    if cont <= 2**N:
        for i in range(len(b)):
            for j in range(len(c)):
                if len(c) != len(l):
                    if b[i]!=0:
                        if b[i]<= 8:
                            c.append(b[i])
                            b[i] = 0
                        elif b[i] - c[j] <= 8 or b[i] - c[j] <= -8:
                            b[i], c[j] = c[j], b[i]

                else:
                    break
    
        cont += 1
    else:
        print("N")
        nao = True
        break

if nao == False:
    print("S")
