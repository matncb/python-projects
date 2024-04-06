N = int(input())

m = []
for i in range(N):
    a = int(input())
    if a == 0:
        m.pop(len(m)-1)
    else:
        m.append(a)
r = 0
for i in range(len(m)):
    r += m[i]

print(r)
    
        