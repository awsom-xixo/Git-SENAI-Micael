import os
import random
os.system ('clear')

numero = random.randint(1,100)
tentativas = 0

print('A máquina escolheu um número de 1 a 100... Tente chegar no valor exato em poucas tentativas para vencer. ')

while True:
    try:
        chute = int(input('Chute um número: '))

    except ValueError:
        print('Valor inválido. Digite um número inteiro. ')
        continue

    tentativas+=1
    

    if (chute == numero):
        print(f'O número era {numero}. Você venceu em {tentativas} tentativas!')
        break

    elif (chute>numero):
        print('O número é menor que seu chute...')

    else:
        print('O número é maior que seu chute...')