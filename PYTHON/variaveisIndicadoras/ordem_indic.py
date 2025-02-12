import os
os.system('clear')

n = int(input("Informe uma quantidade de números para verificar se eles estão em ordem crescente ou não: "))
ordenado = True
valor_anterior = 0

while (n>=1) and (ordenado):
    valor_novo = int(input(f'Insira um valor: '))
    if (valor_novo<valor_anterior):
        ordenado = False
        break
    valor_anterior=valor_novo
    n-=1 

if (ordenado):
    print(f"Crescente!")
else: 
    print(f"Bagunçado.")