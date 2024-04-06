N = int(input())
N_input = []
camadas = []
jatem = False
for i in range(N):
    N_input.append([int(i) for i in input().split()])

print(N_input)
cont = -1
for i in range(N):
    cont += 1
    jatem = False
    if (N_input[i][2] == cont):
        for i in range(len(camadas)):
            if (camadas[i] == cont):
                jatem = True
            if (jatem == False):
                camadas.append(cont)
        
print(camadas)
