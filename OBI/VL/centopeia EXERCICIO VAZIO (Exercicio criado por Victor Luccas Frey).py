#Exercicio criado por Victor Luccas Frey

#CENTOPÉIA ALIENÍGENA
'''
Imagine que um planeta alienígena criou uma maquina centopéia.
Essa máquina é dividida em N segmentos, cada segmento carrega
uma quantidade de peso. Para a máquina funcionar é preciso que
o peso dos segmentos da esquerda seja igual ao peso dos segmentos da direita.
Caso a máquina tenha um número impar de segmentos o peso do meio não precisa
ser levado em consideração.

Crie um programa que dirá se essa maquina irá funcionar ou não, dado
os valores de cada pesso de cada segmento e o numero de segmentos'''

#ENTRADA:
'''na primera linha um inteiro N representando os N segmentos da máquina
na segunda linha os N pesos  de cada segmento'''

#SAÍDA:
'''seu programa deve imprimir uma única linha com "Sim" caso a máquina funcione
ou "Não" caso ela não funcione.'''

#RESTRIÇÕES:
'''
2 ≤ N ≤ 1000
1 ≤ pesos ≤ 1000
'''

#Exemplo1:
'''
Entrada:
5
10 8 3 9 10
Saída: Não
'''

#Exemplo2:
'''
Entrada:
5
10 8 3 9 9
Saída: Sim
'''

N = int(input())
p = input().split()
for i in range(N):
    p[i] = int(p[i])
soma1 = 0
soma2 = 0
for i in range(round(N/2)):
    soma1 += p[i]
    soma2 += p[i+round(N/2)-1]
if soma1 == soma2:
    print("S")
else:
    print("N")


