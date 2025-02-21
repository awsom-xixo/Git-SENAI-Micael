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


dimensao = int(input('Digite a dimensão da matriz: '))
mat = leMatriz(dimensao)
imprimeMatriz(mat)