n = int(input('Digite um valor: '))

lista = []

for i in range(n):
    lista.append(i+1)
    print(" ".join(map(str, lista)))

# 'map()' está convertendo todos os números da lista em strings
# para que possam ser unidos pelo " ".join().