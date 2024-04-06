A = int(input())
B = int(input())
C = int(input())
ja = False

if C>B:
    if B>A:
        if ja == False:
            print(int(1))
            ja = True
    if (B+A)<C:
        if ja == False:
            print(int(1))
            ja = True
    if A>B:
        if ja == False:
            print(int(2))
            ja = True
    if A == B:
        if ja == False:
            print(int(2))
if B>C:
    if ja == False:
        print(int(3))
        ja = True
if C == B:
    if B == A:
        if ja == False:
            print(int(3))
            ja = True
    elif ja == False:
        print(int(2))
        ja = True
if B == A:
    if ja == False:
        if (B+A)<C:
            print(int(1))
            ja = True
    elif ja == False:
        print(int(3))
        ja = True

