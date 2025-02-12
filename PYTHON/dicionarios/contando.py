texto = input('Insira um texto: ').strip().lower()  # Evita sobrescrever str

acentos = ['!', '?', ';', ':', ' ']

for caractere in acentos:
    texto = texto.replace(caractere, '')

dicio = {letra: 0 for letra in "abcdefghijklmnopqrstuvwxyz"}

for caractere in texto:
    if caractere in dicio:
        dicio[caractere] += 1

mais_frequente = ''
anterior = 0

for chave, valor in dicio.items():
    if valor > anterior:
        mais_frequente = chave
        anterior = valor 

print('O caracter mais frequente é:')   
print(mais_frequente, anterior, sep=':')
