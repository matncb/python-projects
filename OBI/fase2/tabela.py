J, P, V, E, D = [int(i) for i in input().split()]

while J == -1 or P == -1 or V == -1 or E == -1 or D == -1:
    if J == -1 and V != -1 and E != -1 and D != -1:
        J = V+E+D
    if P == -1 and V != -1 and E != -1:
        P = (3*V)+E
    if V == -1 and J != -1 and E != -1 and D != -1:
        V = J-E-D
    if V == -1 and E != -1 and D != -1 and J != -1:
        V = J-E-D
    if E == -1 and P != -1 and V != -1:
        E = P-(3*V)
    if D == -1 and J != -1 and V != -1 and E != -1:
        D = J-V-E

print(J, end = " ")
print(P, end = " ")
print(V, end = " ")
print(E, end = " ")
print(D, end = " ")
