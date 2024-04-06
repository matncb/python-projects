m = []

for i in range(15):
    m.append([int(i) for i in input().split()])

def g(i, j, cor):
     if j<=10 and m[i][j] == cor and m[i][j + 1] == cor and m[i][j+2] == cor and m[i][j+3] == cor and m[i][j+4] == cor:
         return True
     if j >= 4 and m[i][j] == cor and m[i][j - 1] == cor and m[i][j-2] == cor and m[i][j-3] == cor and m[i][j-4] == cor:
         return True
     if i <= 10 and m[i][j] == cor and m[i+1][j] == cor and m[i+2][j] == cor and m[i+3][j] == cor and m[i+4][j] == cor:
         return True
     if i >= 4 and m[i][j] == cor and m[i-1][j] == cor and m[i-2][j] == cor and m[i-3][j] == cor and m[i-4][j] == cor:
         return True
     if i <= 10 and j <= 10 and m[i][j] == cor and m[i+1][j+1] == cor and m[i+2][j+2] == cor and m[i+3][j+3] == cor and m[i+4][j+4] == cor:
         return True
     if i >= 4 and j>= 4 and m[i][j] == cor and m[i-1][j-1] == cor and m[i-2][j-2] == cor and m[i-3][j-3] == cor and m[i-4][j-4] == cor:
         return True
     if i <= 10 and j >= 4 and m[i][j] == cor and m[i+1][j-1] == cor and m[i+2][j-2] == cor and m[i+3][j-3] == cor and m[i+4][j-4] == cor:
         return True
     if i >= 4 and j <= 10 and m[i][j] == cor and m[i-1][j+1] == cor and m[i-2][j+2] == cor and m[i-3][j+3] == cor and m[i-4][j+4] == cor:
         return True

     return False

def main():
    for i in range(15):
        for j in range(15):
            if m[i][j] == 1:
                if g(i,j,1):
                    return 1
            elif m[i][j] == 2:
                if g(i, j, 2):
                    return 2

    return 0

print(main())


    
