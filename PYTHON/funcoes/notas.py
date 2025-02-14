def leNota(n):    
    notas = []
    for i in range(n):
        dado = float(input(f'Digite a nota {i+1}: '))
        notas.append(dado)
    return notas

def calculaMedia(notas):
    soma = 0
    for i in range (len(notas)):
        soma = soma + notas[i]
    return (soma/len(notas))

def main():
    n = int(input('Digite o número de notas: '))
    notas = leNota(n)
    media = calculaMedia(notas)
    print('A média é: ', format(media , '.1f'))

main()