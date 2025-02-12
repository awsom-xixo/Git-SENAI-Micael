import os
os.system('clear')

n = int(input(f"Insira um valor para verificar se é primo ou não: "))
if n<=1:
    print(f"Não é primo. Números menores que 1, ou o próprio 1 não são primos.")
else:
    divisores = True
    val = 2

while (val <= n-1):
    if(n%val == 0):
        divisores += 1 
    val+=1

if (divisores == 0):
    print(f"{n} é primo!")
elif (divisores == 1): 
    print(f"{n} não é primo. Possui 1 divisor diferente de 1 e {n}")
else:
    print(f"{n} não é primo. Possui {divisores} divisores diferentes de 1 e {n}")