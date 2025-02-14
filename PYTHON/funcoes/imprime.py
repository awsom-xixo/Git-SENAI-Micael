def imprimeCaixa(num):
    tamanho = len(str(num))

    for i in range(12+tamanho):
        print('+', end='')
    print()

    print('| Número: ', num,'|')
    for i in range(12+tamanho):
        print('+', end='')
    print()

imprimeCaixa(231321)
imprimeCaixa(212321313)