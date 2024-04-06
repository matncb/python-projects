bomba = list(input())
res = []

#verficação 1
corta_azul0 = True
if bomba[3] == "L":
    corta_azul0 = False
if bomba[3] == "P":
    corta_azul0 = False
if bomba[0] != "A":
    corta_azul0 = False

corta_azul1 = True
if bomba[3] == "L":
    corta_azul1 = False
if bomba[3] == "P":
    corta_azul1 = False
if bomba[1] != "A":
    corta_azul1 = False

corta_azul2 = True
if bomba[3] == "L":
    corta_azul2 = False
if bomba[3] == "P":
    corta_azul2 = False
if bomba[2] != "A":
    corta_azul2 = False

corta_azul3 = True
if bomba[3] == "L":
    corta_azul3 = False
if bomba[3] == "P":
    corta_azul3 = False
if bomba[3] != "A":
    corta_azul3 = False


#verificação 2
corta_vermelho0 = False
if bomba[2] == "A":
    corta_vermelho0 = True
if bomba[2] == "P":
    corta_vermelho0 = True
if bomba[0] != "V":
    corta_vermelho0 = False

#verificação 3
corta_primeiro = True
if bomba[0] != bomba[3]:
    corta_primeiro = False
if bomba[1] != bomba[2]:
    corta_primeiro = False
if corta_vermelho0 == True:
    corta_primeiro = True
if corta_azul0 == True:
    corta_primeiro = True

#verficação 4
corta_segundo = True
if bomba[0] == "P":
    corta_segundo = False
if bomba[1] == "P":
    corta_segundo = False
if bomba[2] == "P":
    corta_segundo = False
if bomba[3] == "P":
    corta_segundo = False
if corta_azul1 == True:
    corta_segundo = True

#verificação 5
if bomba[3] == "V":
    corta_segundo = True
if bomba[2] == "V":
    corta_segundo = True

#verificação 6
corta_terceiro = True
if bomba[0] == "A":
    corta_terceiro = False
if bomba[0] == "L":
    corta_terceiro = False
if corta_azul2 == True:
    corta_terceiro = True
    

#res

if corta_primeiro == True:
    res.append("C")
else:
    res.append("N")

if corta_segundo == True:
    res.append("C")
else:
    res.append("N")

if corta_terceiro == True:
    res.append("C")
else:
    res.append("N")

if corta_azul3 == True:
    res.append("C")
else:
    res.append("N")

print(res[0] + res[1] + res[2] + res[3])
