import math

j = 0.00001

h=0.09
r = 1
m = 10
g = 10

q = h/r
lado = 0

Emax = m*g*h
B = math.atan(q/2)

N = 99999
for Ei in range(1, N):

    while Ei > Emax:
        Ei = Ei*j

    A = math.asin(Ei/(m*g*h))

    if A <= B:
        lado += 1

P = (lado/N)*100
print(P)
        

