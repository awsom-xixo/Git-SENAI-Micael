def leNumInt():
    num = int(input('Digite um número inteiro: '))
    return num

def inverterVal(num):
    num = str(num)[::-1]
    return int(num)


num = leNumInt()
val_Inver = inverterVal(num)
print(val_Inver)