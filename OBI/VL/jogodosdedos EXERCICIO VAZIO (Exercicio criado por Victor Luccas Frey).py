#Exercicio criado por Victor Luccas Frey

#Jogo dos dedos
'''
Januário, Ariel, Jaina precisam decidir quem vai começar uma brincadeira.
Para isso eles usarão o jogo dos dedos como fator de decisão.
Para que o jogo dos dedos aconteça os participantes devem mostrar a mão com um número
de dedos esticados, deve-se contar o numero total de dedos esticados entre todos os participantes e,
em seguida, deve-se ir contando até o numero total apontando para cada partipante a cada numero
da contagem numa ordem estipulada.
No caso a ordem será sempre Januário, Ariel, Jaina, Januário, Ariel, Jaina
e assim por diante, podendo mudar quem inicia dependendo da entrada.
.
Por exemplo, digamos que Januario estica 3 dedos, Ariel estica 1 dedo e Jaina não estica nenhum dedo.
o total de dedos é 4, se Januário começar a contagem, o numero 1 será ele, o 2 será Ariel, o 3 será Jaina e
por fim o 4 será Januário novamente, terminando em Januário. Nesse caso Januário vence o jogo dos dedos
e começara a brincadeira.

Crie um programa que dado os valores de cada dedo e quem inicia a contagem mostre quem irá começar a brincadeira.

'''

#ENTRADA:
'''
na primeira linha 3 inteiros representando cada dedo esticado.
na segunda linha o nome de quem irá começar a contagem, sem ascento e tudo em letra minúscula.

'''

#SAÍDA:
'''seu programa deve imprimir o nome de quem venceu o jogo dos dedos e irá iniciar a brincadeira,
sem ascento e tudo em letra minúscula.'''

#RESTRIÇÕES:                 
'''
0 ≤ numero de dedos ≤ 10
'''

#Exemplo1:
'''
ENTRADA:
1 3 0
januario

SAÍDA:
januario
'''

#Exemplo2:
'''
ENTRADA:
10 5 8
ariel

SAÍDA:
jaina
'''

x = input().split()
p = input()
t = 0

for i in range(3):
    x[i] = int(x[i])
    t += x[i]

ordem = ["januario", "ariel", "jaina"]

modificador = 0

if p == "ariel":
    modificador = 1
elif p == "jaina":
    modificador = 2

if modificador == 1:
    ordem[0], ordem[2] = ordem[2], ordem[0]
    ordem[0], ordem[1] = ordem[1], ordem[0]
elif modificador == 2:
    ordem[0], ordem[2] = ordem[2], ordem[0]
    ordem[1], ordem[2] = ordem[2], ordem[1]

print(ordem[t%3-1])

