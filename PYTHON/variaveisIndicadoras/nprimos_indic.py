import os
os.system('clear')

val = int(input(f"Insira um valor para verificar se é primo ou não: "))
primo = True
n = 2

while (n <= val-1) and (primo):
    if(val%n == 0):
        primo = False
        break 
    n+=1

    # esse código rodaria várias vezes,
    # mesmo que tenha identificado que o numero é primo!
    # por isso é adicionado um "break", para que quebre o loop. 

if (primo):
    print(f"Valor primo!")
else: 
    print(f"Valor não primo.")