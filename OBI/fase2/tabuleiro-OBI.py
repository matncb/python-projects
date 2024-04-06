
x = int(input(''))
m = []
for i in range(int(x)):
    l=list(map(int,input().split()))
    m.append(l)
#print(m)

for i in range(int(x)):
    for j in range(int(x)):
       if m[i][j] == 9:
         v = m[i-1][j-1] + m[i][j-1] + m[i-1][j]
         if (v > 1):
           v=0
         else:
           v=1
         m[i][j] = v
#print(m)
print(m[x-1][x-1])
