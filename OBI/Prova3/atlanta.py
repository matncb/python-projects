A = int(input())
B = int(input())

num = A+B

def divisores(num):
    for i in range(1, int(num/4+1)):
        if num % i == 0: 
           yield (i, int(num/i))

d = list(divisores(num))
printou = False

for i in d:
    x, y = i
    if (A == (2*x) + (2*y) -4) and (B == (x*y) - (2*x) - (2*y) + 4):
        printou = True
        print(x, y)

if printou == False:
    print(-1, -1)
    
