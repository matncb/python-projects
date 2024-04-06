#Exercicio criado por Victor Luccas Frey

#Galões de água
'''
Uma empresa responsável por transportar água percebeu que havia um erro
em seu sistema e muitos galões de água não foram totalmente utilizados.
Alguns galões estava com uma quantindade menor de água menor que sua capacidade
máxima. Com medo de sair no prejuízo transportando menos água do que podiam, essa
empresa te contratou para cirar um programa simples que identificasse , com base
em alguns dados, quanto de água, no total eles estavam deixando de transportar.
Crie um programa que dado o número de galões, sua capacidade máxima e a quantidade
de litros que cada galão está atualmente carregando, mostre quantos litros faltam
para atingir a capacidade máxima de transporte.
'''

#ENTRADA:
'''Na primeira linha dois intereiros, N e C representando, respectivamente,
o numero de galões e a capacidade máxima de cada galão.
Na segunda linha os N inteiros representando a quantidade de litros,
que cada galão está atualmente carregando'''

#SAÍDA:
'''Um único inteiro com a quantidade de litros faltantes
para atingir a capacidade máxima de transporte somando todos os galões'''

#RESTRIÇÕES:                 
'''
1 ≤ N ≤ 100
1 ≤ C ≤ 100
'''

#Exemplo1:
'''
ENTRADA:
3 1
1 0 0

SAÍDA:
2
'''

#Exemplo2:
'''
ENTRADA:
10 20
18 15 5 11 13 6 20 18 7 10

SAÍDA:
77
'''
N, C = [int(i) for i in input().split()]
x = input().split()
s = 0

for i in range(N):
    x[i] = int(x[i])
    s += C - x[i]

print(s)
