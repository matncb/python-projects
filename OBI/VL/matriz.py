N = int(input())
pos = list(input())
l = ["A", "B", "C"]
cont = 0
mod = 0
cont2 = 0
p = 0

for i in range(len(pos)):
    pos[i] = int(pos[i])
    
s = pos[0]*N + pos[i] +1

for i in range(N):
    if i >= 2:
        mod += 3
    for j in range(N):
        cont += 1 
        if cont >= 3:
            cont = 0
            mod += 3
        print(l[j+i-mod], end = "")
        cont2 += 1
        if s == cont2:
            p = j+i-mod
            
         
    print("")
    mod = 0
    cont = 0
    
print("")
print(l[p])
