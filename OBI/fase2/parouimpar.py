P = int(input())
D_1 = int(input())
D_2 = int(input())

if P == 0:
    print((D_1 + D_2)%2)

elif (D_1 + D_2)%2 == 0:
    print(int(1))

else:
    print(int(0))
