N = int(input())
div = [int(i) for i in input().split()]
total = 0
for i in range(len(div)):
    div[i] += -1
    total += div[i]

print(total)
