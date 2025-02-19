def leNotas(n):
    notas = []

    for i in range(n):
        notas.append(float(input(f'Insira a nota {i+1}: ')))

    print(f'Notas: {notas}')
    return calculaMedia(notas)


def calculaMedia(notas):

    media = sum(notas) / len(notas) #sum() para ser mais eficiente que um loop
    return media


n = int(input('Insira a quantidade de notas que deseja calcular a média: '))
print(f'Média: {leNotas(n):.2f}') # ' :.2f ' arredonda os valores para ficarem mais exatos