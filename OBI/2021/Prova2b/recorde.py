R = int(input())
M = int(input())
L = int(input())

m = False
o = False

if R < M:
    m = True
if R < L:
    o = True

if m:
    print("RM")
else:
    print("*")

if o:
    print("RO")
else:
    print("*")
