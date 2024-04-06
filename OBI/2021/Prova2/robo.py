N, C, S = [int(i) for i in input().split()]

v = 1

l = [int(i) for i in input().split()]

cont = 0
if v == S:
    cont+=1
    
for i  in l:
    if i == 1:
        v+=1
        if v > N:
            v = 1
    else:
        v-=1
        if v < 1:
            v = N
    if v == S:
        cont +=1
    
print(cont)