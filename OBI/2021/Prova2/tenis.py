A = int(input())
B = int(input())
C = int(input())
D = int(input())

def mod(num):
    if num < 0:
        return num * -1
    else:
        return num
val = []

val.append(mod((A+B) - (C+D)))
val.append(mod((A+C) - (B+D)))
val.append(mod((A+D) - (B+C)))

print(min(val))
