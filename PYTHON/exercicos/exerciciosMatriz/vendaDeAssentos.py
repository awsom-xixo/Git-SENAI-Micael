import random

def imprimeOnibus(matriz):
    for linha in matriz:
        for numero in linha:
            print(numero, end=" ") # imprime uma linha separada por espaços
        print() # da espaço para proxima linha

def verificarAssento(assentos, linha, coluna):
    if (assentos[linha][coluna]) == 'X':
        print('Lugar ocupado! Escolha outro.\n')
        return False

    return True

assentos = [[random.choice(['O', 'X']) for _ in range(5)] for _ in range(10)]

while True:
    imprimeOnibus(assentos)
    linha = int(input(f"Escolha uma posição na linha (1-10): "))-1
    coluna = int(input(f"Escolha uma posição na coluna (1-5): "))-1
    print()

    print(f"Você escolheu a posição ({linha+1}, {coluna+1}), que tem o valor: {assentos[linha][coluna]}")
    if (verificarAssento(assentos, linha, coluna)):
        print('Lugar selecionado.')
        esc = str(input(f'Tem certeza que quer o assento ({linha+1}, {coluna+1})? ')).strip().lower()[0]
        if (esc == 's'):
            break