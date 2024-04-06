N = int(input())
s = input().split()
r = 0

for i in range(N):
    if i < N-2:
        if s[i] == "1" and s[i+1] == "0" and s[i+2] == "0":
            r += 1
        
print(r)
