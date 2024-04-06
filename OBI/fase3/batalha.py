A1 = int(input())
D1 = int(input())
A2 = int(input())
D2 = int(input())

j1 = False
j2 = False

if A1!= D2:
    j2 = True

if A2 != D1:
    j1 = True

if j1 == j2:
    print(-1)
elif j1 == False:
    print(1)
else:
    print(2)
