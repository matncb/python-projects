n1 = int(input())
n2 = int(input())

def mdc_calc(n1, n2):
    m = n1

    if n1>n2:
        m = n1
    else:
        m = n2

    mdc = 0

    for i in range(1, m+1, 1):
        if n1%i == 0 and n2%i == 0:
            mdc = i

    return mdc

mdc = mdc_calc(n1,n2)


