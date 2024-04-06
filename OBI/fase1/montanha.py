N = int(input())
num = input().split()
t = False

for i in range(N):
    num[i] = int(num[i])

for i in range(1, N-1):
    if ((num[i-1])>num[i]) and ((num[i+1])>num[i]):
        print("S")
        t = True
        #break

if t == False:
    print("N")


