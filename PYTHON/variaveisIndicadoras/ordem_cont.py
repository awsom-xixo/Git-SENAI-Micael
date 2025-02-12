import os
os.system('clear')

n = int(input("Informe uma quantidade de números para verificar se eles estão em ordem crescente ou não: "))
valor_anterior = int(input("Insira um valor: "))
ordenado = 0

while (n>=1) and (ordenado == 0):
    valor_novo = int(input(f'Insira um valor: '))
    if (valor_novo<valor_anterior):
        ordenado+=1
        break
    valor_anterior=valor_novo
    n-=1 

if (ordenado == 0):
    print(f"Crescente!")
else: 
    print(f"Desordenado.")