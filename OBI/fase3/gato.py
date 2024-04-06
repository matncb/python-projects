C = int(input())

l = [int(i) for i in input().split()]

pos_atual = 0
s = 0

while pos_atual < C-1:
    if pos_atual <= C-3 and l[pos_atual + 2] == 1:
        pos_atual += 2
        s += 1
    elif pos_atual <= C-2 and l[pos_atual + 1] == 1:
        pos_atual += 1
        s += 1
    else:
        s = -1
        break

print(s)
