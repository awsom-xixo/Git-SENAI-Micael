import os
os.system ('clear')

while True:
    try:
        val = int(input('Digite um valor para saber sua tabuada: '))
        break
    except ValueError:
        print('Precisa ser um número inteiro.')
i=1

for i in range(1,11):
    print(f'{i} x {val} = {i*val}')
    i+=1