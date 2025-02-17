def leNumInt():
    num = int(input('Digite um número inteiro: '))
    return num

def potenciaNumInt(num):
    potencia = int(input(f'Digite quantas vezes deseja multiplicar {num} por ele mesmo: '))
    res = 0

    for _ in range(potencia-1):
        res = res + (num*num)

    return res

val = leNumInt()
print(potenciaNumInt(val))