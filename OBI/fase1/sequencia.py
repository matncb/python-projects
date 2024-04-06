N = int(input())
div = []
select = []
cont = 1

for i in range(N):
    div.append(int(input()))

for i in range(len(div)):
    if (div[i-1]!= div[i]):
        cont += 1
        
print(cont)


