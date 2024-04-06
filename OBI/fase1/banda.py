N,M=input().split()
N=int(N)
M=int(M)

matriz=[]
A=0
B=0
C=0
AB=0
AC=0
BC=0
somaTotal=0

for i in range(M):
    entrada=input().split()
    
    matriz.append(entrada)

for i in range(M):
    for j in range(3):
        matriz[i][j]=int(matriz[i][j])


for m in range(M):
    for n in range(N):
        if(matriz[m][0]!=n+1 and matriz[m][1]!=n+1):
            for x in range(M):
                if(matriz[x][0]==n+1):
                    if(matriz[x][1]==matriz[m][0]):
                        AC=matriz[x][2]
                    elif(matriz[x][1]==matriz[m][1]):
                        BC=matriz[x][2]

                elif(matriz[x][1]==n+1):
                    if(matriz[x][0]==matriz[m][0]):
                        AC=matriz[x][2]
                    elif(matriz[x][0]==matriz[m][1]):
                        BC=matriz[x][2]
            AB=matriz[m][2]
            if(AB+AC+BC>somaTotal):
                    somaTotal=(AB+AC+BC)
                    A=matriz[m][0]
                    B=matriz[m][1]
                    C=n+1
            AB=0
            AC=0
            BC=0
            
print(A,B,C)          
            
        
