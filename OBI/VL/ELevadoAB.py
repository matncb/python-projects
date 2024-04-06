#Exercicio criado por Victor Luccas Frey

#Elevado AB
'''
Abigail está construindo uma calculadora mas ela empacou na programação de
cálculos onde números são elevados à outro número.

Crie um programa que ajude Abigail a calcular um número A elevado à um número B
porém NÃO utilizando o operador padrão de elevado.
(por exemplo, o padrão de 2³em python seria o 2**3, em C++ seria o 2^3)
'''

#ENTRADA:
'''
uma única linha com 2 inteiros A e B representando respectivamente
o numero A que será elevado à B.

'''

#SAÍDA:
'''seu programa deve imprimir um inteiro com o resultado'''

#RESTRIÇÕES:                 
'''
1 = A = 1000
1 = B = 1000
'''

#Exemplo1:
'''
ENTRADA:
2 2

SAÍDA:
4
'''

#Exemplo2:
'''
ENTRADA:
3 4
SAÍDA:
81
'''

#Exemplo3:
'''
ENTRADA:
50 1
SAÍDA:
50
 
'''

A, B = [int(i) for i in input().split()]

def el(a, b):
    if b == 1:
        return a
    else:
        return a * el(a, b-1)

print(el(A,B))
