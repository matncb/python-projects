P = int(input())
D_1 = int(input())
D_2 = int(input())

res =(D_1 + D_2) %2

if P == 0:
    if res ==0:
        print("0")
    else:
        print("1")

if P ==1:
    if res == 0:
        print("1")
    else:
        print("0")

