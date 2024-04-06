N = int(input())
m = []
l = []
ig = []
ig2 = []
s = 0
r = 0

for i in range(N):
    a,b = input().split()
    m.append(a)
    l.append(b)

for i in range(len(m)):
    for j in range(len(m)):
        if m[i] == m[j]:
            s += 1
    if s >= 2:
        ig.append(m[i])
        ig2.append(l[i])
    s = 0

for i in range(len(ig)):
    for j in range(len(ig)):
        if ig[i] == ig[j]:
            if ig2[i] != ig2[j]:
                r += 1
                print(r)
            
print(int(r/2))

