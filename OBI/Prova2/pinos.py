m =[]
s = 0

for i in range(7):
    m.append(list(input()))

for i in range(7):
    for j in range(7):
        if m[i][j] == "o":
            if j<=4:
                if  m[i][j+2] == "." and m[i][j+1] == "o":
                    s += 1
            if j>1:
                if m[i][j-2] == "." and m[i][j-1] == "o":
                    s += 1
            if i<=4:
                if  m[i+2][j] == "." and m[i+1][j] == "o":
                    s += 1
            if i>1:
                if m[i-2][j] == "." and m[i-1][j] == "o":
                    s += 1

print(s)
