n = int(input("Numero: "))
num = 2
primo = True #variavel indicadora

while (num <= n-1) and (primo):
    if (n % num == 0): #se n é divisivel por num
        primo = False
    num+=1

if (primo):
    print("É primo")
else:
    print("Não é primo")