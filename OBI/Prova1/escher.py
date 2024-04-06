N = int(input())
num = []
inpute = input()
naoe= False
soma = []
num.append(inpute.split())

for i in range(N):
    num[0][i] = int(num[0][i])

for i in range(N):
    soma.append(num[0][i] + num[0][N-1-i])

for i in range(len(soma)):
    if soma[i]%soma[0] != 0:
        naoe = True

if naoe == True:
    print("N")
else:
    print("S")
