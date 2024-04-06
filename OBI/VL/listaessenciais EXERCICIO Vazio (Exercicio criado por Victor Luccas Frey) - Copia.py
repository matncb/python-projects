#Exercicio criado por Victor Luccas Frey

#LISTA DE COMPRAS
'''
Carlos está montando uma lista de itens essenciais para sua casa.
Ele escreveu uma lista com N itens e em seguida ele anotou a quantidade de cada
um desses itens que já possui em casa.
Por Exemplo, se ele anotou que precisa de banana, kiwi e feijão,e em seguida
ele anotou 1,2 e 0, isso significa que ele tem 1 banana, 2 kiwis e zero feijão.

Carlos irá fazer compras e irá comprar apenas os itens de sua lista que tem
uma quantidade menor que Q.

Então digamos que Q equivale a 2. Então Carlos precisaria, no caso acima, comprar
banana e feijão.

Crie um programa que ajude Carlos a resumir a lista dele para apenas os
itens que ele deve realmente comprar.
'''

#ENTRADA:
'''
na primera linha um inteiro N representando número de itens da lista
na segunda linha os N itens da lista de itens essenciais
na terceira linha os N valores representando a quantidade de cada item da lista
na quarta linha um inteiro Q que definirá se o item deve ou não ser comprado '''

#SAÍDA:
'''seu programa deve imprimir uma única linha com a lista de itens que devem ser comprados
caso não haja itens a serem comprados seu programa deve imprimir uma única linha com
a frase "lista vazia" '''

#RESTRIÇÕES:
'''
1 ≤ N ≤ 1000
0 ≤ quantidade de cada item ≤ 30
0 ≤ Q ≤ 30
'''

#Exemplo1:
'''
ENTRADA:
3
banana kiwi feijao
1 2 0
2
SAÍDA:
banana feijao 
'''

#Exemplo2:
'''
ENTRADA:
banana feijao 
4
abacate batata pudim cenoura
12 10 5 20
5
SAÍDA:
lista vazia

'''

#Exemplo3:
'''
ENTRADA:
3
coco banana coxinha
10 5 0
4
SAÍDA:
coxinha 
'''

N = int(input())
l = input().split()
x = input().split()
q = int(input())
s = False

for i in range(N):
    x[i] = int(x[i])
    if x[i]<q:
        print(l[i], end = " ")
        s = True
    
if s == False:
    print("lista vazia")
