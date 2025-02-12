import os
os.system ('clear')

def validar_cpf():
    return (len(str(cpf))==11)

while True:
    try:
        cpf = int(input('Insira um CPF com apenas números e 11 caracteres: '))
        if validar_cpf(cpf):
            print('Sucesso!')
            break
        else:
            print('Inválido, deve conter apenas números e exatamente 11 caracteres.')
    except ValueError:
        print('Inválido, deve conter apenas números.')