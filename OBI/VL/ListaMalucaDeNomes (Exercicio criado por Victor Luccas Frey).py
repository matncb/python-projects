#Exercício criado por Victor Luccas Frey

#LOGICA MALUCA DA LISTA DE NOMES
'''
Victor estava analisando um banco de dados do seu trabalho em um dia sen nada pra fazer,
então sua mente maluca percebeu que os nomes estavam em uma ordem lógica.
Se analisarmos cada nome considerando que sua letra inicial corresponde à um numero de zero à 25,
sendo a=0, b=1, c=2 e assim por diante até z=25, Victor pecebeu que sabendo que os tres primeiros
nomes sempre começam sendo o primeiro com a letra a, o segundo com a letra b e o terceiro com a letra c,
todos os outros começam com a letra que seria a soma dos números correspondentes às 3 letras anteriores.

por exemplo uma lista que vai da posição zero à 7
teriam uma ordem de nomes seguinto a seguinte ordem de letras:
a,b,c,d,g ,l,u ,k
que correspondem aos seguintes valores de soma:
0,1,2,3,6,11,20,37

no caso das somas passarem 25, a contagem daria a volta, sendo assim posiçoes como 26,27,28 seriam
respectivamente a,b,c.

Crie um programa que dado o nome de uma pessoa e a posição da lista, o programa diga se
esse nome poderia estar nessa posição ou não.
'''

#Entrada
'''duas linhas a primeira com um nome e a segunda com um inteiro indicando a posição da lista'''

#Saída
'''Caso seja possível ter esse nome na posição indicada a saída deve ser assim:
Sim pois o nome começa com #letraInicialDoNome e na posição #posicaoDaEntrada começa com #letraDaLista

Caso não seja possível ter esse nome na posição indicada  a saída deve ser assim:
Não pois o nome começa com #letraInicialDoNome e na posição #posicaoDaEntrada começa com #letraDaLista
'''

#REGRA ESPECIAL
'''Usar recursividade'''

#listas exeplos, em orde de cima pra baixo: lista de posições, lista das somas, listas das letras iniciais
#0,1,2,3,4,5 ,6 , 7, 8
#0,1,2,3,6,11,20,37,68
#a,b,c,d,g ,l,u ,l, q

'''----------------------------------------------------------------------------------'''
letras = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def seq(x):
    if x == 0 or x == 1 or x == 2:
        return x
    return seq(x-1) + seq(x-2) + seq(x-3)

def letra(y):
    while y>25:
        y += -26
    return letras[y]

nome = list(input())
c = nome[0]
pos = int(input())

var = letra(seq(pos))
if var == c:
    print("Sim, pois o nome começa com " + str(c) + " e na posição " + str(pos) + " começa com a letra " + var)
else:
    print("Não, pois o nome começa com " + str(c) + " e na posição "+ str(pos) + " começa com a letra " + var)
