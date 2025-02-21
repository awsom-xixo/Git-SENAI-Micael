def somaMatriz(mat1,mat2):
    tamanho = len(mat1)
    mat3 = [[0 for j in range(tamanho)]for i in range(tamanho)]
    for i in range(tamanho):
        for j in range(tamanho):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3


def multiplicarMatriz(mat1, mat2):
    tamanho = len(mat1)
    mat3 = [[0 for j in range(tamanho)]for i in range(tamanho)]
    for i in range(tamanho):
        for j in range(tamanho):
            mat3[i][j] = mat1[i][j] * mat2[i][j]
    return mat3

def leMatriz(dimensao):
    mat = [[] for i in range (dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input('('+str(i+1)+','+str(j+1)+'): '))
            mat[i].append(num)
    return mat

def imprimeMatriz(mat):
    for linha in mat:
        for numero in linha:
            print(numero, end=" ") # imprime uma linha separada por espaços
        print() # da espaço para proxima linha

def main():
    n = int(input('Dimensão das matrizes: '))
    mat1 = leMatriz(n)
    mat2 = leMatriz(n)
    print('Matriz 1:')
    imprimeMatriz(mat1)
    print('Matriz 2:')
    imprimeMatriz(mat2)
    print('Soma:')
    mat3Soma = somaMatriz(mat1,mat2)
    imprimeMatriz(mat3Soma)
    print('Multiplicação: ')
    mat3Multi = multiplicarMatriz(mat1,mat2)
    imprimeMatriz(mat3Multi)

main()

