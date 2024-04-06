#Calcular fatorial com recursao
def fatorial(n) :
    if n == 1:
        return 1

    return n * fatorial(n-1)

#calcular soma com recursao
def soma(n):
    if n == 1:
        return 1

    return n*soma(n-1)

#calcular potencia com recursao
def pot(a,b):
    if b == 1:
        return a

    return a * pot(a, b-1)

#print(pot(10,4))

#calcular fibonacci com recursao

def fib(x):
    if x == 0 or x == 1:
        return x
    return fib(x-1) + fib(x-2)

def fib2(a):
    a += -1
    return fib(a)

#print(fib2(100))

#dobro de um n com recursao

def d(a):
    if a == 0:
        return 0

    return 2 + d(a-1)
print(d(1000))

#N = int(input())

'''
N = soma(N)
print (N)
'''

'''
N = fatorial(N)
print(N)
'''
