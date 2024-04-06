f = 2021

def fatorial(f):
    r = 1
    for i in range(f, 1, -1):
        r = r*i
    return r

def soma(r):
    new_r = 0
    for i in r:
        x = int(i)
        new_r += x
    return new_r

fat = fatorial(f)
r = list(str(fat))

s = r
for i in range (fat+1):
    y = soma(s)
    s = list(str(y))
    if len(s) == 1:
        print(i+1)
        break

print(int(s[0]))

