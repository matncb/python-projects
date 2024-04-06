N, K = [int(i) for i in input().split()]

frutas = []
safra = 0
soma = 0

def somaf():
    soma = 0
    for i in range(K):
        soma += frutas[i]
    return soma

frutas = [int(i) for i in input().split()]

P = input().split()

for j in range(N):
    for i in range(K):
        if frutas[i] > 0:
            if P[j] == "E":
                frutas[i] -= 1
            else:
                frutas[i]+=1
    safra += somaf()

print(safra)

