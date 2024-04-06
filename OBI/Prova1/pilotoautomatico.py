A = int(input())
B = int(input())
C = int(input())

if (B-A) < (C-B):
    print(int(1))

if (B-A) > (C-B):
    print(int(-1))

if (B-A) == (C-B):
    print(int(0))
