


def legal(num):
    num = list(bin(num))
    num.pop(0)
    num.pop(0)

    tamanho = len(num)
    if tamanho % 2 != 0:
        tamanho += 1

    cont = 0
    ant = False

    for i in num:
        if i == "1":
            if ant == True:
                return False
            else:
                cont +=1
                ant = True
        else:
            ant = False
            

    if cont >= tamanho/2:
        return True
    else:
        return False

def qnt(num):
    c = 0
    for i in range(1, num+1):
        if i <= num:
            if legal(i):
                c+=1
    return(c)


print(qnt(2**9))



