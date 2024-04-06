N = int(input())
l = list(input())
s = 0

for i in l:
    if i == "P" or i == "C":
        s += 2
    elif i == "A":
        s += 1

print(s)
