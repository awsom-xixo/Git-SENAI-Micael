def leNumInt():
    while True:
        try:
            return int(input('Digite um número inteiro: '))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def inverterVal(num):
    num = str(num)[::-1] #slicing para inverter a string, o passo '-1' lê de forma invertida
    return int(num)


num = leNumInt()
val_Inver = inverterVal(num)
print(val_Inver)