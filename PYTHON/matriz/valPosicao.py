mat = []
for i in range(3): # pra cada linha de 0 a 2
    l = [] # linha começa vazia
    for j in range(4): # pra cada coluna de 0 a 3
        l.append(i*j) # preenche colunas da linha i
    mat.append(l) # adicioan a linha pra matriz
print(mat)