N = int(input())
m = [int(i) for i in input().split()]

for j in range(N-1):
    k = []
    for i in range(len(m)):
        if i!= len(m)-1:
            if m[i] + m[i + 1] == 0:   
                k.append(-1)
            else:
                k.append(1)
    m = k

if m[0] == -1:
    print("branca")
else:
    print("preta")
            
        
            
