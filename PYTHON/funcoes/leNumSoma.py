def leNumInt():
    num = int(input('Digite um número inteiro: '))
    return int(num)

def soma(num1, num2):
    res = num1 + num2
    return res

n1 = leNumInt()
n2 = leNumInt()


res = soma(n1, n2)
print('Número digitado: ',res)