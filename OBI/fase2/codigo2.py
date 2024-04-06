N = int(input())
l = input().split()
s = 0

for i in range(N-2):
    if int(l[i]) == 1 and int(l[i+1]) == 0 and int(l[i+2]) == 0:
        s += 1

print(s)
