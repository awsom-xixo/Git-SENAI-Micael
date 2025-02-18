notas = []

def darNotas(n):
    for i in range(n):
        nota = float(input('Entre com a nota '+ str(i+1) + ': '))
        notas.append(nota)


n = int(input('Entre com um número de notas: '))
darNotas(n)
print('Notas:', end='')

for nota in range(len(notas)):
    print(f'{nota}, ', end="")