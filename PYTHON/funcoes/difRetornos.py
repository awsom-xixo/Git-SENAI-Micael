def validar_Val(val):
    if (val == 0):
        return 'Z'
    elif (val > 0):
        return 'P'
    else:
        return 'N'
    

val = float(input('Insira um valor: '))
print(validar_Val(val))