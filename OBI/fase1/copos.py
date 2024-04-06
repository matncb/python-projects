N = int(input())
L = input()
mov =[]

for i in range(N):
    mov.append(input())

pos = ["A", "B", "C"]

for i in range(N):
    if mov[i] == "1":
       pos[0], pos[1] = pos[1], pos[0]
    elif mov[i] == "2":
        pos[1], pos[2] = pos[2], pos[1]
    else:
        pos[0], pos[2] = pos[2], pos[0]


for i in range(3):
    if pos[i] == L:
        if i == 0:
            print("A")
        elif(i == 1):
            print("B")
        else:
            print("C")
            


#print(pos)
