#Exercicio criado por Victor Luccas Frey

#Tabuleiro N Exercício 2
'''
Giovanna continua criando um tipo jogo de xadrez virtual chamado Tabuleiro N,
e em seu jogo o jogador pode escolher uma casa para invocar uma peça especial,
porém ela quer que o tamanho do tabuleiro do jogo seja decidido
no início da partida, fazendo cada partída única.

O tabuleiro tem tamanho N por N, de zero à N-1.

O tabuleiro é formado por 'X's e 'O's maiúsculos intercalados como nos exemplos a seguir:

Exemplo1:
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX

Exemplo2:
XOX
OXO
XOX


Giovanna precisa que o programa represente visualmente se a casa para invocar
uma peça especial é uma casa "X" ou uma casa "O"

crie um programa que dado o tamanho do tabuleiro e as coordenadas
da casa para invocar uma peça especial mostre se essa casa da peça
especial é uma casa "X" ou uma casa "O".
'''

#ENTRADA:
'''
uma única linha com 3 inteiros N,X,Y representando respectivamente
o tamanho do tabuleiro, a cordenada no eixo horizontal e a cordenada no eixo vertical
da peça especial

'''

#SAÍDA:
'''seu programa deve imprimir "X" ou "O" mostrando qual é a representação
visual da casa da peça especial'''

#RESTRIÇÕES:                 
'''
2 = N = 20
'''

#Exemplo1:
'''
ENTRADA:
2 0 0

SAÍDA:
X
'''

#Exemplo2:
'''
ENTRADA:
5 3 1
SAÍDA:
X
'''

#Exemplo3:
'''
ENTRADA:
8 5 6
SAÍDA:
O
 
'''
N, X, Y = [int(i) for i in input().split()]

if (X+Y)%2 == 0:
    print("X")
else:
    print("O")
