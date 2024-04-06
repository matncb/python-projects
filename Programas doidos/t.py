'''
X = 1
L = 3
N = 4

for i in range(N-1):
    h = (        L * (3**(1/2))  -         (L*((3*X)**(1/2)))/(N**(1/2))         )/2
    X += 1
    print(h)

'''
X = 1
N = 4
H = 5

for i in range(N-1):
    h = (H - ((H*(X**(1/2)))/N**(1/2)))
    X += 1
    print(h)