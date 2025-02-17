def leNumInt():
    num = int(input('Digite um número inteiro: '))
    return num

def potenciaNumInt(num):
    potencia = int(input(f'Digite quantas vezes deseja multiplicar {num} por ele mesmo: '))
    res = 0

    for _ in range(potencia-1): #'-1' está aqui por que se, por exemplo, o expoente fosse 2 e a base 3, ele passaria pelo loop duas vezes e daria 18, como '3*3*3'. Isso pq na primeira vez que passa no for, já existe 'num * num'
        res = res + (num*num)

    return res

val = leNumInt()
print(potenciaNumInt(val))