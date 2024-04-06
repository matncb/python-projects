inpute = list(input())

n = ["2", "3", "4", "5", "6", "7", "8", "9", "-"]
l = [["A", "B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y"],["-"]]

for i in inpute:
    for j in range(9):
        for k in range(len(l[j])):
            if l[j][k] == i:
                print(n[j], end="")
            
