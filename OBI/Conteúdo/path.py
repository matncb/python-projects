m = [[1, 1, 0, 0, 1, 1], [0,1,1,1,0,0], [0, 0 ,1 ,1, 0, 1]]

def v(m):
    for i in m:
        for j in i:
            if j == 0:
                print("#", end='')
            else:
                print("-", end='') 
        print()

sta = (0,0)
fim = (2, 3)


class Block():
    def __init__(self):
        self.visitado = False
        self.acumulado = 0

def ver_pontas(cord):
    x, y = cord
    x_pos = []
    y_pos = []
    comb = []

    coef = [1, -1]

    for i in coef:
        x_pos.append(x+i)
        y_pos.append(y+i)

   
    





    
