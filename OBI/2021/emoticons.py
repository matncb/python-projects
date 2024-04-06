M = list(input())

r = 0
for i in range(len(M)):
    if i < len(M)-2:
        if M[i] == ":" and M[i+1] == "-":
            if M[i+2] == ")":
                r +=1
            elif M[i+2] == "(":
                r -= 1

if r == 0:
    print("neutro")
elif r>0:
    print("divertido")
else:
    print("chateado")