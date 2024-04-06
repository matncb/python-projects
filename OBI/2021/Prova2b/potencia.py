N = int(input())
s = 0
for i in range(N):
    l = list(input())
    p = int(l.pop(-1))
    
    st = ""
    for i in l:
       st += str(i)

    st = int(st)

    s += st**p

print(s)
