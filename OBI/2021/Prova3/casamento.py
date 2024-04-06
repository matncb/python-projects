A = [int(i) for i in list(input())]
B = [int(i) for i in list(input())]

if len(A) > len(B):
    while len(A)>len(B):
        B.insert(0, 0)
elif len(B) > len(A):
    while len(B)>len(A):
        A.insert(0,0)

n1 =''
n2 = ''

for i in range(len(A)):
    if A[i] >= B[i]:
        n1 += str(A[i])
    
    if B[i] >= A[i]:
        n2 += str(B[i])

if n1 == '':
    n1= -1
else:
    n1 = int(n1)

if n2 == '':
    n2 = -1
else:
    n2 = int(n2)

if n1<n2:
    print(n1, end = ' ')
    print(n2, end = ' ')
else: 
    print(n2, end = ' ')
    print(n1, end = ' ')




