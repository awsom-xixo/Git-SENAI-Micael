import random

def criaMatriz():
    # Retorna uma matriz aleatoria de forma direta
    return [[random.randint(0, 1) for _ in range(10)] for _ in range(10)]

def leMatriz(matriz):
    naoNulos = 0
    tamanho = len(matriz)

    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] != 0:  # Conta apenas valores não nulos
                naoNulos += 1
    return naoNulos

def imprimeMatriz(matriz):
    for linha in matriz:
        for numero in linha:
            print(numero, end=" ") # imprime uma linha separada por espaços
        print() # da espaço para proxima linha


matriz = criaMatriz()
print(f'Matriz: ')
imprimeMatriz(matriz)
print(f'Valores nulos: {leMatriz(matriz)}')
