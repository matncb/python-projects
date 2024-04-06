S= int(input())
A= int(input())
B= int(input())
soma = 0
for i in range(A, B+1):
    l = [int(j) for j in list(str(i))]
    s = sum(l)

    if s == S:
        soma +=1

print(soma)