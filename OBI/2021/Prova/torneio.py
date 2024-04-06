
cont = 0
for i in range(6):
    a = input()
    if a == 'V':
        cont += 1

if cont >= 5:
    print(1)
elif (cont == 3) or (cont == 4):
    print(2)
elif (cont == 1) or (cont == 2):
    print(3)
else:
    print(-1)
        