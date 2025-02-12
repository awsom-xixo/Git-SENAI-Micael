import os
os.system ('clear')

i=1
cont_par = 0
cont_impar = 0

for i in range (1, 11):
    while True:
        try:
            val = int(input(f'Digite o {i}º número: '))
            break
        except ValueError:
            print('Precisa ser um número inteiro.')

    if (val%2==0):
        cont_par+=1
    else: 
        cont_impar+=1

    i+=1

print(f'Foram encontrados {cont_impar} números ímpares e {cont_par} pares. ')