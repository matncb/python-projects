'''
A = int(input())
B = int(input())
C = int(input())
H = int(input())
L = int(input())
h = []
l = []
S = False

if (A<=H):
    h.append("A")

if (B<=H):
    h.append("B")

if (C<=H):
    h.append("C")

if (A<=L):
    l.append("A")

if (B<=L):
    l.append("B")

if (C<=L):
    l.append("C")

for i in range(len(h)):
    for j in range(len(l)):
        if (h[i] == l[j]):
            S = True

if (S == True):
    print("S")
else:
    print("N")

'''
A = int(input())
B = int(input())
C = int(input())
H = int(input())
L = int(input())

f1 = [A,B]
f2 = [A,C]
f3 = [B,C]
janela = [H,L]
S = False

if f1[0]<= janela[0] and f1[1]<= janela[1]:
    S = True

if f1[1]<= janela[0] and f1[0]<= janela[1]:
    S = True

if f2[0]<= janela[0] and f2[1]<= janela[1]:
    S = True

if f2[1]<= janela[0] and f2[0]<= janela[1]:
    S = True
    
if f3[0]<= janela[0] and f3[1]<= janela[1]:
    S = True

if f3[1]<= janela[0] and f3[0]<= janela[1]:
    S = True
    
if S ==True:
    print("S")
else:
    print("N")
