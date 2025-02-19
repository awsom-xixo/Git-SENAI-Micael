def criarLista(lista):
    for i in range(5):
        n = int(input(f'Insira um valor inteiro: ({i+1}/5): '))
        lista.append(n)

def valoresComunsDasListas(lista1, lista2):
    valoresComuns = []

    # Converte as listas para sets e encontra a interseção. 
    #Assim ele encontra os valores independente da posição
    valoresComuns = list(set(lista1) & set(lista2))

    #Desta forma não é necessário o uso de 'else', fazendo o código mais simples
    #Quando algo é vazio em python, é tratado como 'Falso', por isso o uso do 'not'
    #também poderia ser escrito como:
    #return valoresComuns if valoresComuns else 'Não tem'

    if not valoresComuns: return 'Não tem'
    return valoresComuns

lista1=[]
lista2=[]

print('Lista 1')
criarLista(lista1)
print('Lista 2')
criarLista(lista2)
print(lista1, lista2)
print(' Valores comuns das listas: ', valoresComunsDasListas(lista1, lista2))