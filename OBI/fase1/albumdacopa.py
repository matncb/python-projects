"""
N = int(input())
M = int(input())
fig = []
resposta = 0

for contador in range(N):
   fig.append(contador + 1)

for contador in range(M):
    NF = int(input())
    for contador2 in range(N):
        if(NF==fig[contador2]):
            fig[contador2] = 0

for contador in range(N):
    if (fig[contador] != 0):
        resposta += 1

print(resposta)
        
"""
N = int(input())
M = int(input())
minhasFig = []

for i in range(M):
    novaFig = int(input())
    jatenho = False
    for j in range(len(minhasFig)):
        if (minhasFig[j] == novaFig):
            jatenho = True
    if (jatenho == False):
        minhasFig.append(novaFig)
        
print(N-(len(minhasFig)))
