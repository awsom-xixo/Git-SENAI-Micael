import random

def leMatriz(matriz):
    naoNulos = 0
    tamanho = len(matriz)

    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] != 0:  # Conta apenas valores não nulos
                naoNulos += 1
    return naoNulos

def criaMatriz():
    return [[random.randint(0, 1) for _ in range(10)] for _ in range(10)]

matriz = criaMatriz()
print(leMatriz(matriz))
