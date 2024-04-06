'''
N = int(input())

m = []

abc = ["a","b","c","d","e","f","g","h","i","j","k", "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(N):
    relacoes = input().split()
    m.append(relacoes)

O, D = input().split()

for i in range(26):
    if (O==abc[i]):
        O = i
    if(D == abc[i]):
        D = i
if (m[O][D] == "1" or m[D][O] == "1"):
    print("S")
else:
    print("N")
'''

N = int(input())
grafo = []
lista = []

for i in range(N):
    lista = input().split()
    grafo.append(lista)

A,B,C = [int(i) for i in input().split()]

print(int(grafo[A][B]) + int(grafo[B][C]))
